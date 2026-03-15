---
name: children-profiling-limits
description: >-
  Implements profiling restrictions for children under GDPR Recital 71,
  Article 22, UK AADC Standard 12, and COPPA. Covers prohibition of
  behavioural advertising to children, recommendation algorithm
  limitations, nudge technique prohibition, and automated decision-making
  safeguards. Keywords: profiling, children, behavioural advertising,
  recommendation algorithm, AADC, automated decision.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: children-data-protection
  tags: "profiling, children, behavioural-advertising, recommendation-algorithm, aadc, automated-decision"
---

# Children's Profiling Restrictions

## Overview

Profiling of children is subject to heightened restrictions under multiple regulatory frameworks. GDPR Recital 71 states that automated decision-making including profiling "should not concern a child." The UK AADC Standard 12 requires profiling to be switched off by default for child users, with exceptions only where the controller can demonstrate a compelling reason and appropriate protective measures. The EU Digital Services Act (DSA) Article 28(2) explicitly prohibits online platforms from presenting targeted advertising based on profiling using the personal data of minors. COPPA prohibits the collection of persistent identifiers from children for behavioural advertising without verifiable parental consent. This skill establishes a comprehensive framework for lawful and ethical data processing that avoids prohibited profiling of children.

## Legal Framework

### GDPR Recital 71 — Children and Automated Decisions

"In any case, such processing should be subject to suitable safeguards, which should include specific information to the data subject and the right to obtain human intervention, to express his or her point of view, to obtain an explanation of the decision reached after such assessment and to challenge the decision. Such measure should not concern a child."

The EDPB interprets "should not concern a child" as a strong presumption against subjecting children to automated decision-making based on profiling that produces legal or similarly significant effects. While "should not" is weaker than "shall not," the EDPB guidance and DPA enforcement practice treat this as an effective prohibition unless exceptional circumstances apply.

### GDPR Article 22 — Automated Individual Decision-Making

Art. 22(1): "The data subject shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her."

For children, this prohibition is reinforced by Recital 71. Exceptions under Art. 22(2) (contract necessity, law, explicit consent) are interpreted narrowly for children:
- **Contract necessity** (Art. 22(2)(a)): Rarely applicable to children; children's contracts are often voidable
- **Law** (Art. 22(2)(b)): May apply for age verification or child safety obligations
- **Explicit consent** (Art. 22(2)(c)): Must be parental consent under Art. 8 for children below the threshold; the child's explicit consent alone is insufficient

### GDPR Article 4(4) — Definition of Profiling

"Profiling means any form of automated processing of personal data consisting of the use of personal data to evaluate certain personal aspects relating to a natural person, in particular to analyse or predict aspects concerning that natural person's performance at work, economic situation, health, personal preferences, interests, reliability, behaviour, location or movements."

### UK AADC Standard 12 — Profiling

"Switch options which use profiling off by default (unless you can demonstrate a compelling reason for profiling to be on by default, taking account of the best interests of the child). Only allow profiling if you have appropriate measures in place to protect the child from any harmful effects (including but not limited to feeding the child content that is detrimental to their health or wellbeing)."

### UK AADC Standard 13 — Nudge Techniques

"Do not use nudge techniques to lead or encourage children to provide unnecessary personal data or weaken or turn off their privacy protections."

### EU Digital Services Act — Article 28(2)

"Providers of online platforms shall not present advertisements on their interface based on profiling as defined in Article 4, point (4), of Regulation (EU) 2016/679, using personal data of the recipient of the service when they are aware with reasonable certainty that the recipient of the service is a minor."

### COPPA — Persistent Identifiers

COPPA defines persistent identifiers as personal information when used for purposes other than support for internal operations. Using persistent identifiers to serve behavioural advertising to children requires verifiable parental consent.

## Types of Profiling and Their Status for Children

### Prohibited Profiling

| Profiling Type | Description | Regulatory Basis | Status |
|---------------|-------------|-----------------|--------|
| **Behavioural advertising** | Using browsing history, interaction patterns, or inferred interests to serve targeted advertisements | DSA Art. 28(2), AADC Std 12, COPPA | Prohibited for children — no exceptions under DSA |
| **Social scoring** | Evaluating a child's social standing, popularity, or reputation based on interactions | AADC Std 5, Recital 71 | Prohibited — detrimental to wellbeing |
| **Emotional profiling** | Inferring emotional state from behavioural signals (typing speed, cursor movement, facial expressions) to adapt content or marketing | AADC Std 5, Art. 9 (if inferring mental health) | Prohibited — exploits developmental vulnerability |
| **Predictive analytics for commercial targeting** | Predicting future purchasing behaviour, susceptibility to marketing, or price sensitivity | AADC Std 5, Recital 71 | Prohibited — commercial exploitation of children |
| **Cross-service behavioural tracking** | Combining data from multiple services or websites to build comprehensive behavioural profiles | AADC Std 9, COPPA, DSA Art. 28(2) | Prohibited — exceeds any legitimate purpose for children |

### Restricted Profiling (Permitted with Safeguards)

| Profiling Type | Description | Conditions for Lawfulness |
|---------------|-------------|--------------------------|
| **Content-based recommendations** | Recommending content based on the characteristics of content the child has engaged with (not the child's personal profile) | Default: OFF. May be enabled with parental consent. Content diversity safeguards required. |
| **Educational adaptive learning** | Adjusting educational content difficulty based on learning progress | Permitted where necessary for the educational purpose. Must not extend to non-educational features. DPO review required. |
| **Safety and moderation profiling** | Detecting grooming, bullying, or abuse patterns in communications | Permitted under legitimate interest (safeguarding). Must be proportionate and subject to DPIA. Must not be used for commercial purposes. |
| **Age-appropriate content filtering** | Using age data to filter inappropriate content | Permitted as necessary for child protection. Must not be used to serve advertising. |

### Permitted Processing (Not Profiling)

| Processing Type | Description | Why It Is Not Profiling |
|----------------|-------------|------------------------|
| **Contextual advertising** | Serving advertisements based on the current page content, not the user's profile | No personal data used for ad selection; based on content context only |
| **Aggregate analytics** | Analysing anonymised, aggregate user patterns to improve the service | No evaluation of individual personal aspects; data is not linked to individual users |
| **A/B testing** | Randomly assigning users to feature variants to test service improvements | Random assignment, not based on personal characteristics |

## Recommendation Algorithm Safeguards

For services that implement content recommendation algorithms for children (where permitted), the following safeguards must be in place:

### Content Diversity Injection

- Recommendation algorithms must include a minimum diversity ratio (e.g., at least 30% of recommended content must be from categories the child has NOT previously engaged with)
- This prevents filter bubbles and content rabbit holes that can be particularly harmful to children's development
- The diversity injection must be documented and periodically reviewed

### Time-Limitation Mechanisms

- Recommendation-driven feeds must include natural stopping points (e.g., "You've been browsing for 20 minutes — time for a break!")
- Autoplay must be disabled by default for children per UK AADC guidance (YouTube implemented this following ICO engagement)
- Infinite scroll must be replaced with paginated content with clear endpoints

### Content Safety Filters

- All recommended content must pass through content safety filters before being presented to children
- Filters must be age-tiered: stricter for younger children, proportionate for teenagers
- Human review for edge cases where automated filtering confidence is low

### Mental Health Circuit Breakers

- If the recommendation algorithm detects engagement patterns associated with harmful content cycles (e.g., repeated engagement with content about self-harm, eating disorders, or extreme body image), the algorithm must:
  1. Stop recommending similar content
  2. Interject wellbeing resources or helpline information
  3. Alert the parent through the parental dashboard (without disclosing specific content details that might violate the child's confidence)

## Nudge Technique Prohibition

### Prohibited Nudge Techniques for Children

| Technique | Description | Why Prohibited |
|-----------|-------------|----------------|
| **Confirmshaming** | "Are you sure you want to miss out?" when declining data collection | Exploits social anxiety and fear of missing out |
| **Reward-for-data** | Offering in-game currency, badges, or rewards in exchange for personal data or weakened privacy settings | Bribes children to surrender privacy; exploits reward-seeking behaviour |
| **Asymmetric choice** | Making the privacy-reducing option larger, brighter, or more prominent than the privacy-protecting option | Manipulates choice architecture to exploit limited decision-making capacity |
| **Hidden opt-out** | Burying the option to decline data collection in sub-menus or requiring multiple clicks | Exploits limited navigation skills and attention span |
| **Social proof** | "95% of users allow notifications!" to pressure acceptance | Exploits conformity bias, which is stronger in children |
| **Urgency/scarcity** | "Enable location sharing now or you'll lose your streak!" | Exploits impulsivity and loss aversion |
| **Default-to-share** | Pre-selecting sharing or public options and requiring the child to actively opt out | Exploits status quo bias and inertia |

### Required Design Patterns

| Pattern | Description | Implementation |
|---------|-------------|---------------|
| **Equal-weight choices** | Accept and reject options must be equally prominent in size, colour, and placement | Both buttons same size, same visual weight, no colour hierarchy |
| **Neutral language** | Choice labels must not favour one option over the other | "Turn on" / "Keep off" — not "Yes, personalise!" / "No, I want a boring experience" |
| **Privacy-first defaults** | The default state must be the most privacy-protective option | All toggles default to OFF for data-intensive features |
| **Friction parity** | The number of clicks to enhance privacy must equal or be fewer than the number to reduce privacy | If enabling a feature takes 1 tap, disabling must take 1 tap or fewer |
| **No dark patterns** | Interface must not use visual tricks, misdirection, or confusing language to influence the child's choice | Regular UX audits with children in the target age group |

## BrightPath Learning Inc. — Profiling Compliance Implementation

### Profiling Status Matrix

| Feature | Profiling Type | Status | Justification |
|---------|---------------|--------|---------------|
| Learning content difficulty adjustment | Educational adaptive learning | ACTIVE (default) | Necessary for educational service delivery; adjusts maths and reading levels based on assessment scores |
| Game recommendations | Content-based | OFF by default | Recommends games based on subject area, not child's behavioural profile; parent can enable |
| Progress reports | Aggregate scoring | ACTIVE (with consent) | Summarises learning outcomes for parent dashboard; no behavioural profiling |
| Advertising | None | NOT PRESENT | BrightPath does not serve advertisements to children |
| Social features | None | NOT PRESENT | No social scoring, popularity metrics, or peer comparison features |
| Communication moderation | Safety profiling | ACTIVE | Automated detection of inappropriate content in pre-approved message templates; DPIA completed |

### Algorithmic Impact Assessment

BrightPath conducts an annual Algorithmic Impact Assessment for its learning content recommendation system:

1. **Purpose test**: Does the algorithm serve the child's educational interests? YES — adjusts content to appropriate difficulty level
2. **Necessity test**: Could the educational purpose be achieved without profiling? NO — adaptive learning requires assessment of current skill level
3. **Proportionality test**: Is the profiling limited to what is necessary? YES — only learning assessment scores are used; no behavioural data, no demographic data beyond age
4. **Harm assessment**: Could the algorithm produce harmful effects? ASSESSED — risk of discouragement if difficulty increases too rapidly; mitigated by gradual progression and positive reinforcement design
5. **Bias audit**: Does the algorithm produce different outcomes based on protected characteristics? TESTED — annual bias audit across age, gender, and language groups; no statistically significant disparities found
6. **Human oversight**: Can a human override the algorithm? YES — parents can manually set content difficulty levels; teachers (in school deployments) can override

## Enforcement Precedents

- **TikTok (DPC Ireland, 2023)**: EUR 345 million fine included findings that TikTok's "For You" algorithmic feed profiled children to serve content, with inadequate safeguards against harmful content amplification, violating GDPR Art. 5(1)(a), 5(1)(c), and 25.
- **Instagram (Meta, DPC Ireland, 2022)**: EUR 405 million fine for failing to restrict profiling and public exposure of children's data, including default public profiles for business accounts used by children aged 13-17.
- **YouTube (FTC, 2019)**: USD 170 million settlement for using persistent identifiers (cookies) to track children's viewing behaviour on child-directed channels and serve behaviourally targeted advertising.
- **TikTok (CNIL France, 2022)**: EUR 5 million fine for making it difficult for users, including children, to refuse tracking cookies — constituting a nudge technique that weakened privacy protections.
- **Fortnite/Epic Games (FTC, 2022)**: USD 275 million for design choices that exposed children to harmful interactions, with dark patterns facilitating in-app purchases by children.

## Common Compliance Failures

1. **Profiling on by default**: Activating recommendation algorithms, personalisation features, or content curation based on behavioural profiling without requiring explicit opt-in
2. **Behavioural advertising to known children**: Serving targeted advertisements based on personal data profiles despite DSA Art. 28(2) prohibition
3. **No algorithmic impact assessment**: Deploying algorithms that affect children without assessing their impact on children's rights, wellbeing, and development
4. **Nudge techniques in consent flows**: Using dark patterns, confirmshaming, or asymmetric choice design to obtain consent for profiling features
5. **Cross-service tracking**: Using persistent identifiers to track children across websites or services for profiling purposes
6. **No content diversity safeguards**: Allowing recommendation algorithms to create filter bubbles or content rabbit holes without diversity injection or time limits

## Integration Points

- **Children's Data Minimisation**: Data minimisation directly limits the data available for profiling — less data collected means less material for profile construction
- **UK AADC Implementation**: AADC Standards 5, 7, 12, and 13 collectively govern profiling, defaults, nudge techniques, and detrimental use
- **Children's Privacy Notice**: The privacy notice must clearly explain what profiling occurs, its effects, and how the child/parent can object
- **GDPR Parental Consent**: Parental consent is required for any profiling of children below the Art. 8 threshold
- **Age-Gating Services**: The age gate result determines which profiling restrictions apply to the user account
