# Cross-Jurisdiction Cookie Compliance Template

## Organization: [Organization Name]
## Jurisdictions Served: [List]
## Date: [YYYY-MM-DD]

---

## Jurisdiction Configuration Matrix

| Jurisdiction | Consent Model | Default State | Banner Type | GPC Required | Max Cookie Life | Reconsent |
|-------------|---------------|---------------|-------------|-------------|----------------|-----------|
| EU/EEA | Opt-in | Denied | Equal accept/reject | No (recommended) | 13 months | 6 months |
| UK | Opt-in | Denied | Clear accept/reject | No (recommended) | Not specified | 12 months |
| California | Opt-out | Granted | Notice + DNSS link | Yes | Not specified | 12 months |
| Brazil | Legal basis | Denied (recommended) | Consent banner | No | Not specified | 12 months |

## Per-Jurisdiction Consent Cookie

| Jurisdiction | Cookie Name | Content Format | Duration |
|-------------|-------------|---------------|----------|
| EU | | JSON with per-category decisions | 6 months |
| UK | | JSON with per-category decisions | 12 months |
| US-CA | | JSON with opt-out decisions | 12 months |
| Brazil | | JSON with per-category decisions | 12 months |

## Testing Checklist

| Test | EU | UK | California | Brazil |
|------|----|----|------------|--------|
| Correct banner appears | [ ] | [ ] | [ ] | [ ] |
| Correct default state | [ ] | [ ] | [ ] | [ ] |
| GPC honored | [ ] | [ ] | [ ] | [ ] |
| Consent persists | [ ] | [ ] | [ ] | [ ] |
| Cookie policy accessible | [ ] | [ ] | [ ] | [ ] |

---

**Configured by**: [Name] | **Approved by**: [DPO] | **Date**: [YYYY-MM-DD]
