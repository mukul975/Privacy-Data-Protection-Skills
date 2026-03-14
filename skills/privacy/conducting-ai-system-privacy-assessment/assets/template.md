# AI System Privacy Assessment Report

## Reference: AIPA-QLH-2026-0002

| Field | Value |
|-------|-------|
| Organisation | QuantumLeap Health Technologies |
| AI System | TalentMatch AI Recruitment Screening System |
| Version | 1.0 |
| Date | 2026-02-20 |
| Next Review | 2026-08-20 (6 months — accelerated due to high-risk AI classification) |
| DPO | Dr. Elena Vasquez, CIPP/E, CIPM |
| AI Governance Lead | Dr. Aisha Patel, Head of AI Ethics |
| Assessment Framework | Combined GDPR Art. 35 DPIA + EU AI Act Conformity + NIST AI RMF |

---

## 1. AI System Description

TalentMatch is a machine learning system that screens job applications for QuantumLeap Health Technologies. The system processes CVs, cover letters, and application form responses to generate a suitability score (0-100) and a shortlist recommendation for each candidate. HR recruiters review all AI recommendations before making interview invitation decisions.

| Attribute | Detail |
|-----------|--------|
| Model type | Gradient boosted decision tree (XGBoost) with natural language processing feature extraction |
| Training data | 45,000 historical applications from 2019-2025 with labelled outcomes (hired/not hired) |
| Input data | CV text, cover letter text, application form responses (skills, qualifications, experience) |
| Output | Suitability score (0-100), shortlist recommendation (Recommend/Consider/Not Recommended), top-5 contributing factors |
| Processing volume | Approximately 12,000 applications per year across 180 open positions |
| Deployment | Hosted on AWS eu-west-1, integrated with SAP SuccessFactors recruitment module |
| Human oversight | All AI recommendations reviewed by HR recruiter before interview decision |

---

## 2. EU AI Act Classification

**Risk Category: High Risk — Annex III(4): Employment, worker management, and access to self-employment**

The AI Act classifies AI systems used for recruitment and selection of natural persons, including placing targeted job advertisements, analysing and filtering job applications, and evaluating candidates, as high-risk AI systems.

### Conformity Assessment Requirements

| Requirement | AI Act Reference | Status |
|-------------|-----------------|--------|
| Risk management system | Art. 9 | Implemented — integrated with this assessment |
| Data governance | Art. 10 | Implemented — training data quality procedures documented below |
| Technical documentation | Art. 11 | Implemented — model card and technical specification maintained |
| Record-keeping | Art. 12 | Implemented — all predictions logged with feature values and outcomes |
| Transparency to deployers | Art. 13 | Implemented — HR team provided with system capability documentation |
| Human oversight | Art. 14 | Implemented — HR recruiter reviews all recommendations |
| Accuracy, robustness, cybersecurity | Art. 15 | Implemented — quarterly model performance evaluation |
| EU database registration | Art. 71 | Pending — registration to be completed before deployment |

---

## 3. Training Data Assessment

### Data Source

| Attribute | Detail |
|-----------|--------|
| Source | QuantumLeap Health Technologies HR application database |
| Period | 2019-2025 |
| Volume | 45,000 applications |
| Data categories | CV text, cover letter text, application form responses, interview outcomes, hiring decisions |
| Special categories excluded | Disability status, ethnicity, religion, sexual orientation — explicitly excluded from feature extraction |
| Lawful basis for collection | Art. 6(1)(b) — necessary for entering into an employment contract |
| Lawful basis for AI training | Art. 6(4) compatible further processing — AI training directly serves the recruitment purpose |

### Art. 6(4) Compatibility Assessment

| Factor | Assessment |
|--------|-----------|
| Link between original and new purpose | Direct link — original purpose was recruitment; AI training purpose is to improve recruitment screening |
| Context of data collection | Employment application context; applicants reasonably expect their applications to inform the organisation's recruitment processes |
| Nature of data | Professional qualifications and experience — not special category data |
| Consequences for data subjects | Potential for discriminatory outcomes if model learns historical biases; mitigated by bias testing and human review |
| Safeguards | Pseudonymisation of training data (names, addresses replaced with tokens); bias testing; human review of all AI outputs |

### Data Quality Measures (AI Act Art. 10)

| Measure | Implementation |
|---------|---------------|
| Relevance | Features limited to job-relevant factors: skills, qualifications, experience, technical competencies |
| Representativeness | Training data demographic distribution compared to applicant pool; underrepresented groups identified and addressed through stratified sampling |
| Freedom from errors | Data cleaning pipeline removes duplicate applications, corrupted records, and incomplete entries |
| Completeness | 98.2% of applications have complete feature sets; 1.8% with missing fields handled through model-native missing value handling |

---

## 4. Art. 22 Automated Decision-Making Assessment

### Applicability

| Question | Answer |
|----------|--------|
| Does the AI make decisions about individuals? | Yes — generates shortlist recommendations for each applicant |
| Are decisions based solely on automated processing? | No — HR recruiter reviews all AI recommendations and makes the final interview decision |
| Do decisions produce legal or significant effects? | Yes — recruitment decisions significantly affect applicants' access to employment |

### Determination

Art. 22(1) does not directly apply because decisions are not solely automated — meaningful human involvement exists through HR recruiter review. However, the following safeguards are implemented as best practice and to ensure human involvement is genuinely meaningful:

| Safeguard | Implementation |
|-----------|---------------|
| Meaningful human review | HR recruiters receive the AI score, shortlist recommendation, and top-5 contributing factors. Recruiters are trained to exercise independent judgment and regularly override AI recommendations (current override rate: 18%). |
| Right to explanation | Candidates who request feedback receive information about the general assessment criteria (skills match, qualification relevance, experience alignment). Individual SHAP values are available to HR reviewers. |
| Right to contest | Candidates can request reconsideration through the careers portal. Reconsideration is conducted by a senior recruiter who independently reviews the application without reference to the AI score. |
| Anti-rubber-stamping | Monthly audit of recruiter decision patterns; alert triggered if any recruiter agrees with AI recommendation more than 95% of the time for three consecutive months. |

---

## 5. Algorithmic Bias Assessment

### Testing Methodology

Bias testing conducted on a holdout test set of 5,000 applications (collected January-December 2025) with voluntary demographic data provided by applicants for diversity monitoring purposes. Protected characteristics tested: gender, age group, ethnicity.

### Gender Bias Results

| Group | Positive Rate (Shortlisted) | Disparate Impact Ratio | Four-Fifths Rule |
|-------|-----------------------------|----------------------|-----------------|
| Male | 32.0% | 1.00 (reference) | Pass |
| Female | 28.0% | 0.875 | Pass (> 0.80) |
| Non-binary | 30.0% | 0.938 | Pass (> 0.80) |

**Demographic parity difference**: 0.04 (below 0.10 threshold)
**Assessment**: No disparate impact detected under four-fifths rule for gender.

### Age Group Bias Results

| Group | Positive Rate | Disparate Impact Ratio | Four-Fifths Rule |
|-------|--------------|----------------------|-----------------|
| 18-30 | 35.0% | 1.00 (reference) | Pass |
| 31-40 | 33.0% | 0.943 | Pass |
| 41-50 | 29.0% | 0.829 | Pass (> 0.80) |
| 51+ | 24.0% | 0.686 | **Fail (< 0.80)** |

**Assessment**: Disparate impact detected for applicants aged 51+. Investigation revealed that the model weighted "years since most recent qualification" as a significant feature, which correlates with age. Mitigation: feature replaced with "relevance of most recent qualification to role requirements" (binary: relevant/not relevant). After retraining, 51+ disparate impact ratio improved to 0.83 (passing four-fifths rule).

### Ongoing Monitoring

- Monthly bias metrics calculated on live predictions
- Automated alert if any group's disparate impact ratio falls below 0.80
- Quarterly bias review by AI Ethics Committee with full retest on updated holdout data
- Annual independent bias audit by external consultancy (scheduled: PwC, October 2026)

---

## 6. Risk Register

| Risk ID | Description | Likelihood | Severity | Level | Mitigation | Residual Level |
|---------|-------------|-----------|----------|-------|------------|---------------|
| R01 | Historical bias in training data perpetuating discriminatory patterns | Possible | Significant | High | Quarterly bias audits; adversarial debiasing; human review of all decisions | Medium |
| R02 | Proxy variable discrimination (university name, postcode, experience gaps correlating with protected characteristics) | Likely | Significant | High | Feature importance analysis; counterfactual fairness testing; university name removed; skills-based assessment only | Medium |
| R03 | Insufficient explanation of AI recommendations to candidates | Possible | Limited | Medium | SHAP values; top-5 factors; candidate feedback mechanism | Low |
| R04 | Model drift reducing accuracy and increasing bias over time | Possible | Significant | High | Monthly performance monitoring; quarterly bias retesting; automated drift detection alerts | Medium |
| R05 | Model inversion attack extracting training data from model API | Remote | Limited | Low | Rate limiting on API; no direct model access for end users; output limited to score and recommendation | Low |

---

## 7. NIST AI RMF MAP Function Outputs

| Subcategory | Assessment |
|-------------|-----------|
| MAP 1.1 Purpose | Screen job applications for QuantumLeap Health Technologies to improve recruitment efficiency while maintaining fairness and compliance |
| MAP 1.5 Stakeholders | Intended users: HR recruiters (6 staff). Affected individuals: job applicants (12,000/year). Other stakeholders: hiring managers, AI Ethics Committee, works council |
| MAP 1.6 Impacts | Positive: faster screening (5 days reduced to 2 days), consistent evaluation criteria. Negative: potential for discriminatory outcomes if bias undetected, candidate perception of dehumanised process |
| MAP 2.1 Knowledge limits | Model trained on QuantumLeap-specific data; not suitable for other organisations. Performance degrades for roles not well represented in training data (new role types require manual screening). |
| MAP 3.2 Risks | Bias amplification, proxy discrimination, model opacity, candidate trust erosion, regulatory non-compliance |
| MAP 3.5 Risk severity | Bias risks rated High (significant impact on employment access); opacity risks rated Medium |
| MAP 5.1 Engagement | Works council consulted on AI deployment; candidate survey on AI-assisted recruitment (n=500, 72% acceptance rate with transparency measures) |

---

## 8. Approvals

| Role | Name | Date |
|------|------|------|
| DPO | Dr. Elena Vasquez | 2026-02-20 |
| AI Governance Lead | Dr. Aisha Patel | 2026-02-20 |
| Head of HR | Marcus Chen | 2026-02-21 |
| CISO | Dr. James Okonkwo | 2026-02-21 |
| COO | Dr. Priya Sharma | 2026-02-22 |
