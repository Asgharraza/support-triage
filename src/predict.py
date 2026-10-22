import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
import sys
import joblib
from transformers import pipeline

# --- Load models with explicit error handling ---
try:
    classifier = pipeline(
        "text-classification",
        model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    )
except Exception as e:
    raise SystemExit(f"Failed to load Hugging Face model: {e}")

try:
    cat_model = joblib.load("models/category_model.joblib")
except FileNotFoundError:
    raise SystemExit("Missing models/category_model.joblib — run `python src/train.py` first")
except Exception as e:
    raise SystemExit(f"Failed to load category model: {e}")


def triage(text):
    # --- Input validation ---
    if not isinstance(text, str):
        return {"error": "input must be a string", "input": str(text)}
    text = text.strip()
    if not text:
        return {"error": "input is empty"}
    if len(text) < 3:
        return {"error": "input too short (min 3 chars)", "input": text}
    if len(text) > 2000:
        text = text[:2000]  # truncate very long tickets safely

    try:
        result = classifier(text)[0]
        label = result["label"]
        score = float(result["score"])
    except Exception as e:
        return {"error": f"sentiment model failed: {e}", "input": text}

    try:
        cat = cat_model.predict([text])[0]
        cat_conf = float(max(cat_model.predict_proba([text])[0]))
    except Exception as e:
        return {"error": f"category model failed: {e}", "input": text}

    urgency = "High" if label == "NEGATIVE" and score > 0.8 else "Medium" if label == "NEGATIVE" else "Low"
    needs_review = bool(score < 0.7 or cat_conf < 0.7)

    return {
        "category": cat,
        "category_confidence": round(cat_conf, 3),
        "urgency": urgency,
        "urgency_confidence": round(score, 3),
        "needs_human_review": needs_review,
    }


if __name__ == "__main__":
    text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("Enter ticket: ")
    print(triage(text))