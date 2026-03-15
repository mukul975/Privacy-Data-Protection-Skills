# Workflows — Oregon OCPA

## Workflow 1: De-Identified Data Compliance

```
TRIGGER: Creation or sharing of de-identified dataset
  │
  ├─► Step 1: Apply De-Identification Techniques
  │     ├─ Remove direct identifiers (name, SSN, email, phone)
  │     ├─ Apply k-anonymity (k ≥ 5) to quasi-identifiers
  │     ├─ Apply differential privacy where appropriate
  │     └─ Generalize or suppress small cell counts
  │
  ├─► Step 2: Technical Safeguards
  │     ├─ Implement access controls on de-identified datasets
  │     ├─ Separate de-identified data from re-identification keys
  │     ├─ Encrypt re-identification keys with restricted access
  │     └─ Monitor for re-identification attempts
  │
  ├─► Step 3: Public Commitment
  │     ├─ Post public statement at privacy.libertycommerce.com/deidentification
  │     ├─ Commit to maintaining data only in de-identified form
  │     └─ Update annually or upon material changes
  │
  ├─► Step 4: Recipient Contracts
  │     ├─ Execute data use agreement with each recipient
  │     ├─ Prohibit re-identification attempts
  │     ├─ Require reasonable technical safeguards
  │     ├─ Include breach notification provisions
  │     └─ Grant audit rights to verify compliance
  │
  ├─► Step 5: Ongoing Monitoring
  │     ├─ Quarterly re-identification risk assessments
  │     ├─ Monitor for new data linkage threats
  │     ├─ Review recipient compliance reports
  │     └─ If re-identification occurs: remediate or destroy dataset
  │
  └─► Step 6: Documentation
        ├─ Record de-identification methodology
        ├─ Document risk assessment results
        └─ Retain for 3 years minimum
```

## Workflow 2: Specific Third-Party Disclosure (§646A.578(1)(f))

```
START: Consumer requests list of specific third parties who received their data
  │
  ├─► Step 1: Authenticate Consumer
  │     └─ Standard verification process
  │
  ├─► Step 2: Compile Third-Party List
  │     ├─ Query data sharing logs for consumer's identifier
  │     ├─ For each sharing event, record:
  │     │     ├─ Third-party name (specific entity, not category)
  │     │     ├─ Date of disclosure
  │     │     ├─ Categories of data disclosed
  │     │     └─ Purpose of disclosure
  │     └─ Include service providers, contractors, and third parties
  │
  ├─► Step 3: Prepare Response
  │     ├─ Format as structured list with entity names
  │     ├─ Include context (purpose) for each disclosure
  │     └─ Cover preceding 12-month period
  │
  └─► Step 4: Deliver Within 45 Days
        ├─ Deliver via secure channel
        └─ Log response for compliance records
```

## Workflow 3: Employee Data Compliance (Partial Exemption)

```
TRIGGER: Processing personal data of Oregon employees
  │
  ├─► Step 1: Identify Processing Activities
  │     ├─ Payroll and compensation
  │     ├─ Benefits administration
  │     ├─ Performance management
  │     ├─ Recruitment and hiring
  │     └─ Workforce analytics
  │
  ├─► Step 2: Apply Exempt Provisions (Not Required)
  │     ├─ Consumer rights requests (access, correct, delete, portability, opt-out)
  │     └─ Consumer request processing timelines
  │
  ├─► Step 3: Apply Non-Exempt Provisions (REQUIRED)
  │     ├─ Privacy notice to employees (§646A.576)
  │     ├─ Data minimization for employee data
  │     ├─ Reasonable data security measures
  │     ├─ Consent for sensitive employee data (health, racial/ethnic, etc.)
  │     ├─ Processor contracts for HR service providers
  │     ├─ De-identified data requirements for workforce analytics
  │     └─ DPIAs for employee profiling (performance scoring, etc.)
  │
  └─► Step 4: Document Exemption Application
        ├─ Record which provisions are exempt vs. applicable
        └─ Review upon changes to employee data processing
```
