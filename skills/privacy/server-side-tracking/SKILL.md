---
name: server-side-tracking
description: >-
  Implementing server-side tracking with privacy controls using Google Tag Manager
  server containers. Covers first-party data collection, IP anonymization, consent-aware
  event forwarding, and reducing client-side third-party cookie exposure.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: cookie-consent-compliance
  tags: "server-side-tracking, gtm-server, first-party-data, ip-anonymization, consent-forwarding"
---

# Server-Side Tracking with Privacy Controls

## Overview

Server-side tracking moves data collection from the user's browser to a server-controlled environment, providing greater control over what data is shared with third parties. Instead of loading third-party JavaScript directly in the browser (which sets third-party cookies and sends data to external servers without intermediation), a server-side container receives events from the client, processes them, and selectively forwards data to analytics and advertising endpoints. This architecture enables IP anonymization before data leaves the first-party infrastructure, consent-based routing of events, and reduced reliance on third-party cookies — directly supporting ePrivacy Directive Article 5(3) compliance and data minimization under GDPR Article 5(1)(c).

## Architecture

### Client-Server Flow

```
User's Browser
    │
    ├── Client-side GTM container (minimal)
    │   └── Sends events to first-party endpoint
    │
    ▼
First-Party Server Endpoint
(https://data.pinnacle-ecommerce.com)
    │
    ├── Server-side GTM container
    │   ├── Validates consent state
    │   ├── Anonymizes IP address
    │   ├── Strips unnecessary identifiers
    │   ├── Applies data minimization rules
    │   │
    │   ├── [If analytics consent granted]
    │   │   └── Forward to Google Analytics 4
    │   │
    │   ├── [If advertising consent granted]
    │   │   ├── Forward to Google Ads
    │   │   ├── Forward to Meta Conversions API
    │   │   └── Forward to other ad platforms
    │   │
    │   └── [If all consent denied]
    │       └── Log aggregate pageview count only (no PII)
    │
    └── First-party server logs (retention: 90 days)
```

### Infrastructure Setup for Pinnacle E-Commerce Ltd

**Server Container Hosting Options:**

| Option | Provider | Monthly Cost (est.) | Latency | Control |
|--------|----------|-------------------|---------|---------|
| Google Cloud Run | Google Cloud | EUR 50-200 | Low | High |
| AWS App Runner | Amazon Web Services | EUR 40-180 | Low | High |
| Custom Docker | Self-hosted | EUR 30-150 | Varies | Maximum |
| Stape.io | Managed service | EUR 20-100 | Low | Medium |

**Pinnacle E-Commerce Ltd Configuration:**

| Setting | Value |
|---------|-------|
| Server container URL | https://data.pinnacle-ecommerce.com |
| Custom domain | data.pinnacle-ecommerce.com (CNAME to container) |
| Container region | europe-west1 (Belgium) — co-located with EU users |
| Scaling | Min 1 instance, max 10 instances |
| SSL certificate | Let's Encrypt via managed certificate |
| First-party cookie domain | .pinnacle-ecommerce.com |

### Custom Domain for First-Party Context

Using a subdomain of the main site domain ensures:
- Cookies set by the server container are first-party cookies
- Requests to `data.pinnacle-ecommerce.com` are same-site, avoiding third-party cookie restrictions
- Safari ITP and Firefox ETP do not apply cross-site tracking protections

**DNS Configuration:**
```
data.pinnacle-ecommerce.com  CNAME  server-container-abc123.run.app
```

## Consent-Aware Event Forwarding

### Consent Validation on the Server

Every event arriving at the server container includes the consent state from the client. The server validates this before forwarding:

**Event Payload from Client:**
```json
{
  "client_id": "1234567890.1709000000",
  "event_name": "purchase",
  "event_params": {
    "transaction_id": "TXN-2026-0314-001",
    "value": 149.99,
    "currency": "EUR",
    "items": [{"item_id": "SKU-001", "item_name": "Widget Pro"}]
  },
  "consent_state": {
    "analytics_storage": "granted",
    "ad_storage": "denied",
    "ad_user_data": "denied",
    "ad_personalization": "denied"
  },
  "user_agent": "Mozilla/5.0...",
  "ip_address": "203.0.113.42"
}
```

**Server-Side Routing Logic:**

| Destination | Required Consent | Data Sent |
|-------------|-----------------|-----------|
| GA4 Measurement Protocol | analytics_storage: granted | Event name, params, anonymized client_id |
| Google Ads Conversion API | ad_storage + ad_user_data: granted | Conversion data, gclid, hashed email |
| Meta Conversions API | ad_storage + ad_user_data: granted | Event data, fbp, hashed email/phone |
| Aggregate counter (internal) | None required | +1 to event type counter (no PII) |

### IP Anonymization

The server container anonymizes IP addresses before forwarding to any third party:

**Anonymization Rules:**

| Method | Description | Use Case |
|--------|-------------|----------|
| IPv4 last octet zeroing | 203.0.113.42 → 203.0.113.0 | Standard GA4 anonymization |
| IPv6 last 80 bits zeroing | 2001:db8::1234:5678 → 2001:db8:: | IPv6 anonymization |
| Full IP removal | IP not forwarded at all | Maximum privacy (Meta CAPI) |
| Geolocation-only | Resolve to country/region, discard IP | Geo reporting without IP |

**Pinnacle E-Commerce Ltd Policy:**
- GA4: Forward anonymized IP (last octet zeroed) for geographic reporting
- Google Ads: Forward anonymized IP for conversion geo-attribution
- Meta CAPI: Do not forward IP; send hashed email only (with ad_user_data consent)
- Internal logs: Retain full IP for 24 hours for security/fraud detection, then anonymize

### Data Minimization at the Server Layer

The server container strips data before forwarding:

| Data Element | Retained for GA4 | Retained for Ads | Retained Internally |
|-------------|-------------------|-------------------|-------------------|
| Full URL | Path only (no query params) | Path only | Full URL (90 days) |
| User agent | Reduced UA (SEC-CH-UA) | Reduced UA | Full UA (24 hours) |
| IP address | Anonymized | Anonymized | Full (24 hours) |
| Referrer | Domain only | Domain only | Full (90 days) |
| Client ID | GA client_id | gclid/wbraid only | Internal session ID |
| Email (hashed) | Not sent | SHA-256 hash | Not stored |

## Server-Side Tag Configurations

### GA4 Server-Side Tag

| Setting | Value |
|---------|-------|
| Measurement ID | G-PINNACLE123 |
| API Secret | Stored in Secret Manager |
| Send to | GA4 Measurement Protocol |
| IP anonymization | Enabled (default in GA4) |
| Client ID source | First-party _ga cookie |
| Session ID source | First-party _ga_* cookie |

### Meta Conversions API Tag

| Setting | Value |
|---------|-------|
| Pixel ID | 123456789012345 |
| Access Token | Stored in Secret Manager |
| Event deduplication | event_id matches browser Pixel event_id |
| Data sent | Event name, event_time, action_source, hashed email |
| IP forwarding | Disabled |
| User agent forwarding | Reduced UA only |

### First-Party Cookie Management

The server container can set first-party cookies via `Set-Cookie` headers, giving them longer lifetimes than client-side JavaScript cookies (which Safari ITP caps at 7 days):

| Cookie | Set By | Duration | Purpose |
|--------|--------|----------|---------|
| _ga | Server (Set-Cookie header) | 2 years | GA4 client identifier |
| _ga_PINNACLE | Server (Set-Cookie header) | 2 years | GA4 session persistence |
| _fbc | Server (Set-Cookie header) | 90 days | Meta click identifier |
| _pin_sess | Server (Set-Cookie header) | 30 minutes | Internal session tracking |

All cookies above are set only when the corresponding consent category is granted.

## Monitoring and Debugging

### Server Container Health Checks

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Request latency (p99) | < 200ms | > 500ms |
| Error rate | < 0.1% | > 1% |
| Event throughput | Baseline +/- 20% | > 30% deviation |
| Consent validation failures | 0 | > 0 |
| Forwarding failures (GA4) | < 0.5% | > 2% |
| Forwarding failures (Meta) | < 1% | > 5% |

### Data Flow Audit

Monthly audit of server-side tracking:
1. Compare client-side events sent vs. server-side events received (expect < 2% loss)
2. Verify consent state is correctly parsed for all forwarded events
3. Confirm no PII is forwarded to destinations where consent is denied
4. Check that IP anonymization is applied before all third-party forwarding
5. Validate first-party cookie durations match policy
6. Review server logs for any unexpected outbound connections

## Key Legal and Technical References

- **ePrivacy Directive 2002/58/EC, Article 5(3)** — Consent for device storage/access; server-side cookies still require consent if non-essential
- **GDPR Article 5(1)(c)** — Data minimization principle; server-side filtering reduces data shared with third parties
- **GDPR Article 28** — Data processor requirements for server hosting providers
- **GDPR Article 44-49** — Transfer restrictions if server container is outside EEA
- **Google Tag Manager Server-Side Documentation** — Container setup and tag configuration
- **Meta Conversions API Documentation** — Server-side event forwarding for Meta advertising
- **Safari Intelligent Tracking Prevention (ITP)** — Client-side cookie limitations driving server-side adoption
- **CNIL Deliberation No. 2020-091** — Server-set cookies still subject to consent requirements
