# HIPAA Research Privacy — Workflows

## Workflow 1: Research PHI Access Pathway Selection

```
Researcher Needs PHI for Research Study
│
├── Step 1: Determine PHI Access Pathway
│   │
│   ├── Can the research be conducted with de-identified data (§164.514(a)-(b))?
│   │   ├── YES → Use de-identified data; no HIPAA restrictions apply
│   │   │         ├── Safe Harbor: remove 18 identifiers (§164.514(b)(2))
│   │   │         └── Expert Determination: engage qualified expert (§164.514(b)(1))
│   │   └── NO → Continue evaluation
│   │
│   ├── Can the research be conducted with a limited data set (§164.514(e))?
│   │   ├── YES → Execute data use agreement; limited data set permitted
│   │   └── NO → Continue evaluation
│   │
│   ├── Will the researcher obtain individual authorization (§164.508)?
│   │   ├── YES → Draft HIPAA-compliant authorization form
│   │   │         ├── Include all required elements per §164.508(c)
│   │   │         ├── Include research-specific elements per §164.508(b)(3)
│   │   │         ├── Combine with informed consent if applicable
│   │   │         └── Obtain signed authorization before PHI access
│   │   └── NO → Continue evaluation
│   │
│   ├── Will the researcher seek IRB/Privacy Board waiver of authorization?
│   │   ├── YES → Proceed to Workflow 2 (IRB Waiver Process)
│   │   └── NO → Continue evaluation
│   │
│   ├── Is this preparatory to research (§164.512(i)(1)(ii))?
│   │   ├── YES → Proceed to Workflow 3 (Preparatory to Research)
│   │   └── NO → Continue evaluation
│   │
│   └── Is this research on decedent information (§164.512(i)(1)(iii))?
│       ├── YES → Proceed to Workflow 4 (Decedent Research)
│       └── NO → No permitted pathway identified; PHI access denied
│
└── Step 2: Document Pathway Selection
    ├── Record selected pathway and rationale
    ├── Maintain documentation per §164.530(j) — 6 years
    └── Notify Privacy Officer of research PHI access
```

## Workflow 2: IRB/Privacy Board Waiver of Authorization

```
Researcher Requests Waiver of HIPAA Authorization
│
├── Step 1: IRB/Privacy Board Application
│   ├── Submit waiver request to IRB or Privacy Board
│   ├── Include in application:
│   │   ├── Description of PHI to be used or disclosed
│   │   ├── Justification that use involves no more than minimal privacy risk
│   │   ├── Plan to protect identifiers from improper use and disclosure
│   │   ├── Plan to destroy identifiers at earliest opportunity (or justification for retention)
│   │   ├── Written assurances against re-use or re-disclosure
│   │   ├── Explanation of why research could not practicably be conducted without waiver
│   │   └── Explanation of why research could not practicably be conducted without access to PHI
│   │
│   └── If seeking alteration (not full waiver):
│       └── Describe specific authorization elements to be altered and justification
│
├── Step 2: IRB/Privacy Board Review
│   ├── Review against all three waiver criteria (§164.512(i)(1)(i)):
│   │   ├── Criterion 1: Minimal risk — adequate protections for identifiers?
│   │   ├── Criterion 2: Could not practicably conduct without waiver?
│   │   └── Criterion 3: Could not practicably conduct without PHI?
│   │
│   ├── Approve, deny, or request modifications
│   │
│   └── If approved:
│       ├── Document approval with required elements per §164.512(i)(2)
│       ├── Statement identifying IRB or Privacy Board
│       ├── Statement that waiver criteria have been satisfied
│       ├── Brief description of PHI for which waiver is approved
│       ├── Signature of IRB chair or Privacy Board chair (or authorized member)
│       └── Date of approval
│
├── Step 3: Covered Entity Verification
│   ├── Privacy Officer reviews waiver documentation
│   ├── Verify all required elements are present per §164.512(i)(2)
│   ├── Confirm the PHI requested matches the waiver scope
│   ├── Apply minimum necessary standard to the disclosure (HITECH §13405(c))
│   └── Approve PHI disclosure
│
└── Step 4: PHI Disclosure and Documentation
    ├── Disclose only the PHI covered by the waiver
    ├── Apply minimum necessary limitation
    ├── Log disclosure for accounting of disclosures (§164.528)
    ├── Retain waiver documentation for 6 years (§164.530(j))
    └── Schedule follow-up to verify identifier destruction per the plan
```

## Workflow 3: Preparatory to Research

```
Researcher Requests PHI Review Preparatory to Research
│
├── Step 1: Obtain Required Representations
│   ├── Researcher provides written representations that:
│   │   ├── (a) Use or disclosure is sought solely to review PHI as necessary
│   │   │     to prepare a research protocol or for similar preparatory purposes
│   │   ├── (b) No PHI will be removed from the covered entity in the course
│   │   │     of the review
│   │   └── (c) PHI for which use or access is sought is necessary for the
│   │         research purposes
│   │
│   └── Representations must be in writing and signed by the researcher
│
├── Step 2: Privacy Officer Review
│   ├── Verify representations are complete and signed
│   ├── Confirm the request is genuinely preparatory (protocol development,
│   │   feasibility assessment, cohort estimation)
│   ├── Confirm no PHI will leave the covered entity
│   │   ├── Physical access on-site: researcher reviews in secure room
│   │   ├── Electronic access: read-only access with no export/download
│   │   └── Aggregate counts permitted (not individual-level data)
│   │
│   └── Approve or deny; document decision
│
├── Step 3: Supervised PHI Review
│   ├── Provide access in controlled environment
│   ├── No copying, photographing, or removing PHI
│   ├── Researcher may record aggregate statistics (counts, means, ranges)
│   ├── Monitor access for compliance with representations
│   └── Time-limited access (defined end date)
│
└── Step 4: Documentation
    ├── Retain written representations for 6 years
    ├── Log access in research PHI access register
    └── No accounting of disclosures required (PHI not disclosed externally)
```

## Workflow 4: Research Authorization Combined with Informed Consent

```
Clinical Trial Requiring HIPAA Authorization and Informed Consent
│
├── Step 1: Determine Dual Requirements
│   ├── Is the study subject to the Common Rule (45 CFR Part 46)?
│   │   ├── YES → Informed consent required (§46.116)
│   │   └── NO → HIPAA authorization only
│   │
│   ├── Is HIPAA authorization required (PHI from covered entity)?
│   │   ├── YES → HIPAA authorization required (§164.508)
│   │   └── NO → Informed consent only
│   │
│   └── If both apply → Dual compliance required
│
├── Step 2: Combined or Separate Documents
│   ├── Option A: Combined document
│   │   ├── Must satisfy ALL elements of both:
│   │   │   ├── Informed consent elements per §46.116
│   │   │   └── HIPAA authorization elements per §164.508(c)
│   │   ├── Authorization portion must be clearly distinguishable
│   │   └── IRB reviews combined document for both requirements
│   │
│   └── Option B: Separate documents
│       ├── Separate informed consent form (per §46.116)
│       ├── Separate HIPAA authorization form (per §164.508)
│       ├── Both must be signed before research commences
│       └── IRB reviews both documents
│
├── Step 3: HIPAA Authorization Elements (§164.508(c))
│   ├── Description of PHI to be used/disclosed
│   ├── Persons authorized to make the use/disclosure (covered entity)
│   ├── Persons authorized to receive the PHI (researchers, sponsors)
│   ├── Purpose: the research study (describe)
│   ├── Expiration date or event ("end of the research study" or "none")
│   ├── Right to revoke authorization in writing
│   ├── Statement that PHI may be re-disclosed and no longer protected by HIPAA
│   ├── Signature and date
│   └── If signed by personal representative: description of authority
│
├── Step 4: Enrollment Process
│   ├── Present consent/authorization to prospective participant
│   ├── Allow adequate time for review and questions
│   ├── Obtain signature on all required documents
│   ├── Provide signed copy to participant
│   └── Retain originals in research file
│
└── Step 5: Revocation Handling
    ├── Participant may revoke authorization at any time in writing
    ├── Revocation does not affect PHI used/disclosed before revocation
    ├── Covered entity may continue to use PHI already collected if:
    │   ├── Necessary to maintain integrity of the research
    │   └── This exception was described in the original authorization
    ├── Document revocation in research and privacy files
    └── Cease further PHI collection/disclosure for that participant
```
