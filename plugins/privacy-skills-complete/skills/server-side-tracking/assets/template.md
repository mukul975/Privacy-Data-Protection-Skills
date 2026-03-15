# Server-Side Tracking Implementation Template

## Organization: [Organization Name]
## Server Container URL: [https://data.pinnacle-ecommerce.com]
## Implementation Date: [YYYY-MM-DD]

---

## 1. Infrastructure

| Setting | Value |
|---------|-------|
| Hosting provider | [ ] Google Cloud Run / [ ] AWS / [ ] Other: ___ |
| Container region | ___ |
| Custom domain | ___ |
| SSL certificate | [ ] Managed / [ ] Let's Encrypt / [ ] Custom |
| Min instances | ___ |
| Max instances | ___ |

## 2. Data Flow Configuration

| Destination | Required Consent | Data Sent | IP Treatment |
|-------------|-----------------|-----------|-------------|
| GA4 | analytics_storage | Events, anonymized client_id | Last octet zeroed |
| Google Ads | ad_storage, ad_user_data | Conversions, gclid | Last octet zeroed |
| Meta CAPI | ad_storage, ad_user_data | Events, hashed email | Removed |
| Internal logs | None | Aggregate counts | Full (24h), then anonymized |

## 3. IP Anonymization Rules

| Destination | IPv4 Method | IPv6 Method | Retention |
|-------------|-------------|-------------|-----------|
| GA4 | Last octet zeroed | Last 80 bits zeroed | Per GA4 retention |
| Meta | Full removal | Full removal | Not sent |
| Internal | Full address | Full address | 24 hours |

## 4. Cookie Management

| Cookie | Set By | Duration | Consent Required | Purpose |
|--------|--------|----------|-----------------|---------|
| | Server (Set-Cookie) | | [ ] Yes / [ ] No | |

## 5. Monitoring

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Request latency (p99) | < 200ms | > 500ms |
| Error rate | < 0.1% | > 1% |
| Event throughput | Baseline +/- 20% | > 30% deviation |

---

**Implemented by**: [Name] | **Reviewed by**: [DPO Name] | **Date**: [YYYY-MM-DD]
