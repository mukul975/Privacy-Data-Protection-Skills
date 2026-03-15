# TCF v2.2 Standards and References

## IAB Europe Framework

### TCF v2.2 Technical Specification (May 2023)
- Defines TC String format (base64url-encoded binary)
- CMP API specification (__tcfapi)
- Global Vendor List (GVL) structure and versioning
- Publisher restriction encoding
- Key changes from v2.0: removal of LI for certain purposes, enhanced transparency requirements

### TCF Policies v4
- Rules governing CMP behavior and vendor obligations
- CMP registration requirements
- Vendor declaration requirements
- Compliance monitoring and enforcement procedures

### Global Vendor List (GVL)
- Published at: https://vendor-list.consensu.org/v3/vendor-list.json
- Updated weekly by IAB Europe
- Contains: vendor declarations, purpose descriptions, special features
- CMPs must consume GVL to display accurate vendor information

## Belgian DPA Decision 21/2022 (IAB Europe)
- Date: 2 February 2022
- Found IAB Europe is a data controller for TC String personal data
- Required IAB Europe to bring TCF into GDPR compliance
- Resulted in TCF v2.2 updates and enhanced validation requirements
- Fine: EUR 250,000
- IAB Europe appealed; CJEU Case C-604/22 pending

## ePrivacy Directive 2002/58/EC
- Article 5(3): consent for device storage (basis for TCF Purpose 1)
- TCF Purpose 1 ("Store and/or access information on a device") maps directly to Art. 5(3)

## GDPR References
- Article 4(11): Consent definition applicable to TCF consent signals
- Article 7: Conditions for valid consent
- Article 13-14: Transparency requirements for vendor disclosures
- Article 28: Processor requirements for CMP-vendor relationships
