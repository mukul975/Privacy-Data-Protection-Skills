---
name: pia-threshold-screening
description: >-
  Conducts pre-DPIA threshold screening to determine whether a full Data
  Protection Impact Assessment is required under GDPR Article 35. Applies
  the EDPB WP248rev.01 nine-criteria test, national supervisory authority
  blacklists, and organisational risk appetite to produce a documented
  screening decision. Keywords: threshold screening, DPIA trigger, pre-DPIA,
  WP248, Article 35(1), blacklist, screening decision.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-impact-assessment
  tags: "threshold-screening, dpia-trigger, pre-dpia, wp248, article-35, blacklist"
---

# PIA Threshold Screening

## Overview

Article 35(1) GDPR requires a DPIA when processing is "likely to result in a high risk to the rights and freedoms of natural persons." This skill provides a structured screening methodology to make that determination before committing to a full DPIA.

## Screening Criteria

### EDPB Nine-Criteria Test (WP248rev.01)

Processing that meets **two or more** of the following criteria generally requires a DPIA:

| # | Criterion | GDPR Reference |
|---|-----------|----------------|
| 1 | Evaluation or scoring | Art. 35(3)(a) |
| 2 | Automated decision-making with legal/similar effect | Art. 35(3)(a) |
| 3 | Systematic monitoring | Art. 35(3)(c) |
| 4 | Sensitive data or data of highly personal nature | Art. 9, Art. 10 |
| 5 | Data processed on a large scale | Recital 91 |
| 6 | Matching or combining datasets | WP248 |
| 7 | Data concerning vulnerable data subjects | WP248 |
| 8 | Innovative use or applying new technological solutions | WP248 |
| 9 | Processing that prevents data subjects from exercising a right | Art. 22, Art. 35(3)(b) |

### Mandatory DPIA Triggers (Art. 35(3))

A DPIA is always required for:

- **(a)** Systematic and extensive evaluation of personal aspects based on automated processing, including profiling, producing legal effects or similarly significant effects
- **(b)** Large-scale processing of special categories of data (Art. 9(1)) or criminal conviction data (Art. 10)
- **(c)** Systematic monitoring of a publicly accessible area on a large scale

### National Supervisory Authority Blacklists (Art. 35(4))

Each EU/EEA supervisory authority publishes a list of processing operations requiring a DPIA. The screening must check the relevant national blacklist based on the controller establishment.

## Screening Process

1. **Identify processing activity** -- Describe the proposed or changed processing
2. **Check mandatory triggers** -- Evaluate against Art. 35(3)(a)-(c)
3. **Check national blacklist** -- Consult the relevant SA published list
4. **Apply nine-criteria test** -- Score each WP248 criterion as met/not met
5. **Document rationale** -- Record the screening decision with justification
6. **Escalate or close** -- Route to full DPIA or document exemption

## Decision Logic

```
IF any Art. 35(3) mandatory trigger is met → DPIA REQUIRED
ELSE IF processing appears on national SA blacklist → DPIA REQUIRED
ELSE IF 2+ WP248 criteria are met → DPIA REQUIRED
ELSE IF 1 WP248 criterion is met → DPIA RECOMMENDED (risk-based decision)
ELSE → DPIA NOT REQUIRED (document exemption)
```

## Integration Points

- **RoPA linkage**: Screening results attach to the corresponding RoPA entry
- **Change management**: New processing or material changes trigger re-screening
- **DPIA register**: Positive screening decisions feed the DPIA pipeline
