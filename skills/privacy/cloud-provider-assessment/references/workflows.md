# Workflows — Cloud Provider Assessment

## Workflow 1: Cloud Provider Privacy Assessment

```
TRIGGER: New cloud service provider evaluation or annual reassessment
  │
  ├─► Step 1: Service Model Classification (Privacy + InfoSec — 1 business day)
  │     ├─ Classify cloud service model: IaaS / PaaS / SaaS
  │     ├─ Determine shared responsibility boundaries
  │     ├─ Identify Summit Cloud Partners data to be processed
  │     └─ Map to cloud-specific assessment domains
  │
  ├─► Step 2: Certification and Attestation Review (Privacy Team — 5 business days)
  │     ├─ Request and verify:
  │     │     ├─ ISO 27001 certificate (scope covering services used)
  │     │     ├─ ISO 27018 certification (cloud privacy)
  │     │     ├─ ISO 27017 certification (cloud security)
  │     │     ├─ SOC 2 Type II report (with Privacy criterion)
  │     │     ├─ CSA STAR registration and level
  │     │     └─ Any sector-specific certifications
  │     ├─ Independently verify certifications:
  │     │     ├─ Check accreditation body registries
  │     │     ├─ Verify certification scope covers relevant services
  │     │     └─ Check for any scope exclusions
  │     └─ Document certification verification results
  │
  ├─► Step 3: Data Residency Assessment (Privacy Team — 3 business days)
  │     ├─ Determine where data will be stored at rest
  │     ├─ Identify all processing locations (including DR, backup, support)
  │     ├─ Assess metadata and telemetry data locations
  │     ├─ Map support staff access countries
  │     ├─ Verify region-locking capabilities
  │     └─ If third-country access: Initiate Transfer Impact Assessment
  │
  ├─► Step 4: Multi-Tenancy Assessment (InfoSec — 3 business days)
  │     ├─ Review tenant isolation architecture
  │     ├─ Assess per-tenant encryption key management
  │     ├─ Review cross-tenant attack testing results
  │     └─ Evaluate shared infrastructure security controls
  │
  ├─► Step 5: Shared Responsibility Model Mapping (Privacy + InfoSec — 3 business days)
  │     ├─ Map every control domain to responsible party
  │     ├─ Identify gaps where neither party has clear responsibility
  │     ├─ Document supplementary measures Summit must implement
  │     └─ Produce shared responsibility matrix
  │
  ├─► Step 6: Cloud-Specific Privacy Controls Review (Privacy Team — 5 business days)
  │     ├─ Assess against ISO 27018 Annex A controls
  │     ├─ Review CSA CCM privacy-relevant domains (DSP, GRC, SEF)
  │     ├─ Review SOC 2 Privacy criterion findings
  │     ├─ Assess government access notification process
  │     └─ Review data portability and deletion capabilities
  │
  ├─► Step 7: Scoring and Decision (Privacy Team Lead — 2 business days)
  │     ├─ Score each assessment domain (1-5)
  │     ├─ Calculate weighted assessment score
  │     ├─ Decision:
  │     │     ├─ APPROVED: Provider meets cloud privacy requirements
  │     │     ├─ CONDITIONAL: Supplementary measures required
  │     │     └─ REJECTED: Insufficient privacy protections
  │     └─ Document decision with rationale
  │
  └─► Step 8: DPA and Configuration (Legal + InfoSec)
        ├─ Negotiate cloud-specific DPA provisions
        ├─ Configure region restrictions per assessment
        ├─ Implement controller-side supplementary measures
        └─ Document complete shared responsibility implementation
```

## Workflow 2: Cloud Provider Configuration Verification

```
TRIGGER: Initial deployment or annual configuration audit
  │
  ├─► Step 1: Verify data residency configuration
  │     ├─ Confirm data region settings match DPA
  │     ├─ Verify no cross-region replication outside approved regions
  │     └─ Check backup location configuration
  │
  ├─► Step 2: Verify encryption configuration
  │     ├─ Confirm encryption at rest enabled with approved algorithm
  │     ├─ Verify key management model (provider-managed vs customer-managed)
  │     ├─ Check key rotation schedule
  │     └─ Verify encryption in transit configuration
  │
  ├─► Step 3: Verify access control configuration
  │     ├─ Review IAM policies and roles
  │     ├─ Confirm MFA enforcement
  │     ├─ Check for overly permissive policies
  │     └─ Verify SSO integration
  │
  ├─► Step 4: Verify logging configuration
  │     ├─ Confirm audit logging enabled
  │     ├─ Verify log retention meets DPA requirements
  │     └─ Confirm log export to Summit SIEM
  │
  └─► Step 5: Document and Report
        ├─ Produce configuration verification report
        └─ Remediate any discrepancies
```
