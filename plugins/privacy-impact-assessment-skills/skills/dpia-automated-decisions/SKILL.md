---
name: dpia-automated-decisions
description: >-
  Conducts a Data Protection Impact Assessment for automated decision-making
  and profiling systems under GDPR Article 35(3)(a), covering algorithmic
  transparency, meaningful human oversight, contestation mechanisms, and
  Art. 22 safeguards. Activate for DPIA automated decision, profiling DPIA,
  algorithmic impact assessment, Art. 35(3)(a), ADM risk assessment queries.
license: Apache-2.0
metadata:
  author: mukul975
  version: 1.0.0
  domain: privacy
  subdomain: privacy-impact-assessment
  tags:
    - dpia
    - automated-decisions
    - profiling
    - gdpr-article-35
    - algorithmic-transparency
  regulatory_frameworks:
    - GDPR
    - EU-AI-Act
---

# DPIA for Automated Decision-Making Systems

## Purpose

Conduct a DPIA specifically tailored to automated decision-making (ADM) and profiling systems that produce legal or similarly significant effects on individuals, as required by GDPR Article 35(3)(a).

## Prerequisites

- System documentation for the ADM/profiling system (algorithm design, training data, decision logic)
- Art. 35(3)(a) threshold confirmed: systematic and extensive evaluation of personal aspects based on automated processing, including profiling, on which decisions are based that produce legal effects or similarly significantly affect natural persons
- Data categories processed identified, including any Art. 9 special categories
- Existing Art. 22 safeguards documentation if available

## Workflow

### Step 1: System Description and Scope

Document the ADM system under assessment:

1. **System purpose**: Business objective and processing purpose
2. **Decision types**: What decisions the system makes or supports (credit scoring, insurance pricing, recruitment screening, fraud detection, content moderation)
3. **Processing scope**: Data categories used as inputs, volume of data subjects affected, geographic scope
4. **Automation level**: Fully automated (no human in loop), semi-automated (human in loop), or automated with human override capability
5. **Legal basis**: Art. 6(1) basis for the processing, and if Art. 22 applies, the Art. 22(2) exception relied upon (contract, EU/Member State law, explicit consent)

### Step 2: Necessity and Proportionality Assessment

Evaluate whether the automated processing is necessary and proportionate:

1. **Purpose limitation**: Confirm processing purpose is specific, explicit, and legitimate per Art. 5(1)(b)
2. **Data minimization**: Verify only data strictly necessary for the decision is processed per Art. 5(1)(c)
3. **Accuracy**: Assess input data quality and its impact on decision accuracy per Art. 5(1)(d)
4. **Less intrusive alternatives**: Document whether the decision could be made through less automated means
5. **Proportionality**: Balance the organizational benefit against the impact on individuals' rights and freedoms

### Step 3: Risk Identification

Identify risks specific to ADM systems:

1. **Discrimination risk**: Assess whether the system could produce discriminatory outcomes based on Art. 9 characteristics (race, ethnicity, political opinions, religion, health, sexual orientation)
2. **Opacity risk**: Evaluate whether the decision logic is explainable to affected individuals per Art. 13(2)(f) and Art. 14(2)(g)
3. **Accuracy risk**: Assess false positive and false negative rates and their consequences
4. **Data quality risk**: Evaluate whether training data reflects real-world populations without bias
5. **Feedback loop risk**: Assess whether the system creates self-reinforcing biases
6. **Scope creep risk**: Evaluate whether the system could be applied beyond its intended purpose
7. **Security risk**: Assess adversarial manipulation vectors (data poisoning, model extraction)

### Step 4: Art. 22 Compliance Assessment

If the system makes solely automated decisions with legal or similarly significant effects:

1. **Art. 22(1) prohibition check**: Confirm whether the default prohibition applies
2. **Art. 22(2) exception**: Document which exception permits the processing:
   - (a) Necessary for entering into or performance of a contract
   - (b) Authorized by EU or Member State law with suitable safeguards
   - (c) Based on explicit consent
3. **Art. 22(3) safeguards**: Verify implementation of mandatory safeguards:
   - Right to obtain human intervention from the controller
   - Right to express the data subject's point of view
   - Right to contest the decision
4. **Art. 22(4) special categories**: If Art. 9 data is processed, confirm explicit consent under Art. 9(2)(a) or substantial public interest under Art. 9(2)(g) with suitable safeguards

### Step 5: Transparency and Explainability

Assess transparency obligations:

1. **Pre-decision transparency**: Art. 13(2)(f) / Art. 14(2)(g) require providing meaningful information about the logic involved, significance, and envisaged consequences
2. **Logic explanation depth**: Document what level of explanation is provided:
   - General system functionality description
   - Key factors/features influencing decisions
   - Decision thresholds and their justification
   - Individual-specific explanation of a particular decision
3. **Recital 71 guidance**: Verify right to explanation is implemented as per Recital 71 (right to obtain an explanation of the decision reached after assessment)

### Step 6: Risk Mitigation Measures

Implement measures to mitigate identified risks:

1. **Bias testing**: Regular testing for discriminatory impact across protected characteristics
2. **Human oversight**: Define when and how human reviewers intervene
3. **Accuracy monitoring**: Ongoing performance monitoring with defined acceptable thresholds
4. **Audit trail**: Complete logging of inputs, model version, and outputs for each decision
5. **Data subject rights**: Clear process for individuals to exercise Art. 22(3) rights
6. **Regular review**: Periodic re-assessment schedule (at minimum annually)

### Step 7: Stakeholder Consultation

Consult required parties per Art. 35(9):

1. **DPO opinion**: Obtain DPO assessment per Art. 35(2)
2. **Data subjects**: Where appropriate, seek views of data subjects or their representatives per Art. 35(9)
3. **Technical experts**: Algorithm developers, data scientists, domain experts
4. **Legal counsel**: Assessment of applicable laws beyond GDPR (EU AI Act, sector-specific regulation)

### Step 8: Documentation and Outcome

Document the DPIA outcome:

1. **Risk matrix**: Residual risk rating after mitigation measures
2. **DPO recommendation**: Documented DPO opinion on whether processing can proceed
3. **Prior consultation**: If residual risk remains high, document decision to consult supervisory authority per Art. 36
4. **Review schedule**: Next mandatory review date and trigger events for early review

## Verification

- [ ] ADM system fully described with decision types, automation level, and data categories
- [ ] Art. 22(2) exception documented with Art. 22(3) safeguards implemented
- [ ] Discrimination risk assessed across Art. 9 protected characteristics
- [ ] Transparency obligations met per Art. 13(2)(f) / Art. 14(2)(g)
- [ ] Human intervention mechanism operational and tested
- [ ] Contestation process documented and accessible to data subjects
- [ ] DPO opinion obtained and documented
- [ ] Review schedule established with clear trigger events
