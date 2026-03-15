---
name: vendor-breach-cascade
description: >-
  Vendor breach notification cascade management per GDPR Article 33(2). Covers
  processor-to-controller notification without undue delay, escalation paths,
  coordinated multi-party breach response, liability allocation, and regulatory
  notification coordination.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: vendor-privacy-management
  tags: "vendor-breach, art-33, breach-cascade, notification-chain, incident-response"
---

# Vendor Breach Notification Cascade

## Overview

GDPR Article 33(2) requires that a processor notify the controller "without undue delay after becoming aware of a personal data breach." This obligation creates a notification cascade: the processor must notify the controller promptly, enabling the controller to assess and notify the supervisory authority within 72 hours per Article 33(1), and to notify affected data subjects per Article 34 where there is a high risk to their rights and freedoms.

The EDPB Guidelines 9/2022 on personal data breach notification emphasize that "without undue delay" for processor-to-controller notification should be interpreted strictly — the processor should notify as soon as it has established that a breach has occurred, even if full details are not yet available. DPA-specific timeframes (e.g., 24 hours) may be contractually imposed.

At Summit Cloud Partners, the Vendor Breach Notification Cascade Protocol ensures rapid, coordinated response when a vendor reports a personal data breach.

## Notification Chain

### Required Notifications and Timeframes

```
BREACH OCCURS AT VENDOR (PROCESSOR)
         │
         ├─► T+0: Vendor detects breach
         │
         ├─► T+[DPA timeframe]: Vendor notifies Summit Cloud Partners
         │     (DPA standard: within 24 hours of becoming aware)
         │     Required content per DPA:
         │     ├─ Nature of the breach
         │     ├─ Categories and approximate number of data subjects
         │     ├─ Categories and approximate number of records
         │     ├─ DPO/contact point name and details
         │     ├─ Description of likely consequences
         │     └─ Measures taken or proposed
         │
         ├─► T+0 to T+72h (from controller awareness): Summit Cloud Partners
         │     assesses and decides on supervisory authority notification
         │     (Article 33(1): within 72 hours, unless unlikely to result
         │     in risk to data subjects)
         │
         ├─► If high risk to data subjects: Summit Cloud Partners notifies
         │     affected data subjects per Article 34
         │
         └─► If sub-processors involved: Vendor ensures sub-processor
               cascade notification (sub-processor → processor → controller)
```

### Timeframe Requirements

| Notification | GDPR Requirement | Summit Cloud Partners DPA Standard |
|-------------|-----------------|-----------------------------------|
| Processor → Controller | "Without undue delay" (Art. 33(2)) | Within 24 hours of becoming aware |
| Controller → Supervisory Authority | Within 72 hours (Art. 33(1)) | Within 72 hours |
| Controller → Data Subjects | "Without undue delay" (Art. 34(1)) | As soon as practicable after SA notification |
| Sub-processor → Processor | Per sub-processor DPA | Within 12 hours of becoming aware |

## Cascade Response Protocol

### Phase 1: Initial Notification Receipt (T+0 to T+2 hours)

**Upon receiving breach notification from vendor:**

| Step | Action | Responsible | Timeframe |
|------|--------|-------------|-----------|
| 1.1 | Log notification in breach register | Privacy Team on-call | Immediate |
| 1.2 | Verify notification came from authorized vendor contact | Privacy Team | 15 minutes |
| 1.3 | Acknowledge receipt to vendor | Privacy Team | 30 minutes |
| 1.4 | Alert Summit Cloud Partners Breach Response Team | Privacy Team | 30 minutes |
| 1.5 | Classify initial severity | Breach Response Team Lead | 1 hour |
| 1.6 | Activate appropriate response level | Breach Response Team Lead | 1 hour |

**Severity Classification:**

| Level | Criteria | Response Level |
|-------|----------|---------------|
| **Critical** | Special category data exposed; > 10,000 data subjects; criminal access confirmed | Full incident response — all hands |
| **High** | Sensitive data exposed; 1,000-10,000 data subjects; active threat | Expanded response team |
| **Medium** | Standard personal data exposed; < 1,000 data subjects; contained | Core response team |
| **Low** | Limited exposure; pseudonymized data; no evidence of access | Privacy Team + InfoSec lead |

### Phase 2: Assessment and Investigation (T+2 to T+24 hours)

| Step | Action | Responsible |
|------|--------|-------------|
| 2.1 | Request detailed incident report from vendor | Privacy Team |
| 2.2 | Identify affected Summit Cloud Partners data and data subjects | Privacy Team + IT |
| 2.3 | Assess whether breach is "likely to result in a risk" (Art. 33(1) threshold) | DPO |
| 2.4 | Assess whether breach results in "high risk" (Art. 34(1) threshold) | DPO |
| 2.5 | Coordinate with vendor on containment confirmation | InfoSec Team |
| 2.6 | Determine if other controllers are affected (multi-tenant breach) | Privacy Team |
| 2.7 | Engage legal counsel if liability implications exist | Legal Team |
| 2.8 | Draft preliminary supervisory authority notification (if threshold met) | DPO + Legal |

**Vendor Information Requests:**

| Information Required | Purpose |
|---------------------|---------|
| Root cause analysis (even preliminary) | Understand attack vector and likelihood of ongoing risk |
| Exact data categories compromised | Assess risk to data subjects |
| Exact data subject count or best estimate | Determine notification scope |
| Timeline: when breach occurred, when detected, when contained | Assess detection capability |
| Containment measures implemented | Verify threat neutralized |
| Evidence of data exfiltration (yes/confirmed no/unknown) | Critical for risk assessment |
| Impact on other clients (for multi-tenant breach) | Coordination requirement |
| Forensic investigation status and expected completion | Planning input |

### Phase 3: Regulatory Notification Decision (T+24 to T+48 hours)

| Decision | Criteria | Action |
|----------|----------|--------|
| **Notify SA** | Breach likely to result in risk to data subjects | File notification within 72 hours of awareness |
| **Do not notify SA** | Breach unlikely to result in risk (documented assessment) | Document decision and rationale; retain in breach register |
| **Notify in phases** | Cannot provide full details within 72 hours | File initial notification within 72 hours; provide updates as available |

**Article 33(3) Notification Content:**

| Required Element | Description |
|-----------------|-------------|
| (a) | Nature of the breach including categories and approximate number of data subjects and records |
| (b) | Name and contact details of DPO or other contact point |
| (c) | Likely consequences of the breach |
| (d) | Measures taken or proposed to address the breach and mitigate effects |

### Phase 4: Data Subject Notification (if required)

Article 34(1) requires notification to data subjects when the breach "is likely to result in a high risk to the rights and freedoms of natural persons."

**Exemptions (Article 34(3)):**
- Controller has applied encryption or other measures rendering data unintelligible
- Controller has taken subsequent measures ensuring high risk is no longer likely
- It would involve disproportionate effort (in which case, public communication required)

**Notification Content:**
- Nature of the breach in clear, plain language
- DPO/contact point name and details
- Likely consequences
- Measures taken and recommended actions for data subjects

### Phase 5: Coordinated Response and Remediation

| Activity | Responsible | Timeline |
|----------|-------------|----------|
| Monitor vendor's ongoing investigation | Privacy Team | Ongoing |
| Request and review vendor's root cause analysis | Privacy Team + InfoSec | Within 30 days |
| Assess vendor's remediation plan | Privacy Team + InfoSec | Within 30 days |
| Verify remediation implementation | InfoSec | Within 60 days |
| Update vendor risk score | Privacy Team | Immediate |
| Evaluate contractual remedies | Legal Team | Within 30 days |
| Conduct lessons-learned review | Breach Response Team | Within 90 days |

## Liability Allocation

### DPA Liability Provisions

The DPA should address breach-related liability:

| Provision | Description |
|-----------|-------------|
| Processor indemnification | Processor indemnifies controller for losses caused by processor breach (including fines to the extent legally permissible) |
| Cooperation obligation | Processor must cooperate fully with controller's investigation and regulatory notifications |
| Forensic costs | Allocation of forensic investigation costs |
| Notification costs | Allocation of data subject notification costs |
| Credit monitoring | Allocation of credit monitoring / identity protection costs for affected data subjects |
| Regulatory engagement | Processor must participate in regulatory inquiries |
| Limitation of liability | Carve-out for data protection breaches from general liability caps (where negotiable) |

### GDPR Liability Framework

- **Article 82(1)**: Any person who has suffered material or non-material damage as a result of GDPR infringement has the right to compensation from the controller or processor.
- **Article 82(2)**: A processor is liable only where it has not complied with processor-specific GDPR obligations or has acted outside or contrary to controller instructions.
- **Article 82(3)**: A controller or processor is exempt from liability if it can prove it is not responsible for the event giving rise to the damage.
- **Article 82(4)**: Where multiple controllers or processors are involved, each is liable for the entirety of the damage — with contribution rights against co-liable parties.

## Multi-Vendor Breach Coordination

When a breach at a sub-processor or infrastructure provider affects multiple processors and controllers:

| Role | Responsibilities |
|------|-----------------|
| **Sub-processor** | Notify all affected processors; provide consistent information |
| **Processor (Vendor)** | Notify all affected controllers; coordinate information flow |
| **Controller (Summit Cloud Partners)** | Assess own impact; make own regulatory notification decisions |
| **Lead Supervisory Authority** | May coordinate cross-border notifications if multiple EU/EEA controllers affected |

## Key Regulatory References

- GDPR Article 33(1) — Controller notification to supervisory authority within 72 hours
- GDPR Article 33(2) — Processor notification to controller "without undue delay"
- GDPR Article 33(3) — Content of supervisory authority notification
- GDPR Article 34 — Communication of breach to data subjects
- GDPR Article 82 — Right to compensation and liability
- EDPB Guidelines 9/2022 — Personal data breach notification under GDPR
- EDPB Guidelines 01/2021 — Examples regarding data breach notification
