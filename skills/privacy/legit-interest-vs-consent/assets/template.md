# Legitimate Interest Assessment (LIA) Report

## Processing Activity

| Field | Value |
|-------|-------|
| **Activity** | Fraud detection on account creation |
| **Controller** | CloudVault SaaS Inc. |
| **Date** | 2026-03-14 |
| **Assessor** | Marta Kowalski, DPO |
| **Data Subjects** | New account registrants |
| **Data Categories** | IP address, email domain, registration velocity, device fingerprint (hashed) |

## Part 1: Purpose Test

**Stated Interest:** CloudVault SaaS Inc. has a legitimate interest in detecting and preventing fraudulent account creation to protect the integrity of the service, prevent abuse of free storage tiers, and protect legitimate users from security threats arising from bot-created accounts.

| Criterion | Assessment |
|-----------|-----------|
| Interest is lawful | YES — fraud prevention is recognized as a legitimate interest per Recital 47 |
| Interest is real and present | YES — CloudVault detected 12,000 fraudulent account attempts in Q4 2025 |
| Interest is clearly articulated | YES — specific threat and protection mechanism described |

**Result: PASS**

## Part 2: Necessity Test

| Question | Answer |
|----------|--------|
| Is processing necessary for the stated interest? | YES — automated pattern detection is the only feasible method at scale |
| Could the interest be achieved with less data? | Partially — IP and velocity are minimum; device fingerprint adds accuracy |
| Is there a less intrusive alternative? | CAPTCHA reduces but does not eliminate fraud; combination is necessary |
| Is the processing proportionate? | YES — hashed device fingerprint minimizes privacy impact |

**Result: PASS**

## Part 3: Balancing Test

| Factor | Assessment | Weight |
|--------|-----------|--------|
| Data sensitivity | Low — no special categories | Favors controller |
| Reasonable expectation | Users expect fraud prevention on registration | Favors controller |
| Existing relationship | New registrants (no prior relationship) | Neutral |
| Impact on data subject | Minimal — legitimate users unaffected; flagged users asked to verify | Favors controller |
| Safeguards | Device fingerprint hashed, retention limited to 30 days, access restricted | Favors controller |
| Vulnerable groups | Registration age-gated; children not expected | Neutral |
| Data volume | Minimal — 4 data points per registration | Favors controller |

**Balance: Controller interest outweighs data subject rights**

**Result: PASS**

## Conclusion

| Item | Determination |
|------|--------------|
| Lawful basis | Legitimate interest (Article 6(1)(f)) |
| Purpose test | PASS |
| Necessity test | PASS |
| Balancing test | PASS |
| Opt-out mechanism | Art. 21 objection right available; however, fraud detection may override per Art. 21(1) compelling legitimate grounds |
| Privacy notice updated | YES — Art. 13(1)(d) legitimate interest disclosure included |
| Review schedule | Annual (next review: 2027-03-14) |

## Sign-Off

| Role | Name | Date |
|------|------|------|
| DPO | Marta Kowalski | 2026-03-14 |
| Head of Security | Patrick O'Connor | 2026-03-14 |
| Legal Counsel | Elena Rodriguez | 2026-03-14 |
