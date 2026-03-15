# Employee Monitoring DPIA Workflows

## Workflow 1: Monitoring DPIA Screening Decision Tree

```
START: Proposal to implement employee monitoring system
│
├─ Does the monitoring involve any of the following?
│  □ Video surveillance / CCTV
│  □ Email or internet monitoring
│  □ GPS or location tracking
│  □ Keystroke logging or screen capture
│  □ Productivity analytics or scoring
│  □ Biometric data collection
│  □ Telephone recording
│  □ Access control logging
│
├─ Is the monitoring directed at employees?
│  ├─ YES → Employees are vulnerable data subjects (EDPB criterion 7)
│  │  ├─ Monitoring is systematic (EDPB criterion 3) → At least 2 criteria met
│  │  └─ DPIA IS MANDATORY. Proceed to Workflow 2.
│  └─ NO → Standard DPIA screening per conducting-gdpr-dpia skill.
│
├─ Has the national supervisory authority listed employee monitoring on its Art. 35(4) list?
│  ├─ YES → DPIA is mandatory by DPA list.
│  └─ NO → DPIA is still mandatory due to EDPB criteria above.
│
└─ END: Document the screening decision. DPIA is required for all employee monitoring.
```

## Workflow 2: Full Employee Monitoring DPIA Process

### Phase 1: Initiation (Days 1-5)

1. Monitoring system proposal received by DPO office.
2. DPO assigns DPIA reference number: DPIA-MON-[YEAR]-[SEQ] (e.g., DPIA-MON-2026-003).
3. DPIA team assembled:
   - Processing owner: HR Director or IT Security Manager
   - DPO: Independent adviser
   - IT Security Officer: Technical assessment
   - Legal Counsel: Employment law and ECHR compliance
   - Employee Representative or Works Council member: Art. 35(9) data subject views
4. In Germany, France, Netherlands, Austria: notify works council of proposed monitoring and DPIA.
5. Kick-off meeting to define monitoring scope, technology, and timeline.

### Phase 2: Systematic Description (Days 5-15)

1. Document the monitoring technology:
   - Vendor and product name
   - Deployment architecture (on-premise, cloud, hybrid)
   - Data collected (precisely: metadata, content, images, location, biometric)
   - Data frequency (continuous, periodic, triggered)
   - Data storage location and encryption
2. Document the monitoring scope:
   - Which employees are monitored (all, specific departments, specific roles)
   - Whether contractors and visitors are also captured
   - Geographic scope (all sites, specific locations)
3. Document data flows:
   - Where data is collected → where it is stored → who can access it → how long it is retained → how it is deleted
4. Document the lawful basis:
   - Art. 6(1) basis for each data element
   - Art. 9(2) condition if biometric or health data is involved
   - National law basis (BDSG Section 26, Labour Code, Workers' Statute)

### Phase 3: Proportionality Assessment (Days 15-25)

1. Apply the Barbulescu six-factor test:
   - Factor 1 (Prior notification): Is the monitoring system described in the privacy notice and AUP?
   - Factor 2 (Extent): What is the degree of intrusion? Content vs. metadata? Continuous vs. triggered?
   - Factor 3 (Legitimate reason): What specific, documented reason justifies the monitoring?
   - Factor 4 (Less intrusive alternatives): Could a less invasive method achieve the same objective?
   - Factor 5 (Consequences): Can monitoring data lead to disciplinary action or dismissal?
   - Factor 6 (Safeguards): What access controls, retention limits, and grievance mechanisms are in place?

2. For each monitoring measure, document:
   - The specific legitimate aim
   - Whether the monitoring is necessary (cannot achieve the aim otherwise)
   - Whether the monitoring is proportionate (intrusion justified by the aim)
   - Available less intrusive alternatives

3. Decision outcome:
   - PROCEED: Monitoring passes proportionality test → continue to Phase 4
   - MODIFY: Monitoring fails on specific factors → revise to use less intrusive method
   - REJECT: Monitoring is fundamentally disproportionate → advise against deployment

### Phase 4: Risk Assessment (Days 25-35)

1. Identify risks specific to the monitoring system:
   - Risk to employee autonomy and dignity
   - Risk of chilling effect on legitimate workplace activity
   - Risk of discrimination (monitoring data used for discriminatory decisions)
   - Risk of function creep (monitoring data used beyond original purpose)
   - Risk of unauthorised access to monitoring data
   - Risk of capturing third-party data (family members in CCTV, visitors)
   - Risk of capturing privileged communications (legal, medical, union)

2. Assess each risk:
   - Likelihood: Remote / Possible / Likely / Almost Certain
   - Severity: Negligible / Limited / Significant / Maximum
   - Inherent Risk Level: Low / Medium / High / Very High

3. Record in risk register with unique identifiers.

### Phase 5: Mitigation and Residual Risk (Days 35-45)

1. For each High or Very High risk, define mitigation measures:
   - Technical: encryption, access controls, automated deletion, privileged communication exclusion
   - Organisational: AUP update, training, grievance procedure, annual proportionality review
   - Contractual: DPA with monitoring vendor, data subject notification

2. Assess residual risk after mitigation.

3. If residual risk remains High or Very High:
   - Consider whether the monitoring can be further modified to reduce risk
   - If not: initiate Art. 36 prior consultation with the supervisory authority

### Phase 6: Review and Approval (Days 45-55)

1. DPO reviews completed DPIA and provides written advice per Art. 35(2).
2. Works council review (where applicable).
3. Employee consultation per Art. 35(9) — if not via works council, through alternative mechanism.
4. Senior management approval with acknowledgment of residual risks.
5. DPIA registered in the central DPIA register.
6. Review date scheduled: minimum annually, or upon any change to the monitoring system.

## Workflow 3: Monitoring DPIA Annual Review

```
START: Annual review date or trigger event
│
├─ Has the monitoring technology changed?
│  ├─ YES → Reassess Phase 2 (systematic description) and Phase 3 (proportionality)
│  └─ NO → Continue
│
├─ Has the monitoring scope changed (new employees, new locations)?
│  ├─ YES → Update Phase 2 and reassess Phase 4 (risk assessment)
│  └─ NO → Continue
│
├─ Have any employee complaints been received about the monitoring?
│  ├─ YES → Review complaints and assess whether they indicate disproportionality
│  └─ NO → Continue
│
├─ Has there been any supervisory authority guidance or enforcement action relevant to the monitoring type?
│  ├─ YES → Assess impact on the DPIA conclusions
│  └─ NO → Continue
│
├─ Are the mitigation measures still effective?
│  ├─ YES → Document review outcome and schedule next review
│  └─ NO → Revise mitigation measures and reassess residual risk
│
└─ END: Document the review, update the DPIA version, and record in the DPIA register.
```
