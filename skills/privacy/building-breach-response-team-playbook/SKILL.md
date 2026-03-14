---
name: building-breach-response-team-playbook
description: >-
  Builds a comprehensive breach response team playbook defining CSIRT and privacy
  team structure with named roles (incident commander, legal counsel, communications,
  IT forensics, DPO), escalation matrices, communication templates, pre-negotiated
  vendor contacts, and regulatory authority contacts organized by jurisdiction.
  Keywords: breach response playbook, CSIRT, incident response team, escalation
  matrix, communication templates, vendor contacts.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-breach-response
  tags: "breach-playbook, csirt, incident-response-team, escalation-matrix, communication-templates"
---

# Building Breach Response Team Playbook

## Overview

A breach response team playbook is the operational manual that enables rapid, coordinated response when a personal data breach occurs. It pre-defines roles and responsibilities, escalation paths, communication templates, and external contact information so that the response team can act immediately without spending critical hours on logistics during an actual incident.

## Team Structure — CSIRT + Privacy Integration

### Core Response Team

| Role | Primary | Backup | Contact | Responsibility |
|------|---------|--------|---------|---------------|
| Incident Commander (IC) | Thomas Brenner (CISO) | Marcus Weber (SOC Lead) | +49 30 7742 8100 / ic@stellarpayments.eu | Overall coordination, resource allocation, containment decisions |
| Data Protection Officer | Dr. Elena Vasquez | Anna Schmidt (Deputy DPO) | +49 30 7742 8001 / dpo@stellarpayments.eu | Notification decisions, risk assessment, regulatory liaison, data subject communication |
| Legal Counsel | Sarah Chen (General Counsel) | External: Dr. Klaus Fischer (Freshfields) | +49 30 7742 8200 / legal@stellarpayments.eu | Legal advice, privilege management, regulatory strategy, law enforcement coordination |
| IT Forensics Lead | Petra Hoffmann (IT Director) | External: Sarah Mitchell (Mandiant) | +49 30 7742 8300 / it-forensics@stellarpayments.eu | Evidence preservation, forensic investigation, scope determination, root cause analysis |
| Communications Lead | Martin Keller (Comms Director) | Lisa Braun (Senior Comms Manager) | +49 30 7742 8400 / comms@stellarpayments.eu | Media response, customer communication, internal communication, social media monitoring |
| Executive Sponsor | Marcus Lindqvist (CEO) | CFO: Dr. Andrea Hoffmann | +49 30 7742 8000 / ceo@stellarpayments.eu | Strategic decisions, board notification, public statements, regulatory engagement |
| Customer Relations | James Park (VP Customer Success) | Maria Santos (Customer Success Director) | +49 30 7742 5000 / customers@stellarpayments.eu | Customer inquiry management, B2B client communication, service status updates |
| HR Lead | Claudia Richter (CHRO) | Stefan Müller (HR Director) | +49 30 7742 7500 / hr-confidential@stellarpayments.eu | Employee communication, Works Council coordination, insider threat scenarios |

### Extended Team (Activated as Needed)

| Role | Contact | Activation Trigger |
|------|---------|-------------------|
| Board Liaison | Board Secretary (Dr. Friedrich Weber) | Breach affecting 10,000+ data subjects or likely to result in high risk |
| Cyber Insurance | Allianz Claims: +49 89 3800 0 (ref: SPG-CYB-2025-001) | Any breach likely to exceed EUR 50,000 in response costs |
| External IR Firm | Mandiant: +1 703 935 1700 (retainer: SPG-IR-2025-007) | Any breach requiring forensic investigation beyond SOC capability |
| External Legal | Freshfields: +49 30 20 28 39 000 (ref: SPG-LEG-2025-012) | Breach involving regulatory risk, litigation risk, or cross-border notification |
| External Communications | Brunswick Group: +49 69 2400 5510 | Breach with media exposure or affecting 50,000+ individuals |
| Credit Monitoring Vendor | Experian Enterprise: +44 115 941 0888 (retainer: SPG-EXP-2025-003) | Breach involving financial data, government IDs, or health data |

## Escalation Matrix

### Severity Classification

| Severity | Criteria | Response Time | Escalation Level |
|----------|----------|---------------|-----------------|
| SEV-1 (Critical) | 10,000+ data subjects; special category data (Art. 9); ongoing exfiltration; ransomware with encryption | Immediate (within 15 minutes) | IC + DPO + CEO + General Counsel |
| SEV-2 (High) | 1,000-10,000 data subjects; financial data; credentials; media exposure | Within 30 minutes | IC + DPO + General Counsel |
| SEV-3 (Medium) | 100-1,000 data subjects; non-sensitive personal data; contained breach | Within 2 hours | IC + DPO |
| SEV-4 (Low) | Under 100 data subjects; low-sensitivity data; contained with no exfiltration | Within 4 hours | SOC Lead + Privacy Coordinator |

### Escalation Flow

```
SOC Analyst detects alert
    ↓
SOC Lead validates (within 15 min)
    ↓
Personal data involved? → No → Standard security incident process
    ↓ Yes
Classify severity (SEV-1 to SEV-4)
    ↓
SEV-1/2: Activate Incident Commander + DPO immediately
SEV-3: Notify IC + DPO within 2 hours
SEV-4: Notify Privacy Coordinator within 4 hours
    ↓
IC convenes Core Response Team
    ↓
72-hour Art. 33 clock determination
    ↓
Investigation → Risk Assessment → Notification Decision
```

## Communication Templates

### Template 1: Internal Breach Alert (Email to Core Response Team)

**Subject: [SEV-X] PERSONAL DATA BREACH — Immediate Action Required**

**From**: SOC / Incident Commander
**To**: Core Response Team distribution list

A personal data breach has been identified requiring immediate response.

**Incident Summary:**
- Discovery time: [UTC timestamp]
- Affected system(s): [system names]
- Breach type: [Confidentiality / Integrity / Availability]
- Estimated data subjects: [count or range]
- Personal data categories: [list]
- Containment status: [Contained / Active / Unknown]

**Immediate Actions Required:**
- IC: Convene response team call at [time] on [bridge/Teams link]
- DPO: Begin risk assessment; determine 72-hour deadline
- IT Forensics: Preserve evidence on affected systems
- Legal: Review for privilege and law enforcement considerations
- Communications: Prepare holding statement; monitor media

**Response Team Bridge**: [Teams meeting link]
**Incident Channel**: Signal group "SPG-IR-Active"

### Template 2: Media Holding Statement

Stellar Payments Group is aware of a security incident affecting [some of our systems / our customer database]. We immediately activated our incident response procedures and are working with leading cybersecurity experts to investigate the matter. The protection of our customers' data is our highest priority. We will provide further information as our investigation progresses. For media inquiries, please contact press@stellarpayments.eu.

### Template 3: Customer Service Talking Points

**For customer-facing staff during an active breach:**

If a customer asks about a security incident:
- "We are aware of a security issue and our team is actively working to resolve it."
- "The security of your information is our top priority."
- "We will communicate directly with any affected customers as soon as our investigation allows."
- "I can take your contact details and ensure you are notified if your account is affected."

Do NOT:
- Confirm or deny specific details of the breach
- Speculate on the number of affected customers
- Provide information not in the approved talking points
- Discuss the incident on social media

### Template 4: Board Notification (Email to Board Chair)

**Subject: Data Breach Notification to the Board — [Breach Reference]**

Dear [Board Chair],

I am writing to inform you of a personal data breach that occurred on [date]. This notification is provided in accordance with our Board-approved Incident Escalation Policy.

**Summary**: [2-3 sentence description]
**Scale**: [approximate data subjects and data categories]
**Status**: [contained/under investigation]
**Regulatory notification**: [filed/pending/not required]
**Financial exposure**: [estimated response costs and potential regulatory penalties]

A full briefing will be provided at [scheduled time]. In the interim, [CEO name] is overseeing the organizational response.

### Template 5: Employee Communication (All-Staff)

**Subject: Important Update from [CEO] Regarding a Security Incident**

Dear Colleagues,

I want to share an important update. On [date], we identified a security incident affecting [description]. Our security and privacy teams are working around the clock to investigate and resolve the situation.

**What we know**: [brief, factual description]
**What we are doing**: [containment and investigation actions]
**What this means for you**: [if employee data was involved, say so directly; if not, clarify]
**What we ask of you**: Report any unusual system activity to security@stellarpayments.eu. Do not discuss this matter externally or on social media.

We will provide updates as we learn more. Thank you for your professionalism and support during this time.

[CEO Name]

## Regulatory Authority Contact Directory

### European Union

| Country | Authority | Breach Portal / Contact | Phone |
|---------|-----------|------------------------|-------|
| Germany (Berlin) | Berliner BfDI | datenschutz-berlin.de | +49 30 13889 0 |
| Germany (Federal) | BfDI | bfdi.bund.de | +49 228 997799 0 |
| France | CNIL | notifications.cnil.fr/notifications | +33 1 53 73 22 22 |
| Ireland | DPC | forms.dataprotection.ie | +353 57 868 4800 |
| Netherlands | AP | autoriteitpersoonsgegevens.nl | +31 70 888 8500 |
| Spain | AEPD | sedeagpd.gob.es | +34 91 266 35 17 |
| Italy | Garante | protocollo@pec.gpdp.it | +39 06 696 77 1 |
| Belgium | APD/GBA | gegevensbeschermingsautoriteit.be | +32 2 274 48 00 |
| Austria | DSB | dsb.gv.at | +43 1 52 152 0 |
| Poland | UODO | uodo.gov.pl | +48 22 531 03 00 |

### United Kingdom

| Authority | Portal | Phone |
|-----------|--------|-------|
| ICO | ico.org.uk/for-organisations/report-a-breach | +44 303 123 1113 |

### United States

| Authority | Portal | Phone |
|-----------|--------|-------|
| HHS/OCR (HIPAA) | ocrportal.hhs.gov | +1 800 368 1019 |
| California AG | oag.ca.gov/privacy/databreach/reporting | +1 916 210 6276 |
| New York AG | ag.ny.gov/internet/filing-a-complaint | +1 800 771 7755 |
| FTC | ftc.gov/enforcement | +1 877 382 4357 |

### Other International

| Jurisdiction | Authority | Contact |
|-------------|-----------|---------|
| Canada | OPC | priv.gc.ca | +1 819 994 5444 |
| Australia | OAIC | oaic.gov.au/privacy/notifiable-data-breaches | +1300 363 992 |
| Brazil | ANPD | gov.br/anpd | +55 61 2025 8900 |
| Singapore | PDPC | pdpc.gov.sg | +65 6377 3131 |

## Pre-Negotiated Vendor Contacts

| Service | Vendor | Contract Reference | Activation Contact | SLA |
|---------|--------|-------------------|-------------------|-----|
| Incident Response | Mandiant | SPG-IR-2025-007 | +1 703 935 1700 / ir@mandiant.com | On-site within 24 hours, remote within 4 hours |
| External Legal (EU) | Freshfields Bruckhaus Deringer | SPG-LEG-2025-012 | +49 30 20 28 39 000 | Partner-level response within 2 hours |
| External Legal (US) | Covington & Burling | SPG-LEG-2025-013 | +1 202 662 6000 | Partner-level response within 2 hours |
| Credit Monitoring | Experian IdentityWorks | SPG-EXP-2025-003 | +44 115 941 0888 | Portal activation within 48 hours |
| Crisis Communications | Brunswick Group | SPG-COM-2025-001 | +49 69 2400 5510 | Team mobilized within 4 hours |
| Cyber Insurance | Allianz Cyber Enterprise | SPG-CYB-2025-001 | +49 89 3800 0 | Claims acknowledgment within 24 hours |
| eDiscovery / Legal Hold | Relativity / Exterro | SPG-LIT-2025-004 | +1 312 263 1333 | Legal hold activation within 4 hours |

## Playbook Maintenance

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Review and update contact information | Quarterly | DPO Office |
| Verify vendor retainer agreements are current | Annually | Procurement + DPO |
| Update regulatory authority contact details | Semi-annually | DPO Office |
| Tabletop exercise using playbook | Semi-annually | DPO + CISO |
| Full playbook revision | Annually or after any SEV-1/SEV-2 incident | DPO |
| Distribute updated playbook to Core Response Team | After every revision | DPO Office |
