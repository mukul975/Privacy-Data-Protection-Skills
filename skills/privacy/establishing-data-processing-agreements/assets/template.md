# Data Processing Agreement

## Between Nexus Technologies GmbH (Controller) and CloudVault Storage Ltd (Processor)

**DPA Reference**: DPA-2026-CV-001
**Effective Date**: 2026-01-15
**Associated Service Agreement**: MSA-2025-CV-003

---

## Schedule 1: Processing Details

| Element | Detail |
|---------|--------|
| Subject-matter | Cloud storage and backup of customer and employee records |
| Duration | Co-terminous with MSA-2025-CV-003 (initial term: 36 months from 2025-07-01) |
| Nature of processing | Storage, backup, replication, retrieval, and deletion of personal data files |
| Purpose | Providing secure cloud storage infrastructure for the Controller's business records |
| Types of personal data | Employee records (name, contact details, employment history, payroll data, tax IDs); Customer records (name, contact details, order history, billing information) |
| Categories of data subjects | Controller's employees (approximately 380), contractors (approximately 45), customers (approximately 145,000) |
| Special category data | Limited: employee occupational health records (Art. 9(1) health data) stored in encrypted containers |

---

## Schedule 2: Technical and Organisational Measures

| Measure | Implementation |
|---------|---------------|
| Encryption at rest | AES-256 (customer-managed keys via AWS KMS) |
| Encryption in transit | TLS 1.3 for all API and data transfer connections |
| Access control | RBAC with quarterly access reviews; MFA required for all administrative access |
| Logging | All data access logged with immutable audit trail retained for 24 months |
| Physical security | ISO 27001 certified data centres in Frankfurt (eu-central-1) and Dublin (eu-west-1) |
| Backup | Daily automated backups with 30-day retention; geo-redundant replication within EEA |
| Incident detection | 24/7 SOC monitoring with automated alerting; average detection time under 15 minutes |
| Penetration testing | Annual third-party penetration test (most recent: Secureworks, November 2025) |
| Certifications | ISO 27001:2022 (cert. no. IS-784521), SOC 2 Type II (report dated October 2025) |

---

## Schedule 3: Sub-Processors

| Sub-Processor | Processing | Location | Safeguard |
|--------------|-----------|----------|-----------|
| Amazon Web Services EMEA SARL | Infrastructure hosting (IaaS) | Frankfurt, Germany | EU entity; no third-country transfer |
| Veeam Software Group GmbH | Backup orchestration software | Prague, Czech Republic | EU entity; no third-country transfer |

**Authorisation model**: General written authorisation with 30-day advance notification of changes.

---

## Core Clauses (Art. 28(3)(a)-(h))

### Clause 1: Documented Instructions (Art. 28(3)(a))

The Processor shall process personal data only on documented instructions from the Controller, as set out in this DPA and the associated service agreement. The Processor shall not process personal data for any other purpose. If the Processor is required by EU or Member State law to process personal data beyond these instructions, the Processor shall inform the Controller of that legal requirement before the relevant processing, unless that law prohibits such notification on important grounds of public interest.

### Clause 2: Confidentiality (Art. 28(3)(b))

The Processor shall ensure that all persons authorised to process personal data under this DPA have committed to confidentiality through written non-disclosure agreements or are under an appropriate statutory obligation of confidentiality. The Processor currently has 23 employees with access to the Controller's data, all of whom have signed confidentiality agreements dated no later than their first day of employment.

### Clause 3: Security (Art. 28(3)(c))

The Processor shall implement and maintain the technical and organisational measures specified in Schedule 2, which the Controller has reviewed and confirmed as appropriate for the risk profile of the processing. The Processor shall not materially reduce the level of security without prior written consent from the Controller.

### Clause 4: Sub-Processors (Art. 28(3)(d), 28(2), 28(4))

The Controller provides general written authorisation for the sub-processors listed in Schedule 3. The Processor shall notify the Controller at least 30 calendar days before engaging any new sub-processor or replacing an existing one, providing the sub-processor's identity, location, and a description of the processing. The Controller may object in writing within 15 calendar days of notification. If the Controller objects and the parties cannot resolve the objection within 30 days, the Controller may terminate the affected processing services without penalty. The Processor shall impose the same data protection obligations on all sub-processors by written contract.

### Clause 5: Data Subject Rights Assistance (Art. 28(3)(e))

The Processor shall assist the Controller in responding to data subject requests under Articles 15-22 by providing technical capabilities for data export (Art. 20 portability), data deletion (Art. 17 erasure), and data rectification (Art. 16). The Processor shall notify the Controller within 48 hours if it receives a data subject request directly and shall not respond to such requests without the Controller's instructions.

### Clause 6: Compliance Assistance (Art. 28(3)(f))

The Processor shall assist the Controller in ensuring compliance with Articles 32-36 by: providing security documentation for DPIA purposes, notifying the Controller of any security incidents, and supporting the Controller in responding to supervisory authority requests relating to the processing.

### Clause 7: Data Return and Deletion (Art. 28(3)(g))

Upon termination or expiry of this DPA, the Processor shall, at the Controller's choice: (a) return all personal data to the Controller in a standard machine-readable format (CSV or JSON) within 30 calendar days; or (b) securely delete all personal data and all existing copies within 30 calendar days and provide written certification of deletion signed by the Processor's CISO. Deletion shall use NIST SP 800-88 compliant methods.

### Clause 8: Audit Rights (Art. 28(3)(h))

The Processor shall make available to the Controller all information necessary to demonstrate compliance with Art. 28 obligations. The Controller may conduct audits, including on-site inspections, with 30 calendar days' notice, during normal business hours, and no more than once per year (unless a breach or regulatory investigation necessitates additional audits). The Processor shall provide the most recent SOC 2 Type II report and ISO 27001 certificate upon request as evidence of ongoing compliance.

---

## Breach Notification (Art. 33(2))

The Processor shall notify the Controller without undue delay, and in any event within 24 hours, after becoming aware of a personal data breach affecting the Controller's data. The notification shall include: (a) the nature of the breach, (b) the categories and approximate number of data subjects affected, (c) the likely consequences, and (d) the measures taken or proposed to address the breach.

---

**Signed for Nexus Technologies GmbH**: Dr. Katharina Weiss, DPO — 2026-01-15
**Signed for CloudVault Storage Ltd**: Rachel Thompson, Head of Legal — 2026-01-15
