---
name: colorado-cpa-compliance
description: >-
  Colorado Privacy Act (CPA) compliance implementation. Covers universal
  opt-out mechanism required since July 2024, profiling opt-out rights,
  sensitive data consent requirements, AG rulemaking under 4 CCR 904-3,
  and consumer rights framework. Effective July 1, 2023.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: us-state-privacy-laws
  tags: "colorado-cpa, universal-opt-out, profiling, sensitive-data, ag-rulemaking"
---

# Colorado Privacy Act (CPA) Compliance

## Overview

The Colorado Privacy Act (CPA), codified as C.R.S. §6-1-1301 through §6-1-1313, was signed into law on July 7, 2021 (SB 21-190), and became effective July 1, 2023. Colorado was the third state to enact comprehensive consumer privacy legislation. The CPA is notable for its robust rulemaking by the Colorado Attorney General, resulting in detailed implementing regulations at 4 CCR 904-3, and for being the first state (alongside Connecticut) to require recognition of universal opt-out mechanisms.

The Colorado AG published final rules effective March 1, 2024, with the universal opt-out mechanism requirement taking effect July 1, 2024.

## Applicability (§6-1-1304)

The CPA applies to controllers that conduct business in Colorado or produce products or services intentionally targeted to Colorado residents AND:

1. Control or process personal data of 100,000 or more Colorado consumers per calendar year; OR
2. Control or process personal data of 25,000 or more Colorado consumers AND derive revenue or receive a discount on the price of goods or services from the sale of personal data.

**Note:** Threshold (2) does not require a specific revenue percentage (unlike Virginia's 50% threshold).

**Exemptions (§6-1-1304(2)):**
- State and local government entities
- National securities associations registered under 15 U.S.C. §78o-3
- Financial institutions and affiliates subject to GLBA (entity-level)
- Covered entities and business associates under HIPAA (entity-level)
- Nonprofit organizations
- Institutions of higher education
- Data governed by GLBA, HIPAA, FERPA, FCRA, DPPA, COPPA, Farm Credit Act, and certain other federal statutes

**Liberty Commerce Inc. Assessment:**
Liberty Commerce Inc. processes data of approximately 98,000 Colorado consumers and derives advertising revenue from data-related activities. It meets threshold (2) and is subject to the CPA.

## Consumer Rights (§6-1-1306)

### 1. Right to Access (§6-1-1306(1)(a))
Confirm whether a controller is processing their personal data and access such data.

### 2. Right to Correct (§6-1-1306(1)(b))
Correct inaccuracies in personal data, taking into account the nature of the data and the purposes of processing.

### 3. Right to Delete (§6-1-1306(1)(c))
Delete personal data provided by or obtained about the consumer.

### 4. Right to Data Portability (§6-1-1306(1)(d))
Obtain personal data in a portable and, to the extent technically feasible, readily usable format.

### 5. Right to Opt Out (§6-1-1306(1)(e))
Opt out of processing for purposes of:
- **Targeted advertising**
- **Sale of personal data**
- **Profiling** in furtherance of decisions that produce legal or similarly significant effects

**Liberty Commerce Inc. Implementation:**
All five rights are exercisable through the privacy portal at privacy.libertycommerce.com/colorado. Opt-out rights are also accessible via universal opt-out mechanism (GPC) and a dedicated "Your Privacy Choices" link with the Colorado-approved opt-out icon.

## Universal Opt-Out Mechanism (4 CCR 904-3, Rule 5.11)

The CPA is the first state law (alongside Connecticut) to mandate that controllers recognize universal opt-out mechanisms. The requirement became effective July 1, 2024.

### Requirements

Controllers must:
1. **Recognize and process** opt-out signals sent through a universal opt-out mechanism
2. **Treat the signal** as a valid opt-out of sale of personal data and targeted advertising
3. **Not require** additional consumer verification to process the signal
4. **Not display** a pop-up, interstitial, or other mechanism asking the consumer to verify or modify the signal
5. **Apply the signal** at the browser/device level for unauthenticated consumers
6. **Apply the signal** at the account level for authenticated consumers
7. **Resolve conflicts** in favor of the most recently expressed preference

### Technical Standards (4 CCR 904-3, Rule 5.11)

The AG rules specify that a universal opt-out mechanism must:
- Be a setting or extension of a platform, technology, or mechanism
- Not be a default setting (must be affirmatively selected by the consumer)
- Clearly communicate to the consumer what the setting means
- Be consumer-friendly and easy to use
- Send a signal to the controller that clearly communicates the consumer's choice

**Global Privacy Control (GPC)** is recognized as a compliant universal opt-out mechanism.

**Liberty Commerce Inc. Implementation:**
Liberty Commerce Inc. detects GPC via the `Sec-GPC: 1` HTTP header and `navigator.globalPrivacyControl` JavaScript API. Upon detection:
- Unauthenticated: Apply session-level opt-out of targeted advertising and sale
- Authenticated: Permanently set account-level opt-out preferences
- Suppress all third-party advertising tags and data sharing for cross-context behavioral advertising
- Allow first-party analytics under processor agreement

## Sensitive Data (§6-1-1304(26), §6-1-1308(7))

### Categories
1. Personal data revealing racial or ethnic origin
2. Religious beliefs
3. Mental or physical health condition or diagnosis
4. Sex life or sexual orientation
5. Citizenship or citizenship status
6. Genetic or biometric data processed for uniquely identifying an individual
7. Personal data of a known child

### Consent Requirement
Processing of sensitive data requires the consumer's **opt-in consent**. Consent must be:
- Freely given, specific, informed, and unambiguous
- Clear affirmative act (no pre-checked boxes)
- Specific to each sensitive data category and purpose

### Profiling Opt-Out (§6-1-1306(1)(e)(III))

Consumers may opt out of profiling in furtherance of decisions that produce legal or similarly significant effects. This is broader than most state laws and includes:
- Decisions about provision or denial of financial or lending services
- Decisions about provision or denial of housing
- Decisions about provision or denial of insurance
- Decisions about provision or denial of education enrollment or opportunity
- Decisions about provision or denial of employment
- Decisions about provision or denial of health care services
- Decisions about access to basic necessities (food, water, shelter, energy, transportation)

**Liberty Commerce Inc. Implementation:**
Liberty Commerce Inc. conducts profiling for its buy-now-pay-later feature (credit scoring). Colorado consumers are provided a specific opt-out mechanism for this profiling activity, with disclosure of the logic involved, significance of the decision, and anticipated consequences.

## Controller Obligations (§6-1-1308)

### Privacy Notice (§6-1-1308(1))
Must include:
- Categories of personal data collected or processed
- Purposes for processing
- Consumer rights and how to exercise them
- Categories of personal data shared with third parties
- Categories of third parties with whom data is shared
- Contact information (email or online mechanism)
- Whether personal data is sold or used for targeted advertising
- Whether profiling is conducted and opt-out information

### Data Minimization (§6-1-1308(3))
Collection must be adequate, relevant, and limited to what is reasonably necessary in relation to the specified purposes.

### Purpose Limitation (§6-1-1308(4))
Processing may not exceed what is reasonably necessary to and compatible with the specified purposes.

### Data Security (§6-1-1308(5))
Reasonable administrative, technical, and physical security practices appropriate to the volume, scope, and nature of the data.

### Non-Discrimination (§6-1-1308(6))
May not process personal data in violation of state and federal antidiscrimination laws.

### DPIA Requirements (§6-1-1309)

Controllers must conduct DPIAs for:
- Targeted advertising processing
- Sale of personal data
- Certain types of profiling
- Sensitive data processing
- Any processing presenting heightened risk of harm

DPIAs must be made available to the AG upon request.

## Enforcement (§6-1-1311, §6-1-1312)

### Attorney General Authority
- Exclusive enforcement under the Colorado Consumer Protection Act (§6-1-101 et seq.)
- May issue civil investigative demands
- May seek injunctive relief, restitution, and civil penalties

### Cure Period
- 60-day cure period was available until January 1, 2025
- After January 1, 2025: No automatic cure period; AG has discretion to consider good-faith efforts

### Penalties
- Treated as a deceptive trade practice under §6-1-105
- Civil penalties up to $20,000 per violation (under Colorado Consumer Protection Act)
- Injunctive relief and restitution

## AG Rulemaking (4 CCR 904-3)

The Colorado AG published comprehensive regulations addressing:
- **Rule 2**: Definitions and general provisions
- **Rule 3**: Consumer rights procedures
- **Rule 4**: Controller and processor obligations
- **Rule 5**: Universal opt-out mechanism technical standards
- **Rule 6**: Consent requirements for sensitive data
- **Rule 7**: Data protection impact assessment requirements
- **Rule 8**: Biennial review of universal opt-out mechanisms

## Key Regulatory References

- C.R.S. §6-1-1301 through §6-1-1313 (Colorado Privacy Act)
- 4 CCR 904-3 (AG implementing regulations, effective March 1, 2024)
- C.R.S. §6-1-101 et seq. (Colorado Consumer Protection Act — enforcement framework)
- AG Technical Guidance on Universal Opt-Out Mechanisms (July 2024)
- Global Privacy Control Specification v1.0
