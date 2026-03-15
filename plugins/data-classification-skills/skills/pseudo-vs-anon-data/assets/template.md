# Anonymisation Adequacy Assessment Record

## Organisation: Vanguard Financial Services
## Assessment Reference: ANON-2026-DW-001
## Dataset: Customer Transaction Analytics Dataset (Generalised)
## Date: 2026-03-14
## Assessor: Sarah Mitchell, Senior Privacy Analyst
## Reviewer: Dr. James Whitfield, Data Protection Officer

---

## 1. Dataset Description

| Field | Detail |
|-------|--------|
| **Dataset Name** | Customer Transaction Analytics Dataset (Generalised) |
| **Source System** | Oracle Data Warehouse |
| **Original Personal Data** | Customer name, account number, transaction amount, date, merchant, location |
| **De-identification Technique** | k-anonymity (k=10) with attribute generalisation and record suppression |
| **Purpose of De-identification** | Enable sharing with external analytics vendor for market trend analysis without GDPR obligations |
| **Records** | 1,850,000 (after suppression of outlier records) |
| **Quasi-identifiers Remaining** | age_band (10-year bands), region (UK region), transaction_month, merchant_category |
| **Sensitive Attributes** | transaction_amount_band (GBP bands) |
| **Direct Identifiers** | REMOVED: customer name, account number, card number, exact location |

### De-identification Transformations Applied

| Original Field | Transformation | Result |
|---------------|---------------|--------|
| customer_name | Suppressed (removed) | — |
| account_number | Suppressed (removed) | — |
| date_of_birth | Generalised to 10-year age band | age_band (e.g., "30-39") |
| postcode | Generalised to UK region | region (e.g., "South East") |
| transaction_date | Generalised to month | transaction_month (e.g., "2025-11") |
| transaction_amount | Generalised to GBP band | transaction_amount_band (e.g., "100-500") |
| merchant_name | Generalised to MCC category | merchant_category (e.g., "Grocery") |
| card_number | Suppressed (removed) | — |
| location_gps | Suppressed (removed) | — |
| Records with unique quasi-identifier combinations (k < 10) | Suppressed (removed) | 42,000 records removed |

---

## 2. Re-identification Key Assessment

| Question | Answer |
|----------|--------|
| Was a re-identification key/mapping table created? | NO — generalisation is one-way (original values not recoverable from generalised values) |
| Does any entity hold the ability to reverse the transformation? | NO — suppressed fields are permanently deleted from this dataset; source data in Oracle DW is separate |
| Can the source data be linked back to this dataset? | Only through quasi-identifier matching, assessed in linkability test below |

**Conclusion**: No re-identification key exists. Proceed to three-criteria test.

---

## 3. WP29 Three-Criteria Test (Opinion 05/2014)

### Criterion 1: Singling Out

| Assessment Element | Finding |
|-------------------|---------|
| **Quasi-identifiers tested** | age_band, region, merchant_category, transaction_month |
| **k-anonymity achieved** | k = 10 (every combination of quasi-identifiers has at least 10 records) |
| **Records with k < 10 before suppression** | 42,000 (suppressed and removed) |
| **Minimum group size after suppression** | 10 |
| **Unique records (k = 1)** | 0 |
| **Result** | **PASS** — No individual can be singled out from the dataset |

**Reasoning**: With k = 10 across all quasi-identifier combinations, any attempt to isolate a specific individual would yield a group of at least 10 indistinguishable records. Suppression of small groups eliminates residual singling-out risk.

### Criterion 2: Linkability

| Assessment Element | Finding |
|-------------------|---------|
| **Consistent identifiers across datasets** | None — all direct identifiers removed, quasi-identifiers generalised |
| **External datasets considered** | UK electoral roll, credit reference agency data, social media, public transaction databases |
| **Linkage feasibility** | LOW — generalised age band + region + merchant category does not provide sufficient precision for cross-dataset matching |
| **Temporal linkage risk** | LOW — transaction_month granularity (not exact date) prevents temporal matching |
| **Result** | **PASS** — Cross-dataset linkage is not feasible with reasonably available means |

**Reasoning**: The generalisation of all quasi-identifiers reduces precision to a level where linkage with external datasets produces ambiguous results. Age band + UK region matches thousands of individuals in public datasets. Merchant category is not available in public datasets for specific individuals.

### Criterion 3: Inference

| Assessment Element | Finding |
|-------------------|---------|
| **Sensitive attribute tested** | transaction_amount_band |
| **l-diversity achieved** | l = 4 (every k-anonymous group has at least 4 distinct transaction amount bands) |
| **Homogeneous groups (l = 1)** | 0 |
| **t-closeness** | t = 0.18 (distribution of transaction amounts in each group is within 0.18 of overall distribution) |
| **Result** | **PASS** — Sensitive attribute values cannot be inferred for specific individuals |

**Reasoning**: With l = 4 and t-closeness of 0.18, knowing a person's age band, region, and merchant category does not enable inference of their transaction amount band. The distribution of amounts within each group is sufficiently diverse.

---

## 4. Motivated Intruder Test (ICO)

| Assessment Element | Finding |
|-------------------|---------|
| **Intruder profile** | Non-specialist with internet access, public registers, social media, general computing tools |
| **Resources available** | UK electoral roll, LinkedIn, social media, Companies House, credit reference (own data only) |
| **Estimated effort** | Would require matching generalised records to external data; imprecision of bands renders matching unreliable |
| **Could intruder identify anyone?** | NO — generalisation granularity prevents reliable matching to any individual |
| **Result** | **PASS** |

**Reasoning**: A motivated intruder knowing that a specific individual is in the dataset could determine their age band and region from public sources, but the merchant category and transaction amount bands yield groups of at least 10 individuals with diverse spending patterns. The intruder cannot determine which record belongs to the target.

---

## 5. Technology Horizon Assessment

| Factor | Assessment |
|--------|-----------|
| **Intended retention period** | 5 years (analysis project) |
| **Foreseeable technology risks** | No anticipated advances in de-anonymisation that would make generalised bands vulnerable. k = 10 provides margin against modest improvements. |
| **Quantum computing risk** | Not applicable — no cryptographic protection to break; anonymisation based on information loss, not encryption |
| **Data enrichment risk** | Medium — future public data releases could narrow the groups. Mitigated by k = 10 margin and t-closeness. |
| **Reassessment date** | 2027-03-14 (annual) |

---

## 6. Classification Decision

| Criterion | Result |
|-----------|--------|
| Re-identification key exists? | NO |
| Singling out test | PASS (k = 10) |
| Linkability test | PASS (no feasible linkage) |
| Inference test | PASS (l = 4, t = 0.18) |
| Motivated intruder test | PASS |
| Technology horizon | No foreseeable risk within 5 years |

### **CLASSIFICATION: ANONYMISED**

This dataset qualifies as anonymised data under Recital 26 GDPR. The GDPR does not apply to this dataset. It may be shared with the external analytics vendor without requiring a lawful basis, data processing agreement, or data subject rights mechanisms.

### Conditions for Maintaining Anonymised Status

1. The dataset must not be enriched with additional data that could enable re-identification
2. The dataset must not be linked with other datasets held by the recipient
3. Annual reassessment must confirm anonymisation remains adequate
4. If any condition changes, the dataset must be reclassified

---

## 7. Approvals

| Role | Name | Date | Signature |
|------|------|------|-----------|
| **Privacy Analyst** | Sarah Mitchell | 2026-03-14 | S. Mitchell |
| **Privacy Engineer** | Michael Chen | 2026-03-14 | M. Chen |
| **DPO** | Dr. James Whitfield | 2026-03-14 | J. Whitfield |

---

*Assessment conducted in accordance with WP29 Opinion 05/2014 (WP216), ICO Anonymisation Code of Practice, and Vanguard Financial Services Anonymisation Standard ANS-2025-v2.0.*
