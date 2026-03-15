# Google Consent Mode v2 Standards and References

## Google Documentation

### Consent Mode v2 Technical Specification
- Introduces two new parameters: ad_user_data and ad_personalization
- Seven total consent parameters controlling Google tag behavior
- Default/update command pattern for consent state management
- Region-specific default settings support

### Google Ads DMA Compliance Requirements (March 2024)
- All EEA advertisers must implement Consent Mode v2
- Without Consent Mode v2, Google cannot process EEA user data for remarketing or conversion measurement
- ad_user_data and ad_personalization must be explicitly set; omission treated as denied
- Google-certified CMP partners recommended for EU consent collection

### GA4 Behavioral Modeling
- Machine learning models estimate metrics for non-consenting users
- Requires minimum 1,000 consented daily users per web data stream
- Requires 7+ consecutive days of Consent Mode data
- Modeled data indicated with badge in reports

### Conversion Modeling
- Estimates conversions from non-consenting users
- Requires 70+ consented conversions per day per conversion action
- Requires Consent Mode active for 7+ consecutive days

## Legal Framework

### EU Digital Markets Act (DMA) — Regulation 2022/1925
- Designates Google as a "gatekeeper" for search, advertising, and browser services
- Article 5(2): Gatekeepers must obtain end-user consent for combining personal data across services
- Google's Consent Mode v2 is its mechanism for DMA Article 5(2) compliance

### ePrivacy Directive 2002/58/EC, Article 5(3)
- Consent required for storing cookies on user devices
- Consent Mode default denied state aligns with Article 5(3) requirements

### CJEU Case C-673/17 (Planet49)
- Active consent required; default consent states must be "denied"
- Consent Mode's default denied state for EEA users reflects Planet49 requirements
