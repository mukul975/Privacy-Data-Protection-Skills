# Transfer Records and Documentation — Compliance Template

## Organisation

| Field | Value |
|-------|-------|
| Organisation | Athena Global Logistics GmbH |
| Group DPO | Elisa Brandt |
| Register Owner | Privacy Office, Frankfurt |
| Last Full Review | March 2025 |

## Transfer Register

| Transfer ID | Exporter | Exporter Country | Importer | Importer Country | Mechanism | Mechanism Ref | TIA Ref | Supplementary Measures | Review Date | Status |
|------------|----------|-----------------|----------|-----------------|-----------|--------------|---------|----------------------|------------|--------|
| ATH-INT-001 | Athena GmbH | Germany (EU) | TransPacific Ltd | Hong Kong SAR | SCCs Module 2 | Executed 15 Mar 2024 | TIA-2024-003 | Encryption (TLS 1.3), pseudonymisation, audit rights | 2025-06-30 | Active |
| ATH-INT-002 | Athena GmbH | Germany (EU) | CloudVault Pte Ltd | Singapore | SCCs Module 3 | Executed 1 Feb 2024 | TIA-2024-005 | Encryption at rest (AES-256), access controls, sub-processor restrictions | 2025-06-30 | Active |
| ATH-INT-003 | Athena GmbH | Germany (EU) | Athena Japan KK | Japan | Adequacy (Decision 2019/419) | EC Decision 2019/419 | N/A | N/A (adequate country) | 2025-12-31 | Active |
| ATH-INT-004 | Athena GmbH | Germany (EU) | Athena India Pvt Ltd | India | SCCs Module 1 | Executed 10 Jan 2024 | TIA-2024-008 | Encryption, contractual government access notification, data minimisation | 2025-06-30 | Active |
| ATH-INT-005 | Athena GmbH | Germany (EU) | Pinnacle Data Services | Thailand | SCCs Module 3 | Executed 20 Apr 2024 | TIA-2024-010 | Encryption, pseudonymisation, contractual audit rights | 2025-06-30 | Active |
| ATH-INT-006 | Athena GmbH | Germany (EU) | Athena US Inc | United States | DPF (Decision 2023/1795) | DPF Cert. verified 1 Jan 2025 | N/A | SCCs as fallback; contractual FISA S.702 notification clause | 2025-06-30 | Active |

## Risk Assessment Summary

| Transfer ID | Destination | Special Category | Volume | Adequate Country | Gov. Access Risk | TIA Current | Supp. Measures | Risk Rating |
|------------|-------------|-----------------|--------|-----------------|-----------------|-------------|---------------|-------------|
| ATH-INT-001 | Hong Kong SAR | No | Medium | No | Medium | Yes | Yes | Medium |
| ATH-INT-002 | Singapore | No | High | No | Low | Yes | Yes | Medium |
| ATH-INT-003 | Japan | No | Medium | Yes | Low | N/A | N/A | Low |
| ATH-INT-004 | India | No | High | No | Medium | Yes | Yes | Medium |
| ATH-INT-005 | Thailand | No | Low | No | Low | Yes | Yes | Low |
| ATH-INT-006 | United States | No | High | Yes (DPF) | High | N/A | Yes | Medium |

## Documentation Completeness Tracker

| Transfer ID | Executed Mechanism | TIA | Supplementary Measures Record | Due Diligence | Annex Review Log | Sub-processor List | Package Complete |
|------------|-------------------|-----|------------------------------|--------------|-----------------|-------------------|-----------------|
| ATH-INT-001 | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| ATH-INT-002 | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| ATH-INT-003 | N/A (adequacy) | N/A | N/A | N/A | N/A | N/A | Yes |
| ATH-INT-004 | Yes | Yes | Yes | Yes | No | N/A | No — annex review log pending |
| ATH-INT-005 | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| ATH-INT-006 | N/A (DPF) | N/A | Yes (fallback SCCs) | Yes | N/A | N/A | Yes |

## Annual Review Cycle

| Quarter | Activity | Owner | Status |
|---------|----------|-------|--------|
| Q1 (Jan-Mar) | Full register review: verify all active transfers, close terminated, update mechanism status | Privacy Office | Completed (March 2025) |
| Q2 (Apr-Jun) | TIA refresh: reassess transfers to non-adequate countries against current legal developments | Privacy Counsel | Scheduled |
| Q3 (Jul-Sep) | Mechanism review: verify SCC execution, adequacy status, BCR compliance, derogation necessity | Privacy Office | Scheduled |
| Q4 (Oct-Dec) | Governance review: documentation completeness, audit trail integrity, SA readiness | Group DPO | Scheduled |

## Audit Trail (Recent Entries)

| Audit ID | Transfer ID | Event | Date | Actor | Details |
|----------|------------|-------|------|-------|---------|
| AUD-20250310-001 | ATH-INT-001 | review_conducted | 2025-03-10 | Elisa Brandt | Annual review — compliant, no changes |
| AUD-20250310-002 | ATH-INT-002 | review_conducted | 2025-03-10 | Elisa Brandt | Annual review — compliant, sub-processor list updated |
| AUD-20250310-003 | ATH-INT-003 | review_conducted | 2025-03-10 | Elisa Brandt | Adequacy decision still in force; monitoring ongoing |
| AUD-20250310-004 | ATH-INT-004 | tia_updated | 2025-03-10 | Markus Stein | TIA refreshed after India DPDP Act update |
| AUD-20250228-005 | ATH-INT-006 | document_attached | 2025-02-28 | Anna Richter | DPF certification re-verification report attached |
| AUD-20250115-006 | ATH-INT-005 | supplementary_measure_added | 2025-01-15 | Elisa Brandt | Added contractual audit rights clause to Thailand DPA |

## Supervisory Authority Readiness Checklist

| Item | Status | Notes |
|------|--------|-------|
| Complete transfer register available | Yes | Updated March 2025 |
| All SCC-based transfers have executed SCCs on file | Yes | All modules signed and dated |
| TIAs completed for all non-adequate country transfers | Yes | Refreshed Q1 2025 |
| Supplementary measures documented | Yes | For all SCC and BCR transfers |
| Audit trail operational and verified | Yes | Integrity check passed Q4 2024 |
| Sub-processor chains documented | Yes | Annex III current for Modules 2 and 3 |
| Response SLA defined | Yes | 10 business days from SA request |
| Escalation path documented | Yes | DPO → Head of Legal → CPO → Board Committee |

## Gaps and Remediation Actions

| Gap | Transfer ID | Action | Owner | Target Date |
|-----|------------|--------|-------|-------------|
| Annex review log not completed | ATH-INT-004 | Complete annex review log for India transfer SCCs | Privacy Counsel | 2025-04-30 |
| DPF contingency plan not yet formalised | ATH-INT-006 | Finalise contingency plan for US transfers if DPF is invalidated | Privacy Office | 2025-06-30 |
| Thailand PDPC adequate country list pending | ATH-INT-005 | Monitor PDPC announcements; maintain contractual safeguards | Privacy Counsel | Ongoing |
