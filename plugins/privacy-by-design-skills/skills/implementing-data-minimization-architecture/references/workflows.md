# Data Minimization Architecture Workflows

## Workflow 1: New Processing Activity — Minimization Review

```
Step 1: Data Inventory
├── List all personal data fields proposed for collection
├── Map each field to a specific, documented processing purpose
└── Identify the lawful basis under Article 6(1) for each field

Step 2: Necessity Assessment
├── For each field, answer: "Can the purpose be achieved without this field?"
├── For each field, answer: "Can a less identifying alternative achieve the same result?"
├── Score each field using the Data Minimization Assessment Matrix
└── Document justification for fields scoring 9-12

Step 3: Technical Controls Selection
├── Fields scoring 0-4: Eliminate from collection or aggregate at source
├── Fields scoring 5-8: Apply pseudonymization, masking, or field-level encryption
├── Fields scoring 9-12: Implement field-level encryption + strict RBAC + audit logging
└── Generate technical specification for selected controls

Step 4: Implementation
├── Configure API gateway allowlists for collection endpoints
├── Deploy pseudonymization transforms at ingestion boundary
├── Configure field-level encryption with per-field DEKs
├── Set up dynamic masking rules for non-privileged access
└── Implement automated data lifecycle policies (TTL, archival, deletion)

Step 5: Validation
├── Verify no unauthorized fields pass API gateway validation
├── Confirm pseudonymized fields cannot be reversed without HSM access
├── Test dynamic masking for each user role
├── Verify encryption key separation between environments
└── Document residual risks and mitigations
```

## Workflow 2: Existing System — Minimization Audit

```
Step 1: Discovery
├── Scan database schemas for personal data fields
├── Map data flows between microservices using service mesh telemetry
├── Identify fields transmitted to third parties or external systems
└── Cross-reference with Article 30 Records of Processing Activities

Step 2: Gap Analysis
├── Compare collected fields against documented processing purposes
├── Identify fields collected but not used for any active purpose
├── Identify fields accessible to roles that do not require them
├── Identify fields stored beyond the defined retention period
└── Score each field using the Data Minimization Assessment Matrix

Step 3: Remediation Planning
├── Priority 1: Delete fields with no documented purpose (potential Art. 5(1)(b) violation)
├── Priority 2: Pseudonymize fields used only for analytics
├── Priority 3: Apply dynamic masking for support and operations roles
├── Priority 4: Implement field-level encryption for remaining sensitive fields
└── Assign remediation owners and target completion dates

Step 4: Execution
├── Execute database migrations to remove unnecessary columns
├── Deploy pseudonymization transforms for analytics pipelines
├── Configure dynamic masking policies in database proxy layer
├── Update API contracts to remove deprecated fields
└── Update Article 30 records to reflect reduced data scope

Step 5: Continuous Monitoring
├── Configure schema drift detection to alert on new personal data columns
├── Monitor API gateway logs for attempts to transmit non-allowlisted fields
├── Schedule quarterly minimization assessments for all processing activities
└── Report metrics: fields eliminated, fields pseudonymized, access scope reductions
```

## Workflow 3: Pseudonymization Key Lifecycle

```
Step 1: Key Generation
├── Generate HMAC-SHA256 keys in HSM (FIPS 140-2 Level 3)
├── Assign key identifiers with version suffix (e.g., PSE-CUST-v003)
├── Register key metadata in key management inventory
└── Set key rotation schedule (90-day default, configurable per data class)

Step 2: Key Distribution
├── Wrap key with KEK for transport to pseudonymization service
├── Load wrapped key into service memory; never persist to disk
├── Verify key integrity via HMAC check on load
└── Log key activation event with timestamp and service instance ID

Step 3: Key Rotation
├── Generate new key version in HSM
├── Run dual-key period: both old and new keys active for reads
├── Re-pseudonymize active records with new key version
├── Deactivate old key version after migration window closes
└── Log rotation completion and update key inventory

Step 4: Key Destruction
├── Triggered by retention period expiry or purpose completion
├── Destroy key material in HSM using zeroization command
├── Verify destruction via HSM audit log
├── Pseudonymized data becomes irreversibly anonymized (Recital 26 applies)
└── Update Article 30 records to reflect anonymization status
```
