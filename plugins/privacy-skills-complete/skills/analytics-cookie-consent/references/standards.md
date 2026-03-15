# Analytics Cookie Consent Standards and References

## Regulatory Framework

### ePrivacy Directive 2002/58/EC, Article 5(3)
- Analytics cookies are NOT strictly necessary for the service requested by the user
- Consent required for analytics cookies across all EU member states

### CNIL Audience Measurement Exemption (2020-2021)
- CNIL permits limited analytics without consent IF configured with strict privacy safeguards
- Conditions: no cross-site tracking, no third-party sharing, anonymized IP, 13-month cookies, 25-month data retention
- CNIL maintains list of tools qualifying for exemption: Matomo (self-hosted), AT Internet, Eulerian, Abla
- GA4 does NOT qualify: data processed by Google (third party), US transfer, cross-service processing

### Austrian DPA Decision (DSB D155.027, December 2021)
- Found Google Analytics non-compliant with GDPR due to US data transfers
- Triggered similar findings across multiple EU member states

### CNIL Decision on Google Analytics (February 2022)
- Ordered unnamed website to comply or cease using Google Analytics
- US transfer concern under Schrems II ruling

### EDPB Guidelines 05/2020 on Consent
- Analytics cookies require consent under GDPR/ePrivacy
- No exception for "anonymized" analytics unless truly anonymous

## GA4 Privacy Configuration
- Data retention: configurable 2 or 14 months
- Google Signals: can be disabled to prevent cross-device tracking
- IP anonymization: enabled by default in GA4
- Data sharing settings: configurable per property
- Consent Mode: behavioral modeling for non-consenting users
