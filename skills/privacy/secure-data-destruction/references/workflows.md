# Secure Data Destruction Workflows

## Workflow 1: In-House Destruction Process

```
[Asset Identified for Destruction]
         │
         ▼
[Check Litigation Hold Register]
   ├── Hold active ──► STOP — do not destroy
   └── No hold ──► Proceed
         │
         ▼
[Determine Data Classification]
   ├── Standard personal data ──► Level: CLEAR (reuse) or DESTROY (disposal)
   ├── Special category data ──► Level: PURGE (reuse within org) or DESTROY
   └── Highly sensitive ──► Level: DESTROY (mandatory)
         │
         ▼
[Collect Asset with Chain of Custody]
   - Signed handover form
   - Sealed tamper-evident container
   - Logged in destruction register
         │
         ▼
[Execute Sanitization]
   ├── CLEAR: ATA Secure Erase → Log → Verify
   ├── PURGE: Degauss/Crypto Erase → Log → Verify
   └── DESTROY: Shred/Disintegrate → Visual Inspect → Dispose
         │
         ▼
[Verification by Independent Officer]
   ├── PASS ──► Generate Certificate of Destruction
   └── FAIL ──► Escalate to next sanitization level
         │
         ▼
[Certificate of Destruction Issued]
[Asset Register Updated]
[Filed in Destruction Records (7 years)]
```

## Workflow 2: Third-Party Destruction Service

```
[Destruction Batch Ready for Collection]
         │
         ▼
[Prepare Collection Manifest]
   - List all assets by serial number
   - Record data classification per asset
   - Seal in tamper-evident containers
   - Affix tracking barcodes
         │
         ▼
[Vendor Collection]
   - Verify driver identity
   - Signed manifest handover
   - GPS-tracked transport
         │
         ▼
[Destruction Execution]
   ├── On-site (witnessed by org representative)
   └── Off-site (video evidence provided within 24h)
         │
         ▼
[Certificate of Destruction Received]
   - Cross-reference against manifest (100% match required)
   - Verify: method, particle size, date, personnel
         │
         ▼
[WEEE Disposal]
   - Destroyed material to licensed recycler
   - Waste transfer note retained
         │
         ▼
[File Documentation (7 years)]
```

## Workflow 3: Vendor Annual Audit

```
[Annual Audit Scheduled]
         │
         ▼
[Pre-Audit Document Review]
   - Current certifications (ISO 27001, EN 15713, ADISA)
   - Insurance certificates
   - Incident register
   - Personnel vetting records
         │
         ▼
[On-Site Audit]
   - Premises security inspection
   - Equipment inspection (shredder calibration, degausser field strength)
   - Process observation (collection, transport, destruction, disposal)
   - Staff interviews
   - Record-keeping review
         │
         ▼
[Audit Report]
   ├── No findings ──► Continue engagement
   ├── Minor findings ──► Remediation plan (30 days)
   ├── Major findings ──► Remediation plan (14 days) + increased monitoring
   └── Critical findings ──► Suspend engagement; switch to alternative vendor
```
