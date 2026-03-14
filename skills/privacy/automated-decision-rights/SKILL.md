---
name: automated-decision-rights
description: >-
  Manages GDPR Article 22 rights related to solely automated decision-making
  and profiling, including identification of automated decisions, meaningful
  human oversight implementation, logic explanation requirements, and
  contestation mechanisms. Activate for automated decision, profiling, Art. 22,
  algorithmic decision, AI decision queries.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-subject-rights
  tags: "automated-decision-making, profiling, gdpr-article-22, human-oversight, algorithmic-rights"
---

# Managing Automated Decision-Making and Profiling Rights

## Overview

GDPR Article 22 provides data subjects with the right not to be subject to decisions based solely on automated processing, including profiling, which produce legal effects concerning them or similarly significantly affect them. This skill covers the identification of automated decision-making, implementation of meaningful human intervention, explanation of logic, and contestation procedures.

## Legal Foundation

### GDPR Article 22 — Automated Individual Decision-Making, Including Profiling

1. **Art. 22(1)** — The data subject has the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning them or similarly significantly affects them.

2. **Art. 22(2)** — Exceptions: Art. 22(1) does not apply if the decision:
   - (a) is necessary for entering into, or performance of, a contract between the data subject and the controller
   - (b) is authorised by Union or Member State law which also lays down suitable measures to safeguard the data subject's rights and freedoms and legitimate interests
   - (c) is based on the data subject's explicit consent

3. **Art. 22(3)** — Where exceptions (a) or (c) apply, the controller must implement suitable measures to safeguard the data subject's rights and freedoms and legitimate interests, **at least** the right to:
   - Obtain **human intervention** on the part of the controller
   - **Express their point of view**
   - **Contest the decision**

4. **Art. 22(4)** — Decisions under Art. 22(2) shall not be based on special categories of data under Art. 9(1) unless Art. 9(2)(a) or (g) applies and suitable measures to safeguard the data subject's rights and freedoms and legitimate interests are in place.

### Definition of Profiling (Art. 4(4))

"Profiling" means any form of automated processing of personal data consisting of the use of personal data to evaluate certain personal aspects relating to a natural person, in particular to analyse or predict aspects concerning that natural person's performance at work, economic situation, health, personal preferences, interests, reliability, behaviour, location, or movements.

### EDPB Guidelines on Automated Decision-Making and Profiling (WP251 rev.01)

The Article 29 Working Party (now EDPB) Guidelines adopted on 6 February 2018 provide authoritative interpretation, distinguishing:
- **Simple profiling**: Automated processing to classify individuals (e.g., marketing segmentation) — may not trigger Art. 22 if no legal/significant effect.
- **Profiling-based decision**: Using profiling output to make a decision about an individual — triggers Art. 22 if solely automated with legal/significant effect.
- **Solely automated decision with profiling**: Full Art. 22 scope — e.g., automated credit scoring leading to loan rejection.

## Identifying Art. 22 Decisions

### Assessment Criteria

For each automated processing activity, assess:

1. **Is the decision solely automated?** No meaningful human intervention in the decision process. Per WP251 rev.01, human involvement must be more than a rubber stamp — the reviewer must have authority, competence, and genuinely consider the automated output before reaching their own decision.

2. **Does the decision produce legal effects?** Examples: denial of a loan application, termination of a contract, refusal of social security benefit, denial of entry to a country.

3. **Does the decision similarly significantly affect the data subject?** Examples: automatic rejection of an online credit application, automated recruitment screening that excludes candidates, differential pricing that materially affects purchasing power, automated insurance risk assessment resulting in premium increases exceeding 20%.

### Meridian Analytics Ltd — Automated Processing Inventory

| Processing Activity | Solely Automated | Legal/Significant Effect | Art. 22 Applies | Exception |
|---------------------|-----------------|--------------------------|-----------------|-----------|
| Client risk scoring for onboarding | Yes | Yes — determines service access | Yes | Art. 22(2)(a) — Necessary for contract |
| Anomaly detection in usage patterns | Yes | No — triggers human review only | No | N/A |
| Automated invoice processing | Yes | No — administrative function | No | N/A |
| Marketing segment assignment | Yes | No — does not produce legal or similarly significant effects | No | N/A |
| Fraud probability scoring | Yes | Yes — may result in account suspension | Yes | Art. 22(2)(a) — Necessary for contract |

## Human Intervention Requirements

### Meaningful Human Oversight Standard

Per WP251 rev.01, paragraph 21, human intervention must meet all of the following criteria:

1. **Authority**: The reviewer has the organisational authority to alter or override the automated decision.
2. **Competence**: The reviewer has the technical understanding and domain knowledge to evaluate the automated output, including awareness of the model's limitations and error rates.
3. **Genuine consideration**: The reviewer actually analyses the automated output and the data subject's specific circumstances, rather than routinely endorsing the automated recommendation.

### Implementation at Meridian Analytics Ltd

For each Art. 22 decision:

1. **Designated reviewers**: Assign trained staff (minimum 2 per decision type) with explicit authority to override automated outcomes.
2. **Review interface**: Provide a dashboard displaying:
   - The automated decision and confidence score
   - Key input factors and their contribution to the decision
   - Historical accuracy rate of the model for similar cases
   - Data subject's profile summary
   - Override history for similar decisions
3. **Review SLA**: All Art. 22 decisions must be reviewed within 48 hours of the automated output.
4. **Override documentation**: Every override must be documented with the reviewer's name, date, reasoning, and alternative outcome.
5. **Quarterly audit**: Review override rates, reviewer engagement metrics, and outcome distributions to verify meaningful human involvement.

## Logic Explanation Requirements

### What Must Be Explained (Art. 15(1)(h))

When a data subject exercises their right of access regarding automated decision-making, the controller must provide:

1. **The existence of the automated decision**: Confirm that automated decision-making, including profiling, is taking place.
2. **Meaningful information about the logic involved**: Not the source code or algorithm weights, but a functional description that a non-technical person can understand:
   - What data inputs are used
   - How those inputs are weighted or combined
   - What thresholds or rules determine the outcome
   - General accuracy and error rates
3. **The significance and envisaged consequences**: What the decision means for the data subject in practical terms.

### Example Logic Explanation — Client Risk Scoring

> "Meridian Analytics Ltd uses an automated risk scoring system to assess new client applications. The system evaluates the following factors:
>
> - **Company registration data**: Age of the company, registered jurisdiction, and filing history (weighted approximately 30% of the overall score).
> - **Financial indicators**: Reported revenue, credit reference agency data, and payment history from public sources (weighted approximately 40%).
> - **Industry risk classification**: The sector in which the applicant operates, mapped against a regulatory risk index (weighted approximately 20%).
> - **Behavioural signals**: Patterns in the application process itself, such as consistency of provided information (weighted approximately 10%).
>
> The system produces a risk score from 0 to 100. Applications scoring below 35 are automatically flagged for enhanced due diligence review by a human analyst. Applications scoring below 15 are automatically declined, subject to review by a Senior Compliance Analyst within 48 hours.
>
> This system has an overall accuracy rate of 91.3% based on quarterly validation against actual client outcomes. The false positive rate (incorrectly flagging low-risk clients as high-risk) is 6.2%, and the false negative rate (failing to flag genuinely high-risk clients) is 2.5%.
>
> If your application is declined or flagged, you have the right to request human review, express your point of view, and contest the decision."

## Contestation Mechanism

### Step 1: Receive Contestation

1. Log with reference ADM-YYYY-NNNN.
2. Record: the automated decision contested, the data subject's grounds for contestation, and any additional information provided.

### Step 2: Assign Human Reviewer

1. Assign a reviewer who was NOT involved in the original automated decision.
2. The reviewer must have authority, competence, and independence.
3. Provide the reviewer with:
   - The original automated decision and its basis
   - The data subject's contestation and supporting information
   - Relevant data inputs and model outputs
   - Historical precedents for similar contestations

### Step 3: Review and Decide

1. The reviewer must genuinely reconsider the decision on its merits.
2. The reviewer may:
   - **Uphold** the original automated decision (with documented reasoning)
   - **Modify** the decision (partially or fully in the data subject's favour)
   - **Overturn** the decision entirely
3. Document the review outcome with full reasoning.

### Step 4: Communicate the Outcome

1. Notify the data subject within 30 calendar days of the contestation.
2. The notification must include:
   - The outcome of the review
   - The reasoning behind the decision
   - If the decision is upheld: the data subject's right to lodge a complaint with the supervisory authority (Art. 77) and seek a judicial remedy (Art. 79)
   - If the decision is modified or overturned: the practical next steps

### Step 5: Systemic Review

1. Log the contestation outcome for model monitoring purposes.
2. If contestation rates exceed 10% for any decision type in a quarter, trigger a model review.
3. If overturn rates exceed 15%, escalate to the Data Protection Officer for assessment of whether the model requires retraining or decommissioning.
