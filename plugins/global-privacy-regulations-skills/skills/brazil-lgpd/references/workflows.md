# LGPD Compliance Workflow Reference

## Workflow 1: Lawful Basis Determination

### Step 1 — Identify the Processing Activity
1. Document the specific processing operation (collection, storage, use, sharing, deletion).
2. Identify the categories of personal data involved.
3. Determine whether any sensitive data (Art. 5, II) is included — if so, use Art. 11 bases.
4. Identify the categories of data subjects (customers, employees, partners, minors).

### Step 2 — Evaluate Applicable Lawful Bases
1. Assess each of the 10 lawful bases under Art. 7 for applicability.
2. For sensitive data, assess the 8 bases under Art. 11.
3. Document why the selected base is appropriate and why alternatives were rejected.
4. Consider whether multiple bases may apply (primary and fallback).

### Step 3 — Apply Base-Specific Requirements
- **Consent (Art. 7, I)**: Implement standalone consent clause; configure revocation mechanism; establish proof-of-consent records.
- **Legal obligation (Art. 7, II)**: Identify the specific law or regulation; document the mandatory processing requirement.
- **Contract performance (Art. 7, V)**: Verify the data subject is a party to the contract; confirm processing is necessary for performance.
- **Legitimate interest (Art. 7, IX)**: Conduct the four-step balancing test per ANPD guidance; document the analysis; prepare a RIPD if warranted.
- **Credit protection (Art. 7, X)**: Confirm the processing relates to credit risk assessment; comply with Lei 12.414/2011 requirements.

### Step 4 — Document and Record
1. Record the lawful basis determination in the processing activity register (Registro de Atividades de Tratamento).
2. Include the determination in the privacy notice for the relevant data subjects.
3. Store the analysis documentation for the ANPD audit trail.
4. Schedule periodic review (annual or upon material change to the processing activity).

## Workflow 2: Data Subject Rights Response

### Receipt and Triage (Day 0)
1. Data subject submits request through the privacy portal, email to DPO, or written correspondence.
2. System assigns a unique request identifier (e.g., DSR-BR-2026-0001).
3. Verify the requestor's identity using two-factor verification (email confirmation + ID document for high-sensitivity requests).
4. Classify the request type: confirmation, access, correction, deletion, portability, automated decision review, consent withdrawal, or information about sharing.

### Assessment (Days 1-3)
1. Determine whether the request falls within LGPD scope (data subject located in Brazil or data collected in Brazil).
2. Identify all systems containing the requestor's personal data using the data inventory.
3. Assess whether any exemptions apply (legal retention obligation, exercise of rights in proceedings, protection of credit).
4. If the request involves automated decision review (Art. 20), route to the responsible business unit for human review preparation.

### Fulfilment (Days 4-12)
1. **Confirmation/Access (Art. 18, I-II)**: Generate a complete data export from all identified systems; compile in structured format (JSON or PDF).
2. **Correction (Art. 18, III)**: Update records across all systems; generate confirmation of corrections made.
3. **Deletion (Art. 18, IV, VI)**: Execute deletion workflows; document any records retained under legal obligation exemptions; notify third-party recipients per Art. 18, §6.
4. **Portability (Art. 18, V)**: Export data in machine-readable format (JSON/CSV); provide to the data subject or directly to the designated recipient controller.
5. **Automated decision review (Art. 20)**: Provide clear explanation of decision criteria; conduct human review; communicate revised or confirmed decision.

### Response and Closure (Days 13-15)
1. Deliver the response in the simplified or complete format as requested.
2. For simplified format: immediate response or within 15 days.
3. For complete declaration: within 15 days per Art. 19, II.
4. Record the response in the DSR management system.
5. Notify the data subject of their right to file a complaint with the ANPD if dissatisfied.

## Workflow 3: ANPD Breach Notification (Resolution 15/2024)

### Detection and Initial Assessment (Hour 0-4)
1. Security incident detected through SIEM, user report, or third-party notification.
2. Incident response team activated per the playbook.
3. Initial triage: classify the incident type (unauthorised access, data exfiltration, ransomware, accidental disclosure).
4. Determine whether personal data is affected — if no personal data involved, handle through IT incident process only.

### Risk Assessment (Hours 4-24)
1. Identify the categories and volume of personal data affected.
2. Determine whether sensitive data (Art. 5, II) is involved.
3. Assess the potential for material damage to data subjects (financial, reputational, discriminatory, physical).
4. Apply the ANPD risk assessment criteria from Resolution 15/2024:
   - Nature and sensitivity of the data
   - Number of affected data subjects
   - Reversibility of consequences
   - Controller's security posture
5. Determine whether the incident triggers the notification obligation (relevant risk or damage threshold met).

### ANPD Notification (Within 3 Business Days of Confirmed Incident)
1. Prepare the notification form per ANPD requirements:
   - Nature of the personal data affected
   - Information on data subjects affected
   - Technical and security measures adopted before and after the incident
   - Risks related to the incident and possible consequences for data subjects
   - Measures adopted or to be adopted to reverse or mitigate the effects
   - Reasons for delay if notification is not made within the recommended period
2. Submit the notification through the ANPD's electronic petition system (Peticionamento Eletrônico do SEI/ANPD).
3. Record the notification reference number.

### Data Subject Communication (Within 3 Business Days if Required)
1. If the ANPD determines (or the controller assesses) that the incident may cause relevant damage to data subjects, communicate directly.
2. Communication must include:
   - Description of the nature of the affected personal data
   - Information about the technical and security measures used for data protection
   - Risks related to the incident
   - Measures that have been or will be adopted
   - Contact details of the DPO (Encarregado)
3. Communication in clear, plain Portuguese language.
4. If individual communication is disproportionately burdensome, use broadly accessible media (website, press release).

### Post-Incident Actions
1. Complete root cause analysis within 30 days.
2. Implement corrective measures to prevent recurrence.
3. Update the security incident register.
4. Report corrective actions to the ANPD as a supplement to the initial notification.
5. Review and update the RIPD if the incident reveals previously unassessed risks.

## Workflow 4: International Transfer Assessment

### Step 1 — Map the Transfer
1. Identify the personal data categories being transferred.
2. Identify the destination country and receiving entity.
3. Classify the receiving entity's role (controller, processor, sub-processor).
4. Determine the technical mechanism of transfer (API, file transfer, cloud hosting).

### Step 2 — Select Transfer Mechanism (Art. 33)
1. Check whether the destination country has an ANPD adequacy determination (Art. 33, I) — as of March 2026, none have been issued.
2. If no adequacy: determine whether ANPD-approved standard contractual clauses (Resolution 19/2024) can be implemented.
3. If SCCs are not available: assess whether global corporate rules (BCR-equivalent) are in place.
4. For specific transactions: evaluate whether specific consent (Art. 33, VIII), contract performance (Art. 33, V), or legal obligation (Art. 33, IV) applies.

### Step 3 — Conduct Transfer Impact Assessment
1. Assess the legal framework of the destination country regarding government access to personal data.
2. Evaluate the effectiveness of the selected transfer mechanism in light of local laws.
3. Document the assessment methodology and conclusions.
4. If the assessment reveals inadequate protection, identify supplementary measures (encryption, pseudonymisation, access restrictions).

### Step 4 — Implement and Document
1. Execute the selected transfer mechanism (sign SCCs, obtain consent, document legal obligation).
2. Record the transfer in the international transfer register.
3. Implement any supplementary measures identified in the TIA.
4. Schedule annual review of the transfer assessment.

## Workflow 5: Legitimate Interest Assessment (Art. 10)

### Step 1 — Purpose Identification
1. Articulate the specific legitimate interest being pursued.
2. Confirm the interest is lawful under Brazilian law.
3. Verify the interest relates to a concrete situation (not hypothetical).
4. Classify under Art. 10 categories: (I) support/promotion of controller activities or (II) protection of data subject.

### Step 2 — Necessity Test
1. Identify the minimum personal data necessary for the stated purpose.
2. Assess whether the purpose can be achieved with less data or without personal data.
3. Apply data minimisation: restrict processing to strictly necessary data (Art. 10, §1).
4. Document why each data element is necessary.

### Step 3 — Balancing Test
1. Identify the data subject's reasonable expectations based on the context of data collection.
2. Assess the potential impact on data subjects (privacy, discrimination, financial, physical).
3. Evaluate whether a power imbalance exists (employer-employee, service provider-consumer).
4. Consider the vulnerability of affected data subjects (children, elderly, employees).
5. Weigh the controller's interest against the identified impacts.

### Step 4 — Safeguards
1. Implement transparency measures: disclose the legitimate interest in the privacy notice.
2. Provide opt-out mechanisms where appropriate.
3. Apply additional technical safeguards (pseudonymisation, access restrictions).
4. Document all safeguards and their rationale.

### Step 5 — Document and Review
1. Record the complete legitimate interest assessment.
2. Store documentation accessible for ANPD requests (Art. 10, §3).
3. Prepare a RIPD if the processing presents a risk to data subjects.
4. Review the assessment annually or upon material changes.
