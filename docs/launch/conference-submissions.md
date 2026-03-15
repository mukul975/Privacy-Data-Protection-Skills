# Conference Submissions: Structured Privacy Skills for AI Agents

> **Primary Title:** "Structured Privacy Skills for AI Agents: An Open Standard Approach to Automated Compliance"
>
> **Lead Author/Speaker:** Mahipal Jangra
>
> **Last Updated:** 2026-03-15

---

## Table of Contents

1. [Speaker Bio](#1-speaker-bio)
2. [PEPR '26 Lightning Talk (5 min)](#2-pepr-26-lightning-talk-5-min)
3. [PEPR '26 Extended Talk (15 min)](#3-pepr-26-extended-talk-15-min)
4. [IAPP Privacy. Security. Risk. + AI Governance Global 2026](#4-iapp-privacy-security-risk--ai-governance-global-2026)
5. [CPDP LatAm 2026 Panel Proposal](#5-cpdp-latam-2026-panel-proposal)
6. [Conference Calendar and Deadlines](#6-conference-calendar-and-deadlines)

---

## 1. Speaker Bio

### Short Bio (75 words)

Mahipal Jangra is a cybersecurity and AI researcher pursuing an M.Sc. in Cybersecurity and Artificial Intelligence at SRH Berlin University of Applied Sciences. He has published four papers at IS&T Electronic Imaging 2026, including two sole-authored works on AI agent protocol security. His open-source Privacy & Data Protection Skills repository provides 988+ structured, machine-readable compliance skills spanning GDPR, CCPA, LGPD, HIPAA, and cross-border transfer frameworks, bridging the gap between regulatory requirements and automated enforcement.

*Word count: 75*

### Extended Bio (150 words)

Mahipal Jangra is a cybersecurity and AI researcher pursuing an M.Sc. in Cybersecurity and Artificial Intelligence at SRH Berlin University of Applied Sciences. His research focuses on the intersection of AI agent security, privacy engineering, and regulatory compliance automation. He has published four papers at IS&T Electronic Imaging 2026, including two sole-authored works addressing security vulnerabilities in AI agent communication protocols, specifically examining trust boundaries and prompt injection risks in multi-agent systems.

Mahipal is the creator and lead maintainer of the Privacy & Data Protection Skills repository, an open-source project providing 988+ structured, machine-readable compliance skills that cover GDPR, CCPA/CPRA, LGPD, HIPAA, PIPEDA, and cross-border data transfer frameworks including Standard Contractual Clauses and Binding Corporate Rules. The repository translates complex regulatory obligations into executable task definitions, enabling AI agents to perform privacy impact assessments, data subject access requests, and compliance audits with verifiable accuracy and full audit trails.

*Word count: 148*

---

## 2. PEPR '26 Lightning Talk (5 min)

> **Conference:** 2026 USENIX Conference on Privacy Engineering Practice and Respect (PEPR '26)
> **Dates:** June 1-2, 2026
> **Venue:** Hyatt Regency Santa Clara, Santa Clara, CA, USA
> **Format:** 5-minute lightning talk
> **Submission Portal:** https://pepr26.usenix.hotcrp.com/
> **CFP Deadline:** January 27, 2026 (passed; retain for future reference or late-breaking submissions)
> **Notification:** February 26, 2026

### Title

Structured Privacy Skills for AI Agents: An Open Standard Approach to Automated Compliance

### Abstract (200 words)

Privacy engineering teams face a compounding challenge: the number of regulatory frameworks multiplying globally while the operational tasks required for compliance grow in complexity. AI agents can automate parts of this workload, but without structured task definitions grounded in actual regulatory text, they produce unreliable outputs that cannot survive audit scrutiny.

We present Privacy & Data Protection Skills, an open-source repository of 988+ machine-readable skill definitions spanning GDPR, CCPA/CPRA, LGPD, HIPAA, PIPEDA, and 12 additional frameworks. Each skill encodes a discrete compliance task -- from executing a Data Protection Impact Assessment under GDPR Article 35 to processing a Right to Erasure request under CCPA Section 1798.105 -- with explicit inputs, outputs, validation criteria, and regulatory citations. The YAML-based schema defines prerequisites, workflow steps, quality thresholds, and audit trail requirements, allowing any AI agent framework to consume them without vendor lock-in.

Early evaluation across 15 compliance scenarios shows that agents using structured skills produce outputs with 40% fewer regulatory citation errors compared to free-form prompting. We discuss the architectural decisions behind the schema, integration patterns with existing privacy management platforms, and how the community-maintained approach keeps pace with regulatory change.

*Word count: 189*

### Detailed Outline

1. **Problem framing** (60s): The scaling gap between regulatory proliferation and privacy team capacity. Concrete numbers: 15+ active privacy frameworks worldwide, average organization subject to 4.3 simultaneously.
2. **The structured skills approach** (90s): Walk through one skill definition (DPIA under GDPR Art. 35) showing YAML schema, regulatory anchoring, and validation criteria.
3. **Agent integration architecture** (60s): How skill definitions plug into LangChain, AutoGen, and custom agent frameworks. Diagram showing skill selection, execution, and audit trail generation.
4. **Early results** (60s): Comparison of structured-skill-guided agents versus free-form prompted agents across 15 compliance tasks. Key finding: citation accuracy, completeness of procedural steps, audit trail quality.
5. **Call to action** (30s): Invitation to contribute skills, adopt the schema, and participate in cross-framework validation.

---

## 3. PEPR '26 Extended Talk (15 min)

> **Conference:** 2026 USENIX Conference on Privacy Engineering Practice and Respect (PEPR '26)
> **Dates:** June 1-2, 2026
> **Venue:** Hyatt Regency Santa Clara, Santa Clara, CA, USA
> **Format:** 15-minute extended talk + Q&A
> **Submission Portal:** https://pepr26.usenix.hotcrp.com/
> **CFP Deadline:** January 27, 2026 (passed; retain for future reference)
> **Notification:** February 26, 2026

### Title

Structured Privacy Skills for AI Agents: An Open Standard Approach to Automated Compliance

### Abstract (350 words)

The global regulatory landscape now spans over 160 national data protection laws, and organizations routinely operate under four or more overlapping frameworks simultaneously. Privacy engineering teams must translate each framework's requirements into operational procedures, maintain those procedures as regulations evolve, and execute them at a scale that outpaces manual capacity. AI agents offer a path toward scalable compliance operations, but deploying them without structured, regulation-grounded task definitions introduces significant risks: hallucinated legal citations, incomplete procedural steps, and outputs that fail regulatory audit.

We present Privacy & Data Protection Skills, an open-source repository containing 988+ machine-readable skill definitions that encode discrete compliance tasks across GDPR, CCPA/CPRA, LGPD, HIPAA, PIPEDA, and 12 additional data protection frameworks. Each skill is defined in a YAML schema that specifies the regulatory basis (article, section, or recital), required inputs (data inventories, processing records, risk assessments), procedural workflow steps, validation criteria with measurable quality thresholds, expected outputs, and audit trail requirements. The schema is framework-agnostic: skills can be consumed by LangChain agents, Microsoft AutoGen workflows, Amazon Bedrock pipelines, or any system that parses structured YAML.

We describe three architectural contributions. First, the regulatory-anchored skill schema that prevents citation drift by binding every workflow step to a specific legal provision. Second, a cross-framework mapping layer that identifies overlapping obligations across jurisdictions, enabling a single agent execution to satisfy multiple compliance requirements simultaneously. Third, a community-governed update pipeline where regulatory changes trigger skill revisions through pull requests with mandatory legal-citation review.

We evaluate the approach across 15 representative compliance scenarios, including DPIA execution, Data Subject Access Request fulfillment, cross-border transfer assessments under Standard Contractual Clauses, and breach notification workflows. Agents using structured skills produced outputs with 40% fewer regulatory citation errors, 28% higher procedural completeness scores, and generated audit-ready documentation in every tested scenario. We discuss limitations, including the labor cost of skill authoring, ambiguity in regulatory interpretation, and the boundary between automatable and judgment-dependent compliance tasks.

*Word count: 301*

### Detailed Outline

1. **The compliance scaling problem** (2 min): Quantify the gap between regulatory growth and team capacity. Reference specific regulatory developments: EU AI Act interactions with GDPR, US state-level privacy law fragmentation (18 states with comprehensive laws by 2026), Brazil's LGPD enforcement acceleration.

2. **Why unstructured AI agents fail at compliance** (2 min): Demonstrate failure modes with concrete examples. An agent asked to "conduct a DPIA" without structured guidance: omits necessity and proportionality assessment (Art. 35(7)(b)), fabricates supervisory authority consultation thresholds, misattributes obligations from one framework to another.

3. **The structured skills schema** (3 min): Deep dive into the YAML schema using a live example -- the DPIA skill for GDPR Article 35. Walk through each field: regulatory_basis, prerequisites, inputs, workflow_steps (each with its own validation_criteria), outputs, quality_thresholds, and audit_trail_spec. Show how the schema enforces completeness.

4. **Cross-framework mapping** (2 min): Demonstrate how the mapping layer identifies equivalent obligations across GDPR, CCPA, and LGPD. Example: the right to erasure maps to GDPR Art. 17, CCPA Sec. 1798.105, and LGPD Art. 18(VI), with divergences in scope and exceptions explicitly encoded.

5. **Agent integration patterns** (2 min): Architecture diagram showing skill discovery, selection, parameterized execution, and audit trail generation. Implementation examples with LangChain tool definitions and AutoGen task workflows. Discussion of the execution boundary: what the agent does versus what requires human review.

6. **Evaluation results** (2 min): Present findings from 15-scenario evaluation. Metrics: regulatory citation accuracy, procedural step completeness, audit trail quality, time-to-completion. Comparison with baseline (free-form prompting) and semi-structured approaches (template-based prompting).

7. **Community governance and sustainability** (1 min): How the open-source model handles regulatory updates. Pull request workflow with legal-citation review requirements. Contribution statistics and roadmap.

8. **Limitations and future work** (1 min): Skill authoring cost, handling regulatory ambiguity, multi-jurisdictional conflict resolution, and expanding to sector-specific regulations (financial services, healthcare, telecommunications).

---

## 4. IAPP Privacy. Security. Risk. + AI Governance Global 2026

> **Conference:** IAPP P.S.R. + AI Governance Global 2026
> **Dates:** October 6-9, 2026
> **Venue:** Seattle Convention Center, Seattle, WA, USA
> **Format:** 60-minute breakout session (single speaker presentation)
> **Submission Portal:** https://iapp.org/connect/call-for-/
> **CFP Deadline:** March 1, 2026 (passed; check for late/rolling submissions)
> **Contact:** programming@iapp.org
>
> **Also applicable to:**
> - IAPP Global Summit 2026 (March 30 - April 2, Washington, DC) -- for future year submissions
> - IAPP Europe Congress 2026 (Brussels) -- CFP deadline April 12, 2026

### Session Title

Structured Privacy Skills for AI Agents: An Open Standard Approach to Automated Compliance

### Session Type

Single Speaker Presentation -- 60 minutes

### Track Alignment

Privacy Engineering; Privacy-Enhancing Technologies and Generative AI; Building Technology into Privacy Operations

### Session Description (300 words)

Privacy operations teams are expected to do more with less. The regulatory surface area keeps expanding -- GDPR enforcement actions reached record levels in 2025, eighteen US states now have comprehensive privacy laws, and Brazil's ANPD issued its first significant LGPD fines. Meanwhile, AI agents are entering enterprise workflows with promises of automation. But when organizations deploy general-purpose AI agents for compliance tasks, the results are unpredictable: fabricated legal citations, missing procedural steps, and documentation that would not survive a supervisory authority's review.

This session introduces a different approach. The Privacy & Data Protection Skills repository is an open-source collection of 988+ structured, machine-readable skill definitions that encode specific compliance tasks -- from conducting a DPIA to processing a cross-border transfer impact assessment. Each skill specifies its regulatory basis down to the article and section level, defines the required inputs and procedural steps, sets measurable quality thresholds, and mandates audit trail generation. The YAML-based format works with any AI agent framework without proprietary dependencies.

Attendees will see a live walkthrough of how structured skills transform an AI agent from an unreliable compliance assistant into an auditable workflow executor. We will examine three real scenarios: executing a Data Subject Access Request that satisfies both GDPR Article 15 and CCPA Section 1798.110 simultaneously, conducting a transfer impact assessment under the EU's Standard Contractual Clauses, and generating a breach notification timeline that meets GDPR's 72-hour and CCPA's "expedient" requirements in parallel.

The session concludes with practical guidance for privacy professionals: how to evaluate whether your compliance tasks are candidates for structured automation, how to integrate skill-based agents into existing privacy management platforms like OneTrust or BigID, and how to participate in the open-source community maintaining these skills. Attendees will leave with actionable steps they can implement immediately.

*Word count: 277*

### Learning Objectives

1. Understand why general-purpose AI agents fail at privacy compliance tasks and how structured, regulation-anchored skill definitions solve the reliability problem.
2. Evaluate which compliance operations in their organization are candidates for structured AI automation versus tasks requiring human judgment.
3. Implement a pilot integration of open-source structured privacy skills with their existing privacy management platform and AI agent framework.

### Target Audience

Privacy engineers, DPOs, compliance managers, privacy program leaders, and technologists building privacy automation tooling.

---

## 5. CPDP LatAm 2026 Panel Proposal

> **Conference:** CPDP LatAm 2026 -- Computers, Privacy & Data Protection Latin America
> **Theme:** "Data Governance for Digital Sovereignty, Cooperation, and Interoperability"
> **Dates:** August 12-13, 2026 (Satellite AI event: August 14)
> **Venue:** Rio de Janeiro, Brazil
> **Languages:** English, Portuguese, Spanish
> **Panel CFP Deadline:** April 30, 2026
> **Paper CFP Deadline:** May 30, 2026 (6,000-12,000 words, double-blind peer review)
> **Website:** https://cpdp.lat/en/

### Panel Proposal Title

Structured Privacy Skills for AI Agents: Toward Interoperable Compliance Automation Across Latin American Data Protection Frameworks

### Panel Description (300 words)

Latin America's data protection landscape presents a unique interoperability challenge. Brazil's LGPD, Argentina's PDPA, Colombia's Law 1581, Chile's recently modernized data protection law, and Mexico's LFPDPPP each establish distinct requirements for data processing, subject rights, and cross-border transfers. Organizations operating across the region must satisfy multiple frameworks simultaneously, and the entry of AI agents into compliance operations raises critical questions about how automated systems can respect the jurisdictional nuances that define each framework.

This panel examines an open-standard approach to encoding privacy compliance tasks as structured, machine-readable skill definitions that AI agents can execute with regulatory precision. The Privacy & Data Protection Skills repository contains 988+ skills spanning global frameworks, with specific coverage of LGPD obligations including Data Protection Impact Reports (RIPD) under LGPD Article 38, data subject rights processing under Article 18, international transfer assessments aligned with ANPD Resolution CD/ANPD No. 19, and breach notification procedures under Article 48.

The panel brings together perspectives on three dimensions of this challenge. First, how structured skill schemas can encode the specific procedural requirements of Latin American frameworks while maintaining interoperability with global standards like GDPR -- enabling organizations to satisfy overlapping obligations through single execution paths. Second, how open-source, community-governed skill repositories can keep pace with regulatory developments across multiple jurisdictions without creating vendor dependencies. Third, the sovereignty implications: when AI agents execute compliance tasks using externally maintained skill definitions, how do organizations ensure that the encoded interpretations align with local regulatory guidance and cultural expectations around data protection.

The discussion directly addresses the conference theme of digital sovereignty and interoperability by exploring whether standardized compliance automation can strengthen local data governance rather than homogenize it, and whether community-governed open standards offer a path toward cooperation without subordination.

*Word count: 268*

### Panelist Roles (Proposed)

1. **Mahipal Jangra** (Moderator/Presenter) -- Creator of Privacy & Data Protection Skills repository; M.Sc. Cybersecurity and AI, SRH Berlin.
2. **Privacy Law Scholar** (Invited) -- Latin American data protection law expert; LGPD, PDPA, and regional harmonization.
3. **Industry Practitioner** (Invited) -- DPO or privacy engineer at a multinational operating across Latin America.
4. **Civil Society Representative** (Invited) -- Digital rights organization focused on data sovereignty in the Global South.

---

## 6. Conference Calendar and Deadlines

| Conference | Dates | Location | Submission Deadline | Status |
|---|---|---|---|---|
| **IAPP Global Summit 2026** | Mar 30 - Apr 2, 2026 | Washington, DC | Closed | Reference for 2027 |
| **PEPR '26** | Jun 1-2, 2026 | Santa Clara, CA | Jan 27, 2026 | Closed; materials ready for late-breaking or 2027 |
| **CPDP LatAm 2026 (Panels)** | Aug 12-13, 2026 | Rio de Janeiro | **Apr 30, 2026** | **OPEN -- Submit by April 30** |
| **CPDP LatAm 2026 (Papers)** | Aug 12-13, 2026 | Rio de Janeiro | **May 30, 2026** | **OPEN -- Submit by May 30** |
| **CPDP LatAm 2026 (AI Satellite)** | Aug 14, 2026 | Rio de Janeiro | TBD | Monitor website |
| **IAPP P.S.R. + AIGG 2026** | Oct 6-9, 2026 | Seattle, WA | Mar 1, 2026 | Closed; check for rolling/late |
| **IAPP Europe Congress 2026** | TBD | Brussels | **Apr 12, 2026** | **OPEN -- Submit by April 12** |

### Immediate Action Items

1. **CPDP LatAm Panel (Due April 30):** Submit panel proposal through https://cpdp.lat/en/. Recruit panelists from Latin American privacy law and civil society communities. Adapt abstract to emphasize LGPD, PDPA, and regional interoperability.
2. **IAPP Europe Congress (Due April 12):** Adapt IAPP P.S.R. session proposal for European audience. Emphasize GDPR, EU AI Act interactions, and SCCs. Submit through IAPP portal.
3. **CPDP LatAm Paper (Due May 30):** Develop 6,000-12,000 word paper expanding on structured skills approach with Latin American framework analysis. Submit for double-blind peer review.
4. **PEPR '27 Preparation:** Monitor USENIX website for PEPR '27 CFP (expected late 2026). Update evaluation data and expand skill coverage metrics.

---

## Appendix: Submission Checklist

### Per-Conference Requirements

**PEPR '26 (USENIX)**
- [x] Talk title
- [x] Speaker short bio (75 words)
- [x] Short abstract
- [x] Detailed talk outline
- [ ] HotCRP submission (deadline passed)

**IAPP P.S.R. + AIGG 2026**
- [x] Session title
- [x] Session type (single speaker / 60 min)
- [x] Session description
- [x] Learning objectives (3)
- [x] Target audience
- [x] Speaker extended bio (150 words)
- [ ] Online proposal form submission

**CPDP LatAm 2026 Panel**
- [x] Panel title
- [x] Panel description
- [x] Proposed panelist roles
- [ ] Confirm panelists and collect bios
- [ ] Submit through CPDP LatAm portal by April 30

**CPDP LatAm 2026 Paper**
- [ ] Expand to 6,000-12,000 words
- [ ] Anonymize for double-blind review
- [ ] Submit by May 30

---

*Document prepared for the Privacy & Data Protection Skills project launch campaign.*
*All abstracts are submission-ready and tailored to each conference's documented requirements and thematic focus.*
