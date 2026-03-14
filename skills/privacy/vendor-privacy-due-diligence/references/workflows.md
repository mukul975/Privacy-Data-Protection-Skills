# Workflows — Vendor Privacy Due Diligence

## Workflow 1: New Vendor Due Diligence Process

```
TRIGGER: Business unit submits Vendor Engagement Request for a vendor that will process personal data
  │
  ├─► Step 1: Initial Screening (Privacy Team — 2 business days)
  │     ├─ Review Vendor Engagement Request form
  │     ├─ Confirm personal data processing will occur
  │     ├─ Classify initial risk tier based on:
  │     │     ├─ Data volume (< 10K subjects = Standard, > 10K = High)
  │     │     ├─ Data sensitivity (special category = High)
  │     │     ├─ Transfer locations (third country = elevated)
  │     │     └─ Processing nature (automated decision-making = High)
  │     └─ If no personal data processing → Issue "No Due Diligence Required" determination
  │
  ├─► Step 2: Issue Privacy Risk Questionnaire (Privacy Team → Vendor)
  │     ├─ Send standardized questionnaire (Sections A-D)
  │     ├─ Request supporting documentation:
  │     │     ├─ Current ISO 27001/27701 certificates
  │     │     ├─ SOC 2 Type II report (bridge letter if period gap)
  │     │     ├─ Data processing architecture documentation
  │     │     ├─ Incident response plan summary
  │     │     └─ Sub-processor list with locations
  │     ├─ Set response deadline: 15 business days
  │     └─ Track in vendor management system
  │
  ├─► Step 3: Questionnaire Review and Verification (Privacy Team — 5 business days)
  │     ├─ Score each section (A-D) on 1-5 scale
  │     ├─ Identify gaps requiring clarification
  │     ├─ Verify certifications independently:
  │     │     ├─ ISO certificates: Check accreditation body registry
  │     │     ├─ SOC 2: Review report scope, exceptions, and qualified opinions
  │     │     └─ CSA STAR: Check CSA STAR Registry
  │     ├─ Conduct public record search:
  │     │     ├─ EDPB enforcement decisions database
  │     │     ├─ National supervisory authority published decisions
  │     │     └─ Breach notification databases (where publicly available)
  │     └─ Send clarification questions to vendor if needed (5 business day response window)
  │
  ├─► Step 4: Technical Controls Assessment (InfoSec Team — 5 business days)
  │     ├─ Review architecture documentation
  │     ├─ Assess encryption implementation (at-rest and in-transit)
  │     ├─ Review access control model
  │     ├─ Evaluate network security architecture
  │     ├─ Review penetration test results (if available under NDA)
  │     └─ Produce Technical Assessment Report
  │
  ├─► Step 5: Data Flow Analysis (Privacy Team — 3 business days)
  │     ├─ Document complete data flow diagram
  │     ├─ Identify all processing locations
  │     ├─ Map sub-processor chain
  │     ├─ Assess cross-border transfer requirements
  │     │     └─ If third-country transfers: Initiate Transfer Impact Assessment
  │     └─ Produce Data Flow Analysis Document
  │
  ├─► Step 6: Sufficiency Decision (DPO — 3 business days)
  │     ├─ Review all assessment materials
  │     ├─ Calculate weighted sufficiency score
  │     ├─ Decision:
  │     │     ├─ APPROVED (4.0+): Proceed to DPA drafting
  │     │     ├─ CONDITIONALLY APPROVED (3.0-3.9):
  │     │     │     ├─ Document required supplementary measures
  │     │     │     ├─ Negotiate additional contractual safeguards
  │     │     │     └─ Set conditions for final approval
  │     │     └─ REJECTED (< 3.0):
  │     │           ├─ Document rejection rationale
  │     │           ├─ Notify requesting business unit
  │     │           └─ Offer vendor opportunity to remediate and resubmit
  │     └─ Sign and date sufficiency determination
  │
  └─► Step 7: File and Schedule (Privacy Team — 1 business day)
        ├─ Assemble complete due diligence file
        ├─ Store in vendor management system
        ├─ Set reassessment date (12 months for High risk, 24 months for Standard)
        └─ Notify requesting business unit of outcome
```

## Workflow 2: Trigger-Based Reassessment

```
TRIGGER: One of the following events detected
  ├─ Vendor reports a personal data breach
  ├─ Regulatory enforcement action against vendor published
  ├─ Vendor ISO/SOC certification lapses or scope changes
  ├─ Material change to vendor services or processing locations
  ├─ Media report of significant security incident at vendor
  │
  ├─► Step 1: Triage (Privacy Team — 1 business day)
  │     ├─ Assess severity of triggering event
  │     ├─ Determine if immediate data flow suspension warranted
  │     └─ Classify: Critical (immediate action) / Major (accelerated review) / Minor (note for annual review)
  │
  ├─► Step 2: Accelerated Assessment (Privacy Team — varies by severity)
  │     ├─ Critical: Request vendor incident report within 48 hours
  │     ├─ Major: Issue focused questionnaire on affected control domain within 5 business days
  │     └─ Minor: Add to annual reassessment agenda
  │
  ├─► Step 3: Re-evaluation Decision (DPO)
  │     ├─ Review updated information
  │     ├─ Recalculate sufficiency score with new evidence
  │     ├─ Decide: Continue / Continue with conditions / Suspend / Terminate
  │     └─ If Suspend or Terminate: Initiate Vendor Termination Data workflow
  │
  └─► Step 4: Document and Communicate
        ├─ Update vendor due diligence file
        ├─ Notify affected business units
        ├─ Update risk scoring in vendor register
        └─ Adjust reassessment schedule if needed
```

## Workflow 3: Annual Scheduled Reassessment

```
TRIGGER: Reassessment date reached in vendor management system
  │
  ├─► Step 1: Determine Reassessment Scope
  │     ├─ High-risk vendors: Full questionnaire refresh (Sections A-D)
  │     ├─ Standard-risk vendors: Abbreviated questionnaire (changes only)
  │     └─ Request updated certifications and attestations
  │
  ├─► Step 2: Issue Reassessment Questionnaire
  │     ├─ Attach previous responses for vendor reference
  │     ├─ Highlight specific areas for update
  │     └─ 15 business day response deadline
  │
  ├─► Step 3: Delta Analysis
  │     ├─ Compare new responses against prior assessment
  │     ├─ Identify improvements and deteriorations
  │     ├─ Verify any new certifications claimed
  │     └─ Review sub-processor list for changes
  │
  ├─► Step 4: Updated Sufficiency Decision
  │     ├─ Recalculate weighted score
  │     ├─ Document decision with year-over-year comparison
  │     └─ Set next reassessment date
  │
  └─► Step 5: Update Records
        ├─ Update vendor register
        ├─ Archive previous assessment
        └─ Notify vendor of outcome and any required actions
```
