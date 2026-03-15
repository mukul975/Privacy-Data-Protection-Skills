# After-Action Report — Breach Simulation Exercise

## Exercise Summary

| Field | Value |
|-------|-------|
| Exercise Title | Ransomware Attack on Production Database |
| Date | 15 April 2026 |
| Duration | 3 hours (14:00-17:00 CET) |
| Scenario Type | Tabletop — discussion-based |
| Facilitator | External consultant (Deloitte Cyber Risk) |
| Observer | Anna Schmidt, DPO Office Analyst |

## Participants

| Name | Role | Function | Attended |
|------|------|----------|----------|
| Thomas Brenner | Incident Commander | CISO | Yes |
| Dr. Elena Vasquez | Privacy Lead | DPO | Yes |
| Sarah Chen | Legal Counsel | General Counsel | Yes |
| Martin Keller | Communications Lead | Communications Director | Yes |
| Petra Hoffmann | IT Operations | IT Director | Yes |
| Marcus Lindqvist | Executive Sponsor | CEO | Yes |
| James Park | Customer Relations | VP Customer Success | Yes |
| Claudia Richter | HR Lead | CHRO | Yes (observer — not primary role in this scenario) |

## Objectives Assessment

| Objective | Met? | Notes |
|-----------|------|-------|
| Test Art. 33 72-hour notification decision-making | Partially | Team debated "awareness" trigger extensively; delayed notification preparation by 30 minutes |
| Validate executive escalation procedures | Yes | CEO was engaged within expected timeframe; board notification discussed proactively |
| Assess media and stakeholder communication readiness | Partially | First media statement was delayed; holding statement was not pre-prepared |
| Evaluate backup restoration and service recovery coordination | Yes | Restoration decision was made promptly; IT team demonstrated clear understanding of backup procedures |

## Timeline Analysis

| Inject | Expected Response Time | Actual Response Time | Delta | Assessment |
|--------|----------------------|---------------------|-------|-----------|
| SOC alert (T+0) | Immediate IC activation | 3 minutes | +3 min | Adequate |
| Encryption spreading (T+15) | Isolation decision within 5 min | 8 minutes | +3 min | Adequate — debate about customer impact |
| Forensic finding (T+30) | Credential revocation within 10 min | 12 minutes | +2 min | Adequate |
| Database encrypted (T+60) | Art. 33 clock determination within 5 min | 22 minutes | +17 min | Needs improvement — extended debate |
| Ransom note + media (T+90) | Immediate no-pay decision; prepared statement within 10 min | 18 minutes for no-pay; 25 minutes for statement | +15 min | Needs improvement — no holding statement ready |
| Mandiant update (T+120) | Art. 33 submission decision within 5 min | 7 minutes | +2 min | Adequate |
| Media/customer crisis (T+150) | Coordinated response within 10 min | 15 minutes | +5 min | Adequate |

## Findings

### Critical Findings

**F-01: Art. 33 "awareness" determination was unclear**
The team spent 22 minutes debating when the controller "became aware" for 72-hour clock purposes. The breach response plan does not define clear criteria for awareness determination. This could lead to late notification in a real incident.
- **Recommendation**: Update the breach response plan with a clear definition: "Awareness occurs when the incident response team has reasonable certainty that personal data has been compromised, regardless of whether the DPO or CEO has been personally informed."
- **Owner**: Dr. Elena Vasquez (DPO)
- **Deadline**: 15 May 2026

### Major Findings

**F-02: No pre-prepared media holding statement**
When the first media inquiry arrived, the communications team took 25 minutes to draft a response. A pre-prepared holding statement should be available for immediate deployment.
- **Recommendation**: Create a generic breach holding statement template that can be deployed within 5 minutes of the first media inquiry.
- **Owner**: Martin Keller (Communications Director)
- **Deadline**: 30 April 2026

**F-03: Ransom payment decision lacked documented policy**
The team correctly decided not to pay the ransom, but the decision relied on individual judgment rather than a documented organizational policy. The discussion consumed 18 minutes.
- **Recommendation**: Document a formal ransom payment policy approved by the Board, aligned with OFAC sanctions compliance and law enforcement guidance.
- **Owner**: Sarah Chen (General Counsel)
- **Deadline**: 31 May 2026

### Minor Findings

**F-04: Customer communication tone was reactive**
The customer support talking points developed during the exercise were factual but lacked empathy. A more human-centered approach would improve customer trust during a crisis.
- **Recommendation**: Include empathy-focused language templates in the customer communication toolkit.
- **Owner**: James Park (VP Customer Success)
- **Deadline**: 30 April 2026

### Observations

**F-05: Works Council not relevant for this scenario but should be considered**
The insider threat scenario should be run next to test Works Council coordination, which was identified as a potential complexity in German breach response.
- **Recommendation**: Schedule the insider threat tabletop exercise for Q3 2026.
- **Owner**: Dr. Elena Vasquez (DPO)
- **Deadline**: Schedule by 30 June 2026

## Metrics

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Time from alert to IC activation | Under 5 minutes | 3 minutes | Met |
| Time from awareness to notification preparation start | Under 15 minutes | 22 minutes | Not met |
| Media response time | Under 10 minutes | 25 minutes | Not met |
| Decision consistency (aligned with policy) | 100% | 86% (6/7 decisions) | Needs improvement |
| Documentation completeness during exercise | All decisions documented | 5/7 decisions documented in real-time | Needs improvement |
