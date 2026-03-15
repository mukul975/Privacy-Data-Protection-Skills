"""
TCF v2.2 TC String Decoder and Validator

Decodes IAB Transparency and Consent Framework TC Strings and validates
them against the GVL and publisher requirements.

Requirements:
    pip install requests
"""

import base64
import json
import os
import struct
from datetime import datetime, timezone, timedelta
from typing import Optional

try:
    import requests
except ImportError:
    print("Required packages not installed. Run: pip install requests")
    raise

# GVL endpoint
GVL_URL = "https://vendor-list.consensu.org/v3/vendor-list.json"


class TCStringDecoder:
    """Decodes IAB TCF v2.2 TC Strings."""

    def __init__(self, tc_string: str):
        self.tc_string = tc_string
        self.bits = self._decode_base64url_to_bits(tc_string)
        self.position = 0
        self.decoded = {}

    def _decode_base64url_to_bits(self, encoded: str) -> str:
        """Convert base64url-encoded TC String to binary bit string."""
        # Add padding if needed
        padding = 4 - len(encoded) % 4
        if padding != 4:
            encoded += "=" * padding

        # Replace base64url characters
        encoded = encoded.replace("-", "+").replace("_", "/")

        try:
            decoded_bytes = base64.b64decode(encoded)
            return "".join(format(byte, "08b") for byte in decoded_bytes)
        except Exception as e:
            raise ValueError(f"Failed to decode TC String: {e}")

    def _read_bits(self, num_bits: int) -> int:
        """Read N bits from the current position and return as integer."""
        if self.position + num_bits > len(self.bits):
            raise ValueError(
                f"Attempted to read beyond bit string length at position {self.position}"
            )
        value = int(self.bits[self.position : self.position + num_bits], 2)
        self.position += num_bits
        return value

    def _read_bool(self) -> bool:
        """Read a single bit as boolean."""
        return self._read_bits(1) == 1

    def _read_datetime(self) -> str:
        """Read 36-bit deciseconds since 2020-01-01 and return ISO 8601."""
        deciseconds = self._read_bits(36)
        epoch = datetime(2020, 1, 1, tzinfo=timezone.utc)
        dt = epoch + timedelta(seconds=deciseconds / 10)
        return dt.isoformat()

    def _read_language(self) -> str:
        """Read 12-bit language code (two 6-bit letters, A=0)."""
        char1 = chr(self._read_bits(6) + ord("a"))
        char2 = chr(self._read_bits(6) + ord("a"))
        return f"{char1}{char2}"

    def _read_country(self) -> str:
        """Read 12-bit country code (two 6-bit letters, A=0)."""
        char1 = chr(self._read_bits(6) + ord("A"))
        char2 = chr(self._read_bits(6) + ord("A"))
        return f"{char1}{char2}"

    def _read_bitfield(self, num_bits: int) -> dict:
        """Read a bitfield and return as dict of {id: bool}."""
        result = {}
        for i in range(num_bits):
            result[i + 1] = self._read_bool()
        return result

    def decode_core(self) -> dict:
        """Decode the core TC String segment."""
        self.position = 0

        core = {
            "version": self._read_bits(6),
            "created": self._read_datetime(),
            "lastUpdated": self._read_datetime(),
            "cmpId": self._read_bits(12),
            "cmpVersion": self._read_bits(12),
            "consentScreen": self._read_bits(6),
            "consentLanguage": self._read_language(),
            "vendorListVersion": self._read_bits(12),
            "tcfPolicyVersion": self._read_bits(6),
            "isServiceSpecific": self._read_bool(),
            "useNonStandardStacks": self._read_bool(),
        }

        # Special feature opt-ins (12 bits)
        core["specialFeatureOptIns"] = self._read_bitfield(12)

        # Purpose consents (24 bits)
        core["purposeConsents"] = self._read_bitfield(24)

        # Purpose legitimate interests (24 bits)
        core["purposeLegitimateInterests"] = self._read_bitfield(24)

        # Purpose one treatment
        core["purposeOneTreatment"] = self._read_bool()

        # Publisher country code
        core["publisherCC"] = self._read_country()

        self.decoded = core
        return core

    def get_consented_purposes(self) -> list[int]:
        """Return list of purpose IDs with consent."""
        if "purposeConsents" not in self.decoded:
            self.decode_core()
        return [
            pid
            for pid, consented in self.decoded["purposeConsents"].items()
            if consented
        ]

    def get_li_purposes(self) -> list[int]:
        """Return list of purpose IDs with legitimate interest."""
        if "purposeLegitimateInterests" not in self.decoded:
            self.decode_core()
        return [
            pid
            for pid, li in self.decoded["purposeLegitimateInterests"].items()
            if li
        ]


class TCFValidator:
    """Validates TC Strings against requirements."""

    TCF_PURPOSES = {
        1: "Store and/or access information on a device",
        2: "Select basic ads",
        3: "Create profiles for personalised advertising",
        4: "Use profiles to select personalised ads",
        5: "Create profiles to personalise content",
        6: "Use profiles to select personalised content",
        7: "Measure ad performance",
        8: "Measure content performance",
        9: "Understand audiences through statistics",
        10: "Develop and improve services",
        11: "Use limited data to select content",
    }

    def __init__(self, tc_string: str, publisher_config: Optional[dict] = None):
        self.tc_string = tc_string
        self.decoder = TCStringDecoder(tc_string)
        self.decoded = self.decoder.decode_core()
        self.publisher_config = publisher_config or {}
        self.issues = []

    def validate_version(self):
        """Check TC String version is 2."""
        if self.decoded["version"] != 2:
            self.issues.append({
                "check": "version",
                "severity": "critical",
                "message": f"TC String version is {self.decoded['version']}, expected 2",
            })

    def validate_cmp_id(self):
        """Check CMP ID is non-zero (registered)."""
        if self.decoded["cmpId"] == 0:
            self.issues.append({
                "check": "cmpId",
                "severity": "critical",
                "message": "CMP ID is 0 — CMP may not be registered with IAB Europe",
            })

    def validate_policy_version(self):
        """Check TCF policy version is current."""
        if self.decoded["tcfPolicyVersion"] < 4:
            self.issues.append({
                "check": "tcfPolicyVersion",
                "severity": "high",
                "message": f"TCF policy version is {self.decoded['tcfPolicyVersion']}, current is 4",
            })

    def validate_timestamps(self):
        """Check timestamps are reasonable."""
        created = datetime.fromisoformat(self.decoded["created"])
        updated = datetime.fromisoformat(self.decoded["lastUpdated"])
        now = datetime.now(timezone.utc)

        if created > now:
            self.issues.append({
                "check": "timestamps",
                "severity": "medium",
                "message": "TC String created timestamp is in the future",
            })

        if updated < created:
            self.issues.append({
                "check": "timestamps",
                "severity": "medium",
                "message": "lastUpdated is before created timestamp",
            })

    def validate_purpose_one(self):
        """Purpose 1 should always use consent (not LI) under ePrivacy."""
        li_purposes = self.decoder.get_li_purposes()
        if 1 in li_purposes:
            self.issues.append({
                "check": "purpose_one_li",
                "severity": "critical",
                "message": "Purpose 1 (device storage) uses legitimate interest — must use consent under ePrivacy Art. 5(3)",
            })

    def validate_publisher_restrictions(self):
        """Check that publisher-required consent overrides are in place."""
        consent_only_purposes = self.publisher_config.get("consent_only_purposes", [])
        li_purposes = self.decoder.get_li_purposes()

        for purpose_id in consent_only_purposes:
            if purpose_id in li_purposes:
                self.issues.append({
                    "check": "publisher_restrictions",
                    "severity": "high",
                    "message": f"Purpose {purpose_id} uses LI but publisher requires consent-only",
                })

    def run_all_validations(self) -> dict:
        """Run all validation checks and return report."""
        self.validate_version()
        self.validate_cmp_id()
        self.validate_policy_version()
        self.validate_timestamps()
        self.validate_purpose_one()
        self.validate_publisher_restrictions()

        consented = self.decoder.get_consented_purposes()
        li = self.decoder.get_li_purposes()

        return {
            "tc_string": self.tc_string,
            "decoded": {
                "version": self.decoded["version"],
                "created": self.decoded["created"],
                "lastUpdated": self.decoded["lastUpdated"],
                "cmpId": self.decoded["cmpId"],
                "cmpVersion": self.decoded["cmpVersion"],
                "consentLanguage": self.decoded["consentLanguage"],
                "vendorListVersion": self.decoded["vendorListVersion"],
                "tcfPolicyVersion": self.decoded["tcfPolicyVersion"],
                "isServiceSpecific": self.decoded["isServiceSpecific"],
                "publisherCC": self.decoded["publisherCC"],
                "purposeOneTreatment": self.decoded["purposeOneTreatment"],
            },
            "consent_summary": {
                "purposes_with_consent": consented,
                "purposes_with_li": li,
                "purpose_details": {
                    pid: {
                        "name": self.TCF_PURPOSES.get(pid, "Unknown"),
                        "consent": pid in consented,
                        "legitimate_interest": pid in li,
                    }
                    for pid in range(1, 12)
                },
            },
            "validation": {
                "total_issues": len(self.issues),
                "critical": len([i for i in self.issues if i["severity"] == "critical"]),
                "high": len([i for i in self.issues if i["severity"] == "high"]),
                "medium": len([i for i in self.issues if i["severity"] == "medium"]),
                "issues": self.issues,
                "status": "VALID" if not self.issues else "ISSUES_FOUND",
            },
        }


def main():
    """Decode and validate a sample TC String."""
    # Example TC String (this is a synthetic example for demonstration)
    sample_tc_string = "CPyXXYAPyXXYAAGABCENB4CgAP_AAH_AAAAAHfoBpDxkBSFCAGJoYtkgAAAGxwAAICACABAAoAAAABoAIAQAAAAQAAAgBAAAABIAIAIAAABAGEAAAAAAQAAAAQAAAEAAAAAAIQIAAAAAAiBAAAAAAAAAAAAAAABAAAAAAAAAAgAAAAAAAQAA"

    print("=== TCF v2.2 TC String Decoder and Validator ===\n")

    # Pinnacle E-Commerce Ltd publisher config
    publisher_config = {
        "consent_only_purposes": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "publisher_name": "Pinnacle E-Commerce Ltd",
        "publisher_cc": "GB",
    }

    try:
        validator = TCFValidator(sample_tc_string, publisher_config)
        report = validator.run_all_validations()

        # Print summary
        print(f"TC String: {report['tc_string'][:60]}...")
        print(f"\nDecoded Core:")
        for key, value in report["decoded"].items():
            print(f"  {key}: {value}")

        print(f"\nConsent Summary:")
        print(f"  Purposes with consent: {report['consent_summary']['purposes_with_consent']}")
        print(f"  Purposes with LI: {report['consent_summary']['purposes_with_li']}")

        print(f"\nValidation Results:")
        print(f"  Status: {report['validation']['status']}")
        print(f"  Total issues: {report['validation']['total_issues']}")
        if report["validation"]["issues"]:
            for issue in report["validation"]["issues"]:
                print(f"  [{issue['severity'].upper()}] {issue['message']}")

        # Save report
        output_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "reports")
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "tcf_validation_report.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        print(f"\nReport saved to {output_path}")

    except ValueError as e:
        print(f"Error decoding TC String: {e}")


if __name__ == "__main__":
    main()
