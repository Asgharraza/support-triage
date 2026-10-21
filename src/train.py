import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

df = pd.read_csv("data/tickets.csv")
X = df["ticket_text"].astype(str)

def build_pipeline():
    return Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 1), max_features=2000, min_df=2)),
        ("clf", LogisticRegression(max_iter=300, C=0.5)),
    ])

def train_task(label_col, out_path):
    y = df[label_col]
    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y)
    pipe = build_pipeline()
    pipe.fit(X_tr, y_tr)
    y_pred = pipe.predict(X_te)
    print(f"\n===== {label_col} =====")
    print("Accuracy:", round(accuracy_score(y_te, y_pred), 4))
    print(classification_report(y_te, y_pred))
    print("Confusion matrix labels:", list(pipe.classes_))
    print(confusion_matrix(y_te, y_pred))
    joblib.dump(pipe, out_path)
    print("Saved", out_path)
    return y_te, y_pred

train_task("category", "models/category_model.joblib")
train_task("urgency", "models/urgency_model.joblib")