---
name: data-inventory-mapping
description: >-
  Builds comprehensive data inventory per GDPR Art. 30 Records of Processing
  Activities. Covers system-by-system discovery, data flow diagramming,
  third-party identification, and legal basis per category. Keywords: data
  inventory, data mapping, Art 30, RoPA, data flow, processing activities.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-classification
  tags: "data-inventory, data-mapping, art-30, ropa, data-flow, processing-activities"
---

# Data Inventory and Mapping for Classification

## Overview

A data inventory is the foundational artefact for privacy compliance, providing a structured catalogue of all personal data processing activities across the organisation. GDPR Article 30 mandates that controllers maintain Records of Processing Activities (RoPA) containing specific fields including categories of personal data, purposes of processing, categories of recipients, and transfers to third countries. This skill focuses on building the data inventory that feeds into the RoPA, with emphasis on system-by-system discovery, data flow mapping, classification linkage, and legal basis assignment per data category.

## Art. 30 Required Content for Controllers — Art. 30(1)

| Required Field | Description | Classification Relevance |
|---------------|-------------|------------------------|
| **(a) Controller identity** | Name and contact details of controller, joint controller, representative, DPO | Administrative — not classification-dependent |
| **(b) Purposes of processing** | Specific purpose for each processing activity | Purpose determines applicable lawful basis and drives classification-to-handling mapping |
| **(c) Categories of data subjects** | Types of individuals whose data is processed (customers, employees, applicants) | Data subject category affects applicable protections (e.g., children, employees) |
| **(d) Categories of personal data** | Types of personal data processed per activity | Direct output of data classification — personal, special category, criminal |
| **(e) Categories of recipients** | Who receives the data, including processors | Determines transfer and sharing controls |
| **(f) Transfers to third countries** | International transfers and safeguard mechanisms | Triggers Chapter V compliance requirements |
| **(g) Retention periods** | Envisaged time limits for erasure of different categories | Classification tier drives retention policy |
| **(h) Security measures** | General description of Art. 32 technical and organisational measures | Classification tier determines security control level |

## Data Inventory Construction Methodology

### Phase 1: System Discovery (Weeks 1-3)

#### Step 1: Enterprise Application Inventory

Build a complete list of systems that process personal data:

| Discovery Method | Sources | Output |
|-----------------|---------|--------|
| IT asset management system | CMDB, ServiceNow, Lansweeper | Registered applications and servers |
| Procurement records | Vendor contracts, SaaS subscriptions, licence management | Third-party systems processing data |
| Network traffic analysis | Firewall logs, proxy logs, DNS queries | Undocumented data flows to external services |
| Shadow IT discovery | Cloud access security broker (CASB) logs, expense reports for SaaS tools | Unauthorised or unknown applications |
| Department interviews | Business unit leads, data stewards | Departmental tools and local databases |

#### Vanguard Financial Services — System Inventory Example

| System | Type | Department | Data Subjects | Classification Priority |
|--------|------|-----------|---------------|----------------------|
| Salesforce CRM | SaaS | Sales, Customer Service | Customers, prospects | Tier 1 |
| Workday HR | SaaS | Human Resources | Employees, candidates | Tier 1 |
| ADP GlobalView | SaaS | Payroll | Employees | Tier 1 |
| Oracle Data Warehouse | On-premises | Data Engineering | All subjects | Tier 1 |
| SharePoint Online | SaaS | All departments | All subjects | Tier 1 |
| NICE Actimize | On-premises | Compliance | Customers, counterparties | Tier 1 |
| HID Global Access | On-premises | Facilities | Employees, contractors | Tier 2 |
| Cority Occ Health | SaaS | Occupational Health | Employees | Tier 2 |
| Bloomberg Terminal | SaaS | Trading | Counterparties | Tier 2 |
| Microsoft Teams | SaaS | All departments | Employees, external contacts | Tier 2 |
| Adobe Analytics | SaaS | Marketing | Website visitors | Tier 2 |
| ServiceNow ITSM | SaaS | IT | Employees | Tier 3 |
| Confluence Wiki | SaaS | Engineering | Employees | Tier 3 |

### Phase 2: Data Element Mapping (Weeks 3-6)

For each system, document every data element:

#### Step 2: Schema Extraction

- **Structured databases**: Extract schema metadata (table names, column names, data types) via SQL metadata queries or data catalogue APIs
- **SaaS applications**: Use API documentation to enumerate data objects and fields
- **Unstructured repositories**: Catalogue document types and their typical personal data content
- **Automated discovery**: Deploy scanning tools to identify PII in all repositories (see `auto-data-discovery` skill)

#### Step 3: Data Element Classification

For each data element, assign:
- **Personal data classification**: PERSONAL_DIRECT, PERSONAL_INDIRECT, SPECIAL_CATEGORY, CRIMINAL_ART10, PSEUDONYMISED, ANONYMISED, NON_PERSONAL (see `personal-data-test` skill)
- **Classification tier**: Public, Internal, Confidential, Restricted (see `classification-policy` skill)
- **Art. 6 lawful basis**: The legal basis for processing this element for each stated purpose
- **Art. 9(2) condition**: If special category, the specific processing condition

### Phase 3: Data Flow Mapping (Weeks 6-9)

#### Step 4: Intra-System Data Flows

Document how data moves within the organisation:

```
Customer Onboarding Data Flow — Vanguard Financial Services

Customer ──[web form]──► Salesforce CRM
                              │
                    ┌─────────┼──────────┐
                    ▼         ▼          ▼
              Oracle DW   SharePoint   Email (welcome)
              (analytics) (documents)  (notifications)
                    │
                    ▼
              Adobe Analytics
              (web behaviour)
```

#### Step 5: External Data Flows (Third-Party Sharing)

Document all data sharing with external parties:

| Sender System | Recipient | Data Categories | Transfer Mechanism | Legal Safeguard |
|--------------|-----------|----------------|-------------------|-----------------|
| Salesforce CRM | Salesforce Inc. (processor) | Customer personal data | SaaS hosting | Standard Contractual Clauses (2021/914) |
| Workday HR | Workday Inc. (processor) | Employee personal + special category | SaaS hosting | EU-US Data Privacy Framework |
| ADP Payroll | HMRC (statutory recipient) | Employee financial data | Secure file transfer | Legal obligation Art. 6(1)(c) |
| NICE Actimize | NCA (statutory recipient) | Customer AML data (Art. 10) | SAR Online portal | Legal obligation POCA 2002 |
| Oracle DW | Deloitte (auditor) | Anonymised financial data | Encrypted file transfer | Joint controller agreement |

### Phase 4: Legal Basis and Purpose Mapping (Weeks 9-11)

#### Step 6: Purpose-Basis Matrix

For each processing activity, map data categories to purposes and legal bases:

| Processing Activity | Data Category | Purpose | Art. 6 Basis | Art. 9(2) / Art. 10 |
|--------------------|--------------|---------|-------------|---------------------|
| Customer account management | Name, email, address, account number | Contract performance | Art. 6(1)(b) | N/A |
| KYC identity verification | Name, DOB, ID documents, address | Legal obligation (MLR 2017) | Art. 6(1)(c) | N/A |
| Employee payroll | Name, NINO, bank details, salary | Contract performance | Art. 6(1)(b) | N/A |
| Employee diversity monitoring | Ethnicity, sexual orientation | Equality monitoring | Art. 6(1)(a) / 6(1)(c) | Art. 9(2)(a) / 9(2)(b) |
| Building access control | Fingerprint template | Physical security | Art. 6(1)(f) | Art. 9(2)(a) |
| AML monitoring | Transaction patterns, SAR data | Legal obligation (POCA 2002) | Art. 6(1)(c) | Art. 10 — DPA Sch.1 Pt.2 para 10 |
| Website analytics | IP address, cookies, browsing | Legitimate interests | Art. 6(1)(f) | N/A |
| Marketing communications | Email, preferences | Consent | Art. 6(1)(a) | N/A |

### Phase 5: Documentation and Maintenance (Ongoing)

#### Step 7: Inventory Consolidation

Consolidate all discovery into the formal data inventory:
- One record per data element per system
- Cross-referenced to processing activities in the RoPA
- Classification labels applied per element
- Review dates set per classification tier

#### Step 8: Ongoing Maintenance

| Maintenance Activity | Frequency | Responsible |
|---------------------|-----------|------------|
| Automated discovery scan reconciliation | Monthly | Privacy Engineering |
| New system onboarding inventory | Per new system deployment | System Owner + Privacy Analyst |
| Department data steward review | Quarterly | Data Stewards |
| Full inventory accuracy audit | Annually | DPO |
| Classification reclassification review | Annually (borderline: 6-monthly) | Privacy Analyst |

## Data Flow Diagram Standards

### Notation Convention (Based on DFD Level 0/1)

| Symbol | Meaning |
|--------|---------|
| Rectangle | External entity (data subject, third party, regulator) |
| Rounded rectangle | Process (system or application) |
| Open rectangle (two parallel lines) | Data store (database, file share) |
| Arrow | Data flow (labelled with data categories) |
| Dashed arrow | Optional or conditional data flow |
| Red border | Contains special category or criminal data |
| Blue border | International transfer |

## Enforcement Precedents

- **Österreichische Datenschutzbehörde (Austrian DPA) v Local Bakery Chain (2020)**: EUR 4,000 fine for failure to maintain Art. 30 records. The DPA noted that even small organisations must maintain processing records.
- **CNIL v Sergic (2019)**: EUR 400,000 fine, partly for inadequate data mapping — the controller could not demonstrate it knew where personal data was stored, leading to a data breach going undetected.
- **ICO v British Airways (2020)**: GBP 20 million fine, where inadequate data mapping contributed to delayed breach detection — the controller lacked visibility into personal data flows through its web infrastructure.

## Integration Points

- **auto-data-discovery**: Automated scanning feeds data elements into the inventory
- **personal-data-test**: Classification decisions applied per data element in the inventory
- **special-category-data**: Art. 9 data flagged and mapped to processing conditions
- **criminal-data-handling**: Art. 10 data identified and mapped to national law authorisation
- **data-lineage-tracking**: Lineage graphs extend the static inventory with dynamic flow information
