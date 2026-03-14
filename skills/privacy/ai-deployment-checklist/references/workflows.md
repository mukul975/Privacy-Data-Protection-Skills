# AI System Pre-Deployment Privacy Checklist — Workflows

## Workflow 1: Pre-Deployment Compliance Gate Execution

### Trigger
- AI system development reaches deployment-ready stage
- Model version promoted to staging environment
- Product owner requests production deployment

### Steps
1. **Initiate Gate Review**: ML Engineering Lead creates deployment request ticket referencing system ID, model version, and target deployment date
2. **Gate 1 — Legal Basis and DPIA**: Privacy Engineer verifies lawful basis documentation, DPIA completion, and risk mitigation status for all personal data processing
3. **Gate 2 — Transparency**: Privacy Engineer confirms privacy notices updated with AI processing details, logic descriptions, and significance disclosures
4. **Gate 3 — Data Subject Rights**: Privacy Engineer validates access, explanation, human intervention, contestation, rectification, and erasure processes
5. **Gate 4 — Data Quality and Bias**: ML Engineer confirms training data documentation, bias testing results, fairness metrics, and data quality verification
6. **Gate 5 — Security**: Information Security Officer verifies encryption, access controls, audit logging, adversarial robustness, and model versioning
7. **Gate 6 — Monitoring**: ML Engineer confirms production monitoring dashboards, drift detection, bias monitoring, incident response plan, and retention enforcement
8. **Gate 7 — EU AI Act (if high-risk)**: Legal Counsel verifies Annex III classification, technical documentation, risk management system, conformity assessment, and EU database registration
9. **Sign-Off Collection**: Each gate owner records approval or blocker status
10. **DPO Final Review**: DPO reviews all gate outcomes and provides final approval or conditional approval with required remediations

### Output
- Completed pre-deployment compliance checklist with all sign-offs
- Deployment authorization or blocker list
- Conditional approval remediation plan (if applicable)

## Workflow 2: DPIA for AI System Deployment

### Trigger
- New AI system processing personal data reaches design phase
- Existing AI system undergoes significant model architecture change
- New data category added to an existing AI system

### Steps
1. **Screening**: Determine if DPIA is required (Art. 35(3) criteria: systematic evaluation/profiling, large-scale special categories, systematic monitoring)
2. **System Description**: Document the AI system purpose, data flows, processing operations, and recipients
3. **Necessity Assessment**: Evaluate whether processing is necessary and proportionate (Art. 35(7)(b))
4. **Risk Identification**: Identify risks to data subjects from AI processing (discrimination, loss of autonomy, profiling effects)
5. **Risk Evaluation**: Score each risk by severity and likelihood using Cerebrum AI Labs risk matrix
6. **Mitigation Measures**: Define technical and organisational measures for each high/critical risk
7. **Residual Risk Assessment**: Evaluate remaining risk after mitigations; if high, trigger Art. 36 prior consultation
8. **DPO Consultation**: DPO reviews and provides opinion on the DPIA per Art. 35(2)
9. **Approval**: Data controller approves DPIA and accepts residual risk
10. **Integration**: DPIA outcomes feed into deployment checklist Gate 1

### Output
- Signed DPIA document
- Risk treatment plan
- Prior consultation record (if applicable)

## Workflow 3: Post-Deployment Monitoring Setup

### Trigger
- AI system passes all pre-deployment gates and receives deployment authorization
- AI system deployed to production environment

### Steps
1. **Performance Monitoring**: Deploy accuracy, precision, recall, F1, and latency dashboards in Cerebrum AI Labs monitoring platform
2. **Drift Detection**: Configure data drift (input distribution shift) and concept drift (target distribution shift) alerts with statistical thresholds
3. **Bias Monitoring**: Set up continuous fairness metric tracking (disparate impact ratio, equalised odds, demographic parity) across protected attributes
4. **Incident Response Integration**: Connect AI monitoring alerts to Cerebrum AI Labs incident response workflow with escalation paths for privacy incidents
5. **Retraining Triggers**: Define automatic model retraining triggers based on drift detection thresholds and scheduled quarterly retraining cycle
6. **Retention Automation**: Configure automated deletion of inference logs (90 days operational, 6 months audit) and training data per retention schedule
7. **Audit Trail**: Verify all model invocations logged with timestamp, input hash, output, requesting user, and decision outcome
8. **Monitoring Review Schedule**: Set quarterly review calendar for monitoring configuration adequacy

### Output
- Monitoring dashboard URLs and alert configurations
- Drift detection threshold documentation
- Retention automation configuration
- Post-deployment monitoring sign-off

## Workflow 4: Deployment Blocker Resolution

### Trigger
- One or more pre-deployment gates result in "Blocked" status
- DPO final review identifies outstanding compliance gap

### Steps
1. **Blocker Documentation**: Gate owner documents specific non-compliance finding with evidence
2. **Remediation Plan**: ML Engineering Lead creates remediation plan with specific actions, owners, and deadlines
3. **Remediation Execution**: Assigned owners implement required fixes (update DPIA, add transparency disclosures, run additional bias tests, implement security controls)
4. **Verification**: Gate owner re-evaluates the specific blocked item and confirms remediation
5. **Re-submission**: ML Engineering Lead re-submits deployment request with remediation evidence
6. **Expedited Review**: DPO conducts targeted review of previously blocked items only
7. **Updated Sign-Off**: All gate owners confirm no new blockers introduced by remediation

### Output
- Updated compliance checklist with resolved blockers
- Remediation evidence package
- Revised deployment authorization
