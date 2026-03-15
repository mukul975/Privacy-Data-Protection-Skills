---
name: uk-aadc-implementation
description: >-
  Implements the UK Age Appropriate Design Code (Children's Code) 15
  standards under the Data Protection Act 2018 Section 123. Covers best
  interests assessment, age-appropriate application, transparency, data
  minimization, geolocation restrictions, and profiling defaults.
  Keywords: AADC, Children's Code, ICO, age appropriate design, UK.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: children-data-protection
  tags: "aadc, childrens-code, ico, age-appropriate-design, uk-gdpr, data-protection"
---

# UK Age Appropriate Design Code Implementation

## Overview

The Age Appropriate Design Code (AADC), also known as the Children's Code, is a statutory code of practice issued by the UK Information Commissioner's Office (ICO) under Section 123 of the Data Protection Act 2018. It came into force on 2 September 2020 with a 12-month transition period ending 2 September 2021. The Code sets out 15 standards of age-appropriate design that information society services (ISS) likely to be accessed by children must conform to. "Children" under the Code means anyone under the age of 18 in the UK. Non-compliance does not directly create criminal liability, but the ICO takes the Code into account when assessing conformance with the UK GDPR and DPA 2018, and violations can result in enforcement action including fines of up to GBP 17.5 million or 4% of annual worldwide turnover.

## Scope — Who Must Comply

The AADC applies to providers of information society services that:

1. **Process personal data**: The service processes the personal data of individual users
2. **Are likely to be accessed by children**: The service is likely to be accessed by users under 18, even if not specifically directed at children. The ICO interprets "likely to be accessed" broadly — if children form any part of the actual or foreseeable user base, the Code applies
3. **Are information society services**: Services normally provided for remuneration, at a distance, by electronic means, and at the individual request of a recipient. Includes apps, games, social media, streaming services, connected toys, news websites, educational platforms, and online marketplaces

### Services NOT in Scope

- Services with no UK users
- Preventive or counselling services offered directly to a child
- Services that can demonstrate children do not and cannot access the service (e.g., authenticated corporate intranets)

## The 15 Standards

### Standard 1: Best Interests of the Child

**Requirement**: The best interests of the child should be a primary consideration when designing and developing online services likely to be accessed by a child.

**Implementation**:
- Conduct a Best Interests Assessment (BIA) documented in writing for each feature or processing activity affecting children
- BIA must consider: the child's physical safety, mental health, developmental needs, educational benefit, privacy interests, and right to play
- Reference the UN Convention on the Rights of the Child (UNCRC) Articles 3, 12, 13, 16, 17, and 31
- Record how children's interests were weighed against commercial interests
- Update BIA when features change or new risks emerge

**BrightPath Learning Inc. Example**: Before launching a "leaderboard" feature comparing children's scores, BrightPath conducted a BIA considering potential psychological pressure and bullying risks. The BIA concluded that public leaderboards were not in children's best interests. BrightPath instead implemented private progress reports visible only to the child and their parent.

### Standard 2: Data Protection Impact Assessments

**Requirement**: Undertake a DPIA for any processing likely to result in a high risk to the rights and freedoms of children, considering the different ages, capacities, and developmental needs of children.

**Implementation**:
- Conduct child-specific DPIAs that assess risk from the perspective of children at different developmental stages (under 5, 5-9, 10-12, 13-15, 16-17)
- Consider risks that adults might tolerate but children cannot (commercial pressure, social exclusion, grooming, exposure to inappropriate content)
- Include children or children's advocates in the DPIA process where possible
- DPIA must address how the service's design affects children's agency and autonomy
- Review DPIA annually and after any significant service change

### Standard 3: Age-Appropriate Application

**Requirement**: Take a risk-based approach to recognising the age of individual users and ensure you effectively apply the standards in this code to child users.

**Implementation**:
- Establish the age of users with a level of certainty proportionate to the risks arising from the data processing
- For high-risk processing: use age verification or estimation technologies with high confidence
- For lower-risk processing: self-declaration may be acceptable if combined with risk-mitigation measures
- Apply different design standards to different age groups where appropriate (pre-literate children, primary school, secondary school, young adults)
- Do not use age information collected for this purpose for any other purpose

### Standard 4: Transparency

**Requirement**: Provide privacy information in a clear, prominent, and age-appropriate manner that is suitable for the audience, including for children who are not the primary users but may still access the service.

**Implementation**:
- Provide a child-friendly version of the privacy notice using language, illustrations, and formats appropriate to each age group
- Use bite-sized, just-in-time notices at the point of data collection rather than relying solely on a single privacy policy page
- For children under 12: use simple vocabulary (maximum Year 5 reading level), illustrations, icons, and interactive elements
- For children 13-17: use plain English at GCSE reading level with practical examples
- Explain what data is collected, why, who sees it, and what the child can do about it
- Make the "so what?" clear — help children understand how data processing affects them in practice

### Standard 5: Detrimental Use of Data

**Requirement**: Do not use children's personal data in ways that have been shown to be detrimental to their wellbeing, or that go against industry codes of practice, other regulatory provisions or Government advice.

**Implementation**:
- Do not use children's data for: behavioural advertising targeting, extensive profiling for commercial purposes, social scoring, emotional manipulation, or dark patterns that exploit developmental vulnerabilities
- Monitor academic research and Government guidance on technology's impact on children's wellbeing
- Maintain a "detrimental use register" documenting processing activities assessed against this standard
- Remove or modify features identified as detrimental following review

### Standard 6: Policies and Community Standards

**Requirement**: Uphold published terms, policies, and community standards, including but not limited to privacy policies, age restriction policies, behaviour rules, and content policies.

**Implementation**:
- Enforce age restrictions consistently — if the service states it is for 13+, actively enforce this
- Apply community standards equally and transparently
- Provide child-accessible reporting mechanisms for policy violations
- Publish and maintain a transparency report on policy enforcement actions

### Standard 7: Default Settings

**Requirement**: Settings must be "high privacy" by default, unless you can demonstrate a compelling reason for a different default, taking account of the best interests of the child.

**Implementation**:
- Profile visibility: default to private or friends-only
- Location sharing: default to off
- Search indexing: default to not indexed by external search engines
- Direct messaging: default to contacts-only or off for younger children
- Personalised advertising: default to off
- Data sharing with third parties: default to off
- Push notifications: default to minimal or off
- Document the compelling reason if any default is not set to highest privacy

### Standard 8: Data Minimisation

**Requirement**: Collect and retain only the minimum amount of personal data needed to provide the elements of the service in which a child is actively and knowingly engaged.

**Implementation**:
- Limit data collection to what is strictly necessary for the specific feature the child is using
- Do not collect data for future use or speculative purposes
- Disable background data collection (microphone, camera, contacts, location) unless actively required for a feature the child has requested
- Implement automated data deletion schedules with short retention periods
- Regularly audit data collection against stated purposes

### Standard 9: Data Sharing

**Requirement**: Do not disclose children's data unless you can demonstrate a compelling reason to do so, taking account of the best interests of the child.

**Implementation**:
- Default to not sharing children's data with third parties
- Where sharing is necessary, document the compelling reason and conduct a BIA
- Contractually require third parties to apply equivalent protections to children's data
- Provide transparent notice to the child and parent about any data sharing
- Maintain a publicly available list of categories of third-party recipients

### Standard 10: Geolocation

**Requirement**: Switch geolocation options off by default (unless you can demonstrate a compelling reason for geolocation to be switched on by default, taking account of the best interests of the child). Provide an obvious sign to the child when location tracking is active. Options which make the child's location visible to others must default to off.

**Implementation**:
- GPS and precise location services: default OFF
- Display a persistent, visible indicator when any location tracking is active (e.g., a pulsing location icon)
- Location visible to others: always default to OFF with no exception
- If location is required for a feature, collect at the lowest precision necessary (city-level rather than street-level)
- Automatically reset location permissions to OFF after each session ends
- Provide parents with the ability to disable location features entirely

**BrightPath Learning Inc. Example**: BrightPath's educational platform does not collect precise geolocation. Country-level location is derived from the IP address (truncated to /16) solely for content localisation (language and curriculum alignment). No location data is shared with third parties or visible to other users. A notice states: "We know which country you're in so we can show you the right lessons. We don't track where you go."

### Standard 11: Parental Controls

**Requirement**: If you provide parental controls, give the child age-appropriate information about this. If your online service allows a parent or carer to monitor their child's online activity or track their location, provide an obvious sign to the child when they are being monitored.

**Implementation**:
- Inform children in age-appropriate language that parental controls exist and what they do
- Display a visible indicator when parental monitoring is active (e.g., an eye icon on the dashboard)
- Balance parental oversight with the child's evolving right to privacy as they mature
- For children 16-17: consider whether parental monitoring is proportionate given the young person's developing autonomy
- Provide children with an age-appropriate way to raise concerns about parental control settings

### Standard 12: Profiling

**Requirement**: Switch options which use profiling off by default (unless you can demonstrate a compelling reason for profiling to be on by default, taking account of the best interests of the child). Only allow profiling if you have appropriate measures in place to protect the child from any harmful effects.

**Implementation**:
- All profiling features: default OFF
- Recommendation algorithms: use content-based (not behavioural) recommendations by default
- Do not use profiling to amplify features that are detrimental to children's wellbeing
- Where profiling is enabled (with consent), implement safeguards: content diversity injection, time limits on algorithmic feeds, mental health circuit-breakers
- Conduct annual impact assessments of profiling on children's wellbeing

### Standard 13: Nudge Techniques

**Requirement**: Do not use nudge techniques to lead or encourage children to provide unnecessary personal data or weaken or turn off their privacy protections.

**Implementation**:
- Do not use dark patterns, confirmshaming, or asymmetric choice architecture to extract consent or data from children
- The "accept all" and "reject all" options must be equally prominent
- Do not offer rewards, in-game currency, or other incentives in exchange for personal data or weakened privacy settings
- Privacy-enhancing choices must be presented with at least equal prominence and ease as privacy-reducing choices
- Test UI/UX designs with children of appropriate ages to identify unintentional nudging

### Standard 14: Connected Toys and Devices

**Requirement**: If you provide a connected toy or device, ensure you include effective tools to enable conformance with this code.

**Implementation**:
- Connected devices must comply with all 15 standards
- Provide clear setup instructions for parents to configure privacy settings
- Default to offline mode; require explicit activation of online features
- Clearly indicate when the device is recording, transmitting, or receiving data (LED indicator, audio cue)
- Provide mechanism to delete all stored data from the device and cloud

### Standard 15: Online Tools

**Requirement**: Provide prominent and accessible tools to help children exercise their data protection rights and report concerns.

**Implementation**:
- Provide child-accessible "privacy centre" with visual, age-appropriate controls
- One-click (or equivalent) mechanisms to: download data, delete data, change privacy settings, report concerns
- Ensure reporting tools do not require providing additional personal data
- Respond to children's requests within the UK GDPR's one-month timeline
- Provide tools that empower children to manage their own privacy as they mature

## ICO Enforcement and Engagement

### Enforcement Actions

- **TikTok (ICO, 2023)**: GBP 12.7 million fine for processing personal data of children under 13 without appropriate parental consent, violating UK GDPR Article 8. The ICO explicitly referenced the AADC in its investigation approach.
- **ICO Engagement with Social Media (2021-2022)**: The ICO wrote to major social media platforms (Instagram, TikTok, YouTube, Snapchat) requiring them to demonstrate AADC compliance. This led to Instagram setting all under-18 accounts to private by default, TikTok disabling direct messaging for under-16s, and YouTube disabling autoplay for children.

### ICO Conformance Assessment

The ICO assesses AADC compliance by examining:
1. Whether the service has conducted a conformance self-assessment
2. Whether DPIAs specifically address risks to children at different developmental stages
3. Whether default settings are genuinely "high privacy"
4. Whether transparency materials are tested with children for comprehension
5. Whether the service monitors compliance and responds to children's complaints

## BrightPath Learning Inc. — AADC Conformance Matrix

| Standard | Conformance Status | Implementation |
|----------|-------------------|----------------|
| 1. Best Interests | Conforming | BIA completed for all features; reviewed quarterly |
| 2. DPIA | Conforming | Child-specific DPIA segmented by age group (5-9, 10-12, 13-15, 16-17) |
| 3. Age-Appropriate Application | Conforming | Age verification via parental account; different UI for under-10 and 10-17 |
| 4. Transparency | Conforming | Illustrated privacy notice for under-12; plain English for 13-17 |
| 5. Detrimental Use | Conforming | No behavioural advertising; no social scoring; no emotional analytics |
| 6. Policies and Community Standards | Conforming | Published community guidelines; child-accessible reporting |
| 7. Default Settings | Conforming | All profiles private; sharing off; push notifications off |
| 8. Data Minimisation | Conforming | Only learning progress and minimal account data collected |
| 9. Data Sharing | Conforming | No third-party data sharing; hosting provider bound by DPA |
| 10. Geolocation | Conforming | GPS off; country-level IP only for content localisation |
| 11. Parental Controls | Conforming | Dashboard with eye icon when monitoring active; child informed |
| 12. Profiling | Conforming | Content-based recommendations only; no behavioural profiling |
| 13. Nudge Techniques | Conforming | No rewards for data; equal-weight accept/reject; no confirmshaming |
| 14. Connected Toys/Devices | N/A | Platform is web and mobile app only; no connected devices |
| 15. Online Tools | Conforming | Child-accessible privacy centre; one-click data download and deletion |

## Integration Points

- **GDPR Parental Consent**: UK GDPR Art. 8 sets the age threshold at 13; AADC applies to all children under 18
- **Age Verification Methods**: AADC Standard 3 requires age-appropriate application with proportionate age verification
- **Children's Privacy Notice**: AADC Standard 4 provides detailed transparency requirements beyond UK GDPR Art. 12-14
- **Children's Data Minimisation**: AADC Standard 8 reinforces GDPR Art. 5(1)(c) with child-specific strictness
- **Children's Profiling Limits**: AADC Standard 12 requires profiling off by default with compelling-reason exceptions
