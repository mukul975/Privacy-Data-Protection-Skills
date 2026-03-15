# Workflows — Data Inventory and Mapping

## Workflow 1: New System Onboarding — Data Inventory Registration

### Purpose
Ensure all new systems processing personal data are inventoried and classified before go-live.

### Process Flow

```
START: New system procurement or development approved
  │
  ├─► Step 1: Privacy Threshold Assessment (PTA)
  │     - System owner completes PTA questionnaire
  │     - Determines: Will the system process personal data?
  │     - If YES → proceed to Step 2
  │     - If NO → document assessment, no further inventory action
  │     Output: PTA result
  │
  ├─► Step 2: Data Element Cataloguing
  │     - Extract complete data schema from system vendor documentation or design
  │     - List all data elements: field name, data type, source, purpose
  │     - Identify data subjects (customers, employees, other)
  │     - Identify data retention requirements
  │     Output: Data element catalogue for the new system
  │
  ├─► Step 3: Classification Assignment
  │     - Apply personal data classification to each element (personal-data-test)
  │     - Flag special category data (special-category-data)
  │     - Flag criminal data (criminal-data-handling)
  │     - Assign classification tier (Public, Internal, Confidential, Restricted)
  │     Output: Classified data element register
  │
  ├─► Step 4: Data Flow Mapping
  │     - Map all inbound data flows (where does data come from?)
  │     - Map all outbound data flows (where does data go?)
  │     - Identify all processors and sub-processors
  │     - Identify international transfers
  │     Output: System data flow diagram
  │
  ├─► Step 5: Legal Basis Assignment
  │     - For each data element and purpose, assign Art. 6 lawful basis
  │     - For special category data, assign Art. 9(2) condition
  │     - For criminal data, identify Art. 10 national law authorisation
  │     - Verify lawful bases with Legal team
  │     Output: Purpose-basis mapping per element
  │
  ├─► Step 6: RoPA Integration
  │     - Create processing activity record in RoPA system
  │     - Link data elements to processing activity
  │     - Link data flows to processing activity
  │     - Link legal basis to processing activity
  │     Output: New RoPA entry
  │
  └─► Step 7: Discovery Tool Configuration
        - Register new system as data source in automated discovery platform
        - Configure scanning schedule
        - Verify first scan results match manual inventory
        Output: System registered in discovery platform
```

## Workflow 2: Quarterly Data Inventory Review

### Purpose
Maintain accuracy of the data inventory through regular review and reconciliation.

### Process Flow

```
START: Quarterly review cycle begins
  │
  ├─► Step 1: Automated Discovery Reconciliation
  │     - Compare automated discovery results to manual inventory
  │     - Identify gaps: data found by scanner not in inventory
  │     - Identify stale entries: inventory items not found by scanner
  │     Output: Reconciliation report
  │
  ├─► Step 2: Data Steward Review
  │     - Each department data steward reviews their systems' inventory entries
  │     - Confirm: Are all data elements still accurate?
  │     - Confirm: Any new data elements added since last review?
  │     - Confirm: Any data elements retired since last review?
  │     - Confirm: Any changes to data flows or recipients?
  │     Output: Data steward sign-off per department
  │
  ├─► Step 3: Classification Review
  │     - Review borderline classifications due for reassessment
  │     - Review any reclassification triggers (technology changes,
  │       new data partnerships, regulatory guidance)
  │     - Update classifications as needed
  │     Output: Updated classifications
  │
  ├─► Step 4: Data Flow Verification
  │     - Verify data flows against actual network traffic (CASB, proxy logs)
  │     - Identify undocumented data flows
  │     - Update data flow diagrams
  │     Output: Updated data flow maps
  │
  ├─► Step 5: Inventory Update
  │     - Apply all changes to the data inventory
  │     - Update RoPA records
  │     - Archive superseded inventory versions
  │     Output: Updated inventory (new version)
  │
  └─► Step 6: Reporting
        - Generate quarterly inventory health report
        - Report to DPO and Privacy Steering Committee
        - Track inventory completeness metrics over time
        Output: Quarterly inventory report
```

## Workflow 3: Data Flow Diagramming Process

### Purpose
Create and maintain visual data flow diagrams for each major processing activity.

### Notation Standards

```
External Entity          Process               Data Store
┌─────────────┐    ┌────────────────┐    ═══════════════════
│  Customer   │    │  Salesforce    │    ║  Oracle DW      ║
│  (data      │───►│  CRM           │───►║  (analytics     ║
│  subject)   │    │  [Confidential]│    ║  store)         ║
└─────────────┘    └────────────────┘    ═══════════════════

Arrow Labels:
─── Name, Email, Phone [PERSONAL_DIRECT] ──►
─── Account ID [PERSONAL_INDIRECT] ──►
═══ Health records [SPECIAL_CATEGORY] ══►   (double line = special category)
--- IP Address [ONLINE_IDENTIFIER] --►      (dashed = indirect/online)
```

### Process Flow

```
START: New or updated processing activity requires data flow diagram
  │
  ├─► Step 1: Identify Scope
  │     - Which processing activity is being documented?
  │     - Which systems are involved?
  │     - Which data subjects and data categories?
  │     Output: Scope definition
  │
  ├─► Step 2: Map Data Collection Points
  │     - Identify where data enters the organisation
  │     - Document collection mechanisms (web forms, APIs, manual entry)
  │     - Label with data categories and classification
  │     Output: Data collection map
  │
  ├─► Step 3: Map Internal Processing and Storage
  │     - Document how data moves between internal systems
  │     - Document where data is stored (primary and backup)
  │     - Document any transformations (aggregation, pseudonymisation)
  │     Output: Internal flow map
  │
  ├─► Step 4: Map External Sharing
  │     - Document all data sharing with third parties
  │     - Label with transfer mechanism and safeguard
  │     - Flag international transfers
  │     Output: External flow map
  │
  ├─► Step 5: Map Data Deletion
  │     - Document retention periods per store
  │     - Document deletion mechanisms (automated, manual)
  │     - Verify deletion propagates to all copies
  │     Output: Data lifecycle endpoint map
  │
  └─► Step 6: Review and Publish
        - DPO reviews diagram for completeness
        - System owners validate technical accuracy
        - Publish to data inventory repository
        - Set review date (annually or on material change)
        Output: Published data flow diagram
```
