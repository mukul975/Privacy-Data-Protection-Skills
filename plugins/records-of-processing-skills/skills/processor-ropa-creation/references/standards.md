# Standards and Regulatory References — Processor RoPA

## Primary Legislation

### GDPR Article 30(2) — Processor Records

- **Art. 30(2)**: Each processor and, where applicable, the processor's representative, shall maintain a record of all categories of processing activities carried out on behalf of a controller, containing:
  - **(a)** the name and contact details of the processor or processors and of each controller on behalf of which the processor is acting, and, where applicable, of the controller's or the processor's representative, and the data protection officer;
  - **(b)** the categories of processing carried out on behalf of each controller;
  - **(c)** where applicable, transfers of personal data to a third country or an international organisation, including the identification of that third country or international organisation and, in the case of transfers referred to in the second subparagraph of Article 49(1), the documentation of suitable safeguards;
  - **(d)** where possible, a general description of the technical and organisational security measures referred to in Article 32(1).

### GDPR Article 28 — Processor

- **Art. 28(1)**: Where processing is to be carried out on behalf of a controller, the controller shall use only processors providing sufficient guarantees to implement appropriate technical and organisational measures.
- **Art. 28(2)**: The processor shall not engage another processor without prior specific or general written authorisation of the controller. General authorisation requires notification of intended changes giving the controller the opportunity to object.
- **Art. 28(3)**: Processing by a processor shall be governed by a contract or other legal act that sets out the subject-matter and duration of the processing, the nature and purpose of the processing, the type of personal data and categories of data subjects, and the obligations and rights of the controller.
- **Art. 28(3)(a)**: The processor shall process personal data only on documented instructions from the controller.
- **Art. 28(4)**: Where a processor engages another processor, the same data protection obligations as set out in the contract between controller and processor shall be imposed on that other processor by way of a contract.

### GDPR Article 32 — Security of Processing

- **Art. 32(1)**: Taking into account the state of the art, the costs of implementation, and the nature, scope, context and purposes of processing, as well as the risk of varying likelihood and severity for the rights and freedoms of natural persons, the controller and processor shall implement appropriate technical and organisational measures.
- **Art. 32(4)**: The controller and processor shall take steps to ensure that any natural person acting under the authority of the controller or the processor who has access to personal data does not process them except on instructions from the controller.

### GDPR Article 33(2) — Processor Breach Notification

- **Art. 33(2)**: The processor shall notify the controller without undue delay after becoming aware of a personal data breach. This obligation links to the processor's Art. 30(2) records, which should identify the controller to be notified.

## Regulatory Guidance

### European Data Protection Board (EDPB)

- **EDPB Guidelines 07/2020 on controller and processor concepts (adopted 7 July 2021)**: Provides detailed criteria for determining whether an entity is a controller or processor, which directly determines whether Art. 30(1) or Art. 30(2) records are required. Key test: does the entity determine the purposes and means of processing?
- **EDPB Guidelines 2/2019 on processing under Article 6(1)(b) (adopted 9 April 2019)**: While focused on controllers, these guidelines clarify the scope of processing activities that must be recorded, which informs what the processor documents under Art. 30(2)(b).

### National Supervisory Authority Guidance

- **CNIL (France)**: The CNIL RoPA template includes a processor-specific section with fields for each controller served, processing categories per controller, sub-processor details, and transfer documentation.
- **ICO (United Kingdom)**: The ICO guidance on documentation emphasises that processors must maintain their own independent records and cannot rely on the controller's records to satisfy this obligation.
- **BfDI (Germany)**: Guidance clarifies that the general description of security measures under Art. 30(2)(d) must reflect the processor's actual implemented measures, which may differ from the controller's own security posture.

## Enforcement Precedents

- **Spanish AEPD — PS/00547/2021**: Fine imposed on a processor for failure to maintain Art. 30(2) records. The supervisory authority confirmed that processor record obligations are independently enforced and that the absence of controller records does not excuse processor non-compliance.
- **Belgian DPA — Decision 21/2022**: While primarily targeting a controller, the decision noted that the controller's processor also failed to maintain adequate records, contributing to the overall accountability failure.
- **Italian Garante — Ordinance against a cloud service provider (2021)**: The Garante required a cloud processor to demonstrate its Art. 30(2) records as part of an investigation into data breach handling, confirming that supervisory authorities routinely request processor records during investigations.

## ISO/IEC Standards

- **ISO/IEC 27701:2019**: Section 8.2.6 requires PII processors to maintain records of PII processing carried out on behalf of each PII controller. This directly maps to GDPR Art. 30(2).
- **ISO/IEC 27001:2022**: Annex A Control 5.34 and 5.20 (information transfer) support the documentation of security measures and data transfers required by Art. 30(2)(c) and (d).

## Contractual Framework

### Standard Contractual Clauses (EU SCCs)

- **Commission Implementing Decision (EU) 2021/914**: Module 3 (processor-to-sub-processor) SCCs include obligations for the processor to maintain records of processing activities and make them available to the controller and supervisory authority. Clause 8.1 requires the data importer to process on documented instructions only.

### Art. 28 Data Processing Agreement Requirements

The processor's Art. 30(2) records should be consistent with and informed by the Art. 28 DPA provisions:

| DPA Clause | Corresponding Art. 30(2) Field |
|------------|-------------------------------|
| Subject-matter and duration of processing | Art. 30(2)(b) — categories of processing |
| Nature and purpose of processing | Art. 30(2)(b) — categories of processing |
| Controller identity | Art. 30(2)(a) — controller details |
| Sub-processor authorisation and list | Art. 30(2)(c) — transfers (if sub-processor is in third country) |
| Security measures | Art. 30(2)(d) — technical and organisational measures |
