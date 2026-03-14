# Pseudonymization and Re-Identification Risk — Standards and References

## Primary GDPR Articles

### Article 4(5) — Definition of Pseudonymization
'Pseudonymisation' means the processing of personal data in such a manner that the personal data can no longer be attributed to a specific data subject without the use of additional information, provided that such additional information is kept separately and is subject to technical and organisational measures to ensure that the personal data are not attributed to an identified or identifiable natural person.

### Recital 26 — Pseudonymized Data Remains Personal Data
The principles of data protection should apply to any information concerning an identified or identifiable natural person. Personal data which have undergone pseudonymisation, which could be attributed to a natural person by the use of additional information should be considered to be information on an identifiable natural person. To determine whether a natural person is identifiable, account should be taken of all the means reasonably likely to be used, such as singling out, either by the controller or by another person to identify the natural person directly or indirectly.

### Article 25(1) — Pseudonymization as a By-Design Measure
The controller shall implement appropriate technical and organisational measures, such as pseudonymisation, which are designed to implement data-protection principles, such as data minimisation, in an effective manner and to integrate the necessary safeguards into the processing.

### Article 32(1)(a) — Pseudonymization as a Security Measure
The controller and the processor shall implement appropriate technical and organisational measures to ensure a level of security appropriate to the risk, including inter alia: (a) the pseudonymisation and encryption of personal data.

### Article 89(1) — Pseudonymization for Research Safeguards
Processing for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes, shall be subject to appropriate safeguards. Those safeguards shall ensure that technical and organisational measures are in place in particular in order to ensure respect for the principle of data minimisation. Those measures may include pseudonymisation provided that those purposes can be fulfilled in that manner.

## Regulatory Guidance

### ENISA "Pseudonymisation Techniques and Best Practices" (November 2019)
The European Union Agency for Cybersecurity (ENISA) published a comprehensive report cataloguing pseudonymization techniques applicable to GDPR compliance. Key findings:
- **Five technique categories:** counter-based, random number generator, cryptographic hash, message authentication code (HMAC), encryption-based
- **Identifier types:** direct identifiers (name, email, ID number), quasi-identifiers (age, ZIP, gender), sensitive attributes
- **Pseudonymization policies:** deterministic (same input always produces same pseudonym) vs. non-deterministic (different pseudonym each time)
- **Recovery mechanisms:** lookup table, deterministic computation, decryption
- The report emphasizes that the "additional information" (Art. 4(5)) — whether a mapping table, encryption key, or HMAC key — must be kept separately with appropriate access controls

### Article 29 Working Party Opinion 05/2014 on Anonymisation Techniques (WP216)
Published April 2014, this opinion distinguishes anonymization from pseudonymization and defines three risk criteria:
- **Singling out:** Is it possible to isolate a record relating to an individual?
- **Linkability:** Is it possible to link two or more records relating to the same individual?
- **Inference:** Is it possible to deduce the value of an attribute from other available values?

A technique must resist all three criteria to achieve anonymization. Pseudonymization typically resists singling out but may not resist linkability or inference.

### ICO Anonymisation Code of Practice (2012)
The UK Information Commissioner's Office introduced the **motivated intruder test**: a reasonably competent person who has access to resources such as the internet, libraries, and all public documents, and who employs investigative techniques such as making enquiries of people who may have information. The test does not assume that the intruder has specialist knowledge (e.g., hacking skills) or access to specialist equipment, or that the intruder would resort to criminality.

### EDPB Guidelines 4/2019 on Article 25 — Data Protection by Design and by Default
Section 2.1.4 identifies pseudonymization as one of the key technical measures for implementing data protection by design. The guidelines note that pseudonymization can:
- Reduce the risk of data processing
- Help controllers meet their data protection obligations
- Be an appropriate safeguard under Article 89(1) for research processing

### CNIL "Guide on the Use of Personal Data in AI Systems" (2022)
The French data protection authority recommends pseudonymization as a baseline measure for training machine learning models. Specific recommendations include:
- Pseudonymize identifiers before ingestion into training pipelines
- Maintain separation between the pseudonymization mapping and the training environment
- Evaluate re-identification risk on the trained model's outputs (membership inference attacks)

## Technical Standards

### NIST SP 800-188 "De-Identifying Government Datasets" (2016)
Provides a framework for assessing re-identification risk in de-identified datasets. Key concepts:
- **Equivalence class:** The set of records sharing the same quasi-identifier values
- **k-anonymity:** Each equivalence class contains at least k records
- **Re-identification risk metrics:** Prosecutor, journalist, and marketer models
- **Threshold guidance:** Acceptable risk thresholds depend on data sensitivity and release context

### ISO/IEC 20889:2018 — Privacy Enhancing Data De-Identification Techniques
International standard classifying de-identification techniques into:
- Statistical tools (sampling, aggregation, perturbation)
- Cryptographic tools (hashing, encryption, tokenization)
- Suppression tools (masking, generalization, swapping)
Provides a framework for selecting techniques based on data utility requirements and privacy risk tolerance.

### ISO/IEC 27559:2022 — Privacy Enhancing Data De-Identification Framework
Extends ISO 20889 with a process framework for planning, implementing, and monitoring de-identification. Includes guidance on:
- Risk assessment methodology for re-identification
- Ongoing monitoring of re-identification risk as external data landscapes change
- Documentation requirements for de-identification decisions
