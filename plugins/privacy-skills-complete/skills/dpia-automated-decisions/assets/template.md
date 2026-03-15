# DPIA Report: Automated Decision-Making System

**Organization**: Meridian Analytics Ltd
**System**: Credit Risk Scorer v3.2
**DPIA Reference**: DPIA-ADM-2026-003
**Assessment Date**: 2026-03-14
**DPO**: Elena Vasquez
**System Owner**: James Thornton, Chief Data Officer

---

## 1. System Description

| Field | Detail |
|-------|--------|
| System name | Meridian Credit Risk Scorer v3.2 |
| Purpose | Automated credit risk assessment for consumer loan applications |
| Decision type | Credit approval/denial with risk-based pricing tiers |
| Automation level | Fully automated (Art. 22(1) applies) |
| Legal basis | Art. 6(1)(b) contract performance; Art. 22(2)(a) necessary for contract |
| Data subjects | Consumer loan applicants (~45,000/year) |
| Geographic scope | United Kingdom and Republic of Ireland |
| Go-live date | Originally deployed 2024-06-15, v3.2 update 2026-01-20 |

## 2. Data Categories Processed

| Category | Source | Art. 9 Special Category |
|----------|--------|------------------------|
| Full name | Application form | No |
| Date of birth | Application form | No |
| Residential address (3 years) | Application form | No |
| Employment history (5 years) | Application form + employer verification | No |
| Annual income | Payslips, P60, employer verification | No |
| Credit history | Experian credit bureau (processor agreement dated 2025-04-10) | No |
| Existing debt obligations | Credit bureau + self-declaration | No |
| Bank account transaction summary | Open Banking API (consent-based) | No |

**Special category data**: None processed directly. Proxy variable analysis conducted to ensure no indirect processing of Art. 9 characteristics.

## 3. Art. 22 Compliance

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Art. 22(2)(a) exception: necessary for contract | Implemented | Credit decision is prerequisite to loan contract; pre-contractual step |
| Art. 22(3): Right to human intervention | Implemented | Applicants can request manual review via online portal or phone (0800-555-0199) within 30 days |
| Art. 22(3): Right to express views | Implemented | Review request form includes free-text field for applicant to provide additional context |
| Art. 22(3): Right to contest | Implemented | Formal contestation process with 14-day response SLA, qualified credit analyst review |
| Art. 22(4): No special categories | Confirmed | No Art. 9 data used as input features |

## 4. Transparency Measures

### Privacy Notice (Art. 13(2)(f))

The loan application privacy notice (last updated 2026-01-15) includes:
- Statement that automated decision-making is used for credit assessment
- Description of key factors: income-to-debt ratio, credit history length, payment history, employment stability
- Description of decision outcomes: approval with tier assignment (Tier 1-4 interest rates) or decline
- Instructions on exercising Art. 22(3) rights

### Logic Explanation

| Layer | Content | Access Method |
|-------|---------|---------------|
| Layer 1 | "Your application was assessed using an automated credit scoring system" | Decision notification email |
| Layer 2 | Top 5 factors that influenced the decision with directional impact (positive/negative) | Online applicant portal |
| Layer 3 | Full SHAP-value based individual explanation with feature contributions | Available on request within 30 days, delivered by credit analyst |

## 5. Bias Assessment Results

### Four-Fifths Rule Analysis (Q4 2025 Production Data, n=11,247)

| Protected Attribute | Group | Approval Rate | Disparate Impact Ratio | Result |
|--------------------|-------|---------------|----------------------|--------|
| Gender | Male | 72.1% | 1.00 (reference) | -- |
| Gender | Female | 68.4% | 0.95 | PASS |
| Age group | 25-34 | 78.2% | 1.00 (reference) | -- |
| Age group | 35-44 | 75.1% | 0.96 | PASS |
| Age group | 45-54 | 68.3% | 0.87 | PASS |
| Age group | 55-64 | 61.7% | 0.79 | FAIL |
| Age group | 65+ | 53.2% | 0.68 | FAIL |
| Ethnicity | White | 74.0% | 1.00 (reference) | -- |
| Ethnicity | Asian | 71.3% | 0.96 | PASS |
| Ethnicity | Black | 63.1% | 0.85 | PASS |
| Ethnicity | Hispanic | 65.8% | 0.89 | PASS |

### Bias Findings and Remediation

**Finding 1**: Age groups 55-64 (0.79) and 65+ (0.68) fail the four-fifths rule. Investigation revealed that shorter remaining employment duration and lower projected income growth were driving lower scores for older applicants.

**Remediation**: Implemented age-fairness constraint in v3.2 model training. Employment duration capped at 10 years relevance window. Projected income growth factor removed. Post-remediation testing shows 55-64 at 0.84 (PASS) and 65+ at 0.76 (marginal improvement, monitoring continues).

**Finding 2**: Ethnicity ratios pass but Black applicant rate (0.85) is close to threshold. Root cause: postal code correlation with credit bureau data density.

**Remediation**: Postal code removed as direct feature. Credit bureau data supplemented with Open Banking data to reduce information asymmetry. Next quarter assessment will validate improvement.

## 6. Risk Assessment

| Risk ID | Description | Likelihood | Impact | Inherent Score | Mitigations | Residual Score | Level |
|---------|-------------|-----------|--------|----------------|-------------|----------------|-------|
| R1 | Age discrimination in credit decisions | 4 | 5 | 20 | Age-fairness constraint, employment cap, bias monitoring | 5.6 | Medium |
| R2 | Ethnic bias from proxy variables | 3 | 5 | 15 | Proxy detection, postal code removal, data supplementation | 4.5 | Medium |
| R3 | Opacity of decision logic to applicants | 3 | 3 | 9 | SHAP explanations, layered transparency, analyst support | 2.7 | Low |
| R4 | Feedback loop amplifying historical bias | 3 | 4 | 12 | Annual training data refresh, external validation dataset | 6.0 | Medium |
| R5 | Adversarial manipulation of inputs | 2 | 3 | 6 | Input validation, anomaly detection, credit bureau verification | 2.4 | Low |

**Overall Residual Risk Level**: Medium

## 7. DPO Opinion

The DPO has reviewed this DPIA and provides the following opinion per Art. 35(2):

> The Credit Risk Scorer v3.2 implements adequate Art. 22(3) safeguards including human intervention, expression of views, and contestation mechanisms. The bias assessment reveals concerns with age-related disparate impact that are being addressed through model retraining. The transparency measures meet Art. 13(2)(f) requirements through a layered approach. I recommend proceeding with processing subject to (1) quarterly bias monitoring with automatic suspension if any group falls below 0.70 disparate impact ratio, (2) completion of age-fairness remediation validation by Q2 2026, and (3) annual full DPIA review.
>
> -- Elena Vasquez, DPO, 2026-03-14

## 8. Prior Consultation Assessment

Art. 36 prior consultation is **not required**. Residual risk level is medium after mitigation measures. The DPO confirms that sufficient measures have been identified to reduce risk to an acceptable level.

## 9. Review Schedule

| Review Type | Frequency | Next Due | Owner |
|-------------|-----------|----------|-------|
| Bias monitoring (four-fifths rule) | Quarterly | 2026-06-14 | Data Science Team |
| Contestation outcome analysis | Monthly | 2026-04-14 | Credit Operations |
| Model performance review | Semi-annually | 2026-09-14 | Data Science Team |
| Full DPIA review | Annually | 2027-03-14 | DPO + System Owner |
| Trigger review | On model update, regulatory change, or significant bias finding | As needed | DPO |

---

**Approved by**: Elena Vasquez (DPO), James Thornton (CDO)
**Date**: 2026-03-14
