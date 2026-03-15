# AI Training Data Card — GDPR and AI Act Compliance

## Organisation: Vanguard Financial Services
## Data Card Reference: DC-ML-2026-001
## Date: 2026-03-14
## Dataset Owner: Priya Sharma, Head of ML Engineering
## Privacy Reviewer: Dr. James Whitfield, Data Protection Officer

---

## 1. Dataset Identity

| Field | Detail |
|-------|--------|
| **Dataset Name** | Customer Churn Prediction Training Set |
| **Version** | 2.1 |
| **Creation Date** | 2026-02-15 |
| **Owner** | ML Engineering Team (Priya Sharma) |
| **Model Purpose** | Predict customer churn probability to enable proactive retention outreach |
| **AI Act Classification** | Not high-risk (internal business analytics, no legal/significant individual effects) |

## 2. Personal Data Classification

| Field | Detail |
|-------|--------|
| **Tier 1 Classification** | TRAINING_PSEUDONYMISED |
| **Direct identifiers present** | NO — customer names, emails, addresses removed |
| **Indirect identifiers present** | YES — customer_token (pseudonymised), postcode, age_band |
| **Re-identification key** | YES — token-to-customer-ID mapping held by Data Engineering team in separate encrypted database |
| **Special category data** | NO direct Art. 9 data. Postcode and credit_score identified as proxy variables. |
| **Criminal data** | NO |

### Data Elements

| Feature | Type | Classification | Notes |
|---------|------|---------------|-------|
| customer_token | VARCHAR(32) | Pseudonymised indirect identifier | Random UUID replacing customer ID |
| age_band | CATEGORY | Personal (indirect) | 10-year bands: 18-29, 30-39, etc. |
| postcode | VARCHAR(4) | Personal (indirect) + PROXY | First 3-4 characters only; proxy for ethnic origin |
| account_tenure_months | INTEGER | Personal (indirect) | Duration of customer relationship |
| transaction_count_30d | INTEGER | Personal (indirect) | Recent transaction frequency |
| avg_transaction_amount | FLOAT | Personal (indirect) | Average transaction value (GBP) |
| product_holdings | INTEGER | Personal (indirect) | Number of Vanguard products held |
| channel_preference | CATEGORY | Personal (indirect) | Online/branch/phone preference |
| complaint_flag | BOOLEAN | Personal (indirect) | Whether customer has open complaint |
| credit_score | INTEGER | Personal (indirect) + PROXY | External credit score; proxy for ethnic origin |
| churn_label | BOOLEAN | Personal (indirect) | Target variable: did customer churn within 6 months |

## 3. Data Subjects and Provenance

| Field | Detail |
|-------|--------|
| **Data subjects** | Vanguard UK retail customers |
| **Record count** | 1,500,000 |
| **Temporal coverage** | January 2023 — December 2025 |
| **Geographic scope** | United Kingdom |
| **Source systems** | Salesforce CRM (customer demographics), Oracle Data Warehouse (transaction history, product holdings) |
| **Processing chain** | CRM + DW → ETL (Azure Data Factory) → Pseudonymisation (tokenisation) → Feature engineering → Training dataset |
| **Original collection purpose** | Financial services delivery, customer relationship management |

## 4. Consent and Lawful Basis

| Field | Detail |
|-------|--------|
| **Consent scope** | Original consent covered financial services delivery; did NOT explicitly cover ML model training |
| **Purpose compatibility (Art. 6(4))** | COMPATIBLE — churn prediction directly improves the service for which data was collected. Assessment documented in PCA-ML-2026-001. |
| **Lawful basis** | Art. 6(1)(f) — Legitimate interests |
| **LIA reference** | LIA-ML-CHURN-2026-001 |
| **LIA outcome** | Processing is necessary for Vanguard's legitimate interest in customer retention. Data subjects would reasonably expect their service usage data to be analysed to improve service. Pseudonymisation and access controls provide adequate safeguards. Opt-out mechanism available. |

## 5. Bias Assessment

### Proxy Variables Identified

| Feature | Correlated Characteristic | Correlation | Mitigation |
|---------|--------------------------|------------|-----------|
| postcode | Racial/ethnic origin | 0.38 | Apply fairness constraints (equalised odds) during training; monitor disparate impact |
| credit_score | Racial/ethnic origin | 0.31 | Include credit_score in fairness constraint; consider removing from model |

### Demographic Representation

| Group | Dataset % | UK Population % | Ratio | Status |
|-------|-----------|----------------|-------|--------|
| White British | 72.0% | 81.7% | 0.88 | Adequate |
| Asian | 10.5% | 7.5% | 1.40 | Over-represented |
| Black | 5.2% | 3.3% | 1.58 | Over-represented |
| Mixed | 3.8% | 2.2% | 1.73 | Over-represented |
| Other | 8.5% | 5.3% | 1.60 | Over-represented |

Note: Dataset over-represents minority groups relative to UK census — this reflects Vanguard's customer base in London and major cities, not intentional oversampling.

### Disparate Impact Analysis (Four-Fifths Rule)

| Group | Positive Prediction Rate | Ratio to Highest | Four-Fifths Rule |
|-------|------------------------|------------------|-----------------|
| White British | 85% | 1.00 (reference) | — |
| Mixed | 82% | 0.96 | PASS |
| Asian | 78% | 0.92 | PASS |
| Other | 76% | 0.89 | PASS |
| Black | 71% | 0.84 | PASS (marginal) |

**Overall Bias Risk**: MEDIUM — proxy variables present; four-fifths rule passes but Black group is marginal at 0.84.

## 6. De-identification

| Field | Detail |
|-------|--------|
| **Technique** | Pseudonymisation — customer IDs replaced with random UUID tokens |
| **Key storage** | Separate encrypted database (Azure Key Vault), accessible only to Data Engineering lead (1 person) |
| **Anonymisation assessment** | NOT anonymised — re-identification key exists |
| **Assessment reference** | ANON-2026-ML-001 |

## 7. Retention and Access

| Field | Detail |
|-------|--------|
| **Training data retention** | Duration of model lifecycle + 1 year for audit |
| **Model weights retention** | Duration of deployment + 3 years |
| **Access controls** | ML Engineering team (5 persons) via Vanguard ML Platform; audit logging |
| **Environment** | Isolated ML training environment (Azure ML workspace) |

## 8. DPIA

| Field | Detail |
|-------|--------|
| **DPIA required?** | YES — automated processing of personal data for evaluation/profiling |
| **DPIA reference** | DPIA-ML-CHURN-2026-001 |
| **DPIA outcome** | Residual risk: MEDIUM. Mitigations: pseudonymisation, fairness constraints, human oversight, opt-out |

## 9. Limitations

- Dataset covers UK retail customers only — model must not be applied to non-UK populations
- Temporal coverage 2023-2025 — model performance may degrade if market conditions change
- Proxy variable postcode present — fairness constraints must be applied during training
- Credit score feature shows marginal disparate impact — ongoing monitoring required
- Model predicts probability only — human review required before retention actions

---

*Data card maintained per Vanguard AI Governance Policy AGP-2025-v2.0 and EU AI Act Art. 10-11 requirements.*
