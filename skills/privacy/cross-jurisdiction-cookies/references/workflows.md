# Cross-Jurisdiction Cookie Implementation Workflow

## Geolocation-Based Consent Routing

### Step 1: User Jurisdiction Detection
1. Primary: IP geolocation (MaxMind GeoIP2 or similar)
2. Secondary: Accept-Language header analysis
3. Tertiary: User account country setting (if logged in)
4. Fallback: Apply most restrictive standard (EU opt-in)

### Step 2: Consent Experience Selection
- EU/EEA users: Full opt-in banner with equal accept/reject
- UK users: Opt-in banner (PECR-compliant)
- California users: Notice with "Do Not Sell or Share" link
- Other US states with privacy laws: Opt-out with universal opt-out support
- Brazil users: Consent banner (LGPD legal basis)
- Other: Apply most restrictive applicable standard

### Step 3: Jurisdiction-Specific Configuration
For each jurisdiction, configure:
- Default cookie state (denied vs. granted)
- Banner type and content
- Consent storage cookie name and format
- Reconsent interval
- GPC signal handling

### Step 4: Testing
Test each jurisdiction configuration with:
- VPN/proxy to simulate user location
- Verify correct banner appears
- Verify correct cookies are set/blocked
- Verify consent state stored correctly
- Verify GPC handled correctly (California, Colorado, Connecticut)

### Step 5: Cookie Policy Localization
- English policy for UK, US, international
- French policy for France (CNIL requirement)
- Portuguese policy for Brazil (LGPD)
- German policy for Germany (recommended)
- Jurisdiction-specific rights sections in each language
