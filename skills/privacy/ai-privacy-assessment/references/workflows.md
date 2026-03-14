# AI System Privacy Assessment Workflows

## Workflow 1: AI System Classification and Screening

```
START: AI system identified for privacy assessment
│
├─ Step 1: Determine AI Act risk category
│  ├─ Is the AI system on the Art. 5 prohibited list?
│  │  ├─ YES → System cannot be deployed. Stop.
│  │  └─ NO → Continue.
│  ├─ Does the AI system fall within Annex III high-risk categories?
│  │  ├─ YES → Classify as high-risk. Full conformity assessment + DPIA required.
│  │  └─ NO → Continue.
│  ├─ Does Art. 50 apply (chatbot, deep fake, emotion recognition)?
│  │  ├─ YES → Classify as limited-risk. Transparency obligations apply.
│  │  └─ NO → Classify as minimal-risk.
│  └─ Document AI Act classification.
│
├─ Step 2: Determine GDPR DPIA requirement
│  ├─ Does the AI system involve evaluation or scoring (WP248 C1)?
│  ├─ Does the AI system involve automated decision-making (WP248 C2)?
│  ├─ Does the AI system involve systematic monitoring (WP248 C3)?
│  ├─ Does the AI system involve innovative technology (WP248 C8)?
│  └─ If 2+ criteria met → DPIA required. Proceed to Workflow 2.
│
├─ Step 3: Determine Art. 22 applicability
│  ├─ Does the AI system make decisions about individuals?
│  ├─ Are decisions based solely on automated processing?
│  ├─ Do decisions produce legal or similarly significant effects?
│  └─ If all yes → Art. 22 applies. Include in assessment.
│
└─ END: Document screening outcome and proceed to full assessment.
```

## Workflow 2: Training Data Lawfulness Assessment

### Process
1. Inventory all training data sources with provenance documentation.
2. For each data source, identify:
   - Original collection purpose and privacy notice provided to data subjects
   - Lawful basis under Art. 6(1) for original collection
   - Whether AI training was disclosed as a purpose at collection time
3. If AI training was not an original purpose:
   - Conduct Art. 6(4) compatibility assessment considering: link between original and new purpose, context of collection, nature of data, consequences for data subjects, safeguards.
   - If compatible → document compatibility assessment.
   - If not compatible → obtain new lawful basis (e.g., consent for AI training) or use anonymised data.
4. If special category data is in training data:
   - Identify applicable Art. 9(2) exemption.
   - If relying on Art. 9(2)(j) scientific research: verify Art. 89(1) safeguards are in place (data minimisation, pseudonymisation where possible).
5. Document training data assessment in the DPIA.

## Workflow 3: Algorithmic Bias Testing

### Pre-deployment Testing
1. Define protected characteristics for bias testing based on:
   - EU Charter of Fundamental Rights Art. 21 (non-discrimination)
   - Applicable national equality legislation (e.g., Equality Act 2010, AGG Germany)
   - Context-specific protected groups
2. Prepare a bias test dataset that is:
   - Representative of the deployment population
   - Labeled with protected characteristics (or proxy variables)
   - Sufficiently large for statistical significance per group
3. Run the AI model on the bias test dataset.
4. Calculate fairness metrics per protected group:
   - Demographic parity difference
   - Equalized odds difference
   - Predictive parity ratio
   - Disparate impact ratio (four-fifths rule threshold: 0.80)
5. If disparate impact detected (ratio < 0.80 for any group):
   - Document the disparity with confidence intervals
   - Assess whether the disparity is justified by a legitimate factor
   - If not justified: implement bias mitigation (resampling, re-weighting, adversarial debiasing, threshold adjustment)
   - Re-test after mitigation
6. Document all bias testing methodology, results, and remediation in the DPIA.

### Post-deployment Monitoring
1. Collect outcome data disaggregated by protected characteristics (where lawful and proportionate).
2. Calculate ongoing fairness metrics monthly.
3. Set automated alerts for fairness metric drift exceeding defined thresholds.
4. Conduct quarterly bias review with human review of edge cases.
5. Update DPIA when bias testing reveals new risks.

## Workflow 4: Art. 22 Compliance Implementation

```
Art. 22 applicability confirmed
│
├─ Identify applicable Art. 22(2) exception:
│  ├─ Art. 22(2)(a): Necessary for contract → Document necessity analysis.
│  ├─ Art. 22(2)(b): Authorised by law → Identify the authorising provision.
│  └─ Art. 22(2)(c): Explicit consent → Obtain and document explicit consent.
│
├─ Implement Art. 22(3) safeguards:
│  ├─ Human intervention mechanism:
│  │  └─ Designate trained human reviewers who can override AI decisions.
│  │  └─ Ensure reviewers have authority and capability to deviate from AI output.
│  │  └─ Document the human review process and criteria for override.
│  ├─ Right to express point of view:
│  │  └─ Provide mechanism for data subjects to submit additional information.
│  │  └─ Ensure submissions are considered in the decision review.
│  ├─ Right to contest:
│  │  └─ Provide clear process for data subjects to contest AI decisions.
│  │  └─ Ensure contested decisions are reviewed by a human with authority to change the outcome.
│  └─ Meaningful information about logic:
│     └─ Provide explanation of the main factors in the decision.
│     └─ Provide the relative weight of factors (feature importance).
│     └─ Provide counterfactual explanations where feasible.
│
├─ If special category data involved (Art. 22(4)):
│  └─ Only Art. 9(2)(a) explicit consent or Art. 9(2)(g) substantial public interest applies.
│  └─ Implement suitable measures to safeguard data subject rights and freedoms.
│
└─ Document all Art. 22 compliance measures in the DPIA.
```

## Workflow 5: Combined DPIA + AI Act Conformity Report

1. Compile the following sections into a single assessment document:
   - AI system description (purpose, design, training methodology, deployment context)
   - AI Act classification and compliance requirements
   - GDPR processing assessment (lawful basis for each processing stage)
   - Training data lawfulness assessment
   - Art. 22 analysis and safeguards
   - Algorithmic bias testing results
   - NIST AI RMF MAP function outputs
   - Risk register (GDPR privacy risks + AI-specific risks)
   - Mitigation measures (privacy controls + AI governance controls)
   - Residual risk assessment
2. Submit to DPO for Art. 35(2) advice.
3. Submit to AI governance committee for AI Act compliance review.
4. If high-risk AI: prepare conformity declaration per AI Act Art. 47.
5. Register in the EU AI database per AI Act Art. 71 (for high-risk AI).
6. Schedule review: minimum annually or upon model retraining, data drift, or regulatory change.
