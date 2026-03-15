# Standards and Regulatory References — Personal Data Classification Test

## Primary Legislation

### GDPR — Regulation (EU) 2016/679

- **Article 4(1)**: Definition of personal data — "any information relating to an identified or identifiable natural person ('data subject'); an identifiable natural person is one who can be identified, directly or indirectly, in particular by reference to an identifier such as a name, an identification number, location data, an online identifier or to one or more factors specific to the physical, physiological, genetic, mental, economic, cultural or social identity of that natural person"
- **Article 4(5)**: Definition of pseudonymisation — processing such that data can no longer be attributed to a specific data subject without the use of additional information, provided such additional information is kept separately and subject to technical and organisational measures
- **Recital 26**: Principles of data protection should apply to any information concerning an identified or identifiable natural person. To determine whether a natural person is identifiable, account should be taken of all the means reasonably likely to be used by the controller or by any other person to identify the natural person
- **Recital 30**: Online identifiers (IP addresses, cookie identifiers, RFID tags) may be combined with other information to create profiles and identify natural persons

## Case Law

### Breyer v Bundesrepublik Deutschland — CJEU Case C-582/14 (19 October 2016)

- **Court**: Court of Justice of the European Union (Second Chamber)
- **Citation**: ECLI:EU:C:2016:779
- **Holding**: Dynamic IP addresses registered by an online media service provider when a user accesses a website constitute personal data in relation to that provider where the provider has the legal means which enable it to identify the data subject with additional data held by the internet service provider
- **Key Paragraphs**: Paras 42-49 (relative approach to identifiability), Para 47 (legal means sufficient, no need for direct access)
- **Significance**: Established that the identifiability assessment is relative to the controller and that legal means of obtaining identifying information from third parties count toward "reasonably likely" means

### Nowak v Data Protection Commissioner — CJEU Case C-434/16 (20 December 2017)

- **Court**: Court of Justice of the European Union (Second Chamber)
- **Citation**: ECLI:EU:C:2017:994
- **Holding**: Written answers submitted by a candidate at a professional examination and any comments made by an examiner constitute personal data of the candidate
- **Significance**: Broadened the "relating to" element — information need not be biographical to be personal data; it suffices that the information is linked to the individual by reason of its content, purpose, or effect

### YS and Others v Minister voor Immigratie — CJEU Joined Cases C-141/12 and C-372/12 (17 July 2014)

- **Court**: Court of Justice of the European Union (Third Chamber)
- **Citation**: ECLI:EU:C:2014:2081
- **Holding**: A legal analysis contained in a document about an asylum decision constitutes personal data of the applicant
- **Significance**: Confirmed the "result" element of the relating-to test — processing impact on a person's rights establishes the data as personal

## Regulatory Guidance

### Article 29 Working Party — Opinion 4/2007 on the Concept of Personal Data (WP136)

- **Adopted**: 20 June 2007
- **Key Content**: Detailed analysis of the four constituent elements of personal data (any information, relating to, identified or identifiable, natural person). Established the content-purpose-result framework for the "relating to" element
- **Status**: Endorsed by the EDPB under Art. 94(2) GDPR and remains authoritative guidance

### Article 29 Working Party — Opinion 05/2014 on Anonymisation Techniques (WP216)

- **Adopted**: 10 April 2014
- **Key Content**: Three-criteria test for anonymisation effectiveness (singling out, linkability, inference). Analysis of anonymisation techniques (noise addition, permutation, differential privacy, k-anonymity, l-diversity, t-closeness)
- **Status**: Endorsed by the EDPB; remains the primary framework for assessing anonymisation adequacy

### EDPB Guidelines 04/2019 on Article 25 — Data Protection by Design and by Default

- **Adopted**: 20 October 2020 (version 2.0)
- **Relevant Section**: Section 2.1 discusses the relationship between data classification and implementing appropriate technical measures under Art. 25

## National Supervisory Authority Guidance

### ICO (UK) — What Is Personal Data?

- **Reference**: ICO Guide to Data Protection, Chapter on Personal Data
- **Key Guidance**: The ICO applies the "motivated intruder" test — would a person with access to the data, without specialist skills but with motivation, be able to identify an individual? If yes, the data is personal data. This supplements the Recital 26 test with a practical assessment methodology

### CNIL (France) — Guide on Personal Data and Anonymisation

- **Reference**: CNIL Practical Guide: Anonymisation, September 2019
- **Key Guidance**: Provides a structured methodology for distinguishing personal data, pseudonymised data, and anonymised data with worked examples from healthcare, transport, and digital services sectors
