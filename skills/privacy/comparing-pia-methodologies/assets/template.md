# PIA Methodology Comparison and Selection Report

## Reference: PIA-METHOD-QLH-2026-001

| Field | Value |
|-------|-------|
| Organisation | QuantumLeap Health Technologies |
| Assessment Purpose | Selection of PIA/DPIA methodology for Phase III clinical trial data processing programme |
| Primary Jurisdiction | Germany (BfDI / Landesdatenschutzbeauftragte) |
| Secondary Jurisdictions | France (CNIL), United Kingdom (ICO), United States (HHS/FTC) |
| Date | 2026-03-14 |
| Prepared By | Dr. Elena Vasquez, DPO, CIPP/E, CIPM |

---

## Organisational Context

| Factor | Assessment |
|--------|------------|
| Privacy programme maturity | Medium — established DPO function, Article 30 register maintained, DPIA process in place but not formally certified |
| Processing complexity | High — Phase III multi-centre clinical trial with genetic data, international transfers, AI-assisted endpoint analysis |
| Resource availability | Moderate — dedicated privacy team of 3 FTE, external counsel available |
| Certification goals | Yes — pursuing ISO 27701 certification for clinical data management systems by Q4 2026 |
| Existing frameworks | ISO 27001 certified (clinical IT infrastructure); NIST CSF v1.1 adopted for US operations |

## Methodology Scoring

| Methodology | Jurisdiction Match | Maturity Alignment | Processing Complexity | Resource Availability | Certification Goals | Weighted Total |
|-------------|-------------------|--------------------|-----------------------|----------------------|--------------------|----|
| CNIL PIA Tool | 0.30 (EU, not France-specific) | 1.00 (Medium fit) | 0.50 (better for medium complexity) | 0.90 (2-4 weeks, moderate resources) | 0.30 (no certification alignment) | 0.600 |
| ICO DPIA Template | 0.30 (EU, not UK-specific) | 0.70 (Low fit vs Medium org) | 0.50 (limited for high complexity) | 1.00 (1-3 weeks, limited resources OK) | 0.30 (no certification alignment) | 0.558 |
| NIST Privacy Framework | 0.30 (US operations only) | 0.70 (Medium-High vs Medium org) | 0.60 (framework-level) | 0.50 (ongoing, moderate resources) | 0.60 (NIST alignment) | 0.524 |
| ISO/IEC 29134 | 1.00 (International — accepted everywhere) | 0.40 (High fit vs Medium org) | 1.00 (designed for complex processing) | 0.40 (4-8 weeks, extensive) | 1.00 (ISO 27701 alignment) | **0.760** |

## Recommendation

**Primary methodology: ISO/IEC 29134:2017** (weighted score: 0.760)

### Rationale

1. **International recognition**: QuantumLeap operates clinical trials across Germany, France, the UK, and the US. ISO 29134 is accepted by all relevant supervisory authorities, avoiding the need for separate methodology justification in each jurisdiction.

2. **Certification alignment**: The organisation's ISO 27701 certification goal requires a PIA methodology that integrates with ISO management system standards. ISO 29134 is explicitly referenced by ISO 27701 Clause 7.2.5 as the recommended PIA approach.

3. **Processing complexity**: Phase III clinical trial processing involving genetic data, AI-assisted analysis, and international transfers requires the most rigorous assessment methodology. ISO 29134's ISO 31000-based risk framework provides the depth needed.

4. **Maturity stretch**: While the organisation's current maturity (Medium) is below the ideal fit for ISO 29134 (High), the certification goal means the organisation is intentionally raising its maturity level. Adopting ISO 29134 now supports that trajectory.

### Supplementary Methodologies

| Methodology | Use Case |
|-------------|----------|
| CNIL PIA Tool | French clinical site DPIAs — use CNIL methodology for site-specific assessments submitted to CNIL |
| ICO DPIA Template | UK clinical site DPIAs — use ICO template for ICO prior consultation submissions |
| NIST Privacy Framework | US operations — maintain NIST PF profile for FTC/HHS regulatory engagement |

## Cross-Methodology Mapping (Applied)

| Activity | ISO 29134 (Primary) | CNIL Supplement | ICO Supplement | NIST PF Supplement |
|----------|---------------------|-----------------|----------------|-------------------|
| Processing description | Clause 6: Preparation | Step 1: Context | Step 2: Describe processing | ID.IM |
| Necessity screening | Clause 6.1 | N/A | Step 1: Identify need | N/A |
| Stakeholder consultation | Clause 6.4 | Recommended | Step 3: Consultation | CT.PO |
| Necessity & proportionality | Clause 7.3 | Step 2: Fundamental Principles | Step 4: Necessity & proportionality | GV.PO |
| Risk analysis | Clause 7.4 | Step 3: Feared events | Step 5: Risk assessment | ID.RA |
| Risk treatment | Clause 7.5 | Step 4: Validation | Step 6: Mitigation | CT.DM |
| Sign-off & follow-up | Clause 8 | DPO sign-off | Step 7: Sign off & record | GV.AT |

## Art. 35(7) Compliance Verification

| Requirement | Reference | Addressed | ISO 29134 Section |
|-------------|-----------|-----------|-------------------|
| Systematic description of processing operations and purposes | Art. 35(7)(a) | Yes | Clause 6 — PIA preparation, information gathering |
| Assessment of necessity and proportionality | Art. 35(7)(b) | Yes | Clause 7.3 — Privacy safeguard analysis |
| Assessment of risks to rights and freedoms | Art. 35(7)(c) | Yes | Clause 7.4 — Risk analysis (identification, estimation, evaluation) |
| Measures to address risks | Art. 35(7)(d) | Yes | Clause 7.5 — Risk treatment |

**Compliance status**: All Art. 35(7) minimum content requirements are addressed by ISO 29134 methodology.

## Implementation Plan

| Phase | Timeline | Activity |
|-------|----------|----------|
| Phase 1 | Weeks 1-2 | Procure ISO 29134 standard; train privacy team on ISO 31000 risk methodology |
| Phase 2 | Weeks 3-4 | Develop ISO 29134-aligned DPIA template customised for clinical trial processing |
| Phase 3 | Weeks 5-6 | Pilot DPIA on QT-CARDIO-301 trial using new methodology |
| Phase 4 | Weeks 7-8 | Review pilot, refine template, develop jurisdiction-specific supplements (CNIL, ICO) |
| Phase 5 | Ongoing | Roll out to all clinical trial DPIAs; integrate with ISO 27701 certification programme |

## Approvals

| Role | Name | Date |
|------|------|------|
| DPO | Dr. Elena Vasquez | 2026-03-14 |
| CISO | Dr. James Okonkwo | 2026-03-15 |
| Head of Clinical Operations | Dr. Lisa Bergmann | 2026-03-15 |
| Head of Regulatory Affairs | Dr. Anika Patel | 2026-03-16 |
