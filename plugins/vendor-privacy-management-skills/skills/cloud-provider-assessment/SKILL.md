---
name: cloud-provider-assessment
description: >-
  Cloud service provider privacy assessment framework. Covers ISO 27018 cloud
  privacy controls, CSA STAR certification, SOC 2 Type II evaluation, shared
  responsibility model mapping, data residency verification, and cloud-specific
  privacy risk analysis.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: vendor-privacy-management
  tags: "cloud-assessment, iso-27018, csa-star, shared-responsibility, data-residency"
---

# Cloud Service Provider Privacy Assessment

## Overview

Cloud service providers present unique privacy assessment challenges due to shared responsibility models, multi-tenancy architectures, global infrastructure, and the abstraction of physical processing locations. GDPR Article 28 obligations apply fully to cloud processing relationships, but the assessment approach must account for cloud-specific characteristics.

ISO/IEC 27018:2019 provides the international standard for protecting personally identifiable information (PII) in public clouds, supplementing ISO 27001 with cloud-specific privacy controls. The Cloud Security Alliance (CSA) STAR program provides a cloud-specific security assurance framework. SOC 2 Type II with the Privacy trust services criterion addresses personal data handling controls.

At Summit Cloud Partners, cloud providers undergo enhanced assessment incorporating these cloud-specific frameworks alongside standard vendor due diligence.

## Cloud Service Models and Privacy Implications

### IaaS (Infrastructure as a Service)

| Aspect | Controller Responsibility | Provider Responsibility |
|--------|--------------------------|------------------------|
| Data encryption at rest | Configure and manage keys | Provide encryption infrastructure |
| Access management (app level) | Define and manage | Provide IAM platform |
| Network security (app level) | Configure security groups, firewall rules | Provide network infrastructure |
| Physical security | None | Full responsibility |
| Patch management (OS) | Controller (or managed service) | Hypervisor and below |
| Data backup | Configure and manage | Provide backup infrastructure |
| Incident detection (app) | Application-level monitoring | Infrastructure-level monitoring |

### PaaS (Platform as a Service)

| Aspect | Controller Responsibility | Provider Responsibility |
|--------|--------------------------|------------------------|
| Application code security | Full responsibility | None |
| Data handling in application | Full responsibility | None |
| Runtime and middleware | Limited — configuration only | Manage platform components |
| OS and infrastructure | None | Full responsibility |
| Platform security patching | None | Full responsibility |
| Identity management | Configure | Provide identity platform |

### SaaS (Software as a Service)

| Aspect | Controller Responsibility | Provider Responsibility |
|--------|--------------------------|------------------------|
| Data entered by users | Determine what data to process | Process per controller instructions |
| Application security | None (except configuration) | Full responsibility |
| Infrastructure security | None | Full responsibility |
| Data portability | Define export requirements | Provide export functionality |
| Data deletion | Request deletion | Implement deletion per DPA |
| Access configuration | Configure user roles | Provide RBAC platform |

## Assessment Framework

### Domain 1: Data Residency and Sovereignty

**Assessment Questions:**

| # | Question | Expected Evidence |
|---|----------|-------------------|
| 1.1 | In which regions/availability zones will personal data be stored at rest? | Architecture documentation specifying data storage locations |
| 1.2 | Can the controller restrict processing to specific geographic regions? | Configuration documentation showing region-locking capability |
| 1.3 | Are there any circumstances where data may be processed outside the selected region? | Disclosure of any cross-region processing (DR, support, analytics) |
| 1.4 | Where is metadata and telemetry data stored? | Often stored in provider's home jurisdiction — must be disclosed |
| 1.5 | Where do support staff access data from? | List of countries from which support personnel may access data |
| 1.6 | What government access or disclosure obligations apply in processing jurisdictions? | Legal analysis of government access powers per EDPB Recommendations 01/2020 |

### Domain 2: Multi-Tenancy and Data Isolation

| # | Question | Expected Evidence |
|---|----------|-------------------|
| 2.1 | How is tenant data isolated from other customers' data? | Architecture documentation — logical/physical separation details |
| 2.2 | Are encryption keys unique per tenant? | Key management architecture documentation |
| 2.3 | Can one tenant's operations affect another tenant's data? | Side-channel and cross-tenant risk assessment |
| 2.4 | How are shared infrastructure components secured? | Hypervisor security, shared storage controls |
| 2.5 | What tenant isolation testing has been performed? | Penetration test results covering cross-tenant attacks |

### Domain 3: ISO 27018 Cloud Privacy Controls

ISO/IEC 27018:2019 extends ISO 27001 with cloud-specific PII protection controls:

| Control | Requirement | Assessment Check |
|---------|-------------|-----------------|
| A.1 | PII processor consent — process only per controller instructions | Verify contractual terms and processing boundaries |
| A.2 | Purpose limitation — no processing beyond controller purpose | Review processing scope documentation |
| A.3 | Use for marketing — no use of PII for marketing without consent | Confirm no data monetization or marketing use |
| A.4 | Notification — notify controller of government access requests | Verify government access notification process |
| A.5 | Disclosure — document all disclosures of PII | Review disclosure logging mechanism |
| A.10 | Return, transfer, and disposal — secure data handling at termination | Verify deletion procedures and certification |
| A.11 | Confidentiality — binding confidentiality obligations on personnel | Verify personnel agreements cover cloud-specific risks |
| A.12 | Sub-contracting — notification of sub-processor engagement | Verify sub-processor management per Art. 28(2) |

### Domain 4: CSA STAR Assessment

The Cloud Security Alliance STAR (Security, Trust, Assurance, and Risk) program provides three levels:

| Level | Description | Assessment Method |
|-------|-------------|-------------------|
| Level 1: Self-Assessment | Provider completes CSA Consensus Assessments Initiative Questionnaire (CAIQ) | Review self-assessment for completeness and substantiation |
| Level 2: Third-Party Audit | Independent audit against CSA Cloud Controls Matrix (CCM) | Review audit report, scope, and findings |
| Level 3: Continuous Monitoring | Real-time monitoring of control effectiveness | Review continuous monitoring dashboard and alerts |

**Key CCM Control Domains for Privacy:**

| Domain | Controls | Privacy Relevance |
|--------|----------|------------------|
| DSP (Data Security & Privacy) | DSP-01 through DSP-19 | Data classification, retention, inventory, privacy by design |
| GRC (Governance, Risk, Compliance) | GRC-01 through GRC-08 | Governance framework, risk assessment, policy management |
| IAM (Identity & Access Management) | IAM-01 through IAM-16 | Access control, credential management, MFA |
| SEF (Security Incident Management) | SEF-01 through SEF-08 | Incident response, breach notification |

### Domain 5: SOC 2 Type II Privacy Criterion

The AICPA Trust Services Criteria Privacy criterion evaluates:

| Criterion | Area | Assessment Focus |
|-----------|------|-----------------|
| P1 | Notice | Provider discloses privacy practices to controllers |
| P2 | Choice and consent | Controller can configure privacy settings |
| P3 | Collection | Data collection limited to stated purposes |
| P4 | Use, retention, disposal | Processing per instructions; retention per DPA; certified deletion |
| P5 | Access | Controller can access and retrieve their data |
| P6 | Disclosure to third parties | Sub-processor disclosure and management |
| P7 | Security for privacy | Technical controls protecting PII |
| P8 | Quality | Data integrity and accuracy controls |
| P9 | Monitoring and enforcement | Compliance monitoring and breach response |

### Domain 6: Shared Responsibility Model Mapping

Document the shared responsibility boundary for every control domain:

| Control Domain | Controller Responsibility | Provider Responsibility | Gap/Risk |
|---------------|--------------------------|------------------------|----------|
| Data classification | Classify data before upload | Provide classification tools | [Gap?] |
| Encryption key management | [Depends on model] | [Depends on model] | [Gap?] |
| Access control (application) | [Depends on model] | [Depends on model] | [Gap?] |
| Vulnerability management | [Depends on model] | [Depends on model] | [Gap?] |
| Incident detection | [Depends on model] | [Depends on model] | [Gap?] |
| Data backup | [Depends on model] | [Depends on model] | [Gap?] |
| Compliance reporting | [Depends on model] | [Depends on model] | [Gap?] |

## Assessment Scoring

| Domain | Weight | Score (1-5) | Weighted |
|--------|--------|-------------|----------|
| Data residency and sovereignty | 20% | | |
| Multi-tenancy and isolation | 20% | | |
| ISO 27018 compliance | 15% | | |
| CSA STAR level | 15% | | |
| SOC 2 Privacy criterion | 15% | | |
| Shared responsibility clarity | 15% | | |
| **TOTAL** | **100%** | | |

## Key Regulatory References

- GDPR Article 28 — Controller-processor relationship applies fully to cloud
- GDPR Article 32 — Security measures including cloud-specific controls
- ISO/IEC 27018:2019 — Code of practice for protection of PII in public clouds
- ISO/IEC 27017:2015 — Code of practice for information security controls for cloud services
- CSA Cloud Controls Matrix (CCM) v4.0 — Cloud security control framework
- EDPB Recommendations 01/2020 — Supplementary measures for cloud transfers
- ENISA Cloud Computing Risk Assessment (2009, updated) — EU cloud risk framework
