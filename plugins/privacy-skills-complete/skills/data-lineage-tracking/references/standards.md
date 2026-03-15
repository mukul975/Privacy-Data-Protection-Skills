# Data Lineage Tracking - Regulatory Standards

## GDPR References

### Article 5(1)(e) - Storage Limitation
Personal data shall be kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed. Lineage tracking must document retention periods at each storage node and the mechanism for deletion or anonymization at expiry.

### Article 5(2) - Accountability
The controller shall be responsible for, and be able to demonstrate compliance with, paragraph 1. Data lineage documentation serves as evidence of accountability by showing exactly how data flows through the organization and what controls apply at each stage.

### Article 30 - Records of Processing Activities
Article 30(1) requires controllers to maintain records including categories of processing, categories of personal data, recipients, transfers to third countries, and envisaged time limits for erasure. Data lineage tracking directly supports Art. 30 compliance by mapping these elements across all systems.

Specific Art. 30(1) fields supported by lineage:
- (b) purposes of the processing — mapped at each lineage node
- (c) categories of data subjects and personal data — documented at collection points
- (d) categories of recipients — captured in data flow documentation
- (e) transfers to third countries — identified in transfer mapping with Art. 44-49 safeguards
- (f) envisaged time limits for erasure — recorded at each storage location

### Article 33(3) - Breach Notification Content
Breach notifications to supervisory authorities must describe the categories and approximate number of data subjects and personal data records concerned. Lineage tracking enables rapid scoping of breach impact by tracing which data flowed through the compromised system.

### Article 35 - Data Protection Impact Assessment
DPIA is required for processing likely to result in high risk. Lineage tracking helps identify processing that meets Art. 35(3) thresholds by revealing data flow patterns involving systematic monitoring, large-scale processing, or special category data combinations.

### Recital 26 - Identifiability Assessment
To determine whether a natural person is identifiable, account should be taken of all the means reasonably likely to be used. Lineage documentation of transformation steps (pseudonymization, aggregation, anonymization) provides the basis for assessing identifiability at each processing stage.

## WP29/EDPB Guidance

### WP29 Opinion 05/2014 on Anonymization Techniques
Provides criteria for assessing whether data has been effectively anonymized: singling out, linkability, and inference. Lineage tracking documents where anonymization occurs and whether re-identification risk exists at downstream nodes.

### EDPB Guidelines 01/2020 on Processing of Personal Data in Context of Connected Vehicles
Section 3.2 demonstrates lineage mapping applied to vehicle telemetry data, showing collection through in-vehicle sensors, transmission to manufacturer backend, processing for service delivery, and sharing with third-party service providers. Establishes precedent for granular data flow documentation.

## NIST Privacy Framework

### NIST PF ID.IM-P1
Data processing ecosystem risk management: The organization identifies and documents data processing ecosystem relationships (e.g., data processors, sub-processors, other third parties). Lineage tracking directly implements this subcategory.

### NIST PF ID.IM-P2
Data processing ecosystem risk management: Data processing ecosystem parties are identified, prioritized, and assessed using a privacy risk assessment process. Lineage provides the mapping needed for this assessment.

### NIST PF CT.DM-P1
Data processing management: Data are processed with adequate safeguards to prevent unauthorized access, disclosure, or use. Lineage documents what safeguards apply at each processing stage.

### NIST PF CT.PO-P3
Data processing policies, processes, and procedures: Policies, processes, and procedures for assessing and maintaining adequate safeguards for the processing of data are established and in place. Lineage maintenance procedures fulfill this subcategory.

## ISO 27701:2019

### Clause 7.2.8 - Records Related to Processing PII
The organization shall determine and maintain the necessary records in support of its obligations for the processing of PII, including records of data transfers between jurisdictions. Data lineage tracking supports this requirement by systematically documenting all processing activities and data movements.

### Clause 7.4.5 - PII Sharing, Transfer, and Disclosure
Prior to sharing, transferring, or disclosing PII, the organization shall identify and document the recipients. Lineage mapping provides this documentation as an inherent output.
