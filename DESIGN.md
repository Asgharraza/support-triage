# Task 1: AI Problem Design

## Title
Automated Support Ticket Triage: Classifying Incoming Support Emails by Category and Urgency

## 1. Problem Statement
Customer support teams receive high volume inbound email. Manually categorizing and prioritizing is slow and inconsistent. We build a text classifier that assigns each ticket one category (Billing, Technical, Account, General) and one urgency (Low/Medium/High).

## 2. Users
- Support agents (primary): pre-sorted, prioritized tickets
- Support lead (secondary): volume dashboard
- Customers (indirect): faster responses

## 3. Data Source
CSV with ticket_text, category, urgency. 3000 rows synthetic. PII removed.

## 4. Constraints
Limited labeled data; no PII; inference under 2s on CPU; confidence scores exposed; free open-source tools only; English only v1; human-in-the-loop.

## 5. Success Criteria
- Category accuracy >= 0.85
- Urgency High recall >= 0.90
- Urgency macro-F1 >= 0.75
- Inference under 2 seconds
- Low-confidence (< 0.7) flagged for human review

## 6. Out of Scope (v1)
Auto-response generation, multi-language support, sentiment analysis.

## 7. Results & Limitations
Held-out 20 percent split: category accuracy 0.837, urgency accuracy 0.902. Technical tickets are often misclassified as Billing/Account due to overlapping vocabulary (payment errors, login errors). Urgency High recall is 0.81, below target — v2 should tune class weights. Synthetic data limitation: real tickets will be noisier; production evaluation is next step.
