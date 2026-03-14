# Cookie-less Alternatives Evaluation Template

## Organization: [Organization Name]
## Evaluation Date: [YYYY-MM-DD]

---

## Current Cookie Dependencies

| Functionality | Current Cookie Solution | Alternative | Cross-Browser |
|--------------|----------------------|-------------|---------------|
| Web analytics | GA4 (_ga, _gid) | [ ] Plausible / [ ] Fathom / [ ] Matomo | [ ] Yes |
| Conversion tracking | Google Ads cookies | Attribution Reporting API | [ ] Chrome only |
| Remarketing | _fbp, _gcl_au | Protected Audiences API | [ ] Chrome only |
| Interest targeting | Third-party cookies | Topics API | [ ] Chrome only |
| A/B testing | Experiment cookies | [ ] Server-side / [ ] Shared Storage | [ ] Yes / Chrome |

## Migration Priority

| Priority | Functionality | Target Solution | Timeline |
|----------|--------------|-----------------|----------|
| High | Web analytics | Plausible + GA4 Consent Mode | |
| Medium | Conversion tracking | Attribution Reporting API | |
| Medium | Remarketing | Protected Audiences API | |
| Low | Interest targeting | Topics API | |

---

**Evaluated by**: [Name] | **Date**: [YYYY-MM-DD]
