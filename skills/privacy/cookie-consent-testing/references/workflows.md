# Cookie Consent Testing Workflows

## Test Development Workflow

### Step 1: Define Test Cases
1. Map each regulatory requirement to one or more test cases
2. Prioritize: pre-consent blocking and reject-all behavior are critical
3. Define selectors for banner elements (data-testid attributes recommended)
4. Define known cookie baselines for regression detection

### Step 2: Implement Tests
1. Set up Playwright or Selenium test project
2. Configure multi-browser testing (Chrome, Firefox, Safari)
3. Implement each test case with clear assertions
4. Add screenshot capture on failure for debugging
5. Implement network request monitoring for tag firing audit

### Step 3: Configure CI/CD
1. Add test execution to CI/CD pipeline
2. Run on every push to staging and main branches
3. Schedule weekly full regression run
4. Configure Slack/email notification on failure
5. Store test artifacts (reports, screenshots, traces)

## Test Execution Workflow

### On Every Deployment
1. Run pre-consent blocking tests (no cookies before interaction)
2. Run banner display tests (visibility, button presence)
3. Run reject-all tests (non-essential cookies blocked)
4. Run cookie regression tests (no unknown cookies)
5. Run GPC signal tests (automatic opt-out)
6. Report results: pass/fail with details

### Weekly Regression
1. Run all deployment tests
2. Run consent persistence tests (state survives navigation)
3. Run consent withdrawal tests (cookies removed on withdrawal)
4. Run accessibility tests (keyboard navigation, ARIA labels)
5. Generate compliance report for DPO review

### Monthly Compliance Audit
1. Run all tests including consent expiry simulation
2. Compare results with previous month
3. Document any new cookies or behavior changes
4. Update cookie baseline if new cookies were intentionally added
5. File compliance report

## Test Failure Response
1. Identify failing test and extract failure details
2. Determine if failure is a true compliance issue or test environment issue
3. If compliance issue: create bug report with high priority
4. Block deployment until pre-consent and reject-all tests pass
5. Fix issue and re-run tests
6. Document incident for compliance records
