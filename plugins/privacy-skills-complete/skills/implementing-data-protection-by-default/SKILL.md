---
name: implementing-data-protection-by-default
description: >-
  Technical implementation of GDPR Article 25(2) data protection by default. Covers
  strictest privacy settings as default configuration, minimum data collection,
  limited storage duration, restricted accessibility, and opt-in rather than opt-out
  patterns. Includes implementation checklist and system design requirements.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-by-design
  tags: "data-protection-by-default, article-25, privacy-defaults, opt-in, minimum-collection"
---

# Implementing Data Protection by Default

## Overview

GDPR Article 25(2) requires that controllers implement appropriate technical and organisational measures for ensuring that, by default, only personal data which are necessary for each specific purpose of the processing are processed. This obligation applies across four dimensions:

1. **Amount** of personal data collected
2. **Extent** of processing performed
3. **Period** of storage
4. **Accessibility** of personal data

The EDPB Guidelines 4/2019 on Article 25 clarify that "by default" means the strictest privacy settings apply automatically, without requiring any action from the data subject. The data subject should not need to take action to protect their privacy — the system does it for them.

## The Four Dimensions of By-Default Protection

### Dimension 1: Minimum Data Collection (Amount)

**Principle:** By default, collect only the data fields strictly necessary for the core service purpose. Additional data collection requires explicit opt-in.

| Default State | Opt-In State | Example |
|--------------|-------------|---------|
| Core fields only | Extended profile | Account creation collects email + display_name only; phone, address, photo collected only if user activates billing or delivery features |
| No location data | Location-enabled features | Mobile app does not request location permission by default; only requests when user activates location-dependent feature |
| No behavioral tracking | Analytics opt-in | Website loads without analytics cookies; tracking begins only after user grants consent in cookie banner |
| Minimal form fields | Progressive disclosure | Registration form shows 3 required fields; optional fields appear only when user clicks "Add more information" |

**Prism Data Systems AG Implementation:**
The default customer registration at Prism Data Systems AG collects exactly three fields: `email`, `display_name`, and `country_code`. The country code is needed for regulatory compliance (determining applicable data protection law). All other fields (phone number, billing address, company name, job title) are collected only when the user activates a feature that requires them (billing module, enterprise integration, support escalation).

### Dimension 2: Minimum Processing (Extent)

**Principle:** By default, process data only for the primary purpose. Secondary processing (analytics, profiling, marketing) requires explicit opt-in.

| Processing Activity | Default State | Opt-In Required |
|--------------------|---------------|-----------------|
| Core service delivery | Active (Art. 6(1)(b)) | No |
| Product analytics | Disabled | Yes — consent toggle in preference center |
| Marketing communications | Disabled | Yes — separate consent at registration |
| Profiling for recommendations | Disabled | Yes — explicit opt-in with explanation |
| Third-party data sharing | Disabled | Yes — named third party + purpose |
| Automated decision-making | Disabled | Yes — Art. 22 explicit consent |

**Prism Data Systems AG Implementation:**
New customer accounts at Prism Data Systems AG have all optional processing activities disabled by default. The account dashboard shows five processing toggles, all set to OFF:
- Product analytics: OFF
- Marketing emails: OFF
- Feature recommendations: OFF
- Usage data for ML training: OFF
- Anonymous benchmarking contributions: OFF

### Dimension 3: Minimum Storage (Period)

**Principle:** By default, apply the shortest defensible retention period. Longer retention requires justification tied to a specific legal obligation.

| Data Category | Default Retention | Extended Retention (Justified) |
|--------------|------------------|-------------------------------|
| Session data | Deleted at session end | Not applicable |
| Server logs | 90 days | 12 months (security investigation) |
| Customer account data | Account duration + 30 days | + statutory period (tax: 10 years for billing) |
| Support tickets | 1 year after closure | 3 years (limitation period) |
| Marketing consent records | Consent duration + 3 years | + 5 years (accountability, Art. 7(1)) |
| Analytics data | 13 months | Not applicable (maximum) |

**Prism Data Systems AG Implementation:**
The retention policy engine at Prism Data Systems AG applies the shortest retention period by default for each data category. Extended retention is applied only for data categories with documented statutory requirements (tax records: 10 years per Swiss CO Art. 958f). All other data follows the purpose-based minimum retention.

### Dimension 4: Minimum Accessibility

**Principle:** By default, restrict access to personal data to the minimum set of roles necessary. Broader access requires explicit authorization.

| Role | Default Access | Elevated Access (Requires Justification) |
|------|---------------|----------------------------------------|
| Customer support (Tier 1) | Masked PII only (m***@domain.ch) | Unmasked PII (30-min timeout, ticket reference required) |
| Analytics team | Pseudonymized data only | No access to direct identifiers |
| Engineering team | No production PII access | Break-glass access (dual approval, logged, time-limited) |
| Marketing team | Aggregate statistics only | No individual-level data access |
| DPO | Full access for compliance investigations | Standing access with audit trail |
| External auditor | Anonymized samples | Purpose-limited access with NDA |

**Prism Data Systems AG Implementation:**
All new employee accounts at Prism Data Systems AG are provisioned with zero personal data access by default. Access is granted per-purpose through an access request workflow requiring manager approval and DPO notification. Access grants expire after 90 days and must be renewed. The Tier 1 support dashboard displays dynamically masked data by default.

## Technical Implementation Checklist

### User Interface Defaults

- [ ] All consent toggles default to OFF (unticked)
- [ ] Privacy settings page accessible from main navigation
- [ ] No pre-selected optional data collection
- [ ] No dark patterns (no misleading button labels, no visual emphasis on "Accept All")
- [ ] Cookie banner defaults to "Reject All" with equal visual prominence to "Accept All"
- [ ] Registration form shows only mandatory fields by default
- [ ] Notification preferences default to minimum (transactional only)
- [ ] Profile visibility defaults to private (not public)
- [ ] Data sharing toggles default to OFF for each third party
- [ ] Search engine indexing of profiles defaults to OFF

### Backend Defaults

- [ ] API endpoints reject non-allowlisted fields (return 400 for unexpected fields)
- [ ] New database tables include TTL metadata columns by default
- [ ] Default retention period applied automatically unless longer period is explicitly configured
- [ ] Pseudonymization applied at analytics ingestion boundary by default
- [ ] Field-level encryption enabled for all PII columns by default
- [ ] Dynamic masking rules applied to all support and operations dashboards
- [ ] Audit logging enabled for all personal data access by default
- [ ] Minimum group size (11) enforced on all analytics outputs
- [ ] Cross-purpose data access blocked by default (requires compatibility assessment)
- [ ] New service deployments fail privacy gate if data minimization assessment is not completed

### Access Control Defaults

- [ ] New employee accounts provisioned with zero personal data access
- [ ] Access grants expire after 90 days by default
- [ ] Elevated access requires documented justification and approval
- [ ] Break-glass access logged and reviewed within 24 hours
- [ ] Third-party access disabled by default until DPA is executed
- [ ] API keys scoped to minimum required data categories

### Communication Defaults

- [ ] Marketing communications disabled for all new accounts
- [ ] Transactional emails only (account confirmations, security alerts)
- [ ] Push notifications limited to security alerts by default
- [ ] Newsletter subscription requires separate opt-in
- [ ] Partner communications disabled by default

## By-Default Verification Process

1. **New account audit** — Create a test account through the standard registration flow. Verify that no optional processing is active, no marketing communications are scheduled, and the minimum data fields are collected.

2. **Dashboard inspection** — Log in as a Tier 1 support agent. Verify that all PII is masked by default and that unmasking requires explicit action with justification.

3. **API testing** — Send API requests with additional fields beyond the allowlist. Verify that extra fields are rejected (HTTP 400).

4. **Retention verification** — Check that newly created records have TTL metadata set according to the minimum retention period.

5. **Analytics output** — Run a standard analytics query. Verify that results are pseudonymized, minimum group size is enforced, and differential privacy noise is applied.

## Key Regulatory References

- GDPR Article 25(2) — Data protection by default
- GDPR Article 25(1) — Data protection by design
- GDPR Recital 78 — Technical measures for data protection by default
- EDPB Guidelines 4/2019 on Article 25, Section 3: Data Protection by Default
- CJEU C-673/17 (Planet49) — Pre-ticked boxes do not constitute consent
- EDPB Guidelines 05/2020 on consent — Consent must be freely given, not default
