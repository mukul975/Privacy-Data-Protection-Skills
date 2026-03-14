---
name: assessing-third-country-adequacy
description: >-
  Guides assessment of third-country adequacy decisions under GDPR Article 45 for
  international data transfers. Covers the current EC adequacy decisions list,
  adequacy assessment criteria, partial adequacy handling, and monitoring of
  adequacy decision reviews. Keywords: adequacy decision, Article 45, third country,
  adequate protection, EC adequacy list.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: cross-border-transfers
  tags: "adequacy-decision, article-45, third-country-adequacy, ec-adequacy-list, data-transfers"
---

# Assessing Third-Country Adequacy

## Overview

GDPR Article 45 provides that the European Commission may determine that a third country, a territory, or one or more specified sectors within a third country, or an international organisation ensures an adequate level of protection for personal data. Where such an adequacy decision exists, transfers of personal data to the covered country, territory, or sector may take place without any specific authorisation or additional safeguard requirement. This skill guides the assessment of existing adequacy decisions and the handling of partial adequacy coverage.

## Current EC Adequacy Decisions

As of March 2026, the European Commission has adopted adequacy decisions for the following countries and territories:

| Country/Territory | Decision Reference | Date Adopted | Scope | Periodic Review |
|------------------|-------------------|-------------|-------|----------------|
| Andorra | Decision 2010/625/EU | 19 October 2010 | Full country | Ongoing monitoring |
| Argentina | Decision 2003/490/EC | 30 June 2003 | Full country | Ongoing monitoring |
| Canada | Decision 2002/2/EC | 20 December 2001 | Commercial organisations subject to PIPEDA only | Ongoing monitoring |
| Faroe Islands | Decision 2010/146/EU | 5 March 2010 | Full territory | Ongoing monitoring |
| Guernsey | Decision 2003/821/EC | 21 November 2003 | Full territory | Ongoing monitoring |
| Israel | Decision 2011/61/EU | 31 January 2011 | Full country | Ongoing monitoring |
| Isle of Man | Decision 2004/411/EC | 28 April 2004 | Full territory | Ongoing monitoring |
| Japan | Decision (EU) 2019/419 | 23 January 2019 | Commercial sector subject to APPI supplementary rules | Biennial review; first review completed January 2021; second review 2023 |
| Jersey | Decision 2008/393/EC | 8 May 2008 | Full territory | Ongoing monitoring |
| New Zealand | Decision 2013/65/EU | 19 December 2012 | Full country | Ongoing monitoring |
| South Korea | Decision (EU) 2022/254 | 17 December 2021 (effective 2022) | Commercial and public sector subject to PIPA | Biennial review |
| Switzerland | Decision 2000/518/EC | 26 July 2000 | Full country | Ongoing monitoring; assessed under revised FADP effective 1 September 2023 |
| United Kingdom | Decision (EU) 2021/1772 | 28 June 2021 | Full country | Sunset clause: expires 27 June 2025 unless renewed; renewal assessment underway |
| Uruguay | Decision 2012/484/EU | 21 August 2012 | Full country | Ongoing monitoring |
| United States (DPF) | Decision (EU) 2023/1795 | 10 July 2023 | Self-certified organisations under the EU-US DPF only | Annual review; first review October 2024 |

## Adequacy Assessment Criteria (Art. 45(2))

When the Commission assesses the adequacy of the level of protection in a third country, it considers:

### (a) Rule of Law and Human Rights

- Respect for human rights and fundamental freedoms
- General and sectoral legislation, including public security, defence, national security, and criminal law
- Access by public authorities to personal data
- Effective and enforceable data subject rights

### (b) Independent Supervisory Authority

- Existence and effective functioning of one or more independent supervisory authorities with responsibility for ensuring and enforcing data protection rules
- Adequate enforcement powers including the power to investigate, intervene, and impose corrective measures
- Independence from government interference

### (c) International Commitments

- International commitments the third country has entered into, including multilateral and bilateral agreements relating to the protection of personal data
- Binding and enforceable obligations arising from such commitments

## Partial Adequacy Handling

Several adequacy decisions cover only specific sectors or types of organisations within a country. Proper handling of partial adequacy is essential.

### Canada — PIPEDA Partial Adequacy

**Scope**: Only transfers to Canadian organisations subject to the Personal Information Protection and Electronic Documents Act (PIPEDA) are covered by the adequacy decision. Provincial private-sector privacy laws that have been declared substantially similar to PIPEDA by the Governor in Council also fall within scope (e.g., Alberta PIPA, British Columbia PIPA, Quebec Act respecting the protection of personal information in the private sector).

**Not covered**:
- Canadian public sector organisations (federal and provincial government agencies)
- Organisations operating under provincial health information legislation
- Organisations not subject to PIPEDA or substantially similar legislation

**Verification**: Before relying on the Canada adequacy decision, confirm that the specific Canadian recipient is subject to PIPEDA or a substantially similar provincial law.

### Japan — APPI Supplementary Rules

**Scope**: The adequacy decision covers commercial sector entities subject to Japan's Act on the Protection of Personal Information (APPI) and the supplementary rules adopted by the Personal Information Protection Commission (PPC) of Japan specifically for the purpose of the EU adequacy finding.

**Supplementary rules**:
1. Treatment of sensitive data: Japanese operators receiving data from the EU must treat all data received as "requiring special care" regardless of its category under APPI
2. Retention limitation: Data must be deleted when no longer necessary for the purpose of use
3. Onward transfers: Transfers outside Japan require either the data subject's consent or assurance that the recipient country provides equivalent protection
4. Anonymously processed information: Restrictions on the use of anonymised data equivalent to GDPR standards

**Verification**: Confirm the Japanese recipient is subject to APPI and has implemented the supplementary rules.

### United States — DPF Self-Certification

**Scope**: Only transfers to US organisations that have actively self-certified to the DPF with the Department of Commerce and are subject to FTC or DoT jurisdiction.

**Not covered**:
- US government agencies
- Non-certified US organisations
- Organisations subject to regulators other than FTC/DoT (e.g., national banks, telecommunications carriers, insurance companies regulated by state insurance commissioners)

**Verification**: Check dataprivacyframework.gov for active certification status before each transfer.

### South Korea — PIPA Coverage

**Scope**: Covers both commercial and public sector organisations subject to the Personal Information Protection Act (PIPA), as amended in 2023.

**Not covered**: Processing by intelligence and national security agencies exempt from PIPA.

## Adequacy Decision Monitoring

### Periodic Review Obligations

Under Art. 45(3), the Commission must periodically review adequacy decisions at least every four years. Some decisions include more frequent review commitments:

| Decision | Review Frequency | Last Review | Next Review Due |
|----------|-----------------|-------------|-----------------|
| Japan | Biennial | 2023 | 2025 |
| South Korea | Biennial | 2024 | 2026 |
| United States (DPF) | Annual | October 2024 | October 2025 |
| United Kingdom | Before sunset (June 2025) | Ongoing | June 2025 |
| Legacy decisions (Andorra, Argentina, etc.) | At least every 4 years | Various | Varies |

### Monitoring Actions for Organisations

1. **Subscribe to Commission notifications**: Monitor the EC's data protection page and the EDPB's news section for announcements regarding adequacy reviews.
2. **Track legislative changes**: Monitor data protection legislative developments in countries where the organisation relies on adequacy decisions.
3. **UK adequacy sunset**: The UK adequacy decision contains a sunset clause expiring 27 June 2025. If not renewed, organisations must transition UK transfers to SCCs or other mechanisms immediately.
4. **DPF legal challenges**: Monitor CJEU proceedings for any challenge to the DPF adequacy decision.
5. **Maintain backup mechanisms**: For transfers relying on adequacy decisions with upcoming reviews or known risks, maintain executed SCCs as a contingency.

## Practical Verification Workflow

For each transfer relying on an adequacy decision:

1. **Identify the adequacy decision**: Confirm which decision covers the destination country or sector.
2. **Verify scope coverage**: Confirm the specific recipient falls within the scope of the adequacy decision (not a partial adequacy gap).
3. **Verify the decision remains in force**: Check the EC's list of adequacy decisions and any recent amendments, suspensions, or repeals.
4. **Document in the transfer register**: Record the adequacy decision reference, scope coverage verification, and next review date.
5. **Set a monitoring reminder**: Calendar the next periodic review date and any sunset clause deadlines.
6. **Contingency planning**: For decisions with known risks (UK sunset, DPF legal challenges), prepare backup SCCs.
