---
name: ai-automated-decisions
description: >-
  Implements GDPR Art. 22 automated decision-making and AI Act Art. 14 human
  oversight requirements for AI systems. Covers identification of solely
  automated decisions, meaningful human intervention design, logic explanation
  mechanisms, and contestation procedures. Keywords: Art. 22, automated
  decision, human oversight, AI Act, profiling, contestation.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: ai-privacy-governance
  tags: "automated-decisions, art-22, human-oversight, ai-act, profiling, contestation"
---

# AI Automated Decision-Making and Human Oversight

## Overview

GDPR Article 22 grants data subjects the right not to be subject to decisions based solely on automated processing, including profiling, which produce legal or similarly significant effects. The EU AI Act Art. 14 supplements this with specific human oversight design requirements for high-risk AI systems. Together, these provisions require organisations to identify when AI systems make consequential decisions, ensure meaningful human intervention where required, provide explainable decision logic, and offer effective contestation mechanisms. This skill provides the complete framework for Art. 22 compliance and AI Act human oversight implementation.

## Art. 22 Scope and Applicability

### Three Cumulative Conditions

Art. 22(1) is triggered only when all three conditions are met:

| Condition | Requirement | AI Application |
|-----------|-------------|----------------|
| 1. Decision | A decision is made (not merely a recommendation or input) | The AI output directly determines an outcome — no genuine human decision-making step between AI output and action |
| 2. Solely automated | Based solely on automated processing including profiling | No meaningful human intervention in the decision chain; rubber-stamping does not constitute human intervention |
| 3. Legal/significant effects | Produces legal effects or similarly significantly affects the data subject | Affects legal rights, contractual status, access to services, financial outcomes, or other significant life impacts |

### "Solely Automated" — EDPB Interpretation

The EDPB Guidelines 06/2020 on automated decision-making clarify:

- **Solely automated** means no meaningful human involvement in the decision process
- A human who merely confirms an AI recommendation without genuine assessment is not providing meaningful intervention
- **Meaningful human intervention** requires:
  - The reviewer has authority and competence to change the decision
  - The reviewer has access to all relevant information
  - Sufficient time is allocated for genuine consideration
  - The reviewer routinely exercises independent judgment (not just confirming AI output)
  - Override capability is actually used in practice

- **Not solely automated** when:
  - A qualified human genuinely reviews the AI output as one input among several
  - The human applies independent judgment and makes the final decision
  - The human has the capability and actually exercises discretion to deviate from AI recommendations

### "Legal or Similarly Significant Effects"

| Category | Examples | Significance |
|----------|----------|-------------|
| Legal effects | Contract formation/termination, legal obligation imposition, legal status determination | Directly affects legal rights |
| Access to services | Denial of credit, insurance, housing, education, employment | Significantly affects life circumstances |
| Financial impact | Pricing discrimination, benefit calculation, payment terms | Material financial consequences |
| Health and safety | Medical diagnosis prioritisation, emergency response triage | Potential physical harm |
| Freedom and autonomy | Surveillance scoring, movement restriction, content blocking | Affects fundamental freedoms |

Effects that are **not** similarly significant (per EDPB):
- Personalised advertising (unless it reinforces prejudices about vulnerable groups)
- Generic recommendation systems (unless they determine access to information)
- Spam filtering (unless it systematically blocks important communications)

## Art. 22 Exceptions and Safeguards

### Art. 22(2) — Permitted Automated Decisions

| Exception | Condition | Required Safeguards |
|-----------|-----------|-------------------|
| Art. 22(2)(a) — Contract necessity | Decision is necessary for entering into or performance of a contract | Art. 22(3) safeguards required |
| Art. 22(2)(b) — Law authorisation | Authorised by Union or Member State law with suitable measures | Law must provide suitable safeguards |
| Art. 22(2)(c) — Explicit consent | Based on explicit consent | Art. 22(3) safeguards required |

### Art. 22(3) — Mandatory Safeguards

When an Art. 22(2) exception is relied upon, the controller must implement at least:

1. **Right to obtain human intervention**: A qualified person reviews the automated decision
2. **Right to express point of view**: Data subject can present additional information or context
3. **Right to contest**: Formal mechanism to challenge the automated decision with review by a different decision-maker

### Art. 22(4) — Special Category Data Restriction

Automated decisions based on Art. 9 special category data are only permitted under:
- Art. 9(2)(a) — Explicit consent, OR
- Art. 9(2)(g) — Substantial public interest based on Union or Member State law

In both cases, suitable measures to safeguard data subject rights must be in place.

## Human Oversight Design — AI Act Art. 14

### Art. 14 Requirements for High-Risk AI

High-risk AI systems must be designed and developed so that they can be effectively overseen by natural persons during use:

| Requirement | Implementation |
|-------------|---------------|
| Understand capabilities and limitations | Documentation, training, model cards |
| Monitor operation | Real-time monitoring dashboards, alert systems |
| Detect anomalies and dysfunction | Drift detection, performance monitoring |
| Interpret outputs correctly | Confidence indicators, explanation tools |
| Override or reverse decisions | Override mechanism with authority chain |
| Intervene or stop the system | Emergency stop capability |
| Be aware of automation bias | Training on automation bias, countermeasures |

### Human Oversight Levels

| Level | Description | Art. 22 Compliance | Appropriate When |
|-------|-------------|-------------------|------------------|
| Human-in-the-loop (HITL) | Human reviews every AI recommendation before decision | Fully compliant if review is meaningful | High-stakes individual decisions (hiring, credit, medical) |
| Human-on-the-loop (HOTL) | Human monitors AI decisions and can intervene | Compliant if intervention capability is genuine and exercised | Medium-risk decisions with effective monitoring |
| Human-in-command (HIC) | Human sets parameters and reviews outcomes periodically | May not satisfy Art. 22 — decision is solely automated | Low-risk bulk decisions with periodic audit |
| Fully autonomous | No human oversight of individual decisions | Art. 22 applies fully — exception needed | Only where Art. 22(2) exception applies with Art. 22(3) safeguards |

### Meaningful Human Intervention Criteria

A human review qualifies as "meaningful intervention" when all criteria are met:

| Criterion | Test | Red Flag |
|-----------|------|----------|
| **Authority** | Reviewer has formal authority to override AI | Reviewer can only escalate, not decide |
| **Competence** | Reviewer has domain expertise to evaluate the decision | Reviewer is a junior staff member without training |
| **Information** | Reviewer has access to all inputs, the AI output, and explanation | Reviewer sees only AI score with no context |
| **Time** | Sufficient time allocated for genuine consideration | Reviewer processes 200+ decisions per hour |
| **Independence** | Reviewer exercises genuine judgment | Override rate is < 1% suggesting rubber-stamping |
| **Accountability** | Reviewer is accountable for the decision | Accountability rests with the AI system owner, not reviewer |

## Contestation and Appeal Mechanism

### Design Requirements

| Element | Requirement |
|---------|-------------|
| Accessibility | Contestation mechanism is easy to find, access, and use |
| Timeliness | Defined response timeframe (e.g., 30 days) |
| Qualified reviewer | Different from the original decision context; has authority to overturn |
| Information provision | Data subject receives explanation of decision factors and how to contest |
| Evidence consideration | Data subject can submit additional evidence and context |
| Written outcome | Decision on contestation is documented and communicated |
| Further appeal | If contestation is denied, path to DPA complaint or judicial remedy is indicated |

### Contestation Workflow

1. Data subject notified of automated decision with explanation
2. Data subject submits contestation with reasons and any supporting evidence
3. Contestation assigned to qualified human reviewer (different from original oversight)
4. Reviewer assesses: AI inputs, AI output, explanation, data subject's arguments
5. Reviewer makes independent decision: uphold, modify, or overturn
6. Outcome communicated to data subject with reasons
7. If upheld: data subject informed of further options (DPA complaint, judicial remedy)
8. Record maintained in rights exercise register

## AI-Specific Decision Categories

### Credit and Financial Decisions

- **AI application**: Credit scoring, loan approval, insurance pricing, fraud detection
- **Art. 22 trigger**: Yes — determines access to financial services
- **Required**: Meaningful human review before denial; explanation of key scoring factors; contestation with independent review
- **Enforcement**: AEPD fined CaixaBank EUR 6M for automated credit decisions without adequate safeguards

### Employment Decisions

- **AI application**: CV screening, candidate ranking, performance scoring, termination prediction
- **Art. 22 trigger**: Yes — significantly affects employment and livelihood
- **Required**: Human hiring manager makes final decision with genuine authority to deviate from AI ranking; applicants informed of AI use; rejected candidates can request explanation
- **Enforcement**: Italian DPA fined Deliveroo EUR 2.5M for algorithmic worker management without Art. 22 safeguards

### Healthcare Decisions

- **AI application**: Diagnosis assistance, treatment recommendations, triage, risk scoring
- **Art. 22 trigger**: Yes if AI determines care pathway — usually mitigated by physician oversight
- **Required**: Physician makes final clinical decision; AI functions as decision support; patient informed of AI role
- **Special category**: Health data — Art. 22(4) applies

### Public Administration

- **AI application**: Benefit eligibility, fraud detection, risk assessment, resource allocation
- **Art. 22 trigger**: Yes — determines access to public services and benefits
- **Required**: Art. 22(2)(b) legal basis required; suitable measures mandated by law; transparency about algorithmic criteria
- **Enforcement**: Dutch court struck down SyRI fraud detection system for lack of transparency and proportionality

## Profiling Assessment

### GDPR Definition of Profiling (Art. 4(4))

Any form of automated processing to evaluate personal aspects relating to a natural person, in particular to analyse or predict:
- Work performance
- Economic situation
- Health
- Personal preferences
- Interests
- Reliability
- Behaviour
- Location
- Movements

### AI Profiling Risk Assessment

| Profiling Type | Risk Level | Art. 22 Trigger | Mitigation |
|---------------|-----------|-----------------|------------|
| Behavioural prediction (purchasing, browsing) | Medium | Only if decision with legal/significant effect | Opt-out, transparency |
| Credit scoring / financial risk | High | Yes — access to financial services | Human review, explanation, contestation |
| Health risk prediction | Very High | Yes — Art. 22(4) applies | Explicit consent, physician oversight |
| Criminal risk assessment | Very High | Yes — liberty and legal effects | Legal basis required, judicial oversight |
| Employment performance scoring | High | Yes — employment effects | HR human review, employee notification |
| Social scoring | Prohibited | N/A — AI Act Art. 5 prohibition | Do not implement |

## Enforcement Precedents

- **AEPD v. CaixaBank (PS/00421/2020, 2021)**: EUR 6M fine for automated credit decision-making without adequate Art. 22 safeguards, explanation, or contestation mechanism.
- **Italian DPA v. Deliveroo (2021)**: EUR 2.5M fine for algorithmic management of delivery riders — Art. 22 applied to automated work allocation and performance scoring.
- **Dutch Court v. SyRI (2020)**: Algorithmic fraud detection system struck down — automated profiling of citizens without proportionality, transparency, or adequate safeguards.
- **Hungarian DPA v. Bank (2019)**: Fine for automated credit denial without providing meaningful information about decision logic or contestation mechanism.
- **French Conseil d'Etat v. Parcoursup (2019)**: Court upheld use of algorithm for university admissions only because meaningful human review was genuinely conducted for each application.
- **Austrian DPA v. CRIF (2023)**: Credit scoring company — violation of Art. 15(1)(h) for failing to provide meaningful information about automated scoring logic.

## Integration Points

- **ai-transparency-reqs**: Explanation requirements feed into transparency framework
- **ai-dpia**: Human oversight assessment is DPIA Phase 5 component
- **ai-data-subject-rights**: Right to explanation and contestation are rights exercise procedures
- **ai-deployment-checklist**: Art. 22 compliance is pre-deployment validation item
- **ai-bias-special-category**: Bias in automated decisions creates Art. 22 harm
