# Cloud Storage Retention Configuration Workflows

## Workflow 1: New Cloud Storage Resource Retention Setup

```
[New S3 Bucket / Azure Container / GCS Bucket Created]
         │
         ▼
[Identify Data Categories to be Stored]
         │
         ▼
[Look Up Retention Schedule for Each Category]
         │
         ▼
[Configure Retention Controls]
   │
   ├── AWS S3:
   │     ├── Create lifecycle rules (transitions + expiration)
   │     ├── Enable Object Lock (Governance or Compliance mode)
   │     ├── Enable versioning
   │     └── Enable CloudTrail logging
   │
   ├── Azure Blob:
   │     ├── Create lifecycle management rules
   │     ├── Configure immutability policy (if required)
   │     ├── Enable soft delete
   │     └── Enable diagnostic logging
   │
   └── GCP GCS:
         ├── Set bucket-level retention policy
         ├── Configure lifecycle rules
         ├── Consider policy locking (if mandatory retention)
         └── Enable Cloud Audit Logs
         │
         ▼
[Enable Cross-Region Replication (if required)]
   - Configure identical retention on destination
   - Enable delete marker replication
   - Set up legal hold propagation
         │
         ▼
[Document Configuration]
   - Record in cloud infrastructure inventory
   - Link to retention schedule entry
   - Tag resources with data-category metadata
         │
         ▼
[Monthly Compliance Verification]
   - Policy drift detection
   - Configuration audit
```

## Workflow 2: Legal Hold Application on Cloud Storage

```
[Litigation Hold Notice Received]
         │
         ▼
[Identify Cloud Storage Objects in Scope]
   - By prefix, tag, date range, or specific object keys
         │
         ▼
[Apply Legal Hold]
   │
   ├── AWS S3: PutObjectLegalHold (Status=ON) for each object
   ├── Azure Blob: Set legal hold tag on container
   └── GCP GCS: Set temporary hold on objects
         │
         ▼
[Record in Litigation Hold Register]
   - Cloud platform, bucket/container, objects/prefixes held
   - Hold reference, date applied
         │
         ▼
[Monitor Hold]
   - Verify holds remain active (monthly)
   - Prevent accidental removal
         │
         ▼
[Hold Release]
   ├── Legal counsel authorizes release
   ├── Remove holds from cloud objects
   ├── Resume normal lifecycle/retention
   └── Update litigation hold register
```

## Workflow 3: Cross-Region Retention Alignment Audit

```
[Quarterly Audit Trigger]
         │
         ▼
[For Each Replicated Storage Resource]
   │
   ├── [Source retention config matches destination?]
   │     ├── Yes ──► Compliant
   │     └── No ──► FLAG — remediate immediately
   │
   ├── [Delete marker replication enabled?]
   │     ├── Yes ──► Compliant
   │     └── No ──► FLAG — data not being deleted in DR region
   │
   ├── [Legal hold propagation configured?]
   │     ├── Yes ──► Compliant
   │     └── No ──► FLAG — legal holds not applied to replicas
   │
   └── [Replication lag within SLA?]
         ├── Yes ──► Compliant
         └── No ──► FLAG — investigate replication backlog
         │
         ▼
[Generate Audit Report]
[Remediate Flagged Items]
```
