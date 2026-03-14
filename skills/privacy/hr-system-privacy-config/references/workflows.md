# HR System Privacy Configuration Workflows

## Workflow 1: Initial Privacy Configuration

```
START: HR system deployment or privacy audit
│
├─ Phase 1: Access Control Configuration
│  ├─ Map organisational roles to HR system security roles/groups
│  ├─ Configure field-level access for each role per RBAC matrix
│  ├─ Restrict health data fields to authorised HR only
│  ├─ Restrict salary/compensation to payroll + authorised HR
│  ├─ Configure manager access to direct reports only
│  ├─ Disable default admin access to personal data content
│  ├─ Enable IP restriction for admin access
│  └─ Test: verify each role sees only permitted data
│
├─ Phase 2: Retention Automation
│  ├─ Configure automated purge rules per data category:
│  │  - Unsuccessful candidates: 6 months
│  │  - Performance reviews: 2 years post-termination
│  │  - Payroll/tax records: 6-7 years
│  │  - Disciplinary warnings: per policy expiry
│  │  - Health records: per occupational health requirements
│  ├─ Set retention triggers (termination date, decision date)
│  ├─ Test purge rules in sandbox environment
│  ├─ Configure anonymisation for aggregate reporting data
│  └─ Verify audit trail survives data deletion
│
├─ Phase 3: Audit Logging
│  ├─ Enable logging for: data access, modification, export, report generation
│  ├─ Enable logging for: permission changes, deletion events
│  ├─ Enable logging for: failed access attempts
│  ├─ Configure log retention (2-3 years)
│  └─ Restrict log access to DPO/security team
│
├─ Phase 4: Cross-Border Configuration
│  ├─ Verify data centre location for EEA data
│  ├─ Assess all integrations for cross-border transfers
│  ├─ Implement SCCs / verify DPF for US transfers
│  ├─ Configure data residency on APIs
│  └─ Document all transfers in ROPA
│
├─ Phase 5: DSAR Capability
│  ├─ Test individual data export (all modules)
│  ├─ Configure DSAR workflow with deadline tracking
│  ├─ Test rectification capability
│  ├─ Test erasure capability
│  └─ Verify referential integrity after deletion
│
└─ END: Configuration documented. Schedule quarterly review.
```

## Workflow 2: Quarterly Access Review

```
START: Quarterly access review date
│
├─ Step 1: Extract current access matrix from HR system
│  ├─ List all users with access and their permission levels
│  └─ Compare against approved RBAC matrix
│
├─ Step 2: Identify anomalies
│  ├─ Users with access beyond their role → Remove excess permissions
│  ├─ Terminated users with active access → Deactivate immediately
│  ├─ Temporary elevated access not revoked → Revoke
│  ├─ New roles not yet mapped → Map to appropriate access level
│  └─ Segregation of duty violations → Remediate
│
├─ Step 3: Review audit logs
│  ├─ Any unusual access patterns (late night, bulk export, unusual departments)
│  ├─ Any failed access attempts indicating permission issues
│  └─ Any access to health/sensitive data by unauthorised roles
│
├─ Step 4: Review retention automation
│  ├─ Verify purge rules executed correctly in the quarter
│  ├─ Check for data past retention period → Trigger manual deletion
│  └─ Verify anonymisation working for aggregate data
│
├─ Step 5: Document and sign-off
│  ├─ Record review findings
│  ├─ Track remediation actions to completion
│  └─ DPO sign-off
│
└─ END: Access review complete. Schedule next quarter.
```

## Workflow 3: Post-Upgrade Privacy Verification

```
START: HR system upgrade applied
│
├─ Step 1: Verify security settings not reset by upgrade
│  ├─ Re-check role-based permissions
│  ├─ Re-check field-level security
│  ├─ Re-check audit logging configuration
│  └─ Re-check retention automation rules
│
├─ Step 2: Assess new features for privacy impact
│  ├─ Any new data collection capabilities? → Assess necessity
│  ├─ Any new analytics/reporting features? → Assess for data minimisation
│  ├─ Any new integrations or APIs? → Assess for transfer compliance
│  └─ Any changes to data storage architecture? → Verify data residency
│
├─ Step 3: Test
│  ├─ Test access controls with sample users per role
│  ├─ Test DSAR export functionality
│  ├─ Test retention automation
│  └─ Verify audit logs capture upgrade-related changes
│
└─ END: Post-upgrade verification complete. Document any configuration changes.
```
