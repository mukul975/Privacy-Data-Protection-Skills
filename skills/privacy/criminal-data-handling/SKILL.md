---
name: criminal-data-handling
description: >-
  Handles GDPR Art. 10 criminal conviction and offence data classification
  including official authority requirements, national law derogations, and
  comprehensive register restrictions. Covers controller obligations for
  criminal background checks and offence records. Keywords: criminal data,
  Art 10, conviction data, offence records, criminal background, DBS check.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-classification
  tags: "criminal-data, art-10, conviction-data, offence-records, background-check, dbs"
---

# Criminal Conviction and Offence Data Handling — GDPR Art. 10

## Overview

Article 10 of the GDPR establishes a separate regime for processing personal data relating to criminal convictions and offences, or related security measures. Unlike Art. 9 special category data which is subject to a general prohibition with listed exceptions, Art. 10 permits processing only under the control of official authority, or when authorised by EU or Member State law providing appropriate safeguards. The maintenance of a comprehensive register of criminal convictions is restricted to processing under the control of official authority. This skill provides a framework for identifying, classifying, and lawfully processing criminal data within enterprise contexts.

## Legal Framework — Art. 10

### Text of Article 10

"Processing of personal data relating to criminal convictions and offences or related security measures based on Article 6(1) shall be carried out only under the control of official authority or when the processing is authorised by Union or Member State law providing for appropriate safeguards for the rights and freedoms of data subjects. Any comprehensive register of criminal convictions shall be kept only under the control of official authority."

### Three Key Requirements

| Requirement | Description | Practical Implication |
|-------------|-------------|----------------------|
| **Official authority control** | Processing must be supervised by or conducted under the authority of a public body with legal competence | Private sector organisations generally cannot process criminal data unless authorised by specific national law |
| **National law authorisation** | EU or Member State law must specifically authorise the processing and provide appropriate safeguards | Controllers must identify the specific legal provision authorising each criminal data processing activity |
| **Comprehensive register prohibition** | No private entity may maintain a comprehensive register of criminal convictions | Aggregating criminal records across individuals for database purposes requires official authority status |

### Relationship to Art. 6 Lawful Basis

Art. 10 operates as an additional layer on top of Art. 6. A controller processing criminal data must satisfy BOTH:
1. A lawful basis under Art. 6(1) — typically Art. 6(1)(c) (legal obligation) or Art. 6(1)(f) (legitimate interests, where national law permits)
2. One of the Art. 10 conditions — official authority control OR national law authorisation with appropriate safeguards

### Relationship to Art. 9

Criminal data is NOT listed in Art. 9(1) as a special category, but Member States may impose Art. 9-equivalent protections. Some data may fall under both Art. 9 and Art. 10 — for example, data about a criminal offence that also reveals racial profiling concerns or political activity.

## Scope of Criminal Data

### Data Elements Within Art. 10 Scope

| Category | Examples | Notes |
|----------|---------|-------|
| **Criminal convictions** | Conviction records, sentences, court judgments | Core Art. 10 scope |
| **Criminal offences** | Charges, indictments, allegations of criminal conduct | Includes unproven allegations |
| **Related security measures** | Probation orders, restraining orders, electronic monitoring conditions | Post-conviction measures |
| **Criminal proceedings** | Arrest records, bail conditions, court appearance dates | Procedural data |
| **Acquittals and dismissals** | Records of charges dropped or acquittals | Still criminal data under Art. 10 |
| **Cautions and warnings** | Police cautions, penalty notices for disorder | Out-of-court disposals |
| **Spent convictions** | Convictions that are rehabilitated under national law (UK: Rehabilitation of Offenders Act 1974) | May have additional protections under national law |

### Data Elements Outside Art. 10 Scope

| Data | Reason |
|------|--------|
| Civil litigation records | Art. 10 covers criminal matters only |
| Regulatory enforcement actions (fines by supervisory authorities) | Administrative, not criminal |
| Disciplinary proceedings (employment misconduct) | Internal employment matter, not criminal |
| Credit defaults and county court judgments | Civil debt matters |
| Self-reported general "good character" statements | Not specific criminal data |

### Boundary Cases at Vanguard Financial Services

| Scenario | Art. 10 Applicable? | Reasoning |
|----------|---------------------|-----------|
| DBS (Disclosure and Barring Service) check results for new hires in regulated roles | YES | Contains criminal conviction and caution data |
| FCA (Financial Conduct Authority) fitness and propriety checks | YES — where criminal history is assessed | FCA Senior Managers and Certification Regime requires criminal history disclosure |
| Anti-money laundering suspicious activity reports (SARs) | BORDERLINE — YES when the SAR relates to suspected criminal activity | SAR data may constitute data relating to criminal offences (suspected fraud, money laundering) |
| Internal investigation into suspected employee fraud | YES — if the investigation relates to conduct that would constitute a criminal offence | Even where no charges are brought, investigation data relating to criminal offences falls under Art. 10 |
| Sanctions screening results | NO — unless a sanctions match relates to criminal conviction or offence | Sanctions are typically administrative/regulatory measures |

## National Law Derogations

### United Kingdom — Data Protection Act 2018

- **Schedule 1, Part 1**: Conditions for processing criminal conviction data under Art. 10 — includes processing necessary for employment purposes, regulatory requirements, preventing or detecting unlawful acts, protecting the public
- **Schedule 1, Part 2**: Substantial public interest conditions — includes safeguarding of children and vulnerable adults, regulatory requirements relating to fraud
- **Rehabilitation of Offenders Act 1974**: Spent convictions must not be disclosed or used in most employment contexts. Exceptions exist for regulated activities (financial services, healthcare, childcare) listed in the Rehabilitation of Offenders Act 1974 (Exceptions) Order 1975
- **DBS Checks**: Enhanced DBS checks available only for prescribed positions; basic DBS check available for any purpose with the individual's consent

### Germany — BDSG §§ 26, 85

- **§ 26 BDSG**: Employee criminal data may be processed where necessary for the employment relationship and proportionate. Processing of criminal data of job applicants is permitted only where the offence is relevant to the specific role
- **Criminal Register Act (Bundeszentralregistergesetz, BZRG)**: Federal Central Criminal Register managed exclusively by the Federal Office of Justice. Private entities cannot maintain criminal registers

### France — Code pénal, Art. 226-19; CNIL Authorisation

- Criminal data processing by private entities requires specific CNIL authorisation or explicit legal basis
- Bulletin No. 3 of the criminal record (casier judiciaire) may be requested by employers only for positions specified by law

### Netherlands — UAVG Art. 32

- Processing of criminal data by private entities permitted only where specifically authorised by law or with explicit consent of the data subject
- Verklaring Omtrent het Gedrag (VOG/Certificate of Good Conduct) system managed by Justis (Screening Authority)

## Classification Methodology

### Step 1: Identify Criminal Data Elements

For each system, scan for data elements that may contain criminal data:

| Detection Pattern | Field Examples | Confidence |
|------------------|---------------|-----------|
| Criminal record identifiers | `criminal_record_number`, `dbs_certificate_number`, `police_reference` | High |
| Offence classifications | `offence_code`, `charge_description`, `conviction_type` | High |
| Court and sentencing data | `court_name`, `sentence_type`, `sentence_duration`, `judge_name` | High |
| Investigation references | `investigation_id`, `sar_reference`, `fraud_case_number` | Medium |
| Background check results | `dbs_result`, `background_check_status`, `criminal_history_flag` | High |
| Free-text fields containing criminal terminology | Any field containing "convicted", "arrested", "charged", "offence", "sentence" | Low — requires manual review |

### Step 2: Determine Art. 10 Applicability

For each identified element:
1. Confirm the data relates to a criminal conviction, offence, or related security measure
2. Distinguish from civil, administrative, or disciplinary matters
3. For borderline cases (e.g., SARs, internal investigations), assess whether the underlying conduct would constitute a criminal offence

### Step 3: Identify National Law Authorisation

For each Art. 10 data element:
1. Identify the specific national law provision authorising the processing
2. Confirm the law provides "appropriate safeguards" as required by Art. 10
3. Document any additional national restrictions (e.g., Rehabilitation of Offenders Act spent conviction protections)

### Step 4: Assess Comprehensive Register Risk

Review whether any system maintains what could constitute a "comprehensive register of criminal convictions":
- A database aggregating criminal records across multiple individuals
- A system that enables searching/querying criminal history across a population
- Even partial aggregation may raise comprehensive register concerns if it covers a defined population comprehensively

### Step 5: Apply Classification Label

- `CRIMINAL_ART10`: Data within Art. 10 scope with identified national law authorisation
- `CRIMINAL_ART10_NO_AUTH`: Data within Art. 10 scope WITHOUT identified national law authorisation (processing must cease until authorisation established)
- `CRIMINAL_SPENT`: Spent conviction data subject to additional Rehabilitation of Offenders Act protections
- `NOT_CRIMINAL`: Data reviewed and confirmed outside Art. 10 scope

## Implementation at Vanguard Financial Services

### Systems Processing Criminal Data

| System | Data Elements | National Law Basis | Purpose |
|--------|-------------|-------------------|---------|
| **HR Recruitment Platform** | DBS check results (basic and enhanced), criminal declaration forms | UK DPA 2018 Sch.1 Part 1 para 1 (employment); Rehabilitation of Offenders Act 1974 (Exceptions) Order 1975 | Pre-employment screening for FCA-regulated roles |
| **Compliance Case Management** | SAR data, internal investigation records, regulatory referral records | UK Proceeds of Crime Act 2002 s.330-332 (SAR obligations); UK DPA 2018 Sch.1 Part 2 para 14 (preventing/detecting unlawful acts) | AML compliance, fraud investigation |
| **FCA Regulatory Reporting** | Senior Manager criminal history declarations, Approved Person criminal record disclosures | Financial Services and Markets Act 2000 s.61 (fitness and propriety); FCA SUP 10C | Regulatory fitness and propriety assessments |
| **Third-Party Due Diligence** | Criminal background check results for vendors and counterparties | UK DPA 2018 Sch.1 Part 2 para 6 (regulatory requirements); Money Laundering Regulations 2017 reg.28 | Know Your Customer, vendor risk management |

### Safeguards Required

| Safeguard | Implementation |
|-----------|---------------|
| **Access restriction** | Criminal data accessible only to designated Compliance and HR personnel with specific role-based access. Named individual authorisation list maintained. |
| **Purpose limitation** | Criminal data processed only for the specific purpose authorised by law. No secondary use for general HR analytics or performance management. |
| **Retention limitation** | DBS check results retained for maximum 6 months after recruitment decision. SAR data retained per Proceeds of Crime Act retention schedules. |
| **Data minimisation** | Only the outcome of criminal checks recorded (clear/not clear + relevant details), not the full criminal record unless required by specific regulation. |
| **Logging and audit** | All access to criminal data logged with user identity, timestamp, and purpose. Quarterly audit of access logs by DPO. |
| **Spent conviction handling** | System flag for spent convictions. Spent convictions excluded from standard employment checks. Visible only for roles exempt under the Exceptions Order (FCA-regulated positions). |

## Enforcement Precedents

- **Metropolitan Police Service v Information Commissioner (UK First-Tier Tribunal, 2014)**: Tribunal addressed the scope of "criminal offence data" and confirmed that allegations of criminal conduct, even where unproven, constitute criminal data requiring Art. 10-equivalent protections
- **ICO Enforcement Notice — Experian Ltd (2020)**: ICO found Experian's processing of personal data in its marketing services business, which included data indicative of financial crime risk, lacked appropriate lawful basis and transparency
- **CNIL Decision SAN-2022-023 — Clearview AI**: While primarily an Art. 9 biometric case, the decision also addressed Clearview's processing of data relating to criminal investigations and the requirement for official authority control when aggregating such data
- **Austrian DPA — CRIF GmbH (2021)**: Fined for maintaining a database of criminal-related financial data (insolvency linked to fraud convictions) without adequate national law authorisation under Art. 10

## Integration Points

- **special-category-data**: Criminal data may overlap with Art. 9 categories (e.g., political offences revealing political opinions)
- **data-inventory-mapping**: Art. 30 RoPA must specifically identify Art. 10 data processing activities
- **classification-policy**: Criminal data classified as "Restricted" tier with enhanced handling procedures
- **cross-jurisdiction-class**: Criminal data protections vary significantly across jurisdictions — mapping required for multinational operations
