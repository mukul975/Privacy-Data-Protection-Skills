# Server-Side Tracking Implementation Workflows

## Infrastructure Setup Workflow

### Step 1: Provision Server Container
1. Choose hosting provider (Google Cloud Run, AWS App Runner, or managed service)
2. Deploy GTM server-side container image
3. Configure environment variables (container config key, preview server URL)
4. Set up auto-scaling (min 1, max based on traffic)
5. Configure health check endpoint

### Step 2: Custom Domain Configuration
1. Choose subdomain (e.g., data.pinnacle-ecommerce.com)
2. Create DNS CNAME record pointing to container
3. Configure SSL certificate (managed or Let's Encrypt)
4. Verify domain resolves to container
5. Test that requests to custom domain are handled by container

### Step 3: Client-Side Configuration
1. Update GA4 tag to send events to server container URL
2. Configure transport_url in gtag.js or GTM
3. Verify events arrive at server container
4. Test cookie setting via Set-Cookie headers

## Consent-Aware Forwarding Workflow

### Event Processing Pipeline
1. Event arrives at server container
2. Parse consent state from event payload
3. Validate consent state against expected schema
4. Route event based on consent:
   - Analytics consent granted: forward to GA4 Measurement Protocol
   - Advertising consent granted: forward to Google Ads, Meta CAPI
   - All consent denied: log aggregate counter only
5. Apply data minimization for each destination
6. Anonymize IP address before forwarding
7. Log forwarding result (success/failure)

### IP Anonymization Workflow
1. Extract IP from incoming request
2. Apply anonymization based on destination policy:
   - GA4: Zero last octet (IPv4) or last 80 bits (IPv6)
   - Meta: Remove IP entirely, use hashed identifiers
   - Internal: Retain full IP for 24 hours (security), then anonymize
3. Forward anonymized IP (or omit) with event data

## Monitoring and Audit Workflow

### Daily Health Check
1. Verify container instances are running
2. Check request latency (p99 < 200ms target)
3. Monitor error rate (< 0.1% target)
4. Verify event throughput matches expected baseline

### Monthly Privacy Audit
1. Compare client events sent vs server events received
2. Verify consent validation is applied to all forwarded events
3. Confirm no PII forwarded where consent is denied
4. Check IP anonymization is applied before third-party forwarding
5. Review cookie durations match policy
6. Audit outbound connections for unexpected destinations
