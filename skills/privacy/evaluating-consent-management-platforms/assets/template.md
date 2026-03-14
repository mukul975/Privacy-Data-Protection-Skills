# CMP Vendor Evaluation Report

## Evaluation Information

| Field | Value |
|-------|-------|
| **Organization** | CloudVault SaaS Inc. |
| **Evaluation Date** | 2026-03-14 |
| **Lead Evaluator** | Marta Kowalski, DPO |
| **Technical Evaluator** | James Park, Engineering Lead |
| **Vendors Evaluated** | OneTrust, Usercentrics, Cookiebot, Didomi, Quantcast Choice |
| **Evaluation Period** | February 1 — March 14, 2026 |

## Requirements Summary

**Mandatory Requirements:**
- TCF v2.2 certification (EU advertising ecosystem participation)
- GPC signal detection (US consumers in CA, CO, CT, MT, TX, OR)
- Mobile SDKs for iOS and Android (CloudVault mobile app)
- EU data hosting (data residency policy)
- REST API for server-side consent queries

**Desirable Requirements:**
- Built-in A/B testing (within CNIL compliance boundaries)
- LGPD support (future Brazil expansion)
- Anomaly alerting for consent rate monitoring

## Scoring Summary

| Vendor | Regulatory (30%) | Technical (25%) | Records (20%) | Reporting (15%) | Vendor (10%) | **Total** |
|--------|-----------------|-----------------|---------------|-----------------|-------------|-----------|
| OneTrust | 2.90 | 2.25 | 1.77 | 1.26 | 0.90 | **9.08** |
| Usercentrics | 2.77 | 2.30 | 1.73 | 1.20 | 0.90 | **8.90** |
| Didomi | 2.70 | 2.15 | 1.67 | 1.15 | 0.85 | **8.52** |
| Cookiebot | 2.55 | 1.85 | 1.37 | 0.78 | 0.90 | **7.45** |
| Quantcast | 2.40 | 1.70 | 1.23 | 0.65 | 0.85 | **6.83** |

## Mandatory Requirement Check

| Vendor | TCF v2.2 | GPC | Mobile SDKs | EU Hosting | API | **All Met** |
|--------|----------|-----|-------------|-----------|-----|-------------|
| OneTrust | PASS | PASS | PASS | PASS | PASS | **Yes** |
| Usercentrics | PASS | PASS | PASS | PASS | PASS | **Yes** |
| Didomi | PASS | PASS | PASS | PASS | PASS | **Yes** |
| Cookiebot | PASS | PASS | FAIL (limited) | PASS | PASS | **No** |
| Quantcast | PASS | PASS | FAIL (limited) | PASS | PASS | **No** |

## Recommendation

**Selected Vendor: Usercentrics**

While OneTrust scored highest overall (9.08 vs 8.90), Usercentrics was selected based on:

1. **Mobile SDK Quality**: Superior iOS and Android SDKs with better documentation (critical for CloudVault mobile app, which represents 60% of user sessions)
2. **A/B Testing**: More mature built-in experimentation framework within CNIL compliance boundaries
3. **Price-Performance**: More competitive pricing for CloudVault's session volume (EUR 50/month vs EUR 300/month for comparable tier)
4. **EU Data Hosting**: Data hosted in Munich, Germany — same jurisdiction as many CloudVault enterprise customers

OneTrust remains a strong alternative if CloudVault's regulatory footprint expands significantly (100+ country support is valuable for future global expansion).

## Sign-Off

| Role | Name | Date | Decision |
|------|------|------|----------|
| DPO | Marta Kowalski | 2026-03-14 | Approve Usercentrics |
| Engineering Lead | James Park | 2026-03-14 | Approve (technical fit confirmed) |
| CFO | David Chen | 2026-03-14 | Approve (within budget) |
| Legal Counsel | Elena Rodriguez | 2026-03-14 | DPA reviewed and acceptable |
