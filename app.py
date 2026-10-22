import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
from src.predict import triage

print("=== Support Ticket Triage (type 'quit' to exit) ===")
while True:
    text = input("\nTicket: ").strip()
    if text.lower() in ("quit", "exit", "q"):
        break
    result = triage(text)
    if "error" in result:
        print(f"ERROR: {result['error']}")
    else:
        print(f"Category: {result['category']} ({result['category_confidence']})")
        print(f"Urgency:  {result['urgency']} ({result['urgency_confidence']})")
        print("Flagged for human review" if result["needs_human_review"] else "High confidence")