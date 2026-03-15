---
name: conflicting-laws-mgmt
description: >-
  Guides managing conflicting privacy requirements across jurisdictions. Covers data
  localisation vs transfer freedom, consent standards variation, age thresholds,
  breach timelines, and resolution frameworks for incompatible obligations. Keywords:
  conflicting laws, data localisation, consent variation, age thresholds, resolution
  framework.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: global-privacy-regulations
  tags: "conflicting-laws, data-localisation, consent-variation, resolution-framework, cross-jurisdiction"
---

# Managing Conflicting Privacy Requirements

## Overview

Organisations operating across multiple jurisdictions inevitably encounter situations where privacy requirements in different countries conflict, are incompatible, or create compliance tensions. These conflicts arise because privacy laws reflect different legal traditions, cultural values, and policy priorities. A structured resolution framework enables organisations to navigate these conflicts while maintaining defensible compliance positions in all jurisdictions.

## Categories of Conflict

### Category 1: Data Localisation vs Transfer Freedom

| Conflict | Detail |
|----------|--------|
| Localisation requirement | China PIPL Art. 40 requires CIIOs to store personal information within the PRC; India RBI circular requires payment data stored in India |
| Transfer freedom | EU GDPR Art. 44-49 permits transfers with appropriate safeguards; Singapore PDPA Section 26 permits transfers with comparable protection |
| Resolution challenge | An organisation may need to store data locally while also making it available to a global headquarters |

**Resolution Framework for Zenith Global Enterprises**:

| Scenario | Approach |
|----------|---------|
| China CIIO data + EU HQ access | Store primary data in PRC; transfer processed copies via CAC-approved mechanism; maintain PRC as system of record |
| India payment data + Global Treasury | Store payment system data in India (RBI compliance); process copies transferred to Treasury with contractual safeguards |
| Cross-jurisdiction analytics | Implement federated analytics: run queries locally, aggregate results centrally; avoid moving raw personal data |

### Category 2: Consent Standards Variation

| Jurisdiction | Consent Standard |
|-------------|-----------------|
| EU (GDPR) | Freely given, specific, informed, unambiguous; not required if other lawful basis applies |
| China (PIPL) | Default basis; separate consent (单独同意) for five scenarios |
| Korea (PIPA) | Prescriptive display requirements (font size, colour); separate consent for marketing |
| Brazil (LGPD) | Standalone consent clause separate from contract terms; 10 alternative bases |
| India (DPDP) | Free, specific, informed, unconditional, unambiguous; Consent Manager integration |
| Japan (APPI) | Implied consent model for general processing; explicit for special care-required info |

**Conflict examples**:
- GDPR allows legitimate interest without consent; PIPL requires consent as default with no legitimate interest basis
- LGPD separates consent from contract clauses; some jurisdictions permit integrated consent
- Korea prescribes font size and display; other jurisdictions are principle-based

**Resolution**: Apply the most restrictive consent standard globally (separate, explicit, purpose-specific consent with clear display) as the harmonised baseline. Where a jurisdiction permits processing without consent (e.g., GDPR legitimate interest), document the jurisdiction-specific basis but maintain the consent infrastructure as a fallback.

### Category 3: Age Thresholds for Children

| Jurisdiction | Age | Implication |
|-------------|-----|-------------|
| India (DPDP) | Under 18 | All under-18 processing requires parental consent |
| Australia (2024) | Under 18 | Children's code applies |
| EU (GDPR) | Under 16 (lowerable to 13) | Parental consent for ISS |
| China (PIPL) | Under 14 | Parental consent + additional protections |
| Korea (PIPA) | Under 14 | Legal representative consent |
| Thailand (PDPA) | Under 10 | Parental consent |

**Conflict**: Different age thresholds create operational complexity for global platforms.

**Resolution**: Apply the highest global threshold (18, from India DPDP) as the harmonised standard for all markets. This ensures compliance everywhere at the cost of stricter treatment in jurisdictions with lower thresholds. Where the highest threshold creates significant business impact, implement jurisdiction-specific age logic in the consent management platform.

### Category 4: Breach Notification Timelines

| Jurisdiction | Timeline | Trigger |
|-------------|----------|---------|
| EU GDPR | 72 hours | Risk to rights and freedoms |
| Korea PIPA | 72 hours | 1,000+ individuals affected |
| India DPDP | 72 hours (draft) | Likely harm |
| Brazil LGPD | 3 business days | Relevant risk or damage |
| Singapore PDPA | 3 days after assessment (30-day assessment window) | Significant harm or 500+ individuals |
| Australia Privacy Act | As soon as practicable (30-day assessment) | Likely serious harm |
| Japan APPI | 3-5 business days (preliminary) | PPC-defined thresholds |

**Conflict**: The 72-hour clock (EU/Korea/India) conflicts with the 30-day assessment window (Singapore/Australia).

**Resolution**: Implement a two-track notification process:
1. **Global fast track**: Begin assessment immediately upon awareness; prepare notification within 72 hours for jurisdictions requiring it
2. **Assessment track**: Continue assessment for up to 30 days for jurisdictions permitting it, but issue preliminary notification at 72 hours to the fast-track jurisdictions
3. **Content**: Preliminary 72-hour notification may be updated as assessment continues

### Category 5: Legitimate Interest Availability

| Jurisdiction | Legitimate Interest Available |
|-------------|------------------------------|
| EU (GDPR) | Yes — Art. 6(1)(f) |
| UK GDPR | Yes — Art. 6(1)(f) |
| Korea (PIPA) | Yes — Art. 15(1)(6) (2023 amendment) |
| Brazil (LGPD) | Yes — Art. 7, IX |
| Thailand (PDPA) | Yes — Section 24(5) |
| China (PIPL) | No |
| India (DPDP) | No (legitimate uses under Section 7 are narrower) |
| Japan (APPI) | No (use limitation approach) |
| Singapore (PDPA) | No (consent + deemed consent model) |

**Conflict**: An organisation relying on legitimate interest in the EU cannot use the same basis in China, India, or Singapore.

**Resolution**: For processing activities that rely on legitimate interest in some jurisdictions, maintain consent collection infrastructure as a parallel mechanism. In jurisdictions without legitimate interest, obtain consent or identify an applicable alternative basis. Document both bases in the processing register with jurisdiction-specific applicability.

### Category 6: DPO Independence vs Organisational Structure

| Conflict | Detail |
|----------|--------|
| GDPR Art. 38(3) | DPO cannot be dismissed or penalised for performing duties; must report to highest management |
| National employment laws | Some jurisdictions limit the enforceability of dismissal protections for senior employees |
| Multi-jurisdiction DPO | A single global DPO may face conflicting reporting requirements across jurisdictions |

**Resolution**: Appoint regional DPOs with local employment protections consistent with national law, reporting to a global Chief Privacy Officer. Each regional DPO holds the statutory DPO role for their jurisdiction while the global CPO provides strategic coordination.

## Resolution Framework

### Decision Tree for Conflicting Requirements

```
START: Identify the conflict
  |
  ├── Can a single harmonised standard satisfy all jurisdictions?
  |     |
  |     ├── YES → Apply the most stringent standard globally
  |     |
  |     └── NO → Are the requirements truly incompatible?
  |           |
  |           ├── YES → Implement jurisdiction-specific controls
  |           |     |
  |           |     └── Document: (a) the conflict, (b) the resolution,
  |           |         (c) the risk accepted in each jurisdiction
  |           |
  |           └── NO (tension but not incompatible) → Apply layered approach:
  |                 global baseline + jurisdiction-specific supplements
  |
  └── Record the resolution in the conflict register
```

### Conflict Register Template

| Conflict ID | Category | Jurisdictions | Description | Resolution | Risk Assessment | Review Date |
|------------|----------|--------------|-------------|------------|----------------|-------------|
| CON-001 | Data localisation | China, India, EU | CIIO data must stay in PRC but EU HQ needs access | Local storage + processed copies transferred via CAC mechanism | Medium — residual risk of CAC rejection on renewal | March 2027 |
| CON-002 | Consent standards | China, EU, Korea | PIPL requires consent; GDPR permits legitimate interest | Dual-basis approach: consent in China/Korea, legitimate interest in EU | Low — consent infrastructure maintained globally | March 2027 |
| CON-003 | Children's age | India (18), EU (16), Korea (14) | Different parental consent thresholds | Global 18 threshold | Low — over-compliant in lower-threshold jurisdictions | March 2027 |
| CON-004 | Breach timeline | EU (72h), Singapore (30d assessment) | Different notification clocks | Two-track: 72h preliminary + 30d full assessment | Low — preliminary notification satisfies fast-track jurisdictions | March 2027 |

## Governance

| Element | Detail |
|---------|--------|
| Conflict register owner | Chief Privacy Officer |
| Review frequency | Semi-annually or upon law change |
| Escalation path | CPO → General Counsel → Board Privacy Committee |
| External counsel | Engaged for novel conflicts requiring jurisdiction-specific legal opinion |
| Documentation | All resolutions documented with legal analysis and risk assessment |
