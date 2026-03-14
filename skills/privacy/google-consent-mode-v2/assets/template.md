# Google Consent Mode v2 Implementation Checklist

## Organization: [Organization Name]
## GA4 Property: [G-XXXXXXX]
## Google Ads Account: [AW-XXXXXXX]
## Implementation Date: [YYYY-MM-DD]

---

## 1. Default Consent Configuration

| Parameter | EEA Default | UK Default | US Default | Other Default |
|-----------|-------------|------------|------------|---------------|
| ad_storage | denied | denied | granted | granted |
| ad_user_data | denied | denied | granted | granted |
| ad_personalization | denied | denied | granted | granted |
| analytics_storage | denied | denied | granted | granted |
| functionality_storage | granted | granted | granted | granted |
| personalization_storage | denied | denied | granted | granted |
| security_storage | granted | granted | granted | granted |

| Setting | Configured | Value |
|---------|-----------|-------|
| wait_for_update | [ ] Yes | 500ms |
| url_passthrough | [ ] Yes | true |
| ads_data_redaction | [ ] Yes | true |

## 2. CMP Integration

| Item | Status | Notes |
|------|--------|-------|
| CMP platform | [ ] Done | Platform: ___ |
| CMP consent categories mapped to Consent Mode | [ ] Done | |
| Consent update fires on user interaction | [ ] Done | |
| Consent state persists across pages | [ ] Done | |
| GPC signal handled | [ ] Done | |

## 3. Tag Consent Settings

| Tag | Required Consent | Additional Consent | Configured |
|-----|-----------------|-------------------|------------|
| GA4 Configuration | analytics_storage | — | [ ] |
| GA4 Events | analytics_storage | — | [ ] |
| Google Ads Conversion | ad_storage | ad_user_data | [ ] |
| Google Ads Remarketing | ad_storage | ad_user_data, ad_personalization | [ ] |
| Floodlight Counter | ad_storage | ad_user_data | [ ] |
| Floodlight Sales | ad_storage | ad_user_data | [ ] |

## 4. Verification

| Test | Pass | Fail |
|------|------|------|
| Default consent fires before Google tags | [ ] | [ ] |
| Consent update fires on CMP interaction | [ ] | [ ] |
| GA4 tags blocked when analytics_storage = denied | [ ] | [ ] |
| Ads tags blocked when ad_storage = denied | [ ] | [ ] |
| Cookieless pings sent when consent denied | [ ] | [ ] |
| gcs parameter correct in analytics requests | [ ] | [ ] |
| No cookies set when consent denied | [ ] | [ ] |

## 5. Modeling Readiness

| Requirement | Current | Target | Met |
|-------------|---------|--------|-----|
| Daily consented users (GA4 modeling) | ___ | 1,000+ | [ ] |
| Daily conversions (conversion modeling) | ___ | 70+ | [ ] |
| Consecutive days with Consent Mode | ___ | 7+ | [ ] |

---

**Implemented by**: [Name] | **Verified by**: [Name] | **Date**: [YYYY-MM-DD]
