# Breach Risk Assessment Workflow

## Phase 1: Initial Information Gathering (Within 4 Hours of Breach Awareness)

1. **Receive the breach incident report** from the SOC, IT security team, or processor notification. Verify the report includes: timestamp of discovery, systems affected, initial scope estimate, and whether the breach is contained.
2. **Confirm personal data involvement**: Determine whether the incident involves personal data as defined in Art. 4(1). If no personal data is involved, document the decision and close the privacy assessment (the incident may still require security incident response).
3. **Classify the breach type**: Determine whether the breach is a confidentiality, integrity, availability, or combined breach. Document the classification with supporting evidence.
4. **Identify affected data categories**: Work with the technical investigation team to determine which specific personal data fields were compromised. Distinguish between directly identifying data, indirectly identifying data, and special category data.
5. **Estimate affected population**: Obtain an initial estimate of the number of affected data subjects and their categories (customers, employees, patients, minors, etc.).

## Phase 2: Factor-by-Factor Scoring (Within 12 Hours of Breach Awareness)

### Factor 1: Data Sensitivity Assessment
1. Review the list of affected data categories identified in Phase 1.
2. Determine the highest sensitivity level present in the affected data:
   - Score 1: Only publicly available data or non-sensitive business contact information.
   - Score 2: Personal identifiers (email, phone) or behavioral data (purchase history, browsing).
   - Score 3: Financial data, government identifiers, employment records, location data.
   - Score 4: Art. 9 special categories, Art. 10 criminal data, authentication credentials, data enabling physical harm.
3. Document the scoring rationale with reference to the specific data categories involved.

### Factor 2: Volume Assessment
1. Obtain the current best estimate of affected data subjects from the investigation team.
2. Apply the volume scoring scale:
   - Score 1: Under 100 data subjects.
   - Score 2: 100 to 1,000 data subjects.
   - Score 3: 1,000 to 100,000 data subjects.
   - Score 4: Over 100,000 data subjects.
3. If the exact count is unknown, use the upper bound of the estimated range for scoring purposes (precautionary principle).

### Factor 3: Identifiability Assessment
1. Examine the combination of data elements exposed to determine how easily individuals can be identified.
2. Consider whether the data was pseudonymized, encrypted, or otherwise protected.
3. Apply the identifiability scoring scale:
   - Score 1: Data pseudonymized or encrypted; key not compromised.
   - Score 2: Indirect identifiers only; re-identification requires additional data.
   - Score 3: Direct identifiers present (name + one other element).
   - Score 4: Multiple direct identifiers, photographs, or biometric data.
4. If encryption was applied, verify: (a) the encryption standard (AES-256 or equivalent), (b) key management integrity, (c) whether the key was stored separately from the encrypted data.

### Factor 4: Consequence Severity Assessment
1. For each type of potential consequence, assess the realistic worst-case scenario:
   - Financial loss: Could the data be used to commit fraud or financial theft?
   - Identity theft: Does the combination of data elements enable identity impersonation?
   - Discrimination: Could the data reveal protected characteristics leading to discriminatory treatment?
   - Physical safety: Could the data be used to locate or harm individuals?
   - Reputational damage: Could disclosure of the data cause embarrassment or professional harm?
   - Emotional distress: Would a reasonable person experience significant distress upon learning of the breach?
2. Score based on the most severe realistic consequence.

### Factor 5: Individual Characteristics Assessment
1. Review the data subject categories identified in Phase 1.
2. Determine whether any vulnerable populations are represented:
   - Minors (under 18)
   - Patients or individuals with health conditions
   - Elderly individuals
   - Asylum seekers or refugees
   - Individuals in dependent relationships (employees, tenants, students)
   - Individuals whose physical safety depends on data confidentiality (domestic abuse survivors, witnesses)
3. Score based on the most vulnerable category present.

### Factor 6: Controller-Specific Factor Assessment
1. Consider the controller's role and the nature of the relationship with data subjects.
2. Evaluate whether the controller's position amplifies the potential harm:
   - Financial institutions: elevated responsibility for financial data security.
   - Healthcare providers: elevated responsibility for health data confidentiality.
   - Employers: power imbalance in employment relationship.
   - Government bodies: data subjects may have no choice about providing data.
   - Technology platforms: scale of processing amplifies impact.

## Phase 3: Threshold Determination (Within 24 Hours)

1. **Sum all factor scores** to produce the aggregate risk score (range: 6-24).
2. **Apply the threshold matrix**:
   - 6-8: Unlikely to result in risk. No Art. 33 notification required. Document in breach register.
   - 9-12: Likely to result in risk. Art. 33 notification required. Art. 34 not required.
   - 13-18: Approaching high risk. Art. 33 notification required. Art. 34 strongly recommended.
   - 19-24: Likely to result in high risk. Both Art. 33 and Art. 34 notification required.
3. **DPO review and recommendation**: Present the completed assessment to the DPO for review. The DPO provides a written recommendation concurring with or dissenting from the assessment.
4. **Management decision**: Senior management (at Stellar Payments Group: the General Counsel and CEO) make the final notification decision, documented with reasons if departing from the DPO recommendation.

## Phase 4: Documentation and Handoff

1. Complete the breach risk assessment form with all factor scores, rationale, threshold determination, DPO recommendation, and management decision.
2. File the assessment in the breach register under Art. 33(5).
3. If SA notification is required, hand off to the Art. 33 notification workflow.
4. If DS notification is required, hand off to the Art. 34 communication workflow.
5. Set a re-assessment trigger: if new information emerges (e.g., exfiltration confirmed, additional affected individuals identified), repeat the assessment with updated factor scores.

## Re-Assessment Triggers

The risk assessment must be repeated when:
- The scope of the breach increases (more data subjects or data categories identified)
- Data exfiltration is confirmed or ruled out after initial assessment
- Evidence emerges that compromised data has been misused
- A supplementary forensic report changes the understanding of the breach
- A supervisory authority requests additional information suggesting the initial assessment was insufficient
