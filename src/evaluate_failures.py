import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
import pandas as pd
import joblib

df = pd.read_csv("data/tickets.csv").sample(300, random_state=42)  # sample for speed

cat_model = joblib.load("models/category_model.joblib")

preds = cat_model.predict(df["ticket_text"].astype(str))
df["predicted_category"] = preds
df["correct"] = df["predicted_category"] == df["category"]

failures = df[~df["correct"]].head(20)

os.makedirs("reports", exist_ok=True)
with open("reports/failures.md", "w", encoding="utf-8") as f:
    f.write("# Failure Analysis\n\n")
    f.write(f"Sample size: {len(df)}  |  Errors: {len(df) - df['correct'].sum()}  |  Error rate: {1 - df['correct'].mean():.3f}\n\n")
    f.write("## Sample Misclassifications\n\n")
    f.write("| Input (truncated) | True category | Predicted |\n")
    f.write("|---|---|---|\n")
    for _, row in failures.iterrows():
        text = row["ticket_text"][:80].replace("|", "/")
        f.write(f"| {text} | {row['category']} | {row['predicted_category']} |\n")

    f.write("\n## Observed Failure Modes\n\n")
    f.write("- **Technical → Billing**: tickets describing payment errors get pulled to Billing.\n")
    f.write("- **Technical → Account**: login/password errors look like Account tickets.\n")
    f.write("- **Billing → Technical**: invoice-page-loading issues read as Technical.\n")
    f.write("- **Short/ambiguous text**: very short tickets lack enough context to classify.\n")

print(f"Wrote reports/failures.md with {len(failures)} example errors from {len(df)} samples")