# Privacy-Preserving Analytics Configuration Template

## Analytics Program Overview

| Item | Value |
|------|-------|
| Organization | Prism Data Systems AG |
| Program Owner | Chief Analytics Officer |
| Privacy Oversight | Data Protection Officer, Dr. Lukas Meier |
| Annual Privacy Budget (ε) | 8.0 |
| Budget Period | 2026-01-01 to 2026-12-31 |
| Minimum Group Size | 11 records |
| Default Delta (δ) | 1e-5 (equivalent to 1/n^2 for n ≈ 316) |

## Budget Allocation Table

| Analytics Function | Epsilon Allocation | Cadence | Mechanism | Sensitivity | Analyst Team |
|-------------------|-------------------|---------|-----------|-------------|-------------|
| Daily active user counts | 1.2 (0.1/day, 120 days) | Daily | Laplace | 1.0 | Platform Analytics |
| Revenue by region | 2.0 (0.5/quarter) | Quarterly | Gaussian | 500.0 CHF | Finance Analytics |
| Feature adoption rates | 3.6 (0.3/month) | Monthly | Laplace | 1.0 | Product Analytics |
| Customer churn prediction | 0.8 (0.2/quarter) | Quarterly | Gaussian | 1.0 | Customer Success |
| A/B experiment results | 0.4 (0.1/experiment) | Per experiment | Laplace | 1.0 | Growth Engineering |
| **Total Allocated** | **8.0** | | | | |

## Budget Exhaustion Protocol

| Utilization Threshold | Action Required | Approver |
|----------------------|-----------------|----------|
| 80% consumed | Alert DPO and analytics leads; review remaining allocations | Automated alert |
| 95% consumed | DPO approval required for each subsequent query | Dr. Lukas Meier (DPO) |
| 100% consumed | All differentially private queries blocked until next period | DPO + CISO joint override only |

## k-Anonymity Configuration

| Dataset Category | Minimum k | Quasi-Identifiers | Generalization Strategy |
|-----------------|-----------|-------------------|------------------------|
| Customer demographics | 5 | age_range, canton, gender | Age: 5-year bands; Canton: region; Gender: suppress if k fails |
| Health-related analytics | 11 | age_range, canton, insurance_type | Age: 10-year bands; Canton: language region; Insurance: category |
| Financial analytics | 7 | income_range, canton, employment_type | Income: CHF 20k bands; Canton: region; Employment: broad category |
| Usage analytics | 5 | subscription_tier, country, device_type | No generalization needed (low dimensionality) |

## Output Validation Rules

| Rule | Threshold | Action on Violation |
|------|-----------|-------------------|
| Minimum group size | < 11 records | Suppress cell value, replace with "< 11" |
| Maximum relative error | > 25% at ε allocation | Flag for review; consider increasing epsilon |
| Outlier contribution | Single record > 10% of aggregate | Clip contribution before noise injection |
| Confidence interval width | > 50% of true value | Report with warning; consider increasing epsilon or sample size |

## Quarterly Review Checklist

- [ ] Review epsilon consumption vs. allocation for each function
- [ ] Assess utility metrics (relative error, confidence interval width)
- [ ] Identify unused or under-utilized budget allocations for rebalancing
- [ ] Review audit logs for unauthorized or anomalous query patterns
- [ ] Update budget allocations based on business priority changes
- [ ] File quarterly privacy budget report with DPO
- [ ] Verify minimum group size enforcement across all published outputs
