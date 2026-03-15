# Controller RoPA Entry — Helix Biotech Solutions GmbH

**Record ID**: RPA-2025-PAY-001
**Processing Activity**: Employee Payroll Processing
**Department**: Human Resources
**Processing Owner**: Julia Richter, HR Director
**Date Created**: 2024-03-15
**Last Reviewed**: 2025-01-20
**Next Review Due**: 2026-01-20
**Record Status**: Approved

---

## Art. 30(1)(a) — Controller Identity and Contact Details

| Field | Value |
|-------|-------|
| **Controller legal name** | Helix Biotech Solutions GmbH |
| **Registered address** | Leopoldstrasse 42, 80802 Munich, Germany |
| **Registration** | HRB 267891, Amtsgericht Munich |
| **Contact email** | privacy@helix-biotech.eu |
| **DPO** | Dr. Elena Voss, dpo@helix-biotech.eu, +49 89 7654 3210 |
| **Joint controller(s)** | None |
| **Art. 26 arrangement ref** | N/A |
| **EU representative (Art. 27)** | Not applicable (established in EEA) |

---

## Art. 30(1)(b) — Purposes of Processing

| # | Purpose | Lawful Basis (Art. 6(1)) | Art. 9(2) Condition (if applicable) |
|---|---------|-------------------------|-------------------------------------|
| 1 | Calculation and disbursement of monthly employee salaries, including statutory deductions for income tax and social insurance | Art. 6(1)(b) — performance of employment contract | N/A |
| 2 | Reporting salary data to Finanzamt Munich and Deutsche Rentenversicherung for tax and pension compliance | Art. 6(1)(c) — legal obligation (EStG Section 41a, SGB IV Section 28a) | N/A |

**Privacy notice reference**: PN-EMP-2024-001 (Employee Privacy Notice, distributed at onboarding via SAP SuccessFactors)

---

## Art. 30(1)(c) — Categories of Data Subjects

- [x] Employees (permanent)
- [x] Employees (fixed-term)
- [ ] Contractors / consultants
- [ ] Job applicants
- [ ] Clinical trial participants
- [ ] Patients
- [ ] Healthcare professionals
- [ ] Customers / clients
- [ ] Suppliers / vendor contacts
- [ ] Website visitors
- [ ] Shareholders / investors

---

## Art. 30(1)(c) — Categories of Personal Data

### Standard Personal Data

- [x] Name (full name, title)
- [x] Contact details (email, phone, postal address)
- [x] Date of birth / age
- [x] National identification numbers (tax ID, social security)
- [x] Financial data (bank account, salary, payment records)
- [x] Employment data (employee ID, role, department, work history)
- [ ] Authentication data (username, password hash)
- [ ] Device and technical data (IP address, browser, OS)
- [ ] Location data (GPS, IP-derived location)
- [ ] Image / video data (photo ID, CCTV)

### Special Category Data (Art. 9(1))

- [ ] Racial or ethnic origin
- [ ] Political opinions
- [x] Religious or philosophical beliefs (church tax indicator for Kirchensteuer processing)
- [ ] Trade union membership
- [ ] Genetic data
- [ ] Biometric data (for identification purposes)
- [x] Health data (disability status for Schwerbehindertenabgabe calculation under SGB IX)
- [ ] Data concerning sex life or sexual orientation
- [ ] None

### Criminal Conviction Data (Art. 10)

- [ ] Criminal conviction or offence data
- [x] None

**Additional legal basis for special categories**: Art. 9(2)(b) — processing necessary for obligations under employment and social security law (SGB IX Section 154, KiStG)

---

## Art. 30(1)(d) — Categories of Recipients

| Recipient | Type | Purpose of Disclosure | Agreement Reference |
|-----------|------|-----------------------|---------------------|
| SAP SE (SAP SuccessFactors) | Processor | Cloud payroll processing platform hosting and computation | DPA-2023-SAP-001 (signed 2023-06-15) |
| Finanzamt Munich | Public authority | Statutory tax reporting under EStG Section 41a | Legal obligation — no DPA required |
| Deutsche Rentenversicherung Bund | Public authority | Social insurance contribution reporting under SGB IV Section 28a | Legal obligation — no DPA required |
| Commerzbank AG | Processor | Salary payment execution via SEPA credit transfer | DPA-2024-CBK-003 (signed 2024-02-10) |
| KPMG AG Wirtschaftspruefungsgesellschaft | Processor | External payroll audit for annual financial statements | DPA-2024-KPM-001 (signed 2024-04-01) |

**Internal recipients**: HR Payroll team (3 named users: J. Richter, M. Bauer, S. Krause), Finance Controlling team (2 named users: T. Fischer, K. Schneider)

---

## Art. 30(1)(e) — International Transfers

| Destination Country | Recipient Entity | Data Categories Transferred | Transfer Mechanism | TIA Reference |
|--------------------|------------------|---------------------------|-------------------|---------------|
| United States | SAP America, Inc. (sub-processor of SAP SE) | Encrypted payroll backup replicas | EU-US Data Privacy Framework (SAP Inc. DPF certification, effective 2023-10-12) | TIA-2023-SAP-US-001 |

---

## Art. 30(1)(f) — Retention Periods

| Data Category | Retention Period | Legal Basis for Retention | Deletion / Anonymisation Method |
|---------------|-----------------|--------------------------|-------------------------------|
| Payroll records (salary slips, tax certificates) | 6 years from end of financial year of creation | Section 257(4) HGB, Section 147(3) AO | Automated deletion via SAP archiving job, verified by quarterly reconciliation |
| Bank account details | Duration of employment + 3 months post-termination | Proportionality assessment (final salary payments, corrections) | Manual deletion by HR Payroll team, logged in SAP change history |
| Tax identification numbers | 6 years from end of financial year of last tax certificate | Section 147(3) AO | Automated deletion via SAP archiving job |
| Disability status records | Duration of employment + 3 years for potential claims (Section 15(4) AGG) | Proportionality assessment for discrimination claims | Manual deletion by HR, documented in retention schedule log |

---

## Art. 30(1)(g) — Technical and Organisational Security Measures

### Technical Measures

- **Encryption at rest**: AES-256 for SAP SuccessFactors database storage; per-tenant encryption keys managed by SAP Key Management Service
- **Encryption in transit**: TLS 1.3 for all data transmission between Helix Biotech and SAP SuccessFactors; SFTP with PGP encryption for Finanzamt ELSTER submissions
- **Access control**: Role-based access control (RBAC) with named-user accounts; quarterly access reviews conducted by DPO office; principle of least privilege enforced
- **Authentication**: Multi-factor authentication (MFA) required for all SAP SuccessFactors access; hardware security keys for administrative accounts
- **Network security**: Network segmentation between HR systems and general corporate LAN; firewall rules restricting SAP SuccessFactors IP ranges
- **Backup**: Daily encrypted backups with 30-day retention; quarterly restore testing documented in IT operations log
- **Monitoring**: SAP SuccessFactors audit log with 2-year retention; SIEM integration via Splunk for anomaly detection on payroll data access
- **Testing**: Annual penetration testing of SAP SuccessFactors integration by SySS GmbH; latest report: PT-2024-HB-042 (2024-11-15)

### Organisational Measures

- **Training**: Mandatory annual data protection training for all employees; role-specific payroll data handling training for HR Payroll team (completed 2025-01-10)
- **Policies**: Data classification policy (POL-DC-001), acceptable use policy (POL-AU-002), clean desk policy (POL-CD-003)
- **Personnel**: Background checks for all HR staff with payroll access; confidentiality agreements signed at onboarding (template: CONF-HR-2023)
- **Incident response**: Incident response procedure (IRP-2024-001) with 4-hour initial assessment SLA; DPO notification within 8 hours of confirmed personal data breach
- **Certification**: ISO 27001:2022 certified (certificate ref: IS 782341, issued by TUeV Sued, valid until 2026-09-30)

---

## DPIA Assessment

| Question | Answer |
|----------|--------|
| Does this processing require a DPIA under Art. 35? | No |
| If yes, DPIA reference | N/A |
| DPIA approval date | N/A |
| If no, justification | Standard payroll processing for 320 employees does not meet Art. 35(3) criteria or BfDI DPIA blacklist criteria. Processing is not large-scale, does not involve systematic monitoring, and does not use new technologies. Disability status processing is limited to statutory calculations and does not involve profiling. |

---

## Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Processing Owner | Julia Richter | 2025-01-20 | J. Richter |
| Data Protection Officer | Dr. Elena Voss | 2025-01-22 | E. Voss |
| IT Security | Thomas Wehner | 2025-01-22 | T. Wehner |

---

*This record conforms to GDPR Article 30(1) requirements. Maintained in electronic form per Art. 30(3) and available to the supervisory authority on request per Art. 30(4).*
