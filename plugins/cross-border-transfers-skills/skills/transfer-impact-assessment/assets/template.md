# Transfer Impact Assessment — Documentation Template

## TIA Identification

| Field | Value |
|-------|-------|
| TIA Reference | TIA-2025-HK-001 |
| Assessment Date | 10 March 2025 |
| Assessed By | Elisa Brandt, Head of Data Protection, Athena Global Logistics GmbH |
| Reviewed By | Dr. Stefan Mueller, External Privacy Counsel |
| Version | 1.0 |

## Step 1: Transfer Mapping

| Element | Detail |
|---------|--------|
| Data Exporter | Athena Global Logistics GmbH, Friedrichstrasse 112, 10117 Berlin, Germany |
| Exporter Role | Controller |
| Data Importer | TransPacific Freight Solutions Ltd, 88 Harbour Road, Wan Chai, Hong Kong SAR |
| Importer Role | Processor |
| Transfer Mechanism | SCCs Module 2 (Commission Implementing Decision (EU) 2021/914) executed 15 March 2025 |
| Data Subject Categories | Shipping customers (consignors and consignees), customs brokers, warehouse workers |
| Personal Data Categories | Full name, business email, business phone, shipping address, customs identification numbers, consignment references |
| Special Category Data | None |
| Transfer Purpose | Freight forwarding contract fulfilment — customs clearance and last-mile delivery in Asia-Pacific |
| Transfer Frequency | Continuous real-time API; daily batch transfer at 02:00 UTC |
| Data Format | JSON via REST API (real-time); CSV via SFTP (batch) |
| Retention in Destination | 36 months from shipment completion |
| Onward Transfers | CloudVault Asia Pte Ltd (Singapore) — cloud hosting; Pinnacle Data Services Co Ltd (Bangkok) — customs data entry |

## Step 2: Transfer Tool

| Element | Detail |
|---------|--------|
| Mechanism | SCCs Module 2 (C2P) |
| Version | Commission Implementing Decision (EU) 2021/914 of 4 June 2021 |
| Execution Date | 15 March 2025 |
| Key Clauses Assessed | Clause 14 (local laws and obligations), Clause 15 (government access obligations) |
| Annex Completeness | Annex I (complete), Annex II (complete), Annex III (complete — 2 sub-processors listed) |

## Step 3: Destination Country Assessment

### 3a: Identified Surveillance Laws

| Law | Statutory Reference | Scope | Relevance |
|-----|-------------------|-------|-----------|
| Interception of Communications and Surveillance Ordinance | Cap. 589, Laws of Hong Kong | Authorises interception of communications and covert surveillance by law enforcement | High — applies to electronic communications including transferred data |
| National Security Law | Promulgated 30 June 2020 | Criminalises secession, subversion, terrorism, and collusion; grants broad investigative powers | Medium — broad powers but primarily targeted at national security offences; freight logistics data unlikely to be of interest |
| Safeguarding National Security Ordinance | Enacted March 2024 | Supplements NSL with additional offences including external interference; expanded police powers | Medium — extends government powers beyond NSL scope |
| Personal Data (Privacy) Ordinance | Cap. 486, Laws of Hong Kong | Data protection framework; provides exemptions for crime prevention and national security | Low — generally protective but exemptions exist |

### 3b: European Essential Guarantees Assessment

#### EEG 1: Clear, Precise, and Accessible Rules

| Criterion | Assessment | Score |
|-----------|-----------|-------|
| Government access based on published legislation | Cap. 589 and NSL are publicly available statutes | Met |
| Scope of access clearly defined in law | Cap. 589 specifies categories of offences; NSL scope is broad regarding national security | Partially Met |
| Categories of data and persons specified | Cap. 589 targets specific subjects; NSL does not clearly limit categories | Not Met |
| Conditions and limitations for access stated | Cap. 589 requires executive authorisation or judicial authorisation; NSL has fewer conditions | Partially Met |

**EEG 1 Score: 50% (2 of 4 criteria met)**

#### EEG 2: Necessity and Proportionality

| Criterion | Assessment | Score |
|-----------|-----------|-------|
| Necessity requirement for each access request | Cap. 589 requires reasonable grounds; NSL uses broader necessity standard | Partially Met |
| Proportionality of access scope to stated objective | Cap. 589 proportionality review by Commissioner; NSL proportionality is less clear | Not Met |
| Safeguards against bulk or untargeted access | Cap. 589 targets specific subjects; no evidence of bulk surveillance capability equivalent to NSA | Met |
| Data minimisation and retention limits for accessed data | Cap. 589 includes retention limits for intercepted material; NSL does not specify | Not Met |

**EEG 2 Score: 25% (1 of 4 criteria met)**

#### EEG 3: Independent Oversight

| Criterion | Assessment | Score |
|-----------|-----------|-------|
| Prior judicial or independent authorisation required | Cap. 589 panel judge or executive authorisation; NSL designated judges are HKSAR-appointed | Met |
| Ongoing independent oversight of access activities | Commissioner on Interception of Communications provides annual oversight reports | Met |
| Oversight body genuinely independent from executive | Commissioner is appointed by Chief Executive; designated NSL judges selected by Chief Executive | Not Met |

**EEG 3 Score: 67% (2 of 3 criteria met)**

#### EEG 4: Effective Remedies

| Criterion | Assessment | Score |
|-----------|-----------|-------|
| Individuals can challenge access in court or before independent body | Judicial review available for Cap. 589 actions; NSL cases have limited appeal pathways | Met |
| Notification mechanism exists (even if delayed) | Cap. 589 does not require notification; NSL does not require notification | Not Met |
| Effective remedies available (compensation, deletion, injunction) | Damages available under Cap. 589 via Commissioner complaint; limited under NSL | Partially Met |

**EEG 4 Score: 33% (1 of 3 criteria met)**

### 3c: Practical Risk Assessment

| Factor | Assessment |
|--------|-----------|
| Data sensitivity | Low-Medium — commercial freight data; no special category data |
| Importer profile | Commercial logistics operator; not a technology or communications provider |
| Sector risk | Low — freight logistics sector has minimal historical exposure to government access requests |
| Data volume | Medium — approximately 50,000 records per month |
| Technical architecture | Importer staff access plaintext data for customs processing |
| Historical government access | No reported government access requests to the importer in the past 5 years |

### 3d: Preliminary Conclusion

**AMBER** — Protection gaps exist, particularly in EEG 2 (proportionality under NSL) and EEG 4 (notification and remedies). However, the practical risk to freight logistics data is low, and the gaps can be mitigated with supplementary measures.

## Step 4: Supplementary Measures

| Measure ID | Type | Description | Gap Addressed | Status |
|-----------|------|-------------|---------------|--------|
| T4 | Technical | TLS 1.3 for all API communications; SFTP with AES-256 for batch transfers | EEG 2 — data in transit protection | Implemented |
| T1 | Technical | AES-256 encryption at rest with key management by Athena Global Logistics (keys held in Berlin) | EEG 2 — prevents plaintext access for government authorities accessing storage | Implementation in progress |
| C1 | Contractual | Obligation on importer to challenge any government access request that is disproportionate or exceeds lawful scope | EEG 2, EEG 4 | Included in SCC addendum |
| C2 | Contractual | Obligation on importer to notify exporter within 48 hours of receiving a government access request (where not legally prohibited) | EEG 1, EEG 4 | Included in SCC addendum |
| C3 | Contractual | Annual audit right exercisable by exporter or independent auditor | EEG 3 | Included in SCC Clause 8.9 |
| O1 | Organisational | Importer restricts access to transferred data to 12 named employees with role-based justification | EEG 2 | Implemented |
| O3 | Organisational | Importer maintains ISO 27001:2022 certification (certified data centre) | EEG 2, EEG 3 | Active — certificate valid to December 2026 |

## Step 5: Implementation Verification

| Measure | Verification Method | Verified Date | Verified By |
|---------|-------------------|---------------|-------------|
| TLS 1.3 encryption | Technical testing of API endpoints | 12 March 2025 | Thomas Richter, IT Security |
| AES-256 at rest with EU-held keys | Key management configuration review | 14 March 2025 | Thomas Richter, IT Security |
| Challenge obligation | Review of executed SCC addendum | 15 March 2025 | Elisa Brandt, DPO |
| Notification obligation | Review of executed SCC addendum | 15 March 2025 | Elisa Brandt, DPO |
| Audit rights | Review of SCC Clause 8.9 | 15 March 2025 | Elisa Brandt, DPO |
| Access restriction | Review of importer access control list | 14 March 2025 | Thomas Richter, IT Security |
| ISO 27001 certification | Certificate review | 10 March 2025 | Elisa Brandt, DPO |

## Step 6: Re-Evaluation Schedule

| Re-Evaluation Trigger | Next Scheduled Date |
|----------------------|-------------------|
| Annual periodic review | 10 March 2026 |
| New HKSAR legislation affecting data access | Continuous monitoring |
| EDPB updated guidance on Hong Kong | Continuous monitoring |
| Government access request received by importer | Ad hoc (within 7 days) |
| Material change in transfer scope | Ad hoc |

## Overall Conclusion

**Transfer may proceed with supplementary measures.**

The combination of technical measures (encryption in transit and at rest with EU-held keys), contractual measures (challenge and notification obligations), and organisational measures (access restriction and ISO 27001 certification) is assessed as sufficient to bridge the identified protection gaps in the Hong Kong SAR legal framework for the specific data categories and risk profile of this transfer.

## Sign-Off

| Role | Name | Date | Decision |
|------|------|------|----------|
| Head of Data Protection | Elisa Brandt | 15 March 2025 | Approved — transfer may proceed |
| External Privacy Counsel | Dr. Stefan Mueller | 15 March 2025 | Concur with assessment |
| IT Security Manager | Thomas Richter | 15 March 2025 | Technical measures verified |
