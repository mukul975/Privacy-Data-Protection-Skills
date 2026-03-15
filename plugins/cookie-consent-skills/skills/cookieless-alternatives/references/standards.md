# Cookie-less Alternatives Standards and References

## Privacy Sandbox APIs

### Topics API
- Chrome-only interest-based advertising API
- ~470 advertising topic taxonomy; 5% noise for privacy
- Users can view and clear topics in Chrome settings
- Sites opt out via Permissions-Policy header

### Attribution Reporting API
- Event-level reports: 3-bit trigger data (clicks), 1-bit (views), 2-day delay
- Aggregatable reports: differential privacy noise via TEE, 10-60 min delay
- Replaces deterministic conversion tracking with privacy-preserving measurement

### Protected Audiences API (FLEDGE successor)
- On-device ad auctions for remarketing without cross-site tracking
- Interest groups stored locally, bidding runs in browser
- Fenced frames prevent publisher-side data leakage

### Shared Storage API
- Cross-site data with restricted output gates (select URL, private aggregation)
- Use cases: frequency capping, A/B testing without cookies

## Legal Framework

### ePrivacy Directive Article 5(3)
- Privacy Sandbox APIs may or may not require consent depending on implementation
- Topics API likely requires consent (stores/accesses data on device)
- CNIL analysis (2023) pending final determination

### CMA Privacy Sandbox Commitments
- UK Competition and Markets Authority oversees Google's Privacy Sandbox development
- Google committed to not giving itself preferential access to APIs
- CMA approval required before Chrome third-party cookie deprecation

## Cookieless Analytics Tools
- Plausible Analytics: no cookies, no PII, EU-hosted
- Fathom Analytics: no cookies, no PII, Canadian/EU hosting
- Umami: open-source, self-hosted, optional cookies
