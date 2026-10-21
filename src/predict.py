import joblib, sys

cat_model = joblib.load("models/category_model.joblib")
urg_model = joblib.load("models/urgency_model.joblib")

def triage(text):
    cat = cat_model.predict([text])[0]
    cat_conf = max(cat_model.predict_proba([text])[0])
    urg = urg_model.predict([text])[0]
    urg_conf = max(urg_model.predict_proba([text])[0])
    needs_review = bool(min(cat_conf, urg_conf) < 0.7)
    return {
        "category": cat, "category_confidence": round(float(cat_conf), 3),
        "urgency": urg, "urgency_confidence": round(float(urg_conf), 3),
        "needs_human_review": needs_review,
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = input("Enter ticket text: ")
    print(triage(text))