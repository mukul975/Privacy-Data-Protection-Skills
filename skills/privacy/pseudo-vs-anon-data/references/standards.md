# Standards and Regulatory References — Pseudonymised vs Anonymised Data

## Primary Legislation

### GDPR — Regulation (EU) 2016/679

- **Article 4(5)**: Definition of pseudonymisation — processing personal data so it cannot be attributed to a specific data subject without additional information, kept separately with technical and organisational measures.
- **Recital 26**: Principles of data protection should not apply to anonymous information or data rendered anonymous. To determine identifiability, account for all means reasonably likely to be used, considering objective factors: cost of identification, time, available technology, and technological developments.
- **Recital 28**: Application of pseudonymisation can reduce risks for data subjects and help controllers and processors meet their data protection obligations. Explicit mention of pseudonymisation in the GDPR does not exclude other data protection measures.
- **Recital 29**: Incentive for pseudonymisation — taken into account when assessing compliance with Art. 6(1)(f) legitimate interests and Art. 32 security, and as a safeguard under Art. 89(1) for research processing.

## Case Law

### Breyer v Bundesrepublik Deutschland — CJEU Case C-582/14 (2016)

- **Significance for anonymisation assessment**: Established that identifiability is assessed relative to the controller, considering legal means to access third-party data. A dataset may be pseudonymised (identifiable) for one controller but effectively anonymous for another who lacks means to re-identify.
- **Relevance**: Directly applicable when assessing whether a dataset shared with a third party retains personal data status for the recipient.

### EDPS v Single Resolution Board — CJEU Case C-413/23 (Pending)

- **Referred question**: Whether pseudonymised data constitutes personal data for a recipient who does not possess and cannot legally access the re-identification key.
- **AG Opinion (September 2024)**: Advocate General Szpunar suggested a relative approach — if the recipient has no legal means to obtain the key, the data may not be personal data for that recipient.
- **Status**: Judgment pending as of March 2026. Will significantly clarify the pseudonymisation/anonymisation boundary for data sharing scenarios.

## Regulatory Guidance

### Article 29 Working Party — Opinion 05/2014 on Anonymisation Techniques (WP216)

- **Adopted**: 10 April 2014
- **Status**: Endorsed by EDPB under Art. 94(2) GDPR
- **Key Content**:
  - Three-criteria test for anonymisation: singling out, linkability, inference
  - Analysis of anonymisation techniques: randomisation (noise addition, permutation, differential privacy) and generalisation (k-anonymity, l-diversity, t-closeness)
  - Conclusion that pseudonymisation (including hashing and encryption) does NOT constitute anonymisation
  - Assessment that k-anonymity alone is insufficient — must be combined with other techniques
  - Recommendation that anonymisation effectiveness be assessed against all three criteria

### ICO — Anonymisation, Pseudonymisation, and Privacy Enhancing Technologies Guidance (Draft Code of Practice, 2022)

- **Key Content**:
  - Motivated intruder test as practical assessment methodology
  - Spectrum of identifiability: identified → identifiable → effectively anonymous → anonymised
  - Recognition that anonymisation is a process, not a state — requires ongoing reassessment
  - Practical guidance on assessing re-identification risk

### CNIL — Practical Guide on Anonymisation (2019)

- **Key Content**:
  - Adopts WP29 three-criteria framework
  - Provides worked examples of anonymisation assessment for healthcare, transport, and telecoms datasets
  - Emphasises that anonymisation must be irreversible — any possibility of re-identification means data remains personal

### ENISA — Pseudonymisation Techniques and Best Practices (2019)

- **Key Content**:
  - Technical analysis of pseudonymisation techniques: counter-based, random number generator, hash function, HMAC, encryption
  - Best practices for key management in pseudonymisation
  - Clarification that pseudonymisation is a security measure, not an anonymisation technique
  - Recommendations for implementing pseudonymisation under Art. 25 and Art. 32

### EDPB Guidelines 04/2020 on the Use of Location Data and Contact Tracing Tools in the Context of the COVID-19 Outbreak

- **Relevant Section**: Section 3 on anonymisation of location data — the EDPB confirmed that simply removing device identifiers from location data does not anonymise it if movement patterns enable re-identification. Applied the WP29 three-criteria test to mobility data.
