# Cookie Lifetime Audit Standards and References

## CNIL 13-Month Maximum

### CNIL Deliberation No. 2020-091 (17 September 2020)
- Recommends maximum cookie lifetime of 13 months from point of collection
- Applies to both the consent cookie and the tracking cookies it enables
- Consent should be renewed at 6-month intervals

### CNIL Recommendation on Cookies (1 October 2020)
- Practical guidance: consent validity should not exceed 13 months
- Cookie lifetime and consent validity are distinct but related concepts

## Planet49 Duration Disclosure

### CJEU Case C-673/17, Paragraph 81
- Users must be informed about cookie duration BEFORE giving consent
- Duration disclosure is part of the "clear and comprehensive information" requirement
- Applies to all cookies, not just advertising cookies

## Browser Lifetime Restrictions

### Safari ITP (Intelligent Tracking Prevention)
- JavaScript cookies: 7-day cap
- JavaScript cookies with link decoration: 24-hour cap
- Server-set first-party cookies: no ITP cap
- Third-party cookies: blocked entirely
- localStorage: 7-day cap

### Firefox ETP (Enhanced Tracking Protection)
- Standard mode: blocks known third-party tracking cookies
- Strict mode: limits tracking first-party cookies to 7 days
- Fingerprinting scripts blocked

### Chrome Privacy Sandbox
- User-choice model for third-party cookies (not full deprecation)
- Privacy Sandbox APIs as alternatives to third-party cookies

## GDPR Storage Limitation

### Article 5(1)(e)
- Personal data stored for no longer than necessary
- Applies to cookie-stored personal data (client IDs, session data)
- Requires justification for retention period of each cookie
