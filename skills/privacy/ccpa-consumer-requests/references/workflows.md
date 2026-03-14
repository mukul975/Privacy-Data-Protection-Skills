# CCPA Consumer Request Workflows

## Workflow 1: Request Intake and Triage

```
[Consumer Request Received]
   (toll-free number, web form, email)
         │
         ▼
[Log CCPA-YYYY-NNNN]
   - Request type (know/delete/correct/opt-out/limit)
   - Consumer identity information
   - Channel of receipt
   - Timestamp
         │
         ▼
[Acknowledge Within 10 Business Days]
   - Confirm receipt
   - Explain the request process
   - Provide expected timeline
         │
         ▼
[Route by Request Type]
   ├── Right to know ──► Identity verification (reasonable/high certainty)
   ├── Right to delete ──► Identity verification (reasonable certainty)
   ├── Right to correct ──► Identity verification (reasonable certainty)
   ├── Right to opt-out ──► No verification needed
   └── Right to limit sensitive PI ──► No verification needed
```

## Workflow 2: Identity Verification

```
[Verification Required]
         │
         ▼
[Consumer Has Account?]
   ├── Yes ──► Verify through existing authentication
   │
   └── No ──► [Request Type?]
               ├── Categories only ──► Match 2 data points
               ├── Specific pieces ──► Match 3 data points + declaration
               ├── Delete ──► Match 2 data points
               └── Correct ──► Match 2 data points
         │
         ▼
[Verification Successful?]
   ├── Yes ──► Proceed with request
   ├── Partial ──► May provide categories only (not specific pieces)
   └── Failed ──► Notify consumer, request additional information
                   If still unable to verify, deny specific pieces request
                   (may still provide category-level information)
```

## Workflow 3: Right to Know Processing

```
[Verification Complete]
         │
         ▼
[Collect Data from All Systems]
   - CRM, billing, analytics, marketing, support, logs
         │
         ▼
[Organize by CCPA Category]
   - Identifiers
   - Customer records
   - Protected classifications
   - Commercial information
   - Internet activity
   - Geolocation
   - Professional information
   - Inferences
   - Sensitive PI
         │
         ▼
[For Each Category, Disclose:]
   - Categories of PI collected
   - Sources
   - Business/commercial purpose
   - Third parties disclosed to
   - Specific pieces (if requested + high verification met)
         │
         ▼
[Format Response]
   - Portable, readily useable format
   - Cover last 12 months
   - Deliver within 45 days (extendable to 90 with notice)
```

## Workflow 4: Opt-Out of Sale/Sharing

```
[Opt-Out Request Received]
   (no verification needed)
         │
         ▼
[Cease Sale/Sharing Within 15 Business Days]
   │
   ├── Remove from advertising audiences
   ├── Remove from data sharing arrangements
   ├── Remove from data broker feeds
   ├── Update CRM: do_not_sell = TRUE
   └── Notify downstream third parties
         │
         ▼
[Confirm to Consumer]
         │
         ▼
[Do Not Sell/Share for at Least 12 Months]
   - Only re-enable if consumer provides affirmative authorization
```
