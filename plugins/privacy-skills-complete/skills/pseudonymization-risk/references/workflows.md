# Pseudonymization and Re-Identification Risk Workflows

## Workflow 1: Selecting a Pseudonymization Technique

```
Step 1: Identify Data Elements
├── Catalog all personal data fields in the processing activity
├── Classify each field:
│   ├── Direct identifiers (name, email, SSN, phone)
│   ├── Quasi-identifiers (age, ZIP, gender, job title)
│   └── Sensitive attributes (health data, political opinion, religion)
├── Map data flows: where each field is collected, stored, processed, shared
└── Document the purpose for processing each field

Step 2: Define Pseudonymization Requirements
├── Determine reversibility requirement:
│   ├── Must be reversible (e.g., support re-identification for DSAR)
│   ├── Should be reversible (e.g., analytics with re-contact capability)
│   └── Must NOT be reversible (e.g., test environments, public releases)
├── Determine linkability requirement:
│   ├── Must link records within same dataset (e.g., longitudinal analytics)
│   ├── Must link records across datasets (e.g., cross-system reconciliation)
│   └── Must NOT link records (e.g., independent research releases)
├── Determine format requirements:
│   ├── Format preservation needed (e.g., phone numbers must remain numeric)
│   └── Format change acceptable (e.g., UUIDs replacing names)
└── Document performance and latency constraints

Step 3: Select Technique
├── If irreversible + unlinkable → Synthetic data replacement
├── If reversible + linkable within dataset → Counter-based (lookup table)
├── If reversible + linkable across datasets → HMAC with shared key
├── If reversible + format-preserving → Format-preserving encryption (FF3-1)
├── If reversible + centralized vault → Tokenization
├── If high-volume real-time → HMAC (no vault latency)
└── Document selection rationale referencing ENISA technique categories

Step 4: Implementation
├── Generate or provision cryptographic keys / tokens / mapping tables
├── Implement pseudonymization at the data collection boundary
├── Store the "additional information" (Art. 4(5)) separately:
│   ├── Mapping tables → HSM-backed database with DPO-only access
│   ├── HMAC keys → AWS KMS / Azure Key Vault with restricted IAM
│   └── Encryption keys → Dedicated key management system
├── Implement access controls on the additional information
├── Enable audit logging for all pseudonymization/de-pseudonymization operations
└── Test with representative data to verify correctness and performance

Step 5: Validation
├── Verify pseudonymized output cannot be reversed without additional information
├── Verify deterministic techniques produce consistent results
├── Verify format-preserving techniques maintain expected format
├── Run re-identification risk assessment (see Workflow 2)
├── Document residual risk level and acceptance decision
└── DPO sign-off on technique selection and residual risk
```

## Workflow 2: Conducting Re-Identification Risk Assessment

```
Step 1: Dataset Characterization
├── Count total records (n)
├── Identify all quasi-identifiers present in the pseudonymized dataset
├── For each quasi-identifier, determine:
│   ├── Number of distinct values
│   ├── Value distribution (uniform vs. skewed)
│   └── Granularity level (exact vs. generalized)
├── Compute equivalence classes based on quasi-identifier combinations
├── Record the smallest equivalence class size (k_min)
└── Record the average equivalence class size (k_avg)

Step 2: Threat Model Selection
├── Identify the most relevant attacker model:
│   ├── Prosecutor: attacker knows target is in dataset, tries to find record
│   │   └── Risk metric: 1/k_min (worst case)
│   ├── Journalist: attacker tries to re-identify anyone for publicity
│   │   └── Risk metric: max(1/k_i) across all equivalence classes
│   └── Marketer: attacker tries to re-identify as many people as possible
│       └── Risk metric: (1/n) × Σ(1/k_i) (average re-identification probability)
├── Consider the motivated intruder test:
│   ├── What auxiliary data sources are publicly available?
│   ├── Can voter rolls, social media, company directories be linked?
│   └── Are there known data breaches containing overlapping fields?
└── Document the selected threat model and justification

Step 3: Quantitative Risk Calculation
├── Compute prosecutor risk: R_prosecutor = 1 / k_min
├── Compute journalist risk: R_journalist = max(1/k_i) for all equivalence classes
├── Compute marketer risk: R_marketer = (1/n) × Σ(1/k_i)
├── Apply the motivated intruder amplification factor:
│   ├── Low auxiliary data availability: factor = 1.0
│   ├── Moderate auxiliary data: factor = 1.5
│   └── High auxiliary data (public registers, social media): factor = 2.0
├── Adjusted risk = max(R_prosecutor, R_journalist, R_marketer) × amplification factor
└── Record the adjusted risk score

Step 4: Linkage Attack Evaluation
├── Record linkage test:
│   ├── Attempt to match pseudonymized records with external identified datasets
│   ├── Use probabilistic record linkage on quasi-identifiers
│   └── Record match rate and confidence levels
├── Attribute linkage test:
│   ├── Check l-diversity of sensitive attributes within each equivalence class
│   ├── If l < 3, attribute linkage risk is HIGH
│   └── Record l-diversity score
├── Membership inference test:
│   ├── Can an attacker determine if a specific individual is in the dataset?
│   └── Check t-closeness of sensitive attribute distributions
└── Document all linkage attack results

Step 5: Risk Classification
├── Map adjusted risk score to classification:
│   ├── 0-15%: LOW — acceptable with monitoring
│   ├── 16-35%: MODERATE — additional controls recommended
│   ├── 36-60%: HIGH — technique upgrade or data reduction required
│   └── 61-100%: VERY HIGH — do not release without anonymization
├── For MODERATE or higher: specify required mitigations
├── For HIGH or higher: escalate to DPO for risk acceptance decision
└── Document risk classification and mitigation plan

Step 6: Ongoing Monitoring
├── Schedule re-assessment quarterly and upon:
│   ├── New auxiliary data sources becoming available
│   ├── Data breaches affecting linked datasets
│   ├── Changes to quasi-identifier granularity
│   └── New data releases from the same population
├── Monitor re-identification research publications for new attack techniques
├── Update risk assessment when external data landscape changes
└── Report re-identification risk metrics to DPO quarterly
```

## Workflow 3: Pseudonymization Technique Audit

```
Step 1: Inventory
├── List all pseudonymization implementations in the organization
├── For each implementation, document:
│   ├── Data flow name and processing activity
│   ├── Technique used (counter, HMAC, encryption, tokenization, synthetic)
│   ├── Key/mapping table storage location
│   ├── Access controls on additional information
│   └── Last audit date
└── Identify implementations without documentation

Step 2: Key Management Review
├── Verify that keys/mapping tables are stored separately from pseudonymized data
├── Verify that access to additional information requires:
│   ├── Role-based authorization (DPO, privacy engineering)
│   ├── Multi-factor authentication
│   └── Documented justification
├── Verify key rotation schedule is followed:
│   ├── HMAC keys: quarterly rotation recommended
│   ├── Encryption keys: per organizational key management policy
│   └── Token vaults: annual access control review
├── Verify key backup and disaster recovery procedures
└── Document any deviations from key management policy

Step 3: Implementation Verification
├── Test deterministic techniques for consistency:
│   └── Same input + same key → same pseudonym
├── Test format-preserving encryption for format correctness:
│   └── Pseudonymized output matches original format constraints
├── Test tokenization for vault integrity:
│   └── All tokens resolve to valid original values
├── Verify no plaintext identifiers leak into:
│   ├── Application logs
│   ├── Error messages
│   ├── Database query logs
│   └── Analytics event payloads
└── Document verification results

Step 4: Remediation
├── For each finding:
│   ├── Classify severity (critical, high, medium, low)
│   ├── Assign remediation owner
│   ├── Set remediation deadline
│   └── Track to completion
├── Common remediations:
│   ├── Migrate from unhashed to HMAC-based pseudonymization
│   ├── Implement key rotation for stale keys
│   ├── Add access logging for additional information access
│   └── Separate mapping tables from pseudonymized data stores
└── Report audit findings and remediation status to DPO
```
