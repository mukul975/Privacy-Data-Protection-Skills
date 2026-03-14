---
name: assessing-marketing-analytics-privacy
description: >-
  Guides DPIA for marketing profiling, behavioural targeting, cross-device
  tracking, and advertising analytics. Covers ePrivacy Directive Art. 5(3)
  cookie consent, PECR regulations, legitimate interest balancing for
  direct marketing, and adtech processing chain assessment. Keywords:
  marketing analytics, DPIA, profiling, behavioural targeting, cross-device
  tracking, ePrivacy, PECR, adtech, legitimate interest.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-impact-assessment
  tags: "marketing-analytics, dpia, profiling, behavioural-targeting, eprivacy, adtech"
---

# Assessing Marketing Analytics Privacy

## Overview

Marketing analytics processing — including customer profiling, behavioural targeting, cross-device tracking, programmatic advertising, and conversion attribution — triggers multiple DPIA criteria under WP248rev.01: evaluation/scoring (C1), systematic monitoring (C3), matching or combining datasets (C6), and potentially innovative technology (C8). This skill provides a DPIA methodology for marketing analytics processing, integrating GDPR obligations with ePrivacy Directive requirements for cookie-based tracking and PECR compliance for UK-based operations.

## Legal Framework

### GDPR Provisions for Marketing Analytics
- **Art. 5(1)(b) Purpose limitation**: Marketing data collected for one purpose cannot be repurposed for incompatible marketing without further lawful basis.
- **Art. 6(1)(a) Consent**: Required for most marketing profiling; must be freely given, specific, informed, and unambiguous.
- **Art. 6(1)(f) Legitimate interest**: May apply to direct marketing to existing customers (Recital 47) but requires balancing test for profiling.
- **Art. 21(2)-(3) Right to object**: Data subjects have an absolute right to object to processing for direct marketing purposes, including profiling related to direct marketing.
- **Art. 22 Automated decision-making**: Profiling that produces legal or similarly significant effects requires Art. 22(2) exception and Art. 22(3) safeguards.

### ePrivacy Directive (2002/58/EC) Art. 5(3)
Storing or accessing information on a user's terminal equipment (cookies, device fingerprinting, local storage) requires:
- Clear and comprehensive information about the purposes
- Consent of the user (interpreted per GDPR standard: freely given, specific, informed, unambiguous)
- Exception: strictly necessary cookies for the service explicitly requested by the user

### PECR (UK Privacy and Electronic Communications Regulations 2003)
- Regulation 6: Cookie consent requirements (mirrors ePrivacy Art. 5(3)).
- Regulation 22: Unsolicited marketing communications require prior consent (opt-in) with exception for existing customer soft opt-in.
- ICO enforcement powers under Regulation 31.

## Marketing Processing Types and Risk Assessment

### Customer Profiling

| Aspect | Assessment |
|--------|-----------|
| Description | Aggregating customer data to create profiles for segmentation and targeting |
| WP248 criteria | C1 (evaluation/scoring), C6 (matching datasets) |
| Lawful basis | Consent (Art. 6(1)(a)) for new prospects; legitimate interest (Art. 6(1)(f)) for existing customers with LIA |
| Key risks | Discriminatory profiling, unexpected inferences, purpose creep |
| Mitigation | Transparency about profiling logic; opt-out mechanism; regular profiling accuracy review |

### Behavioural Targeting

| Aspect | Assessment |
|--------|-----------|
| Description | Tracking online behaviour to serve targeted advertisements |
| WP248 criteria | C1 (scoring), C3 (systematic monitoring), C6 (matching), C8 (innovative tech) |
| Lawful basis | Consent required (ePrivacy Art. 5(3) for cookies + GDPR Art. 6(1)(a) for processing) |
| Key risks | Pervasive tracking, opaque adtech supply chain, data leakage to multiple parties |
| Mitigation | Consent management platform; vendor due diligence; real-time bidding data minimisation |

### Cross-Device Tracking

| Aspect | Assessment |
|--------|-----------|
| Description | Linking user activity across multiple devices (desktop, mobile, tablet, smart TV) |
| WP248 criteria | C1, C3, C6, C8 |
| Lawful basis | Consent required — cross-device tracking exceeds reasonable expectations |
| Key risks | Comprehensive behavioural profiling; re-identification of pseudonymous profiles; tracking beyond user awareness |
| Mitigation | Explicit consent for cross-device linking; device-level opt-out mechanisms; limited retention |

### Conversion Attribution

| Aspect | Assessment |
|--------|-----------|
| Description | Tracking user journey from ad impression to purchase to attribute marketing ROI |
| Lawful basis | Consent for cookie-based attribution; legitimate interest may apply for first-party server-side attribution |
| Key risks | Extended tracking windows; cross-site tracking; data sharing with attribution platforms |

## DPIA Methodology for Marketing Analytics

### Phase 1: Marketing Data Flow Mapping (Week 1)
1. Inventory all marketing data sources (website analytics, CRM, email platform, social media, advertising platforms, DMP/CDP).
2. Map data flows from collection to activation (profiling, targeting, measurement).
3. Identify all third-party recipients (ad exchanges, demand-side platforms, data management platforms, social platforms).
4. Document all cookies, pixels, and tracking technologies deployed.
5. Identify cross-site and cross-device tracking mechanisms.

### Phase 2: Lawful Basis Assessment (Week 2)
1. For each marketing processing activity, determine the lawful basis:
   - Cookie-based tracking: consent required (ePrivacy Art. 5(3))
   - Profiling for targeting: consent (Art. 6(1)(a)) or legitimate interest with LIA (Art. 6(1)(f))
   - Direct marketing emails: consent (PECR Reg. 22) or soft opt-in for existing customers
2. Assess consent quality: is consent freely given, specific, informed, unambiguous, and withdrawable?
3. For legitimate interest claims, conduct and document a legitimate interest assessment (LIA).

### Phase 3: Risk Assessment (Week 3-4)
Assess marketing-specific risks:

| Risk | Description | Typical Level |
|------|-------------|--------------|
| MK-R1 | Opaque adtech supply chain — personal data shared with multiple parties without transparency | High |
| MK-R2 | Cross-site tracking building comprehensive browsing profiles beyond user expectation | High |
| MK-R3 | Discriminatory targeting — excluding or disadvantaging groups based on inferred characteristics | High |
| MK-R4 | Consent fatigue leading to uninformed consent | Medium |
| MK-R5 | Data leakage through real-time bidding bid requests | High |
| MK-R6 | Dark patterns in consent interfaces undermining genuine choice | High |
| MK-R7 | Children encountering targeted advertising | High |
| MK-R8 | Re-identification of pseudonymous marketing profiles | Medium |

### Phase 4: Mitigation and Approval (Week 4-5)
1. Implement technical measures: consent management platform, server-side analytics, data clean rooms, privacy sandbox APIs.
2. Implement organisational measures: marketing data governance policy, vendor due diligence, data subject rights processes.
3. DPO review and approval.
4. Schedule review: annually or upon new marketing technology deployment.

## Enforcement Precedents

- **CNIL vs Google LLC (2022)**: EUR 150 million fine for making cookie rejection more difficult than acceptance on google.fr and youtube.com — dark pattern in consent interface.
- **CNIL vs Amazon Europe (2020)**: EUR 35 million fine for placing advertising cookies without prior consent.
- **CNIL vs Criteo (2023)**: EUR 40 million fine for behavioural advertising without valid consent, insufficient transparency about profiling, and failure to demonstrate consent had been obtained.
- **Belgian DPA vs IAB Europe (2022)**: EUR 250,000 fine — Transparency and Consent Framework (TCF) consent string constitutes personal data; IAB Europe is a joint controller for TCF processing.
- **Norwegian DPA vs Grindr (2021)**: NOK 65 million fine for sharing location and sexual orientation data with advertising technology partners without valid consent.
- **AEPD vs CaixaBank (2020)**: EUR 6 million fine for commercial profiling without adequate consent management and insufficient transparency about profiling purposes.
- **ICO vs TikTok (2023)**: GBP 12.7 million fine for processing children's data for targeted advertising without appropriate age verification and parental consent.
