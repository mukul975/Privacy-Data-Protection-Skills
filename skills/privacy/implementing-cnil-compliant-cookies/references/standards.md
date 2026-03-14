# Regulatory Standards — Implementing CNIL-Compliant Cookies

## Primary Regulations

### CNIL Deliberation No. 2020-091 (September 17, 2020)

The CNIL's official guidelines on cookies and similar trackers, replacing the 2013 guidelines:

- **Paragraph 11-13**: Consent must be a clear positive act. Pre-ticked boxes, scrolling, and browsing do not constitute consent.
- **Paragraph 14-15**: Equal ease — refusing cookies must be as simple as accepting. A "Refuse All" button must be as prominent as "Accept All."
- **Paragraph 16**: Continued browsing does not constitute consent.
- **Paragraph 17**: Cookie walls generally invalid as they deprive users of genuine choice.
- **Paragraph 20-22**: Essential cookies are exempt from consent. The exemption is narrow and applies only to cookies strictly necessary for the service.
- **Paragraph 24**: Consent choices should be stored for an appropriate period. CNIL recommends a maximum of 6 months before reconsent.
- **Paragraph 25-27**: Full information must be provided before consent: controller identity, purposes, recipients, consequences of acceptance/refusal.

### ePrivacy Directive 2002/58/EC

- **Article 5(3)**: Consent required for storing or accessing information on user's device. Exemption only for technically necessary storage.

### GDPR — Regulation (EU) 2016/679

- **Article 4(11)**: Consent definition — clear affirmative action.
- **Article 7**: Conditions for consent — freely given, specific, informed, unambiguous, easy withdrawal.
- **Article 13**: Information to be provided to data subjects.

## CNIL Enforcement Decisions

### Deliberation No. 2022-013 — Google LLC (EUR 150,000,000)

- Date: January 6, 2022
- Violations: (1) No "Refuse All" on first layer of google.fr consent banner; (2) Refusing required multiple clicks through secondary interface
- Key holding: Absence of equally prominent refuse button impedes user's ability to refuse as easily as accept

### Deliberation No. 2022-014 — Meta Platforms Ireland (EUR 60,000,000)

- Date: January 6, 2022
- Violations: Similar asymmetry on facebook.com — accept prominent, refuse buried in secondary layer
- Key holding: Same equal prominence requirement applied

### Deliberation No. 2022-174 — Microsoft Ireland (EUR 60,000,000)

- Date: December 22, 2022
- Violations: bing.com lacked equally visible refuse button
- Key holding: Consistent application of equal prominence standard

### Deliberation No. 2022-177 — TikTok (EUR 5,000,000)

- Date: December 29, 2022
- Violations: (1) Refusing cookies more complex than accepting; (2) Insufficient information about cookie purposes
- Key holding: Both interaction asymmetry and information insufficiency are violations

## Supervisory Authority Guidance

### CNIL Practical Guide to Cookies (Updated 2022)

Complementary guidance to the formal deliberation:
- Visual examples of compliant and non-compliant banners
- Technical guidance on implementing consent management
- FAQ on edge cases (analytics exemptions, A/B testing cookies, consent-as-a-service)
- Guidance on the narrow cookie wall exception

### CNIL Position on Analytics Exemptions (September 2020)

CNIL recognizes a limited exemption for first-party analytics when:
- The analytics serve only to produce anonymous statistical data
- The data is not crossed with other processing or transmitted to third parties
- The cookies are limited in scope (e.g., audience measurement only)
- Users are informed and can object
- Cookie lifetime is limited (13 months maximum)
- Data retention limited to 25 months
- Note: This exemption is CNIL-specific and not universally recognized across the EU
