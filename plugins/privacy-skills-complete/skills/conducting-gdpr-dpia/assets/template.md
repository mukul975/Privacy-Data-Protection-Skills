# Data Protection Impact Assessment Report

## DPIA Reference: DPIA-QLH-2026-0001

| Field | Value |
|-------|-------|
| Organisation | QuantumLeap Health Technologies |
| Processing Name | Employee Workplace Monitoring System |
| DPIA Version | 1.0 |
| Status | Approved with Conditions |
| Date Created | 2026-02-10 |
| Next Review Date | 2026-08-10 |
| DPO | Dr. Elena Vasquez, CIPP/E, CIPM |
| Processing Owner | Marcus Chen, Head of HR Operations |
| DPIA Lead | Dr. Elena Vasquez, DPO |

---

## 1. Screening Outcome

### Art. 35(3) Mandatory Triggers

| Trigger | Met? | Justification |
|---------|------|---------------|
| Art. 35(3)(a) — Systematic extensive profiling with significant effects | No | Monitoring produces departmental reports but does not generate individual profiling decisions with legal or similarly significant effects. Performance management decisions involve human review. |
| Art. 35(3)(b) — Large-scale special category or criminal data | No | No Art. 9 special categories or Art. 10 criminal data are processed. Health-related absence data is handled separately under a distinct processing activity. |
| Art. 35(3)(c) — Systematic large-scale public area monitoring | No | Monitoring is limited to corporate premises and systems; no publicly accessible areas are monitored. |

### EDPB WP248rev.01 Criteria Assessment

| Criterion | Met? | Justification |
|-----------|------|---------------|
| C1: Evaluation or scoring | Yes | Employee productivity metrics are scored and compared against departmental benchmarks. |
| C2: Automated decision-making with legal/significant effect | No | No automated decisions are made; all performance management decisions require human review and approval by HR. |
| C3: Systematic monitoring | Yes | Continuous monitoring of email metadata, internet usage, badge access, and productivity across all employees during working hours. |
| C4: Sensitive data or highly personal data | No | Processing is limited to workplace activity metadata. Content of communications is not accessed. |
| C5: Large-scale processing | No | 2,847 employees and 340 contractors across three locations — this is significant but not large-scale within the meaning of WP248rev.01. |
| C6: Matching or combining datasets | Yes | Email metadata, internet usage, badge access, and productivity metrics are combined per employee into weekly performance summaries. |
| C7: Vulnerable data subjects | Yes | Employees are considered vulnerable data subjects due to the power imbalance inherent in the employment relationship (WP29 Opinion 2/2017, p.7). |
| C8: Innovative technology | No | Standard enterprise monitoring tools; no novel technology applied. |
| C9: Processing preventing exercise of rights | No | Monitoring does not prevent employees from exercising data protection rights or accessing services. |

**Criteria met: 4 (C1, C3, C6, C7)**
**Determination: DPIA is required** (threshold is 2 or more criteria per WP248rev.01).

---

## 2. Systematic Description of Processing — Art. 35(7)(a)

### 2.1 Nature of Processing

QuantumLeap Health Technologies operates an employee workplace monitoring system that collects and processes the following data through automated means:

- **Email metadata**: Sender address, recipient address, timestamp, and subject line for all emails sent and received through corporate email accounts. Email body content is not accessed or stored.
- **Internet usage categories**: Website visits are classified into categories (e.g., business, news, social media, shopping) using CloudSecure Ltd's URL categorisation engine. Individual URLs are not logged; only the category and time spent per category are recorded.
- **Physical badge access logs**: Timestamp and location of badge swipes at building entrances, floor access points, and restricted areas.
- **Daily productivity metrics**: Application usage time, meeting attendance, and task completion rates aggregated into daily summaries by the enterprise resource planning system.

### 2.2 Scope

| Dimension | Detail |
|-----------|--------|
| Data subjects | 2,847 employees and 340 contractors with corporate accounts |
| Geographic scope | London (United Kingdom), Berlin (Germany), Dublin (Ireland) |
| Temporal scope | Continuous during working hours (08:00-20:00 local time) |
| Volume | Approximately 45,000 email metadata records, 12,000 internet category records, 28,000 badge events, and 3,187 productivity summaries per day |

### 2.3 Context

Monitoring is conducted in the context of the employment relationship. Employees are informed of monitoring through the Employee Privacy Notice (version 4.2, issued 2025-11-01), the Acceptable Use Policy (version 3.1), and individual employment contracts which include a monitoring clause. Works council consultation was completed on 2026-01-15 prior to implementation.

### 2.4 Purpose

| Purpose | Lawful Basis | Justification |
|---------|-------------|---------------|
| Workplace security and insider threat detection | Art. 6(1)(f) legitimate interest | Protection of trade secrets, patient data, and intellectual property in a regulated health technology environment |
| Regulatory compliance with FCA record-keeping | Art. 6(1)(c) legal obligation | SYSC 10A.1 requires recording of electronic communications for regulated activities |
| Employee performance management | Art. 6(1)(f) legitimate interest | Departmental productivity analysis to support resource allocation and identify training needs |
| IT infrastructure management | Art. 6(1)(f) legitimate interest | Network capacity planning and software licence optimisation based on usage patterns |

### 2.5 Technology Stack

| Component | Provider | Role | Location |
|-----------|----------|------|----------|
| Email metadata extraction | Microsoft 365 E5 Compliance Center | Collection of email metadata via journaling rules | EU data centres (Netherlands, Ireland) |
| Internet categorisation | CloudSecure Ltd | URL category classification and time tracking | United Kingdom (London data centre) |
| Badge access system | Nedap AEOS | Physical access logging | On-premises at each office location |
| Productivity analytics | SAP SuccessFactors | Aggregation of application usage and task metrics | EU data centre (Germany) |
| Data warehouse | PostgreSQL on AWS eu-west-1 | Central storage and reporting | Ireland (AWS eu-west-1) |

### 2.6 Data Flows

1. **Collection**: Email metadata extracted by Microsoft 365 journaling rules; internet categories classified by CloudSecure proxy; badge events transmitted from Nedap controllers; productivity metrics exported from SAP SuccessFactors.
2. **Transmission**: All data transmitted via TLS 1.3 encrypted connections to the central PostgreSQL data warehouse in AWS eu-west-1.
3. **Storage**: Data stored encrypted at rest using AES-256 in the PostgreSQL data warehouse.
4. **Processing**: Weekly aggregation scripts produce departmental summaries. Individual-level data accessible only by HR department and IT Security team.
5. **Disclosure**: Aggregated departmental reports shared with department heads. Individual data disclosed only during formal HR procedures or security investigations. FCA regulatory disclosures upon lawful request.
6. **Deletion**: Automated retention enforcement: email metadata deleted at 30 days, internet categories at 90 days, badge access at 12 months, individual productivity data at 12 months (then aggregated to department level for 3-year retention).

### 2.7 Processors

| Processor | Service | Art. 28 DPA Status | Sub-processors |
|-----------|---------|-------------------|----------------|
| CloudSecure Ltd | Internet categorisation and hosting | Executed 2025-09-15, DPA ref DPA-QLH-2025-0042 | AWS (Ireland) for infrastructure |
| Amazon Web Services EMEA SARL | Data warehouse hosting | Executed 2024-03-01, DPA ref DPA-QLH-2024-0018 | None relevant |
| SAP SE | Productivity analytics platform | Executed 2024-06-01, DPA ref DPA-QLH-2024-0029 | SAP Deutschland SE & Co. KG |

---

## 3. Necessity and Proportionality Assessment — Art. 35(7)(b)

### 3.1 Necessity Analysis

| Data Category | Necessary? | Justification | Less Invasive Alternative Considered |
|--------------|-----------|---------------|--------------------------------------|
| Email metadata | Yes | Required for FCA SYSC 10A.1 compliance and insider threat detection. Metadata-only approach is already the minimum necessary — full content capture was rejected. | Full email content capture was considered and rejected as disproportionate. |
| Internet usage categories | Yes | Required for security (malware/phishing detection) and acceptable use enforcement. Category-level is the minimum — URL-level logging was rejected. | URL-level logging was considered and rejected following DPO advice. |
| Badge access logs | Yes | Required for physical security of premises containing patient health data and research IP. | No less invasive alternative identified for physical access control. |
| Productivity metrics | Partially | Daily summaries are proportionate for resource planning. Original proposal included keystroke logging, which was rejected as disproportionate. | Keystroke logging was proposed and rejected following works council consultation. |

### 3.2 Data Minimisation Compliance

- Email monitoring: metadata only (sender, recipient, timestamp, subject) — content not accessed
- Internet monitoring: category classification only — URLs not logged
- Productivity monitoring: daily aggregate summaries only — no keystroke or screenshot capture
- All individual-level data subject to automated retention limits

### 3.3 Storage Limitation

All retention periods are technically enforced by automated deletion scripts with cryptographic erasure verification. Retention periods are proportionate to the stated purposes and reflect the minimum period needed for each purpose.

### 3.4 Data Subject Rights

| Right | Facilitation Mechanism |
|-------|----------------------|
| Access (Art. 15) | Employees can request a copy of all monitoring data held about them via the HR Data Privacy Portal. Response within 30 days. |
| Rectification (Art. 16) | Badge access errors can be corrected via IT helpdesk. Other monitoring data is system-generated and not subject to rectification. |
| Erasure (Art. 17) | Automated retention enforces erasure. Manual erasure requests assessed on case-by-case basis; regulatory retention obligations may override. |
| Restriction (Art. 18) | Processing can be restricted for individual employees during dispute resolution. |
| Objection (Art. 21) | Employees may object to monitoring for performance management purposes. Objections assessed against legitimate interest balancing test. Regulatory monitoring (FCA) cannot be objected to. |

---

## 4. Risk Assessment — Art. 35(7)(c)

### Risk Register

#### Risk R01: Unauthorised Access by Line Managers

| Attribute | Assessment |
|-----------|-----------|
| Risk ID | DPIA-QLH-2026-0001-R01 |
| Description | Line managers access individual employee monitoring data for purposes beyond legitimate performance management, leading to discriminatory treatment or punitive action based on monitoring patterns (e.g., penalising employees for break patterns or internet usage categories). |
| Threat Source | Internal — line managers with corporate network access |
| Harm Type | Non-material: discrimination, workplace harassment, chilling effect on legitimate workplace behaviour |
| Inherent Likelihood | Possible (10-50%) — managers have expressed interest in individual data during system design consultations |
| Inherent Severity | Significant — discriminatory treatment could affect career progression, psychological wellbeing, and employment status |
| **Inherent Risk Level** | **High** |

**Mitigation Measures:**

| Measure | Type | Owner | Deadline | Status |
|---------|------|-------|----------|--------|
| Role-based access controls restricting monitoring data access to HR department only; line managers receive aggregated departmental reports without individual-level detail | Organisational | Marcus Chen, Head of HR Operations | 2026-05-01 | Implemented |
| Audit logging of all access to monitoring data with automated alerts for unusual access patterns or bulk data retrieval | Technical | Dr. James Okonkwo, CISO | 2026-04-15 | In progress |

| Residual Attribute | Assessment |
|-------------------|-----------|
| Residual Likelihood | Remote (< 10%) — access controls technically prevent line manager access to individual data |
| Residual Severity | Limited — even if circumvented, audit trail would enable detection and remediation |
| **Residual Risk Level** | **Low** |

---

#### Risk R02: Disproportionate Behavioural Profiling

| Attribute | Assessment |
|-----------|-----------|
| Risk ID | DPIA-QLH-2026-0001-R02 |
| Description | Aggregation of email metadata, internet usage, badge access, and productivity metrics creates a comprehensive behavioural profile of each employee that exceeds reasonable expectations and is disproportionate to stated purposes. |
| Threat Source | System design — multiple data streams combined per individual |
| Harm Type | Non-material: loss of autonomy, chilling effect on workplace behaviour, erosion of trust in employment relationship |
| Inherent Likelihood | Likely (50-90%) — the system inherently combines multiple data sources per employee |
| Inherent Severity | Significant — comprehensive behavioural profiling in the employment context can fundamentally alter the power dynamic |
| **Inherent Risk Level** | **High** |

**Mitigation Measures:**

| Measure | Type | Owner | Deadline | Status |
|---------|------|-------|----------|--------|
| Data minimisation: email monitoring limited to metadata without content; internet monitoring limited to category-level without URLs; productivity metrics aggregated to daily summaries without keystroke data | Technical | Dr. Elena Vasquez, DPO | 2026-04-01 | Implemented |
| Proportionality policy: cross-referencing of monitoring datasets for individual employees prohibited without documented justification approved by DPO and HR Director | Organisational | Dr. Elena Vasquez, DPO | 2026-04-01 | Implemented |

| Residual Attribute | Assessment |
|-------------------|-----------|
| Residual Likelihood | Possible (10-50%) — data minimisation reduces granularity but combined data still exists |
| Residual Severity | Limited — category-level and aggregated data provides significantly less behavioural insight |
| **Residual Risk Level** | **Medium** |

---

#### Risk R03: Data Breach Exposing Monitoring Records

| Attribute | Assessment |
|-----------|-----------|
| Risk ID | DPIA-QLH-2026-0001-R03 |
| Description | External cyber attack or insider threat compromises the monitoring data warehouse, exposing detailed employee behavioural patterns including email communication patterns, internet usage habits, physical movements, and productivity data. |
| Threat Source | External — cyber attack targeting AWS infrastructure or corporate credentials |
| Harm Type | Material: identity theft, targeted social engineering using behavioural data. Non-material: distress, reputational damage, loss of trust. |
| Inherent Likelihood | Possible (10-50%) — health technology sector is a high-value target; monitoring data is an attractive target for corporate espionage |
| Inherent Severity | Significant — exposure of comprehensive workplace monitoring data for 3,000+ individuals would cause significant distress and potential material harm |
| **Inherent Risk Level** | **High** |

**Mitigation Measures:**

| Measure | Type | Owner | Deadline | Status |
|---------|------|-------|----------|--------|
| AES-256 encryption at rest for all monitoring databases; TLS 1.3 encryption in transit; network segmentation isolating monitoring infrastructure from general corporate network | Technical | Dr. James Okonkwo, CISO | 2026-04-15 | In progress |
| 90-day automated retention with cryptographic erasure for monitoring data; 30-day retention for email metadata; 12-month retention for aggregated performance reports | Technical | Sarah Kim, IT Operations Manager | 2026-05-01 | Scheduled |

| Residual Attribute | Assessment |
|-------------------|-----------|
| Residual Likelihood | Remote (< 10%) — encryption and segmentation significantly reduce exploit probability |
| Residual Severity | Limited — short retention periods limit the volume of data at risk at any point |
| **Residual Risk Level** | **Low** |

---

## 5. DPO Advice — Art. 35(2)

**DPO**: Dr. Elena Vasquez, CIPP/E, CIPM

**Date of Advice**: 2026-02-08

**Advice**:

The processing as initially proposed included keystroke logging and full URL capture, which I advised were disproportionate to the stated purposes of workplace security, regulatory compliance, performance management, and IT management. The keystroke logging would have captured personal communications typed in work applications and created an excessively granular record of employee behaviour. Full URL logging would have revealed personal browsing habits (health information searches, political reading, personal interests) beyond what is necessary for security categorisation.

Following my advice, these elements were removed and replaced with aggregated productivity metrics and category-level internet monitoring respectively. I am satisfied that the revised processing, with the documented mitigation measures implemented, represents a proportionate approach to the stated legitimate interests.

I recommend the DPIA be reviewed in 6 months (August 2026) rather than the standard 12 months, given the sensitivity of employee monitoring and the fact that several mitigation measures are still being implemented.

**Advice followed**: Yes. Keystroke logging and URL-level monitoring were removed from scope.

---

## 6. Data Subject Views — Art. 35(9)

**Views sought**: Yes

**Method**: Consultation with employee works council representatives on 2026-01-15.

**Summary of consultation**:

The works council was presented with the proposed monitoring system scope, purposes, data access controls, and retention periods. The consultation resulted in the following changes:

1. **Removal of keystroke logging**: Works council representatives identified this as the most intrusive element and raised concerns about capturing personal communications. Removed from scope.
2. **Restriction of line manager access**: Works council requested that line managers receive only aggregated departmental data. Implemented via role-based access controls.
3. **Six-month DPIA review cycle**: Works council requested more frequent review than the standard annual cycle. Accepted and documented.
4. **Employee notification enhancement**: Works council requested that employees receive a plain-language summary of monitoring scope in addition to the formal privacy notice. Summary distributed to all employees on 2026-02-01.

Union representatives confirmed on 2026-01-22 that these changes addressed their primary concerns regarding proportionality and employee dignity.

---

## 7. Conclusion and Approval

### Risk Summary

| Risk | Inherent Level | Residual Level | Prior Consultation Required? |
|------|---------------|----------------|------|
| R01: Unauthorised access by line managers | High | Low | No |
| R02: Disproportionate behavioural profiling | High | Medium | No |
| R03: Data breach exposing monitoring records | High | Low | No |

### Determination

All residual risks have been reduced to Medium or below through the documented mitigation measures. **Art. 36 prior consultation is not required.**

Processing may proceed subject to:
1. Completion of all mitigation measures by their documented deadlines
2. Six-month review scheduled for August 2026
3. Immediate DPIA review if any material change occurs (new data category, new recipient, technology change, or security incident)

### Approvals

| Role | Name | Date | Signature |
|------|------|------|-----------|
| DPO | Dr. Elena Vasquez | 2026-02-10 | Approved |
| Processing Owner | Marcus Chen | 2026-02-10 | Approved |
| CISO | Dr. James Okonkwo | 2026-02-10 | Approved |
| Senior Management | Dr. Priya Sharma, COO | 2026-02-11 | Approved |
