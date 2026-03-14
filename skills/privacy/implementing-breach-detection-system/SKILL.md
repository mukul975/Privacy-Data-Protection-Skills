---
name: implementing-breach-detection-system
description: >-
  Implements technical breach detection capabilities including SIEM integration,
  DLP alert configuration, anomaly detection rules, and insider threat monitoring.
  Provides a breach classification taxonomy across confidentiality, integrity,
  and availability dimensions. Covers detection tool selection, alert tuning,
  and integration with privacy incident response workflows. Keywords: breach
  detection, SIEM, DLP, anomaly detection, insider threat, classification.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-breach-response
  tags: "breach-detection, siem, dlp, anomaly-detection, insider-threat, classification"
---

# Implementing Breach Detection System

## Overview

Effective breach detection is the prerequisite for timely Art. 33 notification. The GDPR does not prescribe specific detection technologies, but Art. 32 requires appropriate technical and organisational measures, and Art. 33(1) creates a de facto obligation to detect breaches promptly — a controller cannot notify within 72 hours if it takes months to discover a breach. This skill covers the technical architecture for personal data breach detection, including SIEM integration, DLP alerting, behavioral analytics, and insider threat monitoring.

## Breach Classification Taxonomy

### Level 1: CIA Triad Classification

| Type | Definition | Detection Method |
|------|-----------|-----------------|
| Confidentiality | Unauthorized disclosure or access to personal data | DLP alerts, access log anomalies, data exfiltration detection |
| Integrity | Unauthorized modification of personal data | File integrity monitoring, database audit logs, checksum validation |
| Availability | Loss of access to or destruction of personal data | System health monitoring, backup verification, ransomware detection |

### Level 2: Attack Vector Classification

| Vector | Description | Primary Detection |
|--------|-------------|------------------|
| External attack | Unauthorized access from outside the network perimeter | IDS/IPS, firewall logs, authentication failures |
| Insider threat | Authorized user acting beyond their authorized scope | UEBA, DLP, access pattern analysis |
| Third-party compromise | Breach originating from a processor or vendor | Vendor monitoring, API anomaly detection |
| Accidental disclosure | Human error leading to data exposure | DLP content inspection, email gateway filters |
| System failure | Technical failure causing data loss or corruption | Infrastructure monitoring, backup validation |
| Physical breach | Loss or theft of physical devices containing data | Asset tracking, device encryption verification |

### Level 3: Data Sensitivity Classification

| Level | Data Types | Detection Priority |
|-------|-----------|-------------------|
| Critical | Art. 9 special categories, Art. 10 criminal data, financial credentials | Real-time alerting, immediate escalation |
| High | Government identifiers, financial account data, authentication credentials | Real-time alerting, 15-minute escalation |
| Medium | Contact details, employment records, purchase history | Near-real-time (5-minute batching), 1-hour escalation |
| Low | Publicly available business contact data, non-personal metadata | Batch processing (hourly), daily review |

## SIEM Integration Architecture

### Event Source Configuration

Stellar Payments Group deploys Splunk Enterprise Security as the primary SIEM platform. The following log sources are ingested for breach detection:

| Source | Log Type | Ingestion Method | Events/Day |
|--------|----------|-----------------|-----------|
| Active Directory | Authentication, authorization, group changes | Splunk Universal Forwarder | 2.4M |
| AWS CloudTrail | API calls, console logins, resource changes | S3-to-Splunk via SQS | 8.7M |
| PostgreSQL audit | Query logs, schema changes, failed authentications | syslog-ng to Splunk HEC | 14.2M |
| Palo Alto PA-5260 | Firewall sessions, URL filtering, threat prevention | syslog to Splunk | 45.3M |
| CrowdStrike Falcon | Endpoint detections, process execution, file writes | Falcon SIEM Connector | 6.1M |
| Microsoft 365 | Email audit, SharePoint access, Teams DLP | Microsoft Graph API via Splunk Add-on | 3.8M |
| Okta | SSO authentications, MFA events, admin changes | Okta Event Hook to Splunk HEC | 890K |
| AWS GuardDuty | Threat intelligence findings, anomaly detections | CloudWatch to Splunk | 12K |

### Correlation Rules for Breach Detection

#### Rule 1: Mass Data Access Anomaly
```
Trigger: Single user account accesses more than 500 unique personal data records within a 30-minute window.
Data sources: PostgreSQL audit logs, application access logs.
Severity: High
Action: Create incident ticket, alert SOC analyst, notify DPO on-call.
False positive mitigation: Whitelist batch processing service accounts (reviewed quarterly). Flag whitelisted accounts if access occurs outside scheduled batch windows.
```

#### Rule 2: Data Exfiltration Indicator
```
Trigger: Outbound data transfer exceeding 50MB to an unclassified external destination from a system containing personal data.
Data sources: Palo Alto firewall, CrowdStrike network telemetry, DLP alerts.
Severity: Critical
Action: Automated network isolation of source endpoint, SOC analyst investigation, DPO notification.
False positive mitigation: Baseline normal data transfer patterns per endpoint. Whitelist approved SaaS destinations (Salesforce, Workday, etc.).
```

#### Rule 3: Privileged Account Anomaly
```
Trigger: Database administrator account performs SELECT queries on personal data tables outside of change management windows OR from an unrecognized source IP.
Data sources: PostgreSQL audit logs, Okta authentication logs, IP geolocation.
Severity: High
Action: Alert SOC lead and database security team. Log full query text for forensic review.
```

#### Rule 4: Ransomware Behavior Pattern
```
Trigger: More than 20 file rename/encrypt operations per second on file servers or database storage volumes, OR known ransomware file extension creation (.lockbit, .encrypted, .crypt).
Data sources: CrowdStrike Falcon, Windows file audit logs, storage IOPS monitoring.
Severity: Critical
Action: Automated isolation of affected system, activate incident response team, preserve forensic image.
```

#### Rule 5: Authentication Brute Force
```
Trigger: More than 50 failed authentication attempts against personal data systems within 10 minutes from a single source, OR more than 200 failed attempts across multiple accounts from the same source within 30 minutes (password spray).
Data sources: Active Directory, Okta, application authentication logs.
Severity: Medium (escalates to High if followed by successful authentication).
Action: Block source IP at firewall, SOC investigation, check for compromised credentials.
```

## DLP Alert Configuration

### Email DLP Policies

| Policy Name | Detection Content | Action | Severity |
|-------------|------------------|--------|----------|
| PII Outbound | Regex: German ID (Personalausweisnummer), IBAN, credit card numbers, health insurance numbers | Block + encrypt + alert DPO | High |
| Bulk PII | More than 10 rows of structured personal data (name + email/phone/address) in email body or attachment | Block + alert sender manager + SOC | Critical |
| Special Category | Keywords/patterns matching health diagnoses, genetic markers, biometric templates, trade union references | Block + alert DPO | Critical |
| Cross-Border Transfer | Personal data sent to recipients in non-adequate countries without approved transfer mechanism | Hold for review + alert privacy team | Medium |

### Endpoint DLP Policies

| Policy Name | Detection Content | Action |
|-------------|------------------|--------|
| USB Copy PII | Copy of files containing personal data to removable media | Block (exceptions via DPO-approved ticket) |
| Cloud Upload PII | Upload of personal data files to non-approved cloud services | Block + alert SOC |
| Print PII Bulk | Print job containing more than 50 records of personal data | Alert line manager + SOC |
| Screenshot PII | Screen capture of application displaying personal data records | Log + alert SOC (for pattern analysis) |

## Anomaly Detection and UEBA

### Behavioral Baselines

User and Entity Behavior Analytics (UEBA) establishes normal patterns for each user and system account:

| Baseline Metric | Normal Range | Anomaly Threshold | Detection Window |
|----------------|-------------|-------------------|-----------------|
| Daily record access count | Per-user historical average | 3x standard deviation above mean | Rolling 30-day baseline |
| Access time patterns | Historical working hours | Access outside 95th percentile time range | Rolling 90-day baseline |
| Data download volume | Per-user historical average | 2x standard deviation above mean for 2+ consecutive hours | Rolling 14-day baseline |
| Geographic access location | Historical IP geolocation | New country not seen in 90-day history | Rolling 90-day baseline |
| Application access pattern | Historical application mix | Access to new personal data application not in 60-day history | Rolling 60-day baseline |

### Insider Threat Indicators

Composite risk scoring for insider threat detection combines multiple low-severity indicators:

| Indicator | Weight | Source |
|-----------|--------|--------|
| Access outside normal hours to personal data systems | 15 | Okta + application logs |
| Bulk data download from HR or customer databases | 25 | DLP + database audit |
| Use of personal email or cloud storage from corporate device | 10 | CrowdStrike + proxy logs |
| Notice period or performance improvement plan status | 20 | HR system integration (Workday) |
| Access to data outside role scope | 20 | Role-based access comparison |
| Disabling or circumventing security controls | 30 | Endpoint agent tampering alerts |
| Repeated failed access to restricted personal data | 10 | Application access logs |

Composite scores above 60 trigger enhanced monitoring. Scores above 80 trigger SOC analyst investigation and DPO notification.

## Integration with Privacy Incident Response

### Automated Workflow

1. SIEM correlation rule or DLP policy triggers an alert.
2. Alert is enriched with contextual data: user identity, data classification of affected system, data subject count estimate.
3. If the affected system is classified as containing personal data (tagged in the CMDB), the alert is automatically duplicated to the privacy incident queue in ServiceNow.
4. Privacy incident coordinator performs initial triage within 30 minutes.
5. If personal data breach is confirmed, the Art. 33 72-hour clock activation is triggered and the DPO is notified.

### Detection-to-Notification Timeline Target

| Phase | Target | Owner |
|-------|--------|-------|
| Detection to alert | Under 5 minutes | SIEM platform (automated) |
| Alert to triage | Under 30 minutes | SOC analyst |
| Triage to breach confirmation | Under 4 hours | SOC lead + privacy coordinator |
| Breach confirmation to DPO notification | Under 1 hour | Privacy incident coordinator |
| DPO notification to 72-hour clock start | Immediate | DPO |

## Monitoring and Tuning

### Monthly Review Cadence

1. Review false positive rates for all breach detection correlation rules. Target: under 15% false positive rate.
2. Analyze detection gap assessments against known breach scenarios from EDPB Guidelines 01/2021.
3. Update behavioral baselines following organizational changes (new hires, departures, role changes).
4. Validate that all new personal data systems have been onboarded to the SIEM and DLP platforms.
5. Test end-to-end detection-to-notification workflow with a simulated breach scenario quarterly.
