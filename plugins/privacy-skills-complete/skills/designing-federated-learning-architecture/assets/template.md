# Federated Learning Deployment Template

## Consortium Details

| Item | Value |
|------|-------|
| Consortium Coordinator | Prism Data Systems AG |
| ML Task | Diagnostic prediction model for early disease detection |
| Aggregation Strategy | FedProx (mu=0.01) for non-IID hospital data |
| Privacy Mechanisms | Secure aggregation + Differential privacy (DP-FedAvg) |
| Governance | Joint controller agreement under GDPR Article 26 |

## Participants

| Participant | Organization | Data Size | Data Distribution | Lawful Basis | DPO Contact |
|------------|-------------|-----------|-------------------|-------------|-------------|
| hospital-zurich | Universitatsspital Zurich | 5,000 patients | Non-IID (urban demographics) | Art. 6(1)(e) + Art. 9(2)(j) | Dr. Martina Keller |
| hospital-bern | Inselspital Bern | 8,000 patients | Non-IID (mixed demographics) | Art. 6(1)(e) + Art. 9(2)(j) | Prof. Stefan Maurer |
| hospital-basel | Universitatsspital Basel | 3,000 patients | Non-IID (border region demographics) | Art. 6(1)(e) + Art. 9(2)(j) | Dr. Anna Vogel |

## Privacy Configuration

| Parameter | Value | Justification |
|-----------|-------|---------------|
| Target epsilon | 3.0 | Balance between model utility and patient privacy for health data |
| Target delta | 1e-5 | Standard for combined dataset size of 16,000 |
| Gradient clipping norm | 1.0 | Based on gradient magnitude analysis during pilot |
| Noise multiplier | 1.1 | Achieves target epsilon within 500 communication rounds |
| Secure aggregation | Pairwise masking (Bonawitz 2017) | Prevents coordinator from seeing individual hospital updates |
| Privacy accounting | Renyi DP (alpha=5) | Tighter composition bounds than basic composition |

## Training Configuration

| Parameter | Value |
|-----------|-------|
| Model architecture | 3-layer feedforward network (128-64-32 neurons) |
| Local epochs per round | 3 |
| Learning rate | 0.01 |
| Communication rounds | 200 (max 500 within privacy budget) |
| Participation rate | 100% (all hospitals participate each round) |
| Gradient compression | 8-bit quantization |
| Round timeout | 300 seconds |
| Convergence criterion | Validation loss improvement < 0.001 for 10 consecutive rounds |

## DPIA Summary

| DPIA Element | Assessment |
|-------------|------------|
| Processing description | Federated training of diagnostic model across three hospitals using patient health records (Art. 9 special category) |
| Necessity and proportionality | FL is the least privacy-invasive approach for multi-hospital model training; no alternative achieves equivalent model quality without data centralization |
| Risks to data subjects | Gradient inversion (mitigated by secure aggregation + DP), membership inference (mitigated by DP), model inversion (mitigated by DP + access control) |
| Safeguards | Secure aggregation, DP (epsilon=3.0), gradient clipping, access-controlled model deployment, 12-month model sunset |
| DPO opinion | Approved with conditions: quarterly privacy budget review, annual model retraining, immediate halt if gradient inversion detected |

## Monitoring Checklist

- [ ] Per-round loss convergence tracked and visualized
- [ ] Per-participant contribution quality monitored (gradient norms, loss)
- [ ] Privacy budget consumption logged and alerted at 80% threshold
- [ ] Communication latency per participant tracked
- [ ] Model accuracy evaluated on each participant's held-out test set
- [ ] Membership inference attack test run quarterly
- [ ] Joint controller agreement reviewed annually
