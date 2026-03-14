# Transfer Impact Assessment Workflow Reference

## TIA Initiation Workflow

### Trigger Events

A TIA must be conducted:
1. Before commencing any new transfer relying on Art. 46 safeguards (SCCs, BCRs, ad hoc clauses).
2. When renewing or amending existing SCCs or BCRs.
3. When the destination country enacts new surveillance legislation.
4. When a court ruling in the destination country affects government access powers.
5. When the EDPB, EC, or national SA issues updated guidance on the destination country.
6. At the scheduled annual review date for existing TIAs.
7. When a government access request is received by the data importer.
8. When the data categories, volume, or sensitivity of the transfer materially changes.

### Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| Data Protection Officer | Overall accountability for TIA programme; final sign-off on TIA conclusions |
| Privacy Legal Counsel | Legal analysis of destination country laws; assessment of European Essential Guarantees |
| Information Security Manager | Assessment and design of technical supplementary measures |
| Business Process Owner | Provision of transfer details (Step 1 mapping); implementation of organisational measures |
| External Counsel (destination country) | Expert opinion on local surveillance and government access laws |

## Step-by-Step TIA Workflow

### Step 1: Transfer Mapping (Days 1-5)

1. Identify the specific transfer or group of related transfers to be assessed.
2. Document all elements required by the EDPB Step 1: exporter, importer, mechanism, data categories, subjects, purposes, destination, onward transfers, format, retention.
3. Obtain the data flow diagram from the IT architecture team.
4. Confirm the current transfer mechanism and its specific clauses.
5. Record the TIA reference number and assessment date in the TIA register.

### Step 2: Transfer Tool Confirmation (Days 5-7)

1. Confirm the Art. 46 transfer mechanism in place.
2. Verify the mechanism is properly executed (SCCs signed, BCRs approved).
3. Identify the specific clauses that may be affected by destination country law (Clause 14/15 for SCCs).
4. Confirm that the mechanism is current (SCCs version 2021/914; not legacy SCCs).
5. If no valid mechanism is in place, halt the transfer until one is established.

### Step 3: Destination Country Assessment (Days 7-30)

#### Phase 3a: Identify Relevant Laws

1. Conduct legal research to identify all laws in the destination country that authorise government access to personal data:
   - National security and intelligence legislation
   - Law enforcement access legislation
   - Telecommunications interception laws
   - Anti-terrorism legislation
   - Cybersecurity laws with data access provisions
2. Engage local counsel if in-house expertise is insufficient.
3. Document each identified law with: title, statutory reference, date of enactment, scope, and relevant provisions.

#### Phase 3b: Apply European Essential Guarantees

For each identified law, assess against the four EEGs:

**EEG 1 — Clear, Precise, Accessible Rules**:
- Is the law publicly available and accessible?
- Does it clearly define the scope, conditions, and limits of government access?
- Are the categories of data and persons subject to access specified?

**EEG 2 — Necessity and Proportionality**:
- Does the law require a showing of necessity for each access request?
- Is the scope of access proportionate to the stated objective?
- Are there safeguards against bulk or untargeted access?
- Are minimisation and retention limits specified?

**EEG 3 — Independent Oversight**:
- Is there prior judicial or independent authorisation required?
- Is there ongoing independent oversight of access activities?
- Is the oversight body genuinely independent from the executive?

**EEG 4 — Effective Remedies**:
- Can individuals challenge access in court or before an independent body?
- Is there a notification mechanism (even if delayed)?
- Are effective remedies available (compensation, deletion, injunctive relief)?

#### Phase 3c: Assess Practical Risk

Beyond the legal framework, assess the practical likelihood of government access:
- Volume and sensitivity of the transferred data
- Nature of the importer (tech company vs. logistics operator)
- Historical evidence of government access requests to the importer or sector
- Importer's experience and track record with government requests
- Technical architecture (does the importer have access to plaintext data?)

#### Phase 3d: Reach a Preliminary Conclusion

Based on the legal and practical assessment, conclude:
1. **Green**: The legal framework provides essentially equivalent protection; no supplementary measures needed (rare for non-adequate countries).
2. **Amber**: Protection gaps exist but can be effectively bridged with supplementary measures — proceed to Step 4.
3. **Red**: Protection gaps cannot be effectively bridged with any supplementary measures — transfer must be suspended.

### Step 4: Supplementary Measures Design (Days 30-45)

If Step 3 conclusion is Amber:

1. Identify specific protection gaps from the EEG analysis.
2. For each gap, select supplementary measures from the EDPB Annex 2 catalogue:
   - **Technical**: Encryption, pseudonymisation, split processing, anonymisation
   - **Contractual**: Challenge obligations, transparency, audit rights, warrant canary
   - **Organisational**: Access policies, training, transparency reports, DPIA for government access scenarios
3. Assess the effectiveness of each selected measure against the specific gap it is intended to address.
4. Document why the combination of measures is sufficient to bridge the identified gap.
5. If no combination of measures is effective, the conclusion must change to Red.

### Step 5: Implementation (Days 45-60)

1. Implement technical measures (deploy encryption, configure pseudonymisation).
2. Execute contractual amendments incorporating supplementary measure obligations.
3. Deploy organisational measures (update policies, conduct training).
4. Verify the importer has implemented its portion of the supplementary measures.
5. Document the implementation status of each measure.

### Step 6: Monitoring and Re-Evaluation (Ongoing)

1. Set the next re-evaluation date (12 months from completion, unless a trigger event occurs sooner).
2. Subscribe to legal monitoring services for the destination country.
3. Monitor EDPB, EC, and national SA publications for updated guidance.
4. If a trigger event occurs, initiate an ad hoc re-evaluation.
5. Document each re-evaluation in the TIA version history.

## TIA Quality Assurance

1. All TIAs must be reviewed by the DPO before finalisation.
2. TIAs for high-risk transfers (special category data, large-scale transfers, sensitive jurisdictions) must be reviewed by external privacy counsel.
3. TIA conclusions must be consistent across similar transfers to the same jurisdiction.
4. Maintain a TIA library enabling reuse of country assessments across multiple transfers.
5. Ensure all TIAs are available for supervisory authority inspection within 48 hours of request.
