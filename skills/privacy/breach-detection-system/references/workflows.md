# Breach Detection System Implementation Workflow

## Phase 1: Requirements and Data Source Inventory (Weeks 1-2)

1. **Identify all personal data systems**: Cross-reference the Art. 30 Records of Processing Activities with the IT asset management database (CMDB) to produce a complete inventory of systems that store, process, or transmit personal data.
2. **Classify systems by data sensitivity**: Apply the Level 3 classification taxonomy (Critical, High, Medium, Low) based on the data categories processed.
3. **Map existing monitoring coverage**: Determine which personal data systems are already covered by SIEM, DLP, IDS/IPS, or endpoint detection and which have no monitoring.
4. **Identify coverage gaps**: Produce a gap analysis showing systems with no monitoring, incomplete log ingestion, or missing detection rules.
5. **Define detection requirements**: For each system and data sensitivity level, specify the required detection capabilities (real-time vs. batch, alert types, escalation paths).

## Phase 2: SIEM Configuration (Weeks 3-6)

### Log Source Onboarding
1. For each identified personal data system, configure log forwarding to the SIEM (Splunk Enterprise Security):
   - Install Splunk Universal Forwarder on Windows/Linux servers.
   - Configure syslog forwarding for network devices and databases.
   - Set up API-based ingestion for cloud services (AWS CloudTrail, Microsoft 365, Okta).
   - Validate log receipt and parsing — confirm timestamps, user fields, and action fields are correctly extracted.
2. Implement log retention aligned with investigation requirements: minimum 12 months online, 7 years archived (aligned with data retention schedule and regulatory requirements).

### Correlation Rule Deployment
1. Deploy the five core breach detection correlation rules (mass data access, data exfiltration, privileged account anomaly, ransomware behavior, authentication brute force).
2. Set initial thresholds conservatively (lower sensitivity) to gather baseline data.
3. Run rules in "advisory mode" (logging without alerting) for 2 weeks to assess false positive rates.
4. Tune thresholds based on advisory mode results. Target: under 15% false positive rate for each rule.
5. Activate alerting and escalation for tuned rules.

## Phase 3: DLP Deployment (Weeks 4-8)

### Email DLP
1. Configure DLP policies in Microsoft 365 Compliance Center for outbound email inspection.
2. Define sensitive information types: German Personalausweisnummer (regex), IBAN (regex), credit card numbers (Luhn validation), health insurance numbers.
3. Deploy policies in "test mode" for 2 weeks, review matched content for accuracy.
4. Activate enforcement actions: block, encrypt, or alert based on policy severity.

### Endpoint DLP
1. Deploy CrowdStrike Falcon Data Protection agent to all endpoints with access to personal data systems.
2. Configure policies for USB copy, cloud upload, print, and screen capture of personal data.
3. Test policies with representative scenarios from each business unit.
4. Activate enforcement with exception workflow (DPO-approved ticket required for policy override).

## Phase 4: UEBA and Insider Threat Monitoring (Weeks 6-10)

1. **Baseline establishment**: Allow the UEBA platform (Splunk UBA or Exabeam) to collect 30 days of normal activity data to establish per-user behavioral baselines.
2. **Integrate HR data feed**: Connect Workday HR system to provide context on employee status (notice period, performance improvement plan, department transfers) as risk amplifiers.
3. **Configure composite risk scoring**: Implement the insider threat indicator weighting system (access timing, bulk download, personal cloud usage, HR status, role scope violations, control circumvention, repeated failed access).
4. **Set alerting thresholds**: Score above 60 triggers enhanced monitoring. Score above 80 triggers investigation.
5. **Privacy review**: Ensure the insider threat monitoring program has been reviewed by the DPO, works council (Betriebsrat for German employees), and legal counsel. Document the legitimate interest assessment under Art. 6(1)(f) and the employee privacy impact assessment.

## Phase 5: Integration and Automation (Weeks 8-12)

1. **ServiceNow integration**: Configure automated ticket creation in the privacy incident management queue when a SIEM correlation rule triggers on a system tagged as containing personal data.
2. **Enrichment workflow**: Automate enrichment of breach alerts with: data classification of the affected system, data subject count estimate, DPO contact for the relevant business unit, applicable notification deadlines.
3. **Playbook automation**: Create Splunk SOAR playbooks for common breach scenarios:
   - Ransomware detection → auto-isolate endpoint → capture memory dump → alert IR team + DPO.
   - Data exfiltration → auto-block external destination → alert SOC + DPO → initiate forensic hold.
   - Credential compromise → auto-disable account → reset sessions → alert identity team + DPO.
4. **Dashboard creation**: Build real-time dashboards showing: active breach investigations, detection rule alert volume by severity, false positive rates, mean time to detect (MTTD), and mean time to escalate.

## Phase 6: Testing and Validation (Weeks 10-14)

1. **Detection rule validation**: Execute test scenarios for each correlation rule using controlled, authorized penetration testing activities. Confirm detection and correct alerting.
2. **DLP bypass testing**: Attempt to exfiltrate test personal data through each monitored channel (email, USB, cloud, print). Verify policy enforcement.
3. **End-to-end test**: Conduct a simulated breach scenario (red team exercise) and measure the complete detection-to-notification chain. Target: under 4 hours from initial compromise indicator to DPO notification.
4. **Tabletop exercise**: Run a breach simulation tabletop exercise with SOC, privacy, legal, and executive teams to validate that alerting, escalation, and communication processes work as designed.
5. **Document results**: Produce a detection capability assessment report with: coverage percentage, detection latency metrics, false positive rates, and identified gaps.

## Ongoing Operations

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Correlation rule tuning | Monthly | SOC Lead |
| False positive rate review | Monthly | SOC Analyst |
| New system onboarding validation | Per new system deployment | IT Security + DPO |
| UEBA baseline recalibration | Quarterly | SOC Lead |
| Red team detection validation | Semi-annually | CISO |
| Full tabletop exercise | Annually | DPO + CISO |
| Detection capability assessment report | Annually | SOC Lead + DPO |
