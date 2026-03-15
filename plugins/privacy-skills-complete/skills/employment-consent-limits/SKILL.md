---
name: employment-consent-limits
description: >-
  Analyses the limitations on consent as a lawful basis for processing employee
  data under Art. 88 GDPR and WP29 Opinion 2/2017. Addresses power imbalance
  in employment relationships, identifies alternative lawful bases, and maps
  national derogations. Keywords: consent, employment, power imbalance,
  Art. 88, WP29, lawful basis, employee data, labour law.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: employee-data-privacy
  tags: "consent, employment, power-imbalance, article-88, wp29, lawful-basis"
---

# Employment Consent Limits

## Overview

Consent is rarely a valid lawful basis for processing employee personal data under GDPR. The Article 29 Working Party's Opinion 2/2017 on data processing at work (WP249) and the EDPB's subsequent guidance establish a clear presumption against reliance on consent in the employment context. The rationale is straightforward: the inherent power imbalance between employer and employee means that consent cannot be "freely given" as required by Art. 4(11) GDPR when refusal or withdrawal of consent may result in real or perceived adverse consequences for the employee.

Art. 88(1) GDPR explicitly empowers Member States to provide more specific rules for processing in the employment context, and many have enacted legislation that further restricts or modifies the role of consent in employment data processing. This skill maps the consent prohibition landscape, identifies the narrow exceptions where consent may be valid, and provides a decision framework for selecting appropriate alternative lawful bases.

## The Consent Problem in Employment

### Art. 4(11) — Definition of Consent

Consent must be:
- **Freely given**: The data subject must have a genuine and free choice and must be able to refuse or withdraw consent without detriment
- **Specific**: Consent must be given for one or more specific purposes
- **Informed**: The data subject must be informed about the controller's identity, the purpose, the data processed, the right to withdraw, and any automated decision-making
- **Unambiguous indication**: A clear affirmative action is required

### Why Consent Fails in Employment — WP29 Opinion 2/2017

The Article 29 Working Party stated in Section 5.1 of Opinion 2/2017:

> "Employees are almost never in a position to freely give, refuse, or revoke consent, given the dependency that results from the employer/employee relationship. Given the imbalance of power, employees can only give free consent in exceptional circumstances, when no consequences at all are connected to acceptance or rejection of an offer."

**Key factors that negate free consent in employment**:

| Factor | Explanation |
|--------|-------------|
| Power imbalance | The employer controls terms of employment, pay, promotion, and termination |
| Perceived consequences | Even where no actual consequence follows refusal, employees reasonably fear adverse effects |
| Inability to refuse | Processing may be presented as mandatory regardless of the consent mechanism |
| Withdrawal difficulty | Employees may fear that withdrawing consent will be noted negatively |
| Granularity problems | Consent for multiple processing activities may be bundled, preventing genuine choice |

### Recital 43 — Imbalance of Power

Recital 43 GDPR states: "Consent should not provide a valid legal ground for the processing of personal data in a specific case where there is a clear imbalance between the data subject and the controller." The employer-employee relationship is the paradigmatic example of this imbalance.

### EDPB Confirmation

The EDPB Guidelines 05/2020 on consent under Regulation 2016/679 (Section 3.1.1) reaffirmed that consent is "highly unlikely to be a legal basis for data processing at work, unless employees can refuse without adverse consequences."

## Narrow Exceptions — When Consent May Be Valid

Despite the general presumption against consent in employment, there are limited scenarios where genuine free choice may exist:

### Exception 1: Purely Voluntary Benefits

Where an employer offers an optional benefit and participation is genuinely voluntary with no consequence for declining:

- Optional corporate wellness programme with health data processing
- Voluntary employee discount programme requiring sharing of personal preferences
- Optional employee photo directory

**Conditions**: The benefit must be genuinely optional, non-participation must have no negative consequences, and the employee must be able to withdraw at any time with immediate cessation of processing.

**Atlas Manufacturing Group Example**: Atlas offers an optional cycle-to-work scheme that requires processing of home address data for distance calculation. Employees who decline are not disadvantaged in any way. The DPO approved consent as the lawful basis with documented safeguards: the consent form explicitly states that non-participation has no employment consequences, and the scheme administrator is separate from line management.

### Exception 2: Employee-Initiated Processing

Where the employee specifically requests processing for their own benefit:

- Employee requests a reference letter (requiring disclosure of employment data to a third party)
- Employee requests salary advance (requiring additional financial data processing)
- Employee requests flexible working arrangement (requiring processing of personal circumstances)

### Exception 3: Art. 9(2)(a) Explicit Consent for Special Category Data

In limited circumstances, explicit consent under Art. 9(2)(a) may be appropriate for special category data where:
- No other Art. 9(2) condition applies
- The processing is genuinely in the employee's interest
- Refusal has absolutely no adverse consequence
- National law does not prohibit or restrict consent for this purpose

**Example**: An employee voluntarily discloses a disability to access workplace adjustments, and no legal obligation to process this data exists under national disability discrimination law.

## Alternative Lawful Bases for Employment Processing

### Art. 6(1)(b) — Performance of the Employment Contract

**Scope**: Processing necessary for the performance of the contract of employment.

| Processing Activity | Art. 6(1)(b) Applicability |
|---------------------|---------------------------|
| Payroll processing | Yes — directly necessary for contract performance |
| Work scheduling and shift management | Yes — necessary for organising contractual duties |
| Performance management against contractual objectives | Yes — contractual performance evaluation |
| Absence management | Yes — managing contractual leave entitlements |
| Provision of contractual benefits (pension, insurance) | Yes — contractual obligation |
| Background checks beyond contractual requirements | No — extends beyond contract necessity |
| Post-termination data retention beyond legal requirements | No — contract has ended |

**Limitation**: The processing must be genuinely necessary for the contract, not merely useful or convenient. The EDPB has emphasised that "necessary" must be interpreted strictly — what is necessary is determined by the nature of the contract, not the employer's business model.

### Art. 6(1)(c) — Legal Obligation

**Scope**: Processing required by law, including employment law, tax law, social security law, and health and safety law.

| Processing Activity | Legal Obligation |
|---------------------|-----------------|
| Tax withholding and reporting | National tax law (e.g., Income Tax Act, PAYE regulations) |
| Social security contributions | National social security legislation |
| Working time recording | EU Working Time Directive 2003/88/EC, as confirmed in CCOO v Deutsche Bank (CJEU, C-55/18, 2019) |
| Health and safety incident reporting | Framework Directive 89/391/EEC |
| Right-to-work verification | National immigration law |
| Gender pay gap reporting (UK) | Equality Act 2010 (Gender Pay Gap Information) Regulations 2017 |
| Whistleblower channel operation | EU Whistleblowing Directive 2019/1937 |

### Art. 6(1)(f) — Legitimate Interest

**Scope**: Processing necessary for the legitimate interests of the employer, provided these interests are not overridden by the interests, rights, or freedoms of the employee.

**Three-part legitimate interest test (Art. 6(1)(f) + WP217)**:

1. **Purpose test**: Is there a legitimate interest? (Business security, fraud prevention, IT security, organisational efficiency)
2. **Necessity test**: Is the processing necessary for that interest, or could the aim be achieved by less intrusive means?
3. **Balancing test**: Do the employer's interests override the employees' fundamental rights? Consider:
   - The nature of the data (sensitive vs. non-sensitive)
   - The reasonable expectations of employees
   - The impact on the employee
   - The safeguards in place

| Processing Activity | Legitimate Interest Analysis |
|---------------------|------|
| CCTV in production areas for safety | Likely valid — safety interest is strong, cameras in work areas expected |
| Email metadata monitoring for security | Likely valid if limited to metadata and employees are informed |
| Productivity scoring from monitoring data | Unlikely valid — significant impact on employee autonomy, less intrusive alternatives available |
| Social media screening of job applicants | Questionable — high intrusiveness, limited to publicly available professional profiles if at all |

### Art. 6(1)(e) — Public Interest (Public Sector Employers)

For public sector employers, processing may be based on the performance of a task carried out in the public interest or in the exercise of official authority.

## Art. 88 — National Derogations

Art. 88(1) permits Member States to provide more specific rules for processing in the employment context by law or collective agreements. Key national implementations:

### Germany — Section 26 BDSG

- Employee data may be processed if necessary for the employment decision, performance of the employment contract, exercise or enjoyment of rights from collective agreements, or termination of employment
- Consent in the employment context is valid only if the employee derives a legal or economic advantage or the employer and employee pursue the same interest
- Consent must be in writing (unless electronic consent is appropriate due to circumstances)
- The works council (Betriebsrat) has co-determination rights under Section 87(1)(6) BetrVG for any technical monitoring of employee behaviour

### France — Labour Code (Code du travail)

- Art. L.1121-1: No employer may restrict the rights of individuals or individual and collective freedoms unless justified by the nature of the task and proportionate to the aim pursued
- Art. L.1222-4: No information concerning an employee personally may be collected by a device that has not been previously brought to their attention
- CNIL Deliberation No. 2019-160: Specific requirements for employee monitoring transparency and proportionality

### Netherlands — UAVG (Implementing Act GDPR)

- Art. 30 UAVG: Employee consent for processing by the employer is deemed not freely given due to the dependency relationship, unless the processing is clearly in the interest of the employee
- Works council (ondernemingsraad) has consent rights under Art. 27(1)(k) and (l) WOR for personal data processing decisions

### Spain — Organic Law 3/2018 (LOPDGDD)

- Art. 87-91: Specific provisions for digital rights in the employment context
- Art. 87: Right to digital privacy at work
- Art. 89: Right to digital privacy in relation to video surveillance and sound recording at the workplace — employees must be informed of monitoring in advance
- Art. 90: Right to digital privacy in the context of geolocation at work

### Italy — Workers' Statute (Legge 300/1970) and Jobs Act (D.Lgs. 151/2015)

- Art. 4: Remote monitoring of employees is permitted only for organisational, production, safety, or asset protection purposes, and only with trade union agreement or labour inspectorate authorisation
- Individual performance monitoring through remote control systems remains prohibited

## Decision Framework: Selecting the Lawful Basis

```
START: Employer needs to process employee personal data
│
├─ Is the processing required by a specific law or regulation?
│  ├─ YES → Art. 6(1)(c) — Legal Obligation
│  └─ NO → Continue
│
├─ Is the processing necessary for performance of the employment contract?
│  ├─ YES → Art. 6(1)(b) — Contract Performance
│  │  └─ Apply strict necessity test: would the contract fail without this processing?
│  └─ NO → Continue
│
├─ Is the employer a public authority processing for a public task?
│  ├─ YES → Art. 6(1)(e) — Public Interest
│  └─ NO → Continue
│
├─ Does the employer have a legitimate interest?
│  ├─ YES → Conduct three-part LIA under Art. 6(1)(f)
│  │  ├─ Balancing test favours employer → Art. 6(1)(f) — Legitimate Interest
│  │  └─ Balancing test favours employee → Processing cannot proceed on this basis
│  └─ NO → Continue
│
├─ Is the processing genuinely voluntary with zero employment consequences?
│  ├─ YES → Art. 6(1)(a) — Consent (with documented safeguards)
│  │  └─ Document: (1) no consequence for refusal, (2) easy withdrawal, (3) separate from employment terms
│  └─ NO → Consent is not valid. Reassess whether processing is necessary at all.
│
└─ END: If no lawful basis can be identified, the processing must not proceed.
```

## Common Compliance Failures

| Failure | Risk | Remediation |
|---------|------|-------------|
| Using consent as default lawful basis for all employment processing | Invalid processing; enforcement action; employee claims | Audit all employment processing and reassign to appropriate lawful basis |
| Bundling consent for multiple purposes in one form | Consent is not specific per Art. 4(11) | Separate consent requests with granular choices |
| No mechanism for consent withdrawal | Consent invalid from inception | Implement withdrawal mechanism and cease processing on withdrawal |
| Presenting consent as mandatory during onboarding | Consent not freely given | Separate mandatory processing (with alternative lawful basis) from optional processing |
| Ignoring national Art. 88 derogations | Non-compliance with national law | Map all employment processing to applicable national requirements |

## Enforcement Precedents

| Authority | Case | Fine/Outcome | Issue |
|-----------|------|-------------|-------|
| Hellenic DPA | Decision 26/2019 | EUR 150,000 | Employer relied on consent for employee CCTV monitoring — consent invalid due to power imbalance |
| Austrian DPA | DSB-D123.270/0009-DSB/2018 | EUR 4,800,000 (reduced on appeal) | Systematic employee monitoring based on invalid consent |
| ICO (UK) | Mermaids Charity, 2023 | Enforcement notice | Processing of employee special category data without valid lawful basis |
| CNIL (France) | Deliberation SAN-2022-018 | EUR 600,000 | Employer collected excessive employee data, purporting to rely on consent |
| LfDI Baden-Württemberg | 2020 | EUR 35,258,707.95 | Employer processed employee health data based on consent that was not freely given (H&M case, contributed to by German Federal Commissioner) |

## Integration Points

- **Employee Monitoring DPIA**: DPIAs for monitoring must confirm that consent is not relied upon (see employee-monitoring-dpia skill).
- **Employee Biometric Data**: Biometric processing requires Art. 9 condition — consent validity is even more constrained (see employee-biometric-data skill).
- **Employee Health Data**: Health data processing has specific Art. 9(2)(b) and (h) alternatives to consent (see employee-health-data skill).
- **BYOD Privacy Policy**: BYOD arrangements may appear to require consent but often have alternative bases (see byod-privacy-policy skill).
