# Launch Content Package — Privacy & Data Protection Skills

> **Repository**: [github.com/mukul975/Privacy-Data-Protection-Skills](https://github.com/mukul975/Privacy-Data-Protection-Skills)
> **Author**: Mahipal ([@mukul975](https://github.com/mukul975))
> **Credentials**: M.Sc. Cybersecurity and AI, SRH Berlin University of Applied Sciences. 4 papers at Electronic Imaging 2026 (2 sole-authored on AI agent protocol security). Maintainer of [Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) (730+ skills).
> **Date prepared**: 2026-03-15
> **Repo stats**: 282 skills | 21 plugin bundles | 6 LobeHub agents | MIT licensed

---

## Verified Statistics (as of March 2026)

| Stat | Value | Source |
|------|-------|--------|
| Cumulative GDPR fines (since May 2018) | EUR 5.88B -- 7.1B (varies by tracker) | [DLA Piper Jan 2026 Survey](https://www.dlapiper.com/en/insights/publications/2026/01/dla-piper-gdpr-fines-and-data-breach-survey-january-2026), [Enforcement Tracker](https://www.enforcementtracker.com/) |
| Largest single GDPR fine | EUR 1.2B -- Meta (May 2023, Ireland DPC) | [EDPB](https://www.edpb.europa.eu/news/news/2023/12-billion-euro-fine-facebook-result-edpb-binding-decision_en) |
| TikTok GDPR fine | EUR 530M (April 2025, Ireland DPC) | [DPC press release](https://www.dataprotection.ie/en/news-media/latest-news/irish-data-protection-commission-fines-tiktok-eu530-million-and-orders-corrective-measures-following) |
| EU AI Act -- bulk enforcement starts | August 2, 2026 | [European Commission](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) |
| US states with comprehensive privacy laws | 20 (as of Jan 2026) | [MultiState tracker](https://www.multistate.us/insider/2026/2/4/all-of-the-comprehensive-privacy-laws-that-take-effect-in-2026) |
| Texas vs Google privacy settlement | USD 1.375B (finalized Nov 2025) | [Texas AG press release](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-secures-historic-1375-billion-settlement-google-related-texans-data) |
| Texas vs Meta privacy settlement | USD 1.4B (July 2025) | [Texas AG press release](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-finalizes-historic-settlement-google-and-secures-1375-billion-big-tech) |
| India DPDP Act -- full compliance deadline | May 13, 2027 (Phase 2: Nov 13, 2026) | [DPDP Rules](https://www.dpdpa.com/dpdparules.html) |

---

## 1. Hacker News -- Show HN

### Title

```
Show HN: 282 open-source privacy-engineering skills for AI agents (GDPR, CCPA, AI Act, DPDP)
```

### Intro Comment

```
Hi HN,

I built an open-source library of 282 structured privacy and data-protection skills
that any AI agent (Claude, GPT, open-source LLMs) can load to perform real compliance
work -- DPIAs, breach-response playbooks, cross-border transfer assessments, cookie
audits, ROPA generation, and more.

Why this exists: GDPR fines have crossed EUR 5.88 billion. The EU AI Act enforcement
starts August 2, 2026. Twenty US states now have comprehensive privacy laws. India's
DPDP Act enters Phase 2 in November. Texas alone recovered USD 2.77 billion from
Google and Meta. The compliance surface is exploding, but the tooling has not kept up.

Each skill ships with:
- A structured prompt template (agent-ready)
- Reference links to the actual legal text
- Automation scripts (Python/Bash) for recurring tasks
- Asset templates (checklists, matrices, decision trees)

The repo also includes 21 ChatGPT/LobeHub plugin bundles and 6 LobeHub agents.

Stack: Plain Markdown + YAML + Python/Bash scripts. No vendor lock-in. MIT licensed.

I'm a cybersecurity/AI grad student at SRH Berlin with 4 papers at Electronic
Imaging 2026 (2 sole-authored on AI agent protocol security). I also maintain
Anthropic-Cybersecurity-Skills (730+ skills).

Repo: https://github.com/mukul975/Privacy-Data-Protection-Skills

Feedback on coverage gaps, new jurisdiction requests, or integration ideas is very
welcome.
```

---

## 2. Reddit Posts

### 2a. r/privacy

**Title**: I open-sourced 282 privacy-engineering skills that turn AI agents into compliance tools -- GDPR, CCPA, DPDP, AI Act, and more

**Body**:

```
Hey r/privacy,

I've been building an open-source library of privacy and data-protection skills
designed to be loaded by AI agents (Claude, GPT, open-source LLMs). The goal is to
give privacy professionals structured, reusable building blocks for real compliance
work -- not just chatbot answers.

**What's in the repo (282 skills):**
- GDPR compliance: DPIAs, ROPA generation, breach response, cross-border transfers,
  consent management, cookie audits
- US privacy: CCPA/CPRA, 20 state laws, HIPAA (42 CFR Part 2), COPPA, FERPA
- EU AI Act: high-risk documentation, AI bias assessments, automated decision audits
- India DPDP Act: consent manager frameworks, data fiduciary obligations
- Privacy engineering: privacy by design, data classification, retention policies,
  vendor management, PETs (differential privacy, federated learning)

**Why now:**
- EUR 5.88B+ in cumulative GDPR fines
- TikTok hit with EUR 530M fine for EEA-to-China data transfers (April 2025)
- EU AI Act enforcement begins August 2, 2026
- Texas recovered USD 2.77B from Google + Meta in privacy settlements
- India DPDP Phase 2 starts November 2026
- 20 US states now have comprehensive privacy laws

Each skill includes a structured prompt, legal references, automation scripts, and
asset templates. MIT licensed. No vendor lock-in.

Repo: https://github.com/mukul975/Privacy-Data-Protection-Skills

I'm a cybersecurity/AI grad student at SRH Berlin (4 papers at Electronic Imaging
2026, 2 sole-authored on AI agent protocol security). Also maintain
Anthropic-Cybersecurity-Skills (730+ skills).

Looking for feedback on:
- Coverage gaps (jurisdictions, regulations, use cases)
- Integration ideas (MCP servers, IDE plugins)
- Contributions from practicing DPOs and privacy engineers

Happy to answer questions.
```

---

### 2b. r/cybersecurity

**Title**: Open-sourced 282 privacy + data protection skills for AI agents -- structured prompts, scripts, and templates covering GDPR through AI Act

**Body**:

```
r/cybersecurity,

Sharing a project I've been working on: an open-source library of 282 structured
privacy and data-protection skills for AI agents.

**The problem:** Privacy compliance is increasingly a security team responsibility.
GDPR, CCPA, the EU AI Act, India's DPDP Act -- the regulatory surface keeps growing.
Fines have crossed EUR 5.88B under GDPR alone. Texas recovered USD 2.77B from Google
and Meta. But most compliance tooling is expensive SaaS that doesn't integrate with
security workflows.

**The approach:** Each skill is a self-contained unit with:
- A structured prompt template any AI agent can load
- References to the actual legal text
- Python/Bash automation scripts
- Asset templates (checklists, matrices, decision trees)

**Coverage includes:**
- Breach response and notification (GDPR Art. 33/34, state breach laws)
- Cross-border data transfers (SCCs, BCRs, adequacy decisions)
- AI security: automated decision audits, AI DPIAs, bias assessments
- Data classification and retention
- Vendor/third-party privacy management
- Healthcare privacy (HIPAA, 42 CFR Part 2)
- Children's privacy (COPPA, AADC)

Everything is MIT licensed, plain Markdown + YAML + scripts. No vendor lock-in.

Repo: https://github.com/mukul975/Privacy-Data-Protection-Skills

Background: I'm finishing my M.Sc. in Cybersecurity and AI at SRH Berlin. 4 papers
at Electronic Imaging 2026 (2 sole-authored on AI agent protocol security). I also
maintain Anthropic-Cybersecurity-Skills (730+ cybersecurity skills).

Contributions welcome -- especially from folks working incident response, GRC, or
privacy engineering.
```

---

### 2c. r/opensource

**Title**: 282 MIT-licensed privacy-engineering skills for AI agents -- structured prompts, automation scripts, and compliance templates

**Body**:

```
Hi r/opensource,

Sharing a project: **Privacy & Data Protection Skills** -- an open-source library
of 282 structured skills that AI agents can load to perform privacy compliance work.

**What it is:**
A collection of plain Markdown + YAML + Python/Bash scripts. Each skill covers a
specific privacy or data-protection task (DPIA, breach notification, cookie audit,
cross-border transfer assessment, etc.) with a structured prompt, legal references,
automation scripts, and reusable templates.

**What it covers:**
- GDPR (30+ skill areas)
- US privacy (CCPA/CPRA, 20 state laws, HIPAA, COPPA, FERPA)
- EU AI Act compliance
- India DPDP Act
- Privacy engineering (PbD, data classification, PETs)
- 21 ChatGPT/LobeHub plugin bundles
- 6 LobeHub AI agents

**Tech decisions:**
- MIT license -- use it however you want
- No framework dependency -- works with Claude, GPT, open-source LLMs, or as
  standalone reference
- Plain text formats -- easy to grep, version, and extend
- Each skill is self-contained -- take what you need

Repo: https://github.com/mukul975/Privacy-Data-Protection-Skills

I also maintain Anthropic-Cybersecurity-Skills (730+ cybersecurity skills, same
structure).

Looking for contributors -- especially folks who work with non-EU/non-US privacy
regulations (Brazil LGPD, South Korea PIPA, Japan APPI, etc.).
```

---

### 2d. r/gdpr

**Title**: Open-source library of 282 GDPR and privacy skills for AI agents -- DPIAs, breach response, cross-border transfers, ROPA, and more

**Body**:

```
Hi r/gdpr,

I've built an open-source collection of 282 structured privacy skills designed for
AI agents to use in real compliance work.

**GDPR-specific coverage includes:**
- Data Protection Impact Assessments (DPIAs) -- including AI-specific DPIAs
- Records of Processing Activities (ROPA) generation
- Breach response and 72-hour notification workflows
- Cross-border transfer assessments (SCCs, BCRs, adequacy decisions)
- Consent management and cookie compliance
- Data subject rights handling (access, erasure, portability, objection)
- Lawful basis documentation
- Children's data (Age Appropriate Design Code)
- Special category data processing

**Why this matters right now:**
- Cumulative GDPR fines: EUR 5.88B+ since May 2018
- Meta's record EUR 1.2B fine for US data transfers (2023)
- TikTok's EUR 530M fine for EEA-to-China transfers (April 2025)
- EU AI Act enforcement begins August 2, 2026 -- adding new obligations
  for AI systems that process personal data

Each skill ships with structured prompts, links to the relevant GDPR articles,
automation scripts, and templates. MIT licensed.

Repo: https://github.com/mukul975/Privacy-Data-Protection-Skills

I'm particularly interested in feedback from practicing DPOs on:
- Which compliance tasks would benefit most from AI-assisted workflows
- Coverage gaps in the GDPR skill set
- How you'd integrate this into existing DPO tooling

Background: M.Sc. Cybersecurity and AI, SRH Berlin. 4 papers at Electronic
Imaging 2026.
```

---

### 2e. r/legaltech

**Title**: Built 282 open-source privacy compliance skills for AI agents -- turning LLMs into practical tools for DPOs and privacy lawyers

**Body**:

```
r/legaltech,

I've been working on an open-source project that sits at the intersection of AI
agents and privacy law: a library of 282 structured skills that AI agents (Claude,
GPT, open-source LLMs) can load to assist with privacy compliance tasks.

**The pitch for legaltech:** Instead of building one monolithic privacy compliance
tool, this provides modular building blocks. Each skill is a self-contained unit
covering a specific compliance task -- a DPIA, a breach notification workflow, a
cross-border transfer assessment, a cookie audit, etc.

**Each skill includes:**
- A structured prompt template (agent-ready, but also works as a reference checklist)
- Links to the relevant legal text (GDPR articles, CCPA sections, etc.)
- Automation scripts (Python/Bash) for recurring tasks
- Asset templates (checklists, matrices, decision trees)

**Jurisdictional coverage:**
- EU: GDPR, ePrivacy, EU AI Act
- US: CCPA/CPRA, 20 state privacy laws, HIPAA, COPPA, FERPA
- India: DPDP Act
- Cross-border: adequacy decisions, SCCs, BCRs

**Market context:**
- EUR 5.88B+ in GDPR fines and climbing
- EU AI Act enforcement starts August 2, 2026
- 20 US states with comprehensive privacy laws
- India DPDP Phase 2 begins November 2026
- Texas alone recovered USD 2.77B from Google and Meta

MIT licensed. Plain Markdown + YAML. No vendor lock-in.

Repo: https://github.com/mukul975/Privacy-Data-Protection-Skills

Would love feedback from privacy lawyers and legaltech builders on how to make
these skills more useful in legal workflows.
```

---

### 2f. r/europrivacy

**Title**: Open-sourced 282 structured privacy skills for AI agents -- heavy EU coverage (GDPR, ePrivacy, AI Act) plus global regulations

**Body**:

```
Hi r/europrivacy,

Sharing an open-source project relevant to EU privacy practitioners: a library of
282 structured skills for AI agents, with deep coverage of EU privacy law.

**EU-specific coverage:**
- GDPR: DPIAs, ROPA, breach notification, cross-border transfers (SCCs, BCRs,
  adequacy), consent, cookie compliance, data subject rights, lawful basis, DPO
  obligations, special category data, children's data
- ePrivacy: cookie consent, electronic communications privacy
- EU AI Act: high-risk system documentation, AI DPIAs, automated decision
  assessments, bias auditing, deployment checklists

**Context:**
- GDPR fines have crossed EUR 5.88B since enforcement began in May 2018
- Ireland's DPC alone accounts for EUR 4.04B in fines (Meta EUR 1.2B, TikTok
  EUR 530M, etc.)
- EU AI Act high-risk obligations become enforceable August 2, 2026
- The regulatory burden on EU-based privacy teams keeps growing

**How it works:** Each skill is a self-contained Markdown + YAML + Python/Bash
package. Load the prompt into any AI agent and it can guide or execute the
compliance task. Or use the templates and checklists as standalone references.

MIT licensed. No vendor lock-in.

Repo: https://github.com/mukul975/Privacy-Data-Protection-Skills

I'm a cybersecurity/AI student at SRH Berlin. Feedback from EU privacy
professionals is especially valuable -- particularly on coverage gaps for
sector-specific regulations.
```

---

## 3. Twitter/X -- 6-Tweet Thread

### Tweet 1 (Hook)

```
I open-sourced 282 privacy-engineering skills that turn AI agents into compliance
tools.

GDPR. CCPA. EU AI Act. India DPDP Act. 20 US state laws.

DPIAs, breach response, cross-border transfers, cookie audits, ROPA, and more --
all structured for AI agents to execute.

Thread:
```

### Tweet 2 (Problem)

```
The compliance surface is exploding:

- EUR 5.88B+ in cumulative GDPR fines
- EUR 530M TikTok fine for China data transfers
- EU AI Act enforcement starts Aug 2, 2026
- 20 US states with privacy laws
- Texas recovered USD 2.77B from Google + Meta
- India DPDP full compliance by May 2027

Privacy teams are drowning.
```

### Tweet 3 (Solution)

```
Each skill is a self-contained unit:

- Structured prompt template (any AI agent can load it)
- Legal references (actual GDPR articles, CCPA sections)
- Python/Bash automation scripts
- Asset templates (checklists, matrices, decision trees)

Plain Markdown + YAML. No vendor lock-in. MIT licensed.
```

### Tweet 4 (Coverage)

```
What's covered:

- GDPR: DPIAs, ROPA, breach response, transfers, consent
- US: CCPA/CPRA, HIPAA, COPPA, FERPA, 20 state laws
- EU AI Act: high-risk docs, AI DPIAs, bias audits
- India DPDP Act: consent frameworks
- Privacy engineering: PbD, data classification, PETs

282 skills. 21 plugin bundles. 6 LobeHub agents.
```

### Tweet 5 (Background)

```
About me: I'm @mukul975

- M.Sc. Cybersecurity and AI @ SRH Berlin
- 4 papers at Electronic Imaging 2026 (2 sole-authored on AI agent protocol
  security)
- Also maintain Anthropic-Cybersecurity-Skills (730+ skills)

Building the open-source infrastructure for AI-assisted compliance.
```

### Tweet 6 (CTA)

```
Repo: github.com/mukul975/Privacy-Data-Protection-Skills

Looking for:
- DPOs and privacy engineers to test and contribute
- Jurisdiction requests (LGPD, PIPA, APPI, etc.)
- Integration ideas (MCP servers, IDE plugins)

Star it. Fork it. File an issue. PRs welcome.

#privacy #GDPR #AI #opensource #cybersecurity #compliance #EUAIAct #dataprotection
```

### Accounts to Tag

```
@ICaboretDF (IAPP)
@europaborgen (EU data protection)
@PrivacyMatters
@EUDigitalPolicy
@OpenSourceOrg
@naborsky (noyb)
@maxschrems
@ClaudeAI (Anthropic)
@AnthropicAI
@LobeHub
@GitHubCommunity
```

---

## 4. LinkedIn Post

```
I just open-sourced 282 privacy and data-protection skills that turn AI agents into
practical compliance tools.

The regulatory landscape in 2026:
-- EUR 5.88B+ in cumulative GDPR fines since May 2018
-- EUR 530M TikTok fine for EEA-to-China data transfers (April 2025)
-- EUR 1.2B Meta fine -- still the record (May 2023)
-- EU AI Act enforcement starts August 2, 2026
-- 20 US states now have comprehensive privacy laws
-- Texas recovered USD 2.77B from Google and Meta in privacy settlements
-- India DPDP Act enters Phase 2 in November 2026

Privacy teams are expected to handle all of this. The tooling hasn't kept up.

Privacy & Data Protection Skills is an open-source library of structured,
agent-ready skills covering:

-- GDPR: DPIAs, ROPA, breach response, cross-border transfers, consent, cookies
-- US privacy: CCPA/CPRA, HIPAA, COPPA, FERPA, 20 state laws
-- EU AI Act: high-risk documentation, AI DPIAs, automated decision audits
-- India DPDP Act: consent manager frameworks, data fiduciary obligations
-- Privacy engineering: privacy by design, data classification, retention, PETs

Each skill ships with a structured prompt template, legal references, Python/Bash
automation scripts, and reusable asset templates.

282 skills. 21 plugin bundles. 6 LobeHub agents. MIT licensed. No vendor lock-in.

This is the sister project to Anthropic-Cybersecurity-Skills (730+ cybersecurity
skills). Together they provide the largest open-source skill library for
AI-assisted security and privacy work.

Background: I'm finishing my M.Sc. in Cybersecurity and AI at SRH Berlin
University of Applied Sciences. I have 4 papers at Electronic Imaging 2026,
including 2 sole-authored papers on AI agent protocol security.

Repository: https://github.com/mukul975/Privacy-Data-Protection-Skills

If you're a DPO, privacy engineer, GRC professional, or legaltech builder --
I'd love your feedback. Star the repo, file an issue, or reach out directly.
Contributions are very welcome.

#Privacy #DataProtection #GDPR #CCPA #EUAIAct #Cybersecurity #OpenSource
#PrivacyEngineering #Compliance #LegalTech #AI #AIAgents #PrivacyByDesign
#DataPrivacy #GRC #DPO #DPDP #InformationSecurity
```

---

## 5. Discord / Slack Template

> Use for: Privado.ai Slack, Data Privacy Slack community, OWASP Slack

```
Hey everyone,

I just open-sourced a library of 282 structured privacy and data-protection skills
for AI agents.

**What it is:** A collection of self-contained skills covering GDPR, CCPA/CPRA,
EU AI Act, India DPDP Act, HIPAA, COPPA, and more. Each skill includes a
structured prompt, legal references, automation scripts, and templates.

**What you can do with it:**
- Load skills into Claude, GPT, or any LLM to assist with compliance tasks
- Use the templates and checklists as standalone references
- Automate recurring tasks (breach notification, DPIA, cookie audit, ROPA)

282 skills | 21 plugin bundles | 6 LobeHub agents | MIT licensed

Repo: https://github.com/mukul975/Privacy-Data-Protection-Skills

I also maintain Anthropic-Cybersecurity-Skills (730+ cybersecurity skills):
https://github.com/mukul975/Anthropic-Cybersecurity-Skills

Looking for feedback from privacy practitioners on coverage gaps and integration
ideas. PRs welcome!
```

---

## 6. GitHub Discussion -- Cross-Repo Announcement

> Post in: Anthropic-Cybersecurity-Skills repo Discussions

### Title

```
[Announcement] Sister project launched: Privacy & Data Protection Skills (282 skills)
```

### Body

```
Hi everyone,

I'm excited to announce the launch of **Privacy & Data Protection Skills** -- a
sister project to this cybersecurity skills repository.

## What is it?

An open-source library of **282 structured privacy and data-protection skills** for
AI agents, built with the same architecture you're familiar with from this repo.

## Why a separate repo?

Privacy and data protection has grown into its own discipline. With EUR 5.88B+ in
GDPR fines, the EU AI Act enforcement starting August 2, 2026, 20 US states with
comprehensive privacy laws, and India's DPDP Act rolling out -- the compliance
surface deserves dedicated coverage.

## Coverage

| Domain | Examples |
|--------|----------|
| GDPR | DPIAs, ROPA, breach response, cross-border transfers, consent, cookies |
| US Privacy | CCPA/CPRA, 20 state laws, HIPAA, COPPA, FERPA |
| EU AI Act | High-risk docs, AI DPIAs, automated decision audits, bias assessments |
| India DPDP | Consent frameworks, data fiduciary obligations |
| Privacy Engineering | PbD, data classification, retention, vendor management, PETs |

Plus 21 plugin bundles and 6 LobeHub agents.

## How they complement each other

| This repo (Cybersecurity) | New repo (Privacy) |
|---------------------------|-------------------|
| Threat modeling | Privacy impact assessments |
| Incident response | Breach notification (GDPR Art. 33/34) |
| Vulnerability management | Vendor privacy risk management |
| Security architecture | Privacy by design |
| 730+ skills | 282 skills |

## Links

- **Repository**: https://github.com/mukul975/Privacy-Data-Protection-Skills
- **License**: MIT (same as this repo)

If you've contributed to this repo, the privacy repo welcomes the same kind of
contributions. PRs, issues, and feedback are all welcome.
```

---

## 7. Day 2 Reddit Posts

### 7a. r/privacyguides

**Title**: Open-source library of 282 privacy-engineering skills for AI agents -- covers GDPR, CCPA, EU AI Act, DPDP, and privacy-by-design patterns

**Body**:

```
Hi r/privacyguides,

Sharing an open-source project for the privacy-minded: a library of 282 structured
privacy skills that AI agents can load and execute.

**Privacy engineering coverage:**
- Privacy by design patterns and implementation guides
- Data classification and data mapping
- Data retention policy generation
- Privacy-enhancing technologies (differential privacy, federated learning,
  homomorphic encryption)
- Cookie consent and tracking audits
- Consent management frameworks
- Data subject rights automation (access, erasure, portability)
- Age verification and children's privacy (COPPA, AADC)

**Regulatory coverage:**
- GDPR (EU), CCPA/CPRA (California), 20 US state privacy laws
- EU AI Act (enforcement starts August 2, 2026)
- India DPDP Act (Phase 2 starts November 2026)
- HIPAA, FERPA, COPPA

**How it works:** Each skill is a self-contained package with a structured prompt
template, references to actual legal text, automation scripts, and reusable
templates. Load any skill into Claude, GPT, or an open-source LLM and it can
guide or execute the compliance task.

Plain Markdown + YAML + Python/Bash. MIT licensed. No vendor lock-in.
No telemetry. No SaaS dependency.

Repo: https://github.com/mukul975/Privacy-Data-Protection-Skills

Feedback welcome -- especially on privacy engineering patterns you'd like to see
covered.
```

---

### 7b. r/compliance

**Title**: Open-sourced 282 structured compliance skills for AI agents -- GDPR, CCPA, EU AI Act, HIPAA, DPDP, and more

**Body**:

```
Hi r/compliance,

I've been building an open-source library of 282 structured privacy and data
protection skills designed to make compliance work more efficient using AI agents.

**The compliance case:**

The workload keeps growing:
- EUR 5.88B+ in cumulative GDPR fines
- EU AI Act high-risk obligations enforceable August 2, 2026
- 20 US states with comprehensive privacy laws (Indiana, Kentucky, Rhode Island
  joined Jan 1, 2026)
- India DPDP Act Phase 2 begins November 2026
- Texas recovered USD 2.77B from Google and Meta in privacy settlements

Compliance teams need scalable tooling that isn't locked behind expensive SaaS.

**What this provides:**
- 282 self-contained skills covering specific compliance tasks
- Each skill includes: structured prompt, legal references, automation scripts,
  and templates
- Works with any AI agent (Claude, GPT, open-source LLMs) or as standalone
  reference material
- Coverage: GDPR, CCPA/CPRA, EU AI Act, India DPDP, HIPAA, COPPA, FERPA,
  20 US state privacy laws

**Practical examples:**
- Generate a DPIA for a new AI system in under an hour
- Automate ROPA maintenance across business units
- Run a cookie compliance audit with structured checklist
- Assess cross-border transfer mechanisms (SCCs vs BCRs vs adequacy)
- Create breach notification workflows with jurisdiction-specific timelines

MIT licensed. No vendor lock-in.

Repo: https://github.com/mukul975/Privacy-Data-Protection-Skills

Background: M.Sc. Cybersecurity and AI, SRH Berlin. 4 papers at Electronic
Imaging 2026. Also maintain Anthropic-Cybersecurity-Skills (730+ skills).

Feedback from compliance professionals is especially valuable. What tasks do
you most want AI to help with?
```

---

### 7c. r/dataprotection

**Title**: I built 282 open-source data protection skills for AI agents -- practical tools for DPOs, privacy engineers, and compliance teams

**Body**:

```
Hi r/dataprotection,

I've open-sourced a library of 282 structured data protection skills that AI
agents can use to assist with real compliance work.

**Built for data protection practitioners:**

This isn't a chatbot that gives generic GDPR advice. Each skill is a structured,
task-specific unit designed for practical compliance work:

- **DPIAs**: Standard and AI-specific, with risk matrices and mitigation templates
- **Breach response**: 72-hour notification workflows, authority templates,
  communication scripts
- **Cross-border transfers**: SCC assessments, BCR frameworks, adequacy
  decision tracking, TIA templates
- **Data subject rights**: Automated response workflows for access, erasure,
  portability, rectification, objection
- **ROPA**: Generation and maintenance templates
- **Consent management**: Lawful basis documentation, consent lifecycle tracking
- **Cookie compliance**: Audit scripts and category classification
- **Vendor management**: Third-party privacy risk assessments, DPA templates
- **Children's data**: COPPA, Age Appropriate Design Code
- **AI governance**: Automated decision documentation, bias assessment, AI Act
  high-risk compliance

**The numbers (March 2026):**
- EUR 5.88B+ cumulative GDPR fines
- EUR 1.2B Meta fine (record), EUR 530M TikTok fine
- EU AI Act enforcement: August 2, 2026
- 20 US states with comprehensive privacy laws
- India DPDP full compliance: May 2027

MIT licensed. 282 skills. 21 plugin bundles. 6 LobeHub agents.

Repo: https://github.com/mukul975/Privacy-Data-Protection-Skills

I'm a cybersecurity/AI student at SRH Berlin (4 papers at Electronic Imaging
2026). Also maintain Anthropic-Cybersecurity-Skills (730+ skills).

Would love to hear from practicing DPOs -- what compliance tasks take up the
most time? What would you want AI to handle first?
```

---

## Posting Schedule

| Day | Platform | Subreddit / Channel | Time (CET) |
|-----|----------|---------------------|-------------|
| Day 1 (Launch) | Hacker News | Show HN | 14:00 (8am ET) |
| Day 1 | Reddit | r/privacy | 15:00 |
| Day 1 | Reddit | r/cybersecurity | 15:30 |
| Day 1 | Reddit | r/opensource | 16:00 |
| Day 1 | Reddit | r/gdpr | 16:30 |
| Day 1 | Reddit | r/legaltech | 17:00 |
| Day 1 | Reddit | r/europrivacy | 17:30 |
| Day 1 | Twitter/X | Thread | 15:00 |
| Day 1 | LinkedIn | Post | 09:00 |
| Day 1 | Discord/Slack | Privado.ai, Data Privacy Slack, OWASP | 16:00 |
| Day 1 | GitHub | Discussion in Cybersecurity repo | 14:30 |
| Day 2 | Reddit | r/privacyguides | 15:00 |
| Day 2 | Reddit | r/compliance | 15:30 |
| Day 2 | Reddit | r/dataprotection | 16:00 |

---

## Engagement Playbook

### Responding to Comments

**"How is this different from just using ChatGPT?"**

> Great question. ChatGPT gives general answers. These skills provide structured,
> task-specific workflows grounded in actual legal text. Each skill includes the
> relevant GDPR articles, CCPA sections, or AI Act provisions -- plus automation
> scripts and templates. The difference is between asking "tell me about DPIAs"
> and loading a skill that walks through the entire DPIA process with a risk matrix,
> stakeholder template, and Art. 35 checklist.

**"Is this legal advice?"**

> No. This is a compliance engineering toolkit -- structured workflows, templates,
> and automation scripts. It's meant to help privacy professionals work more
> efficiently, not replace legal counsel. Every skill references the actual legal
> text so practitioners can verify against the source.

**"Why not just use OneTrust/TrustArc/etc.?"**

> Those are solid commercial tools. This is complementary, not competitive. It's
> open-source, free, and agent-native -- designed for teams that want to integrate
> privacy workflows into AI-assisted development pipelines without SaaS lock-in.
> It also covers areas those platforms don't (EU AI Act, AI-specific DPIAs,
> privacy-enhancing technologies).

**"What about hallucination risk?"**

> Each skill is grounded in specific legal references and structured templates.
> The AI agent follows a defined workflow rather than generating answers from
> scratch. The scripts and checklists provide guardrails. That said, this is a
> tool for privacy professionals -- human review is always the final step.

---

## Key Metrics to Track

| Metric | Platform | Target (Week 1) |
|--------|----------|-----------------|
| GitHub stars | GitHub | 100+ |
| Forks | GitHub | 20+ |
| HN points | Hacker News | 50+ |
| Reddit upvotes (total) | Reddit | 200+ |
| LinkedIn impressions | LinkedIn | 5,000+ |
| Twitter impressions | Twitter/X | 10,000+ |
| Issues/PRs opened | GitHub | 5+ |
| Contributors | GitHub | 3+ |

---

*This content package was prepared on 2026-03-15. All statistics verified via web search. Update before posting if launch date is later than March 2026.*
