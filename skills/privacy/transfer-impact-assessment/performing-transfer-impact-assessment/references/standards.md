# Standards and Regulatory References for Transfer Impact Assessment

## Primary Case Law

### CJEU Case C-311/18 — Data Protection Commissioner v Facebook Ireland and Maximillian Schrems (Schrems II)
- **Date**: 16 July 2020
- **Holdings**: (1) Invalidated EU-US Privacy Shield Decision 2016/1250; (2) Upheld validity of SCCs Decision 2010/87/EU in principle; (3) Required data exporters to verify on a case-by-case basis whether the law of the destination country ensures adequate protection, supplemented by additional safeguards where necessary; (4) Required supervisory authorities to suspend or prohibit transfers where adequate protection cannot be ensured.
- **Key paragraphs**: Para. 134 (obligation to assess destination country law), Para. 135 (supplementary measures requirement), Para. 142 (supervisory authority intervention obligation).

## EDPB Guidance

### Recommendations 01/2020 on Measures that Supplement Transfer Tools (Version 2.0, Adopted 18 June 2021)
- Established the six-step process for assessing international transfers post-Schrems II.
- **Step 1**: Know your transfers (mapping exercise).
- **Step 2**: Identify the transfer tool relied upon (Chapter V mechanism).
- **Step 3**: Assess whether the third country law impinges on the effectiveness of the transfer tool.
- **Step 4**: Identify and adopt supplementary measures.
- **Step 5**: Take procedural steps to implement supplementary measures.
- **Step 6**: Re-evaluate at appropriate intervals.
- **Annex 2**: Catalogue of essential European guarantees for surveillance measures.
- **Annex 3**: Examples of supplementary measures (technical, contractual, organisational).

### Recommendations 02/2020 on the European Essential Guarantees for Surveillance Measures (Adopted 10 November 2020)
- Established four European Essential Guarantees that third country surveillance legislation must meet:
  1. **Processing based on clear, precise, and accessible rules**: Surveillance powers must be defined by law with sufficient clarity.
  2. **Necessity and proportionality**: Access must be limited to what is strictly necessary; bulk collection must have adequate safeguards.
  3. **Independent oversight**: Surveillance must be subject to oversight by an independent body (judicial or independent administrative).
  4. **Effective remedies**: Data subjects must have access to effective legal remedies before an independent body.

### EDPB Guidelines 05/2021 on the Interplay Between Article 3 and Chapter V (Adopted 14 February 2023)
- Clarified when a transfer occurs under Chapter V (as opposed to direct collection from a data subject by a non-EEA controller under Art. 3(2)).
- Established three cumulative conditions for a transfer: (1) a controller or processor is subject to GDPR; (2) this entity discloses or makes available personal data to another controller or processor; (3) the recipient is in a third country or is an international organisation.

## EU Commission Decisions

### Commission Implementing Decision (EU) 2021/914 — New Standard Contractual Clauses (4 June 2021)
- Replaced the prior SCC sets (2001/497/EC, 2004/915/EC, 2010/87/EU).
- Four modules: Controller-to-Controller (Module 1), Controller-to-Processor (Module 2), Processor-to-Processor (Module 3), Processor-to-Controller (Module 4).
- **Clause 14**: Requires the parties to warrant that they have no reason to believe the laws of the destination country prevent the data importer from fulfilling its obligations under the SCCs, having taken into account: (a) the specific circumstances of the transfer; (b) the laws and practices of the destination country; (c) any contractual, technical, or organisational safeguards.
- **Clause 14(b)**: Requires the parties to document the assessment and make it available to the competent supervisory authority on request.
- **Clause 15.1**: Imposes specific obligations on the data importer regarding government access requests, including notification, challenge, and disclosure limitations.

### Commission Implementing Decision C(2023) 4745 — EU-US Data Privacy Framework Adequacy Decision (10 July 2023)
- Based on US Executive Order 14086 (7 October 2022) and Attorney General regulation establishing the Data Protection Review Court.
- Applies only to US organisations self-certified under the DPF.
- Subject to periodic review; first review completed in October 2024.

## US Surveillance Legislation (Key for US Transfer Assessments)

### FISA Section 702 (50 U.S.C. Section 1881a)
- Authorises the Attorney General and Director of National Intelligence to jointly authorise targeting of non-US persons reasonably believed to be outside the US to acquire foreign intelligence information.
- Section 702 reauthorised in April 2024 with expanded definition of electronic communications service providers.
- Targeting procedures, minimisation procedures, and querying procedures subject to FISA Court review.

### Executive Order 14086 — Enhancing Safeguards for United States Signals Intelligence Activities (7 October 2022)
- Requires signals intelligence collection to be necessary and proportionate to the validated intelligence priority.
- Established Data Protection Review Court (DPRC) as a two-tier review mechanism for EU individuals to challenge US surveillance.
- Designated EU and EEA as qualifying states under the EO.

### CLOUD Act (Clarifying Lawful Overseas Use of Data Act, 2018)
- Authorises US law enforcement to compel disclosure of data held by US-based providers regardless of where the data is physically stored.
- Executive agreements between the US and qualifying foreign governments can enable reciprocal access.

## ISO/IEC Standards

### ISO/IEC 27701:2019 — Privacy Information Management System
- **Section 7.5**: Requires organisations to identify and document international transfers of PII.
- **Section 7.5.1**: Requires identification of countries where PII may be transferred.
- **Section 7.5.2**: Requires documentation of the basis for international transfers.

### ISO/IEC 27018:2019 — Protection of PII in Public Clouds
- **Annex A, A.11.1**: Cloud service providers shall notify customers of countries where PII may be processed.
- **Annex A, A.11.2**: Cloud service providers shall document and make available government access request procedures.

## Enforcement Decisions

- **Austrian DPA (DSB) — D155.027 (22 December 2021)**: Google Analytics found to constitute a transfer to the US; Google's SCCs and supplementary measures (encryption in transit, internal access controls) deemed insufficient because Google as a provider under FISA 702 could be compelled to provide data in clear text.
- **CNIL — Decision of 10 February 2022 (Google Analytics)**: Confirmed Austrian DPA analysis; ordered website operator to bring Google Analytics into compliance or cease use within one month.
- **Italian Garante — Decision of 9 June 2022 (Google Analytics)**: Aligned with Austrian and French decisions; found Google Analytics transfers to US unlawful.
- **DPC Ireland — Meta Platforms IN-21-3-3 (May 2023)**: EUR 1.2 billion fine for continued transfers of EU user data to the US without a valid Chapter V mechanism after Schrems II, relying on SCCs without adequate supplementary measures.
- **EDPS — Decision 2022-0019 (January 2022)**: European Parliament's COVID-19 testing programme involved transfers to US by processor Ecolog; EDPS found inadequate assessment of US surveillance laws and insufficient supplementary measures.
