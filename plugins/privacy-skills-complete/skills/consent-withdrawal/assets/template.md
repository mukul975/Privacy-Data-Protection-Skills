# Consent Withdrawal Impact Assessment

## Assessment Information

| Field | Value |
|-------|-------|
| **Organization** | CloudVault SaaS Inc. |
| **Assessment Date** | 2026-03-14 |
| **Assessor** | Marta Kowalski, DPO |
| **Scope** | All consent-based processing purposes |

## Purpose-Level Withdrawal Impact Matrix

### Purpose 1: Service Improvement Analytics (pur_analytics_001)

| Impact Area | Description | Action Required | Timeline |
|------------|-------------|-----------------|----------|
| Analytics SDK | Stop collecting usage data for this user | Disable tracking for subject_id | Immediate |
| Analytics Cohorts | Remove user from all analytics cohorts | Purge from cohort membership tables | Within 1 hour |
| Historical Data | Flag existing analytics data for this user | Mark as "consent_withdrawn" in data warehouse | Within 24 hours |
| Downstream Reports | Exclude user from future aggregate reports | Update exclusion list in reporting pipeline | Within 24 hours |
| Recommendation Engine | Stop personalized storage recommendations | Disable recommendation feature for user | Immediate |

**Downstream Systems Notified:** analytics_sdk, analytics_data_warehouse
**Third Parties Affected:** None (internal only)
**Estimated Full Cessation:** 24 hours

---

### Purpose 2: Product Update Emails (pur_marketing_002)

| Impact Area | Description | Action Required | Timeline |
|------------|-------------|-----------------|----------|
| Email Marketing Lists | Remove user from all marketing segments | API call to email platform to remove subscriber | Within 1 hour |
| Suppression List | Prevent future marketing emails | Add email to global suppression list | Immediate |
| Scheduled Campaigns | Cancel pending campaign deliveries | Query and cancel all scheduled sends for user | Within 1 hour |
| Email Service Provider | Confirm processing cessation | Verify removal via ESP API audit | Within 4 hours |
| Re-Marketing | Stop retargeting via email-based custom audiences | Remove from custom audience uploads | Within 24 hours |

**Downstream Systems Notified:** email_marketing_platform, campaign_scheduler
**Third Parties Affected:** None (email platform is processor under DPA)
**Estimated Full Cessation:** 4 hours

---

### Purpose 3: Industry Benchmarking with Datalytics Partners Ltd. (pur_benchmarking_003)

| Impact Area | Description | Action Required | Timeline |
|------------|-------------|-----------------|----------|
| Data Export Pipeline | Stop exporting this user's data | Remove from export batch processing | Immediate |
| Staging Table | Flag pending data as withdrawn | Update export_staging SET status = 'withdrawn' | Within 1 hour |
| Datalytics Partners Ltd. | Notify to cease processing | POST to consent withdrawal API endpoint | Within 1 hour |
| Shared Data Deletion | Request deletion of previously shared data | Deletion request per DPA Section 8.3 | Within 24 hours |
| Confirmation | Verify Datalytics Partners Ltd. compliance | Query API for processing cessation confirmation | Within 48 hours |

**Downstream Systems Notified:** data_export_pipeline, datalytics_partners_api
**Third Parties Affected:** Datalytics Partners Ltd. (Amsterdam, Netherlands)
**DPA Section:** 8.3 — Consent withdrawal processing cessation within 24 hours
**Estimated Full Cessation:** 48 hours (including third-party confirmation)

## Equal Ease Compliance Summary

| Purpose | Give Consent (Clicks) | Withdraw (Best Path) | Compliant |
|---------|-----------------------|---------------------|-----------|
| Analytics | 1 (checkbox at signup) | 2 (preference center toggle + confirm) | Yes (confirmation dialog is acceptable per EDPB 05/2020 para 116) |
| Marketing Emails | 1 (checkbox at signup) | 1 (email unsubscribe link) | Yes |
| Benchmarking | 1 (checkbox at signup) | 2 (preference center toggle + confirm) | Yes |

## Escalation Matrix

| Time After Withdrawal | No Acknowledgment From | Action |
|----------------------|----------------------|--------|
| T+1 hour | Any internal system | Automated retry (3 attempts) |
| T+4 hours | Any internal system | Alert engineering on-call via PagerDuty |
| T+4 hours | Datalytics Partners Ltd. | Alert DPO and engineering |
| T+12 hours | Datalytics Partners Ltd. | DPO contacts Datalytics DPO directly |
| T+24 hours | Any system | DPO initiates formal incident report |
| T+48 hours | Datalytics Partners Ltd. | DPA breach process initiated per Section 12.1 |

## Sign-Off

| Role | Name | Date |
|------|------|------|
| DPO | Marta Kowalski | 2026-03-14 |
| Engineering Lead | James Park | 2026-03-14 |
| Legal Counsel | Elena Rodriguez | 2026-03-14 |
