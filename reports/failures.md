# Failure Analysis

Sample size: 300  |  Errors: 36  |  Error rate: 0.120

## Sample Misclassifications

| Input (truncated) | True category | Predicted |
|---|---|---|
| my payment failed and the app shows an error - not working Please advise. | Billing | Technical |
| Good morning, the documentation page isn't loading - please look into this Pleas | General | Technical |
| the password reset link shows an error problem continues Please advise. | Technical | Account |
| Hello, the account settings page shows a blank screen | Technical | Account |
| Hey team, my payment failed and the app shows an error Any update? | Billing | Technical |
| Good morning, the documentation page isn't loading - not working Please advise. | General | Technical |
| the password reset link shows an error Thanks! | Technical | Account |
| Hello, the invoice page won't load - still broken | Billing | Technical |
| Good morning, the documentation page isn't loading Thanks! | Technical | General |
| immediately: the password reset link shows an error | Account | Technical |
| Hey team, the password reset link shows an error - please look into this Please  | Technical | Account |
| Hi, asap: the account settings page shows a blank screen | Technical | Account |
| Good morning, the password reset link shows an error - this keeps happening | Technical | Account |
| Thanks, asap: the billing page shows an error when i try to pay Thanks! | Billing | Technical |
| Hello, the password reset link shows an error Please advise. | Technical | Account |
| Thanks, my payment failed and the app shows an error Thanks! | Billing | Technical |
| Hi, the password reset link shows an error - issue persists | Account | Technical |
| need this fixed now: the password reset link shows an error Any update? | Technical | Account |
| Hello, my payment failed and the app shows an error - failed again | Billing | Technical |
| Thanks, my payment failed and the app shows an error | Billing | Technical |

## Observed Failure Modes

- **Technical → Billing**: tickets describing payment errors get pulled to Billing.
- **Technical → Account**: login/password errors look like Account tickets.
- **Billing → Technical**: invoice-page-loading issues read as Technical.
- **Short/ambiguous text**: very short tickets lack enough context to classify.
