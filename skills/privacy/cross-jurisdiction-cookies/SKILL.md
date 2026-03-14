---
name: cross-jurisdiction-cookies
description: >-
  Implementing cookie compliance across multiple jurisdictions including EU ePrivacy
  Directive, UK PECR, US California CCPA/CPRA opt-out model, and Brazil LGPD.
  Provides a requirements matrix and geolocation-based implementation approach.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: cookie-consent-compliance
  tags: "cross-jurisdiction, pecr, ccpa, lgpd, cookie-compliance-matrix"
---

# Cross-Jurisdiction Cookie Compliance

## Overview

Organizations operating websites accessible to users in multiple jurisdictions face divergent cookie consent requirements. The EU ePrivacy Directive mandates prior opt-in consent for non-essential cookies. The UK's Privacy and Electronic Communications Regulations (PECR) mirrors this approach post-Brexit. California's CCPA/CPRA follows an opt-out model where cookies may be set by default but users must be able to opt out of "sale" or "sharing" of personal information. Brazil's LGPD requires a legal basis for processing but does not have a specific cookie regulation equivalent to ePrivacy. This skill provides a jurisdiction-by-jurisdiction requirements matrix and a unified implementation strategy for Pinnacle E-Commerce Ltd.

## Jurisdiction Requirements Matrix

### Cookie Consent Models by Jurisdiction

| Jurisdiction | Legal Framework | Consent Model | Default State | Key Requirement |
|-------------|----------------|---------------|---------------|-----------------|
| EU (27 member states) | ePrivacy Directive 2002/58/EC + GDPR | Opt-in | All non-essential blocked | Prior informed consent; no pre-ticked boxes (Planet49) |
| France | ePrivacy + Loi Informatique et Libertés + CNIL Guidelines | Opt-in (strict) | All non-essential blocked | Equal prominence accept/reject; 6-month reconsent; 13-month cookie max |
| Germany | TTDSG (Telekommunikation-Telemedien-Datenschutz-Gesetz) + GDPR | Opt-in | All non-essential blocked | Consent required per Section 25 TTDSG; BGH Planet49 implementation |
| UK | PECR (SI 2003/2426) + UK GDPR | Opt-in | All non-essential blocked | Same as EU ePrivacy; ICO enforcement |
| California, US | CCPA/CPRA (Cal. Civ. Code §1798.100 et seq.) | Opt-out | Cookies may be set by default | "Do Not Sell or Share My Personal Information" link; honor GPC signal |
| Colorado, US | CPA (C.R.S. § 6-1-1301 et seq.) | Opt-out | Cookies may be set by default | Universal opt-out mechanism recognized |
| Connecticut, US | CTDPA (P.A. 22-15) | Opt-out | Cookies may be set by default | Honor universal opt-out signals |
| Virginia, US | VCDPA (Va. Code § 59.1-575 et seq.) | Opt-out | Cookies may be set by default | Opt-out of targeted advertising and sale |
| Brazil | LGPD (Lei 13.709/2018) | Legal basis required | Depends on legal basis claimed | Consent or legitimate interest; ANPD guidance evolving |
| Canada | PIPEDA + proposed CPPA (Bill C-27) | Implied consent (evolving) | May be set with notice | Meaningful consent; implied consent may suffice for some cookies |
| South Korea | PIPA (amended 2023) + Act on Promotion of IT Network | Opt-in for tracking | Non-essential blocked | Consent for tracking cookies; strict enforcement |
| Japan | APPI (amended 2022) + Cookie regulation (2023) | Opt-in for third-party sharing | Varies | Consent if cookie data shared with third parties |

### Detailed Requirements Comparison

| Requirement | EU ePrivacy | UK PECR | California CCPA/CPRA | Brazil LGPD |
|-------------|------------|---------|---------------------|-------------|
| Prior consent for analytics | Yes | Yes | No (opt-out model) | Depends on legal basis |
| Prior consent for advertising | Yes | Yes | No (opt-out model) | Yes (consent recommended) |
| Consent for strictly necessary | No (exempt) | No (exempt) | Not applicable | Not applicable |
| Cookie wall allowed | No | No | No (service cannot be denied) | No |
| Equal prominence accept/reject | Yes (CNIL, some DPAs) | Recommended (ICO) | N/A (opt-out model) | Not specified |
| Must honor GPC/DNT | No legal requirement (but EDPB encourages) | No legal requirement | Yes — GPC = valid opt-out | Not specified |
| Consent record required | Yes (GDPR Art. 7(1)) | Yes (UK GDPR Art. 7(1)) | No (but recommended) | Yes (LGPD Art. 8, §2) |
| Maximum cookie lifetime | 13 months (CNIL) | Not specified | Not specified | Not specified |
| Reconsent frequency | 6 months (CNIL); varies by DPA | Not specified | N/A | Not specified |
| Opt-out link required | No (but withdrawal must be easy) | No | Yes — "Do Not Sell or Share" | No |
| Privacy policy cookie section | Yes | Yes | Yes | Yes |
| Child-specific requirements | GDPR Art. 8 (age 16, or member state minimum 13) | UK GDPR Art. 8 (age 13) + Age Appropriate Design Code | CCPA under-16 opt-in required | LGPD Art. 14 (best interest of child) |

## Geolocation-Based Implementation

### Architecture for Pinnacle E-Commerce Ltd

```
User Request
    │
    ├── Determine user jurisdiction
    │   ├── Primary: IP geolocation (MaxMind GeoIP2 or similar)
    │   ├── Secondary: Accept-Language header
    │   ├── Tertiary: User account country setting
    │   └── Fallback: Most restrictive (EU opt-in)
    │
    ├── Select consent configuration
    │   ├── EU/UK → Opt-in banner (full CNIL-style for FR)
    │   ├── US-CA → Opt-out with "Do Not Sell or Share" link
    │   ├── US-CO/CT/VA → Opt-out with universal opt-out support
    │   ├── US-other → Notice-only (monitor state law developments)
    │   ├── Brazil → Consent banner (LGPD legal basis)
    │   └── Other → Apply most restrictive applicable standard
    │
    └── Load appropriate consent experience
```

### Configuration by Jurisdiction

**EU/EEA Configuration:**

| Setting | Value |
|---------|-------|
| Banner type | Opt-in with equal accept/reject |
| Default cookie state | All non-essential denied |
| Tags blocked before consent | GA4, Meta Pixel, Hotjar, Google Ads, all advertising |
| Consent storage | First-party cookie + server-side record |
| Reconsent interval | 6 months (CNIL standard; apply across EU for simplicity) |
| Cookie max lifetime | 13 months |
| GPC signal handling | Treat as opt-out of advertising/targeting |

**UK Configuration:**

| Setting | Value |
|---------|-------|
| Banner type | Opt-in with clear accept/reject |
| Default cookie state | All non-essential denied |
| Tags blocked before consent | Same as EU |
| Legal framework reference | PECR Regulation 6 |
| ICO-specific | Link to ICO cookie guidance in policy |
| Reconsent interval | 12 months (ICO does not specify; annual is prudent) |

**California Configuration:**

| Setting | Value |
|---------|-------|
| Banner type | Notice banner with opt-out link |
| Default cookie state | All cookies set by default |
| Required link | "Do Not Sell or Share My Personal Information" in footer |
| GPC signal | Must be honored as valid opt-out (Cal. Civ. Code §1798.135(e)) |
| Opt-out scope | Advertising cookies and any "sale" or "sharing" of PI |
| Financial incentive notice | Required if offering loyalty program tied to data collection |
| Under-16 users | Opt-in required (no default setting of tracking cookies) |

**Brazil Configuration:**

| Setting | Value |
|---------|-------|
| Banner type | Consent banner (opt-in recommended) |
| Default cookie state | Non-essential denied (conservative approach pending ANPD guidance) |
| Legal basis options | Consent (Art. 7, I) or Legitimate Interest (Art. 7, IX) |
| Cookie policy | Must be available in Portuguese |
| ANPD guidance | Monitor for specific cookie regulation (expected) |
| Data subject rights | Access, correction, deletion, portability per LGPD |

### Consent State Storage by Jurisdiction

| Jurisdiction | Consent Cookie Name | Content | Duration |
|-------------|-------------------|---------|----------|
| EU | pinnacle_consent_eu | `{version:"v3",analytics:false,advertising:false,functionality:false,timestamp:"2026-03-14T10:00:00Z"}` | 6 months |
| UK | pinnacle_consent_uk | `{version:"v3",analytics:false,advertising:false,functionality:false,timestamp:"2026-03-14T10:00:00Z"}` | 12 months |
| US-CA | pinnacle_consent_ccpa | `{version:"v2",optout_sale:false,optout_sharing:false,gpc:false,timestamp:"2026-03-14T10:00:00Z"}` | 12 months |
| Brazil | pinnacle_consent_lgpd | `{version:"v2",analytics:false,advertising:false,timestamp:"2026-03-14T10:00:00Z"}` | 12 months |

## Cross-Jurisdiction Cookie Policy

### Policy Structure for Pinnacle E-Commerce Ltd

The cookie policy must address all jurisdictions served:

**Section 1 — What Cookies We Use**
Universal section listing all cookies by category (same for all users).

**Section 2 — Your Rights by Location**

| If You Are Located In | Your Cookie Rights |
|-----------------------|-------------------|
| European Economic Area | You have the right to accept or reject non-essential cookies before they are set. We will not set analytics, advertising, or functionality cookies without your prior consent. |
| United Kingdom | Under the Privacy and Electronic Communications Regulations (PECR), you have the right to accept or reject non-essential cookies before they are set. |
| California, USA | You have the right to opt out of the "sale" or "sharing" of your personal information collected through cookies. Click "Do Not Sell or Share My Personal Information" to exercise this right. We honor the Global Privacy Control (GPC) signal. |
| Brazil | Under the Lei Geral de Proteção de Dados (LGPD), we process cookie data based on your consent. You may withdraw consent at any time. |
| Other US States | Depending on your state, you may have the right to opt out of targeted advertising. We honor universal opt-out mechanisms. |

**Section 3 — How to Manage Cookies**
Instructions for using the consent banner, browser settings, and GPC.

**Section 4 — Updates to This Policy**
Version history and notification process for material changes.

## Testing Cross-Jurisdiction Compliance

### Verification Matrix

| Test | EU | UK | California | Brazil |
|------|----|----|------------|--------|
| Banner appears on first visit | Opt-in banner | Opt-in banner | Notice with opt-out link | Consent banner |
| No non-essential cookies before interaction | Verify | Verify | N/A (cookies allowed) | Verify |
| Accept All sets all cookies | Verify | Verify | N/A | Verify |
| Reject All blocks non-essential | Verify | Verify | N/A | Verify |
| "Do Not Sell" link present | N/A | N/A | Verify in footer | N/A |
| GPC signal honored | Recommended | Recommended | Required — verify | Recommended |
| Consent persists across pages | Verify | Verify | Verify | Verify |
| Consent expires on schedule | 6 months | 12 months | 12 months | 12 months |
| Cookie policy accessible | Verify | Verify | Verify | Verify (Portuguese) |

## Key Legal References

- **ePrivacy Directive 2002/58/EC, Article 5(3)** — EU cookie consent requirement
- **UK PECR (SI 2003/2426), Regulation 6** — UK cookie consent requirement
- **CCPA/CPRA (Cal. Civ. Code §1798.100 et seq.)** — California opt-out model for sale/sharing
- **California AG Regulations, 11 CCR §7025** — GPC as valid opt-out mechanism
- **LGPD (Lei 13.709/2018), Articles 7-8** — Brazilian consent requirements
- **CJEU Case C-673/17 (Planet49)** — Active consent; disclosure of duration and third-party access
- **TTDSG Section 25** — German implementation of ePrivacy cookie requirements
- **CNIL Deliberation No. 2020-091** — French cookie guidelines
- **UK ICO Guidance on Cookies and Similar Technologies (2023)** — PECR compliance guidance
- **Colorado CPA Rules, 4 CCR 904-3, Rule 5.11** — Universal opt-out mechanism requirements
