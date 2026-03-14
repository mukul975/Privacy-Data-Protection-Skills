# Standards and Regulatory References

## Primary Legislation and Case Law

### Schrems II — CJEU Case C-311/18 (16 July 2020)
- **Core holding**: SCCs and other Art. 46 transfer mechanisms require a case-by-case assessment of whether the legal framework of the destination country ensures essentially equivalent protection.
- **Paragraph 134**: The controller or processor must verify, on a case-by-case basis, whether the law of the third country ensures adequate protection by reference to EU law standards.
- **Paragraph 135**: Where the assessment reveals that the destination country does not provide an essentially equivalent level of protection, supplementary measures must be adopted to bring the level of protection up to the EU standard.
- **Paragraph 142**: If supplementary measures are insufficient, the transfer must be suspended or terminated.
- **Practical impact**: Created the obligation to conduct what is now known as a Transfer Impact Assessment (TIA).

### GDPR Article 46 — Transfers Subject to Appropriate Safeguards
- **Art. 46(1)**: In the absence of an adequacy decision, a transfer may take place only if appropriate safeguards are provided and enforceable data subject rights and effective legal remedies are available.
- **Art. 46(2)(c)**: SCCs adopted by the Commission constitute appropriate safeguards — but per Schrems II, their effectiveness must be verified case-by-case.

### GDPR Article 44 — General Principle for Transfers
- **Art. 44**: Any transfer shall take place only if the conditions in Chapter V are complied with by the controller and processor, including for onward transfers.

## EDPB Recommendations

### EDPB Recommendations 01/2020 on Measures That Supplement Transfer Tools (Version 2.0, 18 June 2021)
- **Six-step methodology**: (1) Know your transfers; (2) Identify the transfer tool; (3) Assess effectiveness in light of third country law; (4) Adopt supplementary measures; (5) Procedural steps; (6) Re-evaluate at appropriate intervals.
- **Annex 2**: Non-exhaustive catalogue of supplementary measures (technical, contractual, organisational) with effectiveness assessments.
- **Annex 3**: Possible sources of information for assessing third country legal frameworks.
- **Key principle**: Supplementary measures must be effective in practice — formal or theoretical compliance is insufficient.

### EDPB Recommendations 02/2020 on the European Essential Guarantees for Surveillance Measures (10 November 2020)
- **Four guarantees**: (1) Clear, precise, accessible rules; (2) Necessity and proportionality; (3) Independent oversight; (4) Effective remedies.
- **Assessment methodology**: Each surveillance law in the destination country must be assessed against all four guarantees.
- **EEG standard**: Derived from the EU Charter of Fundamental Rights (Articles 7, 8, 47, 52), ECHR (Articles 8, 13), and CJEU case law (Digital Rights Ireland, Tele2/Watson, La Quadrature du Net).

### EDPB Guidelines 05/2021 on the Interplay Between Art. 3 and Chapter V (18 November 2021)
- Clarifies when Chapter V transfer rules apply.
- Relevant for determining TIA scope: only transfers within the meaning of Chapter V require a TIA.

## National SA Guidance on TIAs

### CNIL (France) — TIA Guidance and Tools
- Published a practical guide for conducting TIAs with specific questionnaire templates.
- Emphasises that TIAs must be documented and available to the CNIL upon request.

### Datatilsynet (Denmark) — Transfer Impact Assessment Guidance (2021)
- Published one of the earliest detailed TIA methodologies.
- Recommended a risk-based approach considering: likelihood of government access, data sensitivity, volume, and importer profile.

### EDPS (European Data Protection Supervisor) — TIA for EU Institutions
- Published guidance specific to EU institutions on conducting TIAs for cloud services procured from US providers.
- Established a model TIA template adopted by several national SAs.

### BfDI (Germany) — Position Paper on International Transfers (2022)
- Confirmed that a TIA must be a substantive, documented assessment — not a checkbox exercise.
- Stated that organisations unable to complete a meaningful TIA should not proceed with the transfer.

## Enforcement Precedents

### Austrian DSB — Decision D550.738 (January 2022)
- Google Analytics transfer to the US found non-compliant despite SCCs.
- The TIA was found to be inadequate: it acknowledged US surveillance risks but concluded without sufficient analysis that supplementary measures were effective.
- Significance: Established that a TIA must substantively assess the specific risk to the specific transfer, not merely acknowledge surveillance laws exist.

### French CNIL — Google Analytics Decision (February 2022)
- Aligned with the Austrian DSB; found the TIA did not adequately demonstrate that supplementary measures effectively addressed Section 702 FISA risks.

### Italian Garante — Google Analytics Decision (June 2022)
- Third coordinated enforcement; emphasised that statistical pseudonymisation by the importer does not constitute an effective supplementary measure if the importer holds the re-identification key.

### EDPS Order to European Parliament (January 2022)
- Ordered the European Parliament to suspend its use of Google Analytics due to inadequate TIA.
- Confirmed that EU institutions are subject to the same TIA obligations.

## ISO/IEC Standards

- **ISO/IEC 27701:2019**: Section 7.5 on data sharing and transfer supports TIA documentation requirements.
- **ISO/IEC 27001:2022**: Provides the security controls framework referenced in TIA supplementary measures assessment.
- **ISO 31000:2018**: Risk management framework applicable to the risk assessment methodology embedded in TIA Step 3.
