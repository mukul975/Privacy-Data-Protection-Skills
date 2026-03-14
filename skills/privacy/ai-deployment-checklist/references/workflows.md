# AI System Pre-Deployment Privacy Checklist — Workflows

## Workflow 1: Pre-Deployment Privacy Gate Review

### Trigger
- AI system development reaches pre-production readiness
- Existing model updated with new training data or architecture changes
- Deployment target changes (new jurisdiction, new user population)

### Steps
1. **Initiate Gate Review**: ML Engineering Lead submits deployment request with system ID, model version, and target environment
2. **Gate 1 — Legal Basis and DPIA**: Privacy Counsel verifies lawful basis documentation; DPO confirms DPIA completion and risk mitigation status
3. **Gate 2 — Transparency**: Product team confirms privacy notice updated with AI processing details; meaningful logic explanation documented
4. **Gate 3 — Data Subject Rights**: Engineering confirms access, explanation, contestation, rectification, and erasure processes are operational
5. **Gate 4 — Data Quality and Bias**: ML team presents bias testing report; Responsible AI Lead reviews fairness metrics against thresholds (disparate impact ratio >= 0.8)
6. **Gate 5 — Security Controls**: InfoSec confirms encryption, access controls, audit logging, adversarial robustness testing, and model versioning
7. **Gate 6 — Monitoring Setup**: ML Ops confirms performance dashboards, drift detection, bias monitoring, incident response plan, and retention automation
8. **Gate 7 — AI Act (if applicable)**: For high-risk systems, verify risk classification, Annex IV documentation, conformity assessment, EU Declaration, and database registration
9. **Sign-Off Collation**: Collect approvals from ML Lead, DPO, InfoSec, Product Owner, and Legal (for high-risk)
10. **Deployment Decision**: All gates passed → approve deployment; any gate blocked → return to remediation

### Output
- Completed deployment checklist with evidence references
- Sign-off record with dates
- Deployment approval or block notice with remediation requirements

## Workflow 2: Gate Failure Remediation

### Trigger
- Any gate in the pre-deployment review returns a "Blocked" status

### Steps
1. **Issue Identification**: Gate reviewer documents specific deficiency and required remediation
2. **Remediation Assignment**: ML Engineering Lead assigns remediation to responsible team with deadline
3. **Fix Implementation**: Responsible team addresses deficiency (e.g., completes DPIA, updates privacy notice, runs additional bias tests)
4. **Evidence Submission**: Team submits evidence of remediation (updated document, test report, configuration change)
5. **Re-Review**: Original gate reviewer re-evaluates the specific gate
6. **Escalation**: If remediation cannot be completed within deployment timeline, escalate to Chief Privacy Officer for risk acceptance or deployment delay decision

### Output
- Remediation record with actions taken
- Updated gate status
- Escalation record (if applicable)

## Workflow 3: Post-Deployment Monitoring Activation

### Trigger
- AI system deployed to production after all gates passed

### Steps
1. **Monitoring Activation**: Confirm all monitoring dashboards are receiving live data (accuracy, latency, error rates, drift metrics)
2. **Bias Monitoring Baseline**: Capture initial production fairness metrics as baseline for drift detection
3. **Incident Response Readiness**: Verify incident response contacts are updated and on-call rotation includes AI incident expertise
4. **Retention Automation**: Confirm automated deletion schedules are active for inference logs and temporary data
5. **30-Day Post-Deployment Review**: Schedule review to assess initial production performance against pre-deployment benchmarks
6. **Ongoing Cadence**: Establish quarterly privacy review cadence for the deployed system

### Output
- Monitoring activation confirmation
- 30-day review scheduled
- Quarterly review calendar entry

## Workflow 4: Model Update Re-Certification

### Trigger
- Model retrained on new data
- Model architecture changed (fine-tuning, distillation, prompt engineering updates)
- Deployment scope expanded (new geography, new user segment, new use case)

### Steps
1. **Change Classification**: ML Engineering Lead classifies update as minor (parameter update, performance patch), moderate (new training data, feature changes), or major (new architecture, new use case, new jurisdiction)
2. **Gate Re-Run**:
   - Minor: Re-run Gates 4-6 (bias, security, monitoring)
   - Moderate: Re-run Gates 1-6 (full review except AI Act gate unless classification changes)
   - Major: Re-run all Gates 1-7 (full review including AI Act reassessment)
3. **DPIA Update**: If processing changes materially, update DPIA sections affected
4. **Sign-Off**: Collect approvals from roles required for the change classification level
5. **Deployment**: Deploy updated model with updated documentation

### Output
- Change classification record
- Updated checklist (partial or full based on classification)
- Updated DPIA (if applicable)
- Re-certification sign-off
