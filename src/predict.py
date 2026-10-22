import sys
from transformers import pipeline

# Load the same sentiment model locally — downloaded once, then cached
classifier = pipeline(
    "text-classification",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

def triage(text):
    result = classifier(text)[0]
    label = result["label"]
    score = result["score"]
    urgency = "High" if label == "NEGATIVE" and score > 0.8 else "Medium" if label == "NEGATIVE" else "Low"
    needs_review = bool(score < 0.7)
    return {
        "urgency": urgency,
        "confidence": round(float(score), 3),
        "needs_human_review": needs_review,
        "raw_label": label,
    }

if __name__ == "__main__":
    text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("Enter ticket: ")
    print(triage(text))