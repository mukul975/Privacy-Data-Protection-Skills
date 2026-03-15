# Server-Side Tracking Standards and References

## Technical Documentation

### Google Tag Manager Server-Side
- Server container deployment on Google Cloud Run, AWS, or managed providers
- Client-server communication via GA4 Measurement Protocol
- Custom domain configuration for first-party context
- Tag templates for GA4, Google Ads, and Meta Conversions API

### Meta Conversions API (CAPI)
- Server-to-server event forwarding for Meta advertising
- Event deduplication with browser Pixel events
- Required parameters: event_name, event_time, action_source
- Privacy controls: IP anonymization, data hashing

### Safari Intelligent Tracking Prevention (ITP)
- Client-side JavaScript cookies capped at 7 days
- Link-decorated cookies capped at 24 hours
- Server-set first-party cookies not affected by ITP
- Drives adoption of server-side cookie management

## Legal Framework

### ePrivacy Directive 2002/58/EC, Article 5(3)
- Server-side cookies still require consent if non-essential
- Moving cookie setting from client to server does not eliminate consent requirement
- The legal analysis is based on purpose, not technical mechanism

### GDPR Article 5(1)(c) — Data Minimization
- Server-side architecture enables data filtering before third-party sharing
- Reduces data exposure to what is necessary for each destination
- Aligns with purpose limitation (Article 5(1)(b))

### GDPR Article 28 — Data Processor Requirements
- Server hosting providers are processors under GDPR
- Data Processing Agreements required with hosting providers
- Article 28(3) requirements: processing only on controller instructions, security measures

### GDPR Articles 44-49 — International Transfers
- Server container location determines transfer analysis
- EU-hosted containers avoid transfer issues for EU user data
- US-hosted containers require transfer mechanism (adequacy, SCCs, or derogation)

### CNIL Deliberation No. 2020-091
- Confirms server-set cookies still subject to consent requirements
- Technical mechanism does not change legal obligation
