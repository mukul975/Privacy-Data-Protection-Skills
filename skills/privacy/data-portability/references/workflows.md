# Data Portability Workflows

## Workflow 1: Portability Scope Assessment

```
[Portability Request Received]
         │
         ▼
[Identify All Data Held About Subject]
         │
         ▼
[For Each Data Category]
   │
   ├── Was data provided by subject or observed? ──► IN SCOPE
   │     (account info, uploads, activity logs, preferences)
   │
   ├── Was data inferred or derived by controller? ──► OUT OF SCOPE
   │     (profiling scores, analytics outputs, risk assessments)
   │
   └── [Apply Legal Basis Filter]
         │
         ├── Processed under Art. 6(1)(a) consent? ──► PORTABLE
         ├── Processed under Art. 9(2)(a) explicit consent? ──► PORTABLE
         ├── Processed under Art. 6(1)(b) contract? ──► PORTABLE
         └── Other legal basis (c/d/e/f)? ──► NOT PORTABLE
         │
         ▼
[Check automated processing requirement]
   ├── Automated means? ──► PORTABLE
   └── Manual paper processing only? ──► NOT PORTABLE
         │
         ▼
[Check third-party rights (Art. 20(3))]
   ├── Contains other people's data? ──► REDACT
   └── No third-party data ──► INCLUDE AS-IS
```

## Workflow 2: Format Selection and Packaging

```
[Scope Determined]
         │
         ▼
[Data Subject Specified Format?]
   ├── Yes ──► [Format supported?]
   │             ├── Yes ──► Use requested format
   │             └── No ──► Notify subject, offer alternatives
   │
   └── No ──► [Receiving controller specified format?]
               ├── Yes ──► Use controller's format
               └── No ──► Default to JSON
         │
         ▼
[Extract and Format Data]
   │
   ├── Account Data ──► account_data.{format}
   ├── Transaction History ──► transactions.{format}
   ├── User Content ──► content_uploads.{format}
   ├── Activity Logs ──► activity_logs.{format}
   └── Preferences ──► preferences.{format}
         │
         ▼
[Generate manifest.json]
   - File list with checksums (SHA-256)
   - Record counts per file
   - Date range of data
   - Schema version
   - Export timestamp
         │
         ▼
[Package into encrypted ZIP (AES-256)]
```

## Workflow 3: Direct Controller-to-Controller Transfer

```
[Direct Transfer Requested]
         │
         ▼
[Verify Receiving Controller]
   - Confirm organisation identity
   - Obtain technical contact
   - Verify data subject's authorisation for transfer
         │
         ▼
[Negotiate Transfer Mechanism]
   │
   ├── API Available?
   │     └── Yes ──► HTTPS + mutual TLS
   │                  POST data to receiving endpoint
   │                  Await HTTP 200/201 confirmation
   │
   ├── SFTP Available?
   │     └── Yes ──► SSH key exchange
   │                  Upload encrypted archive
   │                  Verify receipt via SFTP listing
   │
   └── Neither Available
         └── Secure portal upload
             Time-limited access (72 hours)
             Credential delivery to receiving controller
         │
         ▼
[Transfer Successful?]
   ├── Yes ──► Log confirmation, notify data subject
   └── No ──► [Technically Feasible?]
               ├── Retry (max 3 attempts) ──► Success? Log and notify
               └── Not feasible ──► Notify data subject per Art. 20(2)
                                     Provide data directly to subject instead
```

## Workflow 4: Self-Export Delivery

```
[Self-Export Requested]
         │
         ▼
[Upload encrypted archive to secure portal]
         │
         ▼
[Send notification to data subject]
   - Secure download link (72-hour expiry)
   - File manifest summary
   - Format documentation/schema reference
         │
         ▼
[Send decryption password via separate channel]
   - SMS to verified mobile number, OR
   - Secondary email address
         │
         ▼
[Data subject downloads?]
   ├── Yes ──► Log download timestamp, close request
   └── No (72 hours) ──► Send reminder
                           │
                           ├── Downloaded after reminder ──► Close
                           └── Not downloaded (7 days total) ──► Close, note in register
```
