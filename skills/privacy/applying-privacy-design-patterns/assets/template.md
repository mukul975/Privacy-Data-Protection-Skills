# Privacy Design Pattern Assessment Template

## Processing Activity

| Item | Value |
|------|-------|
| Activity Name | Customer Behavior Analytics Pipeline |
| Organization | Prism Data Systems AG |
| Purpose | Analyze feature usage patterns for product improvement |
| Lawful Basis | Article 6(1)(f) legitimate interest |
| Assessment Date | 2026-03-14 |
| Assessor | Thomas Richter (Privacy Engineering Lead) |

## Pattern Assessment Matrix

| Pattern | Category | Score | Priority | Selected Sub-Patterns | Implementation Notes |
|---------|----------|-------|----------|----------------------|---------------------|
| MINIMIZE | Data-oriented | 22/25 | HIGH | Strip, Destroy | Pseudonymize at ingestion; TTL-based deletion after 13 months |
| HIDE | Data-oriented | 21/25 | HIGH | Encrypt, Dissociate, Obfuscate | Field-level encryption + HMAC pseudonymization + DP noise |
| ABSTRACT | Data-oriented | 18/25 | HIGH | Summarize, Group | Min group size 11; age brackets; region-level geography |
| ENFORCE | Process-oriented | 17/25 | MEDIUM | Uphold, Maintain | OPA purpose-based access control; CI/CD privacy gate |
| DEMONSTRATE | Process-oriented | 16/25 | MEDIUM | Record, Audit | Immutable audit trail; quarterly privacy review |
| INFORM | Process-oriented | 15/25 | MEDIUM | Supply | Privacy notice for analytics; opt-out mechanism |
| SEPARATE | Data-oriented | 14/25 | MEDIUM | Isolate | Analytics warehouse physically separated from transactional DB |
| CONTROL | Process-oriented | 12/25 | MEDIUM | Choose, Retract | Analytics opt-out in preference center |

## Selected Pattern Implementations

### MINIMIZE — Priority: HIGH

| Sub-Pattern | Implementation | Verification Criteria |
|------------|----------------|----------------------|
| Strip | HMAC-SHA256 pseudonymization applied at analytics ingestion boundary | No direct identifiers present in analytics warehouse |
| Destroy | TTL of 13 months on all analytics records; daily deletion job | Zero records older than 13 months in analytics store |

### HIDE — Priority: HIGH

| Sub-Pattern | Implementation | Verification Criteria |
|------------|----------------|----------------------|
| Encrypt | AES-256-GCM field-level encryption for quasi-identifiers at rest | Encryption verified via database column inspection |
| Dissociate | HMAC key in HSM, separated from analytics infrastructure | HSM access restricted to security operations team only |
| Obfuscate | Differential privacy (epsilon=0.3 per monthly query) on published statistics | Privacy budget tracked and enforced in privacy gateway |

### ABSTRACT — Priority: HIGH

| Sub-Pattern | Implementation | Verification Criteria |
|------------|----------------|----------------------|
| Summarize | Minimum group size of 11 enforced on all analytics outputs | Output validation rejects cells with fewer than 11 records |
| Group | Age stored as 5-year bracket; geography as canton-level | Schema check confirms no exact age or full postal code fields |

## Approval

| Role | Name | Decision | Date |
|------|------|----------|------|
| Privacy Engineering Lead | Thomas Richter | Recommended | 2026-03-14 |
| Data Protection Officer | Dr. Lukas Meier | Approved | 2026-03-14 |
