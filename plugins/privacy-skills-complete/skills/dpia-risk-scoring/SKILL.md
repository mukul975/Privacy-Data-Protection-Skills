---
name: dpia-risk-scoring
description: >-
  Provides a structured risk scoring methodology for Data Protection Impact
  Assessments aligned with ENISA threat taxonomy and ISO 29134. Covers
  likelihood and severity assessment, risk matrix construction, inherent
  vs residual risk calculation, and risk appetite thresholds per EDPB
  WP248rev.01 guidance. Keywords: risk scoring, DPIA risk matrix, likelihood,
  severity, ENISA, ISO 29134, residual risk, risk appetite.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-impact-assessment
  tags: "risk-scoring, dpia, risk-matrix, enisa, iso-29134, residual-risk"
---

# DPIA Risk Scoring Methodology

## Overview

Art. 35(7)(c) GDPR requires a DPIA to include "an assessment of the risks to the rights and freedoms of data subjects." This skill provides a quantifiable risk scoring framework that converts qualitative privacy risks into comparable, prioritised scores supporting mitigation decisions.

## Risk Scoring Framework

### Severity Scale (Impact on Data Subject Rights)

| Level | Score | Description | Examples |
|-------|-------|-------------|----------|
| Negligible | 1 | Minor inconvenience, easily recoverable | Temporary inability to access non-essential service |
| Limited | 2 | Significant inconvenience, recoverable with effort | Targeted advertising based on inferred preferences |
| Significant | 3 | Serious consequences, difficult to recover from | Financial loss, discrimination, reputational harm |
| Maximum | 4 | Irreversible or very difficult to recover from | Identity theft, physical safety risk, loss of employment |

### Likelihood Scale

| Level | Score | Description | Indicators |
|-------|-------|-------------|------------|
| Negligible | 1 | Unlikely given current controls | Strong technical controls, limited access, encrypted at rest and in transit |
| Limited | 2 | Possible but requires specific conditions | Some access controls, partial encryption, known but unproven attack vectors |
| Significant | 3 | Probable given known threat landscape | Weak controls in specific areas, prior incidents in sector, active threat actors |
| Maximum | 4 | Near-certain or already occurring | No controls, known vulnerabilities, prior breach of similar system |

### Risk Matrix

```
Severity →    Negligible(1)  Limited(2)  Significant(3)  Maximum(4)
Likelihood ↓
Maximum(4)        4(M)         8(H)        12(VH)         16(VH)
Significant(3)    3(L)         6(M)         9(H)          12(VH)
Limited(2)        2(L)         4(M)         6(M)           8(H)
Negligible(1)     1(L)         2(L)         3(L)           4(M)

Risk Levels: L=Low(1-3), M=Medium(4-6), H=High(7-9), VH=Very High(10-16)
```

## Risk Categories (ENISA-Aligned)

### Rights and Freedoms Impacts
1. **Loss of confidentiality** -- Unauthorised disclosure of personal data
2. **Loss of integrity** -- Unauthorised modification of personal data
3. **Loss of availability** -- Inability to access or use personal data
4. **Loss of purpose limitation** -- Data used beyond original purpose
5. **Discrimination** -- Unfair treatment based on processing outcomes
6. **Identity theft/fraud** -- Misuse of personal data for impersonation
7. **Financial loss** -- Direct or indirect monetary harm
8. **Reputational damage** -- Social standing or professional harm
9. **Physical harm** -- Safety or health impacts
10. **Loss of autonomy** -- Chilling effects on behaviour or free expression

## Inherent vs Residual Risk

- **Inherent risk**: Risk level before applying any mitigation measures
- **Residual risk**: Risk level after applying planned mitigation measures
- **Risk reduction**: Difference between inherent and residual risk scores
- **Acceptable risk threshold**: Organisation-defined tolerance level

## Art. 36 Prior Consultation Trigger

When residual risk remains **High** or **Very High** after all feasible mitigation measures, the controller must consult the supervisory authority under Art. 36(1) before commencing processing.
