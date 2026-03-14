---
name: background-check-privacy
description: >-
  Manages privacy compliance for employee background checks including criminal
  record processing under Art. 10 GDPR, DBS checks (UK), national law
  variations, and reference verification. Applies proportionality and data
  minimisation to pre-employment screening, defines retention limits, and
  addresses role-based necessity assessments. Keywords: background check,
  criminal record, Art. 10, DBS, pre-employment screening, vetting,
  data minimisation, proportionality.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: employee-data-privacy
  tags: "background-check, criminal-record, article-10, dbs, pre-employment-screening, data-minimisation"
---

# Background Check Privacy

## Overview

Pre-employment background checks involve processing personal data that ranges from routine reference verification to highly sensitive criminal record data. Art. 10 GDPR provides specific restrictions on processing data relating to criminal convictions and offences, requiring that such processing be authorised by EU or Member State law providing appropriate safeguards. Beyond criminal data, background checks may involve credit history, educational qualifications, professional registration, social media presence, and right-to-work verification — each carrying distinct proportionality and data minimisation requirements. The principle that governs all background checking is role-based necessity: the scope of a background check must be proportionate to the specific role and its associated risks, not applied uniformly across all positions.

## Legal Framework

### Art. 10 — Criminal Conviction Data

"Processing of personal data relating to criminal convictions and offences or related security measures based on Article 6(1) shall be carried out only under the control of official authority or when the processing is authorised by Union or Member State law providing for appropriate safeguards for the rights and freedoms of data subjects."

**Key requirements**:
- Criminal data processing requires specific national law authorisation (not merely a legitimate interest)
- The national law must provide appropriate safeguards
- A comprehensive register of criminal convictions may be kept only under the control of official authority

### Art. 6(1) — Lawful Basis for Background Checks Generally

| Check Type | Lawful Basis | Notes |
|-----------|-------------|-------|
| Reference verification | Art. 6(1)(b) contract + Art. 6(1)(f) legitimate interest | Necessary for employment decision; limited to professional references |
| Criminal record check | Art. 6(1)(c) legal obligation or Art. 6(1)(e) public task | Only where national law mandates or authorises the check for the specific role |
| Credit check | Art. 6(1)(f) legitimate interest | Limited to roles with financial responsibility; must pass balancing test |
| Qualification verification | Art. 6(1)(b) contract | Necessary to verify contractual requirements |
| Right-to-work check | Art. 6(1)(c) legal obligation | Mandatory under national immigration law |
| Social media screening | Art. 6(1)(f) legitimate interest | Highly restricted; see detailed analysis below |
| Health screening | Art. 9(2)(b) + national law | Only where role requires specific fitness standard |

### National Criminal Record Check Frameworks

#### United Kingdom — DBS (Disclosure and Barring Service)

Three levels of disclosure:
| Level | Content | Eligible Roles |
|-------|---------|---------------|
| Basic DBS | Unspent convictions only | Any role; self-applied by the individual |
| Standard DBS | Spent and unspent convictions, cautions, reprimands, final warnings | Roles listed in the Rehabilitation of Offenders Act 1974 (Exceptions) Order 1975 (e.g., solicitors, accountants, healthcare professionals) |
| Enhanced DBS | Standard + relevant police intelligence + barred list check where applicable | Regulated activity involving children or vulnerable adults, positions of trust in national security |

**Key GDPR compliance requirements**:
- The Rehabilitation of Offenders Act 1974 prohibits considering spent convictions for most employment purposes
- DBS certificates belong to the applicant, not the employer
- Employers should not retain a copy of the DBS certificate; they should record only the DBS certificate number, date of issue, and the result (clear/not clear)
- DBS Update Service allows ongoing status checks without requesting new certificates

#### Germany — Führungszeugnis (Certificate of Good Conduct)

- Belegart N (standard): Shows convictions with sentences exceeding 90 daily rates or 3 months imprisonment (with exceptions)
- Belegart O (extended): Includes all convictions for roles involving minors
- Employers may request a Führungszeugnis only where the role justifies it; routine requests for all positions are disproportionate
- Employers may view the certificate but should not retain a copy; they should record only the confirmation that the check was satisfactory

#### France — Extrait de Casier Judiciaire

- Bulletin No. 3 (most common for employment): Shows only the most serious convictions (imprisonment over 2 years without suspension)
- Employer may request Bulletin No. 3 only for specific roles justified by the nature of the activity
- For public sector roles, the administration may access Bulletin No. 2 directly

#### Netherlands — Verklaring Omtrent het Gedrag (VOG)

- The VOG (Certificate of Conduct) is issued by the Ministry of Justice
- The VOG states only whether the individual's judicial record contains relevant information for the specific role — it does not disclose the convictions themselves
- The employer specifies the screening profile (e.g., "persons" for working with vulnerable people, "finances" for financial roles)

### Spent Convictions — Rehabilitation Principle

Most European jurisdictions implement the rehabilitation principle: after a specified period, convictions become "spent" and may no longer be considered for employment purposes. Processing spent convictions where they are protected by rehabilitation legislation violates both national law and the GDPR data minimisation principle.

| Jurisdiction | Rehabilitation Framework | Key Rule |
|-------------|------------------------|----------|
| UK | Rehabilitation of Offenders Act 1974 | Spent convictions may not be disclosed or considered except for excepted roles |
| Germany | BZRG (Federal Central Register Act) | Convictions removed from certificate after specified periods (5-15 years) |
| France | Art. 133-16 Code pénal | Automatic rehabilitation after specified periods |
| Netherlands | Wet justitiële en strafvorderlijke gegevens | Judicial data removed after 20 years (adults) or 5 years (minors) |

## Proportionality Framework

### Role-Based Necessity Assessment

Not all roles justify the same level of background checking. The proportionality principle requires that the scope of checks be tailored to the specific risks of the role.

| Role Category | Appropriate Checks | Disproportionate Checks |
|--------------|-------------------|------------------------|
| General office worker | Right-to-work, references, qualification verification | Criminal record, credit check, social media screening |
| Financial controller | Right-to-work, references, qualifications, credit check, basic criminal record (fraud offences) | Enhanced criminal record, social media screening |
| Teacher / youth worker | Right-to-work, references, qualifications, enhanced criminal record with barred list | Credit check, social media screening |
| Security guard | Right-to-work, references, SIA licence verification, standard criminal record | Enhanced criminal record (unless regulated activity), credit check |
| Warehouse operative | Right-to-work, references | Criminal record (unless handling high-value goods), credit check, qualification verification |
| Senior executive | Right-to-work, references, qualifications, directorship checks, basic criminal record | Enhanced criminal record (unless regulated role) |

**Atlas Manufacturing Group Example**: Atlas conducted a proportionality review of its background check programme and found that it was requesting basic DBS checks for all positions including warehouse operatives and canteen staff. Following DPO advice, Atlas implemented a tiered checking framework:
- All roles: right-to-work verification, two professional references
- Roles with financial access (finance, procurement, senior management): credit check + basic DBS
- Roles with access to R&D laboratory: basic DBS (given intellectual property value)
- Roles working with site visitors under 18 (apprenticeship supervisors): enhanced DBS with barred list

### Social Media Screening

Social media screening of candidates is one of the most privacy-invasive background check activities. It may reveal:
- Political opinions (Art. 9(1))
- Religious or philosophical beliefs (Art. 9(1))
- Trade union membership (Art. 9(1))
- Health information (Art. 9(1))
- Sexual orientation (Art. 9(1))
- Racial or ethnic origin (Art. 9(1))

**When social media screening may be justified**:
- Public-facing roles where the candidate's public statements may directly affect the organisation's reputation
- Senior leadership roles with significant public profile
- Roles requiring security clearance where national law authorises screening

**Requirements if conducted**:
- Limited to publicly available information (no friend requests, no fake profiles)
- Limited to information relevant to the role
- Conducted at the latest possible stage (after shortlisting, before final offer)
- Documented with a clear record of what was reviewed and what was found
- Candidate must be informed that social media screening is part of the process
- Special category data encountered incidentally must not be recorded or used in the employment decision

## Data Minimisation and Retention

### Data Minimisation in Collection

- Collect only the specific check results relevant to the role, not blanket screening
- Do not retain copies of identity documents beyond the verification point (photograph the document, verify, delete the image — retain only a record that verification was completed)
- Do not retain copies of criminal record certificates — record only the certificate reference number, date, and result
- Do not collect more references than needed (two professional references is standard; personal character references are generally disproportionate)

### Retention Limits

| Data Type | Retention Period | Justification |
|-----------|-----------------|---------------|
| Right-to-work verification record | Duration of employment + 2 years | Legal obligation (Immigration Act requirements) |
| Reference responses | 6 months from hire decision | Sufficient for probation period disputes |
| Criminal record check result (reference number + outcome only) | Duration of employment | Required for ongoing regulatory compliance in regulated roles |
| Credit check result | 6 months from hire decision | No ongoing necessity after employment decision |
| Qualification verification records | Duration of employment | Ongoing professional registration may be required |
| Social media screening notes | 6 months from hire decision or immediately if candidate not hired | Minimal retention; highly sensitive |
| Unsuccessful candidate background check data | 6 months maximum | Legal claim limitation period (extended to 12 months if discrimination claim risk identified) |

### Unsuccessful Candidates

Background check data for candidates who are not hired must be:
- Deleted within 6 months of the hiring decision (12 months where a discrimination claim risk is identified)
- Not retained in a general candidate database for future recruitment
- Deleted earlier if the candidate withdraws consent or requests erasure

## Candidate Rights

### Right to Be Informed — Art. 13

Before conducting any background check, the candidate must be informed of:
- The specific checks that will be conducted
- The lawful basis for each check
- Who will conduct the checks (third-party screening provider, if applicable)
- What data will be obtained
- How the data will be used in the employment decision
- Retention periods
- Their rights under Arts. 15-22

### Right to Challenge

- Candidates must be given the opportunity to discuss and challenge adverse check results before a final employment decision is made
- If a criminal record check reveals a conviction, the candidate must be allowed to provide context (rehabilitation evidence, mitigating circumstances)
- An automatic disqualification policy (rejecting any candidate with any criminal record) is unlawful — each case must be assessed individually, considering the nature of the offence, its relevance to the role, and the time elapsed

## Third-Party Screening Providers

Where background checks are conducted by a third-party provider:
- A Data Processing Agreement under Art. 28 GDPR must be in place
- The provider is a processor acting on the employer's (controller's) instructions
- The employer must specify what checks may be conducted; the provider must not conduct checks beyond the scope authorised
- The provider must delete check data after transmitting results to the employer, per the agreed retention schedule
- International transfers (common with global screening providers) must comply with Chapter V GDPR

## Enforcement Precedents

| Authority | Case | Fine/Outcome | Key Issue |
|-----------|------|-------------|-----------|
| ICO (UK) | Experian, 2020 | Enforcement notice | Experian's employment screening services processed personal data without adequate transparency to data subjects |
| CNIL (France) | SAN-2019-007 | EUR 30,000 | Employer retained criminal record certificates in personnel files beyond the verification period |
| AEPD (Spain) | PS/00321/2020 | EUR 50,000 | Employer conducted social media screening of candidates without informing them and used special category data in hiring decisions |
| Autoriteit Persoonsgegevens (NL) | 2021 Investigation | Corrective order | Employer requested VOG for all roles without role-based necessity assessment |
| Garante (Italy) | Provvedimento 2020-0893 | Warning | Employer retained background check data for unsuccessful candidates for 5 years — excessive retention |

## Integration Points

- **Employment Consent Limits**: Consent is not the appropriate lawful basis for most background checks (see employment-consent-limits skill).
- **Employee DSAR Response**: Candidates and employees may request access to background check data (see employee-dsar-response skill).
- **HR System Privacy Config**: Background check data storage and access must be configured with appropriate restrictions (see hr-system-privacy-config skill).
- **Employee Health Data**: Pre-employment health screening is governed by separate rules (see employee-health-data skill).
