# Workflows — Criminal Data Handling

## Workflow 1: Pre-Employment Criminal Background Check

### Purpose
Conduct lawful criminal background screening for candidates in FCA-regulated roles at Vanguard Financial Services.

### Process Flow

```
START: Candidate reaches conditional offer stage for regulated role
  │
  ├─► Step 1: Determine Check Level Required
  │     - Basic DBS: All roles (unspent convictions only)
  │     - Standard DBS: Roles involving regulated activity with children/vulnerable adults
  │     - Enhanced DBS: FCA-controlled functions (Senior Managers, Certification Staff)
  │     - Verify role is listed in Exceptions Order 1975 (for enhanced/standard)
  │     Output: Required check level with legal basis citation
  │
  ├─► Step 2: Candidate Consent and Disclosure
  │     - Provide candidate with written explanation of the check purpose and scope
  │     - For basic DBS: candidate applies directly to DBS
  │     - For enhanced DBS: Vanguard submits as registered body
  │     - Obtain candidate's written consent (not Art. 9(2)(a) explicit consent;
  │       Art. 10 relies on legal obligation, not consent)
  │     - Inform candidate of Rehabilitation of Offenders Act protections
  │     Output: Consent form signed, DBS application submitted
  │
  ├─► Step 3: Receive and Process Results
  │     - DBS certificate received by candidate (or by Vanguard for enhanced)
  │     - Record only: check date, certificate number, result (clear/not clear)
  │     - If not clear: record relevant conviction details proportionate to role
  │     - Do NOT photocopy the full DBS certificate (ICO guidance)
  │     Output: Criminal data record in HR system
  │
  ├─► Step 4: Risk Assessment (if convictions disclosed)
  │     - Assess relevance of conviction to the specific role
  │     - Consider: nature of offence, time elapsed, rehabilitation evidence,
  │       role responsibilities, regulatory requirements
  │     - For FCA roles: apply FCA FIT 2.1 criteria
  │     - Decision maker: HR Director in consultation with Compliance
  │     - Document reasoning regardless of outcome
  │     Output: Risk assessment with hire/not-hire recommendation
  │
  ├─► Step 5: Retention and Disposal
  │     - Retain criminal check records for maximum 6 months from decision date
  │     - Automated deletion trigger in HR system
  │     - If ongoing regulatory requirement (FCA approved persons): retain
  │       for duration of appointment + 3 years
  │     - Secure disposal: digital overwrite (not just deletion) of criminal data
  │     Output: Retention schedule applied
  │
  └─► Step 6: Audit and Compliance
        - Log all access to criminal data records
        - DPO quarterly audit of criminal data processing
        - Annual review of appropriate policy document (DPA 2018 s.11)
        Output: Audit records
```

## Workflow 2: Anti-Money Laundering Criminal Data Processing

### Purpose
Process criminal offence data in the context of suspicious activity reporting under the Proceeds of Crime Act 2002.

### Process Flow

```
START: Suspicious activity identified by front-line staff or automated monitoring
  │
  ├─► Step 1: Initial Assessment
  │     - Money Laundering Reporting Officer (MLRO) evaluates the suspicious activity
  │     - Determine whether the activity involves suspected criminal conduct
  │     - If yes: data relating to the suspected offence becomes Art. 10 criminal data
  │     Output: Initial assessment record (classified Art. 10)
  │
  ├─► Step 2: SAR Preparation
  │     - MLRO prepares Suspicious Activity Report for NCA (National Crime Agency)
  │     - Legal basis: Proceeds of Crime Act 2002 s.330 (regulated sector duty to report)
  │     - Art. 10 authorisation: DPA 2018 Sch.1 Part 2 para 10 (preventing/detecting unlawful acts)
  │     - Data minimisation: include only information necessary for the report
  │     Output: SAR draft with Art. 10 compliance record
  │
  ├─► Step 3: Tipping Off Prevention
  │     - Ensure no disclosure to the data subject that a SAR has been filed
  │     - Art. 15 right of access does NOT override tipping-off prohibition
  │       (Proceeds of Crime Act 2002 s.333A)
  │     - If DSAR received for subject of SAR: apply exemption under DPA 2018
  │       Schedule 2 Part 1 para 2 (crime and taxation)
  │     Output: Access restriction applied
  │
  ├─► Step 4: Ongoing Investigation Support
  │     - If NCA or law enforcement request additional information:
  │       provide under lawful authority
  │     - Maintain case file with full audit trail
  │     - Restrict access to MLRO team and DPO only
  │     Output: Case file maintained under Art. 10 safeguards
  │
  └─► Step 5: Case Closure and Retention
        - SAR records retained for 5 years from date of report
          (Money Laundering Regulations 2017 reg.40)
        - If criminal proceedings initiated: retain until proceedings concluded + 1 year
        - Secure disposal after retention period
        Output: Retention and disposal record
```

## Workflow 3: Criminal Data Discovery and Classification Scan

### Purpose
Identify all instances of criminal data across Vanguard systems and ensure Art. 10 compliance.

### Process Flow

```
START: Periodic criminal data audit (annual) or new system onboarding
  │
  ├─► Step 1: System Inventory
  │     - List all systems that may contain criminal data
  │     - Priority targets: HR, Compliance, Legal, Risk Management, KYC/AML
  │     Output: Systems to scan
  │
  ├─► Step 2: Automated Detection
  │     - Scan field names for criminal data indicators
  │     - Scan free-text fields for criminal terminology
  │     - Check for references to external criminal databases
  │     Output: Candidate criminal data elements
  │
  ├─► Step 3: Manual Classification
  │     - Legal review of each candidate element
  │     - Distinguish criminal data (Art. 10) from civil/administrative data
  │     - Classify spent vs unspent convictions
  │     - Flag comprehensive register risks
  │     Output: Classified criminal data inventory
  │
  ├─► Step 4: Legal Basis Verification
  │     - For each criminal data element, identify the specific national law basis
  │     - Verify appropriate safeguards are in place
  │     - Verify appropriate policy document exists (DPA 2018 s.11)
  │     - Flag any elements without established legal basis → processing must cease
  │     Output: Legal basis mapping
  │
  └─► Step 5: Remediation and Documentation
        - For elements without legal basis: cease processing, securely delete,
          or establish legal basis
        - Update Art. 30 RoPA with criminal data processing activities
        - Update data classification labels
        - Report findings to DPO
        Output: Remediation plan and updated documentation
```
