# Breach Detection System — Coverage Assessment Template

## Assessment Metadata

| Field | Value |
|-------|-------|
| Organization | Stellar Payments Group GmbH |
| Assessment Date | 1 March 2026 |
| Assessor | Thomas Brenner, CISO |
| Reviewed By | Dr. Elena Vasquez, DPO |
| Next Review | 1 September 2026 |

## Personal Data System Inventory

| System | Data Sensitivity | Data Subjects | SIEM Coverage | DLP Coverage | UEBA Coverage | Overall Status |
|--------|-----------------|---------------|---------------|-------------|---------------|----------------|
| db-prod-eu-west (PostgreSQL cluster) | Critical | 15,230 customers | Full | N/A (server-side) | Full | Covered |
| crm-prod-01 (Salesforce) | High | 42,000 contacts | Full (API logs) | Email DLP active | Full | Covered |
| hr-workday (Workday SaaS) | High | 3,400 employees | Full (API logs) | Endpoint DLP active | Full | Covered |
| ms365-exchange (Email) | Medium | All employees + external | Full | Email DLP active | Partial | Covered |
| sharepoint-docs (SharePoint Online) | Medium | All employees | Full | Endpoint DLP active | Partial | Covered |
| analytics-dwh (Snowflake) | High | 15,230 customers (aggregated) | Full (query logs) | N/A | Partial | Gap: UEBA not yet integrated |
| legacy-archive (on-prem file server) | Medium | ~8,000 historical records | Partial (file access only) | Not deployed | None | Gap: incomplete coverage |
| mobile-app-backend (AWS ECS) | High | 9,200 app users | Full (CloudTrail + app logs) | N/A | None | Gap: UEBA not integrated |

## Detection Rule Coverage Matrix

| Detection Scenario | Rule Deployed | Systems Covered | Last Tested | False Positive Rate | Status |
|-------------------|--------------|-----------------|-------------|--------------------|---------|
| Mass data access (500+ records/30 min) | Yes | db-prod, crm-prod, hr-workday | 15 February 2026 | 8.2% | Active |
| Data exfiltration (50MB+ outbound) | Yes | All network-connected systems | 15 February 2026 | 12.1% | Active |
| Privileged account anomaly | Yes | db-prod, hr-workday | 20 February 2026 | 6.4% | Active |
| Ransomware behavior pattern | Yes | All endpoints + servers | 1 March 2026 | 3.1% | Active |
| Authentication brute force | Yes | All authentication systems | 15 February 2026 | 14.8% | Active — tuning needed |
| After-hours personal data access | Yes | db-prod, crm-prod, hr-workday | 20 February 2026 | 18.3% | Active — tuning needed |
| Geo-anomaly (new country login) | Yes | Okta, AWS Console | 1 March 2026 | 5.7% | Active |
| DNS tunneling detection | Yes | All DNS-resolving systems | 15 February 2026 | 2.3% | Active |

## DLP Policy Status

| Policy | Scope | Mode | Matches (Last 30 Days) | True Positives | Action |
|--------|-------|------|----------------------|----------------|--------|
| PII Outbound (Email) | All outbound email | Enforce (block + encrypt) | 47 | 39 (83%) | Block + alert DPO |
| Bulk PII (Email) | All outbound email | Enforce (block) | 12 | 11 (92%) | Block + alert SOC |
| Special Category (Email) | All outbound email | Enforce (block) | 3 | 3 (100%) | Block + alert DPO |
| USB Copy PII | All managed endpoints | Enforce (block) | 28 | 22 (79%) | Block + exception workflow |
| Cloud Upload PII | All managed endpoints | Enforce (block) | 34 | 27 (79%) | Block + alert SOC |

## Gap Analysis and Remediation Plan

| Gap | Risk Level | Remediation | Owner | Target Date |
|-----|-----------|-------------|-------|-------------|
| Legacy archive file server — incomplete SIEM coverage | Medium | Deploy Splunk Universal Forwarder, configure file access auditing | SOC Lead | 31 March 2026 |
| Snowflake analytics DWH — no UEBA integration | High | Integrate Snowflake query logs into UEBA platform for behavioral baselining | SOC Lead | 30 April 2026 |
| Mobile app backend — no UEBA integration | High | Extend UEBA coverage to AWS ECS application logs | SOC Lead | 30 April 2026 |
| Authentication brute force rule — 14.8% FP rate | Low | Tune threshold from 50 to 75 failed attempts; add approved scanner whitelist | SOC Analyst | 15 March 2026 |
| After-hours access rule — 18.3% FP rate | Low | Integrate Workday shift schedules to baseline per-user working hours | SOC Analyst | 31 March 2026 |

## Detection Metrics (Last Quarter)

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Mean Time to Detect (MTTD) | 23 minutes | Under 30 minutes | On target |
| Mean Time to Escalate to DPO | 2.1 hours | Under 4 hours | On target |
| Total alerts generated | 4,218 | N/A | N/A |
| True positive rate (average) | 82.4% | Over 85% | Improvement needed |
| Personal data systems with full SIEM coverage | 75% (6/8) | 100% | Gap — 2 systems pending |
| Tabletop exercise detection rate | 4/5 scenarios detected | 5/5 | 1 scenario missed (DNS exfiltration via IPv6) |
