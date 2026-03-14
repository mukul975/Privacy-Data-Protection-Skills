---
name: pia-review-cadence
description: >-
  Guides the periodic DPIA review lifecycle including trigger identification
  for regulatory changes, new data categories, technology changes, and breach
  incidents. Covers version control, stakeholder sign-off procedures, and
  DPIA register management per Art. 35(11). Keywords: DPIA review, PIA
  update, review cadence, version control, Art. 35(11), periodic review,
  trigger events, stakeholder sign-off.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-impact-assessment
  tags: "dpia-review, pia-update, review-cadence, version-control, art-35-11"
---

# Managing PIA Review and Update Cadence

## Overview

Art. 35(11) requires controllers to carry out a review to assess whether processing is performed in accordance with the DPIA, at least when there is a change in the risk represented by processing operations. A DPIA is not a one-time compliance exercise but a living document that must be maintained throughout the processing lifecycle. This skill establishes the governance framework for DPIA reviews, including trigger event identification, scheduled review cadence, version control, stakeholder sign-off, and DPIA register management.

## Art. 35(11) Review Obligation

"Where necessary, the controller shall carry out a review to assess if processing is performed in accordance with the data protection impact assessment at least when there is a change in the risk represented by processing operations."

This means:
1. Reviews are mandatory when risk changes
2. The controller should proactively monitor for risk changes
3. Regular periodic reviews are a best practice even without identified changes
4. The DPIA must be updated to reflect the current state of processing

## Review Trigger Categories

### Category 1: Regulatory Triggers

| Trigger | Assessment Action |
|---------|-------------------|
| New GDPR guidance from EDPB or national supervisory authority | Assess whether guidance changes the interpretation of lawful basis, proportionality, or risk level for the processing |
| Adequacy decision adopted, renewed, or invalidated | Reassess international transfers documented in the DPIA |
| National supervisory authority DPIA list updated (Art. 35(4)) | Check if processing now appears on the mandatory DPIA list |
| New Member State employment, health, or sector-specific law | Assess impact on lawful basis and proportionality for affected processing |
| Enforcement decision against similar processing by same or different SA | Assess whether the enforcement rationale applies to the organisation's processing |
| AI Act obligations becoming applicable | For AI-related DPIAs, assess conformity requirements |

### Category 2: Processing Change Triggers

| Trigger | Assessment Action |
|---------|-------------------|
| New personal data category added | Reassess data minimisation, proportionality, and risk levels |
| New category of data subjects | Reassess impact on new data subject group; check for vulnerable subjects |
| New recipient or processor | Update data flow map; reassess sub-processor chain; verify DPA |
| Change in lawful basis | Full reassessment of lawful basis justification and proportionality |
| Change in retention period | Reassess storage limitation compliance |
| New purpose identified for existing data | Art. 6(4) compatibility assessment; update DPIA purpose description |
| Processing volume significantly increased | Reassess whether processing now qualifies as "large scale" |
| Geographic scope expanded | Assess new jurisdictions for data protection requirements and international transfers |

### Category 3: Technology Change Triggers

| Trigger | Assessment Action |
|---------|-------------------|
| New system or platform deployment | Full technical risk reassessment; update system description and data flow maps |
| System upgrade or migration | Assess whether changes affect security measures, data flows, or processing scope |
| New algorithm or AI model deployed | Reassess algorithmic fairness, Art. 22 applicability, and AI Act classification |
| New tracking or monitoring technology | Reassess proportionality and ePrivacy compliance |
| Security vulnerability discovered | Immediate risk reassessment; assess whether existing mitigations remain effective |
| End-of-life for system component | Assess impact of reduced vendor support on security posture |

### Category 4: Incident Triggers

| Trigger | Assessment Action |
|---------|-------------------|
| Personal data breach involving the processing activity | Mandatory DPIA review; reassess risk levels and mitigation effectiveness |
| Near-miss security incident | Assess whether existing mitigations prevented the near-miss or were bypassed |
| Data subject complaint about the processing | Investigate whether complaint reveals processing not documented in DPIA |
| Supervisory authority enquiry about the processing | Review DPIA for completeness and accuracy before responding |
| Internal audit finding | Address audit findings and update DPIA accordingly |

### Category 5: Organisational Change Triggers

| Trigger | Assessment Action |
|---------|-------------------|
| Merger, acquisition, or divestiture | Reassess controller identity, data sharing arrangements, and international transfers |
| DPO change | New DPO to review and approve existing DPIAs |
| Significant staff restructuring | Verify processing owners, access controls, and organisational measures remain appropriate |
| New business unit using the processing | Assess whether new use case was documented in the DPIA |

## Scheduled Review Cadence

| Processing Risk Level | Recommended Review Interval | Justification |
|----------------------|---------------------------|---------------|
| Very High (prior consultation was required) | Every 6 months | Processing that required Art. 36 prior consultation needs frequent monitoring |
| High (biometric, large-scale special category, AI decision-making) | Every 6-12 months | High-risk processing warrants at least annual review |
| Medium (standard employee monitoring, marketing profiling) | Every 12 months | Annual review is the standard best practice |
| Low (routine processing with low residual risk) | Every 24 months | Extended review interval acceptable for stable, low-risk processing |

## Review Process

### Step 1: Trigger Detection and Triage

1. DPIA register manager monitors for trigger events continuously.
2. When a trigger is detected, it is logged in the DPIA register against the affected DPIA(s).
3. DPO triages the trigger to determine whether a full or targeted review is needed:
   - **Full review**: Re-examine all DPIA sections (new system, major regulatory change, data breach)
   - **Targeted review**: Update only the affected section (new recipient, retention change, minor system update)

### Step 2: Review Execution

1. Assemble the review team: processing owner, DPO, IT security (for technology changes), legal (for regulatory changes).
2. For full reviews: re-execute the complete DPIA methodology from screening through risk assessment.
3. For targeted reviews: update the affected section and reassess overall risk level.
4. Document all changes from the previous version.
5. Update the risk register with any new or modified risks.

### Step 3: Stakeholder Sign-Off

| Stakeholder | Role in Review | Sign-Off Required? |
|-------------|---------------|-------------------|
| Processing Owner | Validates accuracy of processing description and confirms mitigations are implemented | Yes |
| DPO | Provides independent advice on risk assessment and proportionality per Art. 35(2) | Yes |
| IT Security / CISO | Validates technical measures and security risk assessment | Yes (for technology-related reviews) |
| Legal Counsel | Validates lawful basis and regulatory compliance | Yes (for regulatory trigger reviews) |
| Senior Management | Approves residual risk acceptance | Yes (for full reviews or risk level changes) |
| Works Council | Consulted on employee monitoring changes (jurisdiction-dependent) | Yes (for employee monitoring DPIAs) |

### Step 4: Version Control and Registration

1. Create a new version of the DPIA document.
2. Use version numbering: major changes increment the first digit (v2.0); minor changes increment the second digit (v1.1).
3. Include a change log documenting:
   - Date of change
   - Trigger event that prompted the review
   - Sections modified
   - Summary of changes
   - Reviewer and approver names
4. Archive the previous version (do not delete; maintain audit trail).
5. Update the DPIA register with the new version, review date, and next review date.

## DPIA Register Management

The DPIA register is the central index of all DPIAs conducted by the organisation. It must contain:

| Field | Description |
|-------|-------------|
| DPIA Reference | Unique identifier (DPIA-[ORG]-[YEAR]-[SEQ]) |
| Processing Activity Name | Name of the processing operation |
| Version | Current version number |
| Status | Draft, Under Review, Approved, Expired, Superseded |
| Date Created | Date of initial DPIA |
| Last Review Date | Date of most recent review |
| Next Review Date | Scheduled date for next review |
| Processing Owner | Name and role of the processing owner |
| DPO Reviewer | Name of the DPO who reviewed |
| Risk Level (Current) | Current overall risk level after mitigation |
| Prior Consultation Required | Whether Art. 36 was triggered |
| Related Processing Activities | Cross-references to related DPIAs |
| Change Log | Summary of version history |

## Common Review Process Deficiencies

1. **No trigger monitoring**: Organisation relies solely on scheduled reviews without monitoring for change events.
2. **Stale DPIAs**: Reviews conducted on paper without verifying actual processing matches the DPIA description.
3. **No version control**: Edits made to the original document without maintaining previous versions.
4. **Incomplete stakeholder engagement**: DPO reviews without consulting the processing owner or IT security.
5. **No change log**: Updates made without documenting what changed and why.
6. **Expired review dates**: DPIA register shows overdue reviews without remediation.

## Enforcement Context

Supervisory authorities have increasingly scrutinised DPIA currency:
- **Swedish DPA vs Karolinska (2019)**: Noted that DPIA had not been conducted at all, let alone reviewed.
- **CNIL vs Clearview AI (2022)**: The absence of any DPIA was an aggravating factor in the fine determination.
- **Austrian DPA vs Austrian Post (2019)**: Inadequate ongoing review of profiling DPIA was a contributing factor.
