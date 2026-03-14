# DPIA for Automated Decisions - Detailed Workflows

## Workflow 1: ADM System Classification

### Determining if Art. 22 Applies

1. **Is the decision based solely on automated processing?**
   - If a human meaningfully reviews and can override the automated output before it takes effect, Art. 22 may not apply
   - Per WP251rev.01: rubber-stamping or routinely applying automated recommendations without genuine assessment counts as solely automated
   - Document the nature and extent of human involvement

2. **Does the processing include profiling?**
   - Profiling = automated processing to evaluate personal aspects (Art. 4(4))
   - Not all ADM involves profiling; not all profiling involves ADM
   - Example: automated credit scoring based on income data = profiling + ADM
   - Example: automated sorting of email = automated processing but not profiling

3. **Does the decision produce legal effects or similarly significantly affect?**
   - Legal effects: contractual rights, legal status, access to statutory benefits
   - Similarly significant: per WP251, effects comparable in gravity to legal effects
   - Examples qualifying: credit denial, insurance premium increase, recruitment rejection, benefit denial
   - Examples not qualifying: personalized advertising (generally), music recommendations

4. **Classification outcome**:
   - Art. 22 applies: Implement full Art. 22(2)-(4) framework
   - Art. 22 does not apply but Art. 35(3)(a) triggered: DPIA required but Art. 22 safeguards advisory
   - Neither applies: Standard processing, DPIA not mandatory (but may be best practice)

## Workflow 2: Bias and Discrimination Assessment

### Pre-Deployment Bias Testing

1. **Training data analysis**:
   - Document data sources and collection methodology
   - Analyze representation of demographic groups
   - Check for historical bias in outcome labels
   - Assess proxy variables that may correlate with protected characteristics

2. **Disparate impact testing**:
   - Calculate decision rates across protected groups (gender, ethnicity, age, disability)
   - Apply four-fifths (80%) rule: if the selection rate for a protected group is less than 80% of the rate for the group with the highest rate, adverse impact may exist
   - Document any disparities exceeding thresholds

3. **Individual fairness testing**:
   - Verify that similar individuals receive similar decisions
   - Test with counterfactual examples (change protected attribute, observe decision change)
   - Document sensitivity of decisions to protected characteristics

4. **Intersectional analysis**:
   - Test for bias at intersections of protected characteristics (e.g., women of color, elderly disabled persons)
   - Single-axis analysis may miss intersectional discrimination

### Post-Deployment Monitoring

1. **Outcome monitoring**:
   - Track actual outcomes by demographic group
   - Compare predicted outcomes to actual outcomes for systematic errors
   - Monitor for concept drift (changes in data distribution over time)

2. **Feedback loop detection**:
   - Identify whether decisions influence future training data
   - Assess whether the system amplifies existing biases
   - Implement mechanisms to break harmful feedback loops

3. **Complaint analysis**:
   - Track Art. 22(3) contestation requests by demographic group
   - Analyze patterns in overturned decisions
   - Use complaint data to identify systematic issues

## Workflow 3: Human Oversight Implementation

### Designing Meaningful Human Intervention

1. **Define intervention points**:
   - Pre-decision review: human reviews automated recommendation before communicating to subject
   - Post-decision review: human reviews automated decision within defined timeframe, subject notified of right to request review
   - Exception-based review: human reviews cases flagged by confidence threshold or risk indicators

2. **Reviewer qualification**:
   - Define required domain expertise for reviewers
   - Training program on bias awareness, system limitations, and override procedures
   - Regular competency assessment

3. **Override authority**:
   - Document who has authority to override automated decisions
   - Define criteria and process for overrides
   - Track override rates and reasons for quality assurance

4. **Time constraints**:
   - Maximum time from automated decision to human review
   - Maximum time from contestation request to human review
   - Escalation process when timeframes are at risk

### Contestation Process

1. **Access**: Data subject requests explanation of automated decision via designated channel
2. **Explanation**: Controller provides meaningful information about logic involved within 30 days per Art. 12(3)
3. **Expression of views**: Data subject submits their perspective and any relevant information
4. **Human review**: Qualified reviewer examines the case, considers subject's input, and makes independent assessment
5. **Outcome**: Revised decision communicated to subject with reasoning
6. **Documentation**: Complete audit trail of contestation process retained

## Workflow 4: Transparency Documentation

### Pre-Decision Information (Art. 13/14 Compliance)

1. **Privacy notice content for ADM**:
   - Existence of automated decision-making including profiling
   - Meaningful information about the logic involved
   - Significance and envisaged consequences for the data subject
   - How to exercise Art. 22(3) rights

2. **Layered approach**:
   - Layer 1 (at decision point): Brief statement that an automated decision has been/will be made, with link to full explanation
   - Layer 2 (full notice): General system description, key factors, decision range, individual rights
   - Layer 3 (on request): Individual-specific explanation of a particular decision

3. **Technical documentation** (for internal records and regulator requests):
   - Algorithm type and version
   - Training data description and provenance
   - Feature importance rankings
   - Performance metrics (accuracy, precision, recall by demographic group)
   - Known limitations and failure modes

## Workflow 5: DPIA Outcome Decision Tree

1. **Residual risk assessment**:
   - After all mitigation measures, rate residual risk: low, medium, high, very high
   - Consider both likelihood and severity of harm to data subjects

2. **Decision pathways**:
   - **Low residual risk**: Processing may proceed. Document DPIA and review schedule.
   - **Medium residual risk**: Processing may proceed with enhanced monitoring. Increase review frequency.
   - **High residual risk**: Consult DPO for recommendation. May proceed if DPO approves with additional safeguards.
   - **Very high residual risk**: Prior consultation with supervisory authority required per Art. 36. Do not proceed until consultation complete.

3. **Art. 36 prior consultation trigger**:
   - Controller unable to find sufficient measures to reduce risk to acceptable level
   - Must provide SA with: DPIA assessment, controller/processor details, measures and safeguards, DPO contact
   - SA has up to 8 weeks to respond (extendable by 6 weeks for complex cases)
