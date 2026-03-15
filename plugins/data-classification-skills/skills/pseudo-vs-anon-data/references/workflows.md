# Workflows — Pseudonymised vs Anonymised Data Classification

## Workflow 1: Anonymisation Adequacy Assessment

### Purpose
Determine whether a de-identified dataset qualifies as anonymised (GDPR does not apply) or remains pseudonymised (GDPR applies in full).

### Process Flow

```
START: De-identified dataset requires classification
  │
  ├─► Step 1: Document the De-identification Technique
  │     - What technique was applied? (tokenisation, hashing, encryption,
  │       k-anonymity, differential privacy, aggregation, suppression)
  │     - Was a re-identification key/mapping created?
  │     - Who holds the key? (same controller, separate entity, destroyed?)
  │     - What quasi-identifiers remain in the dataset?
  │     Output: De-identification technique documentation
  │
  ├─► Step 2: Re-identification Key Assessment
  │     IF a re-identification key exists AND is accessible to the controller
  │       → PSEUDONYMISED (personal data). Assessment complete.
  │     IF key was destroyed with verified evidence
  │       → Continue to Step 3
  │     IF key held by independent third party with no legal means of access
  │       → Continue to Step 3 (but note Breyer relative approach)
  │     Output: Key existence determination
  │
  ├─► Step 3: WP29 Three-Criteria Test
  │
  │     3a. SINGLING OUT TEST
  │     - List all quasi-identifiers remaining in the dataset
  │     - Calculate k-anonymity: for each combination of quasi-identifiers,
  │       how many records share the same values?
  │     - If k < 5 for any group: singling out is POSSIBLE
  │     - Consider external data that could be combined
  │     Result: PASS (k ≥ 5 for all groups) / FAIL (k < 5 for any group)
  │
  │     3b. LINKABILITY TEST
  │     - Can records in this dataset be linked to records in another dataset
  │       to identify individuals?
  │     - Check for consistent identifiers across datasets (hashed emails,
  │       timestamps, rare attribute combinations)
  │     - Check for sequential patterns enabling re-linking
  │     Result: PASS (no feasible linkage) / FAIL (linkage possible)
  │
  │     3c. INFERENCE TEST
  │     - Can the value of a sensitive attribute be inferred for a specific
  │       individual from the remaining data?
  │     - Check for homogeneity within k-anonymous groups (l-diversity)
  │     - Check for statistical inference from small groups
  │     Result: PASS (no feasible inference) / FAIL (inference possible)
  │
  │     IF ANY test FAILS → PSEUDONYMISED (personal data)
  │     IF ALL tests PASS → Continue to Step 4
  │
  ├─► Step 4: Motivated Intruder Test (ICO)
  │     Scenario: A person with no specialist knowledge but reasonable
  │     motivation, with access to:
  │     - This dataset
  │     - Public internet, social media, public registers
  │     - General computing tools (spreadsheets, databases)
  │     - Willing to invest days (not months) of effort
  │
  │     Could this person identify any individual in the dataset?
  │     YES → PSEUDONYMISED (personal data)
  │     NO  → Continue to Step 5
  │
  ├─► Step 5: Technology Horizon Assessment
  │     - What is the intended retention period for this dataset?
  │     - Are there foreseeable technological developments that could
  │       enable re-identification within this period?
  │       (e.g., advances in de-anonymisation algorithms, quantum computing
  │       threatening hash functions, expansion of public data sources)
  │     - Document the assessment and set a reassessment trigger
  │
  │     IF technology risk exists → PSEUDONYMISED (or set review date)
  │     IF no foreseeable risk → Continue to Step 6
  │
  └─► Step 6: Classification Decision
        CLASSIFICATION: ANONYMISED
        - Document: technique, three-criteria results, motivated intruder
          assessment, technology projection, assessor, date
        - DPO review and sign-off required
        - Set annual reassessment date
        - If shared externally: note that classification is from controller's
          perspective; recipient may need independent assessment
        Output: Anonymisation assessment record (signed by DPO)
```

## Workflow 2: Pseudonymisation Implementation Review

### Purpose
Validate that pseudonymisation measures meet Art. 4(5) requirements and provide adequate safeguards.

### Process Flow

```
START: System implements pseudonymisation for personal data
  │
  ├─► Step 1: Technique Validation
  │     - Verify the pseudonymisation technique is appropriate:
  │       • Tokenisation: mapping table securely stored?
  │       • Hashing: salted? (unsalted hashes vulnerable to rainbow tables)
  │       • Encryption: key management meets NIST/ISO 27001 standards?
  │       • Counter-based: no predictable sequence enabling reverse engineering?
  │     Output: Technique validation record
  │
  ├─► Step 2: Key Separation Verification
  │     Art. 4(5) requires "additional information is kept separately":
  │     - Is the re-identification key stored in a separate system?
  │     - Is the key on a separate network segment?
  │     - Are different access controls applied to key vs. data?
  │     - Is there logical or physical separation?
  │     Output: Key separation assessment
  │
  ├─► Step 3: Access Control Verification
  │     Art. 4(5) requires "technical and organisational measures":
  │     - Who can access the pseudonymised data? (list roles)
  │     - Who can access the re-identification key? (list roles)
  │     - Is there dual-person control for re-identification?
  │     - Are there audit logs for all access to both data and key?
  │     - Are there documented procedures for authorised re-identification?
  │     Output: Access control assessment
  │
  ├─► Step 4: Re-identification Risk Assessment
  │     Even with key separation, assess residual re-identification risk:
  │     - Could the pseudonymised data be re-identified WITHOUT the key?
  │       (unique attribute combinations, small groups, temporal patterns)
  │     - What additional anonymisation would be needed to prevent this?
  │     Output: Residual risk assessment
  │
  └─► Step 5: Documentation and Classification
        - Classify data as PSEUDONYMISED (personal data, GDPR applies)
        - Document pseudonymisation as Art. 32 security measure
        - Document as Art. 25 data protection by design measure
        - Note in RoPA that pseudonymisation is applied
        - Retain assessment for accountability (Art. 5(2))
        Output: Pseudonymisation assessment record
```
