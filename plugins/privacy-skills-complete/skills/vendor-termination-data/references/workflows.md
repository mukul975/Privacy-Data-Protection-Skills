# Workflows — Vendor Termination Data

## Workflow 1: Standard Vendor Termination Data Process

```
TRIGGER: Vendor relationship termination (any trigger type)
  │
  ├─► Step 1: Initiation (Privacy Team — 1 business day)
  │     ├─ Identify termination trigger and timeline
  │     ├─ Review DPA termination provisions (Section on data return/deletion)
  │     ├─ Determine controller election: RETURN or DELETE or RETURN THEN DELETE
  │     ├─ Issue formal written notice to vendor specifying election
  │     └─ Start termination timeline tracking
  │
  ├─► Step 2: Data Scope Confirmation (Privacy Team + IT — 5 business days)
  │     ├─ Request from vendor:
  │     │     ├─ Complete inventory of Summit personal data in vendor systems
  │     │     ├─ All data locations (production, backup, DR, logs, cache, sub-processors)
  │     │     ├─ Data formats and volumes per location
  │     │     └─ Any data subject to legal retention exceptions
  │     ├─ Cross-reference against DPA Annex I data categories
  │     └─ Identify any discrepancies between expected and reported data scope
  │
  ├─► Step 3: Data Return (if elected — within 30 calendar days)
  │     ├─ Agree on export format and method with vendor
  │     ├─ Vendor prepares data export:
  │     │     ├─ Production data in agreed format
  │     │     ├─ Manifest with record counts and SHA-256 checksums
  │     │     └─ Schema documentation
  │     ├─ Transfer via agreed secure method (SFTP/API/encrypted media)
  │     ├─ Summit validates received data:
  │     │     ├─ Record count verification
  │     │     ├─ Checksum verification
  │     │     ├─ Format/schema compliance
  │     │     └─ Random sample review
  │     └─ Confirm successful receipt to vendor in writing
  │
  ├─► Step 4: Data Deletion (within 60-90 calendar days per DPA)
  │     ├─ Vendor performs deletion:
  │     │     ├─ Production databases
  │     │     ├─ Application caches
  │     │     ├─ Log data containing personal data
  │     │     ├─ Derived/aggregated data
  │     │     └─ Metadata referencing personal data
  │     ├─ Vendor instructs sub-processors to delete
  │     ├─ Backup deletion (may follow extended timeline):
  │     │     ├─ Active backup deletion where technically feasible
  │     │     ├─ For tape backups: data expires through normal rotation
  │     │     └─ Maximum backup retention: 90 days from termination
  │     └─ Document any legal retention exceptions
  │
  ├─► Step 5: Deletion Certification (within 90 calendar days)
  │     ├─ Vendor provides written deletion certificate:
  │     │     ├─ Signed by authorized officer
  │     │     ├─ Lists all data locations and deletion methods
  │     │     ├─ Includes sub-processor deletion confirmations
  │     │     ├─ Documents any retention exceptions with legal basis
  │     │     └─ Dated and on vendor letterhead
  │     ├─ Privacy Team reviews certification:
  │     │     ├─ Covers all data categories from DPA Annex I
  │     │     ├─ Covers all known processing locations
  │     │     ├─ Sub-processors accounted for
  │     │     └─ Any exceptions properly justified
  │     └─ If insufficient: request supplementary confirmation
  │
  └─► Step 6: Close and Record (Privacy Team — 2 business days)
        ├─ File deletion certification in vendor records
        ├─ Update vendor register: status = TERMINATED
        ├─ Update SaaS inventory: remove from active inventory
        ├─ Archive DPA and termination correspondence
        └─ Schedule 6-month verification check (for high-risk vendors)
```

## Workflow 2: Emergency Data Retrieval (Vendor Insolvency)

```
TRIGGER: Vendor enters insolvency/administration
  │
  ├─► Step 1: Immediate Assessment (Privacy Team + Legal — 1 business day)
  │     ├─ Assess data access risk:
  │     │     ├─ Is the service still operational?
  │     │     ├─ Is data still accessible?
  │     │     └─ Is there risk of data loss or unauthorized access?
  │     ├─ Engage legal counsel on insolvency implications
  │     └─ Contact insolvency practitioner/administrator
  │
  ├─► Step 2: Emergency Data Export (within 48 hours)
  │     ├─ Execute all available self-service data export capabilities
  │     ├─ If API access available: Automated bulk extraction
  │     ├─ If service accessible: Manual export of critical data
  │     └─ Document all export activities
  │
  ├─► Step 3: Engage Insolvency Administrator
  │     ├─ Assert contractual data return/deletion rights
  │     ├─ Request formal data return under DPA terms
  │     ├─ If data inaccessible: Request administrator assistance
  │     └─ Document all communications
  │
  └─► Step 4: Post-Recovery
        ├─ Verify recovered data completeness
        ├─ Assess whether deletion certification obtainable
        ├─ If deletion cannot be confirmed: Document risk and mitigations
        └─ Report to DPO
```
