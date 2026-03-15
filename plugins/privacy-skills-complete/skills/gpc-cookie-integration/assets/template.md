# GPC Cookie Integration Template

## Organization: [Organization Name]
## Implementation Date: [YYYY-MM-DD]

---

## GPC Signal Handling Configuration

| Setting | Value |
|---------|-------|
| GPC detection method | [ ] Server-side (Sec-GPC header) / [ ] Client-side (navigator.globalPrivacyControl) / [ ] Both |
| Mandatory states | CA, CO, CT, MT, TX, OR, DE, NH, NJ |
| GPC triggers opt-out of | Sale, sharing, targeted advertising |
| Analytics affected by GPC | No (GPC does not cover first-party analytics) |

## Consent Mode Mapping

| GPC State | ad_storage | ad_user_data | ad_personalization | analytics_storage |
|-----------|-----------|--------------|-------------------|-------------------|
| GPC detected (mandatory state) | denied | denied | denied | unchanged |
| GPC detected (non-mandatory state) | recommended: denied | recommended: denied | recommended: denied | unchanged |
| No GPC | per CMP | per CMP | per CMP | per CMP |

## CMP Integration

| CMP Platform | GPC Setting | Regions | Status |
|-------------|-------------|---------|--------|
| [Platform] | Honor GPC: [ ] Enabled | [States] | [ ] Configured |

## Privacy Policy Disclosure

Required language:
> "We recognize the Global Privacy Control (GPC) signal. When we detect GPC from users in [applicable states], we treat it as a valid opt-out of the sale and sharing of personal information."

[ ] Added to privacy policy

## Testing

| Test | Browser | Status |
|------|---------|--------|
| GPC header detected | Firefox | [ ] Pass |
| GPC header detected | Brave | [ ] Pass |
| GPC header detected | DuckDuckGo | [ ] Pass |
| Ad cookies blocked | All GPC browsers | [ ] Pass |
| Analytics unaffected | All GPC browsers | [ ] Pass |
| Opt-out logged | Server | [ ] Pass |

---

**Implemented by**: [Name] | **Reviewed by**: [DPO] | **Date**: [YYYY-MM-DD]
