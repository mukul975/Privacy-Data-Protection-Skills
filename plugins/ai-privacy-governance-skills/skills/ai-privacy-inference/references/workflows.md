# AI Privacy Inference and Derived Data — Workflows

## Workflow 1: Inference Classification and Registration

### Trigger
- New AI system generating inferences about individuals enters development
- Existing AI system adds new inference outputs
- Annual review of inference registry

### Steps
1. **Identify Inference Outputs**: ML Engineer documents all outputs that evaluate, predict, or classify characteristics of individual data subjects
2. **Classify Inference Type**: For each output, classify as observed data, derived data, inferred data, or aggregated data per the SKILL.md taxonomy
3. **Art. 9 Assessment**: Evaluate whether any inference predicts, estimates, or proxies for a special category characteristic (racial origin, political opinions, health, sexual orientation, religious beliefs)
4. **Profiling Level Assessment**: Determine whether inference constitutes (a) profiling only, (b) profiling informing human decision, or (c) solely automated decision with legal/significant effects
5. **Art. 22 Applicability**: If level (c), verify that an Art. 22(2) exception applies (contract, law, or explicit consent) and implement Art. 22(3) safeguards
6. **Register in Inference Registry**: Create entry with system ID, inference type, data subjects affected, input features, output format, accuracy metrics, retention period, lawful basis, DPIA reference
7. **DPO Review**: DPO validates classification, lawful basis, and safeguards
8. **Approval**: DPO approves inference for production or requests remediation

### Output
- Inference registry entry (one per inference type per AI system)
- Art. 22 assessment document (if applicable)
- DPO approval or remediation requirements

## Workflow 2: Art. 22 Safeguard Implementation

### Trigger
- AI system identified as making solely automated decisions with legal or similarly significant effects
- Existing system reclassified due to change in human oversight level

### Steps
1. **Human Intervention Mechanism**: Implement escalation pathway in customer-facing interface allowing data subjects to request human review of any automated decision
2. **Trained Human Reviewers**: Identify and train staff who can meaningfully review AI decisions (not rubber-stamp); document competence requirements and training completion
3. **Expression of Views**: Create form or channel for data subjects to provide additional context before human review
4. **Contestation Process**: Establish appeal pathway with independent review panel; define SLA for contestation resolution (Cerebrum AI Labs: 15 business days)
5. **Explanation Generation**: Implement SHAP or LIME explanation capability to generate individual explanations showing top factors influencing each decision
6. **Process Documentation**: Document the end-to-end Art. 22 safeguard process including roles, SLAs, escalation paths
7. **Testing**: Test end-to-end with sample cases — verify human review, explanation generation, and contestation flow all function correctly
8. **Privacy Notice Update**: Update Art. 13-14 privacy notices to disclose the existence of automated decision-making, logic involved, and safeguard rights

### Output
- Art. 22 safeguard implementation confirmation
- Trained reviewer roster
- Contestation process document
- Updated privacy notice

## Workflow 3: Inference Accuracy Monitoring

### Trigger
- AI system deployed to production with inference outputs
- Quarterly accuracy review cycle
- Data subject complaint about inference accuracy

### Steps
1. **Accuracy Metric Collection**: Retrieve current precision, recall, F1, and AUC metrics from production monitoring for each inference type
2. **Demographic Disaggregation**: Break down accuracy metrics by protected attribute groups (where data available) to identify disparate accuracy
3. **Confidence Calibration Check**: Verify that stated confidence scores (e.g., "78% churn probability") align with actual outcomes — compute expected calibration error
4. **Staleness Detection**: Identify inferences older than the configured staleness threshold (Cerebrum AI Labs: 90 days) that have not been refreshed
5. **Rectification Queue Review**: Process pending rectification requests — where data subjects have challenged an inference, verify whether underlying data correction requires inference regeneration
6. **Fairness Metric Review**: Compute disparate impact ratio across demographic groups; flag any group with ratio below 0.8
7. **Remediation**: For any metric outside acceptable range, escalate to ML Engineering for model investigation and potential retraining
8. **Report**: Generate quarterly inference accuracy report for DPO review

### Output
- Quarterly inference accuracy report with demographic disaggregation
- Fairness metric summary
- Remediation actions (if any)
- Updated inference registry accuracy fields

## Workflow 4: Data Subject Inference Access Request

### Trigger
- Data subject exercises Art. 15 right to access information about profiling and automated decision-making
- Data subject requests explanation of a specific AI decision

### Steps
1. **Request Validation**: Verify data subject identity per standard DSAR verification process
2. **Inference Inventory**: Query all AI systems in the inference registry for inferences associated with the data subject's identifier
3. **Compile Inference Summary**: For each inference, provide: inference type, date generated, input features used (categories, not raw values), output value, confidence score, purpose of processing
4. **Generate Explanation**: If request concerns a specific decision, generate SHAP-based individual explanation showing top 5 contributing features with directional impact
5. **Art. 15(1)(h) Information**: Provide meaningful information about the logic involved, significance, and envisaged consequences (using pre-approved explanation templates)
6. **Legal Review**: Privacy team reviews compiled response for completeness and accuracy
7. **Deliver Response**: Provide response to data subject within 30 days (Art. 12(3))
8. **Log**: Record request and response in DSAR tracking system

### Output
- Art. 15 response covering all inferences about the data subject
- Individual explanation document (if specific decision requested)
- DSAR tracking record

## Workflow 5: Inference Rectification and Objection

### Trigger
- Data subject challenges accuracy of an inference (Art. 16 rectification)
- Data subject objects to profiling (Art. 21 objection)
- Data subject contests an automated decision (Art. 22(3) contestation)

### Steps
1. **Request Classification**: Classify as rectification (inference is factually wrong), objection (data subject does not want to be profiled), or contestation (data subject disputes automated decision outcome)
2. **For Rectification**:
   a. Verify whether underlying input data is incorrect
   b. If input data incorrect: correct data, regenerate inference, notify data subject
   c. If input data correct but inference disputed: document data subject's position, flag inference as contested, escalate to ML team for review
3. **For Objection (Art. 21)**:
   a. Assess whether Cerebrum AI Labs can demonstrate compelling legitimate grounds overriding the data subject's interests
   b. If no compelling grounds: cease profiling for this data subject, delete existing inferences, add to exclusion list
   c. If compelling grounds exist: document reasoning and inform data subject of right to lodge complaint with supervisory authority
4. **For Contestation (Art. 22(3))**:
   a. Route to independent human reviewer (not the original system operator)
   b. Human reviewer assesses the decision considering data subject's additional input
   c. Reviewer can affirm, modify, or reverse the decision
   d. Notify data subject of outcome with reasoning
5. **Update Records**: Update inference registry, DSAR log, and any downstream systems affected by the change
6. **Retention**: Retain records of rectification/objection/contestation for 6 years per statute of limitations

### Output
- Rectification confirmation or reasoned refusal
- Objection processing record
- Contestation decision with reasoning
- Updated inference registry entries
