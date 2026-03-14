# Privacy-Engineering-Skills

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Skills: 253+](https://img.shields.io/badge/Skills-253%2B-brightgreen.svg)](#skill-categories)
[![Platforms: 32+](https://img.shields.io/badge/Platforms-32%2B-orange.svg)](#platform-compatibility)
[![Standard: agentskills.io](https://img.shields.io/badge/Standard-agentskills.io-purple.svg)](https://agentskills.io)

An open-source database of **253+ privacy and data protection skills** for AI agents, following the [agentskills.io](https://agentskills.io) open standard. Every skill contains real regulatory citations (exact GDPR articles, CCPA/CPRA sections, LGPD articles, HIPAA rules, DPDP Act sections, NIST Privacy Framework subcategories), working Python scripts, procedural workflows, and filled-in templates — no placeholder text anywhere.

Compatible with **32+ AI agent platforms** including Claude Code, Cursor, VS Code Copilot, GitHub Copilot, Gemini CLI, OpenAI Codex, Roo Code, and more.

## Quick Start

### Method 1: Claude Code

```bash
claude /install-skills https://github.com/mukul975/Privacy-Data-Protection-Skills
```

### Method 2: Git Clone

```bash
git clone https://github.com/mukul975/Privacy-Data-Protection-Skills.git
cd Privacy-Data-Protection-Skills
```

### Method 3: Browse

Explore the [`skills/privacy/`](skills/privacy/) directory to find skills by topic.

## Skill Categories

| # | Domain | Skills | Description |
|---|--------|--------|-------------|
| 1 | **GDPR Compliance** | 18 | Articles 5-84 compliance, accountability, lawful basis, DPA cooperation |
| 2 | **Data Subject Rights** | 15 | DSAR processing, erasure, portability, restriction, automated decisions |
| 3 | **Consent Management** | 14 | Valid consent, preference centers, GPC signals, cookie consent, withdrawal |
| 4 | **Privacy Impact Assessment** | 14 | DPIA, Transfer Impact Assessment, AI system PIA, NIST PF IDENTIFY |
| 5 | **Data Breach Response** | 13 | 72-hour notification, risk assessment, forensics, multi-jurisdiction |
| 6 | **Cross-Border Transfers** | 12 | SCCs 2021, BCRs, EU-US DPF, Schrems II TIA, Art. 49 derogations |
| 7 | **Privacy-by-Design** | 13 | Data minimization, differential privacy, PETs, LINDDUN, pseudonymization |
| 8 | **Data Classification** | 12 | Personal data test, special categories, PII detection, data lineage |
| 9 | **Records of Processing** | 10 | Controller/processor RoPA, Art. 30 audits, tool integration, dashboards |
| 10 | **Cookie Consent Compliance** | 12 | CNIL banners, TCF v2.2, Google Consent Mode, ePrivacy, GPC integration |
| 11 | **AI Privacy Governance** | 15 | AI DPIA, training data lawfulness, EU AI Act, model auditing, LLM privacy |
| 12 | **Employee Data Privacy** | 11 | Monitoring DPIA, biometric data, BYOD, whistleblower, remote work |
| 13 | **Children's Data Protection** | 10 | GDPR Art. 8, COPPA, UK AADC, age verification, EdTech privacy |
| 14 | **Data Retention & Deletion** | 12 | Retention schedules, automated deletion, NIST SP 800-88, anonymization |
| 15 | **Vendor Privacy Management** | 11 | Due diligence, DPA drafting, sub-processor management, vendor audits |
| 16 | **Privacy Engineering** | 14 | NIST Privacy Framework, LINDDUN, differential privacy, PII pipelines |
| 17 | **US State Privacy Laws** | 13 | CCPA/CPRA, VCDPA, CPA, CTDPA, TDPSA, multi-state compliance |
| 18 | **Healthcare Privacy** | 11 | HIPAA Privacy/Security Rules, HITECH, 42 CFR Part 2, telehealth |
| 19 | **Global Privacy Regulations** | 12 | LGPD, PIPL, PIPA, DPDP Act, PDPA, APPI, multi-jurisdiction matrix |
| 20 | **Privacy Audit & Certification** | 11 | ISO 27701, SOC 2 Privacy, APEC CBPR, maturity models, DPA inspection |

**Total: 253+ skills**

## How It Works

Skills use progressive disclosure to minimize context usage:

1. **Metadata** (~100 tokens) — `name` and `description` fields loaded at startup for all skills. The agent scans these to find relevant skills for the current task.

2. **Instructions** (< 5,000 tokens) — The full `SKILL.md` body loads when a skill activates. Contains workflow steps, prerequisites, and verification criteria.

3. **Resources** (on demand) — Referenced files in `scripts/`, `references/`, and `assets/` load only when the agent needs them. Keeps context lean.

### Skill Anatomy

```
skill-name/
├── SKILL.md              # YAML frontmatter + workflow instructions
├── references/
│   ├── standards.md      # Exact regulation citations
│   └── workflows.md      # Deep procedural reference
├── scripts/
│   └── process.py        # Working Python helper script
└── assets/
    └── template.md       # Filled-in checklist or report template
```

## Platform Compatibility

Skills work with any agent platform supporting the [agentskills.io](https://agentskills.io) open standard:

| Platform | Platform | Platform |
|----------|----------|----------|
| Claude Code | Cursor | VS Code Copilot |
| GitHub Copilot | Gemini CLI | OpenAI Codex |
| Roo Code | Goose | Amp |
| Letta | OpenHands | Junie |
| Mux | Firebender | OpenCode |
| Factory | Piebald | TRAE |
| Spring AI | Mistral Vibe | Command Code |
| Databricks | Snowflake | Qodo |
| Laravel Boost | Emdash | Ona |
| VT Code | Agentman | Autohand |
| Claude (claude.ai) | Tabnine | |

## Regulatory Coverage

- **European Union**: GDPR, ePrivacy Directive, EU AI Act
- **United States**: CCPA/CPRA, HIPAA, HITECH, COPPA, VCDPA, CPA, CTDPA, TDPSA, OCPA, MTDPA, KPPA
- **Brazil**: LGPD (Lei 13.709/2018)
- **China**: PIPL (Personal Information Protection Law)
- **India**: DPDP Act 2023
- **South Korea**: PIPA
- **Japan**: APPI (2022 amendments)
- **Thailand**: PDPA
- **Singapore**: PDPA
- **Australia**: Privacy Act (2024 amendments)
- **United Kingdom**: UK GDPR, AADC, IDTA
- **Frameworks**: NIST Privacy Framework, ISO 27701, ISO 31700, APEC CBPR, LINDDUN

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for the submission guide, SKILL.md format requirements, and quality checklist.

### Quick Contribution Steps

1. Fork this repository
2. Create a branch: `feat/your-skill-name`
3. Add your skill following the [agentskills.io specification](https://agentskills.io/specification)
4. Submit a pull request

## License

This project is licensed under the [Apache License 2.0](LICENSE).

Copyright 2025 Mahipal

---

Built for the privacy engineering community. Every skill is designed to give AI agents the procedural knowledge needed to handle real-world privacy and data protection tasks with regulatory precision.
