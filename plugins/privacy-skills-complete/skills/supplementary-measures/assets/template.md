# Supplementary Measures — Implementation Plan Template

## Transfer Identification

| Field | Value |
|-------|-------|
| TIA Reference | TIA-2025-HK-001 |
| Transfer Reference | SCC-2025-APAC-001 |
| Data Exporter | Athena Global Logistics GmbH |
| Data Importer | TransPacific Freight Solutions Ltd |
| Destination Country | Hong Kong SAR |
| Transfer Mechanism | SCCs Module 2 (Commission Decision 2021/914) |
| TIA Conclusion | Amber — supplementary measures required |

## Identified Protection Gaps

| Gap ID | EEG Category | Description | Severity |
|--------|-------------|-------------|----------|
| GAP-001 | EEG 2 | NSL proportionality review is insufficient; broad access powers without clear proportionality requirement | Major |
| GAP-002 | EEG 3 | Oversight body (Commissioner) appointed by Chief Executive; independence from executive not fully established | Major |
| GAP-003 | EEG 4 | No notification mechanism for data subjects subject to surveillance under Cap. 589 or NSL | Major |
| GAP-004 | EEG 2 | No explicit data minimisation or retention limits for data accessed under NSL | Minor |

## Selected Supplementary Measures

### Technical Measures

| Measure ID | Name | Gap Addressed | Specification | Implementation Owner | Target Date | Status |
|-----------|------|---------------|--------------|---------------------|-------------|--------|
| T4 | Transport-layer encryption | GAP-001, GAP-004 | TLS 1.3 with mTLS for all API endpoints; SFTP AES-256 for batch | Thomas Richter, IT Security | 1 March 2025 | Implemented |
| T1 | Encryption at rest with EU-held keys | GAP-001 | AES-256-GCM; CMK in AWS KMS eu-central-1; importer stores ciphertext for archived shipments | Thomas Richter, IT Security | 15 March 2025 | Implemented |
| T2 | Pseudonymisation of customer identifiers | GAP-001, GAP-002 | HMAC-SHA256; mapping table in Frankfurt PostgreSQL; pseudonymised fields: customer name, email, phone, customs ID | Data Engineering Team | 30 March 2025 | In Progress |

### Contractual Measures

| Measure ID | Name | Gap Addressed | Contract Reference | Execution Date | Status |
|-----------|------|---------------|-------------------|---------------|--------|
| C1 | Challenge obligation | GAP-001, GAP-003 | SCC Supplementary Addendum Clause 3.1 | 15 March 2025 | Implemented |
| C2 | Transparency obligation | GAP-003 | SCC Supplementary Addendum Clause 3.2 | 15 March 2025 | Implemented |
| C3 | Audit rights | GAP-002 | SCC Clause 8.9 + Addendum Clause 3.3 | 15 March 2025 | Implemented |
| C4 | Warrant canary | GAP-003 | SCC Supplementary Addendum Clause 3.4 | 15 March 2025 | Implemented |

### Organisational Measures

| Measure ID | Name | Gap Addressed | Description | Implementation Date | Status |
|-----------|------|---------------|-------------|-------------------|--------|
| O1 | Access policies | GAP-001, GAP-004 | 12 named personnel; quarterly reviews; 24h revocation | 10 March 2025 | Implemented |
| O2 | Transparency reports | GAP-003 | Annual report on government requests; published Q1 | Q1 2026 (first report) | Planned |
| O3 | ISO 27001 certification | GAP-002 | Importer certified; valid to Dec 2026; TUV Rheinland surveillance audits | Active | Verified |

## Combined Effectiveness Assessment

| Criterion | Assessment |
|-----------|-----------|
| Total measures selected | 10 (3 technical + 4 contractual + 3 organisational) |
| Prevents compelled plaintext disclosure | Yes — T1 encryption at rest with EU-held keys for archived data |
| Prevents bulk surveillance of transit data | Yes — T4 TLS 1.3 + mTLS |
| Provides visibility into government access | Yes — C2 transparency + C4 warrant canary |
| Enables independent verification | Yes — C3 audit rights + O3 ISO certification |
| Overall effectiveness verdict | EFFECTIVE — combination bridges identified gaps for freight logistics data with low-medium sensitivity |

## Verification Schedule

| Verification Activity | Frequency | Next Due | Responsible |
|----------------------|-----------|----------|-------------|
| Encryption configuration scan (TLS + at-rest) | Quarterly | June 2025 | IT Security |
| Pseudonymisation sample verification | Quarterly | June 2025 | Data Engineering |
| Access control list review | Quarterly | June 2025 | IT Security |
| Warrant canary publication check | Monthly | April 2025 | DPO Office |
| Audit of importer compliance | Annual | March 2026 | External Auditor |
| ISO certification status check | Annual | December 2025 | DPO Office |
| Full supplementary measures reassessment | Annual | March 2026 | DPO |

## Sign-Off

| Role | Name | Date | Approval |
|------|------|------|----------|
| Head of Data Protection | Elisa Brandt | 15 March 2025 | Approved |
| IT Security Manager | Thomas Richter | 15 March 2025 | Technical measures verified |
| Legal Counsel | Dr. Stefan Mueller | 15 March 2025 | Contractual measures reviewed |
