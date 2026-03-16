# Privacy & Data Protection Skills for AI Agents

> The first structured, machine-readable privacy skills database for AI agents. 282+ open-source privacy compliance procedures covering GDPR, CCPA, EU AI Act, HIPAA, LGPD, PIPL, and India's DPDP Act — following the [agentskills.io](https://agentskills.io) open standard. Works with Claude Code, GitHub Copilot, OpenAI Codex CLI, Cursor, Gemini CLI, and 26+ AI platforms.

[![GitHub Stars](https://img.shields.io/github/stars/mukul975/Privacy-Data-Protection-Skills?style=social)](https://github.com/mukul975/Privacy-Data-Protection-Skills/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/mukul975/Privacy-Data-Protection-Skills?style=social)](https://github.com/mukul975/Privacy-Data-Protection-Skills/network/members)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/Skills-282+-green.svg)](#skill-categories)
[![agentskills.io](https://img.shields.io/badge/agentskills.io-compatible-purple.svg)](https://agentskills.io)
[![Claude Code Plugin](https://img.shields.io/badge/Claude_Code-Plugin_Marketplace-orange.svg)](#claude-code-plugin-marketplace)

---

## Quick Start

```bash
git clone https://github.com/mukul975/Privacy-Data-Protection-Skills.git
cd Privacy-Data-Protection-Skills/skills/privacy/conducting-gdpr-dpia
cat SKILL.md
```

Or install via Claude Code Plugin Marketplace:
```bash
/plugin marketplace add mukul975/Privacy-Data-Protection-Skills
/plugin install privacy-skills-complete@privacy-data-protection-skills
```

---

## Regulation Coverage

| Jurisdiction | Regulation | Skills | Status |
|:---|:---|:---:|:---:|
| EU | GDPR (Regulation 2016/679) | 50+ | Full |
| EU | EU AI Act (Regulation 2024/1689) | 15+ | Full |
| EU | ePrivacy Directive | 12+ | Full |
| US | CCPA/CPRA | 13+ | Full |
| US | HIPAA Privacy and Security Rules | 11+ | Full |
| US | 13 State Privacy Laws | 13+ | Full |
| Brazil | LGPD | 3+ | Yes |
| China | PIPL | 3+ | Yes |
| India | DPDP Act 2023 | 3+ | Yes |
| Japan | APPI | 3+ | Yes |
| South Korea | PIPA | 3+ | Yes |
| Singapore | PDPA | 3+ | Yes |
| Thailand | PDPA | 3+ | Yes |
| South Africa | POPIA | 3+ | Yes |
| Australia | Privacy Act 1988 | 3+ | Yes |
| Canada | PIPEDA | 3+ | Yes |
| Cross-border | APEC CBPR, SCCs, BCRs, EU-US DPF | 12+ | Full |

---

## Why This Exists

AI agents are increasingly used for privacy compliance tasks but operate with zero structured knowledge of privacy regulations, leading to:

- Hallucinated regulation citations (invented GDPR articles, wrong CFR sections)
- Missed jurisdiction-specific requirements (PIPL data localization, LGPD 10 lawful bases)
- Incorrect breach notification timelines (72h GDPR vs 60d HIPAA vs 3d Singapore)
- Dangerous oversimplification of cross-border transfer mechanisms

Each skill provides structured, verified regulatory knowledge that AI agents load on demand, replacing hallucination with precision.

**Real-world use cases:**
- An AI agent processing a **Data Subject Access Request** across EU and US jurisdictions
- An AI agent conducting a **Privacy Impact Assessment** for an AI system ahead of the EU AI Act August 2026 deadline
- An AI agent evaluating **cross-border data transfer mechanisms** (SCCs, BCRs, adequacy decisions) for a multinational organization

**Disclaimer:** These skills are educational reference materials, not legal advice. Consult qualified legal counsel for compliance decisions.

---

## Skill Categories

| Category | Skills | Example |
|:---|:---:|:---|
| GDPR Compliance | 18 | `gdpr-compliance-audit` |
| Privacy Impact Assessment | 18 | `conducting-gdpr-dpia` |
| Data Subject Rights | 15 | `dsar-processing` |
| AI Privacy Governance | 15 | `ai-dpia` |
| Consent Management | 14 | `gdpr-valid-consent` |
| Privacy Engineering | 14 | `differential-privacy-prod` |
| Privacy by Design | 13 | `implementing-homomorphic-encryption` |
| Data Breach Response | 13 | `breach-72h-notification` |
| US State Privacy Laws | 13 | `ccpa-cpra-compliance` |
| Cross-Border Transfers | 12 | `scc-implementation` |
| Cookie and Consent | 12 | `tcf-v2-implementation` |
| Data Classification | 12 | `pii-detection-pipeline` |
| Data Retention | 12 | `retention-schedule` |
| Global Regulations | 12 | `china-pipl` |
| Vendor Management | 11 | `vendor-risk-scoring` |
| Healthcare Privacy | 11 | `hipaa-risk-analysis` |
| Employee Privacy | 11 | `employee-monitoring-dpia` |
| Privacy Audit | 11 | `iso-27701-pims` |
| Records of Processing | 10 | `controller-ropa-creation` |
| Children's Privacy | 10 | `coppa-compliance` |

---

## How Skills Work

Every skill follows the [agentskills.io](https://agentskills.io) open standard:

```
skills/privacy/conducting-gdpr-dpia/
  SKILL.md              # YAML frontmatter + workflow
  references/
    standards.md        # Regulatory citations, enforcement precedents
    workflows.md        # Step-by-step procedures with timelines
  scripts/
    process.py          # Working Python 3 automation (stdlib only)
  assets/
    template.md         # Filled real-world example
```

SKILL.md format:
```yaml
---
name: conducting-gdpr-dpia
description: >-
  Conducts GDPR Data Protection Impact Assessments under Article 35
  following EDPB WP248rev.01 nine-criteria methodology.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-impact-assessment
  tags: "dpia, gdpr, article-35, risk-assessment, edpb"
---
```

Progressive disclosure: agents load only YAML frontmatter (~30-50 tokens) for relevance matching. Full skill content loads only when needed. References, scripts, and templates load on demand.

---

## Claude Code Plugin Marketplace

This repository is a Claude Code Plugin Marketplace with 21 installable plugins:

```bash
/plugin marketplace add mukul975/Privacy-Data-Protection-Skills
/plugin install privacy-skills-complete@privacy-data-protection-skills
/plugin install gdpr-compliance-skills@privacy-data-protection-skills
/plugin install healthcare-privacy-skills@privacy-data-protection-skills
/plugin install ai-privacy-governance-skills@privacy-data-protection-skills
```

See `.claude-plugin/marketplace.json` for the full plugin catalog.

---

## How This Differs from Awesome-Privacy Lists

| Feature | This Repository | Awesome-Privacy Lists |
|:---|:---|:---|
| Format | Structured YAML + markdown workflows | Curated link directories |
| Machine-readable | Yes, agents load directly | No, human-only browsing |
| Workflows | Step-by-step with verification | Links to external resources |
| Automation | Python scripts per skill | None |
| Templates | Filled real-world examples | None |
| Regulatory citations | Exact article/section references | General descriptions |
| Platform support | 26+ AI platforms | GitHub only |
| Enforcement precedents | Named cases with fine amounts | Rarely included |

---

## Framework Mappings

Skills are mapped to major compliance frameworks for organizations aligning their privacy programs:

| Framework | Document | Coverage |
|:---|:---|:---:|
| NIST Privacy Framework 1.0/1.1 | [`docs/nist-privacy-framework-mapping.md`](docs/nist-privacy-framework-mapping.md) | All 100 subcategories |
| ISO 27701:2019/2025 | [`docs/iso-27701-mapping.md`](docs/iso-27701-mapping.md) | All 49 Annex A+B controls |
| OWASP Top 10 Privacy Risks | [`docs/owasp-privacy-risks-mapping.md`](docs/owasp-privacy-risks-mapping.md) | P1-P10 complete |

---

## Roadmap

- [x] v1.0.0 -- 282 skills across 20 privacy domains
- [x] Claude Code Plugin Marketplace with 21 plugins
- [x] Framework mappings: NIST Privacy Framework, ISO 27701, OWASP Privacy Risks
- [ ] EU AI Act deep skills ahead of August 2026 enforcement
- [ ] India DPDP Act implementation rules (Phase 2: November 2026)
- [ ] Privacy automation workflows for DSAR, DPIA, breach pipelines
- [ ] Multi-language support
- [ ] GitHub Pages documentation site

---

## Part of the AI Agent Skills Ecosystem

| Domain | Skills | Repository |
|:---|:---:|:---|
| Cybersecurity | 730+ | [Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) |
| Privacy and Data Protection | 282+ | This repository |
| More domains coming | -- | Star this repo for updates |

Together: **1,012+ structured skills** across cybersecurity and privacy. One open standard. Every AI platform.

Built by [Mahipal](https://github.com/mukul975) -- M.Sc. Cybersecurity and AI.

---

## Contributing

We welcome contributions from both developers and privacy professionals.

> **No Code Required:** DPOs, privacy lawyers, and GRC analysts can contribute by describing privacy workflows in plain language. Use our issue templates or open a GitHub Issue -- maintainers will convert your description into the agentskills.io format and credit you as a contributor.

**Privacy professionals:**
- [Request a new skill](../../issues/new?template=new-skill-request.md) via GitHub Issues
- [Suggest improvements](../../issues/new?template=skill-improvement.md) to existing skills

**Developers:**
- See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide
- Fork, branch (`feat/skill-name`), PR following the agentskills.io format

---

## Cite This Repository

If you use this skills database in your research or work, please cite it:

```bibtex
@misc{mahipal2026privacyskills,
  author       = {Mahipal},
  title        = {Privacy \& Data Protection Skills for AI Agents},
  year         = {2026},
  publisher    = {GitHub},
  url          = {https://github.com/mukul975/Privacy-Data-Protection-Skills},
  version      = {1.0.0},
  note         = {282+ structured privacy skills following the agentskills.io open standard}
}
```

GitHub also provides a citation button -- click **"Cite this repository"** in the sidebar.

---

## Sponsor

If this project helps your privacy compliance work, consider supporting its development:

[![Sponsor](https://img.shields.io/badge/Sponsor-mukul975-ea4aaa?logo=github-sponsors)](https://github.com/sponsors/mukul975)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy_Me_a_Coffee-mukul975-FFDD00?logo=buy-me-a-coffee)](https://buymeacoffee.com/mukul975)

Your support helps maintain 282+ skills, track regulatory changes, and expand coverage to new jurisdictions and frameworks.

---

## License

Apache 2.0. See [LICENSE](LICENSE) for details.

Copyright 2025-2026 Mahipal
