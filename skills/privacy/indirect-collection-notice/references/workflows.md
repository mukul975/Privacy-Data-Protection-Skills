# Indirect Collection Information Workflows

## Workflow 1: Timing Determination

```
[Personal Data Received from Third-Party Source]
         │
         ▼
[Record receipt date + source identity]
         │
         ▼
[Determine applicable timing rule]
   │
   ├── [Will data be used to CONTACT the data subject?]
   │     └── Yes ──► Deadline: At or before first communication
   │
   ├── [Will data be DISCLOSED to another recipient?]
   │     └── Yes ──► Deadline: At or before first disclosure
   │
   └── [Neither of the above]
         └── Deadline: Within reasonable period, max 1 month from receipt
         │
         ▼
[Apply EARLIEST of applicable deadlines]
         │
         ▼
[Set notification task with deadline]
```

## Workflow 2: Exemption Assessment

```
[Art. 14 Notification Obligation Identified]
         │
         ▼
[Does an exemption apply?]
   │
   ├── Art. 14(5)(a): Subject already has the information?
   │     └── [Verify: equivalent information received from another source]
   │         [Document: source, date, content of prior notification]
   │
   ├── Art. 14(5)(b): Impossible or disproportionate effort?
   │     └── [Conduct proportionality assessment]
   │         Factors:
   │         - Number of data subjects affected
   │         - Age of the data
   │         - Nature of processing
   │         - Cost of notification vs. impact on subjects
   │         - Available compensatory measures
   │         │
   │         [If exemption claimed:]
   │         - Document the assessment (DPO approved)
   │         - Implement compensatory measures:
   │           * Publish information on website
   │           * Make information available on request
   │
   ├── Art. 14(5)(c): Acquisition required by law?
   │     └── [Cite specific legal provision]
   │
   └── Art. 14(5)(d): Professional secrecy obligation?
         └── [Cite statutory secrecy obligation]
         │
         ▼
[No valid exemption?] ──► Proceed with Art. 14 notification
[Valid exemption?] ──► Document and archive
```

## Workflow 3: Art. 14 Notice Delivery

```
[Art. 14 Notice Prepared]
         │
         ▼
[Email address available?]
   ├── Yes ──► Send Art. 14 notice by email
   │            Include all Art. 14(1)-(2) elements
   │            Record delivery date
   │
   └── No ──► [Postal address available?]
               ├── Yes ──► Send by first-class post
               │            Record dispatch date
               │
               └── No ──► [First communication planned?]
                           ├── Yes ──► Include with first communication
                           └── No ──► [Assess disproportionate effort]
                                       Publish on website as compensatory measure
```
