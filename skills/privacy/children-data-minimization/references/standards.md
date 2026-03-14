# Standards and Regulatory References — Children's Data Minimisation

## Primary Legislation

### GDPR Article 5(1)(c) — Data Minimisation

"Personal data shall be adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed ('data minimisation')."

### GDPR Article 5(1)(e) — Storage Limitation

"Personal data shall be kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed."

### GDPR Recital 38 — Specific Protection for Children

"Children merit specific protection with regard to their personal data, as they may be less aware of the risks, consequences and safeguards concerned and their rights in relation to the processing of personal data. Such specific protection should, in particular, apply to the use of personal data of children for the purposes of marketing or creating personality or user profiles and the collection of personal data with regard to children when using services offered directly to children."

### GDPR Recital 39 — Storage Limitation Elaboration

"Personal data should be processed only if the purpose of the processing could not reasonably be fulfilled by other means. In order to ensure that personal data are not kept longer than necessary, time limits should be established by the controller for erasure or for a periodic review."

### UK AADC Standard 8 — Data Minimisation

"Collect and retain only the minimum amount of personal data you need to provide the elements of your service in which a child is actively and knowingly engaged. Give children separate choices over which elements they wish to activate."

ICO interpretation:
- "Actively and knowingly engaged" excludes background data collection, passive tracking, and speculative data gathering.
- "Separate choices" requires unbundling: children must be able to use core features without activating data-intensive optional features.
- Retention must be limited to the shortest defensible period.

### COPPA Section 312.7 — Prohibition on Excess Collection

"An operator is prohibited from conditioning a child's participation in a game, the offering of a prize, or another activity on the child disclosing more personal information than is reasonably necessary to participate in such activity."

### COPPA Section 312.10 — Data Retention and Deletion

"An operator of a Web site or online service shall retain personal information collected online from a child for only as long as is reasonably necessary to fulfill the purpose for which the information was collected. The operator must delete such information using reasonable measures to protect against unauthorized access to, or use of, the information in connection with its deletion."

## EDPB Guidance

### EDPB Guidelines 05/2020 on Consent — Children's Data

- Paragraph 133: Processing of children's data should be subject to stricter necessity assessment.
- Paragraph 135: For low-risk processing, minimal data collection is expected; for higher-risk processing, the controller must demonstrate that each data element is strictly necessary.

### WP248rev.01 — DPIA Guidelines — Vulnerable Data Subjects

- Criterion 7: "Data concerning vulnerable data subjects" including children. When processing involves children's data, the EDPB expects heightened data minimisation as a mitigation measure.

## National Guidance

### ICO Age Appropriate Design Code — Standard 8 Detailed Guidance

The ICO provides the following specific interpretations:
- **Background data collection prohibited**: Services must not collect data through sensors (microphone, camera, accelerometer, GPS) unless the child has actively triggered a feature requiring that sensor.
- **Contact list access prohibited**: Uploading or accessing the child's device contact list is not proportionate for "find friends" features when username-based search or invite codes are available alternatives.
- **Persistent identifiers**: Device advertising identifiers (IDFA, GAID) must not be collected from children for advertising purposes. First-party session identifiers are preferable.
- **Metadata collection**: Collection of detailed interaction metadata (screen taps, scroll depth, hover time) is not proportionate for general analytics when aggregate page-view data suffices.
- **Retention in practice**: The ICO expects controllers to implement automated deletion schedules, not merely define retention periods in policies.

### CNIL Guidelines on Children's Data (2021)

- CNIL recommends that controllers processing children's data implement "privacy by default at the strongest level."
- Data collection from children should be limited to what is strictly necessary for the educational, entertainment, or social purpose the child is actively using.
- CNIL specifically warns against collecting location data from children except where strictly necessary for a safety feature actively requested by the parent.

## ISO/IEC Standards

### ISO/IEC 27701:2019 — Privacy Information Management System

- **Section 7.4.1**: Data minimisation — the organisation should limit the processing of PII to what is adequate, relevant and necessary for the identified purposes.
- **Annex D.7.4.1**: Specific guidance on implementing data minimisation, including periodic review of data collected against stated purposes.

### ISO/IEC 29100:2011 — Privacy Framework

- **Principle 3**: Collection limitation — the collection of PII should be limited to what is within the bounds of applicable law and strictly necessary for the specified purposes.
- **Principle 7**: Data minimisation — minimise the PII that is processed and the number of privacy stakeholders and people to whom PII is disclosed or who have access to it.

## Enforcement Decisions

- **TikTok (DPC Ireland, 2023)**: EUR 345 million fine. DPC found excessive data collection from children including default public profiles that exposed children's content beyond what was necessary for the service.
- **YouTube/Google (FTC, 2019)**: USD 170 million. Google collected persistent identifiers from child-directed channel viewers for advertising — data not necessary for the video streaming service.
- **Epic Games/Fortnite (FTC, 2022)**: USD 275 million. Epic collected more data than necessary from children, including enabling voice communications by default when the gaming service could function without them.
- **Clearview AI (Various DPAs, 2022)**: Multiple fines for collecting facial images of individuals including children from public internet sources — extreme example of disproportionate collection affecting children among others.
