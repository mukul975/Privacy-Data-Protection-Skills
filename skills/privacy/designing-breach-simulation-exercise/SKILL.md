---
name: designing-breach-simulation-exercise
description: >-
  Designs and executes tabletop breach simulation exercises to test
  organizational readiness for data breach response. Covers scenario creation
  with realistic attack narratives, participant role assignment, inject timeline
  design, communication channel testing, decision-point evaluation, and
  after-action report generation. Keywords: tabletop exercise, breach
  simulation, incident response drill, scenario testing, after-action report.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-breach-response
  tags: "tabletop-exercise, breach-simulation, incident-response-drill, scenario-testing, after-action"
---

# Designing Breach Simulation Exercise

## Overview

Breach simulation exercises (tabletop exercises) test an organization's ability to detect, respond to, and recover from a personal data breach without the cost and disruption of an actual incident. EDPB Guidelines 9/2022 recommend regular testing of breach response procedures. This skill provides the complete framework for designing, executing, and evaluating tabletop exercises.

## Exercise Types

| Type | Duration | Participants | Complexity | Frequency |
|------|----------|-------------|-----------|-----------|
| Discussion-based tabletop | 2-4 hours | 8-15 senior stakeholders | Medium | Semi-annual |
| Functional exercise | 4-8 hours | 15-30 including operational staff | High | Annual |
| Full-scale simulation | 1-3 days | Organization-wide | Very high | Every 2-3 years |

## Scenario Design Framework

### Scenario 1: Ransomware Attack on Customer Database

**Narrative**: A sophisticated threat actor deploys LockBit 3.0 ransomware targeting the production customer database. The attack begins with a spear-phishing email to an IT administrator. The attacker harvests credentials, moves laterally through the network, and encrypts 48,720 customer records. A ransom note demands 15 BTC (approximately EUR 850,000) within 72 hours.

**Complexity layers**:
- Phase 1: SOC detects anomalous file encryption activity at 11:15 UTC on a Friday before a national holiday.
- Phase 2: Investigation reveals the initial compromise occurred 72 hours earlier — the attacker has been inside the network for 3 days.
- Phase 3: Media inquiry received from a technology journalist who was tipped off about the attack.
- Phase 4: Forensic analysis cannot confirm or deny data exfiltration.
- Phase 5: The 72-hour GDPR notification deadline falls on a national holiday.

### Scenario 2: Insider Threat — Departing Employee Data Theft

**Narrative**: A senior data analyst in the People Operations department who has submitted their resignation downloads a comprehensive employee dataset (3,400 records including names, salaries, performance ratings, and health information) to a personal cloud storage service. The DLP system generates an alert, but the analyst claims the download was for a legitimate work purpose.

**Complexity layers**:
- Phase 1: DLP alert triggers during business hours; analyst's manager confirms no legitimate business need.
- Phase 2: Analyst refuses to provide access to personal cloud storage for verification.
- Phase 3: Works council (Betriebsrat) representative raises concerns about employee surveillance proportionality.
- Phase 4: The dataset includes Art. 9 special category health data from the wellness programme.
- Phase 5: The analyst threatens to publish the data if disciplinary action is taken.

### Scenario 3: Third-Party Processor Breach

**Narrative**: Stellar Payments Group's cloud-hosted customer analytics platform (operated by a processor) experiences a breach. The processor notifies Stellar Payments 5 days after discovering the breach, claiming "investigation was needed." The breach potentially affects 42,000 customer records processed on Stellar Payments' behalf.

**Complexity layers**:
- Phase 1: Processor's notification is vague — minimal details about scope, cause, or affected data.
- Phase 2: Stellar Payments' 72-hour GDPR clock started when the processor notified, but 5 days have already elapsed since the processor became aware.
- Phase 3: The processor's Art. 28 data processing agreement specifies 24-hour notification to the controller.
- Phase 4: Affected data subjects are spread across 8 EU member states.
- Phase 5: The processor is established in the US and disputes GDPR applicability.

## Participant Roles

| Role | Participant | Exercise Responsibility |
|------|------------|----------------------|
| Incident Commander | CISO (Thomas Brenner) | Overall incident coordination and decision-making |
| Data Protection Officer | Dr. Elena Vasquez | Notification decision, regulatory communication, data subject rights |
| Legal Counsel | Sarah Chen (General Counsel) | Legal advice, privilege management, law enforcement coordination |
| Communications Director | Julia Hoffmann | Media response, internal communications, public statement |
| IT Forensics Lead | Marcus Weber (SOC Lead) | Technical investigation, evidence preservation, scope determination |
| HR Representative | Anna Kruger (VP People) | Employee-related breaches, works council coordination |
| Business Unit Lead | Regional Business Director | Operational impact assessment, customer relationship management |
| Executive Sponsor | Marcus Lindqvist (CEO) | Strategic decisions, board communication, budget authorization |
| Exercise Facilitator | External consultant or DPO deputy | Scenario presentation, inject delivery, observation, time management |
| Observer/Scribe | Internal audit representative | Documentation of decisions, gaps, and improvement opportunities |

## Inject Timeline Template

### Exercise: Ransomware Attack Tabletop (3.5 Hours)

| Time | Inject | Decision Point | Expected Response |
|------|--------|---------------|-------------------|
| 0:00 | Exercise brief and ground rules | — | — |
| 0:15 | Inject 1: SOC alert — anomalous file encryption on db-prod cluster | Classify as potential breach or security incident | Activate incident response procedure |
| 0:30 | Inject 2: Investigation confirms ransomware — customer data encrypted | Confirm personal data breach; start 72-hour clock | DPO notified; escalation to Incident Commander |
| 0:50 | Inject 3: Ransom note discovered demanding 15 BTC | Decide on ransom payment policy | Decline payment per policy; engage law enforcement |
| 1:10 | Inject 4: Discovery that initial compromise occurred 3 days ago | Re-assess scope and determine if exfiltration occurred | Expand investigation; preserve additional evidence |
| 1:30 | BREAK (15 minutes) | — | — |
| 1:45 | Inject 5: Media call — journalist asks about the attack | Prepare media statement | Communications Director drafts holding statement |
| 2:00 | Inject 6: Forensics cannot confirm or deny exfiltration | Decide notification approach given uncertainty | Apply precautionary principle; proceed with SA notification |
| 2:20 | Inject 7: 72-hour deadline falls on a national holiday | Determine if SA portal is available; identify backup channels | Submit before deadline; DPO activates on-call |
| 2:40 | Inject 8: Supervisory authority acknowledges notification and requests forensic report | Prepare supplementary submission timeline | Commit to 30-day forensic report delivery |
| 3:00 | Inject 9: Board chair calls demanding briefing | Brief the board on breach and response status | CEO provides structured briefing using prepared template |
| 3:15 | Exercise debrief and initial observations | — | — |
| 3:30 | Exercise concludes | — | — |

## Evaluation Criteria

### Communication Effectiveness
- Were the right people notified at each stage?
- Was internal communication clear and timely?
- Was the media response appropriate and pre-approved?
- Were data subjects considered throughout the decision-making process?

### Decision Quality
- Were decisions evidence-based or assumption-based?
- Were GDPR notification thresholds correctly applied?
- Was the precautionary principle applied where uncertainty existed?
- Were legal and regulatory obligations correctly identified?

### Process Adherence
- Did the team follow the documented breach response procedure?
- Were the escalation matrix and notification timelines followed?
- Was evidence preservation initiated before any remediation?
- Were all actions documented in the incident management system?

### Timeliness
- Would the 72-hour GDPR notification deadline have been met?
- Were all escalation targets reached within the required timeframes?
- Was the risk assessment completed within the expected timeline?

## After-Action Report Template

### Section 1: Exercise Overview
- Exercise name, date, duration, facilitator, participants
- Scenario summary

### Section 2: Key Observations
- What worked well (strengths)
- What needs improvement (gaps)
- Unexpected challenges encountered

### Section 3: Decision Log
- Each decision point, the decision made, the rationale, and whether it was correct

### Section 4: Gap Analysis
- Procedural gaps identified
- Technical capability gaps
- Training gaps
- Communication gaps

### Section 5: Improvement Actions
- Action items with owner, priority, and target completion date

### Section 6: Metrics
- Time to detect (simulated)
- Time to escalate to DPO
- Time to notification decision
- Time to SA notification preparation
- Time to media statement readiness
