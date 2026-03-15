# Cloud Storage Retention Configuration Templates — Orion Data Vault Corp

## Cloud Resource Retention Configuration Record

| Field | Value |
|-------|-------|
| **Cloud Platform** | AWS S3 / Azure Blob / GCP GCS |
| **Resource Name** | |
| **Resource ID/ARN** | |
| **Region** | |
| **Data Categories Stored** | |
| **Retention Period** | |
| **Lifecycle Rule ID** | |
| **Object Lock / Immutability** | Governance / Compliance / None |
| **Legal Hold Active** | Yes / No |
| **Cross-Region Replication** | Yes / No — Destination: |
| **Encryption** | AES-256 / SSE-KMS / SSE-S3 |
| **Last Audit Date** | |
| **Compliant** | Yes / No |

## Monthly Cloud Retention Audit Checklist

- [ ] Policy drift detection: Compare active policies against approved schedule
- [ ] Coverage verification: All PI-containing resources have retention policies
- [ ] Legal hold inventory: Cross-reference with litigation hold register
- [ ] Expiration verification: Sample recently expired objects confirmed deleted
- [ ] Cross-region consistency: Replicated resources have identical configuration
- [ ] Encryption verification: All resources encrypted at rest
- [ ] Access logging: CloudTrail / Diagnostic Logs / Audit Logs active
- [ ] Alert configuration: Policy change alerts active and tested

## Alert Configuration Template

| Alert Name | Condition | Severity | Recipients |
|------------|-----------|----------|------------|
| Policy removed | Retention policy deleted from regulated resource | CRITICAL | Cloud Security, DPO |
| Object lock bypass | Governance mode bypass used | HIGH | DPO |
| Legal hold change | Hold applied or removed | MEDIUM | Legal, DPO |
| Retention unlock attempt | Attempt to modify locked policy | CRITICAL | Cloud Security |
| Replication lag | > 24h behind | HIGH | IT Operations |
