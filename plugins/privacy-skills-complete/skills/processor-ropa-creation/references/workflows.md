# Processor RoPA Creation Workflow Reference

## End-to-End Process

### Phase 1: Controller Relationship Inventory

1. **List all controller relationships**: Review the organisation's DPA register to identify every controller on whose behalf processing is performed.
2. **Verify DPA currency**: Confirm each Art. 28 DPA is current, executed, and covers all processing activities being performed.
3. **Map controller-specific processing**: For each controller, document exactly what processing the organisation performs — not the controller's broader purposes, but the processor's specific operations (hosting, storage, computation, transmission, deletion).
4. **Identify sub-processor chains**: Determine whether any sub-processors are engaged for each controller's data, and whether prior authorisation (specific or general) has been obtained.

### Phase 2: Per-Controller Data Collection

For each controller relationship, complete the following:

#### Step 2.1: Identity Documentation (Art. 30(2)(a))

1. Record the processor's own legal details (entity name, registration, address, DPO).
2. Record the controller's legal details from the Art. 28 DPA.
3. If the controller is established outside the EEA, record their Art. 27 representative details.
4. Record the DPO contact for both processor and controller.

#### Step 2.2: Processing Categories (Art. 30(2)(b))

1. Review the DPA to identify the agreed scope of processing.
2. Interview the technical team to confirm actual processing operations match the DPA scope.
3. Categorise processing operations: hosting/storage, computation/analysis, transmission, backup/recovery, deletion/destruction, support/maintenance, migration.
4. Document each category with a brief description of what the processor does.
5. Flag any processing that may exceed the documented controller instructions (Art. 28(3)(a) compliance risk).

#### Step 2.3: International Transfer Documentation (Art. 30(2)(c))

1. Determine whether any data leaves the EEA during the processor's operations.
2. Check sub-processor locations — any sub-processor in a third country creates a transfer.
3. Check for remote access from third countries (offshore support, follow-the-sun models).
4. For each transfer, document the destination, recipient, safeguard mechanism, and TIA reference.
5. Verify consistency with the transfer provisions in the Art. 28 DPA and any controller-approved sub-processor list.

#### Step 2.4: Security Measures (Art. 30(2)(d))

1. Document the processor's technical and organisational measures that protect the controller's data.
2. Reference relevant certifications (ISO 27001, SOC 2) with scope details.
3. Describe infrastructure security, access controls, encryption, monitoring, incident response, and staff measures.
4. Note any controller-specific security requirements that differ from the processor's standard controls.

### Phase 3: Quality Assurance and Approval

1. **DPA consistency check**: Verify that the Art. 30(2) record aligns with the corresponding Art. 28 DPA in terms of processing scope, controller identity, and sub-processor authorisation.
2. **Completeness validation**: Confirm all four mandatory fields are populated for each controller.
3. **Technical accuracy**: Have the engineering/operations team verify that documented security measures and data flows match actual infrastructure.
4. **DPO review**: The processor's DPO reviews all records for compliance.
5. **Annual review schedule**: Set review dates aligned with DPA renewal dates or at minimum annually.

### Phase 4: Ongoing Maintenance

1. **New controller onboarding**: Create an Art. 30(2) entry for each new controller before processing begins.
2. **Controller offboarding**: When a controller relationship ends, archive the record (do not delete — retain for accountability evidence) and document the data return/deletion per the DPA.
3. **Sub-processor changes**: When adding or changing sub-processors, update the Art. 30(2)(c) transfer field if the sub-processor is in a third country.
4. **Security measure updates**: Reflect infrastructure changes, new certifications, or changes to security controls in the Art. 30(2)(d) field.
5. **Controller instruction changes**: If the controller issues updated processing instructions, update Art. 30(2)(b) to reflect revised processing categories.

## RACI Matrix

| Activity | Responsible | Accountable | Consulted | Informed |
|----------|------------|-------------|-----------|----------|
| Controller relationship inventory | Privacy team | DPO | Legal, Sales/Account Mgmt | Engineering |
| Per-controller data collection | Privacy analyst | DPO | Engineering, Operations | Account manager |
| Transfer documentation | Privacy analyst | DPO | Infrastructure team | Legal |
| Security measures documentation | Security team | CISO | DPO, Engineering | Controller (on request) |
| DPA consistency review | Legal | DPO | Privacy analyst | Account manager |
| Final approval | DPO | DPO | Legal | Senior management |
| Ongoing maintenance | Operations + Privacy | DPO | Engineering | Controller |

## Supervisory Authority Request Protocol

Under Art. 30(4), the processor must make its records available to the supervisory authority on request. Preparation steps:

1. Maintain records in a format that can be exported and shared within 48 hours of a request.
2. Ensure the export does not include the processor's proprietary security configuration details that could create vulnerabilities — Art. 30(2)(d) requires a "general description," not a security blueprint.
3. Coordinate with affected controllers before disclosing records, as the records identify the controllers and the nature of processing.
4. Log all supervisory authority access requests in the compliance register.
