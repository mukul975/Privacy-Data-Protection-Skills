---
name: conducting-gdpr-dpia
description: >-
  Guides the end-to-end GDPR Data Protection Impact Assessment process under
  Article 35, including mandatory trigger identification per Art. 35(3), DPIA
  content requirements per Art. 35(7), and EDPB WP248rev.01 methodology.
  Activate for systematic profiling, large-scale special category processing,
  or large-scale public monitoring. Keywords: DPIA, Article 35, impact
  assessment, WP248, data protection, risk assessment.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-impact-assessment
  tags: "dpia, gdpr, article-35, wp248, risk-assessment, data-protection"
---

# Conducting GDPR Data Protection Impact Assessment

## Overview

A Data Protection Impact Assessment (DPIA) is a structured process mandated by Article 35 of the GDPR to identify, assess, and mitigate risks to the rights and freedoms of natural persons arising from data processing operations. The DPIA is not merely a compliance checkbox but a living risk management instrument that must be conducted before processing begins and updated throughout the processing lifecycle. This skill implements the methodology recommended by the European Data Protection Board in WP248rev.01 (Guidelines on Data Protection Impact Assessment) and incorporates enforceable requirements from Art. 35(1)-(11).

## Mandatory DPIA Triggers — Art. 35(3)

A DPIA is required when processing is likely to result in a high risk to the rights and freedoms of natural persons, particularly in these cases:

### Automatic Triggers Under Art. 35(3)

| Trigger | GDPR Reference | Description |
|---------|---------------|-------------|
| Systematic and extensive profiling with significant effects | Art. 35(3)(a) | Automated processing including profiling that produces legal effects or similarly significant effects on the data subject |
| Large-scale special category or criminal data | Art. 35(3)(b) | Processing on a large scale of data under Art. 9(1) (health, biometric, genetic, racial, political, religious, sexual orientation, trade union) or Art. 10 (criminal convictions) |
| Systematic large-scale monitoring of public areas | Art. 35(3)(c) | CCTV surveillance, drone monitoring, Wi-Fi tracking, or other systematic monitoring of publicly accessible areas on a large scale |

### EDPB WP248rev.01 Criteria — Two or More Triggers Require a DPIA

The EDPB established nine criteria for identifying high-risk processing. If a processing operation meets two or more of these criteria, a DPIA is presumptively required:

1. **Evaluation or scoring** — Profiling, prediction, credit scoring, behavioural analysis
2. **Automated decision-making with legal or significant effect** — Processing that determines access to services, contracts, or benefits
3. **Systematic monitoring** — Observation, tracking, or surveillance of data subjects
4. **Sensitive data or data of a highly personal nature** — Art. 9 special categories, financial data, communications metadata, location data
5. **Data processed on a large scale** — Volume of data subjects, volume of data items, geographic scope, duration of processing
6. **Matching or combining datasets** — Merging data from multiple sources beyond the data subject's reasonable expectation
7. **Data concerning vulnerable data subjects** — Children, employees, mentally ill, asylum seekers, elderly, patients
8. **Innovative use or applying new technological solutions** — Fingerprint and facial recognition combined with access control, IoT applications, AI-driven processing
9. **Processing that prevents data subjects from exercising a right or using a service** — Including but not limited to screening processes that block access

## DPIA Content Requirements — Art. 35(7)

Every DPIA must contain at minimum the following four elements:

### (a) Systematic Description of Processing Operations and Purposes

- Nature of the processing: collection, recording, organisation, structuring, storage, adaptation, alteration, retrieval, consultation, use, disclosure, dissemination, combination, restriction, erasure, destruction
- Scope: categories of data subjects, categories of personal data, volume and frequency, geographic scope
- Context: relationship between controller and data subjects, how data was obtained, data subject expectations
- Purpose: specific purposes per Art. 5(1)(b), lawful basis under Art. 6(1), and if applicable Art. 9(2) condition

### (b) Assessment of Necessity and Proportionality

- Lawful basis justification with specificity
- Purpose limitation analysis: is each data element necessary for the stated purpose?
- Data minimisation assessment: could the purpose be achieved with less data or anonymised data?
- Storage limitation: are retention periods justified and enforced?
- Data subject rights facilitation: how are Arts. 15-22 rights enabled?
- Safeguards for international transfers under Chapter V where applicable

### (c) Assessment of Risks to Rights and Freedoms

For each identified risk, assess:

| Risk Dimension | Assessment Criteria |
|----------------|-------------------|
| Likelihood | Remote (< 10%), Possible (10-50%), Likely (50-90%), Almost certain (> 90%) |
| Severity | Negligible (inconvenience), Limited (significant but recoverable), Significant (serious difficulty), Maximum (irreversible consequences) |
| Risk Level | Likelihood x Severity matrix producing Low, Medium, High, or Very High |

Types of harm to assess:
- Physical harm (discrimination leading to violence, denial of healthcare)
- Material harm (financial loss, identity theft, loss of employment)
- Non-material harm (reputational damage, emotional distress, loss of autonomy)
- Social harm (chilling effect on free speech, discrimination, exclusion)
- Loss of control over personal data (inability to exercise rights, unknown processing)

### (d) Measures to Address Risks

- Technical measures: encryption at rest and in transit (AES-256, TLS 1.3), pseudonymisation per Art. 4(5), access controls (RBAC), automated deletion, audit logging
- Organisational measures: privacy policies, staff training, DPO oversight, incident response procedures, data processing agreements per Art. 28
- Contractual measures: data subject notification, consent mechanisms, processor obligations
- Residual risk assessment: risk level after implementation of mitigating measures

## DPIA Process Methodology

### Step 1: Screening and Scoping (Week 1)

1. Complete the Privacy Threshold Analysis questionnaire to confirm DPIA obligation.
2. Define the processing operation boundary: which systems, data flows, and organisational units are in scope.
3. Identify the DPIA team: processing owner, DPO, IT security representative, legal counsel, and where appropriate a data subject representative per Art. 35(9).
4. Gather existing documentation: system architecture diagrams, data flow maps, privacy notices, consent forms, processor agreements.

### Step 2: Systematic Description (Week 2)

1. Map the complete data lifecycle from collection to deletion.
2. Document all data elements processed, with lawful basis for each.
3. Identify all recipients and sub-processors.
4. Document international transfers and applicable safeguard mechanisms.
5. Record the technology stack and infrastructure involved.

### Step 3: Necessity and Proportionality Assessment (Week 3)

1. For each data element, document why it is necessary for the stated purpose.
2. Assess whether less invasive alternatives could achieve the same purpose.
3. Evaluate data minimisation compliance.
4. Confirm retention periods are proportionate and technically enforced.
5. Verify data subject rights can be exercised effectively.

### Step 4: Risk Identification and Assessment (Week 3-4)

1. Conduct threat modelling against the data flow map (sources of risk: internal actors, external attackers, processors, system failures).
2. For each threat, assess likelihood and severity using the matrix in Art. 35(7)(c).
3. Document risks in the risk register with unique identifiers.
4. Calculate inherent risk levels before mitigation.

### Step 5: Mitigation Measures (Week 4-5)

1. For each High or Very High risk, identify specific technical and organisational measures.
2. Document the expected risk reduction for each measure.
3. Calculate residual risk levels after mitigation.
4. If residual risk remains High or Very High, escalate to Art. 36 prior consultation with the supervisory authority.

### Step 6: DPO Advice and Sign-Off (Week 5-6)

1. Present the completed DPIA to the DPO for independent review per Art. 35(2).
2. Document the DPO's advice and whether it was followed; if not, document reasons.
3. Obtain processing owner sign-off and senior management approval.
4. Record the DPIA in the central DPIA register with a scheduled review date.

### Step 7: Ongoing Review

1. Review the DPIA when there is a material change in risk: new data categories, new recipients, technology change, security incident, regulatory change.
2. Conduct periodic reviews at minimum annually.
3. Document all review outcomes and version the DPIA.

## DPO Consultation — Art. 35(2)

The controller shall seek the advice of the Data Protection Officer where designated. The DPO must be involved from the screening phase. Per Art. 39(1)(c), the DPO has the task of providing advice regarding the DPIA and monitoring its performance. The controller must document the DPO's advice and the reasons for any departure from it.

## Data Subject Views — Art. 35(9)

Where appropriate, the controller shall seek the views of data subjects or their representatives on the intended processing. This may take the form of:
- Surveys or focus groups with representative data subject samples
- Consultation with trade unions where employees are affected
- Public consultation for large-scale government processing
- Consultation with patient advocacy groups for health data processing

The controller must document whether data subject views were sought, and if not, the reasons why it was not appropriate.

## Supervisory Authority Lists — Art. 35(4)-(5)

Each supervisory authority publishes a list of processing operations requiring a DPIA (Art. 35(4)) and may also publish a list of operations not requiring one (Art. 35(5)). Controllers must consult the applicable national list. Notable examples:
- **CNIL (France)**: 14 processing types requiring DPIA, including employee scoring, health data warehouses, biometric access control
- **ICO (UK)**: 10 processing types requiring DPIA, including invisible processing, tracking individuals online, automated decision-making
- **BfDI (Germany)**: Processing of genetic or biometric data for identification, scoring by credit agencies, large-scale profiling

## Common DPIA Deficiencies

1. **Generic risk descriptions**: Risks described as "data breach" without specifying the attack vector, affected data categories, and specific harms
2. **Missing proportionality analysis**: Jumping from description to risk without evaluating whether the processing is necessary and proportionate
3. **No residual risk calculation**: Identifying measures but failing to assess whether they reduce risk to acceptable levels
4. **DPO advice not documented**: DPO involvement limited to signature without recording substantive advice
5. **Static DPIA**: Assessment completed once and never reviewed despite material changes to processing
6. **Missing Art. 35(9) justification**: No documentation of whether data subject views were sought or why they were not

## Enforcement Precedents

- **Karolinska Institute (Swedish DPA, 2019)**: SEK 200,000 fine for processing genetic data without conducting a DPIA as required by Art. 35.
- **Austrian Post (Austrian DPA, 2019)**: EUR 18 million fine related to profiling of political party affinities — DPIA inadequacy was a contributing factor.
- **Clearview AI (CNIL, 2022)**: EUR 20 million fine for biometric processing without DPIA and without lawful basis.
- **Real Madrid CF (AEPD, 2023)**: Sanctioned for implementing Wi-Fi tracking in stadium without conducting DPIA for large-scale public area monitoring under Art. 35(3)(c).

## Integration Points

- **Art. 36 Prior Consultation**: When residual risk remains high after mitigation, the controller must consult the supervisory authority before processing begins.
- **Art. 30 Records of Processing**: DPIA findings should be cross-referenced with the RoPA to ensure consistency.
- **Art. 25 Data Protection by Design**: Mitigation measures identified in the DPIA feed directly into privacy-by-design implementation.
- **Art. 33-34 Breach Notification**: DPIA risk assessments inform breach severity analysis and notification decisions.
