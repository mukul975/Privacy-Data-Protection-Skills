---
name: google-consent-mode-v2
description: >-
  Configuring Google Consent Mode v2 for privacy-compliant measurement and
  advertising. Covers default and update commands, consent state mapping to GA4
  and Google Ads, conversion modeling with cookieless pings, and EEA requirements
  effective March 2024.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: cookie-consent-compliance
  tags: "google-consent-mode, ga4, google-ads, conversion-modeling, eea-compliance"
---

# Configuring Google Consent Mode v2

## Overview

Google Consent Mode v2 is a framework that adjusts the behavior of Google tags (Analytics, Ads, Floodlight) based on user consent status. Announced in November 2023 with enforcement beginning March 2024, Consent Mode v2 introduces two new parameters — `ad_user_data` and `ad_personalization` — alongside the existing `analytics_storage` and `ad_storage` parameters. For advertisers serving users in the European Economic Area (EEA), implementing Consent Mode v2 is required to maintain measurement and audience capabilities in Google Ads and GA4. Without it, Google will not process EEA user data for remarketing lists or conversion measurement.

## Consent Mode v2 Parameters

### Parameter Definitions

| Parameter | Controls | Default | Description |
|-----------|----------|---------|-------------|
| `ad_storage` | Advertising cookies | denied | Controls whether advertising-related cookies (_gcl_*, IDE) can be read/written |
| `ad_user_data` | User data for advertising | denied | Controls whether user data can be sent to Google for advertising purposes |
| `ad_personalization` | Ad personalization | denied | Controls whether data can be used for remarketing and personalized ads |
| `analytics_storage` | Analytics cookies | denied | Controls whether analytics cookies (_ga, _gid) can be read/written |
| `functionality_storage` | Functionality cookies | granted | Controls functionality cookies (language preferences) |
| `personalization_storage` | Personalization cookies | denied | Controls personalization cookies (recommendations) |
| `security_storage` | Security cookies | granted | Controls security-related cookies (authentication, fraud prevention) |

### Consent State Mapping for Pinnacle E-Commerce Ltd

Map CMP consent categories to Consent Mode parameters:

| CMP Category | ad_storage | ad_user_data | ad_personalization | analytics_storage |
|-------------|------------|--------------|-------------------|-------------------|
| All rejected (default) | denied | denied | denied | denied |
| Analytics only | denied | denied | denied | granted |
| Analytics + Advertising | granted | granted | granted | granted |
| Analytics + Advertising (no personalization) | granted | granted | denied | granted |
| All accepted | granted | granted | granted | granted |

## Implementation

### Basic Implementation (Google Tag / gtag.js)

**Step 1: Set defaults before any Google tags load**

Place this script in the `<head>` before the Google tag:

```html
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}

// Set default consent state — deny all non-essential before user interaction
gtag('consent', 'default', {
  'ad_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied',
  'analytics_storage': 'denied',
  'functionality_storage': 'granted',
  'personalization_storage': 'denied',
  'security_storage': 'granted',
  'wait_for_update': 500  // Wait 500ms for CMP to load
});

// Enable URL passthrough for conversion measurement without cookies
gtag('set', 'url_passthrough', true);

// Enable ads data redaction when ad_storage is denied
gtag('set', 'ads_data_redaction', true);
</script>
```

**Step 2: Load the Google tag**

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-PINNACLE123"></script>
<script>
gtag('js', new Date());
gtag('config', 'G-PINNACLE123');
</script>
```

**Step 3: Update consent state when user interacts with CMP**

```javascript
// Called by the CMP when user makes a consent choice
function updateGoogleConsent(consentState) {
  gtag('consent', 'update', {
    'ad_storage': consentState.advertising ? 'granted' : 'denied',
    'ad_user_data': consentState.advertising ? 'granted' : 'denied',
    'ad_personalization': consentState.personalization ? 'granted' : 'denied',
    'analytics_storage': consentState.analytics ? 'granted' : 'denied'
  });
}
```

### Google Tag Manager Implementation

**Step 1: Configure Consent Initialization trigger**

In GTM, use the "Consent Initialization — All Pages" trigger type for the default consent tag. This fires before all other triggers.

**Default Consent Tag (Consent Initialization trigger):**

| Setting | Value |
|---------|-------|
| Tag type | Google tag: Consent configuration |
| Action | Default |
| ad_storage | Denied |
| ad_user_data | Denied |
| ad_personalization | Denied |
| analytics_storage | Denied |
| Wait for update | 500 ms |
| URL passthrough | Enabled |
| Ads data redaction | Enabled |

**Step 2: Configure Consent Update tag**

Create a custom HTML tag or use a CMP-specific template that fires on consent change:

**Update Consent Tag (Custom Event trigger: consent_update):**

| Setting | Value |
|---------|-------|
| Tag type | Google tag: Consent configuration |
| Action | Update |
| ad_storage | {{CMP - Ad Storage Consent}} |
| ad_user_data | {{CMP - Ad User Data Consent}} |
| ad_personalization | {{CMP - Ad Personalization Consent}} |
| analytics_storage | {{CMP - Analytics Storage Consent}} |

**Step 3: Configure tag consent settings**

For each Google tag in GTM, configure the built-in consent checks:

| Tag | Required Consent | Additional Consent |
|-----|-----------------|-------------------|
| GA4 Configuration | analytics_storage | — |
| GA4 Event | analytics_storage | — |
| Google Ads Conversion | ad_storage | ad_user_data |
| Google Ads Remarketing | ad_storage | ad_user_data, ad_personalization |
| Floodlight Counter | ad_storage | ad_user_data |
| Floodlight Sales | ad_storage | ad_user_data |

### Region-Specific Settings

Apply different defaults based on user geography:

```javascript
// Strict defaults for EEA users
gtag('consent', 'default', {
  'ad_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied',
  'analytics_storage': 'denied',
  'region': ['AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR',
             'DE', 'GR', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL',
             'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE', 'IS', 'LI', 'NO']
});

// Less restrictive defaults for US users (adjust per state law)
gtag('consent', 'default', {
  'ad_storage': 'granted',
  'ad_user_data': 'granted',
  'ad_personalization': 'granted',
  'analytics_storage': 'granted',
  'region': ['US']
});
```

## Conversion Modeling and Cookieless Pings

### How Consent Mode Preserves Measurement

When consent is denied, Google tags still send cookieless pings that include:
- Page URL (with ads_data_redaction applied)
- Timestamp
- User agent
- Referrer (if ads_data_redaction is false)
- Aggregate consent state

Google uses these pings, combined with data from consenting users, to build machine learning models that estimate:
- **Conversion modeling**: Estimated conversions from users who did not consent to ad_storage
- **Behavioral modeling in GA4**: Estimated user counts and session metrics for non-consenting users

### Conversion Modeling Requirements

For Google to generate modeled conversions, Pinnacle E-Commerce Ltd must meet:

| Requirement | Threshold |
|-------------|-----------|
| Minimum consented conversions per day | 70+ per conversion action |
| Minimum total conversions per day | 100+ per conversion action |
| Consent Mode implemented for | At least 7 consecutive days |
| Tag coverage | All conversion-relevant pages |

### GA4 Behavioral Modeling

GA4 behavioral modeling fills gaps in analytics data:

| Requirement | Threshold |
|-------------|-----------|
| Minimum daily consented users | 1,000+ per property |
| Minimum days of data | 7+ consecutive days |
| Consent Mode coverage | All GA4 pageview and event tags |

## Verification and Debugging

### Google Tag Assistant Verification

Use Google Tag Assistant (browser extension) to verify:

1. **Default consent fires before tags**: Check that consent defaults appear before the Google tag configuration in the Tag Assistant timeline
2. **Update consent fires on CMP interaction**: Verify consent update events appear when the user interacts with the cookie banner
3. **Tag behavior matches consent state**: Confirm that GA4 and Ads tags fire (or are blocked) based on consent

### Real-Time Debugging

In GA4 DebugView, consent-impacted events display with:
- A "consent" badge showing current consent state
- Missing user/session IDs when analytics_storage is denied
- Cookieless ping indicators

### Network-Level Verification

Monitor network requests to `https://www.google-analytics.com/g/collect`:

| Parameter | Consent Granted | Consent Denied |
|-----------|----------------|----------------|
| `_p` (Page ID) | Present | Present |
| `cid` (Client ID) | From _ga cookie | Randomly generated per-hit |
| `gcs` (Consent State) | G111 (all granted) | G100 (all denied) |
| `gcd` (Consent Default) | Present | Present |
| Cookie set | _ga, _gid | None |

## EEA Requirements (March 2024)

Google's Digital Markets Act (DMA) compliance requirements:

1. **Consent Mode v2 mandatory**: All advertisers targeting EEA users must implement Consent Mode v2 to maintain remarketing lists and conversion measurement
2. **ad_user_data and ad_personalization required**: The two new v2 parameters must be set; omitting them is treated as "denied"
3. **Verified CMP recommended**: Google recommends using a Google-certified CMP partner for EU consent collection
4. **Enhanced Conversions with consent**: Enhanced Conversions (first-party data matching) requires ad_user_data = granted

## Key References

- **Google Consent Mode v2 Documentation** — Official implementation guide
- **Google Tag Manager Consent Configuration** — GTM-specific setup instructions
- **Google Ads DMA Compliance Guide (March 2024)** — EEA-specific requirements
- **EU Digital Markets Act (DMA) Regulation 2022/1925** — Legal basis for Google's consent requirements
- **ePrivacy Directive 2002/58/EC, Article 5(3)** — Cookie consent legal basis
- **CJEU Case C-673/17 (Planet49)** — Active consent requirements applicable to consent mode default states
