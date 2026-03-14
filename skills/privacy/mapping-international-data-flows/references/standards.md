# Standards and Regulatory References

## Primary Legislation

### GDPR Article 30 — Records of Processing Activities
- **Art. 30(1)(e)**: Controllers must record transfers of personal data to a third country or international organisation, including the identification of that country or organisation and, in the case of transfers under Art. 49(1) second subparagraph, the documentation of suitable safeguards.
- **Art. 30(2)(c)**: Processors must record transfers to a third country or international organisation, including identification and safeguard documentation.
- **Relevance**: The data flow map directly supports Art. 30 compliance by providing the information needed to populate the transfer fields in the RoPA.

### GDPR Article 44 — General Principle for Transfers
- **Art. 44**: Any transfer of personal data which are undergoing processing or are intended for processing after transfer to a third country shall take place only if the conditions in Chapter V are complied with.
- **Relevance**: The data flow map identifies every transfer subject to Chapter V rules.

### GDPR Article 35 — Data Protection Impact Assessment
- **Art. 35(7)(a)**: A DPIA must include a systematic description of envisaged processing operations including the purposes and, where applicable, the legitimate interest pursued by the controller.
- **Relevance**: Data flow maps are an essential input to DPIAs for processing that involves international transfers.

## Regulatory Guidance

### EDPB Recommendations 01/2020 on Supplementary Measures (Step 1)
- Step 1 of the EDPB six-step methodology requires organisations to "know your transfers" — a comprehensive inventory of all international data flows.
- The Recommendations specify that the inventory should include: transfer parties, data categories, transfer purposes, destination countries, transfer mechanisms, and onward transfers.

### CNIL (France) — Data Mapping Guide (2023)
- Published a practical guide for data flow mapping including templates and methodology.
- Recommends a combined top-down (organisational structure) and bottom-up (system-by-system) approach.
- Emphasises the importance of identifying shadow IT and informal data sharing.

### ICO (UK) — International Transfer Guidance
- The ICO recommends maintaining a transfer register as the primary record of all restricted transfers.
- The register should be reviewed at least annually and updated whenever a new transfer begins or an existing transfer changes.

### NIST Privacy Framework (Version 1.0, January 2020)
- Identify-P (ID.IM-P) function: Inventory and mapping of personal data processing, including data flows.
- Aligned with the EU data flow mapping requirement but applicable globally.

## ISO/IEC Standards

- **ISO/IEC 27701:2019**: Section 7.2.8 requires organisations to identify and document all transfers of PII to other jurisdictions.
- **ISO/IEC 27001:2022**: Annex A Control 5.14 (Information transfer) requires policies and procedures for information transfer including cross-border data flows.
- **ISO/IEC 27002:2022**: Control 5.14 provides implementation guidance for information transfer controls.

## Tools and Frameworks

### Data Flow Mapping Tools
- **OneTrust Data Mapping**: Automated discovery and mapping of personal data processing activities and cross-border flows.
- **BigID Data Intelligence**: AI-driven data discovery and classification with data flow visualisation.
- **Collibra Data Governance**: Data lineage and data flow documentation with compliance mapping.
- **Manual mapping**: Spreadsheet-based approaches using the Art. 30 field structure remain valid for smaller organisations.

### Network Discovery Tools
- **DLP platforms** (Symantec, Microsoft Purview, Forcepoint): Detect personal data leaving the network boundary.
- **CASB solutions** (Microsoft Defender for Cloud Apps, Netskope): Monitor SaaS application usage and identify unsanctioned cross-border data flows.
