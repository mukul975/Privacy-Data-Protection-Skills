# Standards and Regulatory References — Data Labelling System

## Primary Legislation

### GDPR — Regulation (EU) 2016/679

- **Article 24**: Controller responsibility — implementing appropriate measures to demonstrate compliance. Labelling is an organisational measure demonstrating classification and appropriate handling.
- **Article 25**: Data protection by design — labelling systems implement by-design principles by embedding classification into data assets.
- **Article 32**: Security of processing — labels enable risk-proportionate security by ensuring controls match data sensitivity.

## International Standards

### ISO/IEC 27001:2022

- **Annex A.5.12**: Classification of information — information shall be classified according to legal requirements, value, criticality, and sensitivity.
- **Annex A.5.13**: Labelling of information — an appropriate set of procedures for information labelling shall be developed and implemented in accordance with the classification scheme adopted.

### ISO/IEC 27002:2022

- **Control 5.13 Guidance**: Labels should be applied to digital and physical assets. Automated labelling tools recommended. Labels should be recognisable and consistently applied across the organisation.

### NIST SP 800-53 Rev.5

- **AC-16**: Security and privacy attributes — associates security/privacy attributes (labels) with information and information system components.
- **MP-3**: Media marking — information system media shall be marked indicating distribution limitations, handling caveats, and applicable security markings.

## Technology Standards

### Microsoft Purview Information Protection

- **Sensitivity Labels**: Unified labelling platform for Microsoft 365, Azure, and endpoint devices. Labels embed in file metadata (Open XML custom properties) and persist across platforms.
- **Auto-labelling**: Server-side auto-labelling for Exchange, SharePoint, OneDrive based on sensitive information type detection. Client-side recommendation for Office desktop apps.
- **Azure RMS**: Azure Rights Management Service provides encryption and usage rights enforcement tied to sensitivity labels.

### OASIS Common Security Labels (CSLS)

- **Standard**: Open standard for security classification labelling, enabling interoperability between different classification systems.
