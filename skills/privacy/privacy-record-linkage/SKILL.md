---
name: privacy-record-linkage
description: >-
  Implement privacy-preserving record linkage across datasets using Bloom filter
  encoding, secure hash matching, threshold tuning for precision and recall,
  and false positive management. Enables entity resolution without exposing
  raw personally identifiable information between parties.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-engineering
  tags: "record-linkage, bloom-filters, entity-resolution, secure-matching, pprl"
---

# Privacy-Preserving Record Linkage

## Overview

Privacy-Preserving Record Linkage (PPRL) enables two or more organizations to identify matching records across their datasets without revealing the underlying personal data to each other. This is critical for healthcare research, fraud detection, national statistics, and cross-organizational analytics where direct data sharing is prohibited by privacy regulations.

## Approach Comparison

| Approach | Privacy Level | Accuracy | Scalability | Communication Cost |
|----------|--------------|----------|-------------|-------------------|
| Bloom Filter Encoding | High | Good (>95% F1) | Very High | Low |
| Secure Hash Matching | Very High | High (exact match only) | Very High | Very Low |
| Secure Multi-Party Computation | Cryptographic | Very High | Medium | High |
| Trusted Third Party | Depends on TTP | Very High | High | Medium |
| Differential Privacy Linkage | Formally private | Moderate | High | Low |

## Bloom Filter-Based PPRL

### How It Works

1. Each organization encodes their quasi-identifiers (name, date of birth, address) into Bloom filters
2. The Bloom filter encoding uses cryptographic hash functions with a shared secret key
3. Encoded Bloom filters are compared using similarity metrics (Dice coefficient, Jaccard)
4. Matching pairs above a threshold are identified as linked records
5. Raw data is never exchanged — only Bloom filter bit arrays

### Bloom Filter Encoding Implementation

```python
"""
Privacy-preserving record linkage using Bloom filter encoding.
Implements the approach described by Schnell, Bachteler, and Reiher (2009).
"""

import hashlib
import hmac
import math
from typing import Optional
import numpy as np


class BloomFilterEncoder:
    """
    Encode string attributes into Bloom filters for privacy-preserving
    record linkage using cryptographic keyed hashing.
    """

    def __init__(
        self,
        filter_size: int = 1024,
        num_hash_functions: int = 30,
        ngram_size: int = 2,
        secret_key: bytes = b""
    ):
        """
        Args:
            filter_size: Number of bits in the Bloom filter
            num_hash_functions: Number of hash functions (k)
            ngram_size: Size of character n-grams (bigrams = 2)
            secret_key: Shared secret key for HMAC hashing
        """
        self.filter_size = filter_size
        self.num_hash_functions = num_hash_functions
        self.ngram_size = ngram_size
        self.secret_key = secret_key

    def _generate_ngrams(self, value: str) -> list[str]:
        """Generate character n-grams from a string value."""
        # Pad the string to handle edge characters
        padded = f"_{value}_"
        return [
            padded[i:i + self.ngram_size]
            for i in range(len(padded) - self.ngram_size + 1)
        ]

    def _hash_ngram(self, ngram: str, hash_index: int) -> int:
        """
        Hash an n-gram using HMAC with the shared key and hash index.
        Returns a bit position in the Bloom filter.
        """
        message = f"{hash_index}:{ngram}".encode("utf-8")
        digest = hmac.new(self.secret_key, message, hashlib.sha256).digest()
        # Convert first 4 bytes to integer and modulo by filter size
        position = int.from_bytes(digest[:4], byteorder="big") % self.filter_size
        return position

    def encode_value(self, value: str) -> np.ndarray:
        """
        Encode a single attribute value into a Bloom filter.

        Args:
            value: The string value to encode (e.g., a name)

        Returns:
            Numpy array of bits (0/1) representing the Bloom filter
        """
        bloom_filter = np.zeros(self.filter_size, dtype=np.uint8)

        # Normalize the input
        normalized = value.strip().lower()

        # Generate n-grams
        ngrams = self._generate_ngrams(normalized)

        # Hash each n-gram with each hash function
        for ngram in ngrams:
            for h in range(self.num_hash_functions):
                position = self._hash_ngram(ngram, h)
                bloom_filter[position] = 1

        return bloom_filter

    def encode_record(self, attributes: dict[str, str]) -> np.ndarray:
        """
        Encode multiple attributes into a single composite Bloom filter
        using Cryptographic Longterm Key (CLK) approach.

        Args:
            attributes: Dict mapping attribute names to values
                       e.g., {"first_name": "John", "last_name": "Smith", "dob": "1990-01-15"}

        Returns:
            Composite Bloom filter as numpy array
        """
        composite = np.zeros(self.filter_size, dtype=np.uint8)

        for attr_name, attr_value in attributes.items():
            if attr_value:
                # Use attribute name as additional salt
                salted_key = self.secret_key + attr_name.encode("utf-8")
                encoder = BloomFilterEncoder(
                    filter_size=self.filter_size,
                    num_hash_functions=self.num_hash_functions,
                    ngram_size=self.ngram_size,
                    secret_key=salted_key
                )
                attr_bf = encoder.encode_value(attr_value)
                composite = np.bitwise_or(composite, attr_bf)

        return composite


class BloomFilterMatcher:
    """
    Compare Bloom filter-encoded records to find matching pairs.
    """

    @staticmethod
    def dice_coefficient(bf1: np.ndarray, bf2: np.ndarray) -> float:
        """
        Calculate the Dice coefficient between two Bloom filters.

        Dice = 2 * |bf1 AND bf2| / (|bf1| + |bf2|)

        Returns a similarity score between 0 and 1.
        """
        intersection = np.sum(np.bitwise_and(bf1, bf2))
        cardinality_sum = np.sum(bf1) + np.sum(bf2)

        if cardinality_sum == 0:
            return 0.0

        return 2.0 * intersection / cardinality_sum

    @staticmethod
    def jaccard_similarity(bf1: np.ndarray, bf2: np.ndarray) -> float:
        """
        Calculate the Jaccard similarity between two Bloom filters.

        Jaccard = |bf1 AND bf2| / |bf1 OR bf2|
        """
        intersection = np.sum(np.bitwise_and(bf1, bf2))
        union = np.sum(np.bitwise_or(bf1, bf2))

        if union == 0:
            return 0.0

        return intersection / union

    def find_matches(
        self,
        encodings_a: list[tuple[str, np.ndarray]],
        encodings_b: list[tuple[str, np.ndarray]],
        threshold: float = 0.8,
        similarity_metric: str = "dice"
    ) -> list[tuple[str, str, float]]:
        """
        Find matching record pairs between two encoded datasets.

        Args:
            encodings_a: List of (record_id, bloom_filter) from organization A
            encodings_b: List of (record_id, bloom_filter) from organization B
            threshold: Minimum similarity score for a match
            similarity_metric: "dice" or "jaccard"

        Returns:
            List of (id_a, id_b, similarity_score) for matching pairs
        """
        metric_fn = (
            self.dice_coefficient if similarity_metric == "dice"
            else self.jaccard_similarity
        )

        matches = []

        for id_a, bf_a in encodings_a:
            best_score = 0.0
            best_id_b = None

            for id_b, bf_b in encodings_b:
                score = metric_fn(bf_a, bf_b)
                if score > best_score:
                    best_score = score
                    best_id_b = id_b

            if best_score >= threshold and best_id_b is not None:
                matches.append((id_a, best_id_b, best_score))

        return matches
```

## Secure Hash Matching

For exact matching scenarios where approximate matching is not needed.

```python
"""
Secure hash-based record linkage for exact matching.
Uses keyed HMAC to prevent rainbow table attacks.
"""

import hashlib
import hmac


class SecureHashLinker:
    """
    Link records across organizations using keyed hash matching.
    Suitable for exact match on standardized identifiers.
    """

    def __init__(self, shared_key: bytes):
        self.shared_key = shared_key

    def hash_identifier(self, *fields: str) -> str:
        """
        Create a keyed hash of concatenated identifier fields.

        Args:
            fields: Identifier fields in standardized order
                    e.g., ("john", "smith", "19900115")

        Returns:
            Hex-encoded HMAC-SHA256 hash
        """
        # Normalize and concatenate fields
        normalized = "|".join(f.strip().lower() for f in fields)

        # Generate keyed hash
        digest = hmac.new(
            self.shared_key,
            normalized.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

        return digest

    def hash_dataset(
        self,
        records: list[dict],
        id_field: str,
        linkage_fields: list[str]
    ) -> dict[str, str]:
        """
        Hash all records in a dataset for linkage.

        Returns mapping of hash -> record_id.
        """
        hash_map = {}

        for record in records:
            fields = [str(record.get(f, "")) for f in linkage_fields]
            record_hash = self.hash_identifier(*fields)
            hash_map[record_hash] = record[id_field]

        return hash_map

    @staticmethod
    def find_exact_matches(
        hashes_a: dict[str, str],
        hashes_b: dict[str, str]
    ) -> list[tuple[str, str]]:
        """
        Find exact matches between two hash maps.

        Returns list of (id_a, id_b) pairs.
        """
        common_hashes = set(hashes_a.keys()) & set(hashes_b.keys())
        return [(hashes_a[h], hashes_b[h]) for h in common_hashes]
```

## Threshold Tuning

### Methodology

| Threshold Range | Precision | Recall | Use Case |
|----------------|-----------|--------|----------|
| 0.90 - 1.00 | Very High | Low | High-stakes decisions (medical records) |
| 0.80 - 0.90 | High | Medium | Standard record linkage |
| 0.70 - 0.80 | Medium | High | Exploratory analysis, broad matching |
| 0.60 - 0.70 | Low | Very High | Candidate generation (with manual review) |

### Optimal Threshold Selection Process

1. **Generate labeled pairs**: Create a sample of known matches and non-matches
2. **Compute similarity scores**: Calculate Dice/Jaccard for all pairs in the sample
3. **Plot precision-recall curve**: Sweep threshold from 0 to 1
4. **Select threshold**: Choose based on acceptable false positive rate for the use case
5. **Validate**: Test on held-out labeled data

### False Positive Management

```python
"""
Post-linkage false positive reduction through multi-stage verification.
"""


class FalsePositiveManager:
    """
    Reduce false positive matches through additional verification stages
    without revealing raw data between parties.
    """

    def __init__(self, primary_threshold: float = 0.8, verification_threshold: float = 0.9):
        self.primary_threshold = primary_threshold
        self.verification_threshold = verification_threshold

    def multi_field_verification(
        self,
        candidate_pairs: list[tuple[str, str, float]],
        secondary_encodings_a: dict[str, dict[str, np.ndarray]],
        secondary_encodings_b: dict[str, dict[str, np.ndarray]],
        matcher: BloomFilterMatcher
    ) -> list[tuple[str, str, float, bool]]:
        """
        Verify candidate matches using additional encoded fields.

        Args:
            candidate_pairs: (id_a, id_b, primary_score) from initial matching
            secondary_encodings_a: {record_id: {field: bloom_filter}} from org A
            secondary_encodings_b: {record_id: {field: bloom_filter}} from org B

        Returns:
            (id_a, id_b, composite_score, verified) for each candidate
        """
        verified_pairs = []

        for id_a, id_b, primary_score in candidate_pairs:
            secondary_scores = []

            fields_a = secondary_encodings_a.get(id_a, {})
            fields_b = secondary_encodings_b.get(id_b, {})

            common_fields = set(fields_a.keys()) & set(fields_b.keys())

            for field_name in common_fields:
                score = matcher.dice_coefficient(
                    fields_a[field_name],
                    fields_b[field_name]
                )
                secondary_scores.append(score)

            if secondary_scores:
                avg_secondary = sum(secondary_scores) / len(secondary_scores)
                composite = 0.6 * primary_score + 0.4 * avg_secondary
                verified = composite >= self.verification_threshold
            else:
                composite = primary_score
                verified = primary_score >= self.verification_threshold

            verified_pairs.append((id_a, id_b, composite, verified))

        return verified_pairs
```

## Security Considerations

| Attack | Description | Mitigation |
|--------|-------------|------------|
| Frequency analysis | Analyzing bit patterns to infer common values | Use composite Bloom filters (CLK), add noise bits |
| Dictionary attack | Pre-computing Bloom filters for known values | Use strong shared secret keys, rotate keys periodically |
| Bit pattern cryptanalysis | Exploiting structure in Bloom filter bit patterns | Sufficient filter size (>= 1024), adequate hash functions (>= 20) |
| Collision exploitation | Deliberately crafting records to match target hashes | HMAC-based hashing, input validation |

## References

- Schnell, R., Bachteler, T., and Reiher, J. "Privacy-Preserving Record Linkage Using Bloom Filters." BMC Medical Informatics and Decision Making, 9(1):41, 2009.
- Vatsalan, D., Christen, P., and Verykios, V.S. "A Taxonomy of Privacy-Preserving Record Linkage Techniques." Information Systems, 38(6):946-969, 2013.
- Randall, S.M. et al. "Privacy-Preserving Record Linkage on Large Real World Datasets." Journal of Biomedical Informatics, 50:205-212, 2014.
- AIHW (Australian Institute of Health and Welfare) PPRL Implementation Guide
- Christen, P. "Data Matching: Concepts and Techniques for Record Linkage, Entity Resolution, and Duplicate Detection." Springer, 2012.
