import pandas as pd
import random

random.seed(42)

# Every pool below deliberately shares vocabulary with at least one other pool.
# "Payment", "error", "account", "update", "profile", "sync", "support" appear in
# multiple categories, so TF-IDF keyword matching cannot reach 100%.
billing = [
    "I was charged twice for the same order",
    "My payment failed but the money was deducted",
    "The invoice amount on my account page is wrong",
    "I need an update on my refund status",
    "Why is my subscription price different from the plan page",
    "Please update my payment method in the account settings",
    "My card was declined but I see an error and a charge",
    "I can't access my invoice after the recent update",
    "Refund still pending, please advise",
    "The billing page shows an error when I try to pay",
    "Duplicate charge on my card this month",
    "Can you resend the receipt to my account email",
]
technical = [
    "The app shows an error when I try to pay",
    "My payment failed with a gateway error",
    "The invoice page won't load, just a blank screen",
    "Uploading a file crashes the app with an error",
    "Login page fails with a server error",
    "Sync between my account and the app is broken",
    "My profile photo won't update, the save button errors",
    "Video playback buffers constantly on the web player",
    "The subscription page times out when I open it",
    "Refund flow throws an error at the last step",
    "I can't access the billing settings, page fails",
    "The dashboard is down and shows a blank page",
]
account = [
    "I need to update my password",
    "My login email change isn't saving",
    "I can't access my account after the update",
    "The password reset link shows an error",
    "Please update my profile details on file",
    "My account is locked and the unlock page fails",
    "Two-factor code isn't arriving, please advise",
    "I want to change the email tied to my account",
    "My profile won't sync between devices",
    "The account settings page shows a blank screen",
    "I need an update on my account deletion request",
    "Billing address update won't save on my profile",
]
general = [
    "What are your support hours and response times",
    "Do you have a mobile app and does it work offline",
    "Where is the documentation for the billing page",
    "How do I contact support for billing questions",
    "Is there a student discount on the subscription plan",
    "Can I get an invoice for tax purposes",
    "How does the refund policy work for annual plans",
    "Do you offer a free trial on the pro plan",
    "Is the mobile app available for iOS and Android",
    "Where can I read the update notes for the latest release",
    "What's the difference between the plans on the pricing page",
    "How do I reach the support team by phone",
]

confusable = [
    ("Billing", "My payment failed and the app shows an error"),
    ("Technical", "My payment failed and the app shows an error"),
    ("Billing", "The invoice page won't load"),
    ("Technical", "The invoice page won't load"),
    ("Account", "I updated my card but my account still shows old info"),
    ("Billing", "My account email is wrong and charges are going there"),
    ("Account", "The password reset link shows an error"),
    ("Technical", "The password reset link shows an error"),
    ("General", "What is your refund policy for mobile app purchases"),
    ("Billing", "Do you offer student pricing and how do I apply it"),
    ("General", "The documentation page isn't loading"),
    ("Technical", "The documentation page isn't loading"),
    ("Account", "The account settings page shows a blank screen"),
    ("Technical", "The account settings page shows a blank screen"),
    ("Billing", "The billing page shows an error when I try to pay"),
    ("Technical", "The billing page shows an error when I try to pay"),
]

pools = {"Billing": billing, "Technical": technical,
         "Account": account, "General": general}

urgent_phrases = ["urgent", "asap", "immediately", "critical",
                  "system is down", "cannot access anything", "lost data",
                  "need this fixed now", "this is blocking my work"]
medium_phrases = ["not working", "still broken", "failed again",
                  "getting an error", "issue persists", "problem continues",
                  "this keeps happening", "please look into this"]
low_phrases = ["", "", "", "when you get a chance", "no rush",
               "just curious", "quick question", "for future reference"]

prefixes = ["Hi, ", "Hello, ", "Hey team, ", "", "Good morning, ", "Thanks, "]
suffixes = ["", "", " Thanks!", " Please advise.", " Any update?"]

rows = []
for _ in range(3000):
    if random.random() < 0.40:
        cat, base = random.choice(confusable)
    else:
        cat = random.choice(list(pools.keys()))
        base = random.choice(pools[cat])

    r = random.random()
    if r < 0.20:
        text = f"{random.choice(urgent_phrases)}: {base}"
        urgency = "High"
    elif r < 0.55:
        text = f"{base} - {random.choice(medium_phrases)}"
        urgency = "Medium"
    else:
        text = base
        urgency = "Low"

    if random.random() < 0.12:
        text = f"{text} {random.choice(medium_phrases + urgent_phrases)}"

    text = random.choice(prefixes) + text.lower() + random.choice(suffixes)

    words = text.split()
    if len(words) > 4 and random.random() < 0.10:
        del words[random.randint(0, len(words) - 1)]
        text = " ".join(words)

    rows.append({"ticket_text": text.strip(), "category": cat, "urgency": urgency})

pd.DataFrame(rows).to_csv("data/tickets.csv", index=False)
print("Wrote data/tickets.csv with", len(rows), "rows")