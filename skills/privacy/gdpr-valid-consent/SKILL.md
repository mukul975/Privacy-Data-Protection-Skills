---
name: gdpr-valid-consent
description: >-
  Guide for implementing GDPR-valid consent under Article 7 conditions and Article 4(11)
  definition. Covers five core requirements: freely given, specific, informed, unambiguous,
  and clear affirmative action. Includes pre-ticked boxes prohibition per Planet49 CJEU
  C-673/17, consent form audit checklist, and practical implementation patterns.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: consent-management
  tags: "gdpr-consent, article-7, valid-consent, affirmative-action, consent-audit"
---

# Implementing GDPR-Valid Consent

## Overview

Valid consent under the GDPR is defined in Article 4(11) as "any freely given, specific, informed and unambiguous indication of the data subject's wishes by which he or she, by a statement or by a clear affirmative action, signifies agreement to the processing of personal data relating to him or her." Article 7 sets out the conditions for consent, and Recital 32 clarifies that silence, pre-ticked boxes, or inactivity do not constitute consent.

The Court of Justice of the European Union (CJEU) reinforced this in Case C-673/17 (Planet49 GmbH, October 1, 2019), ruling that pre-ticked checkboxes do not constitute valid consent for placing cookies, and that consent must be specific to each processing purpose.

## The Five Requirements of Valid Consent

### 1. Freely Given (Article 7(4), Recitals 42-43)

Consent is not freely given if:

- There is a clear imbalance between the data subject and the controller (e.g., employer-employee relationships, public authority-citizen relationships)
- Consent is bundled as a non-negotiable condition of a service (the "conditionality test" under Article 7(4))
- The data subject suffers detriment for refusing or withdrawing consent
- There is no genuine choice or the individual feels compelled to consent

**CloudVault SaaS Inc. Implementation:**
CloudVault SaaS Inc. separates consent for core cloud storage services from consent for analytics and marketing. Users who decline marketing consent retain full access to storage functionality. The sign-up flow explicitly states: "Declining optional data processing will not affect your access to CloudVault storage services."

### 2. Specific (Article 6(1)(a), Recital 32)

Consent must be:

- Granular: separate consent for each distinct purpose
- Named: the controller and any third-party controllers must be specifically identified
- Purpose-limited: clearly linked to a defined processing purpose

**CloudVault SaaS Inc. Implementation:**
CloudVault SaaS Inc. presents three separate consent requests during onboarding:
- "Allow CloudVault SaaS Inc. to analyze your file usage patterns to recommend storage optimization" (Purpose: Service improvement)
- "Allow CloudVault SaaS Inc. to send you product update emails" (Purpose: Direct marketing)
- "Allow CloudVault SaaS Inc. to share anonymized usage statistics with Datalytics Partners Ltd. for industry benchmarking" (Purpose: Third-party analytics)

### 3. Informed (Article 13, Recitals 42, 60)

Before consenting, the data subject must be told at minimum:

- The identity of the controller (CloudVault SaaS Inc., registered at 42 Innovation Drive, Dublin, D02 YX88, Ireland)
- The purpose of each processing operation for which consent is sought
- The type of data collected
- The right to withdraw consent at any time
- Information about automated decision-making, including profiling (Article 22(2)(c))
- Risks of data transfers to third countries without an adequacy decision or appropriate safeguards (relevant if Article 49(1)(a) explicit consent applies)

**CloudVault SaaS Inc. Implementation:**
Each consent request includes a layered notice: a short-form summary visible immediately and a "Learn More" expandable section with full Article 13 information. The language is plain English at a Flesch-Kincaid grade level of 8 or below.

### 4. Unambiguous Indication

The data subject's intention must be clear. According to Recital 32:

- Consent requires a clear affirmative act
- Silence, pre-ticked boxes, or inactivity do not constitute consent (confirmed in CJEU C-673/17 Planet49)
- Scrolling or continued browsing of a website does not meet this standard (EDPB Guidelines 05/2020, paragraph 86)

**CloudVault SaaS Inc. Implementation:**
CloudVault SaaS Inc. uses unticked checkboxes for each consent purpose. The "Create Account" button is active regardless of consent choices. No default-on toggles are used. The UI state is logged to demonstrate that the user actively engaged each toggle.

### 5. Clear Affirmative Action (Article 4(11), Recital 32)

Acceptable forms of affirmative action include:

- Ticking an unticked checkbox
- Choosing technical settings on an information society service
- Typing a consent statement
- Signing a written declaration (including electronic signatures under eIDAS Regulation (EU) No 910/2014)

**CloudVault SaaS Inc. Implementation:**
CloudVault SaaS Inc. records the specific UI interaction (checkbox tick, toggle switch activation) along with a timestamp, the user's session ID, the IP address, the version of the consent text displayed, and the user agent string.

## Consent Form Audit Checklist

| # | Audit Item | GDPR Reference | Pass/Fail Criteria |
|---|-----------|----------------|-------------------|
| 1 | Consent is separated from terms of service | Art. 7(2) | Consent request is clearly distinguishable from other matters |
| 2 | No pre-ticked boxes or default-on toggles | Art. 4(11), Recital 32, CJEU C-673/17 | All consent mechanisms start in the "off" state |
| 3 | Granular consent per purpose | Recital 32, EDPB Guidelines 05/2020 | Separate opt-in for each distinct processing purpose |
| 4 | Controller identity stated | Art. 7(2), Art. 13(1)(a) | Full legal name and contact details of data controller visible |
| 5 | Purpose clearly described | Art. 13(1)(c) | Each purpose described in plain language without legal jargon |
| 6 | Data types specified | Art. 13(1)(d) | Categories of personal data listed for each purpose |
| 7 | Third-party recipients named | Art. 13(1)(e) | Specific third parties (not categories) identified by name |
| 8 | Withdrawal mechanism explained | Art. 7(3) | Clear statement that consent can be withdrawn at any time with instructions |
| 9 | No detriment for refusal | Art. 7(4), Recital 42 | Service access not conditional on optional consent |
| 10 | Withdrawal as easy as giving | Art. 7(3) | Withdrawal requires equal or fewer steps than initial consent |
| 11 | Age verification present | Art. 8 | Age gate or verification for services directed at children |
| 12 | Language is plain and clear | Art. 7(2), Recital 42 | Flesch-Kincaid grade level 8 or below, no legal jargon |
| 13 | Consent records stored | Art. 7(1) | Timestamp, version, purpose, mechanism, identity recorded |
| 14 | Re-consent mechanism for purpose changes | Art. 13(3) | Process exists to obtain fresh consent when purposes change |
| 15 | No cookie walls blocking access | EDPB Guidelines 05/2020 para 39 | Content accessible regardless of cookie consent choices |

## Implementation Workflow

1. **Map Processing Activities** — Identify every processing activity that relies on consent as its lawful basis under Article 6(1)(a). Document the purpose, data categories, recipients, and retention period for each.

2. **Design Consent Mechanism** — Create granular, unticked consent controls. Ensure the UI clearly separates each purpose. Follow EDPB Guidelines 05/2020 on consent.

3. **Draft Consent Language** — Write concise, plain-language descriptions for each purpose. Include all Article 13 information in a layered format. Test readability at Flesch-Kincaid grade level 8 or below.

4. **Implement Record-Keeping** — Build a consent receipt system that captures: timestamp (ISO 8601), consent version hash, purpose identifier, mechanism type (checkbox/toggle/signature), data subject identifier, and the exact text presented.

5. **Build Withdrawal Mechanism** — Implement one-click withdrawal accessible from the user's account dashboard. Ensure withdrawal triggers downstream processing cessation within 24 hours.

6. **Run Audit** — Use the checklist above to audit the consent implementation. Document findings and remediation actions.

7. **Schedule Re-Audit** — Set a recurring audit cadence (quarterly recommended) and after any UI changes that affect consent flows.

## Key Regulatory References

- GDPR Article 4(11) — Definition of consent
- GDPR Article 6(1)(a) — Consent as lawful basis
- GDPR Article 7 — Conditions for consent
- GDPR Article 8 — Conditions applicable to child's consent
- GDPR Recitals 32, 33, 42, 43 — Guidance on consent requirements
- CJEU Case C-673/17 (Planet49 GmbH) — Pre-ticked boxes ruling
- EDPB Guidelines 05/2020 on consent under Regulation 2016/679
- eIDAS Regulation (EU) No 910/2014 — Electronic signatures for consent
