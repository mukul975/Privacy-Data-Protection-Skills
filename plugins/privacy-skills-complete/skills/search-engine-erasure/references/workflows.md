# Search Engine Erasure Workflows

## Workflow 1: Delisting Request Assessment

```
[Delisting Request Received]
         │
         ▼
[Preliminary Checks]
   ├── Is the data subject identifiable from search results? ──► No ──► Reject
   ├── Is the request against a search engine operator? ──► No ──► Redirect to publisher
   └── Is the requester the data subject (or authorized)? ──► No ──► Reject
         │
         ▼
[Full EDPB 13-Point Assessment]
   ├── Criterion 1: Role in public life
   ├── Criterion 2: Nature of information
   ├── Criterion 3: Accuracy
   ├── Criterion 4: Relevance
   ├── Criterion 5: Age of information
   ├── Criterion 6: Source of information
   ├── Criterion 7: Context of publication
   ├── Criterion 8: Sensitivity
   ├── Criterion 9: Impact on data subject
   ├── Criterion 10: Access context
   ├── Criterion 11: Minor
   ├── Criterion 12: Criminal data
   └── Criterion 13: Legal obligation to index
         │
         ▼
[Balancing Test]
   ├── Privacy rights prevail ──► APPROVE delisting
   ├── Public interest prevails ──► REFUSE (with reasons)
   └── Borderline ──► Consult DPO + Legal; consider partial delisting
         │
         ▼
[Document Assessment and Decision]
```

## Workflow 2: Delisting Request Submission

```
[Decision to Request Delisting]
         │
         ▼
[Identify Target Search Engines]
   ├── Google
   ├── Bing (cascades to Yahoo, DuckDuckGo)
   └── Others (if applicable)
         │
         ▼
[For Each Search Engine]
   │
   ├── Complete delisting request form
   │     - Name, contact, country
   │     - Specific URLs to delist
   │     - Grounds for each URL
   │     - Identity verification
   │
   ├── Submit request
   │
   └── Log submission (date, reference, search engine)
         │
         ▼
[Monitor Responses]
   ├── Approved ──► Verify delisting; log outcome
   ├── Refused ──► Assess escalation options
   ├── Partial ──► Review; resubmit for refused URLs if warranted
   └── No response (6+ months) ──► DPA complaint
```

## Workflow 3: DPA Complaint Escalation

```
[Search Engine Refuses Delisting Request]
         │
         ▼
[Review Refusal Reasoning]
   ├── Reasoning valid ──► Accept refusal; advise data subject
   └── Reasoning disputed ──► Prepare DPA complaint
         │
         ▼
[Identify Lead DPA]
   - Google/Bing: Irish DPC (lead authority)
   - May also complain to local DPA
         │
         ▼
[Prepare Complaint]
   - Original request and supporting evidence
   - Search engine's refusal with reasoning
   - Counter-arguments per EDPB 13-point criteria
   - Impact evidence
         │
         ▼
[Submit Complaint via DPA Online Portal]
         │
         ▼
[Monitor Investigation (6-18 months typical)]
   ├── DPA upholds complaint ──► Search engine must delist
   ├── DPA rejects complaint ──► Consider judicial review
   └── DPA mediates ──► Partial delisting or compromise
```
