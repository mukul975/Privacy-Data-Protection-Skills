# SCC Implementation Workflow Reference

## Phase 1: Transfer Identification and Module Selection

1. **Identify the transfer**: Determine that personal data is being transferred from the EEA to a third country without an adequacy decision under Art. 45.
2. **Map the parties**: Identify the data exporter (EEA-based party initiating the transfer) and the data importer (third-country recipient).
3. **Determine roles**: Classify each party as controller or processor in relation to the specific processing activity being transferred.
4. **Select the module**:
   - Exporter = Controller, Importer = Controller → Module 1
   - Exporter = Controller, Importer = Processor → Module 2
   - Exporter = Processor, Importer = Sub-processor → Module 3
   - Exporter = Processor, Importer = Controller → Module 4
5. **Document the selection rationale**: Record why the selected module applies, including analysis of each party's role determination.

## Phase 2: Annex Preparation

### Annex I Completion Workflow

1. **Section A — List of Parties**:
   - Record the legal name, registered address, and contact person for each party.
   - Specify the activities relevant to the data transfer.
   - Assign the controller/processor role designation for each party.
   - If using the docking clause (Clause 7), prepare the accession form for additional parties.

2. **Section B — Description of Transfer**:
   - Enumerate all categories of data subjects whose data is transferred.
   - List all categories of personal data, distinguishing between ordinary and special category data (Art. 9 / Art. 10).
   - Specify the frequency of transfer (continuous, daily batch, ad hoc).
   - Describe the nature and purpose of processing by the importer.
   - Define the retention period or criteria for determining retention.

3. **Section C — Competent Supervisory Authority**:
   - Identify the SA of the EU Member State in which the exporter is established.
   - For exporters established in multiple Member States, select the SA per Art. 56 GDPR lead authority rules.
   - For non-EU exporters relying on Art. 3(2), identify the SA of the Member State referred to in Art. 13(1)(a).

### Annex II Completion Workflow

1. Document all technical measures implemented by the importer: encryption standards, access control mechanisms, network security, endpoint protection.
2. Document all organisational measures: staff training, background checks, incident response procedures, sub-processor governance.
3. Cross-reference measures against the EDPB Recommendations 01/2020 supplementary measures catalogue.
4. Ensure measures are specific and verifiable, not generic or aspirational.
5. Include the results of the most recent security audit or certification (ISO 27001, SOC 2 Type II).

### Annex III Completion Workflow (Module 2 and Module 3 only)

1. List every sub-processor engaged by the data importer.
2. For each sub-processor, document: legal name, country of establishment, description of processing activity, safeguard mechanism.
3. Obtain the controller's authorisation for each listed sub-processor (specific or general).
4. Establish the notification procedure for sub-processor additions or replacements.

## Phase 3: Transfer Impact Assessment (Clause 14)

1. Identify the legal framework of the importer's country relevant to government access to personal data.
2. Assess whether any identified laws impinge upon the protections provided by the SCCs.
3. Apply the EDPB four European Essential Guarantees test to each identified law.
4. Document the assessment methodology, sources consulted, and conclusions.
5. If the assessment reveals that the importer cannot comply with the SCCs, identify supplementary measures or suspend the transfer.
6. Record the TIA results and attach to the SCC documentation package.

## Phase 4: Internal Approval and Execution

1. Submit the complete SCC package (clauses, all annexes, TIA) to the DPO for review.
2. Obtain legal review confirming the correct module selection, annex completeness, and governing law/jurisdiction selection.
3. Present the SCC package to the data protection steering committee for approval.
4. Execute the SCCs: both parties sign, date, and retain executed originals.
5. Record the execution in the transfer register with the SCC version number, execution date, module, and next review date.

## Phase 5: Ongoing Compliance Management

1. **Monitor legal developments**: Track legislative changes in the importer's jurisdiction that may affect the Clause 14 assessment.
2. **Sub-processor changes**: Process notifications of sub-processor additions, conducting due diligence and updating Annex III.
3. **Annual review**: Re-assess each SCC at least annually against current conditions.
4. **Incident management**: If the importer receives a government access request, activate the Clause 15 notification and challenge procedures.
5. **Data subject requests**: Ensure the importer's procedures for handling data subject rights requests under Clause 10 are operational and tested.
6. **Audit rights**: Exercise the audit right under the SCCs at least once during the contract term; document findings and remediation.
7. **Termination and data return**: Upon SCC termination, verify data return or certified deletion per the relevant module clause.

## Docking Clause (Clause 7) Workflow

1. New party submits the completed Annex I.A accession form.
2. Existing parties review and consent to the accession.
3. The new party assumes all obligations under the SCCs from the date of accession.
4. Update the transfer register and Annex I.A to reflect the additional party.
5. Conduct a Clause 14 TIA if the new party is located in a different jurisdiction than the original importer.
