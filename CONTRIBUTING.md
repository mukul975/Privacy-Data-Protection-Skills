# Contributing to Privacy-Engineering-Skills

Thank you for your interest in contributing to this open-source privacy and data protection skills database. This guide explains how to submit new skills, improve existing ones, and maintain quality standards.

## How to Contribute

### 1. Fork and Clone

```bash
git clone https://github.com/<your-username>/Privacy-Data-Protection-Skills.git
cd Privacy-Data-Protection-Skills
```

### 2. Create a Feature Branch

```bash
git checkout -b feat/your-skill-name
```

Branch naming convention:
- `feat/skill-name` for new skills
- `fix/skill-name` for corrections to existing skills
- `docs/topic` for documentation changes

### 3. Create Your Skill

Each skill lives in its own directory under `skills/privacy/`:

```
skills/privacy/your-skill-name/
  SKILL.md
  references/
    standards.md
    workflows.md
  scripts/
    process.py
  assets/
    template.md
```

### 4. Submit a Pull Request

```bash
git add skills/privacy/your-skill-name/
git commit -m "feat: add your-skill-name skill"
git push origin feat/your-skill-name
```

Open a pull request against the `main` branch with a clear description of the skill and its regulatory basis.

## Skill Format (agentskills.io Standard)

Every `SKILL.md` must begin with YAML frontmatter following the [agentskills.io](https://agentskills.io) open standard:

```yaml
---
name: your-skill-name
description: >-
  A clear, specific description of what this skill does, when to activate it,
  and which regulatory provisions it covers. Include relevant keywords for
  discovery. Maximum 1024 characters.
license: Apache-2.0
metadata:
  author: your-github-username
  version: "1.0"
  domain: privacy
  subdomain: one-of-twenty-subdomains
  tags: "comma, separated, relevant, tags"
---
```

### Frontmatter Rules

| Field | Requirement |
|-------|------------|
| `name` | Lowercase with hyphens, must match parent directory name, max 64 characters |
| `description` | Max 1024 characters, must include activation keywords |
| `license` | Must be `Apache-2.0` |
| `metadata.domain` | Must be `privacy` |
| `metadata.subdomain` | Must be one of the 20 defined subdomains |

### Valid Subdomains

| Subdomain | Description |
|-----------|-------------|
| `gdpr-compliance` | EU General Data Protection Regulation |
| `data-subject-rights` | Individual rights under privacy laws |
| `consent-management` | Consent collection, storage, and lifecycle |
| `privacy-impact-assessment` | DPIAs, PIAs, and risk assessments |
| `data-breach-response` | Breach detection, notification, and remediation |
| `cross-border-transfers` | International data transfer mechanisms |
| `privacy-by-design` | Privacy engineering and architecture |
| `data-classification` | Data discovery, inventory, and classification |
| `records-of-processing` | RoPA and processing activity documentation |
| `cookie-consent-compliance` | Cookie banners, tracking, and ePrivacy |
| `ai-privacy-governance` | AI/ML privacy, DPIA for AI, AI Act |
| `employee-data-privacy` | Workplace monitoring and HR data |
| `children-data-protection` | COPPA, Age-Appropriate Design Code |
| `data-retention-deletion` | Retention schedules and secure deletion |
| `vendor-privacy-management` | Third-party risk and processor oversight |
| `privacy-engineering` | Technical privacy controls and PETs |
| `us-state-privacy-laws` | CCPA/CPRA, state privacy legislation |
| `healthcare-privacy` | HIPAA, health data protection |
| `global-privacy-regulations` | LGPD, PIPL, DPDP Act, POPIA |
| `privacy-audit-certification` | Privacy audits, certifications, and standards |

## Required Folder Structure

Every skill must contain exactly 5 files:

### 1. `SKILL.md` (Required)
- YAML frontmatter as specified above
- Body under 500 lines
- Progressive disclosure: lean SKILL.md with details in references/
- Sections: Overview, key concepts, decision criteria, integration points

### 2. `references/standards.md` (Required)
- Minimum 2 real regulatory citations with article numbers
- Include primary legislation, regulatory guidance, and enforcement precedents
- Use exact article references (e.g., "GDPR Article 35(7)(c)")
- Include publication dates and document identifiers

### 3. `references/workflows.md` (Required)
- Step-by-step procedural guidance
- Organised in numbered phases and steps
- Actionable instructions, not abstract principles
- Decision points with clear criteria

### 4. `scripts/process.py` (Required)
- Syntactically valid Python 3 (must pass `python3 -m py_compile`)
- Functional tool that implements the skill logic
- Includes `if __name__ == "__main__":` block with realistic sample data
- Uses only standard library modules (no external dependencies)
- Produces formatted output when run

### 5. `assets/template.md` (Required)
- Fully completed template using a realistic example organisation
- No empty fields, no placeholder text
- Demonstrates how the skill output looks in practice
- Includes realistic dates, names, findings, and recommendations

## Quality Checklist

Before submitting your pull request, verify:

- [ ] `name` in frontmatter matches the parent directory name exactly
- [ ] `description` is under 1024 characters
- [ ] `SKILL.md` body is under 500 lines
- [ ] `references/standards.md` contains 2+ real regulatory citations
- [ ] `references/workflows.md` has numbered procedural steps
- [ ] `scripts/process.py` passes `python3 -m py_compile`
- [ ] `assets/template.md` is fully filled with realistic data
- [ ] No placeholder text: no `TODO`, `TBD`, `[insert]`, `example.com`, `PLACEHOLDER`
- [ ] No synthetic or fabricated regulatory citations
- [ ] All GDPR article references are accurate
- [ ] Enforcement precedents include real case references and fine amounts

## Review Process

1. **Automated checks**: GitHub Actions validates frontmatter, Python syntax, and placeholder detection
2. **Maintainer review**: A maintainer reviews regulatory accuracy and skill quality
3. **Merge**: Approved PRs are merged to `main` and included in the next release

Reviews typically complete within 5 business days. Maintainers may request changes for regulatory accuracy, formatting consistency, or quality improvements.

## Reporting Issues

- **Regulatory errors**: Open an issue with the `regulatory-accuracy` label
- **Missing skills**: Use the "New Skill Request" issue template
- **Improvements**: Use the "Skill Improvement" issue template
- **Bugs**: Use the "Bug Report" issue template

## Code of Conduct

This project follows the [Contributor Covenant v2.1](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code.
