# GPC Cookie Integration Workflows

## GPC Detection and Response Workflow

### Step 1: Detect GPC Signal
1. Server-side: Check for Sec-GPC: 1 HTTP header on every request
2. Client-side: Check navigator.globalPrivacyControl === true on page load
3. Both detection methods should be implemented for reliability

### Step 2: Determine User Jurisdiction
1. Resolve user's location via IP geolocation
2. Check if user is in a GPC-mandatory state (CA, CO, CT, MT, TX, OR, DE, NH, NJ)
3. If in mandatory state: GPC is legally binding
4. If in other location: honor GPC as privacy preference (best practice)

### Step 3: Apply GPC Opt-Out
1. Update consent state: ad_storage=denied, ad_user_data=denied, ad_personalization=denied
2. Block advertising cookies and tags
3. Remove any existing advertising cookies
4. Do NOT block analytics (GPC does not cover first-party analytics)
5. Display modified banner acknowledging GPC preference

### Step 4: Record GPC Opt-Out
1. Log GPC-triggered opt-out with timestamp and jurisdiction
2. Store opt-out state for the session/user
3. Maintain records for 24 months (CCPA requirement)

### Step 5: Handle Edge Cases
- User previously opted in: GPC overrides (most recent signal governs)
- User in EU: Apply EU consent rules regardless of GPC
- Multiple signals: Apply most restrictive

## CMP Integration Workflow

1. Configure CMP to detect GPC signal
2. Map GPC to relevant consent categories (advertising, sale, sharing)
3. Set applicable regions for GPC enforcement
4. Configure banner behavior when GPC detected
5. Test GPC detection across browsers (Firefox, Brave, DuckDuckGo)
6. Verify advertising cookies are blocked when GPC active
7. Verify analytics continues to function
8. Update privacy policy to disclose GPC handling
