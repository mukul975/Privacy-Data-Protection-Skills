# Regulatory Standards — Auditing Cookie Consent A/B Testing

## Primary Regulations

### GDPR — Regulation (EU) 2016/679

- **Article 4(11)**: Consent must be an "unambiguous indication" by "clear affirmative action." Manipulative design undermines the unambiguous nature of consent.
- **Article 7(2)**: The request for consent must be "in a manner which is clearly distinguishable from the other matters, in an intelligible and easily accessible form, using clear and plain language." Dark patterns in consent banners violate this provision.
- **Article 7(4)**: Consent is not freely given if it is bundled or if refusal results in detriment. Cookie walls that block content unless cookies are accepted violate this.

### ePrivacy Directive 2002/58/EC (as amended)

- **Article 5(3)**: "The storing of information, or the gaining of access to information already stored, in the terminal equipment of a subscriber or user is only allowed on condition that the subscriber or user concerned has given his or her consent." This covers cookies, local storage, and similar technologies.

### CNIL Deliberation No. 2020-091 (September 17, 2020)

The French supervisory authority's cookie and tracker guidelines specify:
- Users must be able to accept or refuse cookies with the same degree of simplicity
- A "Refuse All" button must be present on the first layer of the consent interface
- Continued browsing does not constitute consent
- Cookie walls are generally prohibited
- Consent must be renewed at appropriate intervals (recommended maximum: 6 months)
- Pre-selected checkboxes are prohibited

## Enforcement Decisions

### CNIL Deliberation No. 2022-013 — Google LLC (January 6, 2022, EUR 150,000,000)

**Finding:** On google.fr, the cookie consent interface offered a prominent "I accept" button but no equivalent "I refuse" button on the first layer. Users who wanted to refuse had to click "Personalize" and then navigate through purpose-level settings before clicking "Confirm choices." Accepting required 1 click; refusing required 2+ clicks with significant cognitive load.

**Relevance to A/B testing:** Any consent banner variant that replicates this asymmetric interaction pattern would be non-compliant, regardless of whether it is a "test" variant.

### CNIL Deliberation No. 2022-014 — Meta Platforms Ireland (January 6, 2022, EUR 60,000,000)

**Finding:** On facebook.com, the "Accept Cookies" button was displayed on the first layer of the consent interface, while refusing required navigating to a second layer. The reject pathway involved additional steps not present in the accept pathway.

### EDPB Guidelines 3/2022 on Dark Patterns in Social Media Platform Interfaces (March 14, 2022)

The EDPB identified categories of dark patterns in privacy interfaces:
- **Overloading**: Bombarding users with requests, options, or information to nudge toward sharing more data
- **Skipping**: Designing interfaces so that users forget or skip privacy-protective options
- **Stirring**: Appealing to emotions or using visual cues to steer users toward less privacy-protective choices
- **Hindering**: Obstructing users from becoming informed or managing their data by making privacy actions difficult
- **Fickle**: Design inconsistency that makes it hard to find or use privacy tools
- **Left in the Dark**: Designing interfaces to hide information or privacy controls

### FTC Report: Bringing Dark Patterns to Light (September 2022)

US Federal Trade Commission report identifying dark patterns in privacy consent including:
- **Trick Questions**: Confusing phrasing that misleads users about what they are agreeing to
- **Misdirection**: Visual design that draws attention away from privacy-protective options
- **Forced Action**: Requiring consent to unrelated processing to access a service
- **Social Proof**: Falsely suggesting most users consent ("98% of users accepted")
