---
name: connecticut-ctdpa
description: >-
  Connecticut Data Privacy Act (CTDPA) compliance. Covers consumer rights,
  controller obligations, dark pattern prohibition, loyalty program
  exemption, universal opt-out requirement effective January 2025,
  sensitive data consent, and AG enforcement. Effective July 1, 2023.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: us-state-privacy-laws
  tags: "ctdpa, connecticut-privacy, dark-patterns, loyalty-program, universal-opt-out"
---

# Connecticut Data Privacy Act (CTDPA)

## Overview

The Connecticut Data Privacy Act (CTDPA), codified as Conn. Gen. Stat. §42-515 through §42-525, was signed into law on May 10, 2022 (SB 6), and became effective July 1, 2023. Connecticut was the fifth state to enact comprehensive consumer privacy legislation. The CTDPA is notable for its explicit prohibition on dark patterns in obtaining consent, its bona fide loyalty program exemption, and its requirement to recognize universal opt-out mechanisms (effective January 1, 2025).

## Applicability (§42-516)

The CTDPA applies to persons that conduct business in Connecticut or produce products or services targeted to Connecticut residents AND during the preceding calendar year:

1. Controlled or processed personal data of at least 100,000 Connecticut consumers (excluding data processed solely for payment transactions); OR
2. Controlled or processed personal data of at least 25,000 Connecticut consumers AND derived more than 25% of gross revenue from the sale of personal data.

**Note:** The 25% revenue threshold is lower than Virginia's 50% and mirrors no specific percentage in Colorado.

**Exemptions:** State/local government, GLBA institutions (entity-level), HIPAA covered entities/BAs (entity-level), nonprofits, higher education institutions, and data governed by certain federal statutes.

**Liberty Commerce Inc. Assessment:**
Liberty Commerce Inc. processes personal data of approximately 87,000 Connecticut consumers. With 12% advertising revenue from data sale activities, it does not meet threshold (2). However, excluding payment-only transactions, the consumer count exceeds the threshold under a conservative reading. Liberty Commerce Inc. treats itself as subject to the CTDPA.

## Consumer Rights (§42-520)

### Six Consumer Rights

1. **Right to Access** (§42-520(a)(1)): Confirm processing and access personal data
2. **Right to Correct** (§42-520(a)(2)): Correct inaccuracies
3. **Right to Delete** (§42-520(a)(3)): Delete personal data
4. **Right to Portability** (§42-520(a)(4)): Obtain data in portable, readily usable format
5. **Right to Opt Out** (§42-520(a)(5)): Opt out of:
   - Targeted advertising
   - Sale of personal data
   - Profiling in furtherance of decisions producing legal or similarly significant effects
6. **Right to Appeal** (§42-520(f)): Appeal a denial of any rights request

### Response Requirements (§42-520(b)-(e))
- Respond within 45 days of receipt
- Extension: up to 45 additional days with notice
- At least one free response per 12 months per right
- Appeal: controller must respond within 60 days

## Dark Pattern Prohibition (§42-515(8), §42-518(a)(5))

The CTDPA explicitly defines and prohibits dark patterns in the context of obtaining consumer consent. A "dark pattern" is defined as:

> "A user interface designed or manipulated with the substantial effect of subverting or impairing user autonomy, decision-making or choice, and includes, but is not limited to, any practice the Federal Trade Commission refers to as a 'dark pattern'."

### Implications

- Consent obtained through dark patterns is **not valid consent** under the CTDPA
- Applies to consent for sensitive data processing (§42-518(a)(5))
- Applies to consent for processing children's data
- Any consent mechanism that uses confusing language, hidden options, visual manipulation, or other deceptive practices is invalid

### Dark Pattern Examples (per FTC guidance and CTDPA legislative history)

| Pattern | Description | CTDPA Impact |
|---------|-------------|-------------|
| Confirm-shaming | Using guilt-inducing language for the opt-out option | Consent invalid |
| Hidden options | Making the reject/decline option visually less prominent | Consent invalid |
| Forced action | Requiring consent to access unrelated features | Consent invalid |
| Trick questions | Using double negatives or confusing language | Consent invalid |
| Misdirection | Visual design that steers users toward consent | Consent invalid |
| Nagging | Repeated prompts after consumer declines | Consent invalid |

**Liberty Commerce Inc. Implementation:**
Liberty Commerce Inc. has conducted a dark pattern audit of all consent interfaces. Consent buttons use equal visual weight (same size, same font, same color prominence). "Accept" and "Decline" options are presented side by side. Language is affirmative and clear. No confirm-shaming language is used.

## Bona Fide Loyalty Program Exemption (§42-517(c))

The CTDPA provides an exemption for bona fide loyalty, rewards, premium, discount, or club card programs. Personal data collected as part of such programs is exempt from the sale opt-out right if:

1. The program is a bona fide loyalty program (genuine value provided to the consumer)
2. The consumer voluntarily participates
3. The controller clearly discloses the data collection in the loyalty program terms
4. The data is used solely for the purpose of the loyalty program

**Liberty Commerce Inc. Implementation:**
Liberty Commerce Inc. operates the "Liberty Rewards" program. The program terms clearly state that purchase history and preference data are used exclusively for rewards calculation, personalized offers within the program, and member benefits. This data is not sold or used for cross-context behavioral advertising outside the loyalty program scope.

## Universal Opt-Out Mechanism (§42-520(a)(6))

Effective January 1, 2025, controllers must recognize universal opt-out mechanisms. Requirements parallel Colorado's framework:

- Must recognize and process universal opt-out signals (including GPC)
- Signal applies to targeted advertising and sale of personal data
- No additional consumer verification required
- No pop-up or interstitial questioning the signal
- Apply at browser/device level for unauthenticated; account level for authenticated

## Sensitive Data (§42-518(a)(5))

### Categories
Same as Virginia VCDPA:
1. Racial or ethnic origin
2. Religious beliefs
3. Mental or physical health condition or diagnosis
4. Sexual orientation
5. Citizenship or immigration status
6. Genetic or biometric data for identification
7. Personal data of a known child
8. Precise geolocation data

### Consent Requirement
Processing requires **opt-in consent** that is not obtained through a dark pattern.

## Controller Obligations (§42-518)

1. **Purpose limitation**: Limit processing to what is adequate, relevant, and reasonably necessary
2. **Data minimization**: Do not collect more than reasonably necessary
3. **Data security**: Appropriate technical and organizational measures
4. **Non-discrimination**: No processing in violation of antidiscrimination laws
5. **Sensitive data consent**: Obtain consent (not via dark pattern) before processing
6. **Privacy notice**: Reasonably accessible and clear
7. **DPIAs**: Conduct assessments for targeted advertising, sale, profiling, sensitive data, and high-risk processing

## Enforcement (§42-524, §42-525)

- **Exclusive AG enforcement** — no private right of action
- **60-day cure period** until December 31, 2024
- **After January 1, 2025**: AG has discretion on cure period
- **Penalties**: Treated as unfair trade practices under Conn. Gen. Stat. §42-110b (CUTPA)
- **Civil penalties**: Up to $5,000 per willful violation under CUTPA

## Key Regulatory References

- Conn. Gen. Stat. §42-515 through §42-525 (CTDPA)
- Conn. Gen. Stat. §42-110b (Connecticut Unfair Trade Practices Act — enforcement)
- FTC Dark Patterns Report (September 2022) — referenced in CTDPA definition
- Global Privacy Control Specification v1.0 — recognized universal opt-out mechanism
