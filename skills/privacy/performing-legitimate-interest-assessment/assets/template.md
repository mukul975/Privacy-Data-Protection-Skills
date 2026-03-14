# Legitimate Interest Assessment — Website Analytics

**Organisation**: Nexus Technologies GmbH
**Assessment Date**: 2026-01-15
**Assessor**: Dr. Katharina Weiss, Data Protection Officer
**Processing Activity**: Website visitor analytics using Google Analytics 4
**RoPA Reference**: RPA-034
**LIA Reference**: LIA-2026-GA4-001

---

## Part 1: Purpose Test

### Identified Legitimate Interest

Nexus Technologies GmbH has a legitimate interest in analysing aggregate website visitor behaviour on nexus-tech.eu to understand user journeys, identify navigation issues, measure marketing campaign effectiveness, and optimise the website's conversion funnel. This directly supports the company's commercial viability by ensuring marketing spend is effective and the website serves customers efficiently.

### Legitimacy Assessment

| Criterion | Assessment |
|-----------|-----------|
| Is the interest lawful? | Yes — commercial analytics is not prohibited by any applicable law |
| Is the interest specific? | Yes — analysis of website user behaviour for conversion optimisation and UX improvement |
| Is the interest real and present? | Yes — the website generates 42% of total revenue through e-commerce; ongoing optimisation is commercially essential |
| Is the interest recognised in GDPR? | Partially — Recital 47 recognises reasonable expectations in the context of the relationship; commercial analytics is widely accepted as a legitimate interest by supervisory authorities |

### Purpose Test Outcome: PASS

A specific, lawful, and present legitimate interest has been identified: optimising website performance and marketing effectiveness through visitor behaviour analysis.

---

## Part 2: Necessity Test

### Processing Description

Google Analytics 4 (GA4) is configured to collect: page views, session duration, device type, browser type, referral source, country-level geolocation, and on-site interaction events (button clicks, form submissions, product views). IP addresses are anonymised (last octet truncated) before storage.

### Alternative Analysis

| Alternative | Feasible? | Rationale |
|-------------|-----------|-----------|
| No analytics at all | No | Without any analytics, the company cannot measure website performance, resulting in uninformed business decisions and inability to identify conversion barriers |
| Server log analysis only | Partially | Server logs provide basic page view data but lack interaction events, session tracking, and attribution — insufficient for conversion funnel analysis |
| Fully anonymised/aggregated analytics | Partially | Fully anonymised data lacks session-level analysis needed to understand user journeys; aggregation loses the ability to segment by acquisition channel |
| First-party analytics (Matomo/Plausible) | Yes, but with trade-offs | Could achieve similar results; however, GA4 with IP anonymisation and restricted data sharing already minimises impact. The necessity of the tool is secondary to the necessity of the processing itself |

### Data Minimisation Measures

- IP anonymisation enabled (last octet truncated before storage)
- User-ID feature disabled — no cross-device tracking
- Google Signals disabled — no demographic/interest reporting
- Data sharing with Google disabled (advertising, benchmarking, technical support)
- Data retention set to 2 months (minimum GA4 allows)
- No personally identifiable dimensions configured (no email, name, phone fields in custom dimensions)

### Necessity Test Outcome: PASS

The processing of pseudonymised website interaction data is necessary for the stated interest. Fully anonymised alternatives do not provide sufficient granularity for conversion funnel analysis. Data minimisation measures have been applied to limit processing to the minimum necessary.

---

## Part 3: Balancing Test

### Controller's Interest Strength: MODERATE

Website analytics supports commercial operations (42% of revenue from e-commerce) but is not essential for the organisation's survival. The interest is genuine and significant but not at the level of fraud prevention or security.

### Data Subject Impact Assessment

| Impact Category | Rating | Rationale |
|-----------------|--------|-----------|
| Financial impact | Negligible | No financial consequences for data subjects |
| Emotional/psychological impact | Negligible | Analytics processing is invisible to users and causes no distress |
| Social impact | Negligible | No social consequences; data not shared or made public |
| Loss of control | Minor | Users may be unaware of analytics tracking; however, data is pseudonymised and not used for individual targeting |
| Discrimination risk | Negligible | No profiling or automated decision-making affecting individuals |

### Reasonable Expectations

Website visitors reasonably expect that a commercial website measures traffic and usage patterns. Web analytics is a standard practice on virtually all commercial websites. The privacy notice at nexus-tech.eu/privacy informs visitors about analytics processing, and a cookie banner provides opt-out functionality before analytics scripts load.

### Vulnerability Factors

| Factor | Present? | Detail |
|--------|----------|--------|
| Children's data | No | The website is a B2B/B2C technology products site; the target audience is business professionals and adult consumers |
| Vulnerable persons | No | No specific vulnerability identified in the target audience |
| Sensitive data | No | No special category data collected through analytics |

### Safeguards Implemented

| Safeguard | Detail |
|-----------|--------|
| IP anonymisation | Last octet truncated before processing/storage by GA4 |
| No cross-site tracking | GA4 configured without cross-site linking; no Google Signals |
| Minimal retention | 2-month data retention in GA4 (minimum permitted) |
| EU processing | GA4 data processed in Google's EU data centres (Frankfurt) |
| Cookie consent | GDPR-compliant cookie banner (Cookiebot) with opt-out before analytics loads; analytics cookies categorised as "statistics" and only activated upon affirmative consent |
| Transparency | Full disclosure in privacy notice including purpose, lawful basis, and GA4 as the specific tool |
| Data sharing disabled | All optional Google data sharing features disabled |
| No individual targeting | Analytics data used only for aggregate reporting; no individual user targeting or personalisation |

### Balancing Outcome: PASS

The controller's moderate commercial interest in website optimisation is not overridden by data subjects' rights. The impact on data subjects is negligible to minor, data subjects reasonably expect this processing, no vulnerable groups are affected, and eight specific safeguards are implemented to mitigate any residual impact. The availability of an opt-out mechanism via the cookie banner further strengthens the balance.

---

## Overall LIA Outcome: PASS

Art. 6(1)(f) legitimate interests is the appropriate lawful basis for website analytics processing via Google Analytics 4, subject to:

1. All safeguards listed above remaining in place.
2. The Art. 21 right to object being facilitated through the cookie banner opt-out and the general objection mechanism described in the privacy notice.
3. Annual reassessment of this LIA or upon material change to the analytics configuration.

---

## Art. 21 Right to Object Implementation

| Mechanism | Detail |
|-----------|--------|
| Cookie banner opt-out | Cookiebot banner allows visitors to decline statistics cookies, preventing GA4 from loading |
| Privacy notice | Right to object described at nexus-tech.eu/privacy with link to cookie settings and DPO contact |
| DPO contact | Data subjects can email dpo@nexus-tech.eu to exercise their right to object |
| Response timeline | Objections acknowledged within 48 hours, processed within 30 days |

---

## Approval

| Role | Name | Date | Decision |
|------|------|------|----------|
| DPO | Dr. Katharina Weiss | 2026-01-15 | Approved |
| Processing Owner | Stefan Richter, Head of Digital Marketing | 2026-01-15 | Acknowledged |

**Next Review**: 2027-01-15 or upon material change to analytics configuration.
