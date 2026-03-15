# APPI Compliance Workflow Reference

## Workflow 1: Cross-Border Transfer with Pre-Transfer Information

### Step 1 — Determine Mechanism
1. Check if destination has PPC adequacy recognition (EU/EEA, UK).
2. If adequate: transfer permitted without consent; document the adequacy basis.
3. If not adequate: assess whether the recipient has equivalent measures (contract or corporate group rules).
4. If no equivalent measures: proceed with consent + pre-transfer information.

### Step 2 — Prepare Pre-Transfer Information
1. Identify the destination country by name.
2. Research the PI protection system of the destination:
   - Does a comprehensive data protection law exist?
   - Is there an independent enforcement authority?
   - What individual rights are available?
3. Document the recipient's specific protection measures.
4. Present this information to the individual in clear Japanese language.

### Step 3 — Obtain Consent
1. After providing pre-transfer information, request consent.
2. Consent must be specific to the cross-border transfer.
3. Record: individual identifier, timestamp, destination disclosed, information provided, consent scope.

### Step 4 — Maintain Records
1. Record the transfer in the cross-border transfer register.
2. Retain pre-transfer information provided and consent records.
3. If the recipient is under "equivalent measures," conduct periodic verification (at least annually) that measures remain in place.
4. If equivalent measures are no longer maintained, cease transfer or obtain consent with pre-transfer information.

## Workflow 2: Individual Rights Response (2022 Enhanced)

### Receipt
1. Individual submits request: disclosure, correction, cessation of use, cessation of provision, or third-party provision record disclosure.
2. Verify identity per PPC Guidelines (government-issued ID, account authentication).
3. May charge a reasonable fee for disclosure requests (Art. 38(2)).

### Assessment
1. Confirm the data qualifies as retained personal data.
2. Note: 2022 amendments removed the 6-month exclusion — all personal data in databases is now subject.
3. For disclosure: determine requested format (paper or electronic/electromagnetic record).
4. For cessation of use: assess which expanded trigger applies (purpose achieved, no longer needed, security incident, rights harmed).

### Fulfilment
1. **Disclosure (Art. 33)**: Provide data in the format requested by the individual (electronic if requested); include third-party provision records if requested under Art. 33(5).
2. **Correction (Art. 34)**: Investigate factual accuracy; correct, add, or delete as warranted.
3. **Cessation of use/erasure (Art. 35(1))**: Delete or cease use; if deletion is difficult, take alternative measures to protect rights.
4. **Cessation of third-party provision (Art. 35(3))**: Cease providing to third parties.

### Response
1. Respond "without delay" (遅滞なく) — target 2 weeks for standard requests, up to 2 months for complex.
2. If request is refused, provide reasons in writing.
3. Inform of the right to file a complaint with the PPC.
4. Record in the DSR management log.

## Workflow 3: Pseudonymously Processed Information

### Step 1 — Apply Processing Standards (Art. 41)
1. Delete descriptions that can identify a specific individual by themselves.
2. Delete Individual Number (My Number) and other specified identifiers.
3. Delete personal identification codes (biometric data used for identification).
4. Delete information that may cause property damage (credit card numbers).
5. Apply additional de-identification appropriate to the database characteristics.

### Step 2 — Separate Additional Information
1. Store information used for pseudonymisation (mapping tables, encryption keys) separately from the pseudonymised data.
2. Implement access controls to prevent re-identification.
3. Establish and publish security management measures.

### Step 3 — Use and Governance
1. Use only internally — third-party provision is prohibited.
2. Publicly announce the purpose of use.
3. No accuracy obligation required.
4. Do not attempt to re-identify individuals.
5. Conduct annual review of pseudonymisation adequacy.

## Workflow 4: Third-Party Provision Record-Keeping (Arts. 29-30)

### Provider Records (Art. 29)
1. When providing personal data to a third party, record: date, recipient name, individual's name, data items provided.
2. Retain records for 3 years (PPC Rules).
3. Records are subject to individual disclosure requests under Art. 33(5).

### Recipient Records (Art. 30)
1. When receiving personal data from a third party, confirm and record: provider name, circumstances of provider's acquisition, individual's name, data items, consent basis.
2. Retain for 3 years.
3. If data was acquired through improper means, do not accept the provision.

## Workflow 5: Breach Notification

### Detection and Assessment
1. Detect breach; activate incident response.
2. Assess whether the breach triggers PPC notification obligations:
   - Special care-required information leaked
   - Information likely to be used for financial damage
   - Potentially wrongful purpose leak
   - 1,000+ individuals affected

### PPC Notification
1. Preliminary report to PPC within 3-5 business days (PPC Guidelines).
2. Full report within 30 days (60 days for wrongful purpose leaks).
3. Include: incident description, data types, individuals affected, measures taken.

### Individual Notification
1. Notify affected individuals promptly.
2. Include: description, data affected, remedial measures, contact information.
3. If direct notification is impracticable, use alternative public methods.
