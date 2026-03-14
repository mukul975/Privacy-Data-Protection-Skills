---
name: designing-breach-simulation-exercise
description: >-
  Designs and executes tabletop breach simulation exercises for testing
  organizational breach response capabilities. Covers scenario creation with
  realistic inject timelines, participant role assignment, communication
  testing across internal and external channels, decision-point evaluation,
  and after-action report generation. Keywords: tabletop exercise, breach
  simulation, incident response testing, scenario design, after-action report.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-breach-response
  tags: "tabletop-exercise, breach-simulation, incident-response, scenario-design, after-action"
---

# Designing Breach Simulation Exercise

## Overview

Breach simulation exercises (tabletop exercises) test an organization's ability to detect, respond to, and recover from a personal data breach without the consequences of an actual incident. A well-designed exercise validates the breach response plan, identifies gaps in procedures, communication, and decision-making, and builds institutional muscle memory. This skill covers the end-to-end design process from scenario creation through after-action reporting.

## Exercise Design Framework

### Exercise Types

| Type | Duration | Participants | Complexity | Purpose |
|------|----------|-------------|-----------|---------|
| Tabletop (discussion-based) | 2-4 hours | 8-15 senior stakeholders | Medium | Test decision-making, communication, and policy application |
| Functional exercise | 4-8 hours | 15-30 cross-functional team members | High | Test operational procedures and tool usage |
| Full-scale simulation | 1-3 days | Organization-wide (50+ participants) | Very high | Test end-to-end response including technical, legal, communications, and executive functions |

### Recommended Exercise Cadence

| Exercise Type | Frequency | Audience |
|--------------|-----------|----------|
| Tabletop | Semi-annually | Executive team, DPO, legal, communications, CISO |
| Functional | Annually | SOC, privacy team, IT operations, HR, customer service |
| Full-scale | Every 2 years | Organization-wide |

## Scenario Design

### Scenario 1: Ransomware Attack on Customer Database

**Complexity**: High
**Duration**: 3 hours
**Primary objectives**: Test Art. 33 72-hour notification decision-making, executive communication, and vendor coordination.

**Background briefing (distributed 24 hours before exercise):**
Stellar Payments Group processes payment transactions for 15,230 account holders across 18 EU member states and 12 US states. The production customer database is hosted on a PostgreSQL cluster in AWS eu-west-1. The DPO is Dr. Elena Vasquez. The CISO is Thomas Brenner. Mandiant is the retained incident response firm.

**Inject timeline:**

| Time | Inject | Expected Action |
|------|--------|-----------------|
| T+0 min | SOC alert: CrowdStrike detects rapid file encryption on db-prod-eu-west-01. 500+ file renames per second. Known ransomware indicators (LockBit 3.0). | SOC initiates incident response. Incident Commander activated. |
| T+15 min | Update: Encryption spreading to db-prod-eu-west-02 and 03. Customer portal returning database errors. Customer complaints arriving via support channels. | Decision point: Isolate database cluster? Accept service disruption vs. further damage? |
| T+30 min | Forensic initial finding: Attack vector appears to be compromised service account (svc-migration-2024). Account authenticated from Tor exit node 3 days prior. | Update risk assessment. Determine scope of potentially compromised data. |
| T+60 min | Customer database confirmed encrypted. 48,720 records across 15,230 data subjects. Backup from 12 hours ago available and verified clean. | Decision point: Restore from backup? Art. 33 notification clock — when did we "become aware"? |
| T+90 min | Ransom note found: 50 BTC demanded. Threat to publish data on dark web if not paid within 48 hours. Media outlet (Handelsblatt) calls communications team for comment. | Decision points: Pay ransom? Engage law enforcement? Media statement? |
| T+120 min | Mandiant confirms no evidence of exfiltration but cannot rule it out. Backup restoration is 60% complete. Berliner BfDI opens office in 2 hours. | Decision point: File Art. 33 notification now or wait for more information? Prepare Art. 34 data subject notification? |
| T+150 min | Second media outlet (Bloomberg) publishes story. Social media discussion begins. 50+ customer support calls in past hour. Three enterprise clients demand written assurance. | Communications crisis management. Customer and B2B stakeholder communication. |
| T+180 min | Exercise conclusion. Facilitator reveals exercise end state and leads debrief discussion. | After-action discussion. |

### Scenario 2: Insider Threat — Employee Data Exfiltration

**Complexity**: Medium
**Duration**: 2.5 hours

**Inject timeline:**

| Time | Inject | Expected Action |
|------|--------|-----------------|
| T+0 min | DLP alert: HR database export (3,400 employee records) copied to personal OneDrive by departing employee (last day is Friday). | Validate alert. Determine whether personal data is involved. |
| T+20 min | Records include names, home addresses, salaries, bank details, and national ID numbers. Employee's manager confirms the employee submitted resignation 2 weeks ago. | Decision point: Confront employee? Preserve evidence? Involve legal? |
| T+45 min | IT confirms the file was synced to the employee's personal laptop. The employee is currently in the office. | Decision points: Device seizure? HR involvement? Works Council (Betriebsrat) notification? |
| T+75 min | Legal advises on employee rights under German labor law. Works Council representative requests consultation before any confrontation. | Balance breach response urgency against employee rights and Works Council obligations. |
| T+105 min | Employee is interviewed with Works Council representative present. Claims data was for "reference purposes." Refuses to allow personal laptop examination. | Decision point: Law enforcement referral? Court order for device examination? Art. 33 notification? |
| T+135 min | DPO completes risk assessment: 3,400 employees, government IDs + financial data = high risk. Art. 33 and Art. 34 notification recommended. | Notification preparation. Employee communication planning (how to tell 3,400 employees their data was compromised by a colleague). |
| T+150 min | Exercise conclusion and debrief. | After-action discussion. |

### Scenario 3: Third-Party Processor Breach

**Complexity**: Medium
**Duration**: 2 hours

**Inject timeline:**

| Time | Inject | Expected Action |
|------|--------|-----------------|
| T+0 min | Email from cloud payroll processor (PayrollCloud GmbH): "We are writing to inform you of a security incident affecting customer data hosted on our platform." No details provided. | Contact processor for details. Review Art. 28 DPA for incident notification obligations. |
| T+20 min | Processor confirms: SQL injection attack. Unclear which clients affected. Estimated timeline for client-specific impact assessment: 5-7 days. | Decision point: Can we wait 5-7 days? How does this affect our 72-hour clock? |
| T+45 min | Processor provides partial information: "Your organization's data was on the affected server, but we cannot confirm whether it was accessed." 3,400 employee payroll records potentially exposed. | Assess when the controller "became aware" for Art. 33 purposes. Begin parallel risk assessment. |
| T+75 min | Media reports the processor breach. Several of the processor's other clients have publicly acknowledged being affected. | Decision point: Proactive disclosure? Wait for confirmed impact? |
| T+105 min | Processor confirms: Stellar Payments Group data was accessed. 3,400 employee records including names, salaries, bank account numbers, and tax IDs. | Art. 33 notification preparation. Employee communication planning. Processor accountability assessment. |
| T+120 min | Exercise conclusion and debrief. | After-action discussion. |

## Participant Roles

| Role | Participant | Responsibilities During Exercise |
|------|------------|----------------------------------|
| Incident Commander | CISO (Thomas Brenner) | Overall incident coordination, resource allocation, containment decisions |
| Privacy Lead | DPO (Dr. Elena Vasquez) | Notification decisions, risk assessment, data subject communication |
| Legal Counsel | General Counsel (Sarah Chen) | Legal advice, privilege management, law enforcement coordination, regulatory strategy |
| Communications Lead | Communications Director (Martin Keller) | Media response, customer communication, internal communication |
| IT Operations | IT Director (Petra Hoffmann) | Technical containment, backup restoration, system recovery |
| Executive Sponsor | CEO (Marcus Lindqvist) | Strategic decisions, board notification, public statements |
| Customer Relations | VP Customer Success (James Park) | Customer communication, B2B client management |
| HR Lead | CHRO (Claudia Richter) | Employee communication, Works Council coordination (insider threat scenarios) |
| Exercise Facilitator | External consultant or internal audit | Scenario delivery, inject timing, discussion facilitation, observation |
| Observer/Recorder | DPO office analyst | Document decisions, actions, timelines, and gaps for after-action report |

## Decision Points to Evaluate

1. **Breach awareness determination**: When exactly did the controller "become aware" for Art. 33 clock purposes?
2. **Containment vs. evidence preservation**: Did the team balance immediate containment with the need to preserve forensic evidence?
3. **Notification timing**: Was the 72-hour deadline tracked and met?
4. **Risk assessment quality**: Was the risk assessment methodology applied consistently and documented?
5. **Communication coordination**: Were media, customer, and internal communications coordinated and consistent?
6. **Escalation effectiveness**: Were the right people involved at the right time?
7. **Cross-functional coordination**: Did legal, privacy, IT, and communications work together effectively?
8. **Regulatory coordination**: Was the correct supervisory authority identified and notification prepared?
9. **Data subject communication**: Was Art. 34 notification considered at the appropriate threshold?
10. **Documentation**: Was the decision-making process documented in real-time?

## After-Action Report Structure

### Section 1: Exercise Summary
- Exercise date, duration, scenario, and participants.
- Exercise objectives and whether they were met.

### Section 2: Timeline Analysis
- Actual timeline of decisions and actions during the exercise.
- Comparison against expected/ideal timeline from the breach response plan.
- Identification of delays and bottlenecks.

### Section 3: Findings
- What worked well (strengths to maintain).
- What needs improvement (gaps and deficiencies).
- Severity rating for each finding: Critical, Major, Minor, Observation.

### Section 4: Recommendations
- Specific, actionable remediation recommendations with owners and deadlines.
- Prioritized by severity.

### Section 5: Metrics
- Time from detection to containment decision.
- Time from awareness to DPO notification.
- Time from awareness to notification preparation completion.
- Communication consistency score (number of conflicting messages identified).
- Decision quality score (percentage of decisions aligned with policy and regulation).
