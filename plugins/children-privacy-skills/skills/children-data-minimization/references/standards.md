# Standards and Regulatory References — Children's Data Minimisation

## Primary Legislation

### GDPR Article 5(1)(c) — Data Minimisation Principle

"Personal data shall be adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed ('data minimisation')."

### GDPR Article 5(1)(e) — Storage Limitation Principle

"Kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data will be processed solely for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes."

### GDPR Recital 38 — Specific Protection for Children

"Children merit specific protection with regard to their personal data, as they may be less aware of the risks, consequences and safeguards concerned and their rights in relation to the processing of personal data. Such specific protection should, in particular, apply to the use of personal data of children for the purposes of marketing or creating personality or user profiles and the collection of personal data with regard to children when using services offered directly to children."

### GDPR Recital 39 — Data Minimisation and Storage Limitation

"The personal data should be adequate, relevant and limited to what is necessary for the purposes for which they are processed. [...] Personal data should be processed only if the purpose of the processing could not reasonably be fulfilled by other means."

### UK AADC Standard 8 — Data Minimisation

"Collect and retain only the minimum amount of personal data you need to provide the elements of your service in which a child is actively and knowingly engaged. Give children separate choices over which elements they wish to activate."

ICO interpretation:
- "Actively and knowingly engaged" means the child is intentionally using a specific feature.
- Background collection is prohibited unless triggered by a feature the child has actively requested.
- "Separate choices" means optional data-intensive features must be individually selectable.

### COPPA Section 312.7 — Prohibition on Conditioning

"An operator is prohibited from conditioning a child's participation in a game, the offering of a prize, or another activity on the child disclosing more personal information than is reasonably necessary to participate in such activity."

### COPPA Section 312.10 — Data Retention and Deletion

"An operator of a website or online service shall retain personal information collected online from a child for only as long as is reasonably necessary to fulfill the purpose for which the information was collected. The operator must delete such information using reasonable measures to protect against unauthorized access to, or use of, the information in connection with its deletion."

## Regulatory Guidance

### EDPB Guidelines 4/2019 on Article 25 Data Protection by Design and by Default (Adopted 20 October 2020)

- **Section 3.1**: Data minimisation by design means that the controller must determine the minimum amount of personal data necessary for each processing purpose and build this into the system design.
- **Paragraph 52**: Controllers should implement technical measures to automatically enforce data minimisation: pseudonymisation at collection, automatic expiry, inability to collect optional fields unless user activates the feature.
- **Paragraph 73**: Data protection by default means that only personal data which are necessary for each specific purpose are processed by default.

### ICO Data Minimisation Guidance (2023)

- Controllers should regularly review the data they hold and delete anything that is no longer necessary.
- For children's data, the ICO expects "a more rigorous approach" to data minimisation than for adult data.
- Background data collection (device identifiers, location, microphone, camera) must be disabled by default for children.
- Data collected for service delivery must not be repurposed for advertising, profiling, or commercial analytics.

### CNIL Deliberation No. 2019-093 on Mobile Applications

- Mobile apps directed at or accessible by children must not request permissions (camera, microphone, contacts, location) beyond what is strictly necessary for the core functionality.
- Pre-installed permissions must default to disabled.
- Data collection must be proportionate to the feature being used at the moment of collection.

## Enforcement Decisions

- **TikTok (DPC Ireland, 2023)**: EUR 345 million fine. TikTok collected excessive data from children including default public profiles (exposing all posted content), location data, device identifiers, and behavioural tracking data beyond what was necessary for the service. Violated Art. 5(1)(c).
- **YouTube/Google (FTC, 2019)**: USD 170 million. Google collected persistent identifiers from child-directed channel viewers for behavioural advertising — data not necessary for the video service.
- **Epic Games/Fortnite (FTC, 2022)**: USD 275 million. Epic collected personal information beyond what was necessary, including enabling real-time voice communications by default and collecting voice data from all players regardless of age.
- **Instagram/Meta (DPC Ireland, 2022)**: EUR 405 million. Meta collected and exposed more data than necessary from child users by allowing children to operate business accounts with public-by-default settings.

## Technical Standards

### ISO/IEC 27701:2019 — Privacy Information Management System

- **Section 7.4.1**: The organization shall limit the collection of PII to that which is adequate, relevant and necessary for the identified purpose(s).
- **Section 7.4.2**: The organization shall limit the processing of PII to that which is adequate, relevant and necessary for the identified purpose(s).
- **Section 7.4.5**: Data at the end of its retention period or no longer necessary for the identified purpose must be securely destroyed, de-identified, or anonymised.

### NIST Privacy Framework (Version 1.0, January 2020)

- **CT.DM-P1**: Data elements can be accessed for authorized processing.
- **CT.DM-P2**: Data elements are minimised following data processing rules.
- **CT.DM-P3**: Data can be deleted or destroyed as needed.

### ISO/IEC 29100:2011 — Privacy Framework

- **Principle 4: Data minimisation**: Minimise the PII that is processed and the number of parties that have access to it.
- **Principle 7: Collection limitation**: Limit the collection of PII to that which is within the boundaries of applicable law and strictly necessary for the specified purpose.
