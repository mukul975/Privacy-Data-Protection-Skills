---
name: assessing-cloud-migration-privacy
description: >-
  Guides DPIA for migrating personal data to cloud infrastructure covering
  controller-processor analysis under Art. 28, international transfer
  assessment, encryption requirements, and shared responsibility model
  evaluation. Activate for cloud adoption, SaaS procurement, or data centre
  migration projects. Keywords: cloud migration, DPIA, Art. 28, processor,
  encryption, shared responsibility, SaaS, IaaS, PaaS.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-impact-assessment
  tags: "cloud-migration, dpia, art-28, processor, encryption, shared-responsibility"
---

# Assessing Cloud Migration Privacy

## Overview

Migrating personal data to cloud infrastructure (IaaS, PaaS, SaaS) introduces fundamental changes to the data protection landscape: the controller cedes physical control over personal data to a cloud service provider (CSP) acting as processor, creating dependencies on the CSP's security measures, geographic infrastructure, and sub-processor chain. This skill provides a DPIA methodology covering the Art. 28 controller-processor relationship, international transfer assessment under Chapter V, encryption and key management requirements, the shared responsibility model, and sub-processor governance.

## Legal Framework

### GDPR Art. 28 — Processor Obligations

Art. 28(1) requires the controller to use only processors providing sufficient guarantees to implement appropriate technical and organisational measures to ensure processing meets GDPR requirements.

Art. 28(3) mandates a binding contract or legal act setting out:
- Subject matter and duration of processing
- Nature and purpose of processing
- Type of personal data and categories of data subjects
- Obligations and rights of the controller
- Specific processor obligations including: processing only on documented instructions, confidentiality, security measures, sub-processor approval, data subject rights assistance, deletion/return on termination, audits and inspections

### Art. 28(2) — Sub-Processor Authorisation

The processor shall not engage another processor without prior specific or general written authorisation of the controller. In the case of general written authorisation, the processor shall inform the controller of any intended changes concerning the addition or replacement of sub-processors, giving the controller the opportunity to object.

### Cloud-Specific Regulatory Guidance

| Authority | Guidance | Key Requirements |
|-----------|----------|-----------------|
| EDPB | Guidelines 07/2020 on controller and processor concepts | Clarified CSP role determination: CSPs acting strictly under controller instructions are processors; CSPs determining purposes of processing for their own use are (joint) controllers |
| CNIL | Recommendations on cloud computing (2022) | Recommended DPIA for cloud migrations involving sensitive data; encryption with customer-held keys; exit strategy requirements |
| BSI (Germany) | C5 Cloud Computing Compliance Catalogue | Technical security criteria for cloud services used by German public sector and recommended for private sector |
| ENISA | Cloud Security Guide for SMEs (2015, updated 2023) | Risk assessment framework for cloud adoption including data protection considerations |

## Cloud Service Models and Privacy Responsibilities

### Shared Responsibility Model

| Responsibility | IaaS | PaaS | SaaS |
|---------------|------|------|------|
| Physical infrastructure security | CSP | CSP | CSP |
| Network security | Shared | CSP | CSP |
| Operating system | Customer | CSP | CSP |
| Application security | Customer | Shared | CSP |
| Data classification | Customer | Customer | Customer |
| Data encryption (at rest) | Customer | Shared | CSP (configuration by customer) |
| Data encryption (in transit) | Customer | Shared | CSP |
| Identity and access management | Customer | Shared | Shared |
| Data backup and recovery | Customer | Shared | CSP (configuration by customer) |
| Logging and monitoring | Customer | Shared | CSP (access by customer) |
| Compliance and governance | Customer | Customer | Customer |
| Data subject rights facilitation | Customer | Customer | Customer |
| DPIA | Customer | Customer | Customer |
| Data processing agreement | Customer | Customer | Customer |

### Key Privacy Considerations by Service Model

**IaaS (Infrastructure as a Service)**
- Controller retains most control but also most responsibility
- CSP has physical access to infrastructure but not application-layer data if encrypted
- Customer responsible for OS patching, application security, encryption implementation
- Data residency controlled by customer's region selection

**PaaS (Platform as a Service)**
- CSP manages infrastructure and platform; customer manages application and data
- CSP may have access to data through platform diagnostics and logging
- Sub-processor chain may be extensive (platform dependencies)
- Data portability may be limited by platform lock-in

**SaaS (Software as a Service)**
- CSP has broadest access to personal data (application-level access)
- Customer has least control over security measures
- Sub-processor chain often complex and opaque
- Data portability and exit strategy are critical concerns

## DPIA Methodology for Cloud Migration

### Phase 1: Cloud Processing Mapping (Week 1)

1. Inventory all personal data to be migrated to cloud.
2. Classify data by sensitivity: public, internal, confidential, restricted.
3. Map data flows: on-premises to cloud, cloud to cloud, cloud to third parties.
4. Identify all CSP services that will process personal data.
5. Determine CSP data processing locations (regions, zones, edge locations).
6. Identify the complete sub-processor chain for each CSP service.

### Phase 2: Controller-Processor Analysis (Week 2)

1. Determine the CSP's role for each service:
   - Processor: CSP processes data only on controller's documented instructions
   - Joint controller: CSP determines purposes of processing (e.g., CSP uses data for service improvement, analytics, AI training)
2. Review the CSP's Data Processing Agreement (DPA) for Art. 28(3) compliance.
3. Verify the CSP's sub-processor list and notification mechanism.
4. Assess the CSP's audit provisions: on-site audit rights, SOC 2 reports, ISO 27001 certification, penetration test results.
5. Review data return and deletion provisions for contract termination.

### Phase 3: International Transfer Assessment (Week 3)

1. Identify all CSP data processing locations.
2. For each location outside the EEA:
   - Check for an adequacy decision (Art. 45)
   - Verify SCCs are in place (Art. 46(2)(c))
   - Conduct Transfer Impact Assessment per EDPB Recommendations 01/2020
3. Assess sub-processor locations for international transfers.
4. Evaluate technical supplementary measures (encryption with customer-held keys).
5. Document the transfer mechanism for each third-country transfer.

### Phase 4: Security and Encryption Assessment (Week 3-4)

1. Evaluate CSP encryption capabilities:
   - Encryption at rest (algorithm, key length, key management)
   - Encryption in transit (TLS version, cipher suites)
   - Customer-managed encryption keys (BYOK/HYOK) availability
   - Client-side encryption capability
2. Assess access controls:
   - CSP staff access to customer data (break-glass procedures, access logging)
   - Customer IAM integration (SSO, MFA, RBAC)
   - Privileged access management
3. Evaluate data isolation:
   - Multi-tenant vs dedicated infrastructure
   - Logical isolation controls
   - Data commingling risks
4. Review incident response:
   - CSP breach notification timeline (Art. 33(2) requires processor to notify controller without undue delay)
   - CSP incident response capabilities
   - Customer access to security event logs

### Phase 5: Risk Assessment (Week 4-5)

| Risk | Description | Typical Level |
|------|-------------|--------------|
| CR-R1 | CSP data breach exposing customer personal data | High |
| CR-R2 | Government access to data via CSP (FISA 702, CLOUD Act for US CSPs) | Medium-High |
| CR-R3 | Sub-processor change introducing new risks without controller awareness | Medium |
| CR-R4 | Vendor lock-in preventing data portability or migration to alternative provider | Medium |
| CR-R5 | CSP service termination or insolvency | Medium |
| CR-R6 | CSP using personal data for own purposes (service improvement, AI training) | Medium |
| CR-R7 | Insufficient logging preventing incident investigation | Medium |
| CR-R8 | Data residency violation through CSP infrastructure changes | Medium |

### Phase 6: Mitigation and Approval (Week 5-6)

1. Implement mitigations for each identified risk.
2. Negotiate DPA amendments where CSP standard terms are insufficient.
3. Implement customer-managed encryption keys where feasible.
4. Establish CSP monitoring procedures (certification renewals, sub-processor changes, incident notifications).
5. DPO review and approval.
6. Schedule review: annually or upon CSP service change, new sub-processor, or security incident.

## Common Cloud Migration DPIA Deficiencies

1. **Accepting CSP DPA without review**: CSP standard DPAs may not meet all Art. 28(3) requirements or may include controller-unfavourable terms (e.g., broad sub-processor general authorisation without objection right).
2. **Ignoring sub-processor chain**: CSPs may use dozens of sub-processors; the controller remains responsible for ensuring adequate protection at each level.
3. **Relying on CSP-managed encryption only**: CSP-managed keys provide protection against physical theft but not against government compulsion to the CSP or CSP staff access.
4. **No exit strategy**: Failure to plan for data return and deletion on contract termination, creating lock-in risk and residual data risk.
5. **No transfer assessment for multi-region CSP**: CSP may replicate data across regions including non-EEA locations for redundancy, backup, or CDN purposes.

## Enforcement Precedents

- **DPC Ireland vs Meta (2023)**: EUR 1.2 billion fine for transferring EU user data to US-based cloud infrastructure without valid transfer mechanism.
- **DPC Ireland vs Microsoft (LinkedIn, 2023)**: EUR 310 million fine related to advertising data processing; highlighted the importance of controller-processor role clarity in cloud services.
- **CNIL vs Microsoft 365 Education (2022)**: Raised concerns about data transfers to the US through Microsoft cloud services and insufficient DPA provisions.
- **German Federal Data Protection Commissioner (2022)**: Advised against use of Microsoft 365 in federal agencies due to insufficient transparency about data processing and transfers.
- **Dutch DPA DPIA on Microsoft Office 365 (SLM Rijk, 2022)**: Identified eight high-risk areas in Microsoft 365 processing including diagnostic data collection, data transfers, and insufficient controller access to processing records.
