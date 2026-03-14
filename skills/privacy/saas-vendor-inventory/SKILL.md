---
name: saas-vendor-inventory
description: >-
  SaaS vendor data processing inventory management. Covers shadow IT discovery,
  API-based data flow detection, processing purpose mapping, contract status
  tracking, and continuous inventory reconciliation for cloud service providers.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: vendor-privacy-management
  tags: "saas-inventory, shadow-it, data-flow-detection, vendor-register, cloud-services"
---

# SaaS Vendor Data Processing Inventory

## Overview

Modern organizations rely on dozens to hundreds of SaaS applications, many of which process personal data. GDPR Article 30 requires controllers to maintain records of processing activities, which includes documenting all processors. Shadow IT — SaaS applications adopted by business units without formal procurement or privacy review — creates significant compliance risk because unrecorded processing cannot be properly governed.

The EDPB Guidelines 07/2020 emphasize that controllers cannot claim ignorance of processing performed by vendors they engage, even if the engagement happened informally. Summit Cloud Partners maintains a comprehensive SaaS Vendor Data Processing Inventory to track all cloud services processing personal data, including those discovered through shadow IT detection.

## Inventory Framework

### Tier 1: Sanctioned SaaS — Formally Procured

Applications that have gone through formal procurement, privacy review, and DPA execution.

| Field | Description |
|-------|-------------|
| Vendor name | Legal entity name |
| Product/service name | SaaS product name |
| Category | CRM, HR, Analytics, Communication, DevOps, etc. |
| Business owner | Department and named individual |
| Procurement date | When the service was contracted |
| DPA status | Executed / In negotiation / Not required |
| DPA reference | DPA document reference number |
| Privacy review status | Completed / In progress / Pending |
| Risk tier | Per vendor risk scoring model |
| Personal data categories | What personal data is processed |
| Data subjects | Whose data is processed |
| Processing purposes | Why data is processed |
| Processing locations | Where data is stored/processed |
| Integration method | SSO, API, manual upload, etc. |
| Data flow direction | Inbound / Outbound / Bidirectional |
| Contract expiry | When the contract term ends |
| Auto-renewal date | When auto-renewal triggers |
| Annual cost | Total annual spend |
| License count | Number of active users/seats |

### Tier 2: Known Unsanctioned — Shadow IT Detected

Applications detected through discovery tools that lack formal procurement or privacy review.

| Field | Description |
|-------|-------------|
| Application name | As detected |
| Detection method | CASB, DNS, expense, SSO log, etc. |
| Detection date | When first observed |
| Usage scope | Estimated users and frequency |
| Likely data categories | Inferred from application type |
| Risk assessment | Preliminary risk level |
| Remediation status | Under review / Sanctioning in progress / Blocked / Accepted |
| Business unit | Department(s) using the application |

### Tier 3: Evaluated and Excluded

Applications evaluated and determined to not process personal data.

| Field | Description |
|-------|-------------|
| Application name | Product name |
| Evaluation date | When reviewed |
| Determination | No personal data processing |
| Rationale | Why excluded from inventory |
| Next review date | When to re-evaluate |

## Shadow IT Discovery Methods

### Method 1: Cloud Access Security Broker (CASB)

Deploy a CASB solution to monitor network traffic and identify cloud service usage.

**Detection Capabilities:**
- SaaS application identification via API call pattern matching
- User activity monitoring across sanctioned and unsanctioned services
- Data transfer volume estimation
- Risk scoring of discovered applications

**Implementation at Summit Cloud Partners:**

| Component | Detail |
|-----------|--------|
| CASB vendor | Deployed as inline proxy and API connector |
| Coverage | All corporate network egress and managed endpoints |
| Discovery scope | HTTP/HTTPS traffic to known SaaS domains |
| Update frequency | Real-time discovery, weekly consolidated reporting |
| Integration | Feeds into SaaS inventory system via API |

### Method 2: DNS and Firewall Log Analysis

Analyze DNS resolution logs and firewall traffic logs to identify connections to SaaS providers.

**Process:**
1. Aggregate DNS query logs from internal resolvers
2. Match resolved domains against SaaS provider domain databases
3. Cross-reference with sanctioned vendor list
4. Flag unmatched SaaS domains for investigation

### Method 3: SSO and Identity Provider Logs

Review identity provider (IdP) logs for OAuth consent grants and SAML integrations.

**Detection Signals:**
- OAuth application consent grants not in approved list
- SAML service provider registrations
- OpenID Connect client registrations
- API token generation for third-party services

### Method 4: Expense and Procurement Analysis

Review corporate expense reports and credit card statements for SaaS subscriptions.

**Detection Signals:**
- Recurring charges to known SaaS providers
- Expense claims categorized as "software" or "subscriptions"
- Purchase order requests for cloud services bypassing IT procurement

### Method 5: API Integration Audit

Scan internal systems for outbound API connections to third-party services.

**Detection Signals:**
- Outbound API calls to non-sanctioned endpoints
- Webhook configurations sending data to external services
- Integration platform (Zapier, Workato, etc.) connections
- Custom script connections to third-party APIs

## Data Flow Mapping

For each sanctioned SaaS vendor, document the complete data flow:

```
Data Flow Template:

Summit Cloud Partners Internal Systems
         │
         ├─► [SaaS Application Name]
         │     │
         │     ├─ Integration: [SSO/API/Manual Upload/Browser Plugin]
         │     ├─ Authentication: [SAML SSO / OAuth 2.0 / Username-Password]
         │     ├─ Encryption in transit: [TLS version]
         │     ├─ Data categories sent: [list]
         │     ├─ Data categories received: [list]
         │     ├─ Data categories stored by vendor: [list]
         │     ├─ Vendor processing locations: [locations]
         │     ├─ Vendor sub-processors: [per sub-processor register]
         │     ├─ Data retention at vendor: [period]
         │     └─ Data deletion capability: [Yes/No — method]
         │
         └─► [Next SaaS Application]
```

## Inventory Reconciliation

### Quarterly Reconciliation Process

| Step | Activity | Responsible |
|------|----------|-------------|
| 1 | Extract current CASB discovery report | InfoSec |
| 2 | Extract current sanctioned vendor list | Privacy Team |
| 3 | Compare: identify new unsanctioned applications | Privacy Team |
| 4 | Compare: identify sanctioned apps no longer in use | Privacy Team |
| 5 | Verify DPA status for all sanctioned vendors | Privacy Team |
| 6 | Check contract expiry dates (90-day lookahead) | Legal/Procurement |
| 7 | Update inventory records | Privacy Team |
| 8 | Report to DPO | Privacy Team Lead |

### Reconciliation Outcomes

| Finding | Action |
|---------|--------|
| New unsanctioned SaaS discovered | Initiate shadow IT remediation workflow |
| Sanctioned SaaS no longer in use | Initiate vendor termination data workflow |
| DPA expired or missing | Expedite DPA execution or service suspension |
| Contract approaching expiry | Trigger renewal privacy review |
| Data processing scope change detected | Initiate DPA amendment review |

## Contract Status Tracking

| Status | Definition | Action Required |
|--------|-----------|-----------------|
| **Active — Compliant** | Contract active, DPA executed, privacy review current | Standard monitoring |
| **Active — DPA Pending** | Contract active, DPA in negotiation | Expedite DPA; restrict data sharing if > 30 days |
| **Active — Review Overdue** | Contract active, privacy review past due | Schedule immediate review |
| **Expiring (< 90 days)** | Contract approaching expiry | Initiate renewal assessment |
| **Expired** | Contract term ended | Initiate termination data workflow |
| **Suspended** | Service suspended pending privacy issue resolution | Track resolution |
| **Terminated** | Contract terminated, data return/deletion in progress | Track deletion certification |

## Key Regulatory References

- GDPR Article 30(1)(d) — Controller ROPA must include categories of recipients (processors)
- GDPR Article 28(1) — Use only processors with sufficient guarantees
- GDPR Article 5(2) — Accountability principle — must document all processing relationships
- GDPR Article 24 — Controller responsibility for demonstrating compliance
- EDPB Guidelines 07/2020 — Controller knowledge of processing operations
- EDPB Guidelines 04/2019 — Data Protection by Design and by Default (privacy in procurement)
