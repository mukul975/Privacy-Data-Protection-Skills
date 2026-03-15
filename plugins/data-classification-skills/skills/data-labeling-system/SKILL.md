---
name: data-labeling-system
description: >-
  Implements data classification labels and tagging systems including metadata
  tagging, DLP integration, automated label propagation, user-applied labels,
  and label inheritance rules. Covers Microsoft Purview sensitivity labels and
  enterprise labeling architecture. Keywords: data labeling, sensitivity labels,
  metadata tagging, DLP integration, label propagation, Purview, classification.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-classification
  tags: "data-labeling, sensitivity-labels, metadata-tagging, dlp, label-propagation, purview"
---

# Data Classification Labels and Tagging System

## Overview

Data classification labels are the operational mechanism through which classification policy is enforced across the enterprise. Labels attach classification metadata to data assets — documents, emails, database records, and cloud resources — enabling automated enforcement of handling requirements through DLP policies, access controls, and encryption. This skill covers the design and implementation of a labelling system using Microsoft Purview Information Protection as the primary platform, with architecture patterns for automated labelling, user-applied labelling, label inheritance, and cross-platform propagation.

## Label Taxonomy

### Vanguard Financial Services Label Hierarchy

```
Vanguard Classification Labels
├── Public
│   └── (no sub-labels)
├── Internal
│   └── Internal - Project Confidential
├── Confidential
│   ├── Confidential - Customer Data
│   ├── Confidential - Employee Data
│   ├── Confidential - Financial Data
│   └── Confidential - Legal
└── Restricted
    ├── Restricted - Special Category (Art. 9)
    ├── Restricted - Criminal Data (Art. 10)
    ├── Restricted - AML Investigation
    └── Restricted - Board & Strategy
```

### Label Properties

| Label | Colour | Visual Marking | Encryption | DLP Policy | Auto-Apply |
|-------|--------|---------------|-----------|-----------|-----------|
| Public | Green | Footer: "Vanguard Financial Services — Public" | None | None | No |
| Internal | Blue | Footer: "Vanguard Financial Services — Internal Use Only" | Optional | Warn on external | No |
| Confidential | Amber | Header + Footer: "CONFIDENTIAL" | Azure RMS (AES-256) | Warn + audit external; block personal email | Yes (when PII detected with >85% confidence) |
| Restricted | Red | Header + Footer: "RESTRICTED" with red background; watermark on print | Azure RMS (AES-256, double key encryption) | Block all external; block USB/print; alert DPO | Yes (when Art. 9/Art. 10 data detected with >85% confidence) |

## Microsoft Purview Implementation Architecture

### Component Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Microsoft Purview                             │
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │ Sensitivity   │  │ Auto-labelling│  │ DLP Policies          │  │
│  │ Labels        │  │ Policies      │  │ (endpoint, email,     │  │
│  │ (definitions) │  │ (rules)       │  │  SharePoint, Teams)   │  │
│  └──────┬───────┘  └──────┬───────┘  └──────────┬───────────┘  │
│         │                  │                      │              │
│         ▼                  ▼                      ▼              │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              Unified Label Application Engine             │   │
│  └──────────────────────────────────────────────────────────┘   │
│         │                  │                      │              │
└─────────┼──────────────────┼──────────────────────┼──────────────┘
          ▼                  ▼                      ▼
   ┌─────────────┐  ┌──────────────┐  ┌──────────────────────┐
   │ Office Apps  │  │ SharePoint/  │  │ Endpoint DLP         │
   │ (Word, Excel,│  │ OneDrive     │  │ (Windows devices)    │
   │  Outlook)    │  │              │  │                      │
   └─────────────┘  └──────────────┘  └──────────────────────┘
```

### Auto-Labelling Configuration

#### Policy 1: Confidential — Customer PII Detection

| Setting | Value |
|---------|-------|
| **Policy Name** | VFS-AutoLabel-Confidential-CustomerPII |
| **Scope** | All SharePoint sites, OneDrive accounts, Exchange mailboxes |
| **Conditions** | Content contains ANY of: UK National Insurance Number (HIGH confidence), IBAN (HIGH), Vanguard Account Number (HIGH), Credit Card (HIGH + Luhn validated) |
| **Minimum count** | 1 instance of any SIT at HIGH confidence |
| **Label applied** | Confidential - Customer Data |
| **Priority** | 2 (overridden by Restricted auto-label) |

#### Policy 2: Restricted — Special Category Detection

| Setting | Value |
|---------|-------|
| **Policy Name** | VFS-AutoLabel-Restricted-SpecialCategory |
| **Scope** | All SharePoint sites, OneDrive accounts, Exchange mailboxes |
| **Conditions** | Content contains ANY of: ICD-10 codes (MEDIUM+), health terminology trainable classifier (HIGH), biometric template format detection, genetic marker patterns |
| **Minimum count** | 1 instance at MEDIUM confidence or above |
| **Label applied** | Restricted - Special Category (Art. 9) |
| **Priority** | 1 (highest priority — overrides all other auto-labels) |

#### Policy 3: Restricted — Criminal Data Detection

| Setting | Value |
|---------|-------|
| **Policy Name** | VFS-AutoLabel-Restricted-CriminalData |
| **Scope** | HR SharePoint sites, Compliance SharePoint sites |
| **Conditions** | Content contains: DBS reference patterns, criminal conviction terminology, SAR reference numbers |
| **Label applied** | Restricted - Criminal Data (Art. 10) |
| **Priority** | 1 |

### Label Inheritance Rules

| Rule | Description | Implementation |
|------|-------------|---------------|
| **Container inheritance** | Items in a labelled SharePoint site inherit the site's label as minimum | Site sensitivity label propagates to new items; existing items retain higher label |
| **Email attachment inheritance** | Attachments inherit the email's label if attachment label is lower | Outlook plugin checks attachment label vs email label on send |
| **Parent-child inheritance** | Child documents inherit parent folder label as minimum | SharePoint library policy; items cannot be labelled below folder label |
| **No downgrade without approval** | Users cannot remove or downgrade labels without justification | Label policy: require justification text for downgrade; audit log entry |
| **Highest label wins** | When documents are merged or combined, the highest label applies | User training + DLP monitoring for combined documents |

## User-Applied Labelling

### Labelling Responsibilities

| Scenario | Who Labels | How |
|----------|-----------|-----|
| New document creation | Author | Select label from Office ribbon (Word, Excel, PowerPoint) |
| New email composition | Sender | Select label from Outlook toolbar; mandatory before sending external |
| File upload to SharePoint | Uploader | Label prompt on upload if no label detected |
| Data export from system | Exporter | Label selection required before export completes |
| Physical document printing | Printer | Classification header/footer printed automatically; user selects tier if not auto-labelled |

### Mandatory Labelling Policy

| Setting | Value |
|---------|-------|
| **Require label on documents** | Yes — all Word, Excel, PowerPoint documents must have a label before save |
| **Require label on emails** | Yes — for emails to external recipients; recommended for internal |
| **Default label** | Internal (applied if user does not select; user can override up or down) |
| **Justification for downgrade** | Required — user must enter text justification; logged in audit |
| **Justification for removal** | Required — DPO-approved exception only |

## DLP Integration

### DLP Policy Matrix

| Label | External Email | USB/Removable | Print | Screenshot | Cloud Upload |
|-------|---------------|---------------|-------|-----------|-------------|
| Public | Allow | Allow | Allow | Allow | Allow |
| Internal | Warn | Warn | Allow | Allow | Block (non-approved cloud) |
| Confidential | Warn + audit | Block | Secure print | Allow (watermarked) | Block |
| Restricted | Block | Block | Block (unless DPO approved) | Block | Block |

### DLP Alert Routing

| Alert Severity | Label Trigger | Routing |
|---------------|--------------|---------|
| Low | Internal label — external email warn overridden | Security team email |
| Medium | Confidential label — external sharing attempted | Security team + Data Owner |
| High | Restricted label — any policy trigger | DPO + CISO + immediate investigation |
| Critical | Restricted label — data exfiltration indicators | DPO + CISO + Incident Response Team + 15-minute SLA |

## Label Propagation Across Platforms

### Supported Platforms

| Platform | Label Method | Propagation |
|----------|-------------|-------------|
| Microsoft 365 (Word, Excel, PowerPoint) | Native sensitivity label in file metadata | Full support — label travels with file |
| Outlook / Exchange | Email header X-MS-Exchange-Organization-Classification | Label persists in message store and forwarded copies |
| SharePoint Online | Document library metadata + file metadata | Dual storage — library and file level |
| OneDrive for Business | File metadata | Same as SharePoint |
| Teams | Channel/chat message metadata | Limited — file attachments inherit, message labels in compliance |
| PDF export | Visual marking (header/footer) + XMP metadata | Visual marking persists; metadata depends on PDF viewer |
| Azure SQL Database | Column-level sensitivity classification (sys.sensitivity_classifications) | Native Azure SQL feature; integrates with Purview |
| AWS S3 | Object tags (key: classification, value: tier) | AWS-native tagging; read by Macie and IAM policies |
| On-premises file shares | File metadata (NTFS ADS) via AIP Unified Labelling client | Requires AIP client installed on endpoints |

## Enforcement Precedents

- **ICO v Interserve Group (2022)**: GBP 4.4 million — failure to implement adequate data classification and labelling contributed to staff not recognising the sensitivity of data compromised in a breach
- **CNIL v Free Mobile (2022)**: EUR 300,000 — customer personal data stored without classification or access controls; staff could access all customer data regardless of role or need

## Integration Points

- **classification-policy**: Labelling system is the technical implementation of the classification policy
- **auto-data-discovery**: Discovery results trigger auto-labelling for newly detected PII
- **pii-in-unstructured**: PII detection in documents drives label recommendation or auto-application
- **data-inventory-mapping**: Labels feed the data inventory with current classification status per asset
- **data-lineage-tracking**: Labels propagate through data lineage — transformed data inherits source label
