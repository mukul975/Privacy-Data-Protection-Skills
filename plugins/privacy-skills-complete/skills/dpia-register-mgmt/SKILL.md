---
name: dpia-register-mgmt
description: >-
  Manages the organisational DPIA register tracking all Data Protection Impact
  Assessments across the enterprise. Covers DPIA lifecycle management, status
  tracking, review scheduling, Art. 35(11) periodic reassessment, and
  supervisory authority reporting. Implements a centralised register linking
  DPIAs to RoPA entries, risk registers, and mitigation plans. Keywords:
  DPIA register, DPIA tracking, Art. 35(11), review schedule, DPIA lifecycle,
  centralised register, DPIA portfolio management.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-impact-assessment
  tags: "dpia-register, dpia-tracking, art-35-11, review-schedule, dpia-lifecycle"
---

# DPIA Register Management

## Overview

Article 35(11) GDPR requires controllers to carry out reviews of DPIAs "at least when there is a change in the risk represented by processing operations." Effective DPIA register management ensures that all assessments are tracked, reviewed on schedule, and updated when processing changes. The register serves as the central accountability record demonstrating that the controller has systematically identified and assessed high-risk processing across the organisation.

## Register Structure

### Core DPIA Record Fields

| Field | Description | GDPR Reference |
|-------|-------------|----------------|
| DPIA Reference | Unique identifier (format: DPIA-[DEPT]-[YEAR]-[SEQ]) | Art. 5(2) Accountability |
| Processing Activity | Name and description of the processing operation assessed | Art. 35(7)(a) |
| RoPA Reference | Link to Records of Processing Activities entry | Art. 30 |
| Controller / Joint Controller | Responsible data controller(s) | Art. 35(1) |
| DPO Consulted | Confirmation DPO was consulted per Art. 35(2) | Art. 35(2) |
| Assessment Date | Date DPIA was completed | Art. 5(2) |
| DPIA Lead | Person who conducted the assessment | Accountability |
| Status | Draft, In Review, Approved, Requires Update, Archived | Art. 35(11) |
| Overall Risk Level | Residual risk level after mitigation (Low/Medium/High/Very High) | Art. 35(7)(c)-(d) |
| Prior Consultation | Whether Art. 36 prior consultation was required and outcome | Art. 36 |
| Review Date | Next scheduled review date | Art. 35(11) |
| Review Trigger | Event that will trigger early reassessment | Art. 35(11) |
| Linked Mitigation Plan | Reference to the mitigation plan document | Art. 35(7)(d) |
| Approval Authority | Senior management or board member who approved | Art. 24 |

### DPIA Lifecycle States

```
[Screening] ──► [Draft] ──► [DPO Review] ──► [Approved]
                                                  │
                                    ┌─────────────┤
                                    │             │
                              [Requires Update]  [Active Monitoring]
                                    │             │
                                    └─► [Revised] ─► [Re-approved]
                                                  │
                                            [Archived]
```

**Screening**: Processing activity identified as potentially requiring DPIA; threshold assessment conducted.

**Draft**: DPIA being prepared; processing description, necessity assessment, and risk assessment in progress.

**DPO Review**: Complete draft submitted to DPO for Art. 35(2) advice.

**Approved**: DPIA reviewed, DPO advice incorporated, residual risk accepted, processing may commence.

**Active Monitoring**: Approved DPIA with ongoing mitigation tracking and periodic review.

**Requires Update**: Triggered by processing change, incident, or scheduled review.

**Revised**: Updated DPIA addressing changes or new risks.

**Re-approved**: Revised DPIA reviewed and approved.

**Archived**: Processing ceased; DPIA retained for accountability records per retention policy.

## Review Scheduling

### Art. 35(11) Periodic Review Requirements

The GDPR does not specify a fixed review frequency. The EDPB recommends that DPIAs be reviewed "at least when there is a change in the risk represented by processing operations." Organisational best practice establishes:

| Risk Level | Review Frequency | Rationale |
|------------|-----------------|-----------|
| Very High (with Art. 36 consultation) | Every 6 months | Highest risk requires most frequent reassessment |
| High | Annually | Significant risk warrants annual review |
| Medium | Every 18 months | Moderate risk with standard review cycle |
| Low | Every 24 months | Lower risk allows extended review cycle |

### Change-Triggered Review Events

Regardless of scheduled review, a DPIA must be reassessed when:

1. **Processing scope changes**: New data categories, new data subjects, expanded geographic scope
2. **Technology changes**: New system, vendor change, algorithm update, infrastructure migration
3. **Legal/regulatory change**: New legislation, supervisory authority guidance, court ruling
4. **Incident or breach**: Data breach affecting the assessed processing activity
5. **Organisational change**: Merger, acquisition, new controller, new processor
6. **Data subject complaint**: Pattern of complaints about the assessed processing
7. **Audit finding**: Internal or external audit identifies DPIA gap
8. **DPO recommendation**: DPO identifies emerging risk or changed context

## Supervisory Authority Reporting

### Art. 35(1) Documentation Obligation

The DPIA register must be available for inspection by the supervisory authority upon request. Key reporting elements:

- Complete list of all DPIAs conducted with dates and outcomes
- Status of each DPIA (current, requires update, archived)
- Art. 36 prior consultation records and supervisory authority responses
- Evidence of Art. 35(11) periodic reviews conducted on schedule
- DPO consultation records for each DPIA

### Art. 36 Prior Consultation Tracking

For DPIAs that triggered prior consultation, the register tracks:

| Field | Description |
|-------|-------------|
| Submission Date | When the DPIA was submitted to the supervisory authority |
| SA Reference | Supervisory authority's case reference number |
| Response Date | When the SA responded |
| SA Outcome | Approved, approved with conditions, objected |
| Conditions | Any conditions imposed by the SA |
| Compliance Status | Whether conditions have been met |

## Integration Points

- **DPIA Risk Scoring**: Risk methodology feeding into register risk levels (see dpia-risk-scoring skill)
- **DPIA Mitigation Plan**: Linked mitigation plans tracked in register (see dpia-mitigation-plan skill)
- **DPIA Stakeholder Consult**: Consultation records linked to DPIA entries (see dpia-stakeholder-consult skill)
- **GDPR Accountability**: Register serves as key accountability evidence (see gdpr-accountability skill)
- **Automated ROPA Generation**: RoPA entries linked to DPIA register (see automated-ropa-generation skill)
