# PIPA Compliance Workflow Reference

## Workflow 1: Consent Collection and Management

### Step 1 — Determine Consent Requirements
1. Identify the processing purpose and data items to be collected.
2. Determine whether any sensitive information (Art. 23) is included — if so, separate explicit consent required.
3. Assess whether the legitimate interest basis (Art. 15(1)(6)) may apply as an alternative to consent.
4. If consent is required, determine whether the processing includes marketing purposes (separate opt-in needed per Art. 22(2)).

### Step 2 — Design Consent Interface
1. Present required information in clear Korean language:
   - Purpose of collection and use
   - Items of personal information collected
   - Retention and use period
   - Right to refuse consent and consequences of refusal
2. Display important information prominently (larger font, contrasting colour, bold text per Art. 22(1)).
3. Separate consent for: (a) essential processing, (b) optional processing, (c) marketing, (d) sensitive information, (e) third-party provision, (f) cross-border transfer.
4. Do not use pre-ticked boxes; each consent must be an affirmative action.

### Step 3 — Record and Maintain Consent
1. Store consent records with: data subject identifier, timestamp, consent scope, version of notice, collection channel.
2. Provide withdrawal mechanism accessible from the same interface used for collection.
3. Upon withdrawal, cease processing within the agreed timeframe (typically within 10 days).
4. Retain consent records for the retention period specified in the consent or until legal obligations are fulfilled.

## Workflow 2: Cross-Border Transfer Under 2023 Amendments

### Step 1 — Identify Transfer Mechanism
1. Check whether the destination has PIPC adequacy recognition (EU/EEA, UK as of March 2026).
2. If adequate: transfer permitted with notification to data subjects per Art. 28-8(3).
3. If not adequate: select from consent, contract necessity, PIPC SCCs, BCR equivalent, or PIPC certification.
4. Document the mechanism selection rationale.

### Step 2 — Provide Notification
1. Notify data subjects of: recipient identity, destination country, PI items transferred, purpose, retention period, right to refuse.
2. For consent-based transfers, notification must precede consent collection.
3. For non-consent mechanisms, notification through privacy notice or direct communication.

### Step 3 — Execute and Document
1. Execute the selected mechanism (sign SCCs, obtain consent, rely on adequacy).
2. Record in the cross-border transfer register.
3. For PIPC SCCs: file with the PIPC within 30 days of execution.
4. Schedule periodic review (annual or upon material change).

## Workflow 3: Data Subject Rights Response

### Receipt and Triage (Day 0)
1. Request received through privacy portal, customer service, or written submission.
2. Verify identity using resident registration number or alternative verification per PIPC guidance.
3. Classify: access, correction, deletion, or suspension.

### Fulfilment (Days 1-10)
1. **Access (Art. 35)**: Compile data from all systems; provide within 10 days.
2. **Correction/Deletion (Art. 36)**: Verify the request; update or delete within 10 days; notify the data subject of completion.
3. **Suspension (Art. 37)**: Suspend processing within 10 days; if suspension would conflict with legal obligations, inform the data subject of the reason.
4. **Automated decision rights (Art. 37-2)**: Provide explanation of automated decision criteria; offer refusal mechanism.

### Response (Day 10)
1. Deliver response in Korean.
2. If extension needed, notify data subject of delay and reason before the 10-day deadline.
3. If request denied, provide written reasons and inform of complaint rights to the PIPC.
4. Record in the DSR management log.

## Workflow 4: Pseudonymisation Processing

### Step 1 — Determine Eligibility
1. Confirm the processing purpose falls within Art. 28-2: statistics, scientific research, or public interest records.
2. Assess whether the purpose can be achieved with anonymised data (preferred) or requires pseudonymised data.
3. If combination with other handlers' pseudonymised data is needed, engage the PIPC-designated combination entity.

### Step 2 — Apply Pseudonymisation
1. Select appropriate technique: generalisation, suppression, noise addition, tokenisation, permutation.
2. Apply risk assessment to determine the adequacy of de-identification.
3. Separate additional information (re-identification keys) into an isolated storage environment.
4. Encrypt additional information using AES-256 or equivalent.
5. Restrict access to additional information to designated authorised personnel only.

### Step 3 — Ongoing Safeguards
1. Maintain access logs for pseudonymised data and additional information (minimum 2 years).
2. Prohibit any attempt to re-identify individuals from pseudonymised data.
3. If accidental re-identification occurs, immediately destroy re-identified data or cease processing.
4. Conduct annual review of pseudonymisation adequacy and risk assessment.

## Workflow 5: Breach Notification

### Detection (Hour 0)
1. Incident detected through monitoring, user report, or external notification.
2. Activate incident response team.
3. Classify: personal information breach or non-PI incident.

### Assessment (Hours 0-24)
1. Determine the number of affected individuals.
2. Identify categories of PI compromised.
3. Assess potential for harm.
4. Determine notification obligations: 1,000+ individuals → PIPC notification within 72 hours.

### Notification (Within 72 hours for PIPC; without delay for individuals)
1. **Individual notification**: Provide facts of breach, items leaked, countermeasures taken, grievance contact.
2. **PIPC notification**: Submit through the PIPC breach notification system within 72 hours if 1,000+ affected.
3. **Public notification**: If 10,000+ affected, public notification through website and media.
4. **Record**: Document all notifications and retain evidence.

### Remediation
1. Implement containment and eradication measures.
2. Conduct root cause analysis.
3. Implement preventive measures.
4. Report remediation actions to the PIPC.
5. Update internal management plan if systemic issues identified.
