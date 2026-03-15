# Cookie Lifetime Audit Workflows

## Quarterly Lifetime Audit

### Step 1: Extract Current Lifetimes
1. Run cookie scanner to capture all cookies with their Max-Age/Expires values
2. Calculate actual lifetime in days for each cookie
3. Record whether cookie is session or persistent
4. Note whether cookie is refreshed on each visit (rolling lifetime)

### Step 2: Compare Against Regulatory Limits
1. Check each persistent cookie against CNIL 13-month (395-day) maximum
2. Flag any cookie exceeding this threshold
3. Note cookies at the borderline (12-13 months)

### Step 3: Compare Against Browser Limits
1. For each JavaScript-set cookie, note effective Safari ITP lifetime (7 days)
2. Identify cookies where declared lifetime exceeds effective browser lifetime
3. Recommend server-side setting for cookies where longer lifetime is justified

### Step 4: Verify Policy Accuracy
1. Compare actual cookie lifetimes with durations stated in cookie policy
2. Flag any discrepancies (policy says "1 year" but cookie is set for 2 years)
3. Update cookie policy text to reflect actual durations

### Step 5: Generate Remediation Plan
1. List all cookies exceeding CNIL 13-month limit
2. Provide specific configuration changes (e.g., GA4 cookie_expires parameter)
3. Recommend server-side tagging for cookies affected by Safari ITP
4. Set timeline for implementing changes

## New Cookie Lifetime Review
1. When a new cookie is added, review its lifetime before deployment
2. Ensure lifetime does not exceed 13 months (CNIL recommendation)
3. Ensure lifetime is accurately documented in cookie policy
4. Verify consent banner reflects the correct duration disclosure
