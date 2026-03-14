---
name: privacy-threshold-analysis
description: >-
  Guides the Privacy Threshold Analysis screening process to determine
  whether a full DPIA is required. Provides a quick-screen questionnaire,
  threshold criteria based on WP248rev.01, escalation triggers, and
  documentation requirements. Activate when evaluating new processing
  activities, system changes, or procurement decisions. Keywords: PTA,
  privacy threshold analysis, DPIA screening, quick-screen, threshold
  criteria, WP248, escalation triggers.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-impact-assessment
  tags: "pta, privacy-threshold-analysis, dpia-screening, wp248, escalation"
---

# Conducting Privacy Threshold Analysis

## Overview

A Privacy Threshold Analysis (PTA) is a lightweight screening tool used to determine whether a processing activity requires a full DPIA under Art. 35. The PTA functions as a triage mechanism: it applies the WP248rev.01 nine criteria, Art. 35(3) mandatory triggers, and national supervisory authority DPIA lists to quickly classify processing activities into three categories: DPIA required, DPIA recommended, or DPIA not required. Every new processing activity, system change, or procurement of data-processing services should pass through the PTA before implementation.

## PTA Quick-Screen Questionnaire

### Section A: Art. 35(3) Mandatory Triggers

| Question | Yes/No | If Yes |
|----------|--------|--------|
| A1. Does the processing involve systematic and extensive evaluation of personal aspects based on automated processing (including profiling) on which decisions are based that produce legal effects or similarly significantly affect individuals? | | DPIA mandatory — Art. 35(3)(a) |
| A2. Does the processing involve large-scale processing of special categories of data (Art. 9(1): health, biometric, genetic, racial/ethnic, political, religious, trade union, sexual orientation) or criminal conviction data (Art. 10)? | | DPIA mandatory — Art. 35(3)(b) |
| A3. Does the processing involve systematic monitoring of a publicly accessible area on a large scale (e.g., CCTV in public spaces, Wi-Fi tracking)? | | DPIA mandatory — Art. 35(3)(c) |
| A4. Does the processing appear on the national supervisory authority's DPIA required list (Art. 35(4))? | | DPIA mandatory |

**If any question in Section A is answered Yes: DPIA is mandatory. Stop. Proceed to full DPIA.**

### Section B: EDPB WP248rev.01 Nine Criteria

| Question | Criterion | Yes/No |
|----------|-----------|--------|
| B1. Does the processing involve evaluation or scoring of individuals (profiling, prediction, credit scoring, behavioural analysis)? | C1 | |
| B2. Does the processing involve automated decision-making that produces legal effects or similarly significant effects on individuals? | C2 | |
| B3. Does the processing involve systematic monitoring of individuals (observation, tracking, surveillance)? | C3 | |
| B4. Does the processing involve sensitive data (Art. 9 special categories) or highly personal data (financial, location, communications)? | C4 | |
| B5. Is the processing carried out on a large scale (number of subjects, volume, geographic scope, duration)? | C5 | |
| B6. Does the processing involve matching or combining datasets from different sources beyond data subject expectations? | C6 | |
| B7. Does the processing involve data concerning vulnerable individuals (children, employees, patients, elderly, disabled, asylum seekers)? | C7 | |
| B8. Does the processing involve innovative use of technology or application of existing technology in a new way? | C8 | |
| B9. Does the processing prevent individuals from exercising a right or using a service or contract? | C9 | |

**Scoring:**
- **2 or more criteria met**: DPIA is strongly recommended (presumptively required per WP248rev.01)
- **1 criterion met**: DPIA is recommended. Consult DPO for final determination.
- **0 criteria met**: DPIA is not required based on EDPB criteria.

### Section C: Additional Risk Factors

| Question | Yes/No | Impact |
|----------|--------|--------|
| C1. Does the processing involve international transfers to countries without an adequacy decision? | | Additional risk factor — TIA required alongside DPIA if applicable |
| C2. Is this a new processing activity not previously assessed? | | New processing should be assessed more conservatively |
| C3. Has similar processing been subject to enforcement action by any supervisory authority? | | Elevated scrutiny — DPIA recommended regardless of criteria count |
| C4. Does the processing involve real-time data processing or urgent decision-making? | | Reduced opportunity for human review — elevated risk |

## PTA Decision Matrix

| Section A Triggers | Section B Criteria | Section C Factors | Determination |
|-------------------|--------------------|-------------------|---------------|
| Any trigger met | N/A | N/A | **DPIA mandatory** |
| No trigger met | 2+ criteria | Any | **DPIA strongly recommended** |
| No trigger met | 1 criterion | 1+ factors | **DPIA recommended** |
| No trigger met | 1 criterion | 0 factors | **DPO consultation recommended** |
| No trigger met | 0 criteria | 1+ factors | **Document screening; monitor** |
| No trigger met | 0 criteria | 0 factors | **DPIA not required** |

## PTA Documentation Requirements

Regardless of the outcome, every PTA must be documented and retained. The documentation must include:

| Field | Content |
|-------|---------|
| PTA Reference | Unique identifier (PTA-[ORG]-[YEAR]-[SEQ]) |
| Processing Activity Name | Descriptive name of the processing activity |
| Processing Owner | Name and role of the person responsible |
| Date of PTA | Date the screening was completed |
| Section A Responses | Yes/No for each Art. 35(3) question |
| Section B Responses | Yes/No for each WP248 criterion with justification |
| Section C Responses | Yes/No for each additional factor |
| Determination | DPIA mandatory/recommended/not required |
| DPO Sign-Off | DPO name, date, and whether they agree with the determination |
| Next Steps | Full DPIA initiated / Processing approved without DPIA / Deferred pending further information |

## Escalation Process

When a PTA determines that a DPIA is required:
1. PTA result is logged in the DPIA register.
2. Processing owner is notified that a DPIA must be completed before processing begins.
3. DPO assigns a DPIA reference number and initiates the DPIA process.
4. Processing must not commence until the DPIA is completed and approved.

When a PTA determines that a DPIA is recommended but not mandatory:
1. DPO reviews the PTA and makes a final determination.
2. If DPO determines DPIA is needed: escalate as above.
3. If DPO determines DPIA is not needed: document the rationale and approve processing.

## Common PTA Mistakes

1. **Skipping the PTA**: Proceeding with new processing without any screening — no documentation of the decision not to conduct a DPIA.
2. **Self-assessment without DPO review**: Processing owners conducting PTA without DPO involvement, leading to underestimation of criteria.
3. **Narrow interpretation of criteria**: Interpreting "large scale" or "systematic monitoring" too narrowly to avoid triggering a DPIA.
4. **No documentation**: Conducting a mental screening without documented PTA — cannot demonstrate accountability under Art. 5(2).
5. **One-time screening**: Completing a PTA at project initiation and never revisiting when the processing scope changes.
