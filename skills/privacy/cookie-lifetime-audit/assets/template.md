# Cookie Lifetime Audit Report Template

## Organization: [Organization Name]
## Audit Date: [YYYY-MM-DD]

---

## Summary

| Metric | Value |
|--------|-------|
| Total cookies | [N] |
| Session cookies | [N] |
| Persistent cookies | [N] |
| Exceeding CNIL 13-month limit | [N] |
| Affected by Safari ITP 7-day cap | [N] |

## Cookies Exceeding CNIL 13-Month Maximum

| Cookie | Domain | Declared Lifetime | CNIL Limit | Action |
|--------|--------|-------------------|------------|--------|
| | | | 395 days | |

## Cookies Affected by Safari ITP

| Cookie | Declared Lifetime | Safari Effective | Set By | Remediation |
|--------|-------------------|-----------------|--------|-------------|
| | | 7 days (JS) | JavaScript | Move to server-side |

## Cookie Policy Accuracy Check

| Cookie | Policy States | Actual Duration | Accurate | Action |
|--------|--------------|-----------------|----------|--------|
| | | | [ ] Yes / [ ] No | |

## Remediation Plan

### Immediate
1. [Override GA4 cookie_expires to 34128000 (395 days)]

### Short-Term
1. [Implement server-side tagging for cookies affected by ITP]

### Ongoing
1. [Add cookie lifetime checks to CI/CD pipeline]

---

**Audited by**: [Name] | **Approved by**: [DPO Name] | **Date**: [YYYY-MM-DD]
