---
name: managing-multi-jurisdiction-breach-notification
description: >-
  Manages coordinated breach notification across multiple legal jurisdictions
  including EU member states (72-hour GDPR deadline), US state breach notification
  laws (varying timelines from 30 to 90 days), and other international regimes.
  Covers conflict resolution when notification timelines differ, lead supervisory
  authority determination, and parallel notification execution. Keywords:
  multi-jurisdiction, cross-border breach, notification coordination, GDPR, US
  state laws, international breach notification.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-breach-response
  tags: "multi-jurisdiction, cross-border-breach, notification-coordination, gdpr, us-state-laws"
---

# Managing Multi-Jurisdiction Breach Notification

## Overview

When a data breach affects individuals across multiple legal jurisdictions, the controller must navigate overlapping and sometimes conflicting notification requirements. The EU GDPR imposes a 72-hour supervisory authority notification deadline; US state laws impose varying timelines and content requirements; and other jurisdictions (Canada, Australia, Brazil, Japan, South Korea) have their own regimes. This skill provides the framework for coordinated notification across jurisdictions.

## Jurisdiction Mapping — Notification Requirements

### European Union — GDPR (All Member States)

| Element | Requirement |
|---------|------------|
| SA notification timeline | 72 hours from awareness (Art. 33(1)) |
| SA notification threshold | Unless breach is "unlikely to result in a risk" |
| DS notification timeline | Without undue delay when "high risk" (Art. 34(1)) |
| Lead SA determination | One-stop-shop: Art. 56 lead SA based on main establishment |
| Cross-border mechanism | Lead SA notified; other concerned SAs informed via Art. 60 |
| Content requirements | Art. 33(3)(a)-(d) for SA; Art. 34(2) for data subjects |

### United States — State Breach Notification Laws

| State | Timeline | AG Notification | Threshold | Key Differences |
|-------|----------|----------------|-----------|----------------|
| California | Most expedient time possible, no unreasonable delay | Yes, if 500+ CA residents | Name + specified data element | Substitute notice for 500,000+ affected; specific template for health data |
| New York | Most expedient time possible, no unreasonable delay | AG, DFS, DOCS simultaneously | Private information (name + data element) | SHIELD Act: 30-day AG notification for NY residents |
| Texas | 60 days from determination | AG if 250+ TX residents | Name + sensitive personal information | Expanded definition of sensitive data includes biometric identifiers |
| Florida | 30 days from determination | FDLE within 30 days if 500+ | Name + specified data element | One of the shortest statutory deadlines |
| Massachusetts | As soon as practicable | AG + OCABR simultaneously | Name + specified data element | Requires description of remedial services offered |
| Illinois | Most expedient time possible, no unreasonable delay | AG if 500+ IL residents | Name + specified data element | BIPA adds biometric data breach notification requirements |
| Virginia | 60 days from discovery | AG + affected individuals | Name + specified data element | VCDPA adds consumer data rights context |
| Colorado | 30 days from determination | AG within 30 days if 500+ | Name + specified data element | Among the shortest deadlines alongside Florida |
| Pennsylvania | Without unreasonable delay | AG if notifying | Name + specified data element | Broad definition of personal information |
| Washington | 30 days from discovery | AG within 30 days if 500+ | Name + specified data element | Biometric and health data included |

### Other International Jurisdictions

| Jurisdiction | Law | SA Timeline | DS Timeline | Notable |
|-------------|-----|-----------|-----------|---------|
| United Kingdom | UK GDPR + DPA 2018 | 72 hours (ICO) | Without undue delay | Mirrors EU GDPR; ICO is sole SA |
| Canada | PIPEDA + provincial laws | "As soon as feasible" to OPC | "As soon as feasible" | Real risk of significant harm (RROSH) threshold |
| Australia | Privacy Act 1988 (NDB scheme) | 30 days to OAIC | As soon as practicable | "Eligible data breach" = serious harm likely |
| Brazil | LGPD | "Reasonable time" to ANPD | "Reasonable time" | ANPD defines timeframes by regulation |
| Japan | APPI | Promptly to PPC (3-5 days recommended) | Promptly | Mandatory for 1,000+ subjects or sensitive data |
| South Korea | PIPA | Within 72 hours to PIPC | Without delay | Mirrors GDPR timeline |
| Singapore | PDPA | 3 calendar days to PDPC | As soon as practicable | Significant harm or significant scale threshold |

## Conflict Resolution Framework

### Principle 1: Meet the Shortest Deadline First

When notification timelines conflict, always prepare to meet the shortest applicable deadline. This typically means:
- EU/UK GDPR 72-hour deadline drives the primary notification timeline.
- US state notifications are prepared in parallel and dispatched as soon as the statutory requirement is met.
- The 72-hour GDPR notification often satisfies the "without unreasonable delay" standard in most US states.

### Principle 2: Superset Content Approach

Prepare a single core notification document containing the superset of all content requirements across jurisdictions, then adapt for jurisdiction-specific formatting:

| Content Element | GDPR Art. 33(3) | California CC §1798.82 | New York GBL §899-aa | Texas BCC §521.053 |
|----------------|-----------------|----------------------|---------------------|---------------------|
| Nature of breach | Required | Required | Required | Required |
| Data categories affected | Required | Required (specific elements) | Required | Required |
| Data subject count | Required (approximate) | Not required but recommended | Required | Required |
| DPO/contact details | Required | Contact details required | Contact details required | Contact details required |
| Likely consequences | Required | Not explicitly required | Not explicitly required | Not explicitly required |
| Measures taken | Required | Remedial actions required | Remedial actions required | Required |
| Credit monitoring offer | Not required (but common) | Required for SSN/financial | Recommended | Required for SSN |
| SA notification reference | Required | AG notification required | AG notification required | AG notification required |

### Principle 3: Parallel Execution Tracks

Manage notifications through parallel workstreams:

**Track 1: EU/UK GDPR (72-hour priority)**
- Lead SA notification within 72 hours
- Phased notification under Art. 33(4) if investigation is ongoing
- Art. 34 data subject notification within 7 days of high-risk determination

**Track 2: US State Notifications (varies by state)**
- AG notifications for each state where affected residents reside
- Individual notifications per state-specific requirements
- Substitute notice where individual notification is not feasible

**Track 3: Other International Jurisdictions**
- OAIC notification (Australia) within 30 days
- OPC notification (Canada) as soon as feasible
- Other jurisdictions as applicable

## Lead Supervisory Authority Determination

For Stellar Payments Group with main establishment in Berlin, Germany:
- **Lead SA**: Berliner Beauftragte für Datenschutz und Informationsfreiheit
- **Concerned SAs**: Any SA in an EU member state where affected data subjects reside
- **One-stop-shop mechanism**: The lead SA coordinates with concerned SAs under Art. 60
- **Exception**: If the breach relates solely to an establishment in another member state, or substantially affects data subjects only in that state, the local SA may be the competent authority under Art. 56(2)

## Notification Coordination Checklist

### Pre-Notification (Within 24 Hours of Awareness)

- [ ] Determine which jurisdictions are affected based on data subject residency analysis
- [ ] Map applicable notification laws for each jurisdiction
- [ ] Identify the shortest notification deadline and set as primary driver
- [ ] Assign jurisdiction-specific notification leads (EU: DPO; US: General Counsel; APAC: Regional Privacy Manager)
- [ ] Engage external counsel in each jurisdiction as needed

### EU/UK Track (72-Hour Deadline)

- [ ] Identify lead SA and prepare notification form
- [ ] Complete Art. 33(3) content requirements
- [ ] Submit notification to lead SA within 72 hours
- [ ] If cross-border, inform lead SA that multiple member states are affected
- [ ] Prepare Art. 34 data subject notification in languages of affected member states

### US Track (Varies by State)

- [ ] Determine affected residents per state using postal/billing addresses
- [ ] For each state with 500+ affected residents, prepare AG notification
- [ ] Draft individual notification letters per state content requirements
- [ ] Include credit monitoring offer where required (SSN/financial data states)
- [ ] Engage outside US counsel for state-specific compliance review
- [ ] Submit AG notifications per each state's required timeline
- [ ] Dispatch individual notifications per each state's required timeline

### International Track

- [ ] Prepare OAIC notification (Australia) within 30 days
- [ ] Prepare OPC notification (Canada) "as soon as feasible"
- [ ] Assess other jurisdictions (Brazil, Japan, South Korea, Singapore) based on affected populations
- [ ] Engage local counsel for jurisdiction-specific requirements

## Coordination with Law Enforcement

In some jurisdictions, law enforcement authorities may request a delay in data subject notification to avoid prejudicing a criminal investigation:
- **EU**: EDPB Guidelines 9/2022 acknowledge that law enforcement may request delay; the controller should document the request and comply while still notifying the SA within 72 hours.
- **US**: Many state laws explicitly permit delay at law enforcement request. The delay must be documented and notification must proceed promptly upon law enforcement clearance.
- **Best practice**: Always notify the supervisory authority/AG on time even if data subject notification is delayed at law enforcement request.
