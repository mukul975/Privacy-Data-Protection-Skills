# Workflow -- DPIA Register Management

## Phase 1: Register Setup

### Step 1.1: Define Register Structure
- Establish DPIA reference numbering convention (DPIA-[DEPT]-[YEAR]-[SEQ])
- Define required fields for each DPIA record (see SKILL.md Core DPIA Record Fields)
- Create register in chosen tool (GRC platform, SharePoint, database, spreadsheet)
- Configure access controls: DPO read/write, privacy team read/write, management read-only
- Establish retention policy for archived DPIAs (minimum 3 years after processing cessation)

### Step 1.2: Import Existing DPIAs
- Inventory all existing DPIAs across the organisation
- Assign reference numbers to existing assessments
- Map existing DPIAs to RoPA entries (Art. 30 cross-reference)
- Set initial review dates based on current risk levels
- Identify overdue DPIAs requiring immediate reassessment

### Step 1.3: Establish Governance
- Appoint register owner (typically DPO or privacy programme manager)
- Define roles: who can create entries, who reviews, who approves status changes
- Establish escalation procedures for overdue reviews
- Define reporting schedule: quarterly dashboard to senior management, annual report to board

## Phase 2: DPIA Intake and Registration

### Step 2.1: Screening and Threshold Assessment
- Receive new processing activity notification from business unit
- Conduct threshold assessment against EDPB WP248rev.01 nine-factor criteria
- If two or more criteria met: create DPIA register entry with status "Screening"
- If DPIA not required: document screening outcome and rationale in register
- Assign DPIA lead and target completion date

### Step 2.2: Register New DPIA Entry
- Generate unique DPIA reference number
- Populate initial fields: processing activity, controller, department, RoPA link
- Set status to "Draft"
- Assign DPO reviewer per Art. 35(2)
- Link to mitigation plan reference (to be created during assessment)
- Notify DPIA lead and DPO of new entry

### Step 2.3: Track DPIA Progress
- Monitor draft completion against target date
- Track DPO review status and advice
- Record any Art. 35(9) stakeholder consultation conducted
- Flag delays to register owner for escalation
- Ensure processing does not commence before DPIA completion (Art. 35(1) "prior to")

## Phase 3: Approval and Activation

### Step 3.1: DPO Review Completion
- DPO provides written advice on the DPIA
- Record DPO advice in register entry
- If DPO identifies deficiencies: return to Draft with specific remediation requirements
- If DPO recommends approval: advance to approval stage

### Step 3.2: Risk Level Classification
- Record overall residual risk level from DPIA (Low, Medium, High, Very High)
- If residual risk is High or Very High: flag for Art. 36 prior consultation assessment
- Calculate next review date based on risk level (see SKILL.md Review Scheduling table)
- Set review date in register

### Step 3.3: Art. 36 Prior Consultation (if required)
- Record prior consultation decision in register
- If required: set status to "Prior Consultation Pending"
- Track submission to supervisory authority with date and SA reference number
- Record SA response and any conditions imposed
- Do not advance to "Approved" until SA response received or 8-week period elapsed

### Step 3.4: Final Approval
- Obtain sign-off from appropriate approval authority
- Record approval date, approver name, and decision
- Set status to "Approved" (or "Approved with Conditions" if SA imposed conditions)
- Processing may commence
- Activate monitoring schedule

## Phase 4: Ongoing Register Maintenance

### Step 4.1: Scheduled Review Management
- Generate automated review reminders 30 days before review date
- Assign review to DPIA lead or current process owner
- Review assesses: has processing changed? Have risks changed? Are mitigations still effective?
- If no changes: record "Reviewed -- no update required" with new review date
- If changes identified: set status to "Requires Update"

### Step 4.2: Change-Triggered Review
- Receive notification of processing change from business unit
- Assess whether change affects DPIA conclusions:
  - Scope change (new data categories, new subjects, new geography)
  - Technology change (new system, vendor change, algorithm update)
  - Legal change (new legislation, new SA guidance)
  - Incident (breach affecting assessed processing)
  - Organisational change (merger, new controller, new processor)
- If DPIA affected: set status to "Requires Update" and assign revision
- If not affected: document assessment and rationale

### Step 4.3: DPIA Revision Process
- Create revised version of DPIA (maintain version history)
- Repeat DPO review and approval cycle
- Update register entry with new assessment date, risk level, review date
- Set status to "Re-approved"
- If risk level increased: reassess review frequency

### Step 4.4: Archival
- When processing ceases: set status to "Archived"
- Record archival date and reason (processing ended, system decommissioned, etc.)
- Retain archived DPIA per retention policy for accountability evidence
- Do not delete archived entries

## Phase 5: Reporting and Dashboard

### Step 5.1: Quarterly Privacy Dashboard
- Total DPIAs in register by status (Draft, Approved, Requires Update, Archived)
- Overdue reviews count and details
- DPIAs completed this quarter
- Art. 36 prior consultations submitted and pending
- Risk distribution: count of DPIAs by residual risk level

### Step 5.2: Annual Board Report
- Summary of DPIA programme maturity
- Year-over-year comparison of DPIA volume and risk levels
- Prior consultation outcomes
- Key findings and trends across DPIAs
- Resource requirements for upcoming year

### Step 5.3: Supervisory Authority Readiness
- Ensure register is export-ready for SA inspection
- Verify all entries have complete documentation
- Confirm all review dates are current
- Validate Art. 36 consultation records are complete
- Test register access for SA audit scenario
