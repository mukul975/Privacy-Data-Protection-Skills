# Privacy-Preserving Record Linkage — Workflows

## Workflow 1: Bloom Filter PPRL
1. **Key Agreement**: Both parties agree on shared HMAC key and encoding parameters
2. **Data Preparation**: Standardize and normalize quasi-identifiers (name, DOB, address)
3. **Bloom Filter Encoding**: Encode records into Bloom filters using keyed hashing
4. **Exchange**: Share encoded Bloom filters (not raw data)
5. **Matching**: Compare Bloom filters using Dice coefficient
6. **Threshold Tuning**: Optimize threshold for precision/recall balance
7. **Verification**: Multi-field verification to reduce false positives
8. **Output**: Deliver matched record ID pairs to both parties

## Workflow 2: Threshold Optimization
1. Generate labeled sample of known matches and non-matches
2. Compute similarity scores for all sample pairs
3. Plot precision-recall curve across threshold values
4. Select threshold based on use case requirements
5. Validate on held-out test set
6. Document chosen threshold and performance metrics

## Workflow 3: Secure Hash Matching
1. Agree on shared key and field ordering
2. Standardize identifier fields identically on both sides
3. Compute HMAC-SHA256 of concatenated fields
4. Exchange hash sets
5. Find intersection of hash sets
6. Return matched record ID pairs
