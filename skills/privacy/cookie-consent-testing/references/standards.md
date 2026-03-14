# Cookie Consent Testing Standards and References

## Legal Requirements Being Tested

### ePrivacy Directive 2002/58/EC, Article 5(3)
- Tests verify: no non-essential cookies set before user consent

### CJEU Case C-673/17 (Planet49)
- Tests verify: active consent mechanism (not pre-ticked)
- Tests verify: cookie duration and third-party access disclosed

### CNIL Deliberation No. 2020-091
- Tests verify: equal prominence for Accept All and Reject All buttons
- Tests verify: no dark patterns in banner design

### CCPA/CPRA Cal. Civ. Code §1798.135(e)
- Tests verify: GPC signal triggers automatic opt-out

### WCAG 2.1 Level AA
- Tests verify: keyboard navigation, screen reader compatibility, color contrast

## Testing Frameworks

### Playwright
- Microsoft open-source browser automation framework
- Cross-browser: Chromium, Firefox, WebKit
- Built-in network interception and cookie inspection
- Native async/await support
- Excellent for consent testing: headless mode, mobile device emulation

### Selenium WebDriver
- Established browser automation standard
- Wide language support (Python, Java, JavaScript, C#)
- WebDriver protocol standardized by W3C
- Good for cookie inspection and network monitoring

## CI/CD Integration

### GitHub Actions
- Automated test execution on push, pull request, and schedule
- Playwright browsers installable via action
- Test results as artifacts for review
- Slack notification on failure

### Test Reporting
- HTML reports with screenshots on failure
- Trace files for debugging failed tests
- CSV export for compliance audit records
