# Regulatory Standards — Cloud Provider Assessment

## Primary Regulations

### GDPR — Regulation (EU) 2016/679

- **Article 28**: The controller-processor framework applies fully to cloud service providers. The controller must conduct due diligence and execute a DPA regardless of the cloud service model (IaaS, PaaS, SaaS).

- **Article 32**: Security measures must account for cloud-specific risks including multi-tenancy, shared infrastructure, and geographic distribution.

- **Article 44-49**: Cross-border transfer rules apply when cloud providers process data outside the EEA, including through metadata, telemetry, or support access.

### ISO/IEC 27018:2019 — Protection of PII in Public Clouds

This standard establishes commonly accepted control objectives and controls for PII protection in cloud computing environments. Key provisions:

- **Clause 5**: Information security policies — must address cloud-specific PII protection
- **Annex A**: Extended control set for cloud PII processors including:
  - A.1: Customer agreement — process PII only per customer instructions
  - A.2: Purpose limitation — no processing beyond contractual purpose
  - A.3: Marketing restriction — no use of PII for advertising or marketing
  - A.4: Government access — notify customer of government disclosure requests
  - A.5: Disclosure logging — maintain records of all PII disclosures
  - A.10: Return, transfer, disposal — secure data handling lifecycle
  - A.11: Confidentiality — personnel obligations specific to cloud PII
  - A.12: Sub-contracting — sub-processor notification and oversight

### ISO/IEC 27017:2015 — Cloud Security Controls

Provides cloud-specific information security guidelines supplementing ISO 27001:
- Additional controls for cloud service customers and providers
- Shared responsibility delineation guidance
- Cloud-specific risk assessment methodology

### CSA Cloud Controls Matrix (CCM) v4.0

The CCM provides a cybersecurity control framework for cloud computing covering 197 control objectives across 17 domains. Privacy-relevant domains include:

- **DSP (Data Security & Privacy Lifecycle Management)**: 19 controls covering data inventory, classification, flow mapping, retention, privacy by design, and privacy impact assessment
- **GRC (Governance, Risk Management and Compliance)**: 8 controls covering governance framework, policy management, and risk assessment
- **SEF (Security Incident Management, E-Discovery, & Cloud Forensics)**: 8 controls covering incident management, notification, and forensic capability

### SOC 2 Type II — Trust Services Criteria

The AICPA Trust Services Criteria provide the framework for SOC 2 examinations:
- **Security (Common Criteria)**: Mandatory for all SOC 2 reports
- **Privacy**: Optional criterion evaluating PII handling per GAPP (Generally Accepted Privacy Principles)
- **Type II** reports cover a minimum 6-month period and include testing of control operating effectiveness

## Supervisory Authority Guidance

### EDPB — Cloud Computing Guidance

The EDPB (previously Article 29 Working Party) Opinion 05/2012 on Cloud Computing addressed:
- Controllers must conduct risk assessment before adopting cloud services
- DPAs must address cloud-specific issues (data location, sub-processing, portability)
- Cloud service transparency regarding data processing locations
- Controller audit rights must be practical in cloud environments

### CNIL — Cloud Computing Recommendations (2022)

CNIL published recommendations for organizations using cloud services:
- Encryption with customer-managed keys when processing sensitive data
- Data residency requirements for French public sector data
- Assessment of non-EU government access risks (per Schrems II)

### German Federal Commissioner (BfDI) — Cloud Computing Position

The BfDI requires:
- Controllers must know exactly where cloud providers process personal data
- Standard cloud terms of service must be supplemented with GDPR-compliant DPAs
- Cloud providers must demonstrate compliance through certifications and audit access

### ENISA — Cloud Computing Risk Assessment

ENISA's cloud risk framework identifies key risks:
- Loss of governance: controller loses control over data
- Lock-in: inability to migrate data between providers
- Isolation failure: cross-tenant attacks in multi-tenant environments
- Compliance risks: cloud infrastructure spanning multiple jurisdictions
- Data protection risks: provider access to customer data
