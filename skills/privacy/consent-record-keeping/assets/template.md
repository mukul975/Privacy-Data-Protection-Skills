# Consent Record Audit Report

## Audit Information

| Field | Value |
|-------|-------|
| **Organization** | CloudVault SaaS Inc. |
| **Audit Period** | 2026-Q1 (January 1 — March 31, 2026) |
| **Audit Date** | 2026-03-14 |
| **Auditor** | Marta Kowalski, Data Protection Officer |
| **Standard** | GDPR Article 7(1), EDPB Guidelines 05/2020 |

## Record Volume Summary

| Metric | Count |
|--------|-------|
| Total consent decisions recorded | 847,293 |
| Unique data subjects | 312,450 |
| Consent grants | 623,118 |
| Consent withdrawals | 84,729 |
| Not-granted (declined at sign-up) | 139,446 |
| Consent text versions active | 9 |
| Consent text versions retired | 4 |

## Field Completeness Analysis

| Field | Populated | Total | Rate | Severity if Missing |
|-------|-----------|-------|------|-------------------|
| consent_id | 847,293 | 847,293 | 100.0% | CRITICAL |
| subject_id | 847,293 | 847,293 | 100.0% | CRITICAL |
| purpose_id | 847,293 | 847,293 | 100.0% | CRITICAL |
| purpose_description | 847,293 | 847,293 | 100.0% | HIGH |
| decision | 847,293 | 847,293 | 100.0% | CRITICAL |
| mechanism | 847,293 | 847,293 | 100.0% | HIGH |
| consent_text_version | 847,293 | 847,293 | 100.0% | CRITICAL |
| timestamp | 847,293 | 847,293 | 100.0% | CRITICAL |
| source | 847,293 | 847,293 | 100.0% | MEDIUM |
| ip_address | 845,881 | 847,293 | 99.8% | LOW |
| user_agent | 843,102 | 847,293 | 99.5% | LOW |
| session_id | 841,566 | 847,293 | 99.3% | LOW |
| record_hash | 847,293 | 847,293 | 100.0% | CRITICAL |
| previous_hash | 847,293 | 847,293 | 100.0% | HIGH |

**Overall Mandatory Field Completeness: 100.0%**

## Chain Integrity Verification

| Metric | Value |
|--------|-------|
| Subjects verified | 312,450 (100%) |
| Chains intact | 312,447 |
| Chains broken | 3 |
| Chain break locations | Records created during database migration on 2026-02-08 |

### Chain Break Details

Three data subjects have chain integrity breaks traced to a database migration performed on February 8, 2026. The migration correctly preserved all record data but recomputed hashes without including the previous_hash chain link. These records have been flagged and a supplementary integrity attestation has been added to the audit trail.

**Remediation:** Engineering team deployed a fix on February 10, 2026. All records created after that date have correct chain linking. The three affected subjects' records have been annotated with migration_chain_break_20260208 flags.

## Version Consistency

| Check | Result |
|-------|--------|
| All consent_text_version hashes map to existing versions | PASS |
| All version references were effective at the record timestamp | PASS |
| No orphaned version references | PASS |
| Current production consent text matches latest version hash | PASS |

## Consent Receipt Generation

| Metric | Value |
|--------|-------|
| Receipts generated on demand (Q1) | 1,247 |
| Receipt format | Kantara CR v1.1.0 JSON |
| Average generation time | 45ms |
| Failed receipt requests | 0 |

## Sign-Off

| Role | Name | Date |
|------|------|------|
| DPO | Marta Kowalski | 2026-03-14 |
| Database Administrator | Tomasz Nowak | 2026-03-14 |
| Engineering Lead | James Park | 2026-03-14 |
