---
name: breach-forensics
description: >-
  Conducts digital forensics investigations following a personal data breach,
  covering evidence preservation, chain of custody documentation, log analysis,
  scope determination, and root cause analysis. References industry-standard
  tools including Splunk, ELK Stack, and Wireshark. Provides forensic workflow
  from initial evidence collection through final investigation report. Keywords:
  digital forensics, breach investigation, evidence preservation, chain of
  custody, root cause analysis, Splunk, ELK, Wireshark.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-breach-response
  tags: "digital-forensics, breach-investigation, evidence-preservation, chain-of-custody, root-cause"
---

# Conducting Breach Investigation Forensics

## Overview

When a personal data breach is confirmed, a thorough forensic investigation is essential to determine the breach scope (which personal data and data subjects were affected), the attack vector, the timeline of unauthorized activity, and the root cause. The investigation findings directly feed into the Art. 33 supervisory authority notification, the Art. 34 data subject communication, and the post-breach remediation plan. This skill provides the complete forensic investigation workflow, evidence handling procedures, and analysis techniques.

## Evidence Preservation Protocol

### Golden Rule: Preserve First, Analyze Second

The first priority upon breach confirmation is to preserve volatile evidence before it is overwritten or destroyed. Evidence must be collected in order of volatility:

1. **CPU registers and cache** — captured via live memory acquisition tools (Volatility, WinPmem, LiME).
2. **Memory (RAM) contents** — full memory dump of affected systems. Contains running processes, network connections, encryption keys, and malware artifacts that may not exist on disk.
3. **Network connections and routing tables** — current active connections may reveal command-and-control (C2) infrastructure or ongoing data exfiltration.
4. **Running processes and services** — process trees, loaded DLLs, open file handles, and user context.
5. **Disk contents** — forensic disk images (bit-for-bit copies) of affected system storage. Use write blockers for physical media.
6. **Log files** — system logs, application logs, security logs, database audit logs. Prioritize logs that may be subject to rotation or overwrite.
7. **Network traffic captures** — packet captures (PCAP) from network taps, SPAN ports, or inline capture points.
8. **External evidence** — cloud service logs (AWS CloudTrail, Azure Activity Log), SaaS audit logs, third-party vendor logs.

### Forensic Image Acquisition

| System Type | Tool | Method | Hash Verification |
|-------------|------|--------|------------------|
| Windows server | FTK Imager 4.7 | Bit-for-bit disk image to external write-blocked storage | SHA-256 + MD5 dual hash |
| Linux server | dc3dd | Bit-for-bit using /dev/sda source to external storage | SHA-256 hash with dcfldd verification |
| AWS EC2 instance | AWS CLI + EBS snapshot | Create EBS snapshot, then convert to forensic image | SHA-256 of snapshot export |
| Database | pg_dump (logical) + disk image | Logical export for data analysis + physical disk image for artifact recovery | SHA-256 of both outputs |
| Mobile device | Cellebrite UFED / GrayKey | Physical extraction where legally permitted | SHA-256 of extraction package |
| Cloud storage (S3) | AWS CLI sync with versioning | Download all object versions including deleted objects | SHA-256 of manifest |

## Chain of Custody Documentation

Every piece of evidence must be tracked from acquisition through analysis to storage using a formal chain of custody record:

### Evidence Tracking Fields

| Field | Description |
|-------|-------------|
| Evidence ID | Unique identifier: SPG-BREACH-2026-003-EV-001 |
| Description | Full RAM dump of db-prod-eu-west-01 (PostgreSQL primary) |
| Date/time acquired | 13 March 2026, 15:47 UTC |
| Acquired by | Thomas Brenner, CISO, Stellar Payments Group |
| Acquisition tool | WinPmem 4.0 — Memory acquisition |
| Hash at acquisition | SHA-256: a3f8b2c1d9e... (full hash recorded in evidence log) |
| Storage location | Forensic evidence vault, Building A, Room 104, Safe #3, Shelf B |
| Access log | All access to evidence is logged with name, date, time, and purpose |

### Chain of Custody Transfer Record

| Transfer # | Date/Time | Released By | Received By | Purpose | Hash Verified |
|-----------|-----------|-------------|-------------|---------|--------------|
| 1 | 13 March 2026, 16:00 UTC | Thomas Brenner (CISO) | Mandiant IR Analyst (Sarah Mitchell) | Forensic analysis | Yes — SHA-256 match |
| 2 | 20 March 2026, 10:00 UTC | Sarah Mitchell (Mandiant) | Thomas Brenner (CISO) | Return after analysis | Yes — SHA-256 match |

## Log Analysis Methodology

### Tool Selection and Application

#### Splunk Enterprise Security
- **Use case**: Centralized log correlation, timeline reconstruction, behavioral analysis.
- **Key searches for breach investigation**:
  - Authentication events: `index=auth sourcetype=okta:log action=authentication.login | stats count by user, result, client.ipAddress, client.geographicalContext.country`
  - Database queries: `index=database sourcetype=postgresql:audit query_type=SELECT table IN (customers, transactions, accounts) | stats count, values(query_text) by user, source_ip`
  - Data exfiltration: `index=network sourcetype=pan:traffic dest_zone=untrust bytes_sent>50000000 | stats sum(bytes_sent) by src_ip, dest_ip, app`

#### ELK Stack (Elasticsearch, Logstash, Kibana)
- **Use case**: Large-volume log ingestion, full-text search, visualization of access patterns.
- **Key queries for breach investigation**:
  - Anomalous access timing: Filter by timestamp outside of business hours (before 07:00 or after 20:00 local time) against personal data system indices.
  - Geo-anomaly detection: Aggregate authentication source IPs by geolocation; flag countries not present in the 90-day baseline.
  - Volume anomaly: Aggregate data access events by user per hour; identify spikes exceeding 3 standard deviations above the 30-day mean.

#### Wireshark / tshark
- **Use case**: Packet-level analysis of network traffic to/from compromised systems.
- **Key filters for breach investigation**:
  - Identify data exfiltration: `ip.src == 10.0.1.50 && tcp.dstport != 443 && frame.len > 1000` (non-HTTPS outbound from compromised host)
  - Identify C2 communication: `dns.qry.name contains ".onion" || dns.qry.name contains "dga"` (DNS queries to suspicious domains)
  - Reconstruct data transfers: Follow TCP streams to recover transferred file contents from PCAP captures.

#### Additional Tools

| Tool | Purpose | Application |
|------|---------|-------------|
| Volatility 3 | Memory forensics | Analyze RAM dumps for malware, injected code, credential harvesting |
| Autopsy / Sleuth Kit | Disk forensics | Recover deleted files, analyze file system timelines, extract artifacts |
| YARA | Malware identification | Scan disk images and memory dumps against malware signature rules |
| Plaso / log2timeline | Super-timeline creation | Create unified timeline from multiple evidence sources |
| Chainsaw | Windows event log analysis | Rapid triage of Windows EVTX logs using Sigma detection rules |

## Scope Determination Process

### Step 1: Identify All Compromised Systems
1. Starting from the initially identified compromised system, trace lateral movement through authentication logs, network connection logs, and endpoint detection alerts.
2. For each system identified, determine whether it stores, processes, or transmits personal data by cross-referencing with the data processing inventory (Art. 30 records).
3. Document each compromised system with: hostname, IP address, function, data classification, personal data categories stored, and estimated data subject count.

### Step 2: Determine Accessed Data
1. For each compromised system containing personal data, analyze access logs to determine which specific tables, files, or records were accessed by the attacker.
2. Distinguish between "system compromised" (attacker had access to the system) and "data accessed" (attacker actually queried or downloaded personal data).
3. Apply the precautionary principle: if logs are insufficient to determine whether specific data was accessed, assume all data on the compromised system was potentially accessed.

### Step 3: Determine Exfiltration
1. Analyze network traffic logs for data transfers from compromised systems to external destinations during the breach window.
2. Review DNS logs for DNS tunneling indicators (unusually long subdomain strings, high query volume to unusual domains).
3. Check for encrypted channel usage (VPN, SSH, HTTPS) to external IPs not in the organization's approved destination list.
4. Examine endpoint logs for evidence of compression, encryption, or staging of files prior to transfer.
5. Report findings as: "Exfiltration confirmed," "No evidence of exfiltration (with confidence level)," or "Exfiltration cannot be ruled out."

### Step 4: Establish Breach Timeline
1. Determine the earliest evidence of unauthorized access (initial compromise date).
2. Identify the timeline of attacker activity — what actions were taken and when.
3. Determine when the breach was detected.
4. Calculate the dwell time (time between initial compromise and detection).
5. Document any periods where log coverage gaps prevent timeline reconstruction.

## Root Cause Analysis

### 5-Whys Framework Applied to Data Breaches

**Example: Stellar Payments Group Ransomware Incident**

1. **Why did the ransomware execute?** The attacker deployed ransomware using a compromised service account with administrative privileges on the database cluster.
2. **Why did the attacker have a compromised service account?** The service account credentials were obtained from a spear-phishing email that an IT operations engineer clicked on 10 March 2026, which installed a credential-harvesting keylogger.
3. **Why did the phishing email reach the engineer?** The email bypassed the email gateway because it was sent from a compromised legitimate domain and contained no detectable malicious payload (the link pointed to a legitimate-appearing login page).
4. **Why did the service account have administrative database privileges?** The service account was originally created for a migration project in 2024 and was never decommissioned. Its privileges were not reviewed as part of the quarterly access review because service accounts were excluded from the review scope.
5. **Why were service accounts excluded from the access review?** The access review policy defined its scope as "user accounts" and did not explicitly include service accounts, machine accounts, or API keys.

**Root cause**: Access review policy gap — service accounts excluded from periodic access certification, combined with stale elevated-privilege service account from completed project.

## Investigation Report Structure

### Section 1: Executive Summary
- Breach type and classification
- Date range of unauthorized activity
- Number of affected data subjects and records
- Root cause (one sentence)
- Current status (contained/ongoing)
- Key remediation recommendations

### Section 2: Investigation Scope and Methodology
- Investigation objectives
- Evidence sources analyzed
- Tools and techniques used
- Investigation team members and roles
- Timeline of investigation activities

### Section 3: Findings
- Detailed breach timeline with evidence citations
- Systems compromised and personal data affected
- Attack vector and technique (mapped to MITRE ATT&CK framework)
- Exfiltration assessment
- Root cause analysis

### Section 4: Impact Assessment
- Data subjects affected (count and categories)
- Personal data compromised (categories and sensitivity)
- Risk assessment for Art. 33/34 notification purposes
- Regulatory exposure assessment

### Section 5: Remediation Recommendations
- Immediate actions (already taken)
- Short-term actions (within 30 days)
- Medium-term actions (within 90 days)
- Long-term systemic improvements

### Section 6: Evidence Inventory
- Complete list of all evidence collected
- Chain of custody records
- Hash verification log
- Evidence retention and disposal schedule
