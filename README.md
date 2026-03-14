# Privacy-Engineering-Skills

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Skills: 253+](https://img.shields.io/badge/Skills-253%2B-brightgreen.svg)](#skill-categories)
[![Platforms: 32+](https://img.shields.io/badge/Platforms-32%2B-orange.svg)](#platform-compatibility)
[![Standard: agentskills.io](https://img.shields.io/badge/Standard-agentskills.io-purple.svg)](https://agentskills.io)

An open-source database of **253+ privacy and data protection skills** for AI agents, following the [agentskills.io](https://agentskills.io) open standard. Every skill contains real regulatory citations (exact GDPR articles, CCPA/CPRA sections, LGPD articles, HIPAA rules, DPDP Act sections, NIST Privacy Framework subcategories), working Python scripts, procedural workflows, and filled-in practitioner templates.

Built for privacy engineers, DPOs, compliance teams, and AI agents that need to execute privacy tasks with precision.

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

### Method 3: Browse Online

Browse the [`skills/privacy/`](skills/privacy/) directory on GitHub to explore individual skills.

## Skill Categories

| # | Domain | Skills | Description |
|---|--------|--------|-------------|
| 1 | **GDPR Compliance** | 18 | Arts. 5-84 compliance, accountability, DPA cooperation, certification |
| 2 | **Data Subject Rights** | 15 | DSAR processing, erasure, portability, objection, CCPA/CPRA rights |
| 3 | **Consent Management** | 14 | Valid consent, preference centers, GPC, withdrawal, CMPs |
| 4 | **Privacy Impact Assessment** | 14 | DPIAs, TIAs, AI assessments, NIST PF, PIA methodologies |
| 5 | **Data Breach Response** | 13 | 72-hour notification, risk assessment, forensics, multi-jurisdiction |
| 6 | **Cross-Border Transfers** | 12 | SCCs 2021, BCRs, EU-US DPF, Schrems II TIAs, Art. 49 derogations |
| 7 | **Privacy-by-Design** | 13 | Data minimization, PETs, differential privacy, LINDDUN, ISO 31700 |
| 8 | **Data Classification** | 12 | Personal data identification, Art. 9 special categories, PII detection |
| 9 | **Records of Processing** | 10 | Art. 30 RoPA creation, maintenance, automation, audit |
| 10 | **Cookie Consent Compliance** | 12 | CNIL banners, TCF v2.2, Google Consent Mode v2, ePrivacy |
| 11 | **AI Privacy Governance** | 15 | AI DPIAs, EU AI Act, training data lawfulness, model auditing |
| 12 | **Employee Data Privacy** | 11 | Monitoring DPIAs, biometrics, BYOD, whistleblower protection |
| 13 | **Children's Data Protection** | 10 | GDPR Art. 8, COPPA, UK AADC, age verification, EdTech |
| 14 | **Data Retention & Deletion** | 12 | Retention schedules, secure destruction, litigation holds, NIST 800-88 |
| 15 | **Vendor Privacy Management** | 11 | DPAs, sub-processor management, vendor audits, cloud assessment |
| 16 | **Privacy Engineering** | 14 | NIST PF functions, LINDDUN, differential privacy, PII pipelines |
| 17 | **US State Privacy Laws** | 13 | CCPA/CPRA, VCDPA, CPA, CTDPA, TDPSA, multi-state compliance |
| 18 | **Healthcare Privacy** | 11 | HIPAA Privacy/Security Rules, HITECH, 42 CFR Part 2, telehealth |
| 19 | **Global Privacy Regulations** | 12 | LGPD, PIPL, PIPA, DPDP Act, PDPA, APPI, multi-jurisdiction |
| 20 | **Privacy Audit & Certification** | 11 | ISO 27701, SOC 2 Privacy, APEC CBPR, maturity models |

## How It Works

Skills use a **three-level progressive disclosure** system designed for efficient context management:

1. **Metadata** (~100 tokens) — The `name` and `description` fields in YAML frontmatter are always loaded, enabling agents to discover relevant skills by keyword matching.

2. **Instructions** (< 5,000 tokens) — The full `SKILL.md` body loads when a skill activates. Contains workflow steps, prerequisites, and verification criteria.

3. **Resources** (on demand) — Files in `references/`, `scripts/`, and `assets/` load only when needed. Includes regulatory citations, Python automation scripts, and filled-in practitioner templates.

### Skill Anatomy

```
skill-name/
├── SKILL.md                 # YAML frontmatter + workflow instructions
├── references/
│   ├── standards.md         # Exact regulation citations
│   └── workflows.md         # Deep procedural reference
├── scripts/
│   └── process.py           # Working Python automation
└── assets/
    └── template.md          # Filled-in checklist or report
```

## Platform Compatibility

Skills follow the [agentskills.io](https://agentskills.io) open standard and are compatible with **32+ AI agent platforms**:

| Platform | Platform | Platform |
|----------|----------|----------|
| Claude Code | Cursor | VS Code (Copilot) |
| GitHub Copilot | OpenAI Codex | Gemini CLI |
| Roo Code | Goose | Amp |
| Letta | OpenHands | Junie (JetBrains) |
| Mux (Coder) | Firebender | OpenCode |
| Factory | Piebald | TRAE (ByteDance) |
| Spring AI | Mistral Vibe | Command Code |
| Databricks | Snowflake | Qodo |
| Laravel Boost | Emdash | Ona |
| VT Code | Agentman | Autohand |
| Claude (claude.ai) | — | — |

## Regulatory Coverage

Skills reference **15+ privacy frameworks** with exact article and section citations:

- **GDPR** — Arts. 4-88, Recitals 26-171
- **CCPA/CPRA** — Cal. Civ. Code §1798.100-199
- **LGPD** — Lei 13.709/2018, Arts. 1-65
- **PIPL** — Personal Information Protection Law (China)
- **DPDP Act** — Digital Personal Data Protection Act 2023 (India)
- **HIPAA** — 45 CFR §160-164, HITECH Act
- **ePrivacy Directive** — Art. 5(3), PECR (UK)
- **EU AI Act** — Arts. 6-15, Annex III
- **NIST Privacy Framework** — ID, GV, CT, CM, PR functions
- **ISO 27701** — PIMS extending ISO 27001
- **COPPA** — 16 CFR §312
- **UK AADC** — Age Appropriate Design Code
- **APPI** — Act on Protection of Personal Information (Japan)
- **PIPA** — Personal Information Protection Act (South Korea)
- **PDPA** — Personal Data Protection Act (Thailand, Singapore)

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for:

- Skill submission guidelines
- YAML frontmatter requirements
- Quality checklist
- PR naming conventions

## License

This project is licensed under the **Apache License 2.0** — see the [LICENSE](LICENSE) file for details.

Copyright 2025 Mahipal

---

Built with the [agentskills.io](https://agentskills.io) open standard.
