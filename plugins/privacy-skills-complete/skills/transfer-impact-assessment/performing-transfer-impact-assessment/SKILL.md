---
name: performing-transfer-impact-assessment
description: >-
  Guides the post-Schrems II Transfer Impact Assessment process following EDPB
  Recommendations 01/2020 six-step methodology. Covers assessment of third
  country legal frameworks, supplementary measures evaluation, and TIA scoring.
  Activate for international data transfers, SCCs, third-country adequacy,
  or Chapter V compliance. Keywords: TIA, Schrems II, transfer assessment,
  EDPB, supplementary measures, SCCs, international transfer.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-impact-assessment
  tags: "tia, schrems-ii, international-transfer, edpb, supplementary-measures, sccs"
---

# Performing Transfer Impact Assessment

## Overview

Following the Court of Justice of the European Union (CJEU) judgment in Data Protection Commissioner v Facebook Ireland and Maximillian Schrems (Case C-311/18, 16 July 2020) — commonly known as Schrems II — controllers and processors transferring personal data outside the EEA must assess whether the legal framework of the destination country provides an essentially equivalent level of protection to that guaranteed by the GDPR and the EU Charter of Fundamental Rights. This assessment is known as a Transfer Impact Assessment (TIA). The European Data Protection Board adopted Recommendations 01/2020 on 18 June 2021, establishing a six-step process for conducting TIAs.

## Legal Foundation

### CJEU C-311/18 Key Holdings

1. **Privacy Shield invalidated**: The EU-US Privacy Shield framework was declared invalid due to US surveillance programmes (Section 702 FISA, EO 12333) enabling mass access to personal data transferred from the EU, with insufficient remedies for EU data subjects.
2. **Standard Contractual Clauses remain valid in principle**: The SCCs decision (2010/87/EU, now replaced by Commission Implementing Decision 2021/914) was upheld but subject to the requirement that data exporters verify the clauses can be complied with in practice in the destination country.
3. **Case-by-case assessment required**: Controllers cannot rely on SCCs mechanically; they must assess the destination country's legal framework and, where necessary, implement supplementary measures to ensure essentially equivalent protection.
4. **Supervisory authority intervention**: Supervisory authorities are required to suspend or prohibit transfers where essentially equivalent protection cannot be ensured.

### EDPB Recommendations 01/2020 — Six-Step Process

The EDPB established a structured methodology for evaluating whether transfers can proceed:

## Step 1: Know Your Transfers

Map all transfers of personal data to third countries or international organisations:

| Transfer Attribute | Documentation Required |
|-------------------|----------------------|
| Data exporter | Legal entity, establishment, contact details |
| Data importer | Legal entity, country of establishment, sector |
| Personal data categories | Specific categories transferred (identifiers, financial, health, behavioural) |
| Special categories | Whether Art. 9 or Art. 10 data is transferred |
| Data subjects | Categories and approximate number |
| Transfer mechanism | SCCs, BCRs, Art. 49 derogation, adequacy decision |
| Purpose of transfer | Specific purposes for which data is transferred |
| Onward transfers | Whether importer transfers data to further third countries |
| Format | Whether data is transferred in clear text, pseudonymised, or encrypted |
| Storage vs transit | Whether data is stored in third country or only transits through it |

## Step 2: Identify the Transfer Tool — Chapter V GDPR

| Transfer Mechanism | GDPR Reference | Assessment Requirement |
|-------------------|----------------|----------------------|
| Adequacy decision | Art. 45 | Rely on Commission assessment; monitor for future invalidation |
| Standard Contractual Clauses (new 2021 SCCs) | Art. 46(2)(c) | Full TIA required per CJEU C-311/18 |
| Binding Corporate Rules | Art. 47 | Full TIA required; BCRs must include supplementary measures |
| Codes of conduct with binding commitments | Art. 46(2)(e) | Full TIA required |
| Certification mechanisms | Art. 46(2)(f) | Full TIA required |
| Ad hoc contractual clauses | Art. 46(3)(a) | Full TIA required plus supervisory authority authorisation |
| Art. 49 derogations | Art. 49 | No TIA required but strict conditions apply; derogations must be interpreted restrictively |

## Step 3: Assess Third Country Legal Framework

Evaluate whether the destination country's laws and practices provide essentially equivalent protection. Key assessment areas:

### 3.1 Government Access to Data

| Assessment Factor | Questions to Address |
|-------------------|---------------------|
| Surveillance legislation | What laws authorise government access to personal data held by private entities? |
| Scope of access powers | Is access limited to what is strictly necessary and proportionate, or does it enable bulk/indiscriminate collection? |
| Independent oversight | Is government access subject to prior authorisation by an independent body (court or independent administrative authority)? |
| Transparency | Are data subjects notified of government access, either directly or through transparency reporting? |
| Effective remedies | Do data subjects have access to an independent tribunal or court to challenge government access? |

### 3.2 Rule of Law and Legal Framework

| Assessment Factor | Questions to Address |
|-------------------|---------------------|
| Constitutional protections | Does the country's constitution protect the right to privacy and data protection? |
| Data protection legislation | Does the country have comprehensive data protection legislation? |
| Independent supervisory authority | Is there an independent data protection authority with enforcement powers? |
| Judicial independence | Is the judiciary independent from the executive, with power to review government surveillance? |

### 3.3 Practical Application

| Assessment Factor | Sources of Information |
|-------------------|----------------------|
| Government access requests | Transparency reports from the data importer and major technology companies |
| Enforcement actions | Published decisions of the destination country's data protection authority |
| Legal reforms | Pending or recent legislative changes affecting surveillance powers |
| International assessments | EDPB adequacy referentials, CoE Convention 108+ ratification status |

## Step 4: Identify and Adopt Supplementary Measures

Where the assessment in Step 3 reveals that the third country framework does not provide essentially equivalent protection, the exporter must identify supplementary measures that, together with the transfer tool, ensure essentially equivalent protection.

### Technical Supplementary Measures

| Measure | EDPB Assessment | Effective Against |
|---------|-----------------|-------------------|
| End-to-end encryption where exporter holds the key | Effective — prevents importer and government access to clear text data | Government access via importer; importer misuse |
| Pseudonymisation where exporter holds the mapping table | Effective — if additional information needed to re-identify is held solely in EEA | Government access where re-identification requires mapping table |
| Split processing across jurisdictions | Effective — if no single jurisdiction has access to complete dataset | Government access in any single jurisdiction |
| Transport encryption (TLS/IPSEC) for data in transit | Insufficient alone — protects only against interception during transit, not access at rest | Transit interception only |
| Encryption at rest where importer holds decryption key | Insufficient — importer can be compelled to provide decryption key | Not effective against government compulsion |

### Contractual Supplementary Measures

| Measure | Purpose |
|---------|---------|
| Obligation to use all available legal remedies to challenge government access requests | Ensures importer resists unlawful government access |
| Warrant canary or transparency reporting obligations | Enables exporter to detect government access |
| Obligation to notify exporter of government access requests (where legally permitted) | Enables exporter to intervene or suspend transfers |
| Obligation to conduct annual assessment of government access laws | Ensures ongoing monitoring of legal framework changes |
| Contractual right for exporter to audit importer's compliance | Enables verification of supplementary measure effectiveness |

### Organisational Supplementary Measures

| Measure | Purpose |
|---------|---------|
| Adoption of internal policies and procedures for handling government access requests | Ensures structured response to government demands |
| Appointment of a DPO or privacy officer by the importer | Ensures designated responsibility for compliance |
| Staff training on government access response procedures | Ensures operational readiness |
| Regular external audits of government access request handling | Independent verification of compliance |

## Step 5: Procedural Steps for Supplementary Measures

1. Document the supplementary measures in writing, either within the SCCs or in a separate supplementary agreement annexed to the SCCs.
2. Ensure supplementary measures are legally binding on the data importer.
3. Verify that supplementary measures are technically implementable given the processing purposes.
4. Assess whether supplementary measures conflict with any obligation of the data importer under the destination country's law.
5. If supplementary measures conflict with local law obligations of the importer, the transfer cannot proceed.

## Step 6: Re-evaluate at Appropriate Intervals

1. Monitor developments in the third country legal framework on an ongoing basis.
2. Conduct formal TIA re-evaluation at minimum annually or upon a trigger event.
3. Trigger events: new surveillance legislation, court decision affecting data access, adequacy decision adopted or withdrawn, law enforcement action affecting the importer.
4. Suspend transfers immediately if supplementary measures can no longer ensure essentially equivalent protection.

## TIA Scoring Rubric

### Government Access Risk Score

| Factor | Weight | Score 1 (Low Risk) | Score 3 (Medium Risk) | Score 5 (High Risk) |
|--------|--------|--------------------|-----------------------|---------------------|
| Surveillance legislation scope | 25% | Targeted access only, strictly necessary and proportionate | Mix of targeted and bulk powers, some proportionality limitations | Bulk/indiscriminate access powers without proportionality requirements |
| Independent prior authorisation | 20% | Judicial authorisation required for all access | Judicial authorisation for some; administrative for others | No independent authorisation required; self-authorisation |
| Effective remedies | 20% | Independent court with full review powers, accessible to foreign nationals | Administrative review body with limited powers | No effective remedy available to foreign nationals |
| Transparency and notification | 15% | Mandatory notification and public transparency reporting | Partial transparency; notification in some cases | No notification obligation; limited or no transparency |
| Rule of law and judicial independence | 20% | Strong constitutional protections; independent judiciary; ratified CoE 108+ | Some constitutional protections; judiciary generally independent | Weak or absent constitutional protections; executive influence over judiciary |

### Overall TIA Risk Level

| Total Weighted Score | Risk Level | Recommendation |
|---------------------|-----------|----------------|
| 1.0 — 2.0 | Low | Transfer may proceed with standard transfer tool |
| 2.1 — 3.0 | Medium | Transfer may proceed with appropriate supplementary measures |
| 3.1 — 4.0 | High | Transfer may proceed only with robust technical supplementary measures (encryption with exporter-held key, pseudonymisation) |
| 4.1 — 5.0 | Very High | Transfer should not proceed unless data is encrypted with exporter-held key and importer has no access to clear text data |

## Country-Specific Assessment Notes

### United States

- **Post-Schrems II status**: EU-US Data Privacy Framework adopted 10 July 2023 (Commission Implementing Decision C(2023) 4745). US companies self-certified under the DPF benefit from an adequacy decision. Non-certified companies require SCCs with TIA.
- **Key legislation**: FISA Section 702 (amended by FISA Section 702 reauthorisation in April 2024), EO 14086 (7 October 2022) establishing proportionality requirements and Data Protection Review Court.
- **Assessment**: For DPF-certified companies, adequacy finding applies. For non-certified companies, TIA must assess whether EO 14086 safeguards are sufficient given the specific data and importer.

### United Kingdom

- **Post-Brexit status**: Adequacy decision adopted 28 June 2021 (Commission Implementing Decision C(2021) 4800), valid until 27 June 2025, extended by new adequacy assessment.
- **Key legislation**: Investigatory Powers Act 2016, Data Protection Act 2018, UK GDPR.
- **Assessment**: Adequacy decision currently in force. Monitor for changes to IPA bulk powers and UK divergence from GDPR standards.

### India

- **Status**: No adequacy decision. Digital Personal Data Protection Act 2023 enacted but implementation through rules pending.
- **Key legislation**: Information Technology Act 2000, DPDP Act 2023, Indian Telegraph Act 1885.
- **Assessment**: Government access powers under IT Act Section 69 and Telegraph Act are broad. TIA should assess proportionality and remedy availability. Supplementary measures recommended.

## Common TIA Deficiencies

1. **Generic country assessments**: Using a template country assessment without considering the specific data, importer, and processing context.
2. **Reliance on contractual measures alone**: Contractual obligations cannot override a government compulsion order; technical measures must supplement contractual ones.
3. **Failure to assess onward transfers**: The importer may transfer data to further third countries with different legal frameworks.
4. **No ongoing monitoring**: TIA conducted once and never updated despite legal framework changes.
5. **Conflating adequacy with absence of risk**: Even countries with adequacy decisions may present risks for specific data types or sectors.

## Enforcement Precedents

- **CJEU C-311/18 Schrems II (2020)**: Invalidated Privacy Shield; required case-by-case assessment for SCCs.
- **Austrian DPA (DSB) — Decision D155.027 of 22 December 2021**: Google Analytics transfers to US found unlawful; TIA inadequate because Google's SCCs and supplementary measures did not prevent US government access under FISA 702.
- **CNIL (France) — Decision of 10 February 2022**: Google Analytics transfers to US found unlawful; echoed Austrian DPA reasoning regarding FISA 702 access.
- **DPC Ireland — Meta Platforms Decision (May 2023)**: EUR 1.2 billion fine for continued transfers to US without valid transfer mechanism following Schrems II.
- **EDPS — Decision on European Parliament COVID testing (January 2022)**: Found that transfers to US by Ecolog (processor) lacked adequate supplementary measures.
