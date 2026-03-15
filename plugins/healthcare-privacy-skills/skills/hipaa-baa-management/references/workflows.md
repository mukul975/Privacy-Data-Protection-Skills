# HIPAA BAA Management — Workflows

## Workflow 1: BA Identification and BAA Execution

```
New Vendor Relationship Under Consideration
│
├── Step 1: Determine if Vendor is a Business Associate
│   ├── Does the vendor create, receive, maintain, or transmit PHI?
│   │   ├── YES → Likely a BA; continue assessment
│   │   └── NO → Not a BA; no BAA required
│   │
│   ├── Is the vendor performing a HIPAA-regulated function?
│   │   (claims processing, data analysis, billing, QA, legal, accounting, etc.)
│   │   ├── YES → BA; BAA required
│   │   └── NO → Continue evaluation
│   │
│   ├── Does the conduit exception apply?
│   │   (Merely transporting PHI without persistent access)
│   │   ├── YES → Not a BA (postal service, ISP, courier)
│   │   └── NO → BA if PHI access is more than transient
│   │
│   └── Determination: [ ] BA — BAA Required [ ] Not a BA — No BAA
│
├── Step 2: Security Assessment (before BAA execution)
│   ├── Vendor completes security assessment questionnaire
│   ├── Review SOC 2 Type II report (or equivalent)
│   ├── Evaluate encryption, access controls, incident response
│   ├── Assess subcontractor management practices
│   └── Risk rating: [ ] Acceptable [ ] Conditional [ ] Unacceptable
│
├── Step 3: BAA Negotiation and Execution
│   ├── Provide standard BAA template to vendor
│   ├── Legal review of any vendor-proposed modifications
│   ├── Verify all §164.504(e)(2) required provisions included
│   ├── Authorized signatories sign BAA
│   ├── BAA effective date precedes any PHI access
│   └── Log BAA in tracking system with key dates
│
└── Step 4: PHI Access Provisioning
    ├── Grant PHI access only after BAA is fully executed
    ├── Configure access per minimum necessary and BAA scope
    └── Document PHI categories shared and access method
```

## Workflow 2: BAA Compliance Monitoring

```
Annual BAA Review Cycle
│
├── Step 1: Inventory Review (Q1)
│   ├── Reconcile BA inventory against accounts payable vendor list
│   ├── Identify new vendors with potential PHI access
│   ├── Identify terminated BA relationships
│   └── Update BA tracking system
│
├── Step 2: Annual Security Assessment (Q1-Q2)
│   ├── Distribute annual security questionnaire to all BAs
│   ├── Review updated SOC 2 reports
│   ├── Evaluate any reported security incidents
│   ├── Assess subcontractor management compliance
│   └── Risk re-rating per BA
│
├── Step 3: BAA Currency Review (Q2)
│   ├── Verify all BAAs are current (not expired)
│   ├── Identify BAAs needing Omnibus Rule updates
│   ├── Review BAAs approaching master agreement renewal
│   └── Flag any vendors operating without current BAA
│
├── Step 4: Remediation (Q3)
│   ├── Execute new/updated BAAs for identified gaps
│   ├── Address security assessment findings
│   ├── Initiate termination process for non-responsive BAs
│   └── Document all remediation activities
│
└── Step 5: Reporting (Q4)
    ├── BA compliance summary to Privacy Officer
    ├── Risk exceptions reported to compliance committee
    └── Board/audit committee reporting for material BA risks
```

## Workflow 3: BAA Termination and PHI Return/Destruction

```
BA Relationship Termination Triggered
│
├── Trigger: Contract expiration / Material breach / Strategic decision
│
├── Step 1: Notification
│   ├── Written notice to BA per BAA termination provisions
│   ├── If material breach: 30-day cure period notice
│   ├── If cure fails: termination notice with wind-down period
│   └── Coordinate with Procurement/Legal
│
├── Step 2: PHI Access Restriction (during wind-down)
│   ├── Limit PHI access to minimum necessary for transition
│   ├── Monitor BA access activity
│   ├── Revoke all system access on termination effective date
│   └── Revoke VPN, API keys, user accounts
│
├── Step 3: PHI Return or Destruction (within 30 days post-termination)
│   ├── BA returns all PHI in agreed format
│   │   OR
│   ├── BA certifies destruction per NIST SP 800-88
│   │   ├── Electronic media: clear/purge/destroy
│   │   └── Paper: cross-cut shred or incinerate
│   │
│   ├── If return/destruction not feasible:
│   │   ├── BA provides written explanation
│   │   ├── BA extends BAA protections indefinitely
│   │   └── Document infeasibility determination
│   │
│   └── Obtain written certification of destruction
│
└── Step 4: Close-Out
    ├── Update BA tracking system (status: terminated)
    ├── Retain BAA and all related documentation for 6 years
    ├── Retain destruction certification
    └── Archive vendor security assessment records
```
