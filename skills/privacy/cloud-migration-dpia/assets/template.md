# Cloud Migration DPIA Report

## Reference: DPIA-QLH-2026-0010

| Field | Value |
|-------|-------|
| Organisation | QuantumLeap Health Technologies |
| Cloud Service Provider | Amazon Web Services EMEA SARL |
| Service Model | PaaS (RDS PostgreSQL, ElastiCache, Lambda, S3) |
| Date | 2026-03-12 |
| DPO | Dr. Elena Vasquez, CIPP/E, CIPM |

---

## 1. Migration Scope

Migrating the central patient trial management database and HR system from on-premises Berlin data centre to AWS eu-west-1 (Ireland) and eu-central-1 (Frankfurt).

| Data Category | Volume | Sensitivity |
|--------------|--------|------------|
| Patient clinical trial identifiers (pseudonymised) | 28,000 records | Restricted |
| Employee HR records | 2,847 records | Confidential |
| Customer billing and contact information | 4,200 records | Confidential |
| Research collaboration metadata | 15,000 records | Internal |

Processing locations: Ireland (eu-west-1) primary, Germany (eu-central-1) failover. No non-EEA processing.

---

## 2. Art. 28 DPA Assessment

DPA executed: 2024-03-01 (AWS GDPR DPA v2.1, reference DPA-QLH-2024-0018).

| Element | Status | Notes |
|---------|--------|-------|
| Processing on documented instructions | Compliant | AWS processes data per customer configuration only |
| Confidentiality | Compliant | AWS staff background checks and confidentiality agreements |
| Security measures (Art. 32) | Compliant | SOC 2 Type II, ISO 27001, ISO 27018 certified |
| Sub-processor governance | Compliant | General authorisation with 30-day prior notice and objection right |
| Data subject rights assistance | Partial | AWS provides API tools but limited direct assistance; QuantumLeap must configure self-service |
| Breach notification, DPIA assistance | Compliant | AWS commits to notification within 72 hours; provides documentation for DPIA |
| Data return/deletion | Compliant | Customer-initiated deletion; cryptographic erasure confirmation |
| Audit rights | Partial | Third-party audit reports (SOC 2) accepted; on-site audit by arrangement only |

**Action**: Negotiate supplementary agreement for enhanced data subject rights assistance and annual on-site audit right.

---

## 3. Encryption Assessment

| Control | Implementation | Score |
|---------|---------------|-------|
| Encryption at rest | AES-256 via AWS KMS | Pass |
| Key management | Customer-managed key (CMK) via BYOK | Pass |
| Encryption in transit | TLS 1.3 enforced | Pass |
| Client-side encryption | Not implemented (processing requires server-side access) | N/A |
| **Overall score** | **70/100 — Adequate** | |

---

## 4. Conclusion

Migration approved subject to: (1) supplementary DPA agreement for audit and DSR assistance, (2) annual encryption posture review, (3) monitoring of AWS sub-processor changes.

| Role | Name | Date |
|------|------|------|
| DPO | Dr. Elena Vasquez | 2026-03-12 |
| CTO | Dr. Rajesh Krishnamurthy | 2026-03-13 |
| CISO | Dr. James Okonkwo | 2026-03-13 |
