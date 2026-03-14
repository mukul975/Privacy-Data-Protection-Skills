---
name: conducting-transfer-impact-assessment
description: >-
  Guides the post-Schrems II Transfer Impact Assessment process following EDPB
  Recommendations 01/2020 six-step methodology. Covers destination country
  surveillance law assessment, European Essential Guarantees evaluation, and
  supplementary measures determination. Keywords: TIA, transfer impact assessment,
  Schrems II, EDPB recommendations, supplementary measures.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: cross-border-transfers
  tags: "tia, transfer-impact-assessment, schrems-ii, edpb-recommendations, surveillance-assessment"
---

# Conducting Transfer Impact Assessment

## Overview

Following the Court of Justice of the European Union's judgment in Schrems II (Case C-311/18, 16 July 2020), organisations relying on Standard Contractual Clauses (SCCs) or other Art. 46 GDPR transfer mechanisms must conduct a Transfer Impact Assessment (TIA) to evaluate whether the legal framework of the destination country provides an essentially equivalent level of protection for personal data. The EDPB adopted Recommendations 01/2020 on measures that supplement transfer tools to ensure compliance with the EU level of protection of personal data (Version 2.0, adopted 18 June 2021), establishing a six-step methodology for this assessment.

## EDPB Six-Step Methodology

### Step 1: Know Your Transfers

Map all personal data transfers to third countries, identifying:

| Element | Required Information |
|---------|---------------------|
| Transfer identification | Unique reference for each transfer or set of transfers |
| Data exporter | Legal entity name, establishment, role (controller/processor) |
| Data importer | Legal entity name, establishment, role (controller/processor) |
| Transfer mechanism | SCCs (specifying module), BCRs, Art. 49 derogation |
| Data categories | Personal data types transferred, including any special categories |
| Data subjects | Categories of individuals whose data is transferred |
| Purpose | Specific purpose(s) for which the data is processed after transfer |
| Destination country | Country where the importer processes the data |
| Onward transfers | Any further transfers from the importer to other jurisdictions |
| Format and channel | How data is transmitted (API, SFTP, email, physical media) |
| Storage duration | How long data is retained in the destination country |

**Athena Global Logistics example transfer mapping**:

| Transfer Ref | Exporter | Importer | Destination | Mechanism | Data Categories |
|-------------|----------|----------|------------|-----------|----------------|
| TIA-2025-HK-001 | Athena Global Logistics GmbH | TransPacific Freight Solutions Ltd | Hong Kong SAR | SCCs Module 2 | Customer names, addresses, customs IDs, consignment data |
| TIA-2025-IN-001 | Athena Global Logistics GmbH | Athena Freight Services India Pvt Ltd | India | SCCs Module 1 | Employee names, contact details, performance records |
| TIA-2025-US-001 | Athena Global Logistics GmbH | Meridian Cloud Services Inc | United States | EU-US DPF + SCCs backup | Customer data, operational analytics |

### Step 2: Identify the Transfer Tool Relied Upon

For each transfer, confirm the Art. 46 transfer mechanism:

1. **SCCs (Art. 46(2)(c))**: Identify the specific module (1-4) and version (2021/914).
2. **BCRs (Art. 47)**: Confirm approval status and scope coverage.
3. **Ad hoc contractual clauses (Art. 46(3)(a))**: Confirm SA authorisation.
4. **Codes of conduct (Art. 46(2)(e))**: Confirm approved code and binding commitments.
5. **Certification mechanisms (Art. 46(2)(f))**: Confirm certification status and scope.

Document the specific clauses that may be affected by the destination country legal framework, particularly:
- Clause 14 (SCCs) — local laws and obligations relating to access by public authorities
- Clause 15 (SCCs) — obligations of the data importer in case of government access

### Step 3: Assess Whether the Transfer Tool Is Effective in Light of All Circumstances

This is the core of the TIA. Assess the legal framework of the destination country against the four European Essential Guarantees (EDPB Recommendations 02/2020):

#### Essential Guarantee 1: Processing Should Be Based on Clear, Precise, and Accessible Rules

| Assessment Question | Analysis |
|-------------------|----------|
| Is government access to personal data based on legislation? | Identify the specific statutes authorising government access (e.g., FISA Section 702, EO 12333 for US; National Security Law for Hong Kong; IT Act Section 69 for India) |
| Are the rules publicly available? | Assess whether the legislation and its implementing regulations are published and accessible |
| Is the scope of government access clearly defined? | Assess whether the legislation specifies the categories of data, persons, or situations subject to access |
| Are there exceptions or conditions for access? | Identify any limitations, thresholds, or prior authorisation requirements |

#### Essential Guarantee 2: Necessity and Proportionality

| Assessment Question | Analysis |
|-------------------|----------|
| Is government access limited to what is strictly necessary? | Assess whether the legislation requires a showing of necessity for each access request |
| Is the scope proportionate to the stated objective? | Evaluate whether bulk/mass surveillance is permitted or whether access must be targeted |
| Are there safeguards against abuse? | Assess minimisation requirements, purpose limitations, and retention limits for accessed data |

#### Essential Guarantee 3: Independent Oversight Mechanism

| Assessment Question | Analysis |
|-------------------|----------|
| Is there prior judicial or independent authorisation? | Determine whether a court or independent body must approve access requests before execution |
| Is there ongoing oversight? | Assess whether an independent body monitors government access activities |
| Are oversight bodies genuinely independent? | Evaluate the appointment, tenure, and dismissal conditions of oversight body members |

#### Essential Guarantee 4: Effective Remedies Available to the Individual

| Assessment Question | Analysis |
|-------------------|----------|
| Can individuals challenge government access in court? | Assess whether there is a right to judicial review of surveillance measures |
| Is there an effective notification mechanism? | Determine whether individuals are notified of surveillance (even if delayed) |
| Can individuals obtain a remedy? | Assess available remedies (compensation, data deletion, injunctive relief) |

### Step 4: Adopt Supplementary Measures

If Step 3 reveals that the transfer tool is not effective on its own, identify and implement supplementary measures to bridge the protection gap:

#### Technical Measures

| Measure | Effectiveness | Applicable Scenarios |
|---------|--------------|---------------------|
| End-to-end encryption (data in transit and at rest) with EU-held keys | High — prevents importer and government access to plaintext | Data storage or transit where importer does not need to process plaintext |
| Pseudonymisation with EU-held mapping table | High — transferred data cannot be attributed to identified individuals | Analytics, research, or aggregation where identification is not needed at the importer |
| Split processing | High — no single entity in the third country holds the complete dataset | Multi-party computation or processing split between jurisdictions |
| Transport-layer encryption (TLS 1.3) | Medium — protects data in transit but not against compelled disclosure at rest | All transfers as a baseline measure; insufficient alone for high-risk jurisdictions |

#### Contractual Measures

| Measure | Effectiveness | Applicable Scenarios |
|---------|--------------|---------------------|
| Obligation to challenge disproportionate government access requests | Medium — depends on legal standing and judicial independence in destination country | All SCC-based transfers (already required under Clause 15) |
| Transparency obligation for government access requests received | Medium — provides visibility but does not prevent access | All transfers |
| Audit rights exercisable by the exporter or independent auditor | Medium — verifies compliance but is retrospective | All transfers |
| Warrant canary (commitment to publish regular transparency reports) | Low-Medium — provides indirect signal but does not prevent access | US transfers where gag orders may apply |

#### Organisational Measures

| Measure | Effectiveness | Applicable Scenarios |
|---------|--------------|---------------------|
| Strict internal access policies limiting who can access transferred data | Medium — reduces the surface of potential government access | All transfers |
| Regular transparency reports on government access requests | Medium — provides accountability | All transfers |
| Data protection impact assessment for government access scenarios | Medium — proactive risk identification | High-risk jurisdiction transfers |
| Adoption of ISO 27001/27701 certification by the importer | Medium — independent verification of security and privacy controls | All transfers |

### Step 5: Procedural Steps If Supplementary Measures Are Adopted

1. Document the supplementary measures in the SCC Annex or in a separate addendum.
2. Implement the technical measures before commencing or continuing the transfer.
3. Execute contractual amendments reflecting the supplementary measures.
4. Verify the importer has the technical capability and legal ability to implement the measures.
5. Notify the competent SA if required (for ad hoc contractual clauses under Art. 46(3)(a)).

### Step 6: Re-Evaluate at Appropriate Intervals

1. Schedule periodic TIA reviews: at minimum annually, or upon any of the following triggers:
   - New legislation enacted in the destination country affecting government access
   - Court rulings in the destination country affecting privacy protections
   - Changes to the EC adequacy decision landscape
   - EDPB or national SA guidance updates
   - Material change in the nature, volume, or sensitivity of transferred data
   - Government access request received by the importer
2. Document each re-evaluation with the date, trigger, findings, and any changes to supplementary measures.
3. If re-evaluation concludes that effective protection cannot be ensured, suspend the transfer and notify the competent SA.

## Country-Specific Assessment Summaries

### United States

| Factor | Assessment |
|--------|-----------|
| Key surveillance laws | FISA Section 702, EO 12333, CLOUD Act, National Security Letters (18 USC 2709) |
| Necessity/proportionality | EO 14086 (October 2022) introduced necessity and proportionality requirements; applies to all signals intelligence activities |
| Independent oversight | FISC (prior authorisation for Section 702); PCLOB (oversight); DPRC (redress for EU data subjects) |
| Remedies | DPRC mechanism established under EO 14086; binding determinations |
| Overall assessment | If importer is DPF-certified: adequacy decision applies. If not DPF-certified: SCCs with supplementary measures (encryption, contractual transparency) |

### People's Republic of China

| Factor | Assessment |
|--------|-----------|
| Key surveillance laws | Cybersecurity Law (Art. 28, 37), National Intelligence Law (Art. 7, 14), Data Security Law (Art. 35-36), PIPL (Art. 38-43) |
| Necessity/proportionality | National Intelligence Law Art. 7 imposes broad cooperation obligations; no explicit proportionality requirement |
| Independent oversight | No independent judicial oversight of intelligence access; procuratorate oversight is not independent from the state |
| Remedies | Limited judicial remedies for foreign data subjects against state surveillance |
| Overall assessment | High risk; supplementary measures must include strong encryption with EU-held keys; consider data minimisation and pseudonymisation before transfer; for some data categories, transfer may not be possible with effective protection |

### India

| Factor | Assessment |
|--------|-----------|
| Key surveillance laws | IT Act 2000 Section 69 (interception), Telegraph Act 1885 Section 5, DPDP Act 2023 Section 36 (government exemptions) |
| Necessity/proportionality | Section 69 requires ministerial authorisation but proportionality review is limited; mass surveillance capability through CMS (Central Monitoring System) |
| Independent oversight | No prior judicial authorisation for interception; review committee is executive-appointed |
| Remedies | Limited remedies under IT Act; High Court writ jurisdiction available but practical access is constrained |
| Overall assessment | Medium-High risk; supplementary measures should include encryption, contractual transparency, and audit rights; TIA should assess specific risk based on data category and importer profile |

### Hong Kong SAR

| Factor | Assessment |
|--------|-----------|
| Key surveillance laws | Interception of Communications and Surveillance Ordinance (Cap. 589), National Security Law (2020), Safeguarding National Security Ordinance (2024) |
| Necessity/proportionality | Cap. 589 requires judicial authorisation for interception; however, NSL provides broad powers with limited proportionality review |
| Independent oversight | Commissioner on Interception of Communications and Surveillance provides oversight under Cap. 589; NSL cases subject to designated judges |
| Remedies | Judicial review available under Cap. 589; limited practical remedies under NSL |
| Overall assessment | Medium risk (elevated since NSL enactment); supplementary measures should include encryption and contractual obligations; assess sensitivity of data and likelihood of government interest |

## TIA Documentation Requirements

Each TIA must be documented and include:

1. **Transfer identification** (Step 1 mapping data)
2. **Transfer mechanism details** (Step 2 analysis)
3. **Destination country legal assessment** with specific legislation citations (Step 3)
4. **European Essential Guarantees analysis** for each identified law (Step 3)
5. **Supplementary measures identified and rationale** (Step 4)
6. **Implementation status of supplementary measures** (Step 5)
7. **Re-evaluation schedule and triggers** (Step 6)
8. **Overall conclusion**: transfer may proceed / transfer may proceed with supplementary measures / transfer must be suspended
9. **Sign-off** by the DPO or Head of Data Protection
10. **Version history** tracking all updates and re-evaluations
