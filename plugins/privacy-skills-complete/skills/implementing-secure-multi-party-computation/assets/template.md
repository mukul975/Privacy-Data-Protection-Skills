# SMPC Deployment Assessment Template

## Computation Details

| Item | Value |
|------|-------|
| Organization | Prism Data Systems AG |
| Computation | Joint credit risk scoring across three financial institutions |
| Parties | Prism Data Systems AG (features: transaction history), Alpine Credit Union (features: credit utilization), Helvetia Insurance AG (features: claims history) |
| Assessment Date | 2026-03-14 |
| DPO Approval | Dr. Lukas Meier (Prism), Dr. Maria Steiner (Alpine), Prof. Jan Huber (Helvetia) |

## Protocol Selection

| Criterion | Assessment |
|-----------|-----------|
| Number of parties | 3 |
| Security model | Semi-honest (trusted consortium members with binding legal agreements) |
| Selected protocol | Rep3 (replicated 3-party sharing with honest majority) |
| Framework | MP-SPDZ |
| Computation type | Arithmetic circuit (logistic regression scoring) |
| Communication model | Star topology via coordinator node at Prism Data Systems AG |

## Input Specification

| Party | Input Features | Record Count | Data Sensitivity |
|-------|---------------|-------------|-----------------|
| Prism Data Systems AG | transaction_count, avg_transaction_value, account_age_months | 50,000 | Art. 6(1)(f) — financial data |
| Alpine Credit Union | credit_utilization_ratio, num_credit_lines, payment_history_score | 50,000 | Art. 6(1)(f) — financial data |
| Helvetia Insurance AG | claims_count, claims_value, coverage_duration_months | 50,000 | Art. 6(1)(f) — insurance data |

## Output Specification

| Item | Value |
|------|-------|
| Output | Credit risk score (0-100) per matched customer |
| Output recipients | All three parties receive scores for their shared customers |
| Output retention | 12 months, subject to each party's retention policy |
| Output usage | Credit decisioning at each party (separate controllers) |

## Performance Estimates

| Metric | Estimate |
|--------|----------|
| PSI (customer matching) | 45 seconds for 50,000 records per party |
| Scoring computation | 12 minutes for 50,000 matched records |
| Communication volume | 2.3 GB total across all parties |
| Memory per party | 4 GB peak |
| Total end-to-end | 15 minutes |

## Joint Controller Agreement Summary

| Clause | Details |
|--------|---------|
| Controller identification | Each party is an independent controller for their input data; joint controllers for the SMPC output |
| Purpose limitation | Output used solely for credit risk assessment; no secondary use without fresh agreement |
| Data subject rights | Each party handles DSARs for their input data; joint protocol for output-related requests |
| Security measures | Rep3 with honest majority security; mTLS communication; audit logging at each party |
| Breach notification | Coordinated notification within 24 hours; lead notifier is Prism Data Systems AG |
| Term and termination | 24-month term with annual renewal; 90-day termination notice; all shares destroyed on exit |

## DPIA Elements

| Element | Assessment |
|---------|-----------|
| Processing description | Joint credit scoring using SMPC across three financial institutions on overlapping customer base |
| Necessity | SMPC is the minimum-data approach; alternatives (data sharing, central processing) require exposing individual-level financial data |
| Risks | Protocol deviation by a party (mitigated: honest majority + legal agreement), communication interception (mitigated: mTLS), output inference of individual features (mitigated: output is aggregate score only) |
| Safeguards | Rep3 information-theoretic security, mTLS, audit logging, 12-month output retention, joint controller agreement |
| DPO opinion | Approved: SMPC provides superior privacy protection compared to traditional data-sharing approaches |

## Approval Signatures

| Party | Representative | Role | Date |
|-------|---------------|------|------|
| Prism Data Systems AG | Dr. Lukas Meier | DPO | 2026-03-14 |
| Alpine Credit Union | Dr. Maria Steiner | DPO | 2026-03-14 |
| Helvetia Insurance AG | Prof. Jan Huber | DPO | 2026-03-14 |
