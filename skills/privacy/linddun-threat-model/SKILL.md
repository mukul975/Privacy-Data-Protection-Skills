---
name: linddun-threat-model
description: >-
  Conduct LINDDUN privacy threat modeling across all seven categories: Linking,
  Identifying, Non-repudiation, Detecting, Data Disclosure, Unawareness, and
  Non-compliance. Includes DFD-based analysis, threat trees, privacy-specific
  mitigation strategies, and integration with STRIDE security threat modeling.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-engineering
  tags: "linddun, threat-modeling, privacy-threats, dfd-analysis, privacy-mitigation"
---

# LINDDUN Privacy Threat Modeling

## Overview

LINDDUN is a systematic privacy threat modeling methodology developed by the DistriNet research group at KU Leuven. It provides a structured approach to identify and mitigate privacy threats in software systems. The acronym represents seven privacy threat categories that map to violations of privacy properties defined in ISO/IEC 29100.

## The Seven LINDDUN Threat Categories

### L — Linking

**Definition**: The ability to associate two or more data items or actions with an individual or group, beyond what is intended by the data subject.

**Privacy Property Violated**: Unlinkability

**Threat Scenarios**:
- Cross-referencing anonymized datasets to re-identify individuals
- Correlating browsing behavior across websites using fingerprinting
- Linking social media profiles to real identities through metadata
- Combining location data points to infer home/work addresses

**Mitigation Strategies**:
| Strategy | Technique | Implementation |
|----------|-----------|----------------|
| Data minimization | Collect only necessary attributes | Review each data field against stated purpose |
| Pseudonymization | Replace identifiers with tokens | Use cryptographic pseudonymization with key separation |
| Mix networks | Obscure communication patterns | Route messages through anonymity networks |
| Aggregation | Present only group-level data | Enforce minimum group size (k>=5) for any query result |
| Session unlinkability | Prevent cross-session tracking | Rotate session tokens, avoid persistent identifiers |

### I — Identifying

**Definition**: The ability to identify a data subject from a set of data items, connecting them to a known individual.

**Privacy Property Violated**: Anonymity

**Threat Scenarios**:
- Direct identification from unmasked PII in logs
- Quasi-identifier attacks (combining age, ZIP code, gender)
- Facial recognition from images in datasets
- Voice identification from audio recordings
- Writing style analysis (stylometry) in anonymous forums

**Mitigation Strategies**:
| Strategy | Technique | Implementation |
|----------|-----------|----------------|
| Anonymization | Remove direct identifiers | Strip names, emails, SSNs before processing |
| k-Anonymity | Generalize quasi-identifiers | Ensure each record shares attributes with k-1 others |
| Differential privacy | Add calibrated noise | Apply epsilon-differential privacy to query responses |
| Data masking | Obscure identifying fields | Replace with realistic synthetic values |
| Access control | Restrict who can see raw data | Implement need-to-know access with purpose verification |

### N — Non-repudiation

**Definition**: The inability of a data subject to deny having performed an action, even when such denial would be desirable for privacy.

**Privacy Property Violated**: Plausible deniability

**Threat Scenarios**:
- Immutable audit logs linking users to actions
- Digital signatures proving authorship of documents
- Non-repudiable transaction records
- Email delivery confirmations and read receipts
- Blockchain-based records that cannot be denied or deleted

**Mitigation Strategies**:
| Strategy | Technique | Implementation |
|----------|-----------|----------------|
| Deniable encryption | Enable plausible deniability | Use deniable encryption schemes for sensitive data |
| Group signatures | Hide individual identity in group | Implement group signature schemes for authenticated actions |
| Minimal logging | Log only what is legally required | Review and minimize audit trail scope |
| Aggregate reporting | Report actions at group level | Aggregate activity reports rather than individual-level |
| Configurable receipts | Let users control acknowledgments | Allow opt-out of read receipts and delivery confirmations |

### D — Detecting

**Definition**: The ability to determine whether a data subject has been involved in an action or is present in a dataset, even without identifying them specifically.

**Privacy Property Violated**: Undetectability

**Threat Scenarios**:
- Traffic analysis revealing communication patterns
- Database membership inference attacks
- Timing attacks revealing user activity
- Side-channel attacks revealing data access patterns
- Presence detection through network metadata

**Mitigation Strategies**:
| Strategy | Technique | Implementation |
|----------|-----------|----------------|
| Traffic padding | Mask communication patterns | Generate dummy traffic to obscure real patterns |
| Steganography | Hide data within other data | Embed sensitive communications in innocuous content |
| Constant-time operations | Prevent timing analysis | Implement constant-time algorithms for sensitive operations |
| Oblivious RAM | Hide access patterns | Use ORAM protocols for privacy-critical data access |
| Differential privacy | Provide membership privacy | Apply differential privacy to prevent membership inference |

### D — Data Disclosure

**Definition**: Unauthorized exposure of personal data to parties who should not have access.

**Privacy Property Violated**: Confidentiality

**Threat Scenarios**:
- SQL injection exposing database contents
- Misconfigured cloud storage buckets
- Insider threats with excessive access privileges
- Man-in-the-middle attacks on unencrypted channels
- API responses returning excessive data fields
- Backup media loss or theft

**Mitigation Strategies**:
| Strategy | Technique | Implementation |
|----------|-----------|----------------|
| Encryption | Protect data at rest and in transit | AES-256 at rest, TLS 1.3 in transit |
| Access control | Enforce least privilege | RBAC with regular access reviews |
| Input validation | Prevent injection attacks | Parameterized queries, input sanitization |
| API field filtering | Return only requested fields | Implement field-level access control in APIs |
| DLP | Detect and prevent data exfiltration | Deploy DLP at network egress and endpoints |

### U — Unawareness

**Definition**: Data subjects being insufficiently aware of data processing activities, their rights, or the consequences of providing or withholding data.

**Privacy Property Violated**: Transparency, Intervenability

**Threat Scenarios**:
- Hidden data collection through tracking pixels
- Opaque algorithmic decision-making
- Buried privacy policies with complex legal language
- Undisclosed data sharing with third parties
- Lack of notification when processing purposes change
- No mechanism for data subjects to exercise rights

**Mitigation Strategies**:
| Strategy | Technique | Implementation |
|----------|-----------|----------------|
| Layered notices | Progressive disclosure | Short notice + full policy + just-in-time |
| Privacy dashboards | Centralized visibility | User-facing dashboard showing all data held |
| Consent management | Granular, informed consent | Purpose-specific consent with clear descriptions |
| Explainable AI | Algorithmic transparency | Provide meaningful explanations of automated decisions |
| Right facilitation | Easy rights exercise | Self-service portal for access, correction, deletion |

### N — Non-compliance

**Definition**: Processing personal data in ways that violate applicable laws, regulations, standards, or organizational policies.

**Privacy Property Violated**: Policy and consent compliance

**Threat Scenarios**:
- Processing without valid legal basis
- Failing to honor data subject rights within deadlines
- Cross-border transfers without adequate safeguards
- Retaining data beyond the stated retention period
- Processing children's data without parental consent
- Failing to conduct required impact assessments

**Mitigation Strategies**:
| Strategy | Technique | Implementation |
|----------|-----------|----------------|
| Compliance mapping | Map processing to legal bases | Document legal basis per processing activity per jurisdiction |
| Automated enforcement | Technical compliance controls | Automated retention enforcement, consent verification |
| DPIA process | Impact assessment for high-risk processing | Mandatory DPIA before deploying new high-risk processing |
| Regulatory monitoring | Track legal developments | Subscribe to regulatory updates, conduct periodic gap analysis |
| Audit program | Verify ongoing compliance | Annual compliance audits with corrective action tracking |

## DFD-Based Threat Analysis Process

### Step 1: Create Privacy-Annotated Data Flow Diagram

```
[Data Subject] ---(personal data)--> [Web Application]
     ^                                      |
     |                                      v
  [Notice]                          [Application Server]
                                          |
                            +-------------+-------------+
                            |             |             |
                            v             v             v
                    [User Database] [Analytics DB] [Third-Party API]
                    (encrypted)     (pseudonymized) (data sharing)
```

Annotate each element with:
- Data types flowing through (PII categories)
- Trust boundaries crossed
- Storage locations and durations
- Processing purposes
- Access controls in place

### Step 2: Map Threats to DFD Elements

| DFD Element | L | I | N | D(etect) | D(isclose) | U | N(on-comply) |
|-------------|---|---|---|----------|------------|---|-------------|
| Data flows | X | X | | X | X | | |
| Data stores | X | X | | | X | | X |
| Processes | X | X | X | X | X | X | X |
| External entities | | X | | X | X | X | X |

### Step 3: Build Threat Trees

For each applicable threat category per DFD element, construct a threat tree:

```
Identifying Threat to User Database
├── Direct identifier exposure
│   ├── SQL injection reveals raw PII
│   ├── Backup media contains unencrypted PII
│   └── Admin access to production database
├── Quasi-identifier attack
│   ├── Combination of age + ZIP + gender
│   └── Temporal correlation of records
└── Inference attack
    ├── Aggregate query with small group size
    └── Differential attack across query results
```

### Step 4: Prioritize and Mitigate

Use a risk matrix to prioritize identified threats:

| Likelihood / Impact | Negligible | Limited | Significant | Maximum |
|---------------------|-----------|---------|-------------|---------|
| Very Likely | Medium | High | Critical | Critical |
| Likely | Low | Medium | High | Critical |
| Possible | Low | Medium | Medium | High |
| Unlikely | Low | Low | Medium | Medium |
| Rare | Low | Low | Low | Medium |

## LINDDUN and STRIDE Integration

| LINDDUN Category | Related STRIDE Category | Overlap Area |
|-------------------|----------------------|--------------|
| Data Disclosure | Information Disclosure | Both address unauthorized data exposure |
| Non-compliance | Tampering | Integrity of consent records |
| Detecting | Information Disclosure | Metadata leakage |
| Identifying | Information Disclosure | PII exposure |
| Non-repudiation | Repudiation | Opposing perspectives on the same property |

## Practical Application at Cipher Engineering Labs

### Threat Modeling Workshop Agenda (4 hours)

1. **System Overview** (30 min): Present the system architecture and data flows
2. **DFD Construction** (45 min): Collaboratively build privacy-annotated DFD
3. **Threat Identification** (90 min): Walk through each LINDDUN category per DFD element
4. **Prioritization** (30 min): Score threats on risk matrix
5. **Mitigation Planning** (45 min): Identify controls for high and critical risks

### Deliverables
- Privacy-annotated Data Flow Diagram
- LINDDUN Threat Register (all identified threats with risk scores)
- Mitigation Plan (prioritized controls for high/critical threats)
- Residual Risk Statement

## References

- Deng, M., Wuyts, K., Scandariato, R., Preneel, B., and Joosen, W. "A Privacy Threat Analysis Framework: Supporting the Elicitation and Fulfillment of Privacy Requirements." Requirements Engineering, 16(1):3-32, 2011.
- Wuyts, K. and Joosen, W. "LINDDUN Privacy Threat Modeling: A Tutorial." CW Reports, KU Leuven, 2015.
- LINDDUN GO — Lightweight approach: linddun.org
- ISO/IEC 29100:2011 — Information Technology — Security Techniques — Privacy Framework
- OWASP Privacy Risks Project
