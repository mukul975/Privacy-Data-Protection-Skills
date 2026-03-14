# Supplementary Measures Implementation Workflow

## Selection Workflow

### Phase 1: Gap Identification (from TIA Step 3)

1. Review the TIA's European Essential Guarantees assessment for the destination country.
2. List each identified gap with its corresponding EEG category (EEG 1-4).
3. Classify each gap by severity:
   - **Critical**: The identified law directly enables government access to the specific data being transferred with no safeguards.
   - **Major**: The identified law enables government access but with some procedural safeguards that do not meet EU standards.
   - **Minor**: Theoretical access risk exists but practical likelihood is low based on data type and importer profile.
4. Document the gap register for use in measure selection.

### Phase 2: Measure Mapping

1. For each identified gap, consult the EDPB Annex 2 use case catalogue.
2. Identify candidate measures from each category (technical, contractual, organisational).
3. Assess each candidate measure against the specific gap:
   - Does the measure directly prevent the identified risk (e.g., encryption prevents plaintext disclosure)?
   - Or does the measure only mitigate the risk (e.g., contractual obligation to challenge reduces likelihood but does not prevent disclosure)?
4. For critical gaps, at least one technical measure that directly prevents the risk must be included.
5. For major gaps, a combination of technical and contractual measures is recommended.
6. For minor gaps, contractual and organisational measures may be sufficient.

### Phase 3: Feasibility Assessment

1. For each selected measure, assess technical feasibility:
   - Can the measure be implemented within the existing architecture?
   - What is the estimated implementation effort and cost?
   - Does the measure affect the importer's ability to fulfil the processing purpose?
2. Assess legal feasibility:
   - Do local laws in the destination country prohibit the measure (e.g., anti-encryption laws)?
   - Can the contractual obligations be enforced in the destination jurisdiction?
3. If a selected measure is not feasible, identify alternatives or escalate to the DPO for a transfer suspension assessment.

## Implementation Workflow

### Phase 4: Technical Measure Deployment

#### Encryption Implementation

1. Define the encryption requirements: algorithm, key length, mode of operation, key management.
2. Design the encryption architecture: where encryption occurs (exporter middleware, application layer, database layer), where keys are stored (EU KMS), key rotation schedule.
3. Implement encryption in the development environment.
4. Conduct security testing: verify cipher suite strength, test key rotation, validate certificate pinning.
5. Deploy to production with monitoring alerts for encryption failures.
6. Document the implementation: architecture diagram, configuration parameters, key custodian assignments.

#### Pseudonymisation Implementation

1. Identify the data elements to be pseudonymised (directly identifying fields only).
2. Select the pseudonymisation technique: HMAC-SHA256 with secret key (recommended).
3. Generate and securely store the pseudonymisation key in the EU key vault.
4. Implement the pseudonymisation function in the data pipeline before the transfer stage.
5. Verify that the pseudonymised dataset cannot be re-identified using data available to the importer.
6. Implement the mapping table storage with restricted access (maximum 4 authorised users).
7. Test the end-to-end flow: pseudonymise, transfer, verify importer receives only pseudonymised data.

#### Split Processing Implementation

1. Identify the data elements that must be split: identity data (names, contacts) vs. operational data (references, dates, quantities).
2. Design the split architecture: which data remains in the EU, which is transferred.
3. Ensure the transferred fragment cannot be recombined with publicly available data to re-identify individuals.
4. Implement data splitting in the ETL pipeline.
5. Verify fragment isolation: the importer's environment must have no access to the identity fragment.
6. Document the recombination procedure (EU-side only) for analytics and reporting.

### Phase 5: Contractual Measure Execution

1. Draft the Supplementary Measures Addendum referencing specific TIA gaps and corresponding measures.
2. Internal legal review of the addendum for enforceability in the destination jurisdiction.
3. Negotiate the addendum with the data importer.
4. Execute the addendum as an annex to the SCCs.
5. Confirm the importer has the operational capability to comply with each contractual obligation (e.g., legal resources to challenge government requests).
6. File the executed addendum with the SCC documentation package.

### Phase 6: Organisational Measure Deployment

1. Communicate the supplementary measures requirements to the importer's operational staff.
2. Deploy access restriction controls per the access policy measure.
3. Establish the transparency reporting schedule and template.
4. Verify the importer's ISO certification status and surveillance audit schedule.
5. Set up the incident escalation communication channel (dedicated email, phone, or secure messaging).
6. Conduct a tabletop exercise simulating a government access request to test the escalation protocol.

## Verification and Monitoring Workflow

### Phase 7: Initial Verification

1. Conduct a technical review of all implemented measures within 30 days of deployment.
2. Verify encryption is active on all transfer channels (certificate check, cipher suite scan).
3. Verify pseudonymisation is applied to all designated fields (sample data inspection).
4. Verify access controls are operative (access list review, log analysis).
5. Confirm contractual addendum is executed and filed.
6. Document the verification results in the TIA record.

### Phase 8: Ongoing Monitoring

1. Continuous: Monitor encryption certificate expiry, key rotation events, and TLS configuration changes via automated alerting.
2. Monthly: Review the warrant canary publication.
3. Quarterly: Review importer access logs for anomalies.
4. Semi-annually: Test the incident escalation protocol.
5. Annually: Full supplementary measures review including:
   - Technical measure effectiveness re-assessment
   - Contractual obligation compliance verification
   - Organisational measure audit
   - Update the TIA with any changes
6. Upon trigger event: Re-assess the supplementary measures package within 14 days of any TIA trigger event.
