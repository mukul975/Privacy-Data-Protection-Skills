# Workflows — Delaware DPPA

## Workflow 1: DPPA Applicability Assessment

```
START: New business activity involving Delaware consumers
  │
  ├─► Step 1: Determine Entity Exemptions (§12D-104)
  │     ├─ Is the entity a state or local government body? → Exempt
  │     ├─ Is the entity a GLBA-regulated financial institution? → Exempt
  │     ├─ Is the entity a HIPAA covered entity or business associate? → Exempt
  │     ├─ Is the entity a nonprofit organization? → Exempt
  │     ├─ Is the entity an institution of higher education? → Exempt
  │     └─ If none apply → proceed to Step 2
  │
  ├─► Step 2: Count Delaware Consumers (§12D-103)
  │     ├─ Identify all natural persons who are Delaware residents
  │     ├─ Exclude persons acting in employment or commercial context
  │     ├─ Exclude data processed solely for payment transactions
  │     ├─ Count: unique consumers whose personal data is controlled/processed
  │     └─ Result: consumer_count
  │
  ├─► Step 3: Apply Threshold Test
  │     ├─ Threshold A: consumer_count >= 35,000 → DPPA APPLIES
  │     ├─ Threshold B: consumer_count >= 10,000 AND revenue_from_sale > 20%
  │     │     └─ If YES → DPPA APPLIES
  │     └─ If neither threshold met → DPPA DOES NOT APPLY
  │
  ├─► Step 4: Check Data-Level Exemptions (§12D-104)
  │     ├─ Identify data categories: HIPAA, GLBA, FCRA, FERPA, DPPA-federal
  │     ├─ Mark exempt data categories
  │     └─ Remaining personal data is subject to DPPA requirements
  │
  └─► Step 5: Document Determination
        ├─ Record assessment date, methodology, and thresholds applied
        ├─ File with privacy program records
        └─ Schedule reassessment for next calendar year
```

## Workflow 2: Consumer Rights Request Processing

```
START: Consumer submits rights request (web portal, email, toll-free number)
  │
  ├─► Step 1: Request Receipt and Logging
  │     ├─ Log: timestamp, request type, channel, consumer identifier
  │     ├─ Assign tracking ID
  │     ├─ Send acknowledgment to consumer within 48 hours
  │     └─ Start 45-day response clock
  │
  ├─► Step 2: Identity Verification
  │     ├─ Authenticated consumer (logged in): match session to account
  │     ├─ Unauthenticated consumer: request 2 data-point verification
  │     ├─ For specific-pieces requests: require 3 data points + declaration
  │     ├─ Do NOT require account creation for verification
  │     └─ If verification fails: deny request, inform consumer of reason
  │
  ├─► Step 3: Route by Request Type
  │     ├─ Access (§12D-106(a)(1)):
  │     │     ├─ Query all systems for consumer's personal data
  │     │     ├─ Compile categories and specific pieces
  │     │     └─ Prepare response in accessible format
  │     ├─ Correction (§12D-106(a)(2)):
  │     │     ├─ Validate correction request against existing records
  │     │     ├─ Update records across all systems
  │     │     └─ Notify processors of correction
  │     ├─ Deletion (§12D-106(a)(3)):
  │     │     ├─ Identify all personal data stores
  │     │     ├─ Check retention obligations (legal, regulatory, contract)
  │     │     ├─ Delete eligible data; retain and document exempt data
  │     │     └─ Propagate deletion to processors and third parties
  │     ├─ Portability (§12D-106(a)(4)):
  │     │     ├─ Extract personal data provided by or collected from consumer
  │     │     ├─ Format as structured, commonly used, machine-readable (JSON)
  │     │     └─ Transmit securely to consumer or designated controller
  │     └─ Opt-Out (§12D-106(a)(5)):
  │           ├─ Apply opt-out to: targeted advertising, sale, profiling
  │           ├─ Update preference across all processing systems
  │           ├─ Notify downstream third parties of opt-out status
  │           └─ No identity verification required for opt-out
  │
  ├─► Step 4: Response
  │     ├─ Respond within 45 days
  │     ├─ If extension needed: notify consumer with reason, extend up to 45 days
  │     ├─ If denying: provide reason and inform of appeal right
  │     └─ Log response date, outcome, and any extension
  │
  └─► Step 5: Appeal Handling (§12D-106(f))
        ├─ Consumer submits appeal within reasonable period
        ├─ Review by senior privacy team member
        ├─ Respond within 60 days
        ├─ If appeal denied: inform consumer of right to contact Delaware AG
        └─ Log appeal and outcome
```

## Workflow 3: Sensitive Data Consent Management

```
START: Processing activity involves sensitive data categories (§12D-102(24))
  │
  ├─► Step 1: Classify Sensitive Data
  │     ├─ Racial or ethnic origin
  │     ├─ Religious beliefs
  │     ├─ Health diagnosis (mental or physical)
  │     ├─ Sexual orientation or sex life
  │     ├─ Citizenship or immigration status
  │     ├─ Genetic data
  │     ├─ Biometric data (for identification)
  │     ├─ Known child data (under 13)
  │     └─ Precise geolocation (within 1,750 feet)
  │
  ├─► Step 2: Design Consent Mechanism
  │     ├─ Clear affirmative act required (not pre-checked box)
  │     ├─ Consent must be freely given, specific, informed, unambiguous
  │     ├─ Must not use dark patterns to obtain consent
  │     ├─ Separate consent per sensitive data category
  │     └─ Clearly state purpose for each sensitive data category
  │
  ├─► Step 3: Collect and Record Consent
  │     ├─ Present consent request at or before point of collection
  │     ├─ Record: consumer ID, timestamp, consent text shown, method, version
  │     ├─ For children under 13: obtain verifiable parental consent per COPPA
  │     └─ For minors 13-17: obtain opt-in consent for targeted ads and sale
  │
  ├─► Step 4: Consent Lifecycle Management
  │     ├─ Allow withdrawal at any time via same ease as granting
  │     ├─ Upon withdrawal: cease processing within 15 business days
  │     ├─ Do not penalize consumer for withdrawal
  │     └─ Retain consent record for duration of processing + 3 years
  │
  └─► Step 5: Audit and Review
        ├─ Quarterly review of consent collection interfaces
        ├─ Verify no dark patterns introduced
        ├─ Confirm consent records are complete and accessible
        └─ Update consent forms when processing purposes change
```

## Workflow 4: Universal Opt-Out Signal Implementation (Effective January 1, 2026)

```
START: Prepare for universal opt-out requirement (§12D-106(a)(5)(c))
  │
  ├─► Step 1: Technical Detection Setup
  │     ├─ Configure web servers to detect Sec-GPC: 1 HTTP header
  │     ├─ Configure mobile apps to check OS-level privacy signals
  │     ├─ Implement server-side signal parsing in request pipeline
  │     └─ Log signal detection events for compliance evidence
  │
  ├─► Step 2: Signal Processing Logic
  │     ├─ GPC signal detected → treat as valid opt-out request
  │     ├─ Apply opt-out to: sale of personal data AND targeted advertising
  │     ├─ If consumer is authenticated: apply account-level opt-out
  │     ├─ If consumer is unauthenticated: apply device/browser-level opt-out
  │     └─ Do NOT require additional confirmation or action from consumer
  │
  ├─► Step 3: Downstream Propagation
  │     ├─ Suppress data sharing with advertising partners for opted-out consumers
  │     ├─ Update consent management platform with GPC opt-out status
  │     ├─ Notify third-party data recipients of opt-out
  │     └─ Ensure real-time tag management respects opt-out
  │
  ├─► Step 4: Conflict Resolution
  │     ├─ GPC signal present but consumer previously opted in via UI:
  │     │     └─ Honor GPC signal (more recent signal prevails)
  │     ├─ GPC signal absent but consumer previously opted out via UI:
  │     │     └─ Maintain existing opt-out
  │     └─ Absence of GPC signal must NOT be interpreted as consent
  │
  └─► Step 5: Testing and Validation
        ├─ Install GPC browser extension and verify detection
        ├─ Test authenticated and unauthenticated flows
        ├─ Verify third-party tag suppression
        ├─ Document test results for AG inquiry readiness
        └─ Schedule quarterly validation
```

## Workflow 5: Data Protection Assessment (§12D-105(b))

```
START: Processing activity identified as requiring DPIA
  │
  ├─► Step 1: Determine If DPIA Required
  │     ├─ Targeted advertising? → YES
  │     ├─ Sale of personal data? → YES
  │     ├─ Profiling with risk of harm? → YES
  │     ├─ Processing sensitive data? → YES
  │     ├─ Processing minor data for non-service purposes? → YES
  │     └─ If none → DPIA not required for this activity
  │
  ├─► Step 2: Describe Processing Activity
  │     ├─ Nature, scope, and context of processing
  │     ├─ Categories of personal data involved
  │     ├─ Categories of consumers affected
  │     ├─ Purpose and necessity of processing
  │     └─ Data flow from collection through deletion
  │
  ├─► Step 3: Assess Benefits
  │     ├─ Benefits to controller (business value, operational necessity)
  │     ├─ Benefits to consumer (service improvement, personalization)
  │     └─ Benefits to public (research, safety, public interest)
  │
  ├─► Step 4: Assess Risks to Consumer
  │     ├─ Risk of unfair or deceptive treatment
  │     ├─ Risk of financial, physical, or reputational injury
  │     ├─ Risk of intrusion on solitude or seclusion
  │     ├─ Risk of discrimination
  │     └─ Consider sensitivity of data and vulnerability of consumers
  │
  ├─► Step 5: Apply Mitigations
  │     ├─ De-identification measures
  │     ├─ Data minimization controls
  │     ├─ Security safeguards
  │     ├─ Consumer transparency mechanisms
  │     └─ Consent mechanisms where applicable
  │
  ├─► Step 6: Weigh and Document
  │     ├─ Benefits must outweigh risks after mitigations
  │     ├─ If benefits do not outweigh: modify or cease processing
  │     ├─ Document assessment methodology and conclusion
  │     └─ Obtain DPO/privacy lead sign-off
  │
  └─► Step 7: Retain and Update
        ├─ Retain DPIA for at least 3 years after processing ends
        ├─ Make available to AG upon request
        ├─ Reassess when processing materially changes
        └─ Annual review of active DPIAs
```

## Workflow 6: Minor Data Processing Compliance

```
START: Processing activity may involve data of consumers under 18
  │
  ├─► Step 1: Age Determination
  │     ├─ Does the service have actual knowledge of consumer age?
  │     ├─ Does the service willfully disregard age information?
  │     ├─ Methods: account registration age, age-gate, parental controls
  │     └─ Classify: under 13, 13-17, 18+, unknown
  │
  ├─► Step 2: Apply Age-Appropriate Controls
  │     ├─ Under 13:
  │     │     ├─ Obtain verifiable parental consent per COPPA
  │     │     ├─ Treat all data as sensitive data
  │     │     └─ No targeted advertising or sale permitted
  │     ├─ 13-17:
  │     │     ├─ Must not process for targeted advertising without opt-in consent
  │     │     ├─ Must not sell personal data without opt-in consent
  │     │     └─ Conduct DPIA for any non-service-related processing
  │     └─ 18+ or Unknown: standard DPPA requirements apply
  │
  ├─► Step 3: Implement Technical Controls
  │     ├─ Age flag in consumer profile system
  │     ├─ Automated suppression of targeted advertising for flagged minors
  │     ├─ Automated suppression of data sale for flagged minors
  │     └─ Consent management records linked to age status
  │
  └─► Step 4: Audit and Evidence
        ├─ Quarterly audit of minor data processing
        ├─ Verify opt-in consent records for 13-17 consumers
        ├─ Verify parental consent records for under-13 consumers
        └─ Document compliance evidence for AG inquiry
```
