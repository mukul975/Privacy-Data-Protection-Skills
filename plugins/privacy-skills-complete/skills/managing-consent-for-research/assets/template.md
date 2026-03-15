# Research Ethics Review — Consent Assessment

## Project Information

| Field | Value |
|-------|-------|
| **Project Title** | Impact of File Deduplication Algorithms on User Storage Efficiency |
| **Principal Investigator** | Dr. Aoife Murphy, Trinity College Dublin |
| **Co-Investigators** | James Park (CloudVault SaaS Inc.), Dr. Liam O'Brien (TCD) |
| **Ethics Reference** | CREC-2026-007 |
| **Review Date** | 2026-03-14 |
| **Data Controller** | CloudVault SaaS Inc. |
| **DPO** | Marta Kowalski |

## Broad Consent Scope Assessment

| Criterion | Assessment |
|-----------|-----------|
| Research area matches broad consent scope | YES — "cloud storage optimization" |
| Data categories within consented scope | YES — file_metadata, storage_patterns, access_frequency |
| New data categories required | NO |
| Ethical standards met | YES — CREC review completed |
| Safeguards implemented | YES — all 6 Art. 89(1) safeguards confirmed |
| **Determination** | **WITHIN SCOPE of broad consent (Recital 33)** |

## Article 89(1) Safeguard Verification

| Safeguard | Implementation | Status |
|-----------|---------------|--------|
| Pseudonymization | User IDs replaced with research pseudonyms using HMAC-SHA256 with rotating key | PASS |
| Data minimization | Only file_metadata, storage_patterns, access_frequency extracted; no file contents, names, or sharing relationships | PASS |
| Access controls | Research data in isolated environment; access limited to named researchers via SSH key authentication | PASS |
| Retention limitation | Research dataset retained for study duration (18 months) plus 5 years for reproducibility per ACM policy | PASS |
| No re-identification | k-anonymity with k=10 applied to all published statistics; quasi-identifiers suppressed | PASS |
| Audit trail | All research data access logged with researcher ID, timestamp, and query executed | PASS |

## Data Subjects

| Metric | Value |
|--------|-------|
| Users with broad research consent | 47,892 |
| Users selected for this study | 15,000 (random stratified sample) |
| Selection criteria | Active users with >100 files, balanced by storage tier |
| Data collection period | January 1 — December 31, 2025 |

## Ethics Committee Decision

**Decision: APPROVED WITH CONDITIONS**

**Conditions:**
1. k-anonymity threshold must be k >= 10 (not the standard k >= 5) due to the specificity of deduplication patterns that could theoretically re-identify users with unique file type distributions
2. Research results must be reviewed by DPO before submission for publication to verify no re-identification risk in published tables or figures
3. Raw pseudonymized data must be deleted within 30 days of study completion; only aggregated results may be retained long-term

## Sign-Off

| Role | Name | Date | Decision |
|------|------|------|----------|
| Ethics Committee Chair | Prof. Sarah Donnelly | 2026-03-10 | Approved with conditions |
| Principal Investigator | Dr. Aoife Murphy | 2026-03-11 | Conditions accepted |
| DPO | Marta Kowalski | 2026-03-14 | Safeguards verified |
| DPIA Reviewer | Elena Rodriguez | 2026-03-14 | Risk level: LOW |
