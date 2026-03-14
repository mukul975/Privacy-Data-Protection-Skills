---
name: employee-health-data
description: >-
  Governs employee health data processing for fitness-for-work assessments,
  occupational health surveillance, COVID testing legacy programmes, and
  absence management. Applies Art. 9(2)(b) employment obligations and
  Art. 9(2)(h) health professional exceptions. Covers data minimisation,
  occupational health provider relationships, and return-to-work procedures.
  Keywords: health data, Art. 9, occupational health, fitness-for-work,
  special category, employment, sickness absence.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: employee-data-privacy
  tags: "health-data, article-9, occupational-health, fitness-for-work, special-category, sickness-absence"
---

# Employee Health Data

## Overview

Employee health data is among the most sensitive categories of personal data processed in the employment context. It falls under Art. 9(1) GDPR as "data concerning health," defined in Art. 4(15) as "personal data related to the physical or mental health of a natural person, including the provision of health care services, which reveal information about his or her health status." Employers routinely process health data for absence management, fitness-for-work assessments, occupational health surveillance, workplace adjustments for disability, and return-to-work programmes. Each of these processing activities requires identification of a valid Art. 9(2) exception, strict data minimisation, and clear boundaries between what the employer needs to know (fitness/unfitness and any required adjustments) and clinical details (diagnosis, treatment, prognosis) that must remain with the occupational health provider.

## Legal Framework

### Art. 9(2) Exceptions for Employee Health Data

| Exception | Article | Employment Application |
|-----------|---------|----------------------|
| Explicit consent | Art. 9(2)(a) | Rarely valid due to power imbalance; may apply for genuinely voluntary wellness programmes |
| Employment law obligations | Art. 9(2)(b) | Primary basis: processing necessary for carrying out obligations in employment, social security, and social protection law — to the extent authorised by national law with appropriate safeguards |
| Vital interests | Art. 9(2)(c) | Emergency situations where employee is physically incapacitated and health data is needed for emergency response |
| Health professional processing | Art. 9(2)(h) | Processing for preventive or occupational medicine, assessment of working capacity, medical diagnosis — by or under the responsibility of a health professional bound by professional secrecy |
| Public health | Art. 9(2)(i) | Public health threats (pandemic response) — must be based on national or EU law |
| Substantial public interest | Art. 9(2)(g) | Where national law establishes a substantial public interest basis, e.g., disability discrimination legislation requiring processing to assess reasonable adjustments |

### Art. 9(2)(b) — Employment Obligations

This is the most commonly relied upon exception. It requires:

1. **National law authorisation**: The processing must be authorised by EU or Member State law (not merely the employment contract)
2. **Appropriate safeguards**: The national law must provide appropriate safeguards for the fundamental rights and interests of the data subject
3. **Necessity**: The processing must be necessary for carrying out obligations — not merely useful

**National implementations**:

| Jurisdiction | Legal Basis | Scope |
|-------------|-------------|-------|
| UK | DPA 2018, Schedule 1, Part 1, Para 1 | Processing necessary for employment obligations including health and safety duties, statutory sick pay, disability adjustments |
| Germany | BDSG Section 26(3) | Processing of special category data for employment purposes where necessary for exercising rights or obligations under employment or social security law |
| France | Labour Code Art. L.4624-1 et seq. | Occupational health surveillance; employer receives fitness/unfitness conclusion only, not diagnosis |
| Netherlands | UAVG Art. 30(1)(a) | Processing necessary for employment rights and obligations under law or collective agreement |
| Italy | D.Lgs. 81/2008, Art. 25 and 41 | Occupational health surveillance; competent doctor (medico competente) conducts assessments and communicates fitness judgment only |

### Art. 9(2)(h) — Health Professional Exception

Processing is permitted when carried out by or under the responsibility of a health professional subject to professional secrecy. This applies to:
- Occupational health physicians conducting fitness-for-work assessments
- Company nurses providing on-site health services
- Employee Assistance Programme (EAP) counsellors

**Critical limitation**: The health professional may share with the employer only the conclusion (fit/unfit/fit with adjustments) and not the underlying clinical details. The diagnosis remains confidential between the health professional and the employee.

## Processing Scenarios

### Scenario 1: Sickness Absence Management

**What the employer needs**: Dates of absence, whether the absence is certified, expected return date, any workplace adjustments required.

**What the employer must not receive**: Diagnosis, treatment details, prognosis, medication, mental health specifics.

**Data flow**:
1. Employee notifies employer of absence per sickness absence policy
2. Employee provides a fit note (UK: Statement of Fitness for Work) or equivalent medical certificate from their GP or treating physician
3. The fit note states: (a) date range, (b) whether the employee is "not fit for work" or "may be fit for work with adjustments," and (c) any recommended adjustments
4. The employer records: absence dates, fit note dates, adjustment requirements
5. The employer does not require or record the diagnosis (the diagnosis field on UK fit notes is visible but the employer should not record it in HR systems unless the employee voluntarily shares it for adjustment purposes)

**Atlas Manufacturing Group Example**: Atlas's sickness absence policy states that employees self-certify for absences up to 7 days and provide a fit note for absences exceeding 7 days. The HR system records absence dates and the fit/unfit conclusion only. The diagnosis field from fit notes is not entered into the HR system. If an employee's absence exceeds 4 weeks, a referral to occupational health is offered — the occupational health report to the employer addresses fitness, adjustments, and anticipated return date, but not clinical diagnosis.

### Scenario 2: Fitness-for-Work Assessment

**Trigger**: Safety-critical roles (drivers, machine operators, work at height), return from long-term absence, concerns about an employee's capacity to perform their role safely.

**Data flow**:
1. Employer refers employee to occupational health provider with a specific, written referral question (e.g., "Is the employee fit to operate forklift equipment? Are any workplace adjustments required?")
2. The referral must not contain health information the employer does not already legitimately hold
3. The occupational health provider examines the employee (with the employee's cooperation)
4. The provider issues a report to the employer addressing the referral question only: fit/unfit/fit with adjustments
5. If adjustments are recommended, they are described functionally (e.g., "reduced lifting to a maximum of 10kg for 6 weeks") without clinical explanation
6. The employee receives a copy of the report and may request amendments before it is sent to the employer (Access to Medical Reports Act 1988, UK)

**Art. 9(2)(h) application**: The occupational health provider is a health professional bound by professional secrecy (GMC, NMC, or equivalent registration). The processing is carried out under their responsibility. They share with the employer only what is necessary for the employment decision.

### Scenario 3: Occupational Health Surveillance

**Scope**: Statutory health surveillance required for employees exposed to occupational hazards (noise, vibration, hazardous substances, ionising radiation, asbestos, lead).

**Legal basis**: Art. 9(2)(b) — legal obligation under national health and safety law implementing Framework Directive 89/391/EEC.

**Key obligations**:
- Health surveillance must be conducted by a competent occupational health professional
- The employer receives a fitness certificate indicating whether the employee is fit for the specific exposure
- Individual health records are maintained by the occupational health provider, not the employer
- The employer receives aggregate statistical data (number of employees fit/unfit) for risk assessment purposes
- Individual results may only be shared with the employer if the employee consents or if national law specifically authorises it

### Scenario 4: Disability and Reasonable Adjustments

**Legal basis**: Art. 9(2)(b) read with national disability discrimination law (UK: Equality Act 2010; EU: Framework Employment Directive 2000/78/EC).

**Data minimisation principle**: The employer needs to know:
- That the employee has a condition meeting the legal definition of disability (or may have such a condition)
- What functional limitations arise from the condition in the work context
- What adjustments would enable the employee to perform the role

**The employer does not need**: The specific diagnosis, medication, treatment history, or prognosis — unless the employee voluntarily shares this information to support the adjustment process.

### Scenario 5: COVID-19 Testing and Vaccination (Legacy)

**Context**: Many organisations implemented COVID-19 testing and vaccination status checking during the pandemic. Residual data and policies may remain.

**Current obligations**:
- COVID testing data collected during the pandemic must be reviewed for retention compliance
- Vaccination status records must be deleted unless ongoing legal obligation requires retention (e.g., healthcare workers in specific jurisdictions)
- Test results and vaccination records are health data under Art. 9(1)
- The lawful basis for pandemic processing (typically Art. 9(2)(b) or (i)) may no longer apply as pandemic legal frameworks are revoked

**Atlas Manufacturing Group Example**: Atlas collected COVID test results and vaccination status during 2020-2022 under Art. 9(2)(b) (UK health and safety legal obligation) and Art. 9(2)(i) (public health). Following the revocation of mandatory testing guidance in 2022, Atlas conducted a retention review and deleted all COVID testing data and vaccination records in March 2023, retaining only aggregate statistical data for occupational health reporting.

### Scenario 6: Employee Wellness Programmes

**Description**: Employer-offered wellness programmes including health risk assessments, fitness challenges, mental health support, and biometric screenings.

**Lawful basis**: Art. 9(2)(a) explicit consent — wellness programmes are the rare employment scenario where consent may be valid, because:
- Participation is genuinely voluntary
- Non-participation has no adverse employment consequences
- The programme is offered for the employee's benefit

**Conditions**:
- Consent must be granular (separate consent for each programme element)
- The employer must not receive individual health data; a third-party wellness provider should process the data and provide only aggregate anonymised reports to the employer
- Employees must be able to withdraw at any time
- Line managers must not know who participates

## Data Minimisation Framework

### What the Employer May Hold

| Data Element | Permitted | Lawful Basis |
|-------------|-----------|-------------|
| Absence dates | Yes | Art. 6(1)(b) contract + Art. 9(2)(b) employment obligation |
| Fit/unfit conclusion | Yes | Art. 9(2)(b) employment obligation |
| Required workplace adjustments | Yes | Art. 9(2)(b) disability legislation |
| Occupational health referral correspondence | Yes | Art. 9(2)(h) health professional |
| Fitness-for-work certificates | Yes | Art. 9(2)(b) health and safety obligation |

### What the Employer Must Not Hold

| Data Element | Prohibited | Reason |
|-------------|-----------|--------|
| Clinical diagnosis | Yes (unless voluntarily shared) | Not necessary for employment decisions |
| Treatment details | Yes | Not necessary; disproportionate intrusion |
| Medication information | Yes | Not necessary; may reveal conditions not relevant to work |
| Mental health counselling records | Yes | Processed under professional secrecy by health professional |
| GP/hospital records | Yes | No lawful basis for employer access |
| Genetic test results | Yes | Art. 9(1) + Art. 9(4) specific national restrictions |

## Access Controls for Health Data

### Need-to-Know Hierarchy

| Role | Access Level |
|------|-------------|
| HR Manager (employee relations) | Absence dates, fit/unfit conclusion, adjustment requirements |
| Line Manager | Absence dates and expected return date only; no health details |
| Occupational Health Provider | Full clinical information (under professional secrecy) |
| DPO | Access to processing records and policy compliance; no individual health data |
| Payroll | Absence dates for statutory sick pay calculation only |
| IT | No access to health data content; system administration only |

### Technical Controls

- Health data must be stored in a separate, access-controlled area of the HR system (not in the general employee record)
- Access to health data fields requires specific role permission and is audit-logged
- Health data must be encrypted at rest (AES-256)
- Health data must not be included in general HR reporting or analytics
- Automated alerts must notify the DPO if health data access patterns indicate unusual activity

## Enforcement Precedents

| Authority | Case | Fine/Outcome | Key Issue |
|-----------|------|-------------|-----------|
| LfDI Hamburg (Germany) | H&M, 2020 | EUR 35,258,707.95 | Employer systematically recorded employee health details from return-to-work conversations, including diagnoses and family health issues |
| CNIL (France) | SAN-2021-015 | EUR 150,000 | Employer collected excessive health data during COVID screening beyond what was legally required |
| Garante (Italy) | Provvedimento 2022-0156 | Processing restricted | Employer required employees to disclose diagnosis on sickness absence forms |
| ICO (UK) | Enforcement notice, 2021 | Processing ordered to cease | Employer shared employee mental health data with line managers without necessity or consent |
| AEPD (Spain) | PS/00142/2022 | EUR 100,000 | Employer processed employee COVID vaccination status after legal basis expired |

## Integration Points

- **Employment Consent Limits**: Consent for health data processing is constrained in employment (see employment-consent-limits skill).
- **Employee DSAR Response**: Health data is frequently requested in employee DSARs (see employee-dsar-response skill).
- **HR System Privacy Config**: Health data requires dedicated access controls in HR systems (see hr-system-privacy-config skill).
- **Employee Monitoring DPIA**: Wellness programmes with health data require DPIA (see employee-monitoring-dpia skill).
- **Background Check Privacy**: Pre-employment health questions are restricted by disability discrimination law (see background-check-privacy skill).
