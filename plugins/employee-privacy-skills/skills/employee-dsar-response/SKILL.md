---
name: employee-dsar-response
description: >-
  Manages Data Subject Access Request procedures for employee requests under
  Art. 15 GDPR. Covers scope of disclosable HR records, emails, CCTV footage,
  performance reviews, monitoring data, and training records. Implements
  third-party data redaction, legal professional privilege, exemptions for
  ongoing proceedings, and the one-month response timeline. Keywords: DSAR,
  subject access request, Art. 15, employee records, redaction, privilege,
  HR data, SAR.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: employee-data-privacy
  tags: "dsar, subject-access-request, article-15, employee-records, redaction, privilege"
---

# Employee DSAR Response

## Overview

Employee Data Subject Access Requests (DSARs) are among the most complex and resource-intensive DSARs that organisations receive. Unlike customer DSARs, which typically involve a defined set of transactional data, employee DSARs can span the entire employment lifecycle and encompass data held across dozens of systems: HR records, emails (sent, received, and about the employee), CCTV footage, access control logs, telephone recordings, performance reviews, investigation files, grievance records, occupational health reports, training records, payroll data, expense claims, monitoring data, and informal notes and communications between managers. The scope, combined with the need to redact third-party personal data and assess legal privilege, makes employee DSARs a distinct operational and legal challenge.

This skill provides a structured response process, a comprehensive data source inventory, and decision frameworks for the exemptions and redactions most commonly encountered in employee DSARs.

## Art. 15 — Right of Access

### What the Employee Is Entitled To

Under Art. 15(1), the employee has the right to obtain from the controller:

| Information | Detail |
|------------|--------|
| Confirmation of processing | Whether personal data concerning the employee is being processed |
| Access to the data | A copy of the personal data undergoing processing |
| Purposes | The purposes of the processing |
| Categories | The categories of personal data concerned |
| Recipients | Recipients or categories of recipients to whom data has been or will be disclosed |
| Retention | The envisaged period of storage, or criteria used to determine the period |
| Rights | The right to rectification, erasure, restriction, and objection |
| Source | Where data was not collected from the employee, information about the source |
| Automated decisions | The existence of automated decision-making including profiling under Art. 22, with meaningful information about the logic, significance, and envisaged consequences |
| Transfer safeguards | Where data is transferred to a third country, the appropriate safeguards under Art. 46 |

### Art. 15(3) — Format

The controller shall provide a copy of the personal data undergoing processing. For any further copies requested, the controller may charge a reasonable fee based on administrative costs. Where the request is made by electronic means, the information shall be provided in a commonly used electronic form, unless otherwise requested.

### Art. 15(4) — Third-Party Rights

"The right to obtain a copy referred to in paragraph 3 shall not adversely affect the rights and freedoms of others."

This provision is the legal basis for redacting third-party personal data from DSAR disclosures.

## Employee DSAR Data Source Inventory

### Comprehensive Search Scope

The following data sources must be searched when processing an employee DSAR:

| Data Source | System/Location | Data Types |
|------------|----------------|------------|
| HR Information System | Workday, SAP SuccessFactors, BambooHR, etc. | Personal details, employment history, contract, salary, benefits, absence records, performance ratings |
| Email system | Microsoft 365, Google Workspace | Emails sent by the employee, received by the employee, and about the employee |
| CCTV system | On-premise recording system | Video footage where the employee is identifiable |
| Access control system | Badge/proximity card system | Entry/exit logs, access attempts to restricted areas |
| Time and attendance | Timekeeping system, biometric readers | Clock-in/out records, attendance patterns |
| Payroll system | SAP, ADP, Sage | Salary history, tax records, pension contributions, benefits |
| Performance management | Workday, Lattice, Culture Amp, etc. | Performance reviews, objectives, competency assessments, calibration data, 360 feedback |
| Learning management system | Cornerstone, SAP LMS, etc. | Training records, certifications, mandatory training completion |
| Recruitment system | Greenhouse, Lever, Workable | Application data, interview notes, assessment scores (for recent hires) |
| Disciplinary and grievance files | HR case management, paper files | Investigation notes, witness statements, outcome letters |
| Occupational health records | OH provider system | Fitness-for-work reports, referral correspondence |
| Monitoring systems | DLP, web proxy, MDM | Email monitoring alerts, internet usage logs, device management data |
| Expenses system | Concur, Expensify | Expense claims, receipts, approval records |
| Informal records | Line manager email, notes, instant messages | Notes about the employee, performance observations, management discussions |
| Telephone system | Call recording platform | Recorded calls where the employee is a participant |
| IT system logs | Active Directory, service desk | Account activity, password resets, service desk tickets |
| File servers and SharePoint | Shared drives, collaboration platforms | Documents authored by or concerning the employee |

### Search Strategy

Not every data source must be searched exhaustively for every DSAR. The search scope should be proportionate to:

1. **The request scope**: If the employee has specified particular data they are seeking (e.g., "I request copies of all performance reviews from 2022-2025"), the search can be focused accordingly
2. **The employment context**: A current employee's DSAR typically spans the entire employment period; a former employee's data may have been partially deleted under retention policies
3. **Reasonableness**: Art. 12(5) allows refusal of requests that are "manifestly unfounded or excessive" — a request for "every email I was ever mentioned in" across a 20-year career may be excessive, but the bar for refusal is high

## Response Timeline

### Standard Timeline — Art. 12(3)

- **One calendar month** from receipt of the DSAR
- The month runs from the day after receipt (if received on 15 March, the deadline is 15 April)
- If the deadline falls on a weekend or public holiday, the deadline extends to the next working day (ICO guidance)

### Extension — Art. 12(3)

- The deadline may be extended by **two further months** where the request is complex or the controller has received numerous requests from the same individual
- The controller must inform the employee of the extension **within one month** of receipt, together with the reasons for the delay
- Employee DSARs frequently justify extension due to the volume of data sources, redaction complexity, and legal privilege review

### Employee DSAR Response Process

**Day 1: Receipt and Acknowledgment**
1. Log the DSAR in the central DSAR register with a unique reference number
2. Verify the employee's identity (for current employees, identity is typically confirmed through the employment relationship; for former employees, additional verification may be needed)
3. Send acknowledgment confirming receipt and expected response date
4. Assign a DSAR coordinator (typically from the privacy/DPO team)

**Days 2-5: Scoping**
1. Review the request to determine scope — is the request for all data, or specific categories?
2. If the request is unclear, contact the employee to clarify scope (the clarification period does not pause the clock unless the request genuinely cannot be processed without clarification — ICO guidance)
3. Map the request to the data source inventory
4. Identify custodians for each data source and issue collection instructions
5. Assess whether an extension is likely needed; if so, notify the employee within the first month

**Days 5-20: Collection**
1. Each data custodian searches their system(s) and exports relevant data
2. Email searches: search for the employee's name and email address in mailboxes of direct managers, HR business partners, and relevant stakeholders
3. CCTV: identify time periods and locations where footage may contain the employee
4. Paper files: retrieve physical personnel file and any archived records
5. All collected data must be logged with source, custodian, and date of extraction

**Days 15-25: Review and Redaction**
1. Review all collected data for personal data of the requesting employee
2. Identify and redact third-party personal data (see redaction framework below)
3. Identify and withhold legally privileged material (see privilege framework below)
4. Identify and assess any other applicable exemptions
5. Compile the disclosure package

**Days 25-30: Quality Check and Dispatch**
1. DPO or senior privacy officer reviews the disclosure package for completeness and proper redaction
2. Prepare a covering letter explaining: scope of search, any exemptions applied, the employee's right to complain to the supervisory authority
3. Deliver the disclosure to the employee via secure channel (encrypted email, secure portal, or registered post)

## Redaction Framework

### Third-Party Personal Data — Art. 15(4)

The right of access must not adversely affect the rights and freedoms of others. This requires redaction of third-party personal data unless:
- The third party has consented to disclosure, or
- It is reasonable in all circumstances to disclose without consent

**Redaction decision matrix**:

| Data Type | Redact? | Reasoning |
|-----------|---------|-----------|
| Names of other employees mentioned in emails about the requesting employee | Generally yes, unless the third party's name is already known to the requestor (e.g., their line manager) | Balance third-party privacy against requestor's right |
| Witness statements in disciplinary investigations | Redact witness identity; disclose substance of allegations | Witness confidentiality vs. right to know allegations |
| 360 feedback with named reviewers | Redact reviewer names; disclose feedback content | Reviewers' reasonable expectation of anonymity |
| Email addresses in CC fields | Generally redact unless already known to requestor | Minimal privacy expectation but apply consistently |
| References provided by the employee's former employer | Disclose — this is the requestor's personal data | The employee has a right to see references about them |
| Performance calibration meeting notes naming other employees | Redact other employees' names and performance data | Other employees' performance data is their personal data |

### Practical Redaction Technique

- Use permanent redaction (not highlight or track-changes redaction)
- Replace names with "Person A," "Person B" consistently throughout the disclosure
- Redact email addresses, phone numbers, and job titles that could identify third parties
- Do not redact the requesting employee's own data or information they already know

## Legal Privilege Exemption

### UK — DPA 2018, Schedule 2, Part 4, Paragraph 19

Personal data is exempt from Art. 15 to the extent that disclosure would involve disclosing information in respect of which a claim to legal professional privilege (LPP) or confidentiality of communications could be maintained in legal proceedings.

### Types of Privilege

| Privilege Type | Scope | Application |
|---------------|-------|------------|
| Legal advice privilege | Confidential communications between client and lawyer for the purpose of obtaining or giving legal advice | Employment law advice about the employee's situation, HR consulting legal counsel about a grievance |
| Litigation privilege | Communications created for the dominant purpose of litigation that is in progress or reasonably anticipated | Documents prepared in anticipation of an employment tribunal claim |
| Without prejudice privilege | Communications made in a genuine attempt to settle a dispute | Settlement negotiation correspondence |

### Privilege Review Process

1. All documents flagged as potentially privileged must be reviewed by legal counsel
2. Legal counsel determines whether privilege applies to each document
3. Privileged documents are withheld and listed in a privilege log
4. The covering letter to the employee must state that certain information has been withheld under the legal privilege exemption, without revealing the privileged content
5. If only part of a document is privileged, the non-privileged portions must be disclosed

## Other Exemptions Applicable to Employee DSARs

### Ongoing Proceedings Exemption

Where disclosure would prejudice ongoing legal proceedings, disciplinary investigations, or regulatory investigations:

| Scenario | Exemption | Scope |
|----------|-----------|-------|
| Active disciplinary investigation | May withhold investigation materials that would prejudice the investigation | Temporary — must be disclosed once the investigation concludes |
| Pending employment tribunal claim | Litigation privilege applies to documents prepared for the dominant purpose of litigation | Duration of the legal proceedings |
| Regulatory investigation (e.g., FCA, HSE) | May withhold documents that would prejudice the regulatory investigation | Coordinate with the regulator |

### Management Planning Exemption — UK DPA 2018, Schedule 2, Part 4, Paragraph 24

Personal data processed for management forecasting or management planning is exempt from Art. 15 to the extent that disclosure would prejudice the planning or forecasting. This may cover:
- Redundancy selection criteria before announcement
- Organisational restructuring plans naming affected employees
- Succession planning documents

**Limitation**: This exemption is narrow and temporary — it applies only while disclosure would genuinely prejudice the planning activity.

### Negotiations Exemption — UK DPA 2018, Schedule 2, Part 4, Paragraph 25

Personal data consisting of a record of the controller's intentions in relation to negotiations with the data subject is exempt to the extent that disclosure would prejudice those negotiations. This may cover:
- Employer's settlement offer strategy
- Planned salary adjustment before communication
- Internal discussion of disciplinary sanction before outcome notification

## Common Pitfalls

| Pitfall | Risk | Resolution |
|---------|------|-----------|
| Failing to search email for "about" data | Incomplete disclosure; ICO complaint | Search line manager and HR mailboxes for the employee's name |
| Over-redaction of manager names | Excessive withholding undermines the right of access | Manager names may be disclosed where the employment relationship means the employee already knows their identity |
| Missing the one-month deadline | Regulatory complaint; enforcement action | Implement automated deadline tracking; request extension early if needed |
| Disclosing third-party special category data | Breach of Art. 9 + third-party complaint | Review all disclosures for special category data of third parties |
| Ignoring informal records | Manager personal notes are personal data and must be searched | Include managers' informal notes in the search scope |
| Treating all DSAR as routine | Employee DSARs often indicate a grievance or impending legal claim | Alert legal counsel when a DSAR is received from an employee in a dispute |

## Atlas Manufacturing Group Example

Atlas received a DSAR from an employee who had recently been placed on a Performance Improvement Plan (PIP). The DSAR coordinator:

1. Logged the request and acknowledged within 24 hours
2. Scoped the request: employee sought "all personal data held about me"
3. Mapped data sources: HR system (SAP SuccessFactors), email (Microsoft 365 — employee's mailbox, line manager's mailbox, HR BP's mailbox), performance management (SuccessFactors Performance & Goals), time and attendance (badge system), occupational health (two referrals on file), CCTV (not requested but technically in scope — employee informed that CCTV search would require specific dates/locations), and the disciplinary file containing the PIP documentation
4. Extended the deadline by two months due to the volume of email data and the need for legal privilege review (the employee had instructed a solicitor, and settlement discussions were ongoing)
5. Redacted: names of other employees mentioned in performance calibration, witness names from an earlier informal investigation, and third-party email addresses
6. Withheld under privilege: three emails between the HR Director and employment lawyer regarding the PIP and potential tribunal claim, and the without-prejudice settlement correspondence
7. Disclosed: 847 pages of material including HR records, performance reviews, PIP documentation, line manager emails about performance, training records, and absence records
8. The covering letter listed exemptions applied, advised the employee of the right to complain to the ICO, and confirmed the search methodology

## Enforcement Precedents

| Authority | Case | Fine/Outcome | Key Issue |
|-----------|------|-------------|-----------|
| ICO (UK) | Mermaids, 2023 | Enforcement notice | Failure to respond to employee DSARs within statutory timeframe |
| CNIL (France) | SAN-2022-009 | EUR 800,000 | Employer failed to provide employee with access to performance evaluation data within one month |
| AEPD (Spain) | PS/00231/2021 | EUR 70,000 | Employer refused employee DSAR claiming disproportionate effort without conducting proper search |
| Autoriteit Persoonsgegevens (NL) | 2022 Decision | EUR 525,000 | Employer provided incomplete DSAR response, omitting email data about the employee |
| Garante (Italy) | Provvedimento 2021-0234 | Corrective order | Employer over-redacted employee DSAR response, withholding non-privileged management communications |
| Datainspektionen (Sweden) | DI-2022-1456 | SEK 200,000 | Employer failed to search backup systems for former employee's DSAR |

## Integration Points

- **Employee Monitoring DPIA**: Monitoring data is within DSAR scope (see employee-monitoring-dpia skill).
- **Employee Health Data**: Health data in DSARs must be handled with particular care regarding access controls (see employee-health-data skill).
- **HR System Privacy Config**: DSAR compliance depends on the HR system's ability to extract and export employee data (see hr-system-privacy-config skill).
- **Background Check Privacy**: Background check data for current/former employees is within DSAR scope (see background-check-privacy skill).
- **Whistleblower Data**: Whistleblower identity data has special access restrictions that may limit DSAR disclosure (see whistleblower-data skill).
