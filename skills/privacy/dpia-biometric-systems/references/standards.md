# Regulatory Standards -- DPIA for Biometric Systems

## Primary Legislation

### GDPR Article 35(1) -- Data Protection Impact Assessment
"Where a type of processing in particular using new technologies, and taking into account the nature, scope, context and purposes of the processing, is likely to result in a high risk to the rights and freedoms of natural persons, the controller shall, prior to the processing, carry out an assessment of the impact of the envisaged processing operations on the protection of personal data."

### GDPR Article 35(3)(b) -- Mandatory DPIA for Special Category Processing
A DPIA is required in particular where there is "processing on a large scale of special categories of data referred to in Article 9(1)." Biometric data processed for unique identification falls under Art. 9(1).

### GDPR Article 9(1) -- Prohibition on Special Category Processing
"Processing of [...] biometric data for the purpose of uniquely identifying a natural person [...] shall be prohibited" except where one of the Art. 9(2) conditions applies.

### GDPR Article 4(14) -- Definition of Biometric Data
"Personal data resulting from specific technical processing relating to the physical, physiological or behavioural characteristics of a natural person, which allow or confirm the unique identification of that natural person, such as facial images or dactyloscopic data."

### GDPR Article 35(7) -- DPIA Content Requirements
A DPIA shall contain at least:
- (a) a systematic description of the processing operations and purposes
- (b) an assessment of necessity and proportionality
- (c) an assessment of the risks to rights and freedoms
- (d) the measures envisaged to address the risks

### GDPR Article 36(1) -- Prior Consultation
"The controller shall consult the supervisory authority prior to processing where a data protection impact assessment under Article 35 indicates that the processing would result in a high risk in the absence of measures taken by the controller to mitigate the risk."

### GDPR Recital 91 -- Biometric DPIA Triggers
Confirms that processing of biometric data should be subject to a DPIA, particularly processing on a large scale or in specific contexts such as large-scale monitoring of publicly accessible areas.

## Regulatory Guidance

### EDPB WP248rev.01 -- Guidelines on DPIA (Revised 2017)
- Section II: Identifies nine criteria for when DPIA is required; meeting two triggers mandatory DPIA
- Criterion 4: Processing of special categories including biometric data
- Criterion 8: Innovative use of new technological or organisational solutions (biometric technologies)
- Annex 1: Provides national DPA DPIA blacklists including biometric processing

### EDPB Guidelines 3/2019 on Processing of Personal Data through Video Devices
- Section 5: Specifically addresses facial recognition in video surveillance
- Paragraph 77-78: Facial recognition for identification requires Art. 9(2) condition plus DPIA
- Paragraph 80: Distinguishes between facial detection (not Art. 9) and facial recognition (Art. 9)

### CNIL Reglement Type Biometrie (Deliberation 2019-001)
- Establishes three-tier template storage hierarchy: (1) individual device, (2) centralised with employee control, (3) centralised without control
- Requires necessity justification proportionate to storage tier
- Mandates alternative non-biometric access method
- Specifies technical safeguards including anti-spoofing and template encryption

### EDPB Opinion 13/2024 on Facial Recognition in Air Transport
- Requires DPIA for all facial recognition deployments in airports
- Mandates opt-in consent model for passengers
- Templates must be stored on passenger-held boarding documents, not in centralised database
- Retention limited to duration of the journey

## International Standards

### ISO/IEC 24745:2022 -- Biometric Information Protection
- Defines biometric template protection requirements
- Section 5: Template irreversibility -- templates must not allow reconstruction of raw biometric data
- Section 6: Template unlinkability -- templates from same biometric source in different systems must not be linkable
- Section 7: Template renewability -- compromised templates must be revocable and re-issuable

### ISO/IEC 30107:2023 -- Biometric Presentation Attack Detection
- Part 1: Framework for presentation attack detection (anti-spoofing)
- Part 3: Testing and reporting for biometric presentation attack detection mechanisms
- Liveness detection requirements for preventing spoofing with photographs, masks, and artificial fingerprints

### ISO/IEC 19795:2021 -- Biometric Performance Testing
- Framework for testing biometric system accuracy
- Defines False Acceptance Rate (FAR), False Rejection Rate (FRR), and Failure to Enrol (FTE)
- Requires demographic-disaggregated performance reporting

### ISO/IEC 29134:2023 -- Privacy Impact Assessment Guidelines
- Section 7.3: Processing description for biometric systems
- Section 7.5: Risk assessment methodology applicable to biometric data
- Section 7.7: Risk treatment for special category data
- Annex B: Example risk mitigation measures for biometric processing

## Enforcement Precedents

### Clearview AI -- Multiple Jurisdictions (2022-2024)
- CNIL: EUR 20,000,000 fine for scraping facial images without lawful basis or DPIA
- ICO: GBP 7,552,800 fine for facial recognition database without DPIA or lawful basis
- Garante (Italy): EUR 20,000,000 fine for biometric processing without Art. 9(2) condition
- Hellenic DPA (Greece): EUR 20,000,000 fine for biometric data processing violations

### Swedish DPA -- Facial Recognition in Schools (DI-2019-2221, 2019)
SEK 200,000 fine for using facial recognition for student attendance; found disproportionate when simpler alternatives existed.

### AEPD (Spain) -- Workplace Fingerprint (PS/00218/2021, 2021)
EUR 20,000 fine for employer requiring fingerprint timekeeping without necessity assessment or offering an alternative method.

### Belgian DPA -- Brussels Airport Facial Recognition (2021)
Required airport to conduct DPIA, implement opt-in consent, and provide manual alternative before deploying facial recognition boarding gates.
