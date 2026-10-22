# Support Ticket Triage

Classifies support emails into **Category** (Billing, Technical, Account, General)
and **Urgency** (Low, Medium, High). Low-confidence predictions are flagged for
human review.

Built across three tasks:
- **Task 1** — Problem design + TF-IDF classifier
- **Task 2** — Model integration (pre-trained DistilBERT + custom classifier)
- **Task 3** — Interactive interface, error handling, failure analysis

---

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1      
pip install -r requirements.txt