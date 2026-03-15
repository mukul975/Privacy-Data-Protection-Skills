# CNIL Cookie Banner Implementation Workflow

## Banner Design and Approval Workflow

### Step 1: Draft Banner Content
1. Write banner text in plain French (and English if applicable)
2. Ensure text explains: what cookies are used, for what purposes, who the third-party partners are
3. Draft Layer 1 (initial banner) and Layer 2 (preference detail) content
4. Include equal-prominence Accept All and Reject All buttons

### Step 2: Legal Review
1. DPO reviews banner text for CNIL compliance
2. Verify all third-party vendors are listed by name in Layer 2
3. Confirm cookie categories match actual cookie inventory
4. Verify no dark patterns (asymmetric buttons, guilt language, confusing toggles)
5. Check WCAG 2.1 Level AA accessibility compliance

### Step 3: Design Review
1. UI team implements banner with equal visual weight for Accept/Reject
2. Verify button sizes, colors, and fonts are identical for Accept and Reject
3. Test responsive design on mobile, tablet, and desktop
4. Confirm banner does not obscure essential page content
5. Test focus trap and keyboard navigation

### Step 4: Technical Implementation
1. Banner script loads synchronously before any tags
2. Default consent state: all non-essential denied
3. Tag manager configured to respect consent state
4. Consent cookie set on user interaction
5. Server-side consent validation implemented

### Step 5: Testing
1. Run automated consent tests (see cookie-consent-testing skill)
2. Verify no cookies set before consent
3. Verify Accept All enables all categories
4. Verify Reject All blocks all non-essential categories
5. Test granular preference toggles
6. Verify consent persists across page navigations
7. Verify consent expires after 6 months

### Step 6: Deployment
1. Deploy to staging environment
2. Full QA pass on staging
3. Deploy to production
4. Monitor consent rates and error rates for first 7 days

## Reconsent Cycle Workflow (Every 6 Months)

### Preparation (2 weeks before)
1. Review cookie inventory — have any new cookies been added?
2. Update banner text if cookie categories or vendors changed
3. Test updated banner on staging

### Execution (Reconsent day)
1. Expire existing consent cookies (set Max-Age to 0)
2. Banner re-appears for all users on next visit
3. Users make new consent choices
4. New consent timestamp stored

### Post-Reconsent Monitoring
1. Monitor consent rates for 7 days
2. Compare consent rates with previous cycle
3. Investigate any significant drop in consent rates
4. Report reconsent metrics to DPO

## Cookie Policy Update Workflow

1. Cookie inventory changes trigger policy review
2. DPO approves updated cookie policy text
3. Update cookie policy page with new version number and date
4. If material change: trigger reconsent (new banner version)
5. Archive previous policy version
