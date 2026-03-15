# HR System Privacy Configuration Audit Template

## System Details

| Field | Value |
|-------|-------|
| Organisation | [Atlas Manufacturing Group] |
| HR System | [ ] SAP SuccessFactors [ ] Workday [ ] BambooHR [ ] Other: _____ |
| Data Centre Location | _________ |
| Audit Date | [DD/MM/YYYY] |
| Auditor | [Name, Title] |

## Access Control Audit

### RBAC Matrix Verification

| Role | Personal Details | Salary | Performance | Absence | Health | Disciplinary |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| Employee Self | Own [Y/N] | Own [Y/N] | Own [Y/N] | Own [Y/N] | Own OH [Y/N] | Own [Y/N] |
| Line Manager | DR Limited [Y/N] | None [Y/N] | DR [Y/N] | DR Dates [Y/N] | None [Y/N] | None [Y/N] |
| HR BP | CG Full [Y/N] | CG Full [Y/N] | CG Full [Y/N] | CG Full [Y/N] | Fit/Unfit [Y/N] | CG Full [Y/N] |
| Payroll | Minimal [Y/N] | All [Y/N] | None [Y/N] | SSP [Y/N] | None [Y/N] | None [Y/N] |
| IT Admin | System [Y/N] | None [Y/N] | None [Y/N] | None [Y/N] | None [Y/N] | None [Y/N] |
| DPO | Audit [Y/N] | Audit [Y/N] | Audit [Y/N] | Audit [Y/N] | Audit [Y/N] | Audit [Y/N] |

### Violations Found

| Role | Data Category | Expected | Actual | Severity | Remediation |
|------|-------------|----------|--------|----------|-------------|
| _____ | _____ | _____ | _____ | _____ | _____ |

## Retention Automation Audit

| Data Category | Required Period | Configured? | Configured Period | Gap? |
|--------------|----------------|:-----------:|-------------------|:----:|
| Unsuccessful candidates | 6 months | [ ] Yes [ ] No | _________ | [ ] |
| Employment contract | 6 years post-term | [ ] Yes [ ] No | _________ | [ ] |
| Payroll/tax | 6-7 years | [ ] Yes [ ] No | _________ | [ ] |
| Performance reviews | 2 years post-term | [ ] Yes [ ] No | _________ | [ ] |
| Absence records | 2 yrs + 1 yr archive | [ ] Yes [ ] No | _________ | [ ] |
| Training records | 3 years post-term | [ ] Yes [ ] No | _________ | [ ] |

## Audit Logging

| Event Type | Logging Enabled? | Retention |
|-----------|:----------------:|-----------|
| Data access | [ ] Yes [ ] No | _________ |
| Data modification | [ ] Yes [ ] No | _________ |
| Data export | [ ] Yes [ ] No | _________ |
| Report generation | [ ] Yes [ ] No | _________ |
| Permission changes | [ ] Yes [ ] No | _________ |
| Deletion events | [ ] Yes [ ] No | _________ |

## DSAR Capability

| Test | Pass? |
|------|:-----:|
| Individual data export (all modules) | [ ] Yes [ ] No |
| DSAR workflow with deadline tracking | [ ] Yes [ ] No |
| Rectification capability | [ ] Yes [ ] No |
| Erasure with referential integrity | [ ] Yes [ ] No |

## Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Auditor | _________ | _________ | _________ |
| DPO | _________ | _________ | _________ |
