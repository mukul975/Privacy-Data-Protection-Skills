"""
Privacy-Preserving Record Linkage — Bloom Filter PPRL

Implements Bloom filter encoding, similarity matching, and
threshold optimization for privacy-preserving entity resolution.
"""

import hashlib
import hmac
import math
from dataclasses import dataclass
from typing import Optional
import json


class BloomFilterEncoder:
    """Encode string attributes into Bloom filters for PPRL."""

    def __init__(self, filter_size: int = 1024, num_hashes: int = 30,
                 ngram_size: int = 2, secret_key: bytes = b"default_key"):
        self.filter_size = filter_size
        self.num_hashes = num_hashes
        self.ngram_size = ngram_size
        self.secret_key = secret_key

    def _ngrams(self, value: str) -> list[str]:
        padded = f"_{value}_"
        return [padded[i:i + self.ngram_size] for i in range(len(padded) - self.ngram_size + 1)]

    def _hash_position(self, ngram: str, hash_idx: int) -> int:
        msg = f"{hash_idx}:{ngram}".encode()
        digest = hmac.new(self.secret_key, msg, hashlib.sha256).digest()
        return int.from_bytes(digest[:4], "big") % self.filter_size

    def encode(self, value: str) -> list[int]:
        """Encode a single value into a Bloom filter bit array."""
        bf = [0] * self.filter_size
        normalized = value.strip().lower()
        for ngram in self._ngrams(normalized):
            for h in range(self.num_hashes):
                pos = self._hash_position(ngram, h)
                bf[pos] = 1
        return bf

    def encode_record(self, fields: dict[str, str]) -> list[int]:
        """Encode multiple fields into a composite Bloom filter (CLK)."""
        composite = [0] * self.filter_size
        for field_name, field_value in fields.items():
            if field_value:
                salted = self.secret_key + field_name.encode()
                enc = BloomFilterEncoder(self.filter_size, self.num_hashes, self.ngram_size, salted)
                field_bf = enc.encode(field_value)
                composite = [a | b for a, b in zip(composite, field_bf)]
        return composite


class BloomFilterMatcher:
    """Compare Bloom filter encoded records."""

    @staticmethod
    def dice_coefficient(bf1: list[int], bf2: list[int]) -> float:
        intersection = sum(a & b for a, b in zip(bf1, bf2))
        sum_bits = sum(bf1) + sum(bf2)
        if sum_bits == 0:
            return 0.0
        return 2.0 * intersection / sum_bits

    @staticmethod
    def jaccard(bf1: list[int], bf2: list[int]) -> float:
        intersection = sum(a & b for a, b in zip(bf1, bf2))
        union = sum(a | b for a, b in zip(bf1, bf2))
        if union == 0:
            return 0.0
        return intersection / union

    def find_matches(
        self,
        encodings_a: list[tuple[str, list[int]]],
        encodings_b: list[tuple[str, list[int]]],
        threshold: float = 0.8,
    ) -> list[tuple[str, str, float]]:
        """Find matching pairs above threshold."""
        matches = []
        for id_a, bf_a in encodings_a:
            best_score = 0.0
            best_id = None
            for id_b, bf_b in encodings_b:
                score = self.dice_coefficient(bf_a, bf_b)
                if score > best_score:
                    best_score = score
                    best_id = id_b
            if best_score >= threshold and best_id:
                matches.append((id_a, best_id, round(best_score, 4)))
        return matches


class SecureHashLinker:
    """Exact matching via keyed hashing."""

    def __init__(self, key: bytes):
        self.key = key

    def hash_record(self, *fields: str) -> str:
        normalized = "|".join(f.strip().lower() for f in fields)
        return hmac.new(self.key, normalized.encode(), hashlib.sha256).hexdigest()

    def find_matches(self, hashes_a: dict[str, str], hashes_b: dict[str, str]) -> list[tuple[str, str]]:
        common = set(hashes_a.keys()) & set(hashes_b.keys())
        return [(hashes_a[h], hashes_b[h]) for h in common]


@dataclass
class LinkageReport:
    method: str
    org_a_records: int
    org_b_records: int
    matches_found: int
    threshold: float
    avg_similarity: float


def generate_linkage_report(
    matches: list[tuple[str, str, float]],
    n_a: int, n_b: int, threshold: float, method: str,
) -> dict:
    """Generate a PPRL results report."""
    avg_sim = sum(m[2] for m in matches) / len(matches) if matches else 0
    return {
        "method": method,
        "org_a_records": n_a,
        "org_b_records": n_b,
        "matches_found": len(matches),
        "match_rate_a": f"{len(matches) / n_a * 100:.1f}%" if n_a > 0 else "N/A",
        "threshold": threshold,
        "avg_similarity": round(avg_sim, 4),
        "top_matches": [
            {"id_a": m[0], "id_b": m[1], "similarity": m[2]}
            for m in sorted(matches, key=lambda x: x[2], reverse=True)[:10]
        ],
    }


if __name__ == "__main__":
    key = b"shared_secret_key_2026"
    encoder = BloomFilterEncoder(filter_size=1024, num_hashes=30, secret_key=key)

    # Organization A records
    org_a = [
        ("A001", {"first_name": "john", "last_name": "smith", "dob": "19900115"}),
        ("A002", {"first_name": "maria", "last_name": "garcia", "dob": "19850720"}),
        ("A003", {"first_name": "robert", "last_name": "johnson", "dob": "19781203"}),
    ]

    # Organization B records (with slight variations)
    org_b = [
        ("B001", {"first_name": "jon", "last_name": "smith", "dob": "19900115"}),
        ("B002", {"first_name": "maria", "last_name": "garcia-lopez", "dob": "19850720"}),
        ("B003", {"first_name": "alice", "last_name": "williams", "dob": "19920530"}),
    ]

    enc_a = [(rid, encoder.encode_record(fields)) for rid, fields in org_a]
    enc_b = [(rid, encoder.encode_record(fields)) for rid, fields in org_b]

    matcher = BloomFilterMatcher()
    matches = matcher.find_matches(enc_a, enc_b, threshold=0.7)

    report = generate_linkage_report(matches, len(org_a), len(org_b), 0.7, "bloom_filter_clk")
    print(json.dumps(report, indent=2))
