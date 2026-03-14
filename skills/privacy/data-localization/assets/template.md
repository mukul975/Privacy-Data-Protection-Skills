# Data Localization — Compliance Assessment Template

## Organisation

| Field | Value |
|-------|-------|
| Organisation | Athena Global Logistics GmbH |
| Assessment Date | March 2025 |
| Assessed By | Elisa Brandt, Head of Data Protection |

## Jurisdiction Compliance Matrix

| Country | Law | Requirement | Local Storage | Transfer Mechanism | Filing | Status |
|---------|-----|-------------|--------------|-------------------|--------|--------|
| Russia | 242-FZ / 152-FZ | Primary storage in Russia | Moscow DC (OVHcloud) | Replication to Frankfurt; adequate country under Roskomnadzor list | Roskomnadzor notification filed | Compliant |
| China | PIPL Art. 40 | Domestic storage + CAC transfer mechanism | Alibaba Cloud Shanghai | CAC Standard Contract filed | Filed with Shanghai CAC 15 Feb 2025 | Compliant |
| India | DPDP Act S.16 | No current localization | AWS Mumbai | No blacklist issued; transfer permitted | No filing required | Compliant |
| India (Payments) | RBI Circular | Strict localization | Local payment gateway (India) | No cross-border transfer of payment data | RBI compliance audit passed | Compliant |
| Turkey | KVKK Art. 9 | Board approval for non-adequate transfer | No local DC | Board application pending | Application submitted March 2025 | In Progress |
| Vietnam | Decree 13/2023 | Impact assessment for transfers | No local DC (not required) | Transfer assessment dossier prepared | Filed with MPS January 2025 | Compliant |

## Architecture Decisions

| Jurisdiction | Architecture Pattern | Infrastructure | Notes |
|-------------|---------------------|---------------|-------|
| Russia | Pattern 1: Primary local + replication | OVHcloud Moscow (primary); Frankfurt (replica) | 242-FZ requires primary in Russia; encrypted replication permitted |
| China | Pattern 1: Primary local + controlled transfer | Alibaba Cloud Shanghai (primary); Frankfurt (analytics) | CAC Standard Contract governs Frankfurt transfer |
| India | Pattern 3: Hybrid cloud with residency | AWS Mumbai (PD storage); Frankfurt (app logic) | Data residency policy in AWS; PD does not leave ap-south-1 |
| Turkey | Pattern 2: Local processing (planned) | Cloud DC in Istanbul (planned Q3 2025) | Will reduce dependency on Board approval for transfers |

## Gap Register

| Gap ID | Country | Description | Remediation | Owner | Target |
|--------|---------|-------------|-------------|-------|--------|
| LOC-001 | Turkey | KVKK Board approval pending for transfers to Germany | Await Board decision; prepare local DC as alternative | Legal Counsel | Q3 2025 |
| LOC-002 | Indonesia | GR 71 supervisory access provisions not formally documented | Prepare access provision agreement with Ministry | Privacy Counsel | Q2 2025 |

## Monitoring Calendar

| Country | Monitoring Action | Frequency | Next Due |
|---------|------------------|-----------|----------|
| Russia | Verify Moscow DC operational; check Roskomnadzor updates | Quarterly | June 2025 |
| China | CAC Standard Contract reassessment (2-year cycle) | Biennial | February 2027 |
| India | Monitor DPDP Act blacklist notifications | Monthly | April 2025 |
| India (RBI) | RBI payment data compliance audit | Annual | October 2025 |
| Turkey | KVKK Board decision follow-up | Monthly | April 2025 |
| Vietnam | Decree 13 impact assessment review | Annual | January 2026 |
| Indonesia | GR 71 compliance review | Annual | October 2025 |
