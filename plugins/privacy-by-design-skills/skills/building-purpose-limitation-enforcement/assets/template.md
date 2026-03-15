# Purpose Limitation Enforcement — Assessment Template

## Article 6(4) Compatibility Assessment Form

| Item | Value |
|------|-------|
| Assessment Reference | COMPAT-2026-0047 |
| Assessment Date | 2026-03-14 |
| Assessor | Dr. Lukas Meier, Data Protection Officer |
| Organization | Prism Data Systems AG |
| Review Date | 2027-03-14 |

## Purpose Details

| Item | Original Purpose | Proposed Purpose |
|------|-----------------|------------------|
| Purpose ID | PRP-ONBRD-001 | PRP-ANALYT-001 |
| Purpose Name | Customer onboarding | Product analytics |
| Description | Account creation and identity verification | Analyzing feature usage to improve product experience |
| Lawful Basis | Article 6(1)(b) — Contract | Article 6(1)(f) — Legitimate interest |
| Data Categories | email, display_name, country_code | pseudonymized_user_id, feature_events, session_duration |

## Factor Assessment

### Factor (a): Link Between Purposes — Article 6(4)(a)

| Item | Value |
|------|-------|
| Score | 4/5 |
| Assessment | Strong link exists. Product analytics directly informs improvements to the onboarding flow, feature prioritization, and user experience enhancements that benefit the customer. Both purposes serve the overarching goal of delivering and improving the contracted service. |

### Factor (b): Context of Collection — Article 6(4)(b)

| Item | Value |
|------|-------|
| Score | 3/5 |
| Assessment | Customers signing up for a SaaS platform have a reasonable expectation that their usage patterns may be analyzed to improve the product. However, detailed behavioral profiling (session recordings, click heatmaps) exceeds typical expectations. The proposed analytics scope is limited to aggregate feature adoption metrics and session duration, which falls within reasonable expectations. |

### Factor (c): Nature of Data — Article 6(4)(c)

| Item | Value |
|------|-------|
| Score | 5/5 |
| Assessment | No special categories of data (Article 9) or criminal conviction data (Article 10) are involved. The data categories for analytics are limited to pseudonymized user identifiers, feature interaction events, and session duration. Direct identifiers (email, display_name) are pseudonymized before entering the analytics pipeline. |

### Factor (d): Consequences — Article 6(4)(d)

| Item | Value |
|------|-------|
| Score | 4/5 |
| Assessment | Consequences are minimal. Analytics outputs are aggregated statistics used for product roadmap decisions. No individual-level automated decisions are made from analytics data. No profiling under Article 22 is performed. The only residual risk is that aggregate patterns could theoretically contribute to feature removal that affects specific user segments, which is mitigated by user feedback channels. |

### Factor (e): Safeguards — Article 6(4)(e)

| Item | Value |
|------|-------|
| Score | 4/5 |
| Assessment | Comprehensive safeguards are in place. HMAC-SHA256 pseudonymization is applied at the boundary between the transactional database and the analytics warehouse. The HMAC key is stored in an HSM managed by a separate team. Analytics team members cannot access raw identifiers. Differential privacy (epsilon = 0.3 per monthly query budget) is applied to published statistics. Access is logged and audited quarterly. |

## Scoring Summary

| Factor | Score |
|--------|-------|
| (a) Link between purposes | 4/5 |
| (b) Context of collection | 3/5 |
| (c) Nature of data | 5/5 |
| (d) Consequences | 4/5 |
| (e) Safeguards | 4/5 |
| **Total** | **20/25** |

## Decision

| Item | Value |
|------|-------|
| Result | **Compatible** |
| Decision | Approved with conditions |

## Conditions

1. Data must be pseudonymized via HMAC-SHA256 before ingestion into the analytics pipeline
2. Analytics team must not have access to the HMAC key or any mechanism to reverse pseudonymization
3. Published statistics must apply differential privacy with epsilon budget tracked per the analytics privacy budget framework
4. No individual-level decisions or profiling under Article 22 may be based on analytics data
5. Compatibility assessment must be reassessed within 12 months (by 2027-03-14)

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Data Protection Officer | Dr. Lukas Meier | Approved | 2026-03-14 |
| Analytics Team Lead | Sarah Brunner | Acknowledged conditions | 2026-03-14 |
| Engineering Lead | Thomas Richter | Confirmed safeguards in place | 2026-03-14 |
