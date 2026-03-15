---
name: comparing-pia-methodologies
description: >-
  Compares PIA/DPIA methodologies: CNIL PIA tool, ICO DPIA template, NIST
  Privacy Framework, and ISO 29134. Provides methodology selection criteria
  based on regulatory jurisdiction, organisation maturity, processing
  complexity, and resource availability. Covers regulatory acceptance,
  tool features, and cross-methodology mapping. Keywords: PIA methodology,
  CNIL, ICO, NIST Privacy Framework, ISO 29134, DPIA comparison, assessment.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-impact-assessment
  tags: "pia-methodology, cnil, ico, nist-privacy-framework, iso-29134, dpia-comparison"
---

# Comparing PIA Methodologies

## Overview

Multiple established methodologies exist for conducting Privacy Impact Assessments: the CNIL PIA tool, ICO DPIA template, NIST Privacy Framework, and ISO/IEC 29134:2017. Each methodology reflects its originating regulatory context, organisational assumptions, and privacy philosophy. Selecting the appropriate methodology — or combining elements from several — is critical for producing assessments that satisfy regulatory expectations, align with organisational maturity, and address the actual risks of the processing activity. This skill provides a structured comparison framework for methodology selection.

## Methodology Profiles

### 1. CNIL PIA Tool (France)

**Origin**: Commission Nationale de l'Informatique et des Libertes (CNIL), first published 2015, updated 2018 for GDPR alignment.

**Structure**:
- Step 1: Context — Describe the processing, its purposes, the data processed, and the actors involved.
- Step 2: Fundamental Principles — Assess compliance with necessity, proportionality, data subject rights, and obligations (Art. 5, 6, 9, 12-22, 28, 44).
- Step 3: Risks — Identify feared events (illegitimate access, unwanted modification, disappearance of data), assess severity and likelihood.
- Step 4: Validation — Map risks against controls. Decide whether to accept residual risk, implement additional measures, or consult the supervisory authority.

**Key Features**:
- Three feared events model (access, modification, disappearance) structured around CIA triad adapted for privacy.
- Severity scale: Negligible, Limited, Significant, Maximum.
- Likelihood scale: Negligible, Limited, Significant, Maximum.
- Risk matrix: 4x4 grid mapping severity against likelihood.
- Explicit link to Art. 35 and Art. 36 prior consultation threshold.
- Open-source PIA software tool available for download.

**Regulatory Acceptance**:
- Required format for French supervisory authority submissions.
- Accepted by Belgian DPA (APD/GBA) as compliant methodology.
- Referenced by EDPB as an example of good practice in WP248rev.01.
- Widely used across francophone jurisdictions (Belgium, Luxembourg, Switzerland).

### 2. ICO DPIA Template (United Kingdom)

**Origin**: Information Commissioner's Office (ICO), UK. Published as part of ICO GDPR guidance, updated for UK GDPR post-Brexit.

**Structure**:
- Step 1: Identify the need for a DPIA — Screening checklist against Art. 35(3) triggers and ICO's published list of processing requiring DPIA.
- Step 2: Describe the processing — Nature, scope, context, purposes. Data flows including recipients and transfers.
- Step 3: Consultation process — Record of consultation with data subjects, DPO, and other stakeholders.
- Step 4: Assess necessity and proportionality — Lawful basis, purpose limitation, data minimisation, accuracy, storage limitation, security, international transfers.
- Step 5: Identify and assess risks — Risks to individuals organised by source, nature of harm, severity, likelihood.
- Step 6: Identify measures to mitigate risks — For each risk, identify measures that reduce it to an acceptable level.
- Step 7: Sign off and record outcomes — DPO advice, controller decision, integration with processing register.

**Key Features**:
- Seven-step linear process designed for practical completion.
- Emphasis on consultation with data subjects (Step 3) — a distinctive feature not prominent in other methodologies.
- Risk assessment focused on harm to individuals rather than CIA triad.
- Explicit requirement to record DPO advice and whether it was followed.
- Template available as downloadable Word document.
- Screening checklist integrated into Step 1.

**Regulatory Acceptance**:
- Required format for UK ICO submissions and prior consultation.
- Accepted by Irish DPC as compliant methodology for UK-Ireland processing.
- Used as basis for several Member State DPA templates (Denmark, Netherlands).
- Recommended by UK government for public sector processing.

### 3. NIST Privacy Framework (United States)

**Origin**: National Institute of Standards and Technology (NIST), Version 1.0 published January 2020. Voluntary framework.

**Structure**:
- Core: Five functions — IDENTIFY, GOVERN, CONTROL, COMMUNICATE, PROTECT.
- Profiles: Current state and target state assessment for each subcategory.
- Implementation Tiers: Tier 1 (Partial) to Tier 4 (Adaptive) maturity levels.

**Key Features**:
- Not a PIA methodology per se, but provides the organisational context within which PIAs are conducted.
- IDENTIFY function (ID.RA) maps directly to risk assessment activities in PIA.
- Complementary to NIST Cybersecurity Framework (CSF) — designed for joint deployment.
- Sector-agnostic: applicable across all industries, not limited to specific regulatory context.
- Privacy Engineering objectives: Predictability, Manageability, Disassociability.
- No prescribed risk scale or matrix — organisations define their own.

**Regulatory Acceptance**:
- Not a regulatory requirement but widely referenced by US federal agencies (FTC, HHS, DOE).
- Accepted as evidence of privacy program maturity by US state regulators (CCPA/CPRA, VCDPA, CPA).
- Referenced by APEC CBPR system for cross-border data flows.
- Increasingly referenced by EU organisations as complementary to GDPR DPIA.

### 4. ISO/IEC 29134:2017 — Privacy Impact Assessment Guidelines

**Origin**: International Organization for Standardization, published 2017. International standard.

**Structure**:
- Clause 6: PIA preparation — Determine necessity, establish PIA team, develop PIA plan, stakeholder engagement.
- Clause 7: PIA execution — Information gathering, data flow analysis, privacy risk analysis (identification, estimation, evaluation), privacy risk treatment.
- Clause 8: PIA follow-up — PIA report, publication of summary, implementation of treatment plan, audit/review.

**Key Features**:
- Most comprehensive and structured methodology — designed as auditable standard.
- Risk assessment based on ISO 31000 risk management framework.
- Privacy risk = likelihood x consequence (consequence to the data subject, not the organisation).
- Requires formal PIA plan before assessment begins.
- Mandates stakeholder engagement including data subjects.
- PIA report has prescribed structure (Clause 8.2) with 13 required sections.
- Integrates with ISO/IEC 27701 (privacy information management) and ISO/IEC 27001 (information security).

**Regulatory Acceptance**:
- Accepted by supervisory authorities globally as evidence of systematic approach.
- Referenced by EDPB in WP248rev.01 as an example of PIA methodology.
- Required or recommended by several Asian-Pacific DPAs (Singapore PDPC, South Korea PIPC, Japan PPC).
- Certification bodies use ISO 29134 as assessment framework for Art. 42 GDPR certification schemes.

## Methodology Comparison Matrix

| Dimension | CNIL PIA | ICO DPIA | NIST PF | ISO 29134 |
|-----------|----------|----------|---------|-----------|
| Regulatory origin | French DPA (CNIL) | UK DPA (ICO) | US NIST | International (ISO/IEC) |
| Legal framework | GDPR | UK GDPR | Sector-agnostic | International |
| Risk model | 3 feared events (CIA-adapted) | Harm to individuals | Organisation-defined | ISO 31000-based |
| Risk scale | 4x4 (Negligible to Maximum) | Qualitative (Low/Medium/High) | Organisation-defined tiers | Likelihood x Consequence |
| Steps/phases | 4 steps | 7 steps | 5 functions | 3 clauses (prep/execute/follow-up) |
| Data subject consultation | Recommended | Explicitly required (Step 3) | COMMUNICATE function | Required (Clause 6.4) |
| DPO involvement | Required | Required with advice recording | N/A (no DPO concept) | Recommended |
| Tool availability | Open-source software | Word template | Excel self-assessment | No official tool |
| Cost | Free | Free | Free | Standard purchase required (~CHF 166) |
| Certification alignment | None | None | NIST CSF alignment | ISO 27701, ISO 27001 |
| Typical completion time | 2-4 weeks | 1-3 weeks | Ongoing (framework) | 4-8 weeks |
| Best suited for | EU/GDPR processing, French-regulated entities | UK processing, practical quick-start | US organisations, framework-based programs | Multinational, auditable, certification-seeking |

## Methodology Selection Criteria

### Decision Factors

| Factor | Weight | Considerations |
|--------|--------|----------------|
| Regulatory jurisdiction | High | Which supervisory authority will review the assessment? Use their preferred methodology. |
| Organisational maturity | Medium | Low maturity → ICO (simplest). Medium → CNIL. High → ISO 29134. |
| Processing complexity | Medium | Simple processing → ICO. Complex/high-risk → CNIL or ISO 29134. |
| International scope | High | Single jurisdiction → local DPA methodology. Multi-jurisdiction → ISO 29134. |
| Certification goals | Medium | Seeking ISO 27701 or Art. 42 certification → ISO 29134. |
| Resource availability | Medium | Limited resources → ICO. Dedicated privacy team → ISO 29134. |
| Existing framework | Low | Already using NIST CSF → add NIST PF. Already ISO 27001 → ISO 29134. |

### Selection Decision Tree

1. Is the processing subject to a specific supervisory authority that mandates or recommends a methodology?
   - Yes → Use that authority's methodology (CNIL for France, ICO for UK).
   - No → Continue to step 2.
2. Does the organisation operate across multiple jurisdictions?
   - Yes → ISO 29134 (internationally recognised).
   - No → Continue to step 3.
3. What is the organisation's privacy maturity level?
   - Low (no formal privacy program) → ICO DPIA template (quickest to adopt).
   - Medium (privacy program exists) → CNIL PIA tool (structured but accessible).
   - High (mature privacy program, certification goals) → ISO 29134.
4. Is the organisation US-based with an existing NIST CSF deployment?
   - Yes → NIST PF as organisational framework, supplemented by CNIL or ICO for individual DPIAs.
   - No → Use selection from steps 1-3.

## Cross-Methodology Mapping

| CNIL Step | ICO Step | NIST PF Function | ISO 29134 Clause |
|-----------|----------|-------------------|-------------------|
| Step 1: Context | Step 2: Describe processing | ID.IM (Inventory & Mapping) | Clause 6: Preparation |
| — | Step 1: Identify need | — | Clause 6.1: Determine necessity |
| — | Step 3: Consultation | CT.PO (Communication Policies) | Clause 6.4: Stakeholder engagement |
| Step 2: Fundamental Principles | Step 4: Necessity & proportionality | GV.PO (Governance Policies) | Clause 7.3: Privacy safeguard analysis |
| Step 3: Risks | Step 5: Identify & assess risks | ID.RA (Risk Assessment) | Clause 7.4: Risk analysis |
| Step 4: Validation | Step 6: Mitigation measures | CT.DM (Data Processing Management) | Clause 7.5: Risk treatment |
| — | Step 7: Sign off & record | GV.AT (Awareness & Training) | Clause 8: Follow-up |

## Enforcement and Regulatory Guidance

- **EDPB WP248rev.01**: References both CNIL and ISO 29134 as acceptable DPIA methodologies. Does not mandate any specific methodology but requires that the chosen approach satisfies Art. 35(7)(a)-(d) minimum content.
- **Art. 35(7) Minimum Content**: Any methodology must include: (a) systematic description of processing and purposes; (b) necessity and proportionality assessment; (c) risk assessment; (d) measures to address risks. All four methodologies satisfy these requirements.
- **CJEU C-175/20 (SS SIA 'Valsts ieņēmumu dienests')**: Court confirmed that DPIA must assess risks from the perspective of data subjects, not the controller — aligns with ICO and ISO 29134 harm-based approaches.
- **CNIL Deliberation 2018-327**: Published criteria for acceptable DPIA methodologies — 10 criteria that any methodology must satisfy, regardless of which tool is used.
