# Breach Investigation Report Template

## Document Control

| Field | Value |
|-------|-------|
| Report Reference | SPG-BREACH-2026-003-IR |
| Classification | CONFIDENTIAL — Attorney Work Product Where Applicable |
| Version | 1.0 — Final |
| Date | 28 March 2026 |
| Prepared By | Mandiant Incident Response (Sarah Mitchell, Lead Analyst) |
| Reviewed By | Thomas Brenner, CISO, Stellar Payments Group |
| Approved By | Dr. Elena Vasquez, DPO, Stellar Payments Group |

## Section 1: Executive Summary

On 13 March 2026, Stellar Payments Group detected a ransomware attack (LockBit 3.0) that encrypted the production customer database cluster serving 15,230 account holders. The attack was initiated via a spear-phishing email targeting an IT operations engineer on 10 March 2026. The attacker harvested credentials, bypassed multi-factor authentication through push fatigue, and pivoted through a database administration jump server to deploy ransomware. The attacker exploited a stale service account (svc-migration-2024) with database administrator privileges that was created for a 2024 data migration project and never decommissioned.

Affected personal data includes: full names, postal addresses, email addresses, payment card last-4-digits, transaction histories, and account balances for 15,230 data subjects. Data was restored from clean backups within 36 hours. Forensic analysis could not confirm or rule out data exfiltration prior to encryption. The root cause is a combination of inadequate service account lifecycle management and exclusion of service accounts from the quarterly access review scope.

## Section 2: Investigation Scope and Methodology

### Objectives
1. Determine the complete attack timeline from initial access to ransomware deployment.
2. Identify all compromised systems and affected personal data.
3. Determine whether data exfiltration occurred.
4. Identify the root cause and contributing factors.
5. Provide remediation recommendations.

### Evidence Analyzed

| Evidence ID | Type | Description | Hash Verified |
|-------------|------|-------------|--------------|
| EV-001 | Memory dump | RAM capture of db-prod-eu-west-01 (128 GB) | Yes (SHA-256) |
| EV-002 | Disk image | Full disk image of db-prod-eu-west-01 (2 TB) | Yes (SHA-256) |
| EV-003 | Log export | Splunk export: auth + DB audit, 10 Feb - 14 Mar 2026 | Yes (SHA-256) |
| EV-004 | Network capture | PCAP from db-prod VLAN, 12-14 Mar 2026 | Yes (SHA-256) |
| EV-005 | Cloud log | AWS CloudTrail for eu-west-1, 1 Feb - 14 Mar 2026 | Yes (SHA-256) |
| EV-006 | Malware sample | LockBit 3.0 binary extracted from EV-001 | Yes (SHA-256) |
| EV-007 | Log export | Okta system log, 1 Feb - 14 Mar 2026 | Yes (SHA-256) |
| EV-008 | Disk image | Full disk image of ws-jrichter-01 workstation | Yes (SHA-256) |

### Tools Used
- Splunk Enterprise Security 7.3 — Log correlation and search
- Volatility 3.0 — Memory forensics
- FTK Imager 4.7 — Disk image acquisition
- Wireshark 4.2 — Network traffic analysis
- YARA 4.5 — Malware signature scanning
- Plaso/log2timeline — Super-timeline creation
- Autopsy 4.21 — Disk forensics
- Chainsaw 2.9 — Windows event log analysis

## Section 3: Findings

### 3.1 Attack Timeline

| Timestamp (UTC) | Event | MITRE ATT&CK | Evidence |
|-----------------|-------|---------------|----------|
| 10 Mar 09:23 | Phishing email received | T1566.002 | EV-007 |
| 10 Mar 09:24 | Credentials harvested + keylogger installed | T1056.001 | EV-008 |
| 10 Mar 14:07 | Attacker authenticates via Okta (Tor exit node) | T1078.002 | EV-007 |
| 10 Mar 14:07 | MFA bypassed via push fatigue | T1078.002 | EV-007 |
| 11 Mar 02:15 | SSH to db-admin-jumpbox | T1021.004 | EV-003 |
| 11 Mar 02:18 | Pivot to db-prod-eu-west-01 via svc-migration-2024 | T1078 | EV-003 |
| 11 Mar 02:30 - 13 Mar 10:45 | Reconnaissance: database schema queries, table row counts | N/A | EV-003 |
| 13 Mar 11:15 | Ransomware deployment (LockBit 3.0) | T1486 | EV-001, EV-006 |
| 13 Mar 12:45 | Network isolation by SOC team | N/A (containment) | EV-003 |
| 13 Mar 14:30 | Breach awareness — 72-hour clock started | N/A | EV-003 |

### 3.2 Exfiltration Determination

**Status: Cannot be ruled out.**

- Between 11 March 02:30 and 13 March 10:45, the attacker executed 47 SELECT queries against customer-facing database tables, retrieving schema information and row counts.
- Network capture (EV-004) covers only 12-14 March. No network capture exists for 10-11 March when initial compromise occurred.
- During the 12-14 March capture window, no outbound data transfers exceeding normal baselines were detected from the db-prod VLAN.
- However, the 48-hour gap in network capture (10-12 March) means exfiltration during the initial compromise period cannot be confirmed or denied.
- The LockBit 3.0 variant used in this attack (SHA-256: 8a3b...ef91) is associated with the LockBit affiliate program, which frequently practices double extortion (encryption + data theft). The absence of a ransom note mentioning stolen data is not conclusive.

### 3.3 Root Cause

**Primary root cause**: Stale privileged service account (svc-migration-2024) with database administrator privileges was not decommissioned after the 2024 migration project was completed.

**Contributing factors:**
1. Service accounts were excluded from the quarterly access certification review scope.
2. Multi-factor authentication was configured with push notifications allowing push fatigue attacks; no phishing-resistant MFA (FIDO2/WebAuthn) was enforced.
3. Network segmentation did not prevent direct SSH from the VPN to the database administration jump server.
4. No anomaly detection rule for service account usage outside of scheduled batch windows.

## Section 4: Impact Assessment

| Metric | Value |
|--------|-------|
| Data subjects affected | 15,230 |
| Personal data records affected | 48,720 |
| Breach type | Availability (primary) + Confidentiality (potential) |
| Dwell time | 71 hours (10 Mar 09:24 to 13 Mar 08:15 detection) |
| Data recovery | Full — restored from clean backup (12 Mar 23:00 UTC) |
| Financial cost (estimated) | EUR 2.8 million (forensics, credit monitoring, operational disruption, legal) |

## Section 5: Remediation Recommendations

| Priority | Recommendation | Target |
|----------|---------------|--------|
| Immediate | Decommission all stale service accounts (audit identified 14 additional candidates) | Completed 14 Mar 2026 |
| 30 days | Include service accounts in quarterly access certification scope | 15 Apr 2026 |
| 30 days | Deploy phishing-resistant MFA (FIDO2/WebAuthn) for all privileged access | 15 Apr 2026 |
| 60 days | Implement network segmentation: database tier accessible only via approved bastion host with session recording | 15 May 2026 |
| 60 days | Deploy SIEM correlation rule for service account usage outside batch windows | 15 May 2026 |
| 90 days | Implement service account lifecycle management with automated expiry | 15 Jun 2026 |
| 90 days | Deploy organization-wide phishing simulation and awareness training | 15 Jun 2026 |

## Section 6: Evidence Inventory

All evidence items are stored in the forensic evidence vault, Building A, Room 104, Safes 3-4. Access is restricted to authorized investigation team members and requires two-person access protocol. Evidence retention follows the schedule defined in the Stellar Payments Group Forensic Evidence Retention Policy (SPG-POL-SEC-014). Chain of custody records are maintained in the evidence management system.
