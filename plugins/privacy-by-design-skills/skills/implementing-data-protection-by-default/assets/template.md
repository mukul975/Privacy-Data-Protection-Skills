# Data Protection by Default — Implementation Checklist

## Product Information

| Item | Value |
|------|-------|
| Product Name | Prism Analytics Platform v3.2 |
| Organization | Prism Data Systems AG |
| Assessment Date | 2026-03-14 |
| Assessor | Thomas Richter (Privacy Engineering Lead) |
| DPO Approval | Dr. Lukas Meier |

## Dimension 1: Amount (Minimum Data Collection)

| Check | Default State | Compliant | Notes |
|-------|--------------|-----------|-------|
| Registration collects only mandatory fields | email, display_name, country_code | Yes | Phone, address, company name require feature activation |
| No pre-filled optional fields | All optional fields blank | Yes | Progressive disclosure pattern |
| API rejects non-allowlisted fields | HTTP 400 for unknown fields | Yes | Gateway validation enforced |
| Mobile app: no location permission by default | Location OFF | Yes | Requested only for geo-features |
| No device fingerprinting by default | Disabled | Yes | Enabled only with analytics consent |

## Dimension 2: Extent (Minimum Processing)

| Processing Activity | Default State | Opt-In Required | Compliant |
|--------------------|---------------|-----------------|-----------|
| Core service delivery | ON | No (Art. 6(1)(b)) | Yes |
| Product analytics | OFF | Yes (consent toggle) | Yes |
| Marketing communications | OFF | Yes (separate consent) | Yes |
| Feature recommendations | OFF | Yes (preference center) | Yes |
| ML model training | OFF | Yes (explicit opt-in) | Yes |
| Third-party data sharing | OFF | Yes (per-partner consent) | Yes |
| Automated decision-making | OFF | Yes (Art. 22 consent) | Yes |

## Dimension 3: Period (Minimum Storage)

| Data Category | Default Retention | Justified | Compliant |
|--------------|------------------|-----------|-----------|
| Session tokens | Session end | Minimum possible | Yes |
| Server access logs | 90 days | Security monitoring | Yes |
| Application logs | 30 days | Debugging | Yes |
| Customer account data | Contract + 30 days | Contract necessity | Yes |
| Support tickets | 1 year post-closure | Limitation period | Yes |
| Analytics data | 13 months | Annual comparison | Yes |
| Billing records | 10 years | Swiss CO Art. 958f | Yes |
| Consent records | Consent + 5 years | Accountability | Yes |

## Dimension 4: Accessibility (Minimum Access)

| Role | Default Access | PII Visibility | Compliant |
|------|---------------|----------------|-----------|
| Support Tier 1 | Masked email, country only | Dynamic masking | Yes |
| Support Tier 2 (escalation) | Full PII (30-min timeout) | Requires ticket + approval | Yes |
| Analytics team | Pseudonymized events only | No direct identifiers | Yes |
| Engineering | No production PII | Break-glass only | Yes |
| Marketing | Aggregate statistics | No individual data | Yes |
| DPO | Full access with audit trail | Compliance investigations | Yes |

## Verification Results

| Dimension | Checks | Compliant | Rate |
|-----------|--------|-----------|------|
| Amount | 5 | 5 | 100% |
| Extent | 7 | 7 | 100% |
| Period | 8 | 8 | 100% |
| Accessibility | 6 | 6 | 100% |
| **Total** | **26** | **26** | **100%** |

## Approval

| Role | Name | Decision | Date |
|------|------|----------|------|
| Privacy Engineering Lead | Thomas Richter | Verified compliant | 2026-03-14 |
| Data Protection Officer | Dr. Lukas Meier | Approved | 2026-03-14 |

## Next Verification

Scheduled: 2026-06-14 (quarterly) and after any UI release affecting privacy controls.
