# DSAR Processing Workflows

## Workflow 1: Standard DSAR End-to-End Process

```
[Request Received] ──► [Log in Register] ──► [Send Acknowledgement]
         │
         ▼
[Identity Verification]
   ├── Pass ──► [Scope Assessment]
   │                    │
   │                    ▼
   │            [System Data Collection]
   │                    │
   │                    ▼
   │            [Exemption Review]
   │                    │
   │                    ▼
   │            [Response Compilation]
   │                    │
   │                    ▼
   │            [QA Review & DPO Sign-off]
   │                    │
   │                    ▼
   │            [Secure Delivery]
   │                    │
   │                    ▼
   │            [Close & Archive]
   │
   └── Fail ──► [Request Additional ID] ──► [Clock Paused]
                        │
                        ▼
                [ID Provided?]
                  ├── Yes ──► [Resume at Scope Assessment]
                  └── No (30 days) ──► [Close as Unverified]
```

## Workflow 2: Extension Decision Process

```
[Initial Assessment Complete]
         │
         ▼
[Is request complex?]
   ├── Multiple systems involved (>5 data stores) ──► Consider Extension
   ├── Large volume of data (>10,000 records) ──► Consider Extension
   ├── Multiple concurrent DSARs from same subject ──► Consider Extension
   ├── Significant redaction required ──► Consider Extension
   └── None of the above ──► Standard 30-day timeline
         │
         ▼
[Extension Required?]
   ├── Yes ──► [Notify data subject within 30 days]
   │              - State the extension period (max +60 days)
   │              - Provide specific reasons for the delay
   │              - Confirm the new expected response date
   │
   └── No ──► [Proceed with standard timeline]
```

## Workflow 3: Fee or Refusal Assessment

```
[DSAR Received]
         │
         ▼
[Is request manifestly unfounded?]
   ├── Requester stated disruptive intent ──► [Document evidence]
   ├── No legitimate purpose identified ──► [Document reasoning]
   └── Request appears genuine ──► [Process normally]
         │
         ▼
[Is request excessive?]
   ├── Repetitive: identical request within 6 months ──► [Count prior requests]
   │     └── 4+ identical requests in 12 months ──► [Excessive threshold met]
   └── Not repetitive ──► [Process normally]
         │
         ▼
[Manifestly unfounded OR excessive?]
   ├── Yes ──► [Choose: Charge Fee OR Refuse]
   │     ├── Charge Fee ──► [Calculate: GBP 10 + GBP 0.10/page over 500]
   │     │                    └── [Notify subject of fee and basis]
   │     └── Refuse ──► [Notify subject with: reasons, right to complain to SA, right to judicial remedy]
   │
   └── No ──► [Process at no charge]
```

## Workflow 4: Exemption Application Process

```
[Data Compiled for Response]
         │
         ▼
[Review each data item]
         │
         ├── Contains third-party personal data?
         │     └── Yes ──► [Redact third-party identifiers]
         │                  [Document: Art. 15(4) applied]
         │
         ├── Subject to legal privilege?
         │     └── Yes ──► [Withhold entirely]
         │                  [Document: Legal privilege exemption]
         │
         ├── Confidential reference?
         │     └── Yes ──► [Withhold entirely]
         │                  [Document: Confidential reference exemption]
         │
         ├── Management forecasting data?
         │     └── Yes ──► [Assess prejudice to business]
         │                  [If prejudicial: withhold. Document basis]
         │
         └── Negotiation records?
               └── Yes ──► [Assess prejudice to negotiations]
                            [If prejudicial: withhold. Document basis]
         │
         ▼
[Generate redaction log]
   - Item reference
   - Exemption applied
   - Legal basis citation
   - Approver name and date
```

## Workflow 5: Secure Delivery Decision

```
[Response Ready for Delivery]
         │
         ▼
[Original request channel?]
   ├── Customer portal ──► [Upload to secure portal, notify via portal message]
   ├── Email ──► [Encrypted email with password-protected ZIP]
   │              [Send password via SMS or separate email]
   ├── Postal mail ──► [Print, seal in tamper-evident envelope]
   │                    [Send via registered/tracked post]
   └── In-person ──► [Schedule secure handover appointment]
                      [Verify identity at handover]
         │
         ▼
[Record delivery confirmation]
   - Delivery timestamp
   - Delivery method
   - Confirmation reference (tracking number, read receipt, portal log)
```
