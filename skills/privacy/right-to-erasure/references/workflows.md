# Right to Erasure Workflows

## Workflow 1: Erasure Request Assessment

```
[Erasure Request Received]
         │
         ▼
[Identity Verification]
   ├── Verified ──► [Identify Erasure Ground]
   │                    │
   │                    ├── Art. 17(1)(a): Purpose fulfilled?
   │                    ├── Art. 17(1)(b): Consent withdrawn?
   │                    ├── Art. 17(1)(c): Successful objection?
   │                    ├── Art. 17(1)(d): Unlawful processing?
   │                    ├── Art. 17(1)(e): Legal obligation to erase?
   │                    └── Art. 17(1)(f): Child's data (ISS)?
   │                    │
   │                    ▼
   │            [Ground Established?]
   │              ├── Yes ──► [Check Exceptions]
   │              └── No ──► [Refuse with reasons + right to complain]
   │
   └── Not Verified ──► [Request ID, pause clock]
```

## Workflow 2: Exception Assessment

```
[Erasure Ground Established]
         │
         ▼
[Check Each Exception]
   │
   ├── Art. 17(3)(a): Freedom of expression?
   │     └── [Assess: Is data part of journalism/public discourse?]
   │
   ├── Art. 17(3)(b): Legal obligation to retain?
   │     └── [Check: Companies Act (6y), HMRC (6y), MLR (5y), etc.]
   │
   ├── Art. 17(3)(c): Public health necessity?
   │     └── [Assess: Art. 9(2)(h)/(i) applicability]
   │
   ├── Art. 17(3)(d): Archiving/research?
   │     └── [Assess: Would erasure make research impossible?]
   │
   └── Art. 17(3)(e): Legal claims?
         └── [Check: Pending litigation, regulatory investigation, litigation hold?]
         │
         ▼
[Any Exception Applies?]
   ├── Full exception ──► [Refuse erasure, cite specific exception, notify rights]
   ├── Partial exception ──► [Erase non-excepted data, retain excepted data]
   └── No exception ──► [Proceed to erasure execution]
```

## Workflow 3: Technical Erasure Execution

```
[Erasure Approved]
         │
         ▼
[Inventory All Data Locations]
   │
   ├── Primary Databases
   │     └── Execute DELETE/PURGE operations
   │
   ├── Data Warehouse / Analytics
   │     └── Remove from data lake, update ETL exclusion list
   │
   ├── Application Caches
   │     └── Flush cache entries, invalidate CDN objects
   │
   ├── Email / Communication Systems
   │     └── Delete correspondence, purge from sent/received
   │
   ├── Backup Systems
   │     └── Flag for deletion at next rotation cycle
   │         Document expected completion (max 90 days)
   │
   ├── Third-Party Processors
   │     └── Issue Art. 19 notification
   │         Request confirmation within 14 days
   │
   └── Public-Facing Systems (if Art. 17(2) applies)
         └── Submit de-indexing requests to search engines
             Remove from public websites / APIs
         │
         ▼
[Verification Sweep]
   - Query all systems for residual data
   - Confirm third-party deletion confirmations received
   - Log verification results
         │
         ▼
[Erasure Complete — Notify Data Subject]
```

## Workflow 4: Third-Party Notification Under Art. 19

```
[Erasure Executed]
         │
         ▼
[Retrieve Art. 30 Recipient List]
         │
         ▼
[For Each Recipient]
   │
   ├── Send erasure notification
   │     - Subject reference (pseudonymised)
   │     - Data categories to erase
   │     - Legal basis for erasure
   │     - 14-day confirmation deadline
   │
   ├── Track response
   │     ├── Confirmed ──► Log confirmation date
   │     ├── Partial ──► Follow up, document scope
   │     └── No response (14 days) ──► Escalate, send reminder
   │
   └── [All recipients processed?]
         ├── Yes ──► Update erasure record
         └── No ──► Continue processing
         │
         ▼
[Data subject requests recipient list?]
   ├── Yes ──► Provide list of notified recipients
   └── No ──► Close notification workflow
```
