---
name: cookie-consent-testing
description: >-
  Automated cookie consent validation using Selenium and Playwright. Covers banner
  interaction testing, consent state verification, tag firing audit after consent
  choices, regression testing for cookie compliance, and CI/CD pipeline integration.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: cookie-consent-compliance
  tags: "cookie-testing, selenium, playwright, consent-validation, regression-testing"
---

# Automated Cookie Consent Validation

## Overview

Manual cookie consent testing is insufficient for modern web applications where deployments occur multiple times daily and third-party scripts update independently. Automated testing using browser automation frameworks — Selenium and Playwright — enables continuous verification that the cookie consent banner functions correctly, that non-essential cookies are blocked before consent, that consent choices are respected, and that tag firing aligns with the user's consent state. Integrating these tests into the CI/CD pipeline ensures that every deployment is verified for cookie compliance before reaching production.

## Test Architecture

### Test Categories

| Category | What It Tests | When to Run |
|----------|--------------|-------------|
| Banner display | Banner appears on first visit; correct layout and text | Every deployment |
| Pre-consent blocking | No non-essential cookies/tags before user interaction | Every deployment |
| Consent acceptance | Accept All sets correct cookies and fires correct tags | Every deployment |
| Consent rejection | Reject All blocks all non-essential cookies and tags | Every deployment |
| Granular consent | Per-category toggles work correctly | Every deployment |
| Consent persistence | Consent state survives page navigation and browser restart | Daily |
| Consent withdrawal | Changing consent removes cookies and stops tags | Weekly |
| Consent expiry | Banner re-appears after consent expires | Monthly |
| GPC signal | GPC header triggers automatic opt-out | Every deployment |
| Regression | New cookies not introduced without documentation | Every deployment |

### Test Environment Setup

**Playwright Configuration for Pinnacle E-Commerce Ltd:**

```javascript
// playwright.config.js
const { defineConfig, devices } = require('@playwright/test');

module.exports = defineConfig({
  testDir: './tests/cookie-consent',
  timeout: 30000,
  retries: 1,
  use: {
    baseURL: 'https://staging.pinnacle-ecommerce.com',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
    {
      name: 'mobile-chrome',
      use: { ...devices['Pixel 5'] },
    },
    {
      name: 'mobile-safari',
      use: { ...devices['iPhone 13'] },
    },
  ],
});
```

## Test Implementations

### Test 1: Pre-Consent Cookie Blocking

Verify that no non-essential cookies are set before the user interacts with the consent banner.

```javascript
// tests/cookie-consent/pre-consent-blocking.spec.js
const { test, expect } = require('@playwright/test');

const ESSENTIAL_COOKIES = [
  'session_id',
  'csrf_token',
  'consent_state',
  'load_balancer',
  'pinnacle_consent_eu',
  'pinnacle_consent_uk',
  'pinnacle_consent_ccpa',
];

const NON_ESSENTIAL_COOKIES = [
  '_ga',
  '_ga_',
  '_gid',
  '_fbp',
  '_fbc',
  '_gcl_au',
  '_hjSession',
  '_hjSessionUser',
  'IDE',
  'fr',
  'NID',
];

test.describe('Pre-Consent Cookie Blocking', () => {
  test('no non-essential cookies are set on page load before consent', async ({ page }) => {
    // Navigate to homepage without any prior consent
    await page.goto('/');

    // Wait for page to fully load including all third-party scripts
    await page.waitForLoadState('networkidle');

    // Get all cookies
    const cookies = await page.context().cookies();
    const cookieNames = cookies.map(c => c.name);

    // Verify no non-essential cookies exist
    for (const nonEssential of NON_ESSENTIAL_COOKIES) {
      const found = cookieNames.filter(name => name.startsWith(nonEssential));
      expect(found, `Non-essential cookie ${nonEssential} found before consent`).toHaveLength(0);
    }
  });

  test('no analytics network requests before consent', async ({ page }) => {
    const analyticsRequests = [];

    // Monitor network requests
    page.on('request', request => {
      const url = request.url();
      if (
        url.includes('google-analytics.com') ||
        url.includes('analytics.google.com') ||
        url.includes('facebook.com/tr') ||
        url.includes('connect.facebook.net') ||
        url.includes('hotjar.com')
      ) {
        analyticsRequests.push(url);
      }
    });

    await page.goto('/');
    await page.waitForLoadState('networkidle');

    expect(analyticsRequests, 'Analytics requests fired before consent').toHaveLength(0);
  });

  test('no localStorage tracking entries before consent', async ({ page }) => {
    await page.goto('/');
    await page.waitForLoadState('networkidle');

    const trackingKeys = await page.evaluate(() => {
      const suspicious = [];
      for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        if (key.startsWith('_hj') || key.startsWith('_ga') || key.includes('fb_')) {
          suspicious.push(key);
        }
      }
      return suspicious;
    });

    expect(trackingKeys, 'Tracking localStorage entries found before consent').toHaveLength(0);
  });
});
```

### Test 2: Banner Display and Interaction

```javascript
// tests/cookie-consent/banner-display.spec.js
const { test, expect } = require('@playwright/test');

test.describe('Cookie Banner Display', () => {
  test('banner appears on first visit', async ({ page }) => {
    await page.goto('/');

    // Banner should be visible
    const banner = page.locator('[data-testid="cookie-banner"]');
    await expect(banner).toBeVisible();
  });

  test('banner has Accept All button', async ({ page }) => {
    await page.goto('/');
    const acceptButton = page.locator('[data-testid="cookie-accept-all"]');
    await expect(acceptButton).toBeVisible();
    await expect(acceptButton).toHaveText(/Accept All/i);
  });

  test('banner has Reject All button with equal prominence', async ({ page }) => {
    await page.goto('/');
    const acceptButton = page.locator('[data-testid="cookie-accept-all"]');
    const rejectButton = page.locator('[data-testid="cookie-reject-all"]');

    await expect(rejectButton).toBeVisible();
    await expect(rejectButton).toHaveText(/Reject All/i);

    // Verify equal visual prominence (same size)
    const acceptBox = await acceptButton.boundingBox();
    const rejectBox = await rejectButton.boundingBox();

    expect(Math.abs(acceptBox.width - rejectBox.width)).toBeLessThan(10);
    expect(Math.abs(acceptBox.height - rejectBox.height)).toBeLessThan(5);
  });

  test('banner has Customise/Manage Preferences option', async ({ page }) => {
    await page.goto('/');
    const customiseButton = page.locator('[data-testid="cookie-customise"]');
    await expect(customiseButton).toBeVisible();
  });

  test('banner does not reappear after making a choice', async ({ page }) => {
    await page.goto('/');
    await page.locator('[data-testid="cookie-accept-all"]').click();

    // Navigate to another page
    await page.goto('/products');
    await page.waitForLoadState('networkidle');

    const banner = page.locator('[data-testid="cookie-banner"]');
    await expect(banner).not.toBeVisible();
  });

  test('banner is keyboard accessible', async ({ page }) => {
    await page.goto('/');
    await page.keyboard.press('Tab');

    // Focus should be within the banner
    const focusedElement = await page.evaluate(() => {
      const el = document.activeElement;
      return el ? el.closest('[data-testid="cookie-banner"]') !== null : false;
    });
    expect(focusedElement).toBe(true);
  });
});
```

### Test 3: Consent State Verification

```javascript
// tests/cookie-consent/consent-state.spec.js
const { test, expect } = require('@playwright/test');

test.describe('Consent State Verification', () => {
  test('Accept All sets all consent categories to granted', async ({ page }) => {
    await page.goto('/');
    await page.locator('[data-testid="cookie-accept-all"]').click();
    await page.waitForLoadState('networkidle');

    const cookies = await page.context().cookies();
    const consentCookie = cookies.find(c => c.name === 'pinnacle_consent_eu');

    expect(consentCookie).toBeTruthy();
    const consentState = JSON.parse(decodeURIComponent(consentCookie.value));
    expect(consentState.analytics).toBe(true);
    expect(consentState.advertising).toBe(true);
    expect(consentState.functionality).toBe(true);
  });

  test('Reject All sets all consent categories to denied', async ({ page }) => {
    await page.goto('/');
    await page.locator('[data-testid="cookie-reject-all"]').click();
    await page.waitForLoadState('networkidle');

    const cookies = await page.context().cookies();
    const consentCookie = cookies.find(c => c.name === 'pinnacle_consent_eu');

    expect(consentCookie).toBeTruthy();
    const consentState = JSON.parse(decodeURIComponent(consentCookie.value));
    expect(consentState.analytics).toBe(false);
    expect(consentState.advertising).toBe(false);
    expect(consentState.functionality).toBe(false);
  });

  test('Reject All blocks GA4 cookies', async ({ page }) => {
    await page.goto('/');
    await page.locator('[data-testid="cookie-reject-all"]').click();
    await page.waitForLoadState('networkidle');

    // Navigate to multiple pages to give GA4 time to attempt cookie setting
    await page.goto('/products');
    await page.waitForLoadState('networkidle');
    await page.goto('/about');
    await page.waitForLoadState('networkidle');

    const cookies = await page.context().cookies();
    const gaCookies = cookies.filter(c => c.name.startsWith('_ga'));
    expect(gaCookies).toHaveLength(0);
  });

  test('Granular consent: analytics only sets only analytics cookies', async ({ page }) => {
    await page.goto('/');

    // Open customisation layer
    await page.locator('[data-testid="cookie-customise"]').click();

    // Enable only analytics
    const analyticsToggle = page.locator('[data-testid="consent-toggle-analytics"]');
    await analyticsToggle.click();

    // Ensure advertising is off
    const advertisingToggle = page.locator('[data-testid="consent-toggle-advertising"]');
    const isAdvertisingChecked = await advertisingToggle.isChecked();
    expect(isAdvertisingChecked).toBe(false);

    // Confirm choices
    await page.locator('[data-testid="cookie-confirm-choices"]').click();
    await page.waitForLoadState('networkidle');

    const cookies = await page.context().cookies();
    const cookieNames = cookies.map(c => c.name);

    // GA cookies should be present
    expect(cookieNames.some(n => n.startsWith('_ga'))).toBe(true);

    // Advertising cookies should NOT be present
    expect(cookieNames.some(n => n === '_fbp')).toBe(false);
    expect(cookieNames.some(n => n === '_gcl_au')).toBe(false);
  });
});
```

### Test 4: Tag Firing Audit

```javascript
// tests/cookie-consent/tag-firing.spec.js
const { test, expect } = require('@playwright/test');

test.describe('Tag Firing Audit', () => {
  test('GA4 tag fires only after analytics consent', async ({ page }) => {
    let ga4Fired = false;

    page.on('request', request => {
      if (request.url().includes('google-analytics.com/g/collect') ||
          request.url().includes('analytics.google.com/g/collect')) {
        ga4Fired = true;
      }
    });

    // Load page — GA4 should not fire
    await page.goto('/');
    await page.waitForLoadState('networkidle');
    expect(ga4Fired, 'GA4 fired before consent').toBe(false);

    // Accept analytics
    await page.locator('[data-testid="cookie-customise"]').click();
    await page.locator('[data-testid="consent-toggle-analytics"]').click();
    await page.locator('[data-testid="cookie-confirm-choices"]').click();
    await page.waitForLoadState('networkidle');

    // Navigate to trigger a pageview
    await page.goto('/products');
    await page.waitForLoadState('networkidle');
    expect(ga4Fired, 'GA4 did not fire after analytics consent').toBe(true);
  });

  test('Meta Pixel does not fire when advertising is rejected', async ({ page }) => {
    let metaPixelFired = false;

    page.on('request', request => {
      if (request.url().includes('facebook.com/tr') ||
          request.url().includes('connect.facebook.net')) {
        metaPixelFired = true;
      }
    });

    await page.goto('/');
    await page.locator('[data-testid="cookie-reject-all"]').click();
    await page.waitForLoadState('networkidle');

    await page.goto('/products');
    await page.waitForLoadState('networkidle');
    await page.goto('/products/widget-pro');
    await page.waitForLoadState('networkidle');

    expect(metaPixelFired, 'Meta Pixel fired after reject all').toBe(false);
  });

  test('Google Consent Mode sends correct consent state', async ({ page }) => {
    const consentPings = [];

    page.on('request', request => {
      const url = request.url();
      if (url.includes('google-analytics.com') && url.includes('gcs=')) {
        const gcsMatch = url.match(/gcs=([^&]+)/);
        if (gcsMatch) consentPings.push(gcsMatch[1]);
      }
    });

    await page.goto('/');
    await page.locator('[data-testid="cookie-reject-all"]').click();
    await page.waitForLoadState('networkidle');

    // Navigate to trigger consent mode ping
    await page.goto('/products');
    await page.waitForLoadState('networkidle');

    // If consent mode pings are sent, verify denied state
    if (consentPings.length > 0) {
      for (const gcs of consentPings) {
        // G100 = all denied, G111 = all granted
        expect(gcs).toContain('100');
      }
    }
  });
});
```

### Test 5: Cookie Regression Detection

```javascript
// tests/cookie-consent/regression.spec.js
const { test, expect } = require('@playwright/test');
const fs = require('fs');

// Baseline of known cookies — update when new cookies are intentionally added
const KNOWN_COOKIES = new Set([
  'session_id',
  'csrf_token',
  'consent_state',
  'pinnacle_consent_eu',
  'load_balancer',
  '_ga',
  '_ga_PINNACLE',
  '_gid',
  '_fbp',
  '_fbc',
  '_gcl_au',
  '_hjSessionUser',
  '_hjSession',
  'locale',
  'currency',
  'recently_viewed',
  'cart_session',
  'auth_token',
]);

test.describe('Cookie Regression Detection', () => {
  test('no unknown cookies after Accept All', async ({ page }) => {
    await page.goto('/');
    await page.locator('[data-testid="cookie-accept-all"]').click();
    await page.waitForLoadState('networkidle');

    // Visit several pages to trigger all tag scenarios
    const pages = ['/', '/products', '/products/widget-pro', '/cart', '/about', '/blog'];
    for (const path of pages) {
      await page.goto(path);
      await page.waitForLoadState('networkidle');
    }

    const cookies = await page.context().cookies();
    const unknownCookies = cookies.filter(c => {
      // Check if cookie name matches any known prefix
      return !Array.from(KNOWN_COOKIES).some(known =>
        c.name === known || c.name.startsWith(known)
      );
    });

    if (unknownCookies.length > 0) {
      const unknownNames = unknownCookies.map(c => `${c.name} (domain: ${c.domain}, expires: ${c.expires})`);
      console.error('Unknown cookies detected:', unknownNames);

      // Write to report file for review
      fs.writeFileSync(
        'test-results/unknown-cookies.json',
        JSON.stringify(unknownCookies, null, 2)
      );
    }

    expect(unknownCookies, `Unknown cookies found: ${unknownCookies.map(c => c.name).join(', ')}`).toHaveLength(0);
  });
});
```

### Test 6: GPC Signal Handling

```javascript
// tests/cookie-consent/gpc-signal.spec.js
const { test, expect } = require('@playwright/test');

test.describe('Global Privacy Control Signal', () => {
  test('GPC signal triggers automatic opt-out for California users', async ({ browser }) => {
    // Create context with GPC header
    const context = await browser.newContext({
      extraHTTPHeaders: {
        'Sec-GPC': '1',
      },
      locale: 'en-US',
      geolocation: { latitude: 34.0522, longitude: -118.2437 }, // Los Angeles
      permissions: ['geolocation'],
    });

    const page = await context.newPage();
    await page.goto('/');
    await page.waitForLoadState('networkidle');

    // Verify advertising cookies are not set
    const cookies = await context.cookies();
    const adCookies = cookies.filter(c =>
      c.name === '_fbp' || c.name === '_gcl_au' || c.name.startsWith('IDE')
    );

    expect(adCookies, 'Advertising cookies set despite GPC signal').toHaveLength(0);

    await context.close();
  });
});
```

## CI/CD Pipeline Integration

### GitHub Actions Workflow

```yaml
name: Cookie Consent Compliance Tests
on:
  push:
    branches: [main, staging]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 6 * * 1'  # Weekly Monday 6 AM UTC

jobs:
  cookie-consent-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm ci

      - name: Install Playwright browsers
        run: npx playwright install --with-deps

      - name: Run cookie consent tests
        run: npx playwright test tests/cookie-consent/
        env:
          BASE_URL: ${{ vars.STAGING_URL }}

      - name: Upload test results
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: cookie-consent-test-results
          path: |
            test-results/
            playwright-report/

      - name: Post results to Slack
        if: failure()
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "Cookie consent tests FAILED on ${{ github.ref }}. Review: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}"
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_PRIVACY_WEBHOOK }}
```

## Key Legal and Technical References

- **ePrivacy Directive 2002/58/EC, Article 5(3)** — Legal requirement that automated tests verify
- **CJEU Case C-673/17 (Planet49)** — Active consent requirements validated by banner interaction tests
- **CNIL Deliberation No. 2020-091** — Equal prominence requirement tested by button size comparison
- **CCPA/CPRA Cal. Civ. Code §1798.135(e)** — GPC signal handling tested in GPC test suite
- **Playwright Documentation** — Browser automation framework for cross-browser testing
- **WCAG 2.1 Level AA** — Accessibility requirements tested by keyboard navigation tests
- **Google Consent Mode Documentation** — Consent state parameters validated in tag firing tests
