import pandas as pd, joblib, os
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

os.makedirs("reports", exist_ok=True)
df = pd.read_csv("data/tickets.csv")
X = df["ticket_text"].astype(str)

for label_col, model_path in [("category", "models/category_model.joblib"),
                               ("urgency", "models/urgency_model.joblib")]:
    y = df[label_col]
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    pipe = joblib.load(model_path)
    y_pred = pipe.predict(X_te)
    labels = list(pipe.classes_)
    cm = confusion_matrix(y_te, y_pred, labels=labels)

    fig, ax = plt.subplots(figsize=(5, 4))
    ax.imshow(cm, cmap="Blues")
    ax.set_xticks(range(len(labels))); ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.set_yticks(range(len(labels))); ax.set_yticklabels(labels)
    ax.set_xlabel("Predicted"); ax.set_ylabel("Actual"); ax.set_title(f"{label_col} confusion matrix")
    for i in range(len(labels)):
        for j in range(len(labels)):
            ax.text(j, i, cm[i, j], ha="center", va="center")
    plt.tight_layout(); plt.savefig(f"reports/{label_col}_cm.png"); plt.close()

    with open(f"reports/{label_col}_report.txt", "w") as f:
        f.write(classification_report(y_te, y_pred))
    print("Wrote reports for", label_col)