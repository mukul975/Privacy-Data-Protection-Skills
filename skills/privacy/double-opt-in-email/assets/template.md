# Double Opt-In Email System — Configuration Specification

## System Configuration

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Token Length** | 256 bits (base64url encoded) | Cryptographic security against brute force |
| **Token Expiry** | 48 hours | Balance between user convenience and security |
| **Rate Limit** | 3 DOI requests per IP per hour | Prevent email flooding abuse |
| **Suppression List Storage** | SHA-256 hashed emails | Data minimization per Art. 5(1)(c) |
| **Consent Record Retention** | Duration of subscription + 6 years | Art. 7(1) + limitation period for claims |
| **Max Email Frequency** | 2 emails per month | As stated in consent text |
| **Re-consent Interval** | 24 months of inactivity | Maintain active consent |

## Email Templates

### Confirmation Email

| Field | Value |
|-------|-------|
| **From** | CloudVault SaaS Inc. <noreply@cloudvault-saas.eu> |
| **Subject** | Confirm your CloudVault newsletter subscription |
| **List-Unsubscribe** | <mailto:unsubscribe@cloudvault-saas.eu> |
| **List-Unsubscribe-Post** | List-Unsubscribe=One-Click |

**Body:**

Dear subscriber,

You requested to receive product updates and news from CloudVault SaaS Inc.

To confirm your subscription, please click the button below:

**[Confirm My Subscription]**

If you did not request this, simply ignore this email — you will not be subscribed.

This confirmation link expires in 48 hours.

CloudVault SaaS Inc.
42 Innovation Drive, Dublin, D02 YX88, Ireland
privacy@cloudvault-saas.eu

## Suppression List Status Report

| Metric | Count | As Of |
|--------|-------|-------|
| Total suppressed emails | 28,451 | 2026-03-14 |
| Suppressed via unsubscribe | 24,102 (84.7%) | |
| Suppressed via hard bounce | 3,219 (11.3%) | |
| Suppressed via spam complaint | 887 (3.1%) | |
| Suppressed via DSAR erasure | 243 (0.9%) | |

## Consent Record Example

```json
{
  "email": "sarah.murphy@protonmail.com",
  "purpose": "product_updates_newsletter",
  "initial_opt_in": {
    "timestamp": "2026-03-14T10:15:00Z",
    "ip_address": "198.51.100.42",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
  },
  "doi_confirmation": {
    "timestamp": "2026-03-14T10:22:30Z",
    "ip_address": "198.51.100.42",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
  },
  "consent_text": "I'd like to receive product updates, tips, and news from CloudVault SaaS Inc. Emails sent max 2 times per month. Unsubscribe anytime.",
  "consent_text_version": "sha256:a3b4c5d6...",
  "status": "confirmed"
}
```

## Sign-Off

| Role | Name | Date |
|------|------|------|
| DPO | Marta Kowalski | 2026-03-14 |
| Email Operations | Tomasz Nowak | 2026-03-14 |
| Engineering Lead | James Park | 2026-03-14 |
