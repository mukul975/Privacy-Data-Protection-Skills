# Data Flow Mapping Workflow Reference

## Full Inventory Workflow

### Phase 1: Planning (Week 1)

1. Define the scope: entire organisation or specific business unit/subsidiary.
2. Assemble the mapping team: DPO office, IT architecture, information security, business process owners.
3. Prepare the data collection template (system inventory questionnaire, data flow tracing form).
4. Schedule interviews with system owners and business process owners.
5. Obtain the current application inventory, vendor register, and network architecture diagrams.

### Phase 2: System Discovery (Weeks 2-3)

1. Start with the IT asset management system or application portfolio to enumerate all systems processing personal data.
2. For each system, complete the system inventory form:
   - System name and vendor
   - Hosting location (on-premise DC, cloud region, SaaS provider)
   - Data categories processed
   - Data subjects categories
   - System owner and business function
   - Integration points (APIs, file transfers, database links, email)
3. Identify SaaS applications using CASB logs or shadow IT discovery.
4. Include development, testing, and staging environments if they contain personal data (even pseudonymised or test data derived from production).

### Phase 3: Flow Tracing (Weeks 3-5)

For each system:
1. **Inbound flows**: Trace every source of personal data entering the system. For each source, document: source system, source country, data categories, transfer method (API, SFTP, email, manual).
2. **Processing locations**: Document all locations where the data is stored or processed: primary DC, DR site, CDN nodes, backup locations.
3. **Outbound flows**: Trace every destination receiving personal data from the system. For each destination, document: destination system, destination country, recipient identity, data categories, transfer method.
4. **Sub-processor chains**: For SaaS and processor relationships, request the sub-processor list and document the data processing locations of each sub-processor.
5. **Support access**: Document any remote access by vendor support staff from third countries.

### Phase 4: Third-Party Cataloguing (Week 5)

1. Consolidate all third-party recipients identified during flow tracing.
2. For each third party: legal name, country, role (processor, sub-processor, joint controller, independent controller), data received, purpose, contract reference.
3. Cross-reference against the vendor register and DPA register.
4. Identify any third parties receiving data without a documented contractual arrangement.

### Phase 5: Mechanism Assignment (Week 6)

1. For each cross-border flow, determine the applicable transfer mechanism using the decision tree.
2. Verify the mechanism is valid (adequacy decision current, SCCs executed, DPF certification active).
3. Verify supporting documentation exists (TIA for SCCs, DPF verification record).
4. Record the mechanism assignment in the flow register.

### Phase 6: Gap Analysis (Week 7)

1. Identify all flows without a valid transfer mechanism (critical gaps).
2. Identify all flows with mechanisms but missing TIAs or expired documentation (high gaps).
3. Identify all undocumented flows discovered during mapping (high gaps).
4. Prioritise gaps by risk: data sensitivity, transfer volume, destination country risk.
5. Create the remediation plan with owners, deadlines, and tracking.

### Phase 7: Reporting and Integration (Week 8)

1. Produce the data flow inventory report with:
   - Executive summary (total flows, flows by mechanism, flows by country, gaps identified)
   - Detailed flow register
   - Gap analysis and remediation plan
   - Visualisations (geo-map, system diagram)
2. Integrate findings into:
   - Art. 30 Records of Processing Activities
   - Transfer register
   - Vendor management system
   - DPIA register (for high-risk transfers)
3. Present findings to the data protection steering committee.
4. Set the next full inventory review date (12 months).

## Ongoing Maintenance Workflow

### Trigger-Based Updates

| Trigger | Action | Timeline |
|---------|--------|----------|
| New system procurement | Complete system inventory and flow tracing forms | Before system go-live |
| New vendor onboarding | Add to third-party register; identify cross-border flows | Before data sharing begins |
| System decommissioning | Remove system from inventory; verify data deletion; update flow register | Within 30 days |
| Corporate restructuring (M&A, subsidiary changes) | Re-map affected entity data flows; update transfer mechanisms | Within 90 days |
| New country operations | Map all data flows to/from new country; establish transfer mechanisms | Before operations commence |
| Adequacy decision change | Re-assess all flows to affected country; update mechanisms if needed | Within 30 days |

### Quarterly Review

1. Review the flow register for accuracy against recent system changes.
2. Check for new SaaS subscriptions not captured in the inventory.
3. Verify transfer mechanism validity (certification expiry, SCC review dates).
4. Update the gap tracker for remediation progress.

### Annual Full Review

1. Repeat the full inventory process (Phases 1-7) on a compressed timeline (4 weeks for organisations with a mature baseline).
2. Compare against the prior year's inventory to identify changes.
3. Report year-over-year trends to the steering committee.
