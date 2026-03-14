# Cookie Audit Workflows

## Quarterly Cookie Audit Workflow

### Phase 1: Scope Definition (Day 1)

1. Confirm domains and subdomains in scope
2. Identify new pages or features deployed since last audit
3. Review any new third-party integrations added
4. Update the scanning configuration to include new URLs

### Phase 2: Automated Scanning (Days 2-3)

1. Run headless browser crawl across all in-scope pages
2. Capture all cookies (first-party and third-party), localStorage, sessionStorage
3. Monitor network requests for tracking pixels, beacons, and server-to-server calls
4. Run authenticated scan (logged-in user flow: login, browse, add to cart, checkout)
5. Run unauthenticated scan (anonymous visitor flow)
6. Export results to structured format (CSV or JSON)

### Phase 3: Classification and Analysis (Days 4-5)

1. Compare scanned cookies against previous audit baseline
2. Identify new cookies not in the previous inventory
3. Classify each new cookie into ICC categories (strictly necessary, performance, functionality, targeting)
4. For each cookie, document: name, domain, path, duration, purpose, category, legal basis
5. Flag cookies exceeding CNIL 13-month lifetime recommendation
6. Identify any pre-consent cookie setting violations

### Phase 4: Gap Analysis (Day 6)

1. Apply Planet49 compliance checklist to each cookie category
2. Verify cookie policy accurately describes all cookies found
3. Check consent banner discloses all third-party partners
4. Verify withdrawal mechanism functions correctly
5. Test consent state propagation to downstream systems

### Phase 5: Reporting and Remediation (Days 7-8)

1. Generate executive summary with key findings
2. Create detailed cookie inventory spreadsheet
3. Document compliance gaps with severity ratings
4. Draft remediation recommendations with timelines
5. Present findings to DPO and development team
6. Track remediation items in the compliance issue tracker

## New Feature Deployment Cookie Check Workflow

### Pre-Deployment (CI/CD Pipeline)

1. Run automated cookie scanner on staging environment
2. Compare cookies found against approved cookie baseline
3. If new cookies detected:
   - Flag deployment for privacy review
   - Require cookie documentation (name, purpose, category, duration)
   - Require cookie policy update if new category or third-party
   - Require consent banner update if new category or vendor
4. If no new cookies: approve deployment

### Post-Deployment Verification

1. Run production cookie scan within 24 hours of deployment
2. Verify no unexpected cookies appeared
3. Confirm consent banner correctly blocks new cookies before consent
4. Verify cookie policy was updated if required

## Third-Party Script Update Monitoring

1. Monitor third-party script versions (tag management audit)
2. When a third-party script updates (e.g., Google Analytics SDK, Meta Pixel):
   - Re-scan to check for new cookies introduced by the update
   - Verify existing cookie behavior unchanged
   - Update cookie inventory if new cookies found
   - Notify privacy team of any material changes
