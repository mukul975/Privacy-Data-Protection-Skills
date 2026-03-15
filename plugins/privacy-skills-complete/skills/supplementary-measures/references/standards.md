# Standards and Regulatory References

## Primary Guidance

### EDPB Recommendations 01/2020 on Supplementary Measures (Version 2.0, 18 June 2021)
- **Annex 2 — Use Cases**: Non-exhaustive catalogue of supplementary measures categorised as technical, contractual, and organisational, with effectiveness assessments per use case.
- **Use Case 1**: Data storage for backup without access by the importer — strong encryption with EU-held keys effective.
- **Use Case 2**: Transfer to cloud providers where importer needs access to plaintext — encryption alone is insufficient; consider pseudonymisation or split processing.
- **Use Case 3**: Remote access by the importer for support purposes — transport encryption with session logging; limit to minimum necessary access.
- **Use Case 4**: Transfer of pseudonymised data — effective where the mapping table is in the EU and the importer cannot re-identify.
- **Use Case 5**: Split processing — effective where no single entity in the third country holds the complete dataset.
- **Use Case 6**: Encrypted data merely transiting through a third country — transit encryption effective.
- **Use Case 7**: Transfer to country with adequate protection for specific sector — sector-specific laws may reduce supplementary measure burden.
- **Key principle**: Supplementary measures must be assessed on a case-by-case basis; there is no one-size-fits-all solution.

### EDPB Recommendations 02/2020 on European Essential Guarantees (10 November 2020)
- Provides the assessment framework against which supplementary measure effectiveness is evaluated.
- Each supplementary measure should address one or more EEG gaps identified in the TIA.

## GDPR Provisions

### Article 32 — Security of Processing
- **Art. 32(1)**: Controllers and processors must implement appropriate technical and organisational measures to ensure a level of security appropriate to the risk, including: (a) pseudonymisation and encryption; (b) ongoing confidentiality, integrity, availability, and resilience; (c) ability to restore availability and access; (d) regular testing and evaluation.
- **Relevance**: Art. 32 measures form the baseline for technical supplementary measures.

### Article 25 — Data Protection by Design and by Default
- **Art. 25(1)**: The controller shall implement appropriate technical and organisational measures designed to implement data protection principles effectively, including pseudonymisation.
- **Relevance**: Supplementary measures should be designed into the transfer architecture from the outset.

### Recital 26 — Anonymisation
- Personal data that has been rendered anonymous in such a manner that the data subject is no longer identifiable is not subject to the GDPR.
- **Relevance**: Anonymisation before transfer removes the data from Chapter V scope entirely.

## Encryption Standards

### NIST SP 800-175B Rev. 1 — Guideline for Using Cryptographic Standards in the Federal Government
- AES-256 recommended for data classified at the highest sensitivity levels.
- Key management guidance aligned with NIST SP 800-57 Part 1 Rev. 5.

### ENISA Report on Cryptographic Standards (2024)
- Recommends AES-256, ChaCha20-Poly1305, and RSA-4096/ECDSA P-384 for data protection in transit and at rest.
- Advises against deprecated algorithms: 3DES, RC4, SHA-1, RSA < 2048-bit.

### BSI Technical Guideline TR-02102-1 (Germany, 2024)
- German Federal Office for Information Security cryptographic recommendations.
- Aligns with ENISA; recommends AES-256-GCM and TLS 1.3 as minimum standards.

## Pseudonymisation Guidance

### ENISA Report on Pseudonymisation Techniques and Best Practices (2019)
- Defines pseudonymisation techniques: counter-based, RNG-based, cryptographic hash-based (HMAC), encryption-based, tokenisation.
- Recommends HMAC-SHA256 with a secret key as a robust pseudonymisation method.
- Emphasises that the security of pseudonymisation depends on the protection of the mapping table/key.

### WP29 Opinion 05/2014 on Anonymisation Techniques
- Criteria for assessing anonymisation effectiveness: singling out, linkability, and inference.
- If any of these risks remain, the data is pseudonymised (not anonymised) and remains personal data.

## Enforcement Precedents

### Austrian DSB — D550.738 (2022)
- Found that IP address pseudonymisation by truncating the last octet was insufficient because Google could re-identify using additional data held by Google.
- Significance: Supplementary measures must prevent re-identification in practice, considering all data available to the importer.

### Italian Garante — Google Analytics (2022)
- Statistical identifier assigned by the analytics platform was not effective pseudonymisation because the importer (Google) held the mapping data.
- Significance: Pseudonymisation is only effective as a supplementary measure if the mapping table is held exclusively in the EU.

### EDPS — Microsoft 365 Assessment (2024)
- Found that Microsoft's data encryption for EU institutional data was insufficient as a supplementary measure because Microsoft held the decryption keys and could be compelled to produce plaintext under US law.
- Significance: Encryption is only effective as a supplementary measure if the keys are held by the EU entity, not the cloud provider.

## ISO/IEC Standards

- **ISO/IEC 27001:2022**: Baseline information security management framework.
- **ISO/IEC 27701:2019**: Privacy information management extension to ISO 27001.
- **ISO/IEC 27018:2019**: Code of practice for PII protection in public clouds.
- **ISO/IEC 11770-3:2021**: Key management mechanisms.
