# Support Ticket Triage — Final AI Application

A beginner-friendly AI tool that reads a customer support email and automatically
labels it with a **category** (Billing, Technical, Account, General) and an
**urgency level** (Low, Medium, High). If the model isn't confident, it flags the
ticket for human review instead of guessing.

---

## 1. The Problem

Customer support teams get hundreds of emails a day. Someone has to read each one,
decide what it's about, and figure out how urgent it is. That's slow, tiring, and
inconsistent — two agents may label the same ticket differently.

**Our goal:** automate the first pass so agents open the right ticket first. The
model proposes a category and urgency; a human always makes the final call.

**Who it helps:**
- **Support agents** — see prioritized, sorted queues instead of a raw inbox
- **Team leads** — see volume by category to plan staffing
- **Customers** — get faster, more accurate replies

---

## 2. The Method (in plain English)

Two small classifiers run side by side:

### Category classifier (custom-trained)
- Built with **TF-IDF** (turns text into word-frequency numbers) + **Logistic Regression** (a simple classifier)
- Trained on 3,000 synthetic support tickets
- Predicts: **Billing**, **Technical**, **Account**, or **General**

### Urgency signal (pre-trained model)
- Uses **DistilBERT**, a small pre-trained language model from Hugging Face
- Reads the emotional tone of the ticket: negative tone → higher urgency
- Predicts: **Low**, **Medium**, or **High**

### Human-in-the-loop safety
If either model's confidence is below **0.7**, the ticket is flagged
`needs_human_review: True`. The system never silently guesses on uncertain tickets.

**Why this design:**
- Fast (runs on a laptop CPU, no GPU, no cloud API)
- Free (no API keys, no costs)
- Interpretable (confidence scores visible for every prediction)
- Safe (uncertain predictions escalated to humans)

---

## 3. The Demo (try it yourself)

### Setup (first time only)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt