---
name: dpia-mitigation-plan
description: >-
  Structures risk mitigation planning and residual risk tracking for Data
  Protection Impact Assessments under GDPR Article 35(7)(d). Covers
  mitigation measure identification, implementation tracking, residual
  risk acceptance, and Art. 36 prior consultation triggers. Keywords:
  DPIA mitigation, risk treatment, residual risk, Art. 35(7)(d),
  safeguards, mitigation tracking, prior consultation.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-impact-assessment
  tags: "dpia-mitigation, risk-treatment, residual-risk, art-35-7d, safeguards"
---

# DPIA Mitigation Planning

## Overview

Article 35(7)(d) GDPR requires a DPIA to include "the measures envisaged to address the risks, including safeguards, security measures and mechanisms to ensure the protection of personal data and to demonstrate compliance with this Regulation." This skill provides a structured mitigation planning framework.

## Mitigation Strategy Categories

### Technical Measures
| Category | Examples | GDPR Reference |
|----------|----------|----------------|
| Encryption | At-rest, in-transit, end-to-end | Art. 32(1)(a) |
| Pseudonymisation | Tokenisation, hashing, key-coded | Art. 25(1), Art. 32(1)(a) |
| Access controls | RBAC, MFA, privileged access management | Art. 32(1)(b) |
| Data minimisation | Field-level reduction, aggregation, sampling | Art. 5(1)(c), Art. 25(1) |
| Anonymisation | k-anonymity, differential privacy, generalisation | Recital 26 |
| Monitoring | SIEM, DLP, anomaly detection | Art. 32(1)(d) |

### Organisational Measures
| Category | Examples | GDPR Reference |
|----------|----------|----------------|
| Policies | Data protection policy, acceptable use | Art. 24(2) |
| Training | Privacy awareness, role-specific training | Art. 39(1)(b) |
| Contracts | DPAs, joint controller arrangements, NDAs | Art. 28, Art. 26 |
| Audits | Internal audits, processor audits, certification | Art. 28(3)(h) |
| Governance | DPO oversight, privacy committee, RACI | Art. 37-39 |
| Incident response | Breach procedures, notification protocols | Art. 33-34 |

## Mitigation Plan Structure

For each identified risk:

1. **Risk reference** -- Link to DPIA risk register entry
2. **Inherent risk level** -- Before mitigation
3. **Proposed measures** -- Specific technical and organisational controls
4. **Implementation owner** -- Accountable person
5. **Implementation deadline** -- Target completion date
6. **Verification method** -- How effectiveness will be confirmed
7. **Residual risk level** -- After planned mitigation
8. **Acceptance decision** -- Within appetite / escalation required / prior consultation

## Residual Risk Decision Framework

```
Residual Risk LOW → Accept; document; routine monitoring
Residual Risk MEDIUM → Accept with enhanced monitoring; annual review
Residual Risk HIGH → Escalate to senior management; consider additional measures
Residual Risk VERY HIGH → Art. 36 prior consultation required before processing
```

## Implementation Tracking

Each mitigation measure progresses through:
- **Proposed** -- Identified but not yet approved
- **Approved** -- Budget and resources allocated
- **In Progress** -- Implementation underway
- **Implemented** -- Deployed and operational
- **Verified** -- Effectiveness confirmed through testing
