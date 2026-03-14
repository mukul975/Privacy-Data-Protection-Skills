# HIPAA De-Identification Certification — Template

## Dataset Information

| Field | Value |
|-------|-------|
| Dataset Name | |
| Source System | |
| Purpose of De-Identification | |
| Method | [ ] Safe Harbor [ ] Expert Determination [ ] Limited Data Set |
| Record Count | |
| Date Prepared | |
| Prepared By | |

---

## Safe Harbor Checklist (§164.514(b)(2))

| # | Identifier | Removed | Method | Verified |
|---|-----------|---------|--------|----------|
| 1 | Names | [ ] | | [ ] |
| 2 | Geographic data < state | [ ] | | [ ] |
| 3 | Dates (except year) | [ ] | | [ ] |
| 4 | Telephone numbers | [ ] | | [ ] |
| 5 | Fax numbers | [ ] | | [ ] |
| 6 | Email addresses | [ ] | | [ ] |
| 7 | Social Security numbers | [ ] | | [ ] |
| 8 | Medical record numbers | [ ] | | [ ] |
| 9 | Health plan beneficiary numbers | [ ] | | [ ] |
| 10 | Account numbers | [ ] | | [ ] |
| 11 | Certificate/license numbers | [ ] | | [ ] |
| 12 | Vehicle identifiers | [ ] | | [ ] |
| 13 | Device identifiers | [ ] | | [ ] |
| 14 | Web URLs | [ ] | | [ ] |
| 15 | IP addresses | [ ] | | [ ] |
| 16 | Biometric identifiers | [ ] | | [ ] |
| 17 | Full-face photographs | [ ] | | [ ] |
| 18 | Other unique identifiers | [ ] | | [ ] |

### Additional Safe Harbor Checks
- [ ] 3-digit ZIP codes validated against Census 20,000 population threshold
- [ ] Ages over 89 aggregated to 90+
- [ ] No actual knowledge that remaining information can identify an individual

---

## Quality Assurance

- [ ] Automated identifier scan completed (regex, dictionary matching)
- [ ] Human review sample completed (____% of records)
- [ ] Cross-reference check against source data
- [ ] Statistical uniqueness analysis performed
- [ ] Unstructured text (clinical notes) NER de-identification verified
- [ ] Imaging data DICOM headers stripped and verified

---

## Certification

I certify that this dataset has been de-identified in accordance with 45 CFR §164.514(b) using the method indicated above and that, to the best of my knowledge, the remaining information cannot be used alone or in combination with other reasonably available information to identify an individual.

| Role | Name | Signature | Date |
|------|------|-----------|------|
| De-Identification Analyst | | | |
| Privacy Officer | | | |
| Expert (if expert determination) | | | |
