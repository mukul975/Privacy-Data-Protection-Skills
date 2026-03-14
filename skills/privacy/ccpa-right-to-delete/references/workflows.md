# CCPA Right to Delete Workflows

## Workflow 1: Deletion Request Processing

```
[Consumer Deletion Request Received]
   (Via designated channels: online form, toll-free number, email)
         │
         ▼
[Acknowledge Receipt (within 10 business days)]
         │
         ▼
[Identity Verification]
   │
   ├── Account holder (logged in) ──► Verified
   │
   ├── Account holder (not logged in) ──► Request login or 2 data points
   │     ├── Match ──► Verified
   │     └── No match ──► Request additional info or deny
   │
   └── Non-account holder ──► 2 data points (standard) or 3 + declaration (sensitive)
         ├── Match ──► Verified
         └── No match ──► Deny with right to appeal
         │
         ▼
[Authorized Agent Check (if applicable)]
   - Verify written permission or power of attorney
   - May still require direct consumer verification
         │
         ▼
[Identify All PI Categories Held]
   - Inventory personal information across all systems
         │
         ▼
[Exception Assessment Per Category]
   ├── (d)(1) Active transaction? ──► Retain
   ├── (d)(2) Security investigation? ──► Retain
   ├── (d)(3) Debug needed? ──► Retain
   ├── (d)(4) Free speech? ──► Retain
   ├── (d)(5) Research? ──► Retain
   ├── (d)(6) Internal use aligned? ──► Retain
   ├── (d)(7) Legal obligation? ──► Retain
   ├── (d)(8) Lawful internal use? ──► Retain
   ├── (d)(9) Other law? ──► Retain
   └── No exception ──► DELETE
         │
         ▼
[Execute Deletion]
   - Delete from business systems
   - Direct service providers/contractors to delete
   - Notify third parties (if sold/shared)
         │
         ▼
[Respond to Consumer (within 45 days)]
   - What was deleted
   - What was retained (with exception citation)
   - Service provider/third party actions taken
```

## Workflow 2: Service Provider Deletion Flow-Down

```
[Business Directs Service Provider to Delete]
         │
         ▼
[Service Provider Receives Direction]
         │
         ▼
[Service Provider Assesses Own Exceptions]
   ├── Exception applies ──► Notify business within 5 business days
   └── No exception ──► Proceed with deletion
         │
         ▼
[Delete Consumer PI from Service Provider Systems]
         │
         ▼
[Direct Sub-Service Providers to Delete]
         │
         ▼
[Confirm Deletion to Business (within 20 business days)]
         │
         ▼
[Business Logs Confirmation]
```

## Workflow 3: Consumer Appeal Process

```
[Consumer Disputes Deletion Denial]
         │
         ▼
[Appeal Received]
         │
         ▼
[Senior Privacy Analyst Reviews]
   - Re-assess exception cited
   - Re-verify consumer identity if needed
   - Consider additional information from consumer
         │
         ▼
[Appeal Decision]
   ├── Upheld (original denial correct) ──► Inform consumer; cite CPPA complaint right
   ├── Overturned (delete now) ──► Execute deletion; inform consumer
   └── Partial (additional categories now deleted) ──► Execute partial; inform consumer
         │
         ▼
[Document Appeal and Outcome]
[Update Metrics]
```
