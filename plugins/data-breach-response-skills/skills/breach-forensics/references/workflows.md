# Breach Investigation Forensics Workflow

## Phase 1: Evidence Preservation (Hours 0-6)

### 1.1 Activate Forensic Response
1. Incident Commander confirms breach status and authorizes forensic investigation under reference number SPG-BREACH-2026-003.
2. CISO (Thomas Brenner) activates the external forensic retainer — Mandiant incident response team (retainer agreement SPG-IR-2025-007).
3. Establish investigation communication channel: dedicated Signal group for investigation team members (out-of-band from potentially compromised corporate communications).
4. Brief the investigation team on what is known: affected systems, initial indicators, timeline of events so far.

### 1.2 Volatile Evidence Collection (Priority 1 — Within 2 Hours)
1. **RAM acquisition**: For each affected system, capture a full memory dump before any remediation or shutdown:
   - Windows: Run WinPmem (`winpmem_mini_x64.exe output.raw`) from a forensic USB.
   - Linux: Use LiME kernel module (`insmod lime.ko "path=/mnt/forensic/mem.lime format=lime"`).
   - Record: system hostname, timestamp, operator name, tool version, output file hash (SHA-256).
2. **Live network state**: Capture active network connections, routing tables, and ARP cache:
   - Windows: `netstat -anob > netstat_output.txt && route print > routes.txt && arp -a > arp.txt`
   - Linux: `ss -tupan > ss_output.txt && ip route > routes.txt && ip neigh > arp.txt`
3. **Running processes**: Capture process listings with full command lines, parent-child relationships, and loaded modules.
4. **Open files and handles**: Document which files and network resources are currently open by each process.

### 1.3 Non-Volatile Evidence Collection (Priority 2 — Within 6 Hours)
1. **Forensic disk images**: Create bit-for-bit disk images of affected system storage:
   - Use FTK Imager or dc3dd with write-blocking.
   - Calculate SHA-256 and MD5 hashes of both source and image.
   - Verify hashes match.
   - Store images on dedicated forensic storage (not connected to the production network).
2. **Log preservation**: Export and archive the following logs for the investigation window (30 days before estimated breach start through current date):
   - SIEM aggregated logs (Splunk export to CSV/JSON).
   - Database audit logs (PostgreSQL pg_audit output).
   - Authentication logs (Okta system log, Active Directory Security event log).
   - Network logs (Palo Alto firewall session logs, DNS query logs).
   - Cloud logs (AWS CloudTrail, S3 access logs).
   - Email logs (Microsoft 365 Unified Audit Log).
3. **Evidence inventory**: Create a master evidence log documenting every item collected with: evidence ID, description, collection timestamp, collector name, tool used, hash value, and storage location.

## Phase 2: Initial Analysis and Scoping (Hours 6-24)

### 2.1 Timeline Reconstruction
1. Ingest all collected evidence into the forensic analysis environment (isolated network segment).
2. Create a super-timeline using Plaso/log2timeline that merges:
   - File system timestamps (MACB: Modified, Accessed, Created, Birth)
   - Event log entries
   - Browser history and download records
   - Email metadata
   - Database query timestamps
   - Network connection logs
3. Filter the super-timeline to focus on the investigation window.
4. Identify the earliest indicator of compromise (IOC) and work forward chronologically.

### 2.2 Malware Analysis (If Applicable)
1. Extract identified malware samples from memory dumps and disk images.
2. Calculate file hashes (SHA-256, MD5) and check against threat intelligence feeds (VirusTotal, AlienVault OTX, MISP).
3. Conduct static analysis: strings extraction, PE header analysis, import table review.
4. If safe to do so, conduct dynamic analysis in an isolated sandbox environment.
5. Map malware capabilities to MITRE ATT&CK techniques.

### 2.3 Initial Scope Determination
1. From the timeline analysis, identify all systems accessed by the attacker or affected by the incident.
2. For each system, determine:
   - Whether it contains personal data (cross-reference with Art. 30 records).
   - Whether the attacker accessed, modified, or exfiltrated personal data.
   - The data categories and approximate data subject count.
3. Provide an initial scope assessment to the DPO within 24 hours to support the Art. 33 notification decision.

## Phase 3: Deep Analysis (Hours 24-168 / Days 1-7)

### 3.1 Attack Path Reconstruction
1. Map the complete attack path from initial access through lateral movement to objective completion.
2. For each step in the attack path, document:
   - Timestamp (UTC)
   - Source system and destination system
   - Technique used (mapped to MITRE ATT&CK)
   - Evidence source (log entry, artifact, network capture)
   - Personal data exposure assessment for this step
3. Create a visual attack path diagram showing the sequence of compromise.

### 3.2 Exfiltration Analysis
1. Analyze network flow data for the breach window:
   - Identify all outbound data transfers from compromised systems.
   - Calculate total data volume transferred to external destinations.
   - Classify destinations as known-good (approved SaaS, CDN, partner), suspicious, or malicious.
2. Check for non-standard exfiltration channels:
   - DNS tunneling: analyze DNS query logs for unusually long subdomains or high query volume to unusual domains.
   - ICMP tunneling: check for oversized or high-frequency ICMP traffic.
   - Steganography: if image files were transferred, check for embedded data.
   - Encrypted channels: identify SSH, VPN, or HTTPS connections to unknown external IPs.
3. Correlate network exfiltration analysis with endpoint forensics:
   - Check for file staging (compression, encryption, renaming) before transfer.
   - Review clipboard history and screen capture activity.
4. Formulate an exfiltration determination: Confirmed / Not Confirmed / Cannot Be Ruled Out.

### 3.3 Root Cause Analysis
1. Identify the initial access vector: how did the attacker gain first access?
2. Identify the privilege escalation method: how did the attacker obtain sufficient access to reach personal data?
3. Identify the contributing factors: what security control gaps enabled the attack?
4. Apply the 5-Whys methodology to trace contributing factors to root causes.
5. Document root causes with supporting evidence references.

## Phase 4: Reporting (Days 7-14)

### 4.1 Draft Investigation Report
1. Follow the standard report structure (Executive Summary, Scope and Methodology, Findings, Impact Assessment, Remediation Recommendations, Evidence Inventory).
2. Ensure all findings are supported by specific evidence references.
3. Include MITRE ATT&CK mapping for the complete attack chain.
4. Provide precise data impact figures: which personal data categories were confirmed compromised, how many data subjects, and the confidence level of these determinations.

### 4.2 Legal Review
1. External counsel (Freshfields Bruckhaus Deringer) reviews the non-privileged report for:
   - Accuracy and consistency with prior statements to supervisory authorities.
   - Potential liability implications.
   - Recommendations that may have regulatory or litigation impact.
2. Privileged analysis (attorney work product) is maintained separately.

### 4.3 Report Distribution
1. Final report distributed to: DPO, CISO, CEO, General Counsel, Board Audit Committee.
2. Redacted summary prepared for supervisory authority submission (if requested).
3. Evidence is preserved in the forensic evidence vault per the retention schedule.

## Evidence Retention Schedule

| Evidence Type | Retention Period | Storage | Disposal Method |
|--------------|-----------------|---------|----------------|
| Forensic disk images | 7 years from investigation close | Encrypted forensic storage vault | Secure erasure (NIST 800-88 Clear + Purge) |
| Memory dumps | 3 years from investigation close | Encrypted forensic storage vault | Secure erasure |
| Log exports | 7 years from investigation close | Encrypted archive storage | Secure erasure |
| Network captures (PCAP) | 3 years from investigation close | Encrypted forensic storage vault | Secure erasure |
| Investigation report | 10 years from investigation close | Document management system | Controlled destruction |
| Chain of custody records | 10 years from investigation close | Document management system | Controlled destruction |
