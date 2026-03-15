# Purpose Limitation Standards and Regulatory References

## Primary GDPR Articles

### Article 5(1)(b) — Purpose Limitation
Personal data shall be collected for specified, explicit and legitimate purposes and not further processed in a manner that is incompatible with those purposes; further processing for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes shall, in accordance with Article 89(1), not be considered to be incompatible with the initial purposes.

### Article 6(4) — Compatibility Assessment
Where the processing for a purpose other than that for which the personal data have been collected is not based on the data subject's consent or on a Union or Member State law, the controller shall, in order to ascertain whether processing for another purpose is compatible with the purpose for which the personal data are initially collected, take into account, inter alia:
(a) any link between the purposes
(b) the context in which the personal data have been collected
(c) the nature of the personal data
(d) the possible consequences of the intended further processing
(e) the existence of appropriate safeguards

### Article 13(1)(c) — Purpose Disclosure at Collection
The controller shall, at the time when personal data are obtained, provide the data subject with the purposes of the processing for which the personal data are intended as well as the legal basis for the processing.

### Article 14(1)(c) — Purpose Disclosure for Indirect Collection
Where personal data have not been obtained from the data subject, the controller shall provide the data subject with the purposes of the processing for which the personal data are intended as well as the legal basis for the processing.

## Regulatory Guidance

### Article 29 Working Party Opinion 03/2013 (WP203)
Provides detailed analysis of the purpose limitation principle including:
- Definition of "specified, explicit and legitimate" purposes
- Assessment framework for compatibility of further processing
- Five key factors for compatibility assessment (now codified in Article 6(4))
- Relationship between purpose limitation and lawful basis
- Practical examples of compatible and incompatible processing

### EDPB Guidelines 4/2019 on Article 25
Addresses purpose limitation in the context of data protection by design:
- Technical measures to enforce purpose limitation at the system level
- Purpose-tagged data stores as a design pattern
- Automated enforcement through access control policies
- Logging and monitoring of purpose compliance

### Recital 50 — Further Processing Compatibility
The processing of personal data for purposes other than those for which the personal data were initially collected should be allowed only where the processing is compatible with the purposes for which the personal data were initially collected.

## Technical Standards

### ISO/IEC 27701:2019 — Privacy Information Management
Section 7.2.1 requires organizations to identify and document purposes for processing personal data. Section 7.4.1 requires limiting the collection of personal data to that which is relevant and necessary for identified purposes.

### NIST Privacy Framework v1.0
CT.DM-P1: Data elements can be accessed for authorized processing. CT.DM-P3: Data elements are limited to the minimum necessary for authorized processing.

### Open Policy Agent (OPA) / Cedar
Policy-as-code frameworks for implementing fine-grained, purpose-based access control. OPA uses Rego language for policy definition; Cedar (developed by Amazon) uses a declarative syntax designed specifically for authorization policies.
