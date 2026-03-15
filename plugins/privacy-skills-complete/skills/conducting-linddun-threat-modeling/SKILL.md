---
name: conducting-linddun-threat-modeling
description: >-
  Complete guide to LINDDUN privacy threat modeling methodology covering seven
  threat categories: Linking, Identifying, Non-repudiation, Detecting, Data Disclosure,
  Unawareness, and Non-compliance. Includes DFD-based analysis, threat tree catalogs,
  mitigation mapping to privacy design patterns, and step-by-step process.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-by-design
  tags: "linddun, threat-modeling, privacy-threats, dfd-analysis, privacy-risk-assessment"
---

# Conducting LINDDUN Threat Modeling

## Overview

LINDDUN is a systematic privacy threat modeling methodology developed by the DistriNet research group at KU Leuven. It provides a structured approach to identifying privacy threats in software systems through Data Flow Diagram (DFD) analysis and threat tree catalogs. LINDDUN stands for seven privacy threat categories:

- **L**inking — Associating data items with each other or with an individual
- **I**dentifying — Learning the identity of a data subject
- **N**on-repudiation — Being unable to deny an action or association
- **D**etecting — Deducing that an individual is involved in a process
- **D**ata Disclosure — Exposing personal data to unauthorized parties
- **U**nawareness — Data subjects being unaware of data processing
- **N**on-compliance — Failing to comply with privacy legislation or policies

LINDDUN complements security threat modeling (STRIDE) by focusing specifically on privacy threats. While STRIDE addresses confidentiality, integrity, and availability, LINDDUN addresses unlinkability, anonymity, plausible deniability, undetectability, confidentiality of data content, content awareness, and policy compliance.

## LINDDUN Threat Categories Detailed

### L — Linking

**Definition:** An adversary can sufficiently distinguish whether two items of interest (IOI) are related or not within a particular context.

**DFD element applicability:** Data flows, data stores, processes.

**Examples:**
- Linking browsing sessions across websites via cookies or fingerprinting
- Linking pseudonymized records across datasets via quasi-identifiers
- Linking transactions to the same individual over time

**Threat trees (selected):**
- L1: Linking via identifiers shared across contexts
- L2: Linking via quasi-identifier combination (age + postal code + gender)
- L3: Linking via temporal correlation (simultaneous events)
- L4: Linking via behavioral patterns (unique usage signatures)

**Mitigations:** HIDE (Dissociate, Mix), SEPARATE (Isolate), MINIMIZE (Strip), differential privacy, pseudonymization with context separation.

### I — Identifying

**Definition:** An adversary can sufficiently identify a data subject within a set of data subjects.

**DFD element applicability:** Data flows, data stores, external entities.

**Examples:**
- Re-identifying individuals in an anonymized dataset via linkage attacks
- Identifying a user from aggregated location data
- Identifying the author of an anonymous document via stylometry

**Threat trees (selected):**
- I1: Identification via direct identifiers (name, email, SSN)
- I2: Identification via quasi-identifier combination
- I3: Identification via unique behavioral patterns
- I4: Identification via metadata (IP address, device fingerprint)

**Mitigations:** HIDE (Encrypt, Obfuscate), MINIMIZE (Strip), ABSTRACT (Group, Summarize), k-anonymity, differential privacy.

### N — Non-repudiation

**Definition:** A data subject is unable to deny having performed an action or being associated with specific data.

**DFD element applicability:** Data flows, processes, data stores.

**Examples:**
- Digital signatures on messages prevent denying authorship
- Transaction logs linking purchases to an identity
- Audit trails that irrevocably associate actions with individuals

**Threat trees (selected):**
- N1: Non-repudiation via digital signatures or cryptographic evidence
- N2: Non-repudiation via witness testimony or log entries
- N3: Non-repudiation via photographic or biometric evidence

**Mitigations:** HIDE (Mix), group signatures, ring signatures, deniable encryption.

### D — Detecting

**Definition:** An adversary can sufficiently distinguish whether an item of interest (IOI) exists or not.

**DFD element applicability:** Data flows, processes.

**Examples:**
- Detecting that an individual visited a specific website via traffic analysis
- Detecting that a patient is in a hospital database (membership inference)
- Detecting the existence of encrypted communication between parties

**Threat trees (selected):**
- D1: Detection via traffic analysis (communication metadata)
- D2: Detection via timing side channels
- D3: Detection via presence in a dataset (membership inference)
- D4: Detection via access pattern analysis

**Mitigations:** HIDE (Mix, Obfuscate), cover traffic, onion routing, steganography, ORAM.

### D — Data Disclosure

**Definition:** Personal data is disclosed to or accessed by unauthorized parties.

**DFD element applicability:** Data flows, data stores, processes.

**Examples:**
- Unencrypted personal data intercepted in transit
- Database breach exposing customer records
- Employee accessing records without authorization

**Threat trees (selected):**
- DD1: Disclosure via unencrypted communication channels
- DD2: Disclosure via unauthorized database access
- DD3: Disclosure via side-channel attacks on encrypted data
- DD4: Disclosure via excessive data sharing with third parties
- DD5: Disclosure via improper data deletion (residual data)

**Mitigations:** HIDE (Encrypt), access control, TLS 1.3, field-level encryption, secure deletion, DLP systems.

### U — Unawareness

**Definition:** Data subjects are unaware of the collection, processing, or sharing of their personal data.

**DFD element applicability:** External entities (data subjects), processes.

**Examples:**
- Collecting data without providing a privacy notice
- Processing data for purposes not disclosed to the data subject
- Sharing data with third parties without informing the data subject

**Threat trees (selected):**
- U1: Unawareness due to missing or inadequate privacy notice
- U2: Unawareness of purpose change (purpose creep without notification)
- U3: Unawareness of third-party sharing
- U4: Unawareness of automated decision-making or profiling

**Mitigations:** INFORM (Supply, Notify, Explain), layered privacy notices, just-in-time notifications, consent management.

### N — Non-compliance

**Definition:** The system or organization fails to comply with applicable privacy legislation, policies, or standards.

**DFD element applicability:** All DFD elements.

**Examples:**
- Processing without a valid lawful basis
- Failing to respond to data subject access requests within 30 days
- Not conducting a required DPIA for high-risk processing
- Retaining data beyond the defined retention period

**Threat trees (selected):**
- NC1: Non-compliance with lawful basis requirements
- NC2: Non-compliance with data subject rights (Art. 15-22)
- NC3: Non-compliance with cross-border transfer rules (Chapter V)
- NC4: Non-compliance with data breach notification (Art. 33-34)
- NC5: Non-compliance with accountability obligations (Art. 5(2), Art. 24)

**Mitigations:** ENFORCE (Create, Maintain, Uphold), DEMONSTRATE (Record, Audit, Report), GDPR compliance framework.

## LINDDUN Process

### Step 1: Define the System Scope

Create a Data Flow Diagram (DFD) of the system showing:
- **External entities** (data subjects, third parties, regulators)
- **Processes** (system components that process data)
- **Data stores** (databases, file systems, logs)
- **Data flows** (movement of data between elements)
- **Trust boundaries** (boundaries between different trust domains)

### Step 2: Map Threats to DFD Elements

For each DFD element, determine which LINDDUN threat categories apply:

| DFD Element | L | I | N | D | DD | U | NC |
|-------------|---|---|---|---|----|---|-----|
| External entity (data subject) | | X | | | | X | |
| External entity (third party) | | | | | X | | X |
| Process | X | X | X | X | X | | X |
| Data store | X | X | X | | X | | X |
| Data flow | X | X | X | X | X | | X |

### Step 3: Elicit Threats Using Threat Trees

For each applicable threat category on each DFD element, walk through the threat tree catalog to identify specific threats. Document each threat with:
- Threat ID
- Category (LINDDUN letter)
- DFD element
- Description
- Likelihood (1-5)
- Impact (1-5)
- Risk score (likelihood x impact)

### Step 4: Prioritize Threats

Rank threats by risk score. Apply risk acceptance thresholds:
- Risk 1-6: Accept with documentation
- Risk 7-12: Mitigate within 6 months
- Risk 13-19: Mitigate within 3 months
- Risk 20-25: Mitigate immediately

### Step 5: Select Mitigations

Map each threat to privacy design patterns and specific technical controls. Document the mitigation strategy and responsible team.

### Step 6: Validate Mitigations

Verify that selected mitigations adequately address each threat. Update the DFD to reflect implemented controls. Re-assess residual risk.

## Key Regulatory References

- GDPR Article 25 — Data protection by design and by default
- GDPR Article 35 — Data protection impact assessment
- GDPR Article 32 — Security of processing
- EDPB Guidelines 4/2019 on Article 25 Data Protection by Design and by Default
- Deng, M., Wuyts, K., Scandariato, R., Preneel, B., & Joosen, W. (2011). "A privacy threat analysis framework: supporting the elicitation and fulfillment of privacy requirements." Requirements Engineering, 16(1), 3-32.
- LINDDUN: linddun.org — Official methodology documentation and threat tree catalogs
