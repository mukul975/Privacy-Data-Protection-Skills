# Data Classification Label Configuration Record

## Organisation: Vanguard Financial Services
## Reference: LBL-CFG-2026-001
## Date: 2026-03-14
## Configured By: Michael Chen, Privacy Engineering Lead
## Approved By: Dr. James Whitfield, DPO

---

## Label: Restricted - Special Category (Art. 9)

| Setting | Value |
|---------|-------|
| **Label ID** | LBL-REST-SC |
| **Display Name** | Restricted - Special Category (Art. 9) |
| **Parent Label** | Restricted |
| **Colour** | Red (#CC0000) |
| **Tooltip** | Apply this label to data containing GDPR Art. 9 special category data (health, biometric, genetic, racial/ethnic origin, political, religious, trade union, sexual orientation). This data requires the highest level of protection. |

### Visual Markings

| Marking | Setting |
|---------|---------|
| **Header** | Text: "RESTRICTED"; Colour: Red (#CC0000); Size: 12pt; Alignment: Centre |
| **Footer** | Text: "RESTRICTED — Art. 9 Special Category Data — Vanguard Financial Services"; Colour: Red; Size: 10pt |
| **Watermark** | Text: "RESTRICTED"; Colour: Light red (50% opacity); Diagonal; Applied on print only |

### Encryption

| Setting | Value |
|---------|-------|
| **Encryption enabled** | Yes |
| **Encryption type** | Azure Rights Management — Double Key Encryption (DKE) |
| **Permissions** | View, Edit — VFS-Restricted-Users security group only; No forward, no print, no copy (default) |
| **Offline access** | 7 days maximum |
| **Content expiry** | None (controlled by retention policy) |

### Auto-Labelling Policy

| Setting | Value |
|---------|-------|
| **Policy Name** | VFS-AutoLabel-Restricted-SpecialCategory |
| **Conditions** | Content contains ANY of: ICD-10 code (MEDIUM confidence), Health terminology trainable classifier (HIGH), Biometric template format (HIGH), Genetic marker rs-number (HIGH) |
| **Minimum instances** | 1 |
| **Confidence threshold** | 70% minimum |
| **Priority** | 1 (highest — overrides lower-priority auto-labels) |
| **Simulation mode** | Disabled (production active) |
| **Simulation results** | 4,281 items would be labelled (validated in 30-day simulation Feb 2026) |

### DLP Policies

| Policy | Rule | Action |
|--------|------|--------|
| VFS-DLP-Restricted-Email | Restricted label detected in email to external recipient | Block send; notify sender; alert DPO |
| VFS-DLP-Restricted-SharePoint | Restricted content shared with external user | Block sharing; audit log; alert DPO |
| VFS-DLP-Restricted-Endpoint | Restricted content copied to USB/removable media | Block copy; audit log; alert Security |
| VFS-DLP-Restricted-Print | Restricted content sent to printer | Block print (unless DPO exception); watermark if allowed |

### Label Audit Metrics (Last 30 Days)

| Metric | Value |
|--------|-------|
| Total items with this label | 4,281 |
| Auto-applied | 3,847 (89.9%) |
| User-applied | 434 (10.1%) |
| Downgrade requests | 12 |
| Downgrades approved | 3 (false positive confirmations) |
| Downgrades rejected | 9 |
| DLP blocks triggered | 47 |

---

*Label configuration maintained per Vanguard Data Classification Policy DCP-2026-v1.0. Reviewed quarterly by Privacy Engineering and DPO.*
