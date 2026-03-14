# Direct Marketing Objection Workflows

## Workflow 1: Marketing Objection Processing

```
[Marketing Objection Received]
   (via any channel: unsubscribe link, email, phone, web form, letter)
         │
         ▼
[Log MKT-YYYY-NNNN + Confirm Identity Match]
   (No full ID verification needed — just match to marketing recipient)
         │
         ▼
[Determine Scope]
   ├── Full opt-out (all channels) ──► Suppress ALL marketing
   ├── Partial opt-out (specific channels) ──► Suppress specified channels
   └── Unclear ──► Treat as full opt-out, clarify later
         │
         ▼
[Immediate Cessation (within 24 hours)]
   │
   ├── Email: Remove from lists, suppress address
   ├── SMS: Remove from lists, suppress number
   ├── Telephone: Add to do-not-call list
   ├── Postal: Remove from mailing lists
   ├── Online ads: Remove from remarketing audiences
   └── Profiling: Cease marketing profiling
         │
         ▼
[Add to Suppression List]
   - Hash identifiers (SHA-256)
   - Record suppression date
   - Record scope (full/partial + channels)
         │
         ▼
[Cross-Channel Enforcement]
   - Update CRM
   - Update marketing platforms
   - Update advertising platforms
   - Notify third-party marketing processors
         │
         ▼
[Confirm to Data Subject (within 14 days)]
```

## Workflow 2: Suppression List Pre-Campaign Check

```
[Marketing Campaign Prepared]
         │
         ▼
[Load Suppression List]
         │
         ▼
[For Each Intended Recipient]
   │
   ├── On suppression list?
   │     ├── Full suppression ──► EXCLUDE from campaign
   │     └── Channel-specific suppression
   │           ├── This channel suppressed? ──► EXCLUDE
   │           └── This channel not suppressed? ──► INCLUDE
   │
   └── Not on suppression list ──► INCLUDE
         │
         ▼
[Suppression Applied — Generate Audit Report]
   - Total intended recipients
   - Total suppressed
   - Final distribution list count
   - Suppression rate percentage
         │
         ▼
[Approve Campaign for Distribution]
```

## Workflow 3: New Data Import Screening

```
[New Customer Data Import]
         │
         ▼
[Screen Against Suppression List]
   - Match on hashed email
   - Match on hashed phone
   - Match on normalised postal address
         │
         ▼
[Match Found?]
   ├── Yes ──► Set marketing_consent = FALSE
   │            Set marketing_suppressed = TRUE
   │            Allow non-marketing processing only
   │
   └── No ──► Process according to consent status
```
