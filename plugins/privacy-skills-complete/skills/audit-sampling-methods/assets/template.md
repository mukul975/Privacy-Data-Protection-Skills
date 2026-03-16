# Audit Sampling Design and Results Record

## Engagement Details

| Field | Value |
|-------|-------|
| Engagement | DSAR Compliance Audit — Q1 2026 |
| Auditable Entity | Data Subject Access Request Processing |
| Population | All DSARs received 1 Jan 2026 – 28 Feb 2026 |
| Population Size | 247 DSARs |
| Attribute Tested | Response provided within one month (GDPR Article 12(3)) |
| Lead Auditor | Priya Sharma |
| Date | 10 March 2026 |

## Sampling Design

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Sampling Approach | Statistical — Attribute Sampling | Large population; regulatory-facing; results must be defensible |
| Confidence Level | 95% | Critical control (DSAR response is a statutory obligation) |
| Tolerable Deviation Rate | 5% | Standard threshold for compliance testing |
| Expected Deviation Rate | 2% | Based on prior audit (Q3 2025) showing 1.8% deviation |
| Calculated Sample Size | 50 | Per attribute sampling table at 95%/5% for population of 247 |

## Stratification

| Stratum | Population | Sample | Method |
|---------|-----------|--------|--------|
| EU DSARs (GDPR) | 158 | 32 | Proportional allocation |
| UK DSARs (UK GDPR) | 62 | 13 | Proportional allocation |
| Other jurisdictions | 27 | 5 | Proportional allocation |
| **Total** | **247** | **50** | |

## Sample Selection

| Detail | Value |
|--------|-------|
| Selection Method | Simple random selection using random number generator |
| Selection Date | 4 March 2026 |
| Sample List Reference | WP-SAM-001 (attached to working papers) |
| All items accessible | Yes |

## Test Results

| Stratum | Sample | Deviations | Deviation Rate |
|---------|--------|-----------|---------------|
| EU DSARs | 32 | 4 | 12.5% |
| UK DSARs | 13 | 1 | 7.7% |
| Other | 5 | 0 | 0.0% |
| **Overall** | **50** | **5** | **10.0%** |

## Deviation Details

| Item | DSAR Ref | Stratum | Deviation | Root Cause |
|------|---------|---------|-----------|-----------|
| 1 | DSAR-2026-0034 | EU | Response at day 38 (8 days late) | Manual triage delay; no escalation |
| 2 | DSAR-2026-0089 | EU | Response at day 42 (12 days late) | Auditor absence; no deputy |
| 3 | DSAR-2026-0112 | EU | Response at day 35 (5 days late) | Cross-department data retrieval delay |
| 4 | DSAR-2026-0156 | EU | Response at day 51 (21 days late) | Complex request; extension not communicated to data subject |
| 5 | DSAR-2026-0201 | UK | Response at day 33 (3 days late) | System queue backlog |

## Evaluation

| Element | Value |
|---------|-------|
| Sample Deviation Rate | 10.0% |
| Tolerable Deviation Rate | 5.0% |
| Rate Exceeds Tolerable | Yes |
| Projected Population Deviations | 25 DSARs (10% of 247) |
| Conclusion | Material non-compliance — formal finding required |

## Conclusion

The sample deviation rate of 10.0% significantly exceeds the tolerable deviation rate of 5.0% at the 95% confidence level. The auditor concludes that the DSAR response timeliness control is not operating effectively. Root cause analysis indicates systemic issues with manual triage, absence coverage, and extension notification.

**Finding Reference**: AUDIT-2026-001 (High severity)

**Recommendation**: Implement automated deadline tracking with escalation at day 20; assign deputy responders; automate extension notification to data subjects.
