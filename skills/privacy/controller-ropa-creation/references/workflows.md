# Controller RoPA Creation Workflow Reference

## End-to-End RoPA Creation Process

### Phase 1: Processing Activity Discovery

1. **Obtain the organisational chart**: Map every business unit, department, and team that handles personal data.
2. **Review the IT application inventory**: List all systems that store, transmit, or process personal data, including SaaS platforms, on-premises databases, shared drives, and email systems.
3. **Conduct departmental workshops**: Schedule 60-minute workshops with each department head and key staff to identify all processing activities. Use the prompt: "Walk me through every way your team collects, uses, stores, shares, or deletes personal data about individuals."
4. **Identify shadow IT processing**: Specifically ask about spreadsheets, personal devices, messaging apps, and cloud storage not managed by IT.
5. **Cross-reference with existing documentation**: Check privacy notices, data processing agreements, DPIA register, and consent records for processing activities not yet captured.
6. **Create the processing activity register**: Assign each identified activity a unique identifier (e.g., RPA-001) and a descriptive name.

### Phase 2: Data Collection per Processing Activity

For each identified processing activity, complete the following data collection steps:

#### Step 2.1: Controller Identity (Art. 30(1)(a))

1. Confirm the legal entity acting as controller for this specific processing activity.
2. Verify DPO contact details are current.
3. Determine if any joint controller relationships exist (Art. 26).
4. Check if an EU representative is required (Art. 27) — applicable if controller is established outside the EEA.

#### Step 2.2: Purpose Documentation (Art. 30(1)(b))

1. Interview the processing owner to articulate the specific purpose in plain language.
2. Map the purpose to a lawful basis under Art. 6(1).
3. If special category data is involved, identify the additional condition under Art. 9(2).
4. Verify the purpose matches what is communicated to data subjects in the privacy notice (Art. 13/14).
5. Ensure purpose granularity — one RoPA entry per distinct purpose, not per department.

#### Step 2.3: Data Subject and Data Categories (Art. 30(1)(c))

1. List every category of individual whose data is processed in this activity.
2. For each data subject category, list the specific data elements collected.
3. Flag any special category data (Art. 9(1)): racial/ethnic origin, political opinions, religious beliefs, trade union membership, genetic data, biometric data for identification, health data, sex life/sexual orientation.
4. Flag any criminal conviction data (Art. 10).
5. Verify against the actual data fields in the source system(s).

#### Step 2.4: Recipient Identification (Art. 30(1)(d))

1. Map the data flow diagram for this processing activity.
2. Identify all internal access (which departments/roles can view or modify the data).
3. Identify all external recipients: processors, sub-processors, other controllers, public authorities.
4. For each processor, verify an Art. 28 DPA is in place and record the reference number and execution date.
5. For joint controllers, verify an Art. 26 arrangement exists.

#### Step 2.5: International Transfer Documentation (Art. 30(1)(e))

1. Determine whether any data leaves the EEA at any point in the processing chain.
2. Include remote access from third countries (e.g., offshore IT support accessing EU systems).
3. For each transfer, identify and document the transfer mechanism.
4. For transfers relying on SCCs, confirm a Transfer Impact Assessment has been conducted.
5. Monitor the EU adequacy decision list for any changes affecting current transfer mechanisms.

#### Step 2.6: Retention Period Specification (Art. 30(1)(f))

1. Identify the applicable legal retention obligation, if any (tax law, employment law, sector regulation).
2. Where no legal obligation exists, apply the data minimisation principle: retain only as long as necessary for the stated purpose.
3. Express retention as a specific duration with a clear trigger (e.g., "6 months from date of application decision" not "6 months").
4. Where different data categories within the same activity have different retention needs, document each separately.
5. Specify the deletion or anonymisation method.

#### Step 2.7: Security Measures Description (Art. 30(1)(g))

1. Document both technical and organisational measures at a general level.
2. Reference the organisation's ISMS controls without disclosing specific configurations that could create security risks.
3. Include encryption standards, access control mechanisms, backup procedures, incident response capabilities, and staff training.
4. Cross-reference with the most recent security audit or certification (ISO 27001, SOC 2).

### Phase 3: Quality Assurance

1. **Completeness check**: Verify all seven mandatory fields are populated for every RoPA entry using the validation script.
2. **Consistency check**: Ensure purposes, lawful bases, and privacy notice disclosures are aligned across related entries.
3. **Accuracy check**: Sample 20% of entries and verify data flows against actual system behaviour through technical inspection.
4. **DPO review**: The DPO reviews all entries for legal accuracy and regulatory alignment.
5. **Processing owner sign-off**: Each business owner confirms the factual accuracy of their entries.

### Phase 4: Registration and Governance

1. Enter all validated entries into the organisation's RoPA management system.
2. Set individual review dates (maximum 12 months, shorter for high-risk processing).
3. Establish change triggers: new system deployment, organisational restructuring, new vendor engagement, regulatory change, or data breach involving the processing activity.
4. Assign ongoing maintenance responsibilities to processing owners with DPO oversight.
5. Configure automated reminders for upcoming review dates.

## RACI Matrix for RoPA Creation

| Activity | Responsible | Accountable | Consulted | Informed |
|----------|------------|-------------|-----------|----------|
| Processing activity discovery | DPO Office | DPO | Business unit heads | Board/senior management |
| Data collection interviews | DPO Office / Privacy team | DPO | Processing owners, IT | Legal |
| Draft RoPA entry | Privacy analyst | DPO | Processing owner | IT security |
| Legal review (purposes, lawful basis) | DPO | DPO | External counsel (if needed) | Processing owner |
| Technical validation | IT security | CISO | DPO | Processing owner |
| Final approval | Processing owner | DPO | Legal, IT | Senior management |
| Entry into RoPA system | Privacy analyst | DPO | IT | Processing owner |
| Ongoing maintenance | Processing owner | DPO | Privacy team | IT, Legal |

## Interview Question Template

Use these questions during departmental data collection:

1. What personal data does your team collect or receive, and from whom?
2. Why do you collect this data — what is the specific business purpose?
3. Where is this data stored (systems, databases, spreadsheets, paper files)?
4. Who within the organisation can access this data?
5. Do you share this data with any external parties? If so, who and why?
6. Does this data leave the EU/EEA at any point, including via cloud services or remote access?
7. How long do you keep this data, and what triggers deletion?
8. What security measures protect this data?
9. Has anything changed about this processing in the past 12 months?
10. Are there any planned changes to this processing in the next 12 months?
