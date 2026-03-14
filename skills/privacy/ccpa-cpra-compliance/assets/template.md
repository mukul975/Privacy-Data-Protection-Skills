# CCPA/CPRA Compliance Assessment Report

## Organization Information

| Field | Value |
|-------|-------|
| **Organization** | Liberty Commerce Inc. |
| **Assessment Date** | 2026-03-14 |
| **Assessor** | Sarah Mitchell, Chief Privacy Officer |
| **Scope** | E-commerce platform, mobile app, in-store kiosks |
| **Reporting Period** | January 1, 2025 — December 31, 2025 |

## Applicability Determination

| Criterion | Threshold | Liberty Commerce Inc. Value | Met? |
|-----------|-----------|----------------------------|------|
| Annual gross revenue | >$25,000,000 | $48,000,000 | YES |
| California consumers processed | ≥100,000 | 320,000 | YES |
| Revenue from sale/sharing of PI | ≥50% | 12% | NO |
| For-profit entity | Required | Yes | YES |
| Does business in California | Required | Yes | YES |

**Determination:** CCPA/CPRA applies — two of three alternative thresholds met.

## Consumer Rights Implementation Status

| Right | Section | Implemented | Method | Notes |
|-------|---------|-------------|--------|-------|
| Right to Know (categories) | §1798.110 | YES | Web portal + toll-free | Automated disclosure generation |
| Right to Know (specific pieces) | §1798.110 | YES | Web portal + toll-free | Manual review for sensitive data |
| Right to Delete | §1798.105 | YES | Web portal + toll-free | Cascading deletion to 12 service providers |
| Right to Correct | §1798.106 | YES | Self-service + web portal | Self-service for profile data; assisted for backend |
| Right to Opt-Out (sale/sharing) | §1798.120 | YES | Homepage link + GPC | GPC signal honored per §7025 |
| Right to Limit Sensitive PI | §1798.121 | YES | Homepage link | Restricts geolocation, payment processing |
| Right to Non-Discrimination | §1798.125 | YES | Policy + technical controls | No price differentiation for opt-out consumers |

## Privacy Notice Compliance

| Requirement | Section | Status | Notes |
|-------------|---------|--------|-------|
| Categories of PI collected | §1798.100(a)(1) | COMPLIANT | 11 categories documented |
| Categories of sensitive PI | §1798.100(a)(1) | COMPLIANT | 4 categories documented |
| Purposes per category | §1798.100(a)(1) | COMPLIANT | Purpose-to-category mapping table |
| Sale/sharing disclosure per category | §1798.100(a)(1) | COMPLIANT | Advertising, analytics disclosed |
| Retention periods per category | §1798.100(a)(3) | COMPLIANT | Specific periods stated |
| Sources of PI | §1798.110(c)(2) | COMPLIANT | Direct, automated, third-party |
| Third-party categories | §1798.110(c)(4) | COMPLIANT | Named categories with examples |
| Request submission methods | §1798.130(a)(1) | COMPLIANT | Web portal, email, toll-free |
| Do Not Sell or Share link | §1798.135(a)(1) | COMPLIANT | Footer of all pages |
| Limit Sensitive PI link | §1798.135(a)(2) | COMPLIANT | Adjacent to opt-out link |
| Last updated date | CPPA Regs §7011(e) | COMPLIANT | January 15, 2026 |

## Data Processing Agreements

| Recipient | Type | Agreement Status | Last Reviewed |
|-----------|------|-----------------|---------------|
| PaySecure Corp. | Service Provider | Executed | 2025-11-01 |
| SwiftShip Logistics | Service Provider | Executed | 2025-09-15 |
| DataInsight Analytics | Contractor | Executed | 2025-10-01 |
| AdReach Network | Third Party (sale) | Executed | 2025-08-20 |
| CloudStore Hosting | Service Provider | Executed | 2025-12-01 |
| CRM Solutions Inc. | Service Provider | Executed | 2025-07-15 |

## Annual Metrics (CPPA Regs §7101)

| Request Type | Received | Fulfilled (whole/part) | Denied | Median Days to Respond |
|-------------|----------|----------------------|--------|----------------------|
| Right to Know (categories) | 1,247 | 1,198 | 49 | 12 |
| Right to Know (specific) | 834 | 789 | 45 | 22 |
| Right to Delete | 2,156 | 2,089 | 67 | 18 |
| Right to Correct | 312 | 298 | 14 | 8 |
| Right to Opt-Out | 8,923 | 8,923 | 0 | 1 |
| Right to Limit Sensitive PI | 1,456 | 1,456 | 0 | 1 |
| **Total** | **14,928** | **14,753** | **175** | **12** |

## Findings and Remediation

### Finding 1: Third-Party Data Sharing Agreement Gap (SEVERITY: HIGH)

**Description:** AdReach Network sub-contracts data processing to two entities (TargetAds LLC and BidStream Corp.) not covered under the current data processing agreement. Per §1798.100(d), all downstream recipients must be contractually bound.
**Remediation:** Require AdReach Network to either (a) execute sub-processor agreements with TargetAds LLC and BidStream Corp. with CCPA-compliant terms, or (b) cease sub-contracting. Deadline: April 15, 2026.
**Owner:** Marcus Chen, Legal Counsel

### Finding 2: Deletion Verification Incomplete (SEVERITY: MEDIUM)

**Description:** Deletion confirmation from DataInsight Analytics does not include verification that backup systems have purged consumer data. §1798.105(c) requires service providers to delete PI from all systems.
**Remediation:** Update DPA with DataInsight Analytics to require backup deletion confirmation within 90 days. Implement quarterly audit of deletion confirmation receipts.
**Owner:** Priya Sharma, Privacy Operations Manager
**Deadline:** May 1, 2026

## Sign-Off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| CPO | Sarah Mitchell | 2026-03-14 | [Signed] |
| Legal Counsel | Marcus Chen | 2026-03-14 | [Signed] |
| CTO | David Park | 2026-03-14 | [Pending] |

## Next Assessment

**Scheduled Date:** 2026-09-14 (Semi-annual cadence)
**Trigger Conditions:** Material change in data practices, new enforcement action, CPPA regulation update.
