#!/usr/bin/env python3
"""Generate remaining GDPR compliance skill files (skills 11-18)."""
import os

base = "D:/Privacy&Data Protection-Skills/skills/privacy"

skills = [
    ("developing-codes-of-conduct", "Developing Codes of Conduct", "gdpr, codes-of-conduct, article-40, article-41, monitoring-body, industry-code",
     "Guides development of GDPR Article 40-41 codes of conduct for industry sectors including drafting, submission, and monitoring body requirements. Activate when creating industry codes or establishing monitoring bodies. Keywords: codes of conduct, Article 40, Article 41, monitoring body, industry code.",
     "Articles 40-41 provide a framework for associations representing categories of controllers or processors to prepare codes of conduct. Codes specify the application of GDPR to specific sectors, provide practical guidance, and serve as an accountability tool under Art. 24(3).",
     "### GDPR Article 40 -- Codes of Conduct\n- **Art. 40(1)**: Encouragement of codes to contribute to proper GDPR application.\n- **Art. 40(2)**: Codes may cover fair processing, legitimate interests, pseudonymisation, data subject information, children protection, security measures, breach notification, transfers, and dispute resolution.\n- **Art. 40(5)**: Draft codes submitted to supervisory authority for approval.\n- **Art. 40(9)**: Commission may grant general EU validity.\n\n### GDPR Article 41 -- Monitoring of Approved Codes\n- **Art. 41(1)**: Accredited monitoring bodies oversee compliance.\n- **Art. 41(2)**: Bodies must demonstrate independence and expertise.\n- **Art. 41(4)**: Bodies inform supervisory authority of infringements.",
     "- **EDPB Guidelines 1/2019 on Codes of Conduct (adopted 12 February 2019)**: Comprehensive guidance on drafting codes, monitoring bodies, and the approval process.\n- **EU Cloud Code of Conduct (CISPE, 2021)**: First transnational code approved under GDPR Art. 40 for cloud infrastructure service providers."),

    ("managing-one-stop-shop-mechanism", "Managing One-Stop-Shop Mechanism", "gdpr, one-stop-shop, article-56, lead-authority, cross-border, cooperation",
     "Guides the GDPR Article 56 one-stop-shop mechanism for determining lead supervisory authority in cross-border processing. Covers main establishment identification and cooperation. Activate when processing across EU borders. Keywords: one-stop-shop, Article 56, lead authority, cross-border.",
     "Article 56 establishes that the supervisory authority of the main establishment shall be the lead authority for cross-border processing, providing a single point of contact for organisations operating across multiple Member States.",
     "### GDPR Article 56 -- Lead Supervisory Authority\n- **Art. 56(1)**: Authority of the main establishment is competent as lead for cross-border processing.\n- **Art. 56(2)**: Each authority retains competence for local complaints or local-only infringements.\n- **Art. 56(6)**: Lead authority is the sole interlocutor for cross-border matters.\n\n### GDPR Article 4(16) -- Main Establishment\n- Controllers: place of central administration in the Union, unless processing decisions are made elsewhere.\n- Processors: place of central administration in the Union, or where main processing occurs.\n\n### GDPR Articles 60-66 -- Cooperation\n- **Art. 60**: Lead authority cooperates with concerned authorities for consensus.\n- **Art. 65**: EDPB dispute resolution when authorities disagree.",
     "- **EDPB Guidelines 8/2022 on Identifying Lead Authority (adopted 28 March 2023)**: Criteria for determining main establishment and lead authority.\n- **WhatsApp Ireland (DPC, 2021, EUR 225M)**: Landmark cross-border one-stop-shop case with Art. 65 dispute resolution."),

    ("appointing-eu-representative", "Appointing EU Representative", "gdpr, eu-representative, article-27, non-eu-controller, territorial-scope, appointment",
     "Guides appointment of GDPR Article 27 EU representative for non-EU controllers or processors. Covers criteria, responsibilities, and documentation. Activate when a non-EU entity processes EU data. Keywords: EU representative, Article 27, non-EU controller, territorial scope.",
     "Article 27 requires controllers or processors not established in the Union but subject to GDPR under Art. 3(2) to designate a representative in a Member State where affected data subjects are located.",
     "### GDPR Article 27 -- EU Representative\n- **Art. 27(1)**: Non-EU controllers/processors subject to Art. 3(2) must designate a representative in writing.\n- **Art. 27(2)**: Exemptions: occasional processing without large-scale special category data and unlikely risk; public authorities.\n- **Art. 27(3)**: Representative established in a Member State where affected data subjects are located.\n- **Art. 27(4)**: Representative is the contact point for supervisory authorities and data subjects.\n- **Art. 27(5)**: Designation does not affect legal proceedings against the controller/processor itself.\n\n### GDPR Article 3(2) -- Territorial Scope\nGDPR applies to non-EU entities when processing relates to offering goods/services to EU data subjects or monitoring their behaviour within the Union.",
     "- **EDPB Guidelines 3/2018 on Territorial Scope (adopted 12 November 2019)**: When Art. 3(2) applies and when an EU representative must be appointed.\n- **Clearview AI (Multiple DPAs, 2021-2022)**: Non-EU company fined without EU representative by Italian, Greek, French, and UK authorities."),

    ("conducting-gdpr-compliance-gap-analysis", "Conducting GDPR Compliance Gap Analysis", "gdpr, gap-analysis, compliance-assessment, remediation, readiness, maturity",
     "Guides systematic assessment of current state versus GDPR requirements across all chapters with prioritised remediation matrix. Activate when starting compliance programmes or conducting periodic reassessment. Keywords: gap analysis, compliance assessment, remediation matrix, GDPR readiness.",
     "A GDPR compliance gap analysis systematically compares current data protection practices against full GDPR requirements across all chapters, identifying gaps, assigning risk ratings, and producing a prioritised remediation matrix.",
     "### GDPR Chapters Assessed\n- **Chapter II (Art. 5-11)**: Principles -- lawfulness, purpose limitation, minimisation, accuracy, storage limitation, security, accountability.\n- **Chapter III (Art. 12-23)**: Data subject rights -- transparency, access, rectification, erasure, portability, objection.\n- **Chapter IV (Art. 24-43)**: Controller/processor obligations -- responsibility, privacy by design, processors, RoPA, security, breach notification, DPIAs, DPO.\n- **Chapter V (Art. 44-49)**: International transfers -- adequacy, SCCs, BCRs, derogations.",
     "- **EDPB Coordinated Enforcement Actions (2022-2024)**: Focus areas (DPO, cloud, access rights) indicate supervisory priorities for gap analysis weighting.\n- **ICO Accountability Framework Tool**: Structured 10-category self-assessment usable as a gap analysis framework."),

    ("creating-gdpr-remediation-roadmap", "Creating GDPR Remediation Roadmap", "gdpr, remediation, roadmap, implementation-plan, prioritisation, compliance-programme",
     "Guides conversion of gap analysis findings into phased implementation plans with milestones and risk-based prioritisation. Activate when building compliance programmes or allocating privacy budgets. Keywords: remediation roadmap, implementation plan, phased approach, prioritisation.",
     "A remediation roadmap converts gap analysis findings into an actionable, phased implementation plan prioritised by regulatory risk, data subject impact, and organisational capability.",
     "### GDPR Article 24(1) -- Controller Implementation Obligation\nThe controller shall implement appropriate technical and organisational measures to ensure and demonstrate compliance, reviewed and updated where necessary.\n\n### GDPR Article 83(2) -- Fine Calculation Factors\nRelevant mitigating factors: (c) actions taken to mitigate damage; (f) degree of cooperation with supervisory authority. Proactive remediation is a recognised mitigating factor.",
     "- **EDPB Guidelines on Administrative Fines (2017)**: Remediation efforts considered mitigating under Art. 83(2)(c) and (f).\n- **British Airways (ICO, 2020, GBP 20M)**: Post-breach remedial actions cited as mitigating factor in fine reduction."),

    ("performing-gdpr-controller-self-assessment", "Performing GDPR Controller Self-Assessment", "gdpr, self-assessment, controller, questionnaire, scoring, compliance-review",
     "Guides comprehensive controller self-assessment covering GDPR Articles 5-49 with scoring methodology and reporting format. Activate when conducting internal reviews or benchmarking maturity. Keywords: self-assessment, controller assessment, compliance questionnaire, scoring.",
     "A controller self-assessment provides structured internal review of GDPR compliance using a standardised questionnaire with scoring, enabling organisations to identify strengths, weaknesses, and maturity trends.",
     "### GDPR Article 5(2) -- Accountability\nThe controller shall be responsible for, and be able to demonstrate compliance with, the data protection principles.\n\n### GDPR Article 24 -- Controller Responsibility\nControllers must implement appropriate measures to ensure and demonstrate compliance.\n\n### GDPR Article 39(1)(b) -- DPO Monitoring\nThe DPO shall monitor compliance including assignment of responsibilities, awareness-raising, training, and related audits.",
     "- **EDPB Coordinated Enforcement Framework**: Annual enforcement focus areas provide benchmark for self-assessment weighting.\n- **CNIL Compliance Toolkit**: Self-assessment tool covering GDPR requirements with sector-specific modules."),

    ("reviewing-documentation-of-processing", "Reviewing Documentation of Processing", "gdpr, documentation-review, processing-records, completeness, accuracy, audit",
     "Guides systematic review of processing documentation for completeness against GDPR Articles 5, 13-14, 24, 28, and 30. Activate when auditing documentation or preparing for inspections. Keywords: documentation review, processing records, completeness, privacy notices, RoPA.",
     "GDPR compliance depends on comprehensive, accurate, and current documentation. This skill provides methodology for reviewing RoPA, privacy notices, DPAs, DPIAs, consent records, and internal policies for internal consistency and alignment with actual processing.",
     "### GDPR Article 30 -- Records of Processing Activities\nMandatory documentation with specific field requirements for controllers (Art. 30(1)(a)-(g)) and processors (Art. 30(2)(a)-(d)).\n\n### GDPR Articles 13-14 -- Transparency\nPrivacy notices must contain: controller identity, DPO contact, purposes, lawful basis, recipients, transfers, retention, rights, and automated decision-making information.\n\n### GDPR Article 28(3) -- Processor Contracts\nDPAs must contain all eight mandatory elements.\n\n### GDPR Article 24 -- Controller Documentation\nControllers must maintain documentation demonstrating compliance.",
     "- **Romanian DPA (ANSPDCP, 2019)**: Fined Unicredit Bank EUR 130,000 for incomplete processing documentation.\n- **ICO Documentation Guidance**: Documentation must be a living record reflecting current processing."),

    ("developing-gdpr-policy-framework", "Developing GDPR Policy Framework", "gdpr, policy-framework, privacy-policy, procedures, guidelines, documentation",
     "Guides creation of organisational privacy policy hierarchy aligned to GDPR chapters including top-level policy, supporting procedures, operational guidelines, and training materials. Activate when building or updating policy frameworks. Keywords: policy framework, privacy policy, procedures, guidelines, policy hierarchy.",
     "A GDPR policy framework provides the documented governance structure underpinning operational compliance, comprising strategic policies, operational procedures, practical guidelines, and training materials aligned to specific GDPR requirements.",
     "### GDPR Article 24(2) -- Data Protection Policies\nWhere proportionate, controller measures shall include implementation of appropriate data protection policies.\n\n### GDPR Article 32(1)(d) -- Testing and Evaluation\nProcess for regularly testing and evaluating effectiveness of technical and organisational measures.\n\n### GDPR Article 39(1)(b) -- DPO Tasks\nDPO monitors compliance including assignment of responsibilities, awareness-raising, training, and related audits.",
     "- **H&M (Hamburg DPA, 2020, EUR 35.3M)**: Absence of adequate data protection policies contributed to fine severity.\n- **EDPB Guidelines on DPO (2016, revised 2017)**: DPOs should monitor compliance with internal policies and ensure regular reviews."),
]

for (dirname, title, tags, desc, overview, standards_primary, standards_enforcement) in skills:
    d = os.path.join(base, dirname)

    # SKILL.md
    with open(os.path.join(d, "SKILL.md"), "w", encoding="utf-8") as f:
        f.write(f"""---
name: {dirname}
description: >-
  {desc}
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: gdpr-compliance
  tags: "{tags}"
---

# {title}

## Overview

{overview}

## Implementation Approach

### Phase 1: Assessment
1. Review current state against applicable GDPR articles.
2. Identify gaps between current practices and requirements.
3. Classify gaps by severity and regulatory risk.
4. Document the assessment with evidence references.

### Phase 2: Design
1. Design measures to address identified gaps.
2. Align measures with organisational capacity and risk appetite.
3. Obtain DPO and stakeholder review of proposed measures.
4. Create implementation timeline with milestones.

### Phase 3: Implementation
1. Execute the implementation plan according to priority.
2. Document all measures implemented with evidence.
3. Train relevant staff on new procedures and requirements.
4. Validate implementation through testing or review.

### Phase 4: Maintenance
1. Schedule periodic reviews (minimum annual).
2. Monitor for regulatory changes affecting the scope.
3. Update measures in response to audit findings or incidents.
4. Report on compliance status to the governance structure.
""")

    # references/standards.md
    with open(os.path.join(d, "references", "standards.md"), "w", encoding="utf-8") as f:
        f.write(f"""# Standards and Regulatory References

## Primary Legislation

{standards_primary}

## Regulatory Guidance and Enforcement

{standards_enforcement}

## ISO/IEC Standards

- **ISO/IEC 27701:2019**: Privacy Information Management System extending ISO 27001/27002 with privacy-specific controls aligned to GDPR.
- **ISO/IEC 27001:2022**: Information Security Management System providing security foundation for GDPR compliance.
""")

    # references/workflows.md
    with open(os.path.join(d, "references", "workflows.md"), "w", encoding="utf-8") as f:
        f.write(f"""# {title} -- Workflow Reference

## Initiation Workflow

1. Identify the trigger: new compliance programme, periodic review, organisational change, or regulatory development.
2. Define the scope: which GDPR articles, processing activities, and business units are in scope.
3. Assign the assessment lead (typically the DPO or a senior privacy analyst).
4. Establish the timeline and milestones.
5. Notify relevant stakeholders.

## Execution Workflow

1. Gather documentation: policies, procedures, records, contracts, and technical documentation.
2. Conduct interviews with processing owners and key stakeholders.
3. Map current state against each requirement in scope.
4. Classify each requirement as: Compliant, Partially Compliant, Non-Compliant, or Not Applicable.
5. Document evidence for each classification.
6. Produce findings report with prioritised recommendations.

## Review and Approval Workflow

1. DPO reviews findings for accuracy and completeness.
2. Processing owners review findings relevant to their areas.
3. Data Protection Steering Committee reviews and approves the assessment.
4. Remediation actions assigned to owners with deadlines.

## Follow-Up Workflow

1. Track remediation actions through the findings register.
2. Conduct follow-up reviews at defined intervals based on severity.
3. Update compliance status upon remediation completion.
4. Feed findings into the annual DPO report and risk register.
5. Schedule the next periodic review.
""")

    print(f"  Written: {dirname}")

print("All SKILL.md, standards.md, workflows.md for skills 11-18 complete")
