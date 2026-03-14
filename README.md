# Privacy-Engineering-Skills

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Skills: 253+](https://img.shields.io/badge/Skills-253%2B-brightgreen.svg)](#skill-categories)
[![Platforms: 32+](https://img.shields.io/badge/Platforms-32%2B-orange.svg)](#platform-compatibility)
[![Standard: agentskills.io](https://img.shields.io/badge/Standard-agentskills.io-purple.svg)](https://agentskills.io)

An open-source database of **253+ privacy and data protection skills** for AI agents, following the [agentskills.io](https://agentskills.io) open standard. Every skill contains **real regulatory citations** (exact GDPR articles, CCPA/CPRA sections, LGPD articles, HIPAA rules, DPDP Act sections, NIST Privacy Framework subcategories), working Python scripts, procedural workflows, and filled-in practitioner templates — absolutely no placeholder text.

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

Browse the [`skills/privacy/`](skills/privacy/) directory directly on GitHub to explore individual skills.

## Skill Categories

| # | Category | Skills | Description |
|---|----------|--------|-------------|
| 1 | **GDPR Compliance** | 18 | Arts. 5-49 compliance, accountability, lawful basis, DPAs, certifications, gap analysis |
| 2 | **Data Subject Rights** | 15 | DSAR processing, erasure, portability, restriction, objection, CCPA consumer requests |
| 3 | **Consent Management** | 14 | Valid consent, preference centers, GPC signals, withdrawal, record-keeping, CMPs |
| 4 | **Privacy Impact Assessment** | 14 | GDPR DPIAs, transfer impact assessments, AI system PIAs, methodology comparison |
| 5 | **Data Breach Response** | 13 | 72-hour notification, risk assessment, forensics, multi-jurisdiction, HIPAA breach |
| 6 | **Cross-Border Transfers** | 12 | SCCs 2021, BCRs, EU-US DPF, Schrems II TIA, Art. 49 derogations, UK IDTA |
| 7 | **Privacy-by-Design** | 13 | Data minimization, differential privacy, PETs, LINDDUN, ISO 31700, pseudonymization |
| 8 | **Data Classification** | 12 | Personal data test, special categories, PII detection, data lineage, cross-jurisdiction |
| 9 | **Records of Processing** | 10 | Art. 30 controller/processor RoPA, tool integration, automated generation, dashboards |
| 10 | **Cookie Consent** | 12 | Cookie audits, CNIL banners, TCF v2.2, Google Consent Mode v2, GPC integration |
| 11 | **AI Privacy Governance** | 15 | AI DPIAs, training data lawfulness, EU AI Act, model auditing, LLM privacy risks |
| 12 | **Employee Data Privacy** | 11 | Monitoring DPIAs, biometric data, BYOD, health data, whistleblower protection |
| 13 | **Children's Data Protection** | 10 | GDPR Art. 8, COPPA, UK AADC, age verification, EdTech privacy, profiling limits |
| 14 | **Data Retention & Deletion** | 12 | Retention schedules, automated deletion, NIST SP 800-88, litigation holds, anonymization |
| 15 | **Vendor Privacy Management** | 11 | Due diligence, DPA drafting, sub-processor management, vendor audits, cloud assessment |
| 16 | **Privacy Engineering** | 14 | NIST Privacy Framework (all 5 functions), LINDDUN, differential privacy, PII pipelines |
| 17 | **US State Privacy Laws** | 13 | CCPA/CPRA, VCDPA, CPA, CTDPA, TDPSA, OCPA, MTDPA, KPPA, multi-state compliance |
| 18 | **Healthcare Privacy** | 11 | HIPAA Privacy/Security Rules, risk analysis, BAAs, 42 CFR Part 2, telehealth |
| 19 | **Global Privacy Regulations** | 12 | LGPD, PIPL, PIPA, DPDP Act, PDPA, APPI, Australia Privacy Act, multi-jurisdiction |
| 20 | **Privacy Audit & Certification** | 11 | ISO 27701, SOC 2 Privacy, APEC CBPR, EU Code of Conduct, maturity models |

**Total: 253+ skills across 20 privacy domains**

## How It Works

Skills use **progressive disclosure** to efficiently manage agent context:

1. **Metadata** (~100 tokens) — `name` and `description` fields are loaded at startup for all skills, enabling the agent to identify which skill to activate based on the task.

2. **Instructions** (< 5,000 tokens) — The full `SKILL.md` body loads when the skill triggers, providing workflow steps, prerequisites, and verification criteria.

3. **Resources** (on demand) — Scripts in `scripts/`, references in `references/`, and templates in `assets/` load only when the agent needs them, keeping context lean.

### Skill Anatomy

```
skill-name/
├── SKILL.md                 # YAML frontmatter + workflow instructions
├── references/
│   ├── standards.md         # Exact regulation citations
│   └── workflows.md         # Detailed procedural reference
├── scripts/
│   └── process.py           # Working Python helper script
└── assets/
    └── template.md          # Filled-in practitioner template
```

## Platform Compatibility

Skills work with any agent that supports the [agentskills.io](https://agentskills.io) open standard:

| Platform | Platform | Platform |
|----------|----------|----------|
| Claude Code | Cursor | VS Code (Copilot) |
| GitHub Copilot | Gemini CLI | OpenAI Codex |
| Roo Code | Goose | Amp |
| Letta | OpenHands | Junie |
| Mux | Firebender | OpenCode |
| Factory | Piebald | TRAE |
| Spring AI | Mistral Vibe | Command Code |
| Databricks | Snowflake | Qodo |
| Laravel Boost | Emdash | Ona |
| VT Code | Agentman | Autohand |
| Claude (claude.ai) | Piebald | — |

## Regulatory Coverage

| Regulation | Jurisdiction | Skills |
|------------|-------------|--------|
| GDPR | EU/EEA | 100+ |
| CCPA/CPRA | California, US | 20+ |
| HIPAA | United States | 11 |
| EU AI Act | EU/EEA | 15 |
| LGPD | Brazil | 5+ |
| PIPL | China | 5+ |
| DPDP Act | India | 5+ |
| PIPA | South Korea | 5+ |
| PDPA | Thailand/Singapore | 5+ |
| APPI | Japan | 5+ |
| NIST Privacy Framework | United States | 14 |
| ISO 27701 | International | 5+ |
| ePrivacy Directive | EU/EEA | 12 |
| US State Laws (10+) | United States | 13 |

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for:

- Skill submission guidelines and YAML frontmatter format
- Quality checklist and validation instructions
- PR naming conventions

## License

This project is licensed under the Apache License 2.0 — see the [LICENSE](LICENSE) file for details.

Copyright 2025 Mahipal
