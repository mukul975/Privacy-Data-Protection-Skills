# Standards and Regulatory References — Anonymization as Retention Alternative

## Primary Legislation

### GDPR (Regulation (EU) 2016/679)
- **Recital 26** — Anonymous information outside GDPR scope; "all means reasonably likely to be used" test
- **Article 4(5)** — Definition of pseudonymization (contrast with anonymization)
- **Article 5(1)(e)** — Storage limitation: anonymization as a technique enabling compliant retention
- **Article 89(1)** — Safeguards for archiving, research, and statistical purposes; anonymization as a safeguard
- **Recital 162** — Statistical purposes and anonymization

### UK Data Protection Act 2018
- **Section 171** — Re-identification of de-identified personal data is a criminal offence

## Article 29 Working Party (WP29) Opinions

### Opinion 05/2014 on Anonymization Techniques (WP216) — Adopted 10 April 2014
- Establishes three risks: singling out, linkability, inference
- Evaluates randomization techniques: noise addition, permutation, differential privacy
- Evaluates generalization techniques: aggregation, k-anonymity, l-diversity, t-closeness
- Concludes that no single technique guarantees anonymization; combination approach required
- Pseudonymization is NOT anonymization

### Opinion 06/2013 on Open Data and Public Sector Information (WP207)
- Anonymization requirements for open data publication
- Re-identification risk assessment obligations

## Regulatory Guidance

### ICO (UK Information Commissioner's Office)
- **Anonymisation: Managing Data Protection Risk Code of Practice** — "Motivated intruder" test; practical guidance on achieving anonymization
- **ICO guidance on pseudonymization and anonymization** — Distinction between techniques; regulatory expectations

### EDPB (European Data Protection Board)
- **Guidelines 04/2020 on the use of location data and contact tracing tools** — Anonymization requirements for COVID-19 data (practical application)

### CNIL (France)
- **CNIL guidance on anonymization** — Practical anonymization techniques and validation criteria

## Academic and Research Standards

### Privacy-Preserving Data Publishing
- **Sweeney, L. (2002)** — k-Anonymity: A Model for Protecting Privacy. International Journal on Uncertainty, Fuzziness and Knowledge-Based Systems, 10(5), 557-570. — Established k-anonymity framework
- **Machanavajjhala, A. et al. (2007)** — l-Diversity: Privacy Beyond k-Anonymity. ACM Transactions on Knowledge Discovery from Data, 1(1). — Extended k-anonymity with l-diversity
- **Li, N., Li, T., & Venkatasubramanian, S. (2007)** — t-Closeness: Privacy Beyond k-Anonymity and l-Diversity. 23rd IEEE ICDE. — Established t-closeness metric
- **de Montjoye, Y-A. et al. (2013)** — Unique in the Crowd: The privacy bounds of human mobility. Scientific Reports, 3, 1376. — 4 spatiotemporal points uniquely identify 95% of individuals
- **Dwork, C. (2006)** — Differential Privacy. 33rd ICALP. — Foundational work on differential privacy

## Technical Standards
- **ISO/IEC 20889:2018** — Privacy enhancing data de-identification terminology and classification
- **ISO/IEC 27559:2022** — Privacy enhancing data de-identification framework
- **NIST SP 800-188** — De-Identifying Government Datasets (2016)
