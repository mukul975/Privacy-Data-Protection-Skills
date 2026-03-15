# Criminal Data Processing Record — Art. 10 GDPR

## Organisation: Vanguard Financial Services
## Record Reference: ART10-2026-001
## Date: 2026-03-14
## Prepared By: Rebecca Jones, Compliance Manager
## Reviewed By: Dr. James Whitfield, Data Protection Officer

---

## 1. Processing Activity: Pre-Employment DBS Screening

| Field | Detail |
|-------|--------|
| **Activity ID** | ART10-HR-001 |
| **System** | HR Recruitment Platform (Workday Recruiting) |
| **Criminal Data Elements** | DBS certificate number, check date, result (clear/not clear), relevant conviction details (if applicable) |
| **Data Subjects** | Candidates for FCA-regulated roles (~450 checks annually) |
| **Purpose** | Pre-employment criminal background screening for fitness and propriety assessment |
| **Art. 6 Lawful Basis** | Art. 6(1)(c) — Legal obligation (FSMA 2000 s.61; FCA SUP 10C) |
| **Art. 10 Authorisation** | DPA 2018 Schedule 1, Part 1, Paragraph 1 — Employment, and Schedule 1, Part 2, Paragraph 6 — Regulatory requirements (FCA fitness and propriety) |
| **Rehabilitation of Offenders Act** | Enhanced DBS checks permitted — roles exempt under Exceptions Order 1975 (FCA controlled functions). Both spent and unspent convictions disclosed. |
| **DBS Check Level** | Enhanced DBS with barred list check (for roles with FCA controlled function designation) |

### Data Handling Procedures

| Control | Implementation |
|---------|---------------|
| **Collection** | Candidate submits DBS application through DBS online service. Enhanced check results returned to Vanguard as registered body. |
| **Recording** | HR records: certificate number, date, and outcome only. Full certificate NOT photocopied per ICO guidance. If convictions disclosed, relevant details recorded in secure compliance file. |
| **Access** | Restricted to: Head of HR (1), Senior Recruitment Manager (1), Compliance Officer (1), DPO (1). Four named individuals only. |
| **Storage** | Encrypted at rest in Workday with field-level encryption. Separate from general employee records. |
| **Retention** | 6 months from recruitment decision date. For successful candidates in FCA roles: duration of FCA approval + 3 years. |
| **Disposal** | Automated secure deletion at retention expiry. Digital overwrite verification logged. |
| **Audit** | All access logged with user ID, timestamp, and purpose. DPO quarterly review of access logs. |

### Risk Assessment for Disclosed Convictions

When a DBS check returns convictions, the following assessment framework is applied:

| Factor | Assessment Criteria |
|--------|-------------------|
| **Nature of offence** | Is the offence directly relevant to the role? (e.g., fraud conviction for financial services role — highly relevant) |
| **Seriousness** | Severity of the offence and sentence imposed |
| **Time elapsed** | How long ago did the offence occur? |
| **Pattern** | Single offence or pattern of offending? |
| **Rehabilitation** | Evidence of rehabilitation, training, changed circumstances |
| **Role requirements** | What are the specific trust and integrity requirements of the role? |
| **Regulatory requirements** | Does the FCA specifically require consideration of this type of offence? (FCA FIT 2.1.3) |
| **Proportionality** | Is exclusion from the role proportionate given all factors? |

**Decision Authority**: HR Director, with mandatory consultation with Head of Compliance for FCA-regulated roles.

**Documentation**: All risk assessments documented regardless of outcome. Unsuccessful candidates informed of the decision with reference to the Rehabilitation of Offenders Act where applicable.

---

## 2. Processing Activity: Anti-Money Laundering Investigations

| Field | Detail |
|-------|--------|
| **Activity ID** | ART10-COMP-001 |
| **System** | Compliance Case Management (NICE Actimize) |
| **Criminal Data Elements** | SAR reference numbers, suspected offence descriptions, investigation findings, NCA correspondence, law enforcement requests |
| **Data Subjects** | Customers and third parties subject to AML investigation (~200 cases annually) |
| **Purpose** | Detection and reporting of suspected money laundering and terrorist financing offences |
| **Art. 6 Lawful Basis** | Art. 6(1)(c) — Legal obligation (Proceeds of Crime Act 2002 s.330-332) |
| **Art. 10 Authorisation** | DPA 2018 Schedule 1, Part 2, Paragraph 10 — Preventing or detecting unlawful acts; Proceeds of Crime Act 2002 |
| **Tipping Off** | Art. 15 DSAR exemption applied under DPA 2018 Schedule 2, Part 1, Paragraph 2 (crime prevention) where disclosure would risk tipping off under POCA 2002 s.333A |

### Data Handling Procedures

| Control | Implementation |
|---------|---------------|
| **Collection** | Transaction monitoring alerts (NICE Actimize), staff reports, external intelligence |
| **Access** | MLRO (1), Deputy MLRO (1), AML Investigation Team (6). No access for front-line staff, relationship managers, or general compliance. |
| **Storage** | Isolated database segment within compliance system. Encrypted at rest and in transit. No replication to data warehouse or analytics systems. |
| **Retention** | 5 years from date of SAR filing (Money Laundering Regulations 2017 reg.40). If criminal proceedings initiated: until proceedings concluded + 1 year. |
| **Disposal** | Secure deletion with verification audit log. SAR filing confirmation retained separately for regulatory audit purposes. |
| **Reporting** | SARs filed to NCA via SAR Online system. No disclosure to data subject. |

---

## 3. Appropriate Policy Document — DPA 2018 s.11

### Document Reference: APD-CRIM-2026-v1.0

This Appropriate Policy Document is maintained as required by section 11 of the Data Protection Act 2018 when processing criminal conviction data under Schedule 1 conditions.

### Schedule 1 Conditions Relied Upon

| Processing Activity | Schedule 1 Condition | Art. 6 Basis |
|--------------------|---------------------|-------------|
| Pre-employment DBS screening | Part 1 para 1 (Employment) + Part 2 para 6 (Regulatory) | Art. 6(1)(c) |
| AML investigation and SAR filing | Part 2 para 10 (Preventing/detecting unlawful acts) | Art. 6(1)(c) |
| FCA fitness and propriety | Part 2 para 6 (Regulatory requirements) | Art. 6(1)(c) |
| Internal fraud investigation | Part 2 para 14 (Preventing fraud) | Art. 6(1)(f) |
| Third-party due diligence | Part 2 para 6 (Regulatory requirements) | Art. 6(1)(c) |

### Compliance with Data Protection Principles

| Principle | How Achieved |
|-----------|-------------|
| **Lawfulness, fairness, transparency** | Privacy notices inform data subjects of criminal data processing. Art. 10 legal basis documented per activity. Exemptions from transparency applied only where legally justified (tipping off). |
| **Purpose limitation** | Criminal data processed only for the specific authorised purpose. No secondary use for general analytics, performance management, or marketing. |
| **Data minimisation** | Only the minimum criminal data necessary is recorded. DBS outcomes recorded without full certificate reproduction. |
| **Accuracy** | Criminal data sourced from official channels (DBS, NCA). Regular verification against updated checks for ongoing FCA-regulated roles. |
| **Storage limitation** | Defined retention periods per activity (see above). Automated deletion triggers. |
| **Integrity and confidentiality** | Field-level encryption, named-individual access lists, comprehensive audit logging, quarterly DPO access reviews. |

### Retention and Erasure Policy

| Data Category | Retention Period | Trigger | Disposal Method |
|--------------|-----------------|---------|----------------|
| DBS results — unsuccessful candidates | 6 months from decision | Decision date | Secure digital overwrite |
| DBS results — FCA approved persons | Duration of approval + 3 years | Cessation of approval | Secure digital overwrite |
| SAR records | 5 years from filing | Filing date | Secure digital overwrite |
| Internal investigation records | Investigation closure + 2 years | Closure date | Secure digital overwrite |
| FCA fitness declarations | Duration of appointment + 6 years | Cessation of appointment | Secure digital overwrite |

---

*This record is maintained in accordance with GDPR Art. 10, UK Data Protection Act 2018, and Vanguard Financial Services Appropriate Policy Document APD-CRIM-2026-v1.0. Reviewed annually by the DPO. Next review: 2027-03-14.*
