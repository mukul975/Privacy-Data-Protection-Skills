# AI DPIA Workflow Procedures

## Workflow 1: AI DPIA Screening Decision Tree

```
START: New AI/ML system proposed or existing system materially changed
│
├─ Does the AI system fall under AI Act Art. 5 (prohibited practices)?
│  ├─ YES → STOP. Processing is prohibited. Do not proceed.
│  └─ NO → Continue screening.
│
├─ Is the AI system classified as high-risk under AI Act Art. 6 + Annex III?
│  ├─ YES → DPIA is mandatory. AI Act conformity assessment also required. Proceed to Workflow 2.
│  └─ NO → Continue screening.
│
├─ Does the AI system make automated decisions with legal or significant effects (Art. 35(3)(a))?
│  ├─ YES → DPIA is mandatory. Proceed to Workflow 2.
│  └─ NO → Continue screening.
│
├─ Is the AI model trained on special category data at scale (Art. 35(3)(b))?
│  ├─ YES → DPIA is mandatory. Proceed to Workflow 2.
│  └─ NO → Continue screening.
│
├─ Does the AI system perform surveillance or monitoring of public areas (Art. 35(3)(c))?
│  ├─ YES → DPIA is mandatory. Proceed to Workflow 2.
│  └─ NO → Continue screening.
│
├─ Count EDPB WP248 criteria met by the AI system:
│  □ Evaluation or scoring (inherent to most ML models)
│  □ Automated decision-making with legal/significant effect
│  □ Systematic monitoring
│  □ Sensitive data or highly personal data in training/inference
│  □ Large-scale processing (training dataset size, inference volume)
│  □ Matching or combining datasets (multi-source training data)
│  □ Vulnerable data subjects
│  □ Innovative technology (novel architectures, techniques)
│  □ Processing preventing exercise of rights
│
│  ├─ 2+ criteria → DPIA is required. Proceed to Workflow 2.
│  ├─ 1 criterion → DPIA recommended. Consult DPO. If AI processes personal data, conduct DPIA.
│  └─ 0 criteria → Document screening. If AI processes personal data at any stage, conduct DPIA as best practice.
│
├─ Does the AI system use foundation models or LLMs trained on personal data?
│  ├─ YES → DPIA required per EDPB Guidelines 04/2025. Proceed to Workflow 2.
│  └─ NO → Continue.
│
├─ Does the AI system infer sensitive attributes from non-sensitive inputs?
│  ├─ YES → DPIA required. Proceed to Workflow 2.
│  └─ NO → Document screening outcome.
│
└─ END: Record screening decision with DPO sign-off.
```

## Workflow 2: Full AI DPIA Execution

### Phase 1: Initiation and Scoping (Days 1-5)

1. AI system owner submits DPIA request with preliminary system description to the DPO office.
2. DPO assigns AI-DPIA reference number (format: AI-DPIA-[YEAR]-[SEQ], e.g., AI-DPIA-2026-003).
3. Assemble the AI DPIA team:
   - AI system owner (lead)
   - Data Protection Officer (advisor)
   - ML/AI engineer responsible for the model
   - IT security officer
   - Legal counsel
   - Domain expert (for the application domain)
   - Optional: AI ethics representative
4. Kick-off meeting: define scope (training data, model architecture, deployment context, inference pipeline).
5. Gather documentation: model architecture specifications, training data catalogues, data flow diagrams, existing privacy notices, processor agreements for AI infrastructure.

### Phase 2: AI System Description (Days 6-15)

1. Document the complete AI lifecycle per the extended Art. 35(7)(a) framework:
   - Training data sources with provenance and lawful basis per source
   - Data preprocessing and feature engineering pipeline
   - Model architecture and training methodology
   - Deployment infrastructure and inference pipeline
   - Output types and downstream decision processes
2. Map data flows from training data collection through model inference and output delivery.
3. Document all personal data categories at each pipeline stage.
4. Identify all processors and sub-processors (cloud providers, labelling services, MLOps platforms).
5. Document international transfers (training data location, model hosting jurisdiction, inference processing location).
6. ML engineer provides model card with technical specifications and privacy-relevant properties.
7. DPO reviews completeness of the AI system description.

### Phase 3: Training Data Lawfulness Assessment (Days 16-22)

1. For each training data source, complete the lawful basis assessment:
   - Identify the Art. 6(1) basis for using the data in AI training
   - If legitimate interest: conduct and document the three-part balancing test
   - If consent: verify that AI training was a specified purpose at collection time
   - If contract: verify that AI training is necessary for the contracted service
2. For datasets containing Art. 9 special category data, identify the Art. 9(2) condition.
3. For web-scraped data: apply EDPB Guidelines 04/2025 heightened scrutiny — document why legitimate interest is justified despite the data subjects' lack of reasonable expectation.
4. For third-party datasets: verify the upstream lawful basis chain and obtain contractual warranties.
5. Assess Art. 6(4) compatibility where data is repurposed for AI training.
6. Legal counsel provides written opinion on training data lawfulness.

### Phase 4: Necessity and Proportionality (Days 23-27)

1. Document why AI/ML is necessary for the stated purpose (vs. rule-based or manual alternatives).
2. Assess data minimisation: can acceptable model performance be achieved with less personal data?
3. Evaluate privacy-enhancing alternatives: federated learning, differential privacy, synthetic data.
4. Confirm inference-time data collection is limited to what is necessary.
5. Assess retention periods for training data, model artefacts, and inference logs.
6. Verify data subject rights can be exercised effectively (access to AI logic, erasure from training data, correction of AI outputs).

### Phase 5: AI Risk Assessment (Days 28-37)

1. Identify AI-specific threat scenarios:
   - Training data extraction attacks
   - Membership inference attacks
   - Model inversion attacks
   - Attribute inference
   - Bias amplification and discriminatory outcomes
   - Output inaccuracy causing material harm
   - Re-identification through AI outputs
   - Concept drift causing unequal performance degradation
2. For each scenario, assess likelihood and severity using the risk matrix.
3. ML engineer conducts technical privacy testing:
   - Run membership inference attacks using shadow models
   - Test for training data extraction with canary values
   - Evaluate fairness metrics across demographic groups
   - Assess model confidence calibration
4. Document results in the AI risk register (format: AI-DPIA-[REF]-R[SEQ]).
5. Cross-reference with AI Act risk classification.

### Phase 6: Mitigation and Residual Risk (Days 38-43)

1. For each High or Very High risk, identify specific AI privacy measures:
   - Differential privacy (specify epsilon value and mechanism)
   - Model output perturbation (specify noise calibration)
   - Fairness constraints (specify metric and threshold)
   - Input/output filtering for PII
   - Human oversight mechanisms
   - Model monitoring and drift detection
2. Document implementation responsibility and timeline for each measure.
3. Reassess risk after mitigation to determine residual risk.
4. If residual risk remains High or Very High, flag for Art. 36 prior consultation.
5. DPO reviews all mitigation measures and residual risk assessments.

### Phase 7: Human Oversight Assessment (Days 44-47)

1. Assess whether the AI system involves solely automated decision-making under Art. 22.
2. If Art. 22 applies, verify that one of the Art. 22(2) exceptions is met.
3. Evaluate the effectiveness of human oversight per AI Act Art. 14:
   - Can the human reviewer meaningfully assess the AI recommendation?
   - Is sufficient time allocated for review?
   - Does the reviewer have expertise to identify errors?
   - Does the reviewer have authority to override?
   - Are automation bias countermeasures in place?
4. Document human oversight design and any deficiencies requiring remediation.

### Phase 8: Approval and Registration (Days 48-52)

1. DPO provides written advice on the AI DPIA findings.
2. AI system owner documents acceptance or departure from DPO advice with reasons.
3. Document data subject consultation per Art. 35(9) or justification for not consulting.
4. Senior management and AI governance board review and approve.
5. Register the AI DPIA in the central register with:
   - AI Act risk classification
   - Next review date (maximum 12 months or at next model retraining)
   - Linked conformity assessment reference (for high-risk AI)
6. If Art. 36 prior consultation is required, initiate Workflow 3.

## Workflow 3: AI DPIA Review Triggers

```
TRIGGER EVENT DETECTED
│
├─ Model retrained or fine-tuned with new data?
│  └─ YES → Review training data lawfulness. Reassess privacy risks. Update DPIA.
│
├─ New training data source added?
│  └─ YES → Complete lawful basis assessment for new source. Update DPIA.
│
├─ Model architecture changed (new version, different approach)?
│  └─ YES → Reassess technical risks (memorization, extraction). Update DPIA.
│
├─ New deployment context or use case?
│  └─ YES → Full DPIA review — proportionality and risk may differ by context.
│
├─ AI privacy incident (data extraction, bias incident, inaccurate output causing harm)?
│  └─ YES → Mandatory DPIA review. Reassess risk levels and mitigation effectiveness.
│
├─ Regulatory change (new EDPB guidance, AI Act implementing acts, DPA enforcement)?
│  └─ YES → Assess impact on DPIA analysis. Update if legal basis or risk assessment affected.
│
├─ Model performance drift detected?
│  └─ YES → Assess whether drift creates differential impact across groups. Update risk assessment.
│
├─ Scheduled review date reached (maximum 12 months)?
│  └─ YES → Conduct full DPIA review. Update all sections.
│
├─ AI Act conformity assessment updated?
│  └─ YES → Synchronise DPIA with conformity assessment findings.
│
└─ No trigger → Document monitoring check in DPIA register.
```

## Workflow 4: Training Data Lawfulness Assessment

```
FOR EACH TRAINING DATA SOURCE:
│
├─ Step 1: Classify the data source
│  ├─ First-party collected data → Assess original collection purpose compatibility
│  ├─ Licensed third-party dataset → Verify upstream lawful basis and contractual warranties
│  ├─ Public dataset (academic, government) → Assess whether personal data is present
│  ├─ Web-scraped data → Apply heightened scrutiny per EDPB Guidelines 04/2025
│  └─ User-contributed data → Verify consent scope covers AI training
│
├─ Step 2: Identify lawful basis under Art. 6(1)
│  ├─ Consent (Art. 6(1)(a)) → Verify AI training specified, freely given, withdrawable
│  ├─ Contract (Art. 6(1)(b)) → Verify AI training necessary for service
│  ├─ Legal obligation (Art. 6(1)(c)) → Identify the specific legal requirement
│  ├─ Legitimate interest (Art. 6(1)(f)) → Complete three-part balancing test (Workflow 5)
│  └─ No valid basis identified → DATA SOURCE CANNOT BE USED. Remove from training pipeline.
│
├─ Step 3: Check for Art. 9 special category data
│  ├─ Present → Identify Art. 9(2) condition. If none available, remove special category data.
│  └─ Not present → Continue.
│
├─ Step 4: Art. 6(4) compatibility assessment (if data repurposed)
│  ├─ Compatible → Document assessment.
│  └─ Not compatible → Obtain fresh consent or identify alternative lawful basis.
│
└─ Step 5: Document assessment in training data register.
```

## Workflow 5: Legitimate Interest Balancing Test for AI Training

```
THREE-PART TEST:
│
├─ Part 1: Legitimate Interest Identification
│  ├─ What is the specific interest pursued? (not generic "AI improvement")
│  ├─ Is the interest lawful?
│  ├─ Is the interest real and present (not hypothetical)?
│  └─ Is the interest sufficiently clearly articulated?
│
├─ Part 2: Necessity Assessment
│  ├─ Is processing this personal data necessary for the identified interest?
│  ├─ Could the interest be achieved without this personal data?
│  ├─ Could anonymised or synthetic data achieve the same result?
│  └─ Is the amount of personal data proportionate?
│
├─ Part 3: Balancing Test
│  ├─ What are the reasonable expectations of data subjects?
│  ├─ Was the data publicly available? (lower expectation, but does not eliminate rights)
│  ├─ What is the nature of the data? (sensitive data tips balance toward data subject)
│  ├─ What is the impact on data subjects? (consider AI-specific impacts)
│  ├─ What safeguards does the controller implement? (differential privacy, access controls)
│  ├─ Can data subjects effectively exercise their rights? (opt-out, erasure)
│  └─ EDPB position: large-scale web scraping for AI training faces high bar
│
├─ Outcome: Interest overrides → Document. Implement safeguards.
├─ Outcome: Data subject rights override → Do not process. Find alternative basis.
└─ Outcome: Marginal → Implement maximum safeguards. Consider alternative basis.
```
