# RoPA Audit Workflow Reference

## Pre-Audit Preparation Workflow

1. **Define audit scope**: Identify whether the audit covers all processing activities organisation-wide or is limited to a specific business unit, subsidiary, or processing category.
2. **Assemble audit team**: Assign a lead auditor (typically from the DPO office or internal audit function), a technical reviewer for security measures validation, and a business process analyst for accuracy verification.
3. **Gather input documents**: Collect the current RoPA, organisational chart, application inventory, vendor register, DPIA register, previous audit reports, and any supervisory authority correspondence.
4. **Prepare audit checklist**: Use the Art. 30(1) and Art. 30(2) field requirements to create a per-entry checklist customised to the organisation's RoPA format.
5. **Schedule stakeholder interviews**: Book 30-minute interviews with processing owners for the sample verification phase, targeting 20% of all RoPA entries.
6. **Establish audit timeline**: Allocate 2-4 weeks for a full organisational audit, or 3-5 days for a single business unit audit.

## Field-Level Validation Workflow

### For Each Controller Record (Art. 30(1)):

1. **Art. 30(1)(a) — Controller Identity**
   - Verify legal entity name matches current Companies House / Handelsregister registration.
   - Confirm DPO contact details are current (name, email, phone).
   - If joint controllers exist, verify Art. 26 arrangement is referenced and both controllers are identified.
   - Check that the EU representative (Art. 27) is listed if the controller is established outside the EEA.

2. **Art. 30(1)(b) — Purposes of Processing**
   - Confirm each purpose is specific and granular (not department-level).
   - Verify purposes align with the lawful basis recorded (cross-reference with lawful basis register).
   - Check that no secondary purposes have been added without a compatibility assessment under Art. 6(4).
   - Validate purposes match the privacy notice provided to data subjects under Art. 13/14.

3. **Art. 30(1)(c) — Categories of Data Subjects and Personal Data**
   - Verify data subject categories are exhaustive (employees, contractors, customers, website visitors, job applicants, etc.).
   - Confirm personal data categories are specific (not just "personal data" but "name, email address, IP address, purchase history").
   - Check whether special category data under Art. 9 is flagged and a separate lawful basis recorded.
   - Validate that data categories match what is actually collected in the relevant systems.

4. **Art. 30(1)(d) — Categories of Recipients**
   - List all internal recipients (departments, roles) and external recipients (processors, joint controllers, public authorities).
   - Verify each external recipient has a corresponding contractual arrangement (Art. 28 DPA for processors).
   - Confirm sub-processor chains are documented where the primary processor engages sub-processors.

5. **Art. 30(1)(e) — International Transfers**
   - Identify all transfers to countries outside the EEA.
   - Verify the transfer mechanism for each: adequacy decision (Art. 45), SCCs (Art. 46(2)(c)), BCRs (Art. 47), or derogation (Art. 49).
   - Confirm a Transfer Impact Assessment has been conducted where SCCs are relied upon (per Schrems II / EDPB Recommendations 01/2020).
   - Check that the specific destination country and recipient entity are recorded.

6. **Art. 30(1)(f) — Retention Periods**
   - Verify retention periods are expressed as specific durations (e.g., "7 years from contract termination") or objectively determinable criteria.
   - Cross-reference against the organisation's data retention schedule.
   - Confirm that different data categories within the same processing activity have separately defined retention periods where they differ.
   - Check that deletion or anonymisation procedures are documented and operational.

7. **Art. 30(1)(g) — Technical and Organisational Measures**
   - Verify the description references actual implemented measures, not planned or aspirational ones.
   - Check that measures are proportionate to the risk profile of the processing activity.
   - Confirm the description covers both technical measures (encryption, access controls, logging) and organisational measures (training, policies, incident response).
   - Cross-reference with the most recent information security audit or ISO 27001 certification scope.

### For Each Processor Record (Art. 30(2)):

1. Apply the same validation rigour to fields (a)-(d) as described above for the corresponding controller fields.
2. Additionally verify that the processor record references the specific controller(s) on whose behalf processing is carried out.
3. Confirm the processor has not expanded processing beyond the controller's documented instructions.

## Sample Verification Workflow

1. Select a stratified random sample: 20% of entries, ensuring representation across business units, processing types (automated/manual), and risk levels.
2. For each sampled entry, conduct a 30-minute interview with the processing owner covering:
   - "Walk me through what happens with personal data in this process from collection to deletion."
   - "Who else sees or accesses this data, internally and externally?"
   - "When was the last time this record was reviewed and updated?"
   - "Has anything changed about this processing in the past 12 months?"
3. Compare interview responses against the RoPA entry field by field.
4. Document discrepancies as findings with severity classification.

## Findings Classification

| Severity | Definition | Remediation Timeline |
|----------|-----------|---------------------|
| Critical | Mandatory Art. 30 field completely missing or processing activity not recorded at all | 30 calendar days |
| Major | Field populated but materially inaccurate, outdated by more than 12 months, or too vague to be meaningful | 60 calendar days |
| Minor | Formatting inconsistency, minor inaccuracy that does not affect compliance, or administrative improvement opportunity | 90 calendar days |
| Observation | Best practice recommendation not tied to a specific compliance gap | Next scheduled review |

## Post-Audit Remediation Tracking

1. Create a findings register with unique identifiers, severity, description, affected RoPA entry, assigned owner, and target remediation date.
2. Issue the audit report to the DPO, the Data Protection Steering Committee, and relevant processing owners within 10 business days of audit completion.
3. Schedule a 30-day checkpoint to verify remediation of all critical findings.
4. Schedule a 90-day checkpoint to verify remediation of all major findings.
5. Feed systemic findings into the RoPA governance procedure update cycle.
6. Report audit outcomes in the annual DPO report to the board under Art. 38(3).
