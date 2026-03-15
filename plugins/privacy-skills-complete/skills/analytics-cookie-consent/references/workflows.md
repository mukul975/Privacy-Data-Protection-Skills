# Analytics Cookie Consent Workflows

## GA4 Privacy Configuration Workflow

1. Access GA4 Admin > Data Settings > Data Collection
2. Disable Google Signals (prevents cross-device tracking)
3. Disable Granular location and Device data collection
4. Set Data retention to 2 months (minimum)
5. Enable Reset user data on new activity
6. Disable all Data Sharing settings (benchmarking, technical support, etc.)
7. Disable Ads personalization in GA4 property settings
8. Configure Consent Mode integration
9. Document all settings in privacy compliance record

## Dual Analytics Implementation Workflow

### Deploy Matomo (CNIL-Exempt)
1. Install Matomo on EU-hosted self-managed infrastructure
2. Configure CNIL-exempt settings: anonymized IP, 13-month cookies, no cross-site
3. Set data retention: 25 months for visitor logs, indefinite for aggregated reports
4. Deploy Matomo tracking code on all pages (no consent required under CNIL exemption)
5. Configure Do Not Track respect
6. Add opt-out widget to cookie policy page

### Deploy GA4 (Consent-Required)
1. Implement Consent Mode v2 with default denied for analytics_storage
2. Configure GA4 with privacy-first settings
3. GA4 tags fire only when analytics consent granted
4. Consent Mode behavioral modeling fills gaps for non-consenting users

### Monitoring
1. Compare Matomo total traffic with GA4 consented traffic
2. Calculate effective consent rate: GA4 users / Matomo users
3. Monitor GA4 behavioral modeling coverage
4. Report combined analytics to stakeholders
