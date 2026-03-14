# DPIA Workflow Procedures

## Workflow 1: DPIA Screening Decision Tree

```
START: New or changed processing operation identified
│
├─ Does the processing appear on the national supervisory authority's Art. 35(4) list?
│  ├─ YES → DPIA is mandatory. Proceed to Workflow 2.
│  └─ NO → Continue screening.
│
├─ Does the processing fall under Art. 35(3)(a): systematic/extensive profiling with significant effects?
│  ├─ YES → DPIA is mandatory. Proceed to Workflow 2.
│  └─ NO → Continue screening.
│
├─ Does the processing fall under Art. 35(3)(b): large-scale special category or criminal data?
│  ├─ YES → DPIA is mandatory. Proceed to Workflow 2.
│  └─ NO → Continue screening.
│
├─ Does the processing fall under Art. 35(3)(c): systematic large-scale public area monitoring?
│  ├─ YES → DPIA is mandatory. Proceed to Workflow 2.
│  └─ NO → Continue screening.
│
├─ Count the EDPB WP248rev.01 criteria met:
│  □ Evaluation or scoring
│  □ Automated decision-making with legal or significant effect
│  □ Systematic monitoring
│  □ Sensitive data or highly personal data
│  □ Large-scale processing
│  □ Matching or combining datasets
│  □ Vulnerable data subjects
│  □ Innovative technology
│  □ Processing preventing exercise of rights or use of service
│
│  ├─ 2 or more criteria met → DPIA is strongly recommended (presumptively required). Proceed to Workflow 2.
│  ├─ 1 criterion met → DPIA is recommended. Consult DPO for final determination.
│  └─ 0 criteria met → DPIA is not required. Document screening outcome and file.
│
└─ END: Document the screening decision, rationale, and DPO sign-off.
```

## Workflow 2: Full DPIA Execution Process

### Phase 1: Initiation (Days 1-5)
1. Processing owner submits DPIA request to the DPO office with preliminary processing description.
2. DPO assigns DPIA reference number from the central register (format: DPIA-[YEAR]-[SEQ], e.g., DPIA-2026-017).
3. DPO confirms DPIA obligation based on screening outcome.
4. DPIA team is assembled: processing owner (lead), DPO (advisor), IT security officer, legal counsel.
5. Kick-off meeting held to define scope, timeline, and documentation requirements.
6. Processing owner gathers supporting documentation: system architecture, data flow diagrams, privacy notices, consent forms, processor agreements, prior DPIA versions.

### Phase 2: Systematic Description (Days 6-15)
1. Processing owner completes Art. 35(7)(a) systematic description using the DPIA template.
2. Data flow mapping: identify all data sources, collection points, storage locations, processing steps, recipients, and deletion mechanisms.
3. Document all personal data elements with corresponding lawful basis under Art. 6(1) and, if applicable, Art. 9(2) condition.
4. Identify all processors and sub-processors with Art. 28 agreement status.
5. Document international transfers with applicable Chapter V safeguard mechanism.
6. IT security officer documents the technology stack, infrastructure, and existing security controls.
7. DPO reviews the systematic description for completeness and accuracy.

### Phase 3: Necessity and Proportionality (Days 16-20)
1. For each processing purpose, assess whether the processing is necessary to achieve that purpose.
2. Evaluate data minimisation: for each data element, document why it cannot be omitted or replaced with less identifying data.
3. Assess whether anonymisation or pseudonymisation could achieve the processing purpose.
4. Confirm retention periods are proportionate with documented justification.
5. Verify data subject rights mechanisms: access, rectification, erasure, restriction, portability, objection.
6. Legal counsel reviews lawful basis documentation and provides written opinion.

### Phase 4: Risk Assessment (Days 21-30)
1. Identify risk sources: internal employees (accidental/malicious), external attackers, processors, system failures, regulatory changes.
2. For each risk source, identify threat scenarios against the data flow map.
3. For each threat scenario, identify potential harms to data subjects (physical, material, non-material, social).
4. Assess likelihood for each scenario: Remote (< 10%), Possible (10-50%), Likely (50-90%), Almost Certain (> 90%).
5. Assess severity for each scenario: Negligible, Limited, Significant, Maximum.
6. Calculate inherent risk level using the Likelihood x Severity matrix.
7. IT security officer validates technical risk assessments.
8. Compile the risk register with unique risk identifiers (format: DPIA-[REF]-R[SEQ]).

### Phase 5: Mitigation and Residual Risk (Days 31-35)
1. For each High or Very High inherent risk, identify specific mitigation measures.
2. Document whether each measure is technical, organisational, or contractual.
3. Assign implementation responsibility and target completion date for each measure.
4. Reassess likelihood and severity after mitigation to determine residual risk level.
5. If any residual risk remains High or Very High, flag for Art. 36 prior consultation.
6. DPO reviews all mitigation measures and residual risk assessments.

### Phase 6: Approval and Registration (Days 36-40)
1. DPO provides written advice on the DPIA findings per Art. 35(2).
2. Processing owner documents whether DPO advice is accepted; if not, records reasons for departure.
3. Document whether data subject views were sought per Art. 35(9) and, if not, the justification.
4. Senior management (data controller representative) reviews and approves the DPIA.
5. DPIA is registered in the central DPIA register with next review date.
6. If Art. 36 prior consultation is required, initiate Workflow 3.

### Phase 7: Ongoing Monitoring
1. Processing owner monitors for material changes that trigger DPIA review.
2. Scheduled periodic review at minimum annually.
3. Incident-triggered review following any personal data breach involving the processing activity.
4. Version control: all updates create a new DPIA version with change log.

## Workflow 3: Art. 36 Prior Consultation Escalation

1. DPO prepares the prior consultation package per Art. 36(3): DPIA report, controller/processor responsibilities, measures and safeguards, DPO contact details.
2. Processing is paused until supervisory authority response is received.
3. Supervisory authority has 8 weeks to respond (extendable by 6 weeks for complex cases).
4. If supervisory authority provides written advice, implement required changes.
5. If supervisory authority indicates the processing would infringe the GDPR, do not proceed without remediation.
6. Document the entire prior consultation process and outcome in the DPIA register.

## Workflow 4: DPIA Review Trigger Assessment

```
TRIGGER EVENT DETECTED
│
├─ New data category added to processing?
│  └─ YES → Assess whether the new category changes the risk profile. If yes, update DPIA.
│
├─ New recipient or processor added?
│  └─ YES → Update data flow map and reassess transfer risks. Update DPIA.
│
├─ Technology change (new system, platform migration, algorithm update)?
│  └─ YES → Reassess technical risks and security measures. Update DPIA.
│
├─ Personal data breach involving this processing activity?
│  └─ YES → Mandatory DPIA review. Reassess risk levels and mitigation effectiveness.
│
├─ Regulatory change (new guidance, enforcement decision, supervisory authority list update)?
│  └─ YES → Assess whether the change affects the processing legality or risk assessment. Update DPIA if needed.
│
├─ Scheduled annual review date reached?
│  └─ YES → Conduct full DPIA review. Update all sections as needed.
│
├─ Complaint or data subject rights request revealing unexpected processing?
│  └─ YES → Investigate and update DPIA scope if processing was not fully documented.
│
└─ No trigger detected → No review required. Document monitoring check.
```
