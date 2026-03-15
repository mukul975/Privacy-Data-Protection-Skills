---
name: hr-system-privacy-config
description: >-
  Configures privacy settings for enterprise HR systems including SAP
  SuccessFactors, Workday, and BambooHR. Covers role-based access controls,
  automated data retention enforcement, cross-border transfer configurations,
  audit logging, data subject rights facilitation, and field-level security.
  Keywords: HR system, SAP SuccessFactors, Workday, BambooHR, RBAC,
  retention automation, cross-border transfer, privacy configuration.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: employee-data-privacy
  tags: "hr-system, sap-successfactors, workday, bamboohr, rbac, retention-automation, privacy-config"
---

# HR System Privacy Configuration

## Overview

Enterprise HR systems are the central repository for employee personal data, processing everything from recruitment to retirement. Systems like SAP SuccessFactors, Workday, and BambooHR contain names, addresses, national identifiers, salary data, performance evaluations, absence records, health-related fitness conclusions, disciplinary records, and benefits information. The default configuration of these systems is designed for operational efficiency, not GDPR compliance. Privacy professionals must actively configure role-based access controls, data retention automation, cross-border transfer settings, audit logging, and field-level security to ensure that the HR system enforces — rather than merely documents — privacy requirements.

This skill provides configuration guidance for the three most widely deployed HR platforms, focusing on the privacy-critical settings that determine who can see what data, how long data is retained, and how data subject rights are facilitated.

## Cross-Platform Privacy Requirements

### Requirement 1: Role-Based Access Controls (RBAC)

**Principle**: No employee should have access to more HR data than is necessary for their specific role. Line managers need access to their direct reports' data; HR business partners need access to their client group; payroll needs salary and tax data; IT administrators need system access but not data content.

**Standard RBAC Matrix**:

| Role | Personal Details | Salary/Compensation | Performance Reviews | Absence Records | Health Data | Disciplinary Records | Recruitment Data |
|------|-----------------|--------------------|--------------------|----------------|-------------|---------------------|-----------------|
| Employee (self) | Full | Own salary only | Own reviews | Own absence | Own OH reports | Own records | Own application |
| Line Manager | Direct reports: name, contact, role, start date | No (unless approval workflow) | Direct reports only | Direct reports: dates only (no diagnosis) | No | No (unless involved in process) | Hiring manager: interview candidates |
| HR Business Partner | Client group: full | Client group: full | Client group: full | Client group: dates + fit note status | Fit/unfit conclusion only | Client group: full | Client group: all candidates |
| Payroll | Minimal: name, employee ID, bank details, tax code | Full: all employees | No | Statutory sick pay relevant data only | No | No | No |
| Benefits Administrator | Name, employee ID, enrolment selections | Salary bands (for benefits calculation) | No | No | No | No | No |
| IT Administrator | System access management: name, employee ID, department, email | No | No | No | No | No | No |
| DPO | Audit access to all processing records; no routine access to individual data | Audit only | Audit only | Audit only | Audit only | Audit only | Audit only |
| Senior Leadership | Aggregate reports only | Aggregate/anonymised | Aggregate/anonymised | Aggregate/anonymised | No | No | No |

### Requirement 2: Data Retention Automation

**Principle**: Data should be automatically deleted or anonymised when the retention period expires. Manual deletion is unreliable and non-compliant.

**Standard Retention Schedule for HR Data**:

| Data Category | Retention Trigger | Retention Period | Post-Retention Action |
|--------------|------------------|-----------------|----------------------|
| Recruitment — unsuccessful candidates | Application decision date | 6 months (12 months where discrimination claim risk) | Delete application, CV, interview notes, assessment scores |
| Employment contract | Termination date | 6 years post-termination (contractual claim limitation) | Delete or archive to restricted storage |
| Payroll and tax records | End of tax year | 6-7 years (varies by jurisdiction) | Delete |
| Performance reviews | Termination date | 2 years post-termination (unless ongoing dispute) | Delete |
| Absence records | End of absence year | 2 years current + 1 year archive | Delete detail; retain aggregate statistics |
| Disciplinary records | Outcome date | Per policy: warnings expire after 6-12 months; dismissal records 6 years | Delete expired warnings; retain dismissal records for limitation period |
| Health/occupational health records | Termination date or end of health surveillance | Varies: standard employment 6 years; occupational health surveillance 40 years (asbestos, radiation) | Transfer to occupational health archive |
| Training records | Termination date | 3 years post-termination | Delete |
| DSAR response records | Response date | 2 years | Delete copies; retain log entry |

### Requirement 3: Cross-Border Transfer Configuration

For multinational organisations, HR systems transfer employee data across borders. Each transfer must comply with Chapter V GDPR.

**Transfer scenarios requiring configuration**:

| Scenario | Transfer Mechanism | System Configuration |
|----------|-------------------|---------------------|
| EU headquarters → EU subsidiary | No restriction (intra-EEA) | Ensure data residency within EEA data centres |
| EU headquarters → UK subsidiary | UK adequacy decision (valid until June 2025, extended) | Configure UK entity as adequate recipient |
| EU headquarters → US subsidiary | EU-US Data Privacy Framework (where US entity is certified) or SCCs | Verify DPF certification; configure SCC-based transfer if not certified |
| EU entity → cloud HR provider (US-hosted) | DPF + SCCs + supplementary measures | Verify provider DPF status; enable encryption; configure data residency if available |
| EU entity → India/Philippines shared services | SCCs + TIA | Implement SCCs; conduct Transfer Impact Assessment; enable supplementary measures |

### Requirement 4: Audit Logging

**Mandatory audit events**:

| Event | Log Content | Retention |
|-------|------------|-----------|
| Data access | Who accessed which employee's record, when, from where | 2 years |
| Data modification | Who changed what field, old value, new value, when | 2 years |
| Data export | Who exported data, scope, format, destination | 2 years |
| Report generation | Who ran what report, parameters, number of records | 2 years |
| Access permission changes | Who granted/revoked access, to whom, scope | 3 years |
| Data deletion | What was deleted, by whom, automated or manual | Permanent (audit trail survives data deletion) |
| Failed access attempts | Who attempted to access data they were not authorised to see | 1 year |

## SAP SuccessFactors Configuration

### Role-Based Permissions

SuccessFactors uses a **Role-Based Permissions (RBP)** framework:

1. **Permission Roles**: Create roles corresponding to the RBAC matrix (Employee Self-Service, Line Manager, HR BP, Payroll, Benefits Admin, IT Admin, DPO Audit)
2. **Permission Groups**: Define target populations for each role (e.g., Line Manager sees direct reports only; HR BP sees client group employees)
3. **Field-Level Permissions**: For each role, configure read/write/no-access at the individual field level
   - Health data fields: No access for all roles except HR BP (read-only for fit/unfit fields) and Employee (own data)
   - Salary fields: No access for Line Manager, IT Admin; read-only for HR BP; read-write for Payroll
   - Disciplinary fields: No access for Line Manager (unless party to process), read-only for HR BP
4. **IP Restriction**: Restrict admin access to corporate network IP ranges

### Data Retention Management (DRM)

SuccessFactors provides a **Data Retention Management** module:

1. **Purge Rules**: Configure automated purge rules per data category:
   - Inactive employees: purge personal data X years after termination date (configure per retention schedule)
   - Recruitment: purge unsuccessful candidate data after configured period
   - Performance: purge historical reviews per retention policy
2. **Data Purge Requests**: Create purge requests targeting specific employee populations based on termination date
3. **Anonymisation**: Where full deletion is not possible (e.g., data required for aggregate reporting), configure anonymisation to replace personal identifiers with pseudonyms
4. **Audit Trail**: DRM maintains an audit trail of all purge activities, including what was deleted and by whom

### Cross-Border Data Handling

1. **Data Centre Selection**: SuccessFactors operates data centres in the EU (Germany, Netherlands), UK, US, and APAC. Configure the instance to use the EU data centre for EEA employee data
2. **Employee Central Global Assignment**: For international assignments, configure transfer rules that apply appropriate safeguards when data moves between legal entities in different jurisdictions
3. **Integration Centre**: API integrations that export employee data to third-party systems must be configured with data residency restrictions

### DSAR Facilitation

1. **Personal Data Report**: SuccessFactors provides a Personal Data Report feature that compiles all data fields containing the requesting employee's personal data
2. **Data Subject Request Tool**: Automated workflow for receiving, tracking, and responding to DSARs with configurable deadlines and escalation
3. **Right to Erasure**: The system supports targeted deletion of specific employee records while maintaining the audit trail

## Workday Configuration

### Security Groups

Workday uses a **Security Group** model:

1. **Role-Based Security Groups**: Map to the RBAC matrix:
   - Manager: inherits based on supervisory organisation
   - HR Partner: assigned to specific supervisory organisations
   - Payroll Administrator: assigned to specific companies/pay groups
   - Benefits Administrator: assigned to benefit groups
2. **Domain Security Policies**: Control access to functional areas (Compensation, Talent, Absence, Recruitment) independently
3. **Field-Level Security**: Configure visibility and editability per field per security group
4. **Segment-Based Security**: Restrict access to specific employee segments (e.g., executives, works council members, employees under investigation)

### Business Process Security

Workday business processes (hire, promote, terminate, compensation change) have their own security:
1. **Initiator permissions**: Who can start the process
2. **Approval chain**: Who must approve at each step
3. **Notification restrictions**: Who is notified (avoid sending sensitive data in email notifications)
4. **Document attachment security**: Restrict who can view supporting documents (offer letters, performance evidence)

### Data Retention

Workday provides **Data Purge** functionality:
1. **Purge Framework**: Configure purge rules by data type and retention period
2. **Worker History Purge**: Systematically remove historical data for terminated workers after the retention period
3. **Recruitment Purge**: Automatically delete unsuccessful candidate records
4. **Archive and Purge**: Move data to archive before permanent deletion, allowing recovery within a grace period

### Cross-Border Transfers

1. **Tenant Configuration**: Workday allows configuration of data residency at the tenant level
2. **Multi-Region Deployment**: Large enterprises may have separate tenants for different regions
3. **Integration Security**: Workday integrations (HCM, Payroll, Benefits) that transfer data across borders must be assessed under the TIA framework

## BambooHR Configuration

### Access Levels

BambooHR uses a simpler access model suitable for small to medium enterprises:

1. **Access Levels**: Pre-defined levels (Employee Self-Service, Manager, HR Admin, Payroll Admin, No Access) plus custom levels
2. **Field Visibility**: Each access level defines which fields are visible and editable
3. **Custom Access Levels**: Create privacy-compliant custom levels:
   - DPO Audit: Read-only access to processing records and audit logs, no access to individual employee data
   - Restricted HR: Access to specific employee populations only
   - Benefits Only: Access to benefits fields only

### Reporting Restrictions

1. **Report Filters**: Configure default report filters to prevent inadvertent disclosure (e.g., reports automatically exclude health data fields)
2. **Custom Reports**: Restrict who can create custom reports (custom reports can bypass field visibility if not properly configured)
3. **Data Export**: Restrict CSV/Excel export permissions to authorised roles only

### Retention Configuration

BambooHR provides:
1. **Inactive Employee Management**: Configure rules for archiving and deleting terminated employee records
2. **Document Purge**: Automated deletion of uploaded documents (offer letters, ID copies, certificates) after configured retention period
3. **Application Tracking Purge**: Delete unsuccessful candidate data after configured period

## Privacy Configuration Checklist

### Initial Setup

- [ ] Map organisational roles to HR system security roles/groups
- [ ] Configure field-level access for each role per RBAC matrix
- [ ] Restrict health data fields to authorised roles only
- [ ] Restrict salary/compensation fields to authorised roles
- [ ] Configure manager access to direct reports only (not entire organisation)
- [ ] Disable default admin access to personal data content
- [ ] Enable audit logging for all data access, modification, and export events

### Data Retention

- [ ] Configure automated purge rules for each data category
- [ ] Set retention triggers (termination date, application decision date, etc.)
- [ ] Test purge rules in sandbox environment before production deployment
- [ ] Verify that purge rules maintain required audit trails
- [ ] Configure anonymisation for data required for aggregate reporting post-retention

### Cross-Border Transfers

- [ ] Verify data centre location for EEA employee data
- [ ] Assess all integrations that transfer data outside the EEA
- [ ] Implement SCCs or verify DPF certification for US transfers
- [ ] Conduct TIA for transfers to non-adequate countries
- [ ] Configure data residency restrictions on APIs and integrations

### DSAR Compliance

- [ ] Test the system's ability to export a complete copy of an individual's data
- [ ] Verify that the export includes all modules (core HR, performance, absence, recruitment)
- [ ] Configure DSAR workflow with deadline tracking and escalation
- [ ] Test rectification capability: can specific fields be corrected without system integrity issues?
- [ ] Test erasure capability: can individual records be deleted while maintaining referential integrity?

### Ongoing Monitoring

- [ ] Schedule quarterly access reviews — review who has access to what
- [ ] Review audit logs monthly for anomalous access patterns
- [ ] Test retention automation quarterly — verify that purge rules execute correctly
- [ ] Review security configuration after system upgrades (upgrades may reset security settings)
- [ ] Conduct annual privacy assessment of HR system configuration

## Atlas Manufacturing Group Example

Atlas Manufacturing Group uses SAP SuccessFactors for 2,400 employees across Germany, France, UK, and the Netherlands. The DPO conducted a privacy configuration audit and identified the following issues:

1. **Over-broad manager access**: Line managers had read access to salary data for all employees in their department, not just direct reports. Remediation: Reconfigured RBP to limit manager access to direct reports only.
2. **No automated retention**: Terminated employee data was retained indefinitely. Remediation: Implemented DRM purge rules — personal data purged 6 years after termination, with 40-year retention for occupational health records of employees in the chemical production unit.
3. **Cross-border transfer gap**: The SuccessFactors integration with a US-based benefits provider was transferring employee data without SCCs. Remediation: Verified the benefits provider's DPF certification and implemented supplementary encryption measures.
4. **Missing audit logging**: Data exports to Excel were not logged. Remediation: Enabled export audit logging and restricted export permissions to HR BP and Payroll roles.
5. **Health data visibility**: The absence management module displayed the "reason for absence" field (which sometimes contained health information) to line managers. Remediation: Removed reason field visibility for managers; managers see absence dates and type (sick, annual leave, other) only.

## Enforcement Precedents

| Authority | Case | Fine/Outcome | Key Issue |
|-----------|------|-------------|-----------|
| LfDI Hamburg (Germany) | H&M, 2020 | EUR 35,258,707.95 | HR system used to record excessive employee health and personal data; insufficient access controls |
| CNIL (France) | Dedalus Biologie, 2022 | EUR 1,500,000 | Insufficient access controls on health data in information systems |
| ICO (UK) | British Airways, 2020 | GBP 20,000,000 | Insufficient technical and organisational measures — includes system access controls |
| AEPD (Spain) | CaixaBank, 2021 | EUR 6,000,000 | Insufficient granularity in access controls for personal data systems |
| Autoriteit Persoonsgegevens (NL) | 2022 Audit | Corrective measures | HR system retained terminated employee data beyond retention period |

## Integration Points

- **Employee DSAR Response**: HR system must support data export for DSARs (see employee-dsar-response skill).
- **Employee Health Data**: Health data fields require dedicated access controls (see employee-health-data skill).
- **Employee Biometric Data**: Biometric integration with timekeeping requires privacy configuration (see employee-biometric-data skill).
- **Background Check Privacy**: Background check data storage must comply with retention limits (see background-check-privacy skill).
- **Remote Work Monitoring**: HR system integration with monitoring tools must respect data separation (see remote-work-monitoring skill).
