# HIPAA Minimum Necessary — Workflows

## Workflow 1: Minimum Necessary Decision Tree

```
PHI Use or Disclosure Request
│
├── Does the minimum necessary standard apply?
│   ├── Disclosure for treatment? → NO (exception)
│   ├── Disclosure to the individual? → NO (exception)
│   ├── Pursuant to valid authorization? → NO (exception)
│   ├── Disclosure to HHS for enforcement? → NO (exception)
│   ├── Required by law? → NO (exception)
│   ├── Administrative Simplification compliance? → NO (exception)
│   └── None of the above → YES, minimum necessary APPLIES
│
├── Is this an internal USE by workforce?
│   ├── YES → Apply role-based access policy
│   │   ├── Identify workforce member's role category
│   │   ├── Grant access only to PHI categories defined for that role
│   │   └── Document role-to-PHI mapping per §164.514(d)(2)
│   │
│   └── NO → Is this a DISCLOSURE?
│
├── Is this a routine, recurring disclosure?
│   ├── YES → Apply standard protocol
│   │   ├── Use pre-defined standard PHI set for this disclosure type
│   │   ├── Do not include additional PHI beyond standard set
│   │   └── Document protocol per §164.514(d)(3)(i)
│   │
│   └── NO → Non-routine disclosure
│       ├── Review request on case-by-case basis
│       ├── Apply criteria limiting PHI to what is reasonably necessary
│       ├── Obtain Privacy Officer review if required categories involved
│       └── Document rationale for scope of disclosure
│
└── Can reasonable reliance be applied? (§164.514(d)(3)(iii))
    ├── Request from public official stating minimum necessary → YES
    ├── Request from another covered entity → YES
    ├── Request from workforce/BA professional → YES
    ├── Research with IRB/Privacy Board waiver → YES
    └── Other → NO, disclosing entity must independently determine minimum necessary
```

## Workflow 2: Role-Based Access Review

```
Quarterly Access Review Process
│
├── Step 1: Extract current access profiles
│   ├── Export all active user accounts from EHR and clinical systems
│   ├── Map each account to workforce role category
│   └── Identify access permissions assigned to each account
│
├── Step 2: Compare actual access to role-based policy
│   ├── For each user: does assigned access match their role's approved PHI categories?
│   ├── Flag users with excess access (access beyond role requirement)
│   ├── Flag users with role changes not reflected in access (transferred, promoted)
│   └── Flag dormant accounts (no login in 90+ days)
│
├── Step 3: Manager certification
│   ├── Distribute access reports to department managers
│   ├── Managers certify or revoke access for each direct report
│   ├── Deadline: 15 business days from distribution
│   └── Uncertified access suspended after deadline
│
├── Step 4: Remediation
│   ├── Remove excess access immediately
│   ├── Deactivate dormant accounts
│   ├── Update access profiles for role changes
│   └── Document all access modifications
│
└── Step 5: Reporting
    ├── Access review completion rate
    ├── Number of access modifications made
    ├── Exceptions requiring Privacy Officer approval
    └── Report to compliance committee
```
