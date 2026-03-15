# Data Protection by Default Workflows

## Workflow 1: Implementing By-Default Controls in a New Product

```
Step 1: Default Configuration Design
├── List all personal data fields the product could collect
├── Classify each field as: mandatory (core purpose) or optional (secondary)
├── For mandatory fields: document the necessity justification
├── For optional fields: design opt-in mechanism (consent toggle, feature activation)
├── Define the default state for each processing activity:
│   ├── Core service delivery: ON (contractual basis)
│   ├── Analytics: OFF (requires consent)
│   ├── Marketing: OFF (requires consent)
│   ├── Profiling: OFF (requires explicit consent)
│   └── Third-party sharing: OFF (requires consent)
└── Document the default configuration in the product privacy specification

Step 2: UI/UX Implementation
├── Design consent toggles with OFF as default state
├── Ensure "Accept" and "Reject" buttons have equal visual prominence
├── Implement progressive disclosure for optional data fields
├── Design privacy preference center accessible from main navigation
├── Implement just-in-time consent for feature-activated data collection
├── Verify no dark patterns (no trick questions, no visual manipulation)
└── Test with representative users for comprehension

Step 3: Backend Implementation
├── Configure API allowlists to reject non-mandatory fields
├── Implement TTL metadata on all database tables
├── Set default retention to shortest defensible period
├── Enable field-level encryption for PII columns
├── Configure dynamic masking rules for support dashboards
├── Deploy pseudonymization at analytics ingestion boundary
├── Configure access control with zero-default-access principle
└── Enable audit logging for all personal data access

Step 4: Verification
├── Create test accounts through standard registration
├── Verify: only mandatory fields collected
├── Verify: all consent toggles in OFF state
├── Verify: no marketing communications sent
├── Verify: support dashboard shows masked data
├── Verify: API rejects non-allowlisted fields
├── Verify: retention TTL correctly set
├── Document verification results
└── DPO sign-off on by-default compliance
```

## Workflow 2: Auditing Existing Products for By-Default Compliance

```
Step 1: Default State Inventory
├── Create a new user account through each registration channel
├── Document: which fields are requested, which are pre-filled, which are required
├── Document: state of all consent toggles and preferences
├── Document: which communications are received without opt-in
├── Document: what data is visible to support agents by default
└── Screenshot all default states as evidence

Step 2: Gap Identification
├── Compare default state against four dimensions:
│   ├── Amount: Are non-mandatory fields collected by default?
│   ├── Extent: Are secondary processing activities active by default?
│   ├── Period: Is the shortest retention applied by default?
│   └── Accessibility: Is data accessible to more roles than necessary?
├── For each gap, document:
│   ├── Current default state
│   ├── Required default state (per Art. 25(2))
│   ├── Remediation action
│   └── Priority (based on number of affected data subjects)
└── Generate gap report

Step 3: Remediation
├── Execute remediation in priority order
├── For UI changes: update consent toggles to OFF default
├── For backend changes: reconfigure data collection endpoints
├── For access changes: revoke unnecessary default access grants
├── For retention changes: apply shorter default TTL
├── Verify each remediation with test account
└── Update the by-default compliance register

Step 4: Ongoing Monitoring
├── Include by-default checks in CI/CD pipeline
├── Automated test: new account creation verifies default states
├── Quarterly: manual audit of consent toggle defaults
├── After each UI release: verify no default states have regressed
└── Report by-default compliance metrics to DPO quarterly
```
