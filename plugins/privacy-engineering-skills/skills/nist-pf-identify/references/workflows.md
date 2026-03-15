# NIST PF IDENTIFY Function — Implementation Workflows

## Workflow 1: Data Processing Ecosystem Inventory (ID.DA-P1)

### Trigger
- New privacy program implementation
- Annual inventory refresh
- Organizational restructuring
- M&A activity

### Steps

1. **Identify Stakeholders**
   - Business unit leaders
   - IT system owners
   - Third-party relationship managers
   - Legal and compliance teams

2. **Distribute Discovery Questionnaires**
   - System/application name and owner
   - Types of personal data processed
   - Data subjects affected (customers, employees, prospects)
   - Processing purposes
   - Data sources and destinations
   - Retention periods
   - Security controls in place

3. **Conduct Technical Discovery**
   - Network traffic analysis for data flows
   - Database schema review for PII fields
   - API endpoint inventory
   - Cloud service audit (IaaS, PaaS, SaaS)

4. **Compile Data Processing Register**
   - Map all processing activities
   - Classify by risk tier (high/medium/low)
   - Assign data stewards
   - Document legal bases

5. **Validate and Approve**
   - Business unit review and sign-off
   - DPO/CPO review
   - Gap identification
   - Remediation planning

### Output
- Complete data processing inventory
- Risk-tiered classification
- Gap analysis report

## Workflow 2: Privacy Risk Assessment (ID.RA)

### Trigger
- New processing activity proposed
- Significant change to existing processing
- Privacy incident or near-miss
- Regulatory change
- Annual reassessment cycle

### Steps

1. **Scope Definition**
   - Identify the processing activity under assessment
   - Define assessment boundaries
   - Identify applicable regulations

2. **Data Action Mapping**
   - Document all data actions (collect, store, use, share, delete)
   - Map to NIST problematic data actions catalog
   - Identify data subjects at risk

3. **Likelihood Assessment**
   - Evaluate probability of each problematic data action occurring
   - Consider threat actors, vulnerabilities, and existing controls
   - Score on 1-5 scale (Rare to Almost Certain)

4. **Impact Assessment**
   - Evaluate consequences for data subjects if problematic action occurs
   - Consider physical, financial, psychological, and reputational harm
   - Score on 1-5 scale (Negligible to Severe)

5. **Risk Calculation and Prioritization**
   - Calculate risk score: Likelihood x Impact
   - Map to risk matrix (Low/Medium/High/Critical)
   - Rank risks by score

6. **Response Strategy Selection**
   - Mitigate: implement additional controls
   - Transfer: insurance, contractual allocation
   - Avoid: cease the processing activity
   - Accept: document rationale for acceptance

7. **Control Mapping**
   - Map selected controls to risks
   - Document expected risk reduction
   - Calculate residual risk

### Output
- Risk assessment report
- Risk register entries
- Control implementation plan
- Residual risk statement

## Workflow 3: Continuous Improvement (ID.IM)

### Trigger
- Quarterly review cycle
- Post-incident review
- Regulatory update
- Audit finding

### Steps

1. **Collect Improvement Inputs**
   - Incident lessons learned
   - Audit findings
   - Regulatory developments
   - Industry benchmarking
   - Stakeholder feedback

2. **Evaluate Current Risk Assessment Approach**
   - Review methodology effectiveness
   - Assess tool adequacy
   - Evaluate team capability
   - Check process efficiency

3. **Identify Improvements**
   - Process improvements
   - Tool enhancements
   - Training needs
   - Resource requirements

4. **Plan and Implement**
   - Prioritize improvements
   - Assign owners and deadlines
   - Allocate resources
   - Execute changes

5. **Verify Effectiveness**
   - Measure improvement impact
   - Update metrics
   - Report to governance body

### Output
- Improvement register
- Updated risk assessment methodology
- Training plan updates
- Budget requests
