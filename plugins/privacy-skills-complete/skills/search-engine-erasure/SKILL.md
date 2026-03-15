---
name: search-engine-erasure
description: >-
  Implements the right to be forgotten in search engines under GDPR Article 17 and the
  CJEU Google Spain ruling (C-131/12). Covers delisting request procedures, criteria
  assessment balancing privacy against public interest, and geographic scope determination.
  Activate for right to be forgotten, search delisting, Google Spain, de-indexing queries.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-retention-deletion
  tags: "right-to-be-forgotten, search-engine-delisting, google-spain, de-indexing, gdpr-article-17"
---

# Search Engine Erasure (Right to Be Forgotten)

## Overview

The right to be forgotten in the search engine context refers to the right of individuals to request that search engine operators delist (remove from search results) links to web pages containing personal data about them. This right was established by the CJEU in Google Spain SL v AEPD (Case C-131/12) and subsequently codified in GDPR Article 17. It requires a balancing exercise between the data subject's privacy rights and the public's right to access information. This skill provides the assessment criteria, request procedures, and operational workflows for both data controllers (whose content may be subject to delisting) and organizations assisting data subjects with delisting requests.

## Legal Foundation

### CJEU Case C-131/12 — Google Spain SL v AEPD (13 May 2014)

The Court of Justice of the European Union held that:
1. A search engine operator is a data controller in respect of the processing of personal data that appears on web pages published by third parties.
2. The operator of a search engine is obliged to remove from the list of results displayed following a search made on the basis of a person's name, links to web pages published by third parties and containing information relating to that person, if certain conditions are met.
3. The data subject's rights override, as a rule, the interest of internet users in having access to that information, unless particular reasons (such as the role played by the data subject in public life) justify the interference with the data subject's fundamental rights.

### CJEU Case C-507/17 — Google LLC v CNIL (24 September 2019)

The Court clarified the territorial scope of de-indexing:
1. EU law does not require that de-indexing be carried out on all versions of the search engine globally.
2. The search engine operator must carry out de-indexing on the versions of its search engine corresponding to all EU Member States.
3. The search engine operator must take sufficiently effective measures to prevent or seriously discourage users in the EU from accessing the de-indexed links via non-EU versions of the search engine (geo-blocking).

### GDPR Article 17 — Right to Erasure

Article 17(1) establishes six grounds for erasure. In the search engine context, the most commonly invoked grounds are:
- Art. 17(1)(a): Data no longer necessary for the original purpose
- Art. 17(1)(c): Data subject objects and no overriding legitimate grounds exist
- Art. 17(1)(d): Unlawful processing

Article 17(3) establishes exceptions, particularly:
- Art. 17(3)(a): Freedom of expression and information

### EDPB Guidelines 5/2019 on the Right to Be Forgotten in Search Engine Cases

Adopted 7 July 2020, these guidelines provide 13 criteria for assessing delisting requests.

## Delisting Assessment Criteria

### EDPB 13-Point Assessment Framework

The following criteria must be evaluated when assessing a delisting request. The assessment is a balancing exercise — no single criterion is determinative:

| # | Criterion | Assessment Question | Weight Factors |
|---|-----------|--------------------|----------------|
| 1 | **Role in public life** | Does the data subject play a role in public life? | Public figures (politicians, senior executives, public officials) have reduced expectation of delisting for information related to their public role |
| 2 | **Nature of information** | What type of personal data is involved? | Special category data (Art. 9) weighs heavily toward delisting; criminal conviction data requires careful balancing |
| 3 | **Accuracy of information** | Is the information accurate and up-to-date? | Inaccurate information strongly favours delisting |
| 4 | **Relevance** | Is the information still relevant to the public interest? | Information that was once relevant may become irrelevant over time |
| 5 | **Age of information** | How old is the information? | Older information generally weighs toward delisting, unless there is a continuing public interest |
| 6 | **Source of information** | Who published the original content? | Journalistic sources and official government publications weigh against delisting |
| 7 | **Context of publication** | Was the information published voluntarily by the data subject? | Self-published information may weigh against delisting |
| 8 | **Sensitivity** | How sensitive is the information? | Health data, sexual orientation, political opinions — higher sensitivity favours delisting |
| 9 | **Impact on data subject** | What impact does continued indexing have? | Significant harm (employment, reputation, safety) favours delisting |
| 10 | **Access context** | What is the context in which users access the information via search? | Name-based searches are more intrusive than topic-based searches |
| 11 | **Minor** | Is the data subject a minor (or was the data published when they were a minor)? | GDPR Recital 65: data subjects who were children at the time have a strengthened right to erasure |
| 12 | **Criminal data** | Does the information relate to criminal proceedings? | Spent convictions favour delisting; ongoing proceedings may not; national rehabilitation legislation applies |
| 13 | **Legal obligation** | Is there a legal obligation to index the information? | Court orders, regulatory requirements to maintain public registers |

### Assessment Decision Matrix

```
[Delisting Request Received]
         │
         ▼
[Preliminary Assessment]
   │
   ├── Is the data subject identifiable from the search results? ──► No ──► Reject (no personal data at issue)
   │
   ├── Is the request against a search engine operator? ──► No ──► Redirect to content publisher (separate Art. 17 request)
   │
   └── Yes to both ──► [Full EDPB 13-Point Assessment]
         │
         ▼
[Apply Balancing Test]
   │
   ├── STRONG DELISTING CASE:
   │     - Data subject is a private individual
   │     - Information is inaccurate or outdated
   │     - Information is sensitive (Art. 9 categories)
   │     - Data subject was a minor when information published
   │     - Significant demonstrable harm from continued indexing
   │     - Information was not self-published
   │     ──► APPROVE delisting
   │
   ├── STRONG REFUSAL CASE:
   │     - Data subject is a prominent public figure
   │     - Information relates to their public role
   │     - Information is accurate and current
   │     - Strong public interest in access to the information
   │     - Information published by journalistic source
   │     - Legal obligation to maintain the information
   │     ──► REFUSE delisting (cite specific public interest justification)
   │
   └── BORDERLINE CASE:
         - Mixed factors present
         ──► [Detailed written balancing assessment required]
         ──► [Consider partial delisting or time-limited delisting]
         ──► [Consult DPO and Legal counsel]
```

## Delisting Request Procedures

### Step 1: Submitting Delisting Requests to Search Engines

Each major search engine maintains a dedicated form for delisting requests:

#### Google
- **Form**: Google Search removal request under European privacy law
- **URL path**: Available via Google's support documentation under "Remove personal information"
- **Required information**: Full name, email address, country of residence, specific URLs to delist, explanation of why each URL should be delisted, identity verification
- **Response timeline**: Google typically responds within 3-6 months; complex cases may take longer

#### Microsoft Bing
- **Form**: Request to Block Bing Search Results in Europe
- **Required information**: Full name, email address, country of residence, specific URLs, explanation, identity verification
- **Response timeline**: Typically 3-6 months

#### Other Search Engines
- DuckDuckGo: Does not maintain its own index of web pages; relies primarily on Bing results. A successful Bing delisting will typically cascade.
- Yahoo: Uses Bing's index in most European markets. A successful Bing delisting will typically cascade.

### Step 2: Delisting Request Template for Orion Data Vault Corp Employees/Customers

```
DELISTING REQUEST — SEARCH ENGINE
Organization Support Reference: DELIST-YYYY-NNNN

Data Subject: [Name]
Search Engine: [Google / Bing / Other]
Date of Request: [YYYY-MM-DD]

URLs REQUESTED FOR DELISTING:
1. [Full URL] — Reason: [Specific reason per EDPB criteria]
2. [Full URL] — Reason: [Specific reason per EDPB criteria]

GROUNDS FOR DELISTING (cite applicable Art. 17(1) ground):
□ Art. 17(1)(a) — Data no longer necessary for original purpose
□ Art. 17(1)(c) — Data subject objects; no overriding legitimate grounds
□ Art. 17(1)(d) — Unlawful processing
□ Other: [specify]

SUPPORTING INFORMATION:
- Relationship to Orion Data Vault Corp: [employee/customer/former employee/other]
- Nature of information: [describe what the search results reveal]
- Impact of continued indexing: [describe harm]
- Age of information: [when was the content published?]
- Public role: [any public-facing role that may be relevant?]
- Previous attempts to resolve: [contact with content publisher?]

IDENTITY VERIFICATION:
- [Attach government-issued ID — to be submitted to search engine only]
- [Orion Data Vault Corp can verify employment/customer relationship if needed]
```

### Step 3: Handling Search Engine Responses

| Response | Action |
|----------|--------|
| **Delisting approved** | Verify URLs no longer appear in name-based searches from EU locations; log outcome; notify data subject |
| **Delisting refused** | Review reasoning; assess whether to escalate; advise data subject of right to complain to DPA |
| **Partial delisting** | Review which URLs were accepted/refused; assess remaining URLs; advise data subject |
| **Request for more information** | Provide requested information within 14 days |
| **No response (6+ months)** | Escalate: lodge complaint with relevant DPA |

### Step 4: DPA Complaint Escalation

If a search engine refuses a delisting request, the data subject may complain to the supervisory authority:

1. **Identify the lead DPA**: For Google, the lead authority is the Irish Data Protection Commission (DPC). For Bing, it is the Irish DPC (Microsoft Ireland Operations Ltd).
2. **Prepare complaint**: Include the original request, the search engine's refusal with reasoning, the data subject's counter-arguments per the EDPB 13-point criteria.
3. **Submit complaint**: Via the DPA's online complaint form.
4. **Timeline**: DPA investigations typically take 6-18 months.

## Geographic Scope of Delisting

### EU/EEA Scope (Minimum)

Following C-507/17 (Google v CNIL), delisting must be implemented on:
- All EU/EEA country-specific versions of the search engine (e.g., google.de, google.fr, google.nl, etc.)
- The global version (e.g., google.com) when accessed from within the EU/EEA (geo-blocking)

### Geo-Blocking Requirements

The search engine must implement measures to prevent EU/EEA users from circumventing delisting:
- IP-based geo-blocking on non-EU versions
- GPS-based location verification on mobile devices
- The measures must be "sufficiently effective" but absolute prevention is not required

### Global Delisting (Exceptional Cases)

In exceptional circumstances, a DPA or national court may order global delisting. This remains controversial and is assessed case-by-case. Factors favouring global scope include:
- Safety of the data subject (e.g., stalking, domestic violence)
- Information about a minor
- Manifestly inaccurate or defamatory content

## Interaction with Content Source

Delisting from search results does NOT remove the original content from the source website. For complete erasure:

1. **Contact the content publisher directly**: Submit an Art. 17 erasure request to the website hosting the content.
2. **National defamation/privacy law**: If the content is defamatory or violates privacy law, pursue removal under applicable national law.
3. **Court order**: In severe cases, obtain a court order requiring the publisher to remove the content.
4. **Cache clearing**: After source content is removed, request that search engines clear their cached copies.

## Record Keeping for Delisting Cases

| Record | Retention Period | Purpose |
|--------|-----------------|---------|
| Delisting request and assessment | 3 years from final outcome | Demonstrate compliance with Art. 17 |
| Search engine correspondence | 3 years from final outcome | Evidence of due diligence |
| DPA complaint (if any) | 6 years from final outcome | Legal records |
| Balancing assessment documentation | 3 years from final outcome | Demonstrate EDPB criteria application |
| Outcome verification (screenshots) | 1 year from delisting confirmation | Verify ongoing effectiveness |
