# HIPAA PHI Inventory — Workflows

## Workflow 1: Enterprise-Wide ePHI Inventory Process

```
ePHI Inventory Initiation
│
├── Step 1: Define Scope and Methodology
│   ├── Scope: ALL electronic systems, media, and locations where ePHI is
│   │   created, received, maintained, or transmitted
│   ├── Assign inventory lead (Security Officer or delegate)
│   ├── Establish inventory team (IT, clinical informatics, compliance, facilities)
│   ├── Select inventory methodology (automated scanning + manual survey)
│   └── Set timeline and department interview schedule
│
├── Step 2: Automated Discovery
│   ├── Network scanning: identify all connected devices and systems
│   ├── Data loss prevention (DLP) scanning: detect PHI patterns in file systems
│   ├── Active Directory / IAM review: identify systems with healthcare user groups
│   ├── Cloud service inventory: enumerate SaaS, IaaS, PaaS with PHI
│   ├── API gateway review: identify external data exchange endpoints
│   └── Mobile device management (MDM): enumerate enrolled devices
│
├── Step 3: Manual Survey and Interviews
│   ├── Department-by-department survey:
│   │   ├── What systems do you use to access patient information?
│   │   ├── Do you store patient information on local drives, USB, or personal devices?
│   │   ├── Do you send patient information via email, fax, or messaging?
│   │   ├── Do you share patient information with external parties?
│   │   └── Are there paper records with PHI that are scanned or digitized?
│   │
│   ├── IT infrastructure team interview:
│   │   ├── Complete server inventory (physical and virtual)
│   │   ├── Storage systems (SAN, NAS, cloud storage)
│   │   ├── Backup systems and retention schedules
│   │   ├── Network diagrams showing PHI flow paths
│   │   └── Disaster recovery / business continuity sites
│   │
│   └── Business associate inventory:
│       ├── List all BAs with PHI access
│       ├── What PHI does each BA create, receive, maintain, or transmit?
│       └── Where does BA-held PHI reside?
│
├── Step 4: Inventory Compilation
│   ├── Consolidate automated and manual findings
│   ├── Classify each asset:
│   │   ├── System name and description
│   │   ├── System owner (department, individual)
│   │   ├── PHI types contained (clinical, billing, demographics, etc.)
│   │   ├── Volume (approximate records count)
│   │   ├── Location (on-premises, cloud provider, BA-hosted)
│   │   ├── Access method (network, VPN, internet, physical)
│   │   └── Current security controls (encryption, access control, audit)
│   │
│   ├── Map data flows between systems
│   └── Identify gaps: systems found via scanning but not reported in surveys
│
└── Step 5: Validation and Approval
    ├── Cross-reference inventory with known systems (EHR, billing, HR, etc.)
    ├── Validate with department heads that their systems are accurately captured
    ├── Security Officer reviews and approves final inventory
    ├── Feed inventory into risk analysis process (§164.308(a)(1))
    └── Establish update schedule (minimum annual; trigger-based for new systems)
```

## Workflow 2: New System PHI Assessment

```
New System, Application, or Service Being Deployed
│
├── Step 1: PHI Determination
│   ├── Will the system create, receive, maintain, or transmit ePHI?
│   │   ├── YES → Add to PHI inventory; proceed to assessment
│   │   └── NO → Document determination; no further action
│   │
│   └── If uncertain, consult Privacy Officer for classification
│
├── Step 2: Inventory Registration
│   ├── Register system in PHI asset inventory:
│   │   ├── System name, vendor, version
│   │   ├── System owner and administrator
│   │   ├── PHI types to be processed
│   │   ├── Expected record volume
│   │   ├── Hosting location (on-premises, cloud, hybrid)
│   │   ├── User base (roles, departments, approximate count)
│   │   └── Integration points (systems it connects to)
│   │
│   └── Classify sensitivity: standard PHI, sensitive PHI (42 CFR Part 2,
│       HIV, mental health, genetic), or de-identified
│
├── Step 3: Security Assessment
│   ├── Does the system meet Security Rule technical safeguards?
│   │   ├── Access control (§164.312(a))
│   │   ├── Audit controls (§164.312(b))
│   │   ├── Integrity controls (§164.312(c))
│   │   ├── Authentication (§164.312(d))
│   │   └── Transmission security (§164.312(e))
│   │
│   ├── Is BAA required with vendor?
│   │   ├── YES → Execute BAA before go-live
│   │   └── NO → Document rationale
│   │
│   └── Conduct risk assessment for the new system
│
├── Step 4: Data Flow Documentation
│   ├── Map all data flows to/from the new system
│   ├── Document interfaces, APIs, and integration methods
│   ├── Identify encryption status for each flow
│   └── Update enterprise data flow diagrams
│
└── Step 5: Approval and Go-Live
    ├── Security Officer approves PHI inventory registration
    ├── Risk assessment findings remediated or accepted
    ├── System added to ongoing monitoring (audit, vulnerability scanning)
    └── Update enterprise risk analysis to include new system
```

## Workflow 3: Annual PHI Inventory Review

```
Annual PHI Inventory Review Cycle
│
├── Step 1: Preparation
│   ├── Pull current PHI inventory from asset management system
│   ├── Pull list of systems added/decommissioned since last review
│   ├── Pull BA inventory updates
│   └── Schedule department review sessions
│
├── Step 2: System-by-System Review
│   ├── For each system in inventory:
│   │   ├── Is the system still in use?
│   │   │   ├── NO → Verify data disposition; remove from inventory
│   │   │   └── YES → Continue review
│   │   │
│   │   ├── Has the PHI scope changed (new data types, increased volume)?
│   │   ├── Has the hosting location changed?
│   │   ├── Have access roles changed?
│   │   ├── Are security controls current (encryption, patching, audit)?
│   │   └── Is BAA current (not expired, covers current scope)?
│   │
│   └── Identify any new systems not yet in inventory
│
├── Step 3: Data Flow Validation
│   ├── Review and update data flow diagrams
│   ├── Verify encryption status for all flows
│   ├── Identify new integration points added during the year
│   └── Validate BA data flows against BAA terms
│
├── Step 4: Gap Remediation
│   ├── Systems found but not in inventory → Add and assess
│   ├── Decommissioned systems still in inventory → Verify disposal; remove
│   ├── Security control gaps → Add to risk register
│   └── BAA gaps → Escalate to BAA management process
│
└── Step 5: Documentation and Reporting
    ├── Update master PHI inventory
    ├── Produce annual inventory review report
    ├── Feed findings into annual risk analysis update
    ├── Report to compliance committee
    └── Set next review date
```
