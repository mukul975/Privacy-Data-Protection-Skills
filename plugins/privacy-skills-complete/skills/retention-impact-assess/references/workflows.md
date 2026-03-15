# Retention Impact Assessment Workflows

## Workflow 1: RIA for New Processing Activity

```
[New Processing Activity Proposed]
         │
         ▼
[Phase 1: Scope and Context]
   - Document processing activity details
   - Identify data subjects, categories, purposes
   - Determine legal basis
         │
         ▼
[Phase 2: Regulatory Requirements Scan]
   - Check tax/fiscal requirements
   - Check company law requirements
   - Check employment law requirements
   - Check sector-specific requirements
   - Check limitation periods
   - Check jurisdictional requirements
         │
         ▼
[Phase 3: Purpose-Based Retention Determination]
   - For each purpose: determine duration of purpose
   - For each purpose: determine minimum necessary retention
   - Identify statutory overrides
   - Calculate resulting retention period (longest justified)
         │
         ▼
[Phase 4: Proportionality Review]
   - Necessity assessment
   - Data minimization over time (staged deletion)
   - Access restriction over time
   - Risk to data subjects
   - Alternatives to retention
         │
         ▼
[Phase 5: Recommendation]
   - Phased retention structure (active → passive → reduced → anonymized → deleted)
   - Retention trigger identification
   - Deletion method specification
         │
         ▼
[Approval]
   - Business Owner sign-off
   - DPO sign-off
   - Legal sign-off (if statutory retention involved)
         │
         ▼
[Implementation]
   - Add to retention schedule
   - Configure automated deletion
   - Update ROPA
   - Update privacy notice
   - Set review date (12 months)
```

## Workflow 2: RIA Triggered by Processing Change

```
[Material Change to Existing Processing Activity]
   (Purpose change, scope change, new data categories, technology change)
         │
         ▼
[Retrieve Original RIA]
         │
         ▼
[Identify What Has Changed]
   ├── New purpose added ──► Assess retention for new purpose
   ├── Purpose removed ──► Can retention period be shortened?
   ├── New data categories ──► Assess retention for new categories
   ├── Scope expanded ──► Assess proportionality of existing period for expanded scope
   └── Technology changed ──► Assess whether new technology enables shorter retention
         │
         ▼
[Update Phases 2-5 as Needed]
         │
         ▼
[Re-Approval if Retention Period Changed]
         │
         ▼
[Update Retention Schedule, ROPA, Privacy Notice]
```

## Workflow 3: Post-Breach RIA Review

```
[Data Breach Involving Over-Retained Data]
         │
         ▼
[Incident Analysis]
   - Was excessive retention a contributing factor to breach scope?
   - How much of the breached data was beyond its retention period?
         │
         ▼
[Targeted RIA Review]
   - Review retention period for affected data category
   - Assess whether shorter period would have reduced breach impact
   - Assess whether staged deletion (minimization over time) was in place
         │
         ▼
[Recommendation]
   ├── Reduce retention period ──► Update schedule; reconfigure systems
   ├── Implement staged deletion ──► Add intermediate deletion/anonymization steps
   ├── Improve enforcement ──► Fix gaps in automated deletion compliance
   └── No change needed ──► Document that retention period was appropriate
         │
         ▼
[Report to DPO and Board]
[Update RIA Register]
```
