# Google Consent Mode v2 Implementation Workflows

## Implementation Workflow

### Step 1: Audit Current Tag Setup
1. List all Google tags (GA4, Google Ads, Floodlight) on the site
2. Identify current consent mechanism (CMP platform)
3. Map CMP consent categories to Consent Mode parameters
4. Document current tag firing behavior

### Step 2: Implement Default Consent
1. Add consent default snippet before Google tag script
2. Set all non-essential parameters to "denied" for EEA
3. Configure region-specific defaults if serving multiple jurisdictions
4. Set wait_for_update to 500ms to allow CMP to load
5. Enable url_passthrough for cookieless conversion measurement
6. Enable ads_data_redaction for privacy when ad_storage denied

### Step 3: Implement Consent Update
1. Configure CMP callback to fire consent update
2. Map each CMP consent category to Consent Mode parameters
3. Test that update fires immediately on user consent interaction
4. Verify consent state persists across page navigations

### Step 4: Configure Tag Consent Settings (GTM)
1. For each tag in GTM, set required consent permissions
2. GA4 tags: require analytics_storage
3. Google Ads tags: require ad_storage + ad_user_data
4. Remarketing tags: require ad_storage + ad_user_data + ad_personalization
5. Floodlight tags: require ad_storage + ad_user_data

### Step 5: Verify Implementation
1. Use Google Tag Assistant to verify consent default fires first
2. Check Tag Assistant timeline shows correct consent state per tag
3. Verify GA4 DebugView shows consent badges on events
4. Monitor network requests for gcs parameter (consent state encoding)
5. Check that cookies are only set when consent is granted

### Step 6: Monitor Modeling Readiness
1. Check GA4 property for behavioral modeling eligibility
2. Verify daily consented user count exceeds 1,000
3. Check conversion actions for modeling eligibility (70+ daily conversions)
4. Wait 7+ days after implementation for modeling to activate

## Debugging Workflow

1. Open Google Tag Assistant in Chrome
2. Navigate to the site and observe consent flow
3. Check "Consent" tab in Tag Assistant for each tag
4. Verify default consent state matches configuration
5. Interact with CMP and verify consent update event appears
6. Confirm tag firing/blocking aligns with consent state
7. Check GA4 DebugView for consent-aware event processing
8. Monitor Chrome DevTools Network tab for gcs parameter in analytics requests
