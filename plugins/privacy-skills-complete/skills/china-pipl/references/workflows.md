# PIPL Compliance Workflow Reference

## Workflow 1: Cross-Border Transfer Assessment

### Step 1 — Determine Applicability
1. Identify whether personal information is being transferred outside the PRC.
2. Confirm the transfer involves personal information of natural persons within the PRC.
3. Determine whether the processor is a CIIO — if yes, mandatory CAC security assessment (no alternatives).
4. If not a CIIO, proceed to threshold assessment.

### Step 2 — Threshold Assessment for Mechanism Selection
1. Count the total number of individuals whose personal information the processor handles:
   - 1 million or more → CAC security assessment mandatory
   - Fewer than 1 million → proceed to cumulative transfer count
2. Count cumulative cross-border transfers since 1 January of the preceding year:
   - 100,000 or more individuals → CAC security assessment mandatory
   - Fewer than 100,000 → proceed to sensitive PI check
3. Count cumulative cross-border transfers of sensitive personal information:
   - 10,000 or more individuals → CAC security assessment mandatory
   - Fewer than 10,000 → eligible for standard contract or certification

### Step 3 — Exemption Check (March 2024 Relaxation)
1. Assess whether the contract/HR necessity exemption applies (transfer necessary for contract with the individual or HR management).
2. Assess whether the small volume exemption applies (<100,000 non-sensitive PI within one year).
3. Assess whether the free trade zone negative list exemption applies.
4. If an exemption applies, document the basis and proceed without CAC assessment, standard contract, or certification.

### Step 4 — Execute Selected Mechanism

**CAC Security Assessment**:
1. Conduct self-assessment (PIPIA) per Art. 55-56.
2. Prepare application materials: self-assessment report, legal documents with overseas recipient, data export descriptions.
3. Submit application through the provincial CAC office.
4. Respond to CAC questions within the 45+15 working day review period.
5. Receive assessment result; implement any conditions imposed.
6. Record the assessment validity period (2 years); calendar the renewal date.

**Standard Contract**:
1. Conduct PIPIA per Art. 55-56.
2. Execute the CAC-published standard contract text (no modifications permitted to the standard terms).
3. Complete the annexes with transfer-specific details (data types, purposes, security measures).
4. File the executed contract with the provincial CAC office within 10 working days.
5. Retain filing confirmation and PIPIA report for at least 3 years.

**Certification**:
1. Both parties jointly engage an accredited certification body.
2. Submit documentation of PI protection policies and cross-border processing arrangements.
3. Certification body conducts review (typically 3-6 months).
4. Upon certification, both parties accept ongoing supervision.
5. Annual supervision audits; certification valid for 3 years.

### Step 5 — Obtain Separate Consent (Art. 39)
1. Inform the individual of: the overseas recipient's name, contact information, processing purpose, processing method, and categories of personal information.
2. Inform the individual of the method and procedure for exercising rights with the overseas recipient.
3. Obtain separate consent specifically for the cross-border transfer (distinct from general processing consent).
4. Record the consent with timestamp, scope, and version.

## Workflow 2: Separate Consent Collection

### Step 1 — Identify Trigger
1. Review the processing activity against the five separate consent triggers:
   - Art. 23: Providing PI to another processor
   - Art. 25: Public disclosure of PI
   - Art. 26: Processing public surveillance images for non-security purposes
   - Art. 29: Processing sensitive personal information
   - Art. 39: Cross-border transfer of PI
2. If multiple triggers apply to a single processing activity, each trigger requires its own separate consent element.

### Step 2 — Design Consent Mechanism
1. Create a dedicated consent interface separate from general consent collection.
2. Include all information required by the specific PIPL provision:
   - For Art. 23 (sharing): Identity of recipient, processing purpose, PI categories, individual rights with recipient
   - For Art. 29 (sensitive PI): Necessity of processing, impact on individual rights, categories of sensitive PI
   - For Art. 39 (cross-border): Overseas recipient details, processing purpose/method, rights exercise procedure
3. Ensure the consent mechanism requires a clear affirmative action (no default selection, no bundling).
4. Provide a withdrawal mechanism on the same interface.

### Step 3 — Record and Maintain
1. Store the consent record with: individual identifier, consent timestamp, specific trigger article, consent scope, version of notice shown, IP address, device identifier (if applicable).
2. Link the consent record to the specific processing activity in the PI processing register.
3. Schedule periodic review of consent validity (at least annually or upon processing change).
4. If consent is withdrawn, cease the specific processing activity within the defined timeframe (typically 15 working days).

## Workflow 3: Personal Information Protection Impact Assessment (PIPIA)

### Step 1 — Determine Mandatory Triggers
1. Check Art. 55 triggers:
   - Processing sensitive personal information
   - Using PI for automated decision-making
   - Entrusting processing to a third party
   - Providing PI to another processor
   - Cross-border transfer of PI
   - Other processing significantly impacting individual rights
2. If any trigger is met, PIPIA is mandatory before the processing activity commences.

### Step 2 — Conduct Assessment
1. **Legality and legitimacy review**:
   - Verify the processing purpose is lawful, specific, and clear
   - Confirm the lawful basis under Art. 13 is applicable
   - Verify that the PI collected is the minimum necessary for the stated purpose
2. **Impact on individual rights**:
   - Assess the potential for harm (financial loss, reputational damage, discrimination, physical harm)
   - Evaluate the scope and severity of potential impact
   - Consider the vulnerability of affected individuals (minors, elderly, employees)
3. **Security measures evaluation**:
   - Document technical measures (encryption, access control, de-identification)
   - Document organisational measures (policies, training, incident response)
   - Assess whether measures are proportionate to the identified risks
4. **Risk identification and mitigation**:
   - Identify residual risks after security measures
   - Propose additional mitigation measures for unacceptable risks
   - If risks cannot be mitigated to an acceptable level, recommend against the processing

### Step 3 — Document and Retain
1. Produce the PIPIA report documenting all assessment elements.
2. Obtain sign-off from the personal information protection responsible person.
3. Retain the PIPIA report and related processing records for at least 3 years (Art. 56).
4. Schedule review upon material changes to the processing activity or regulatory environment.

## Workflow 4: Individual Rights Response

### Receipt (Day 0)
1. Individual submits request through the privacy portal, customer service, or written correspondence.
2. System assigns a tracking identifier.
3. Verify the requestor's identity through the PRC-standard verification method (ID verification, phone verification, or account authentication).

### Assessment (Days 1-5)
1. Classify the right being exercised (access, copy, portability, correction, deletion, explanation, automated decision objection).
2. Identify all systems processing the individual's personal information.
3. Assess whether any exemptions apply:
   - Art. 44: Rights may be restricted where laws/administrative regulations provide
   - Art. 47(2): Deletion not required if retention period has not expired
   - Art. 47(3): Deletion may be replaced with cessation of processing (except storage) if deletion is technically difficult

### Fulfilment (Days 6-12)
1. **Access/Copy (Art. 45)**: Generate a comprehensive data export in a commonly used format.
2. **Portability (Art. 45(3))**: Transfer data to the designated processor per CAC-specified conditions (when implemented).
3. **Correction (Art. 46)**: Update records; notify relevant recipients.
4. **Deletion (Art. 47)**: Execute deletion workflows; where technically difficult, cease processing except storage and inform individual.
5. **Explanation (Art. 48)**: Prepare clear description of processing rules and individual rights exercise procedures.
6. **Automated decision (Art. 24)**: Provide explanation of the automated decision logic; offer alternative non-automated decision method.

### Response (Days 13-15)
1. Deliver the response in a clear, understandable format in Simplified Chinese.
2. The PIPL does not specify a hard deadline, but GB/T 35273-2020 recommends within 15 working days (30 working days for complex requests).
3. If the request is refused, provide reasons and inform of the right to file a complaint with the CAC.
4. Record the response in the individual rights request log.
