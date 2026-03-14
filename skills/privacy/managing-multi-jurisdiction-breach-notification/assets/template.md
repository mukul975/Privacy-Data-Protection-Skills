# Multi-Jurisdiction Breach Notification Tracker

## Breach Reference: SPG-BREACH-2026-003

| Field | Value |
|-------|-------|
| Breach Awareness Date | 13 March 2026, 14:30 UTC |
| Total Data Subjects | 21,725 |
| Jurisdictions Affected | 11 |
| Notification Lead | Dr. Elena Vasquez (DPO) |

## Jurisdiction Notification Status

| Jurisdiction | Law | Affected | Deadline | Authority | Submitted | Reference | Status |
|-------------|-----|----------|----------|-----------|-----------|-----------|--------|
| EU (GDPR) | Art. 33/34 | 12,450 | 16 Mar 14:30 UTC | Berliner BfDI | 15 Mar 10:00 | BLN-DPA-2026-00847 | Complete |
| UK | UK GDPR | 1,830 | 16 Mar 14:30 UTC | ICO | 15 Mar 11:00 | IC-2026-03892 | Complete |
| California | CC §1798.82 | 2,340 | ASAP | CA AG | 25 Mar | CAG-2026-0291 | Complete |
| New York | GBL §899-aa | 1,870 | ASAP | NY AG + DFS + DOS | 25 Mar | NYA-2026-0184 | Complete |
| Texas | BCC §521.053 | 980 | 12 May | TX AG | 25 Mar | TXA-2026-0073 | Complete |
| Florida | Stat. §501.171 | 620 | 12 Apr | FDLE | 25 Mar | FLD-2026-0156 | Complete |
| Colorado | Rev. Stat. §6-1-716 | 340 | 12 Apr | CO AG | 25 Mar | COA-2026-0042 | Complete |
| Canada | PIPEDA | 890 | ASAP | OPC | 20 Mar | OPC-2026-00391 | Complete |
| Australia | NDB Scheme | 210 | 12 Apr | OAIC | 28 Mar | NDB-2026-0087 | Complete |
| Brazil | LGPD Art. 48 | 150 | 18 Mar | ANPD | 17 Mar | ANPD-2026-0014 | Complete |
| South Korea | PIPA Art. 34 | 45 | 16 Mar 14:30 UTC | PIPC | 15 Mar 14:00 | PIPC-2026-0008 | Complete |

## Data Subject Notification Status

| Jurisdiction | Method | Count | Dispatched | Delivery Rate | Status |
|-------------|--------|-------|------------|---------------|--------|
| EU (18 member states) | Email + Postal | 12,450 | 16-18 Mar | 94.2% | Complete |
| UK | Email + Postal | 1,830 | 16-18 Mar | 95.1% | Complete |
| US (all states) | Email + Postal | 6,150 | 28-30 Mar | 91.8% | Complete |
| Canada | Email + Postal | 890 | 22-24 Mar | 93.4% | Complete |
| Australia | Email + Postal | 210 | 30 Mar | 96.2% | Complete |
| Brazil | Email + Postal | 150 | 20-22 Mar | 89.3% | Complete |
| South Korea | Email + Postal | 45 | 18 Mar | 100% | Complete |

## Credit Monitoring Activation

| Region | Provider | Duration | Enrolled | Enrollment Rate |
|--------|----------|----------|----------|----------------|
| EU/UK | Experian IdentityWorks | 12 months | 9,847 | 68.9% |
| US | Experian IdentityWorks | 12 months | 4,231 | 68.8% |
| Canada | TransUnion | 12 months | 612 | 68.8% |
| Australia | Equifax Protect | 12 months | 145 | 69.0% |

## Regulatory Follow-Up Log

| Date | Authority | Communication | Response Required | Status |
|------|-----------|--------------|-------------------|--------|
| 20 Mar 2026 | Berliner BfDI | Acknowledgment of notification; request for supplementary forensic report | Yes — within 30 days | Submitted 10 Apr |
| 22 Mar 2026 | ICO | Acknowledgment; no further action at this time | No | Closed |
| 5 Apr 2026 | CA AG | Request for details on credit monitoring enrollment rates | Yes — within 14 days | Submitted 15 Apr |
| 12 Apr 2026 | Berliner BfDI | Follow-up: exfiltration determination requested | Yes — within 14 days | Submitted 22 Apr |
| 30 Apr 2026 | OPC (Canada) | Acknowledgment; compliance verification inquiry | Yes — within 30 days | In progress |

## Lessons Learned

1. **Parallel execution worked well**: Running EU, US, and international notification tracks in parallel met all deadlines.
2. **Superset content approach saved time**: Creating one master notification document and adapting for each jurisdiction was more efficient than drafting separately.
3. **State-by-state data subject count was time-consuming**: Automating the geographic mapping of data subjects by billing address should be implemented before the next incident.
4. **Brazilian 3-business-day deadline was tight**: ANPD notification required rapid engagement of local counsel. Pre-negotiated retainer with Brazilian law firm recommended.
