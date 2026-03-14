#!/usr/bin/env python3
"""
Cloud Storage Retention Configuration Process
Generates lifecycle rules and retention policies for AWS S3, Azure Blob, and GCP GCS.
"""

import json
from datetime import datetime


RETENTION_TIERS = {
    "customer-data": {
        "description": "Customer transaction records",
        "retention_days": 2190,
        "transitions": [
            {"days": 90, "target": "cool"},
            {"days": 365, "target": "archive"},
        ],
        "statutory_basis": "HMRC record-keeping; Companies Act 2006 s.386",
    },
    "marketing-data": {
        "description": "Marketing contact data",
        "retention_days": 730,
        "transitions": [
            {"days": 180, "target": "cool"},
        ],
        "statutory_basis": "Consent-based; 2-year engagement window",
    },
    "analytics": {
        "description": "Website analytics data",
        "retention_days": 790,
        "transitions": [
            {"days": 90, "target": "cool"},
        ],
        "statutory_basis": "ICO/CNIL 26-month recommendation",
    },
    "cctv": {
        "description": "CCTV footage",
        "retention_days": 30,
        "transitions": [],
        "statutory_basis": "ICO CCTV Code of Practice",
    },
    "recruitment": {
        "description": "Job applicant data",
        "retention_days": 180,
        "transitions": [],
        "statutory_basis": "ICO Employment Practices Code",
    },
    "finance": {
        "description": "Financial and tax records",
        "retention_days": 2190,
        "transitions": [
            {"days": 365, "target": "archive"},
        ],
        "statutory_basis": "Companies Act 2006; HMRC requirements",
    },
}

AWS_STORAGE_CLASS_MAP = {
    "cool": "GLACIER_IR",
    "archive": "DEEP_ARCHIVE",
}

AZURE_TIER_MAP = {
    "cool": "tierToCool",
    "archive": "tierToArchive",
}

GCP_CLASS_MAP = {
    "cool": "NEARLINE",
    "archive": "ARCHIVE",
}


def generate_s3_lifecycle_rules() -> dict:
    """Generate AWS S3 lifecycle configuration."""
    rules = []
    for prefix, config in RETENTION_TIERS.items():
        rule = {
            "ID": f"{prefix}-lifecycle",
            "Filter": {"Prefix": f"{prefix}/"},
            "Status": "Enabled",
            "Transitions": [],
            "Expiration": {"Days": config["retention_days"]},
            "NoncurrentVersionExpiration": {"NoncurrentDays": config["retention_days"]},
        }
        for transition in config["transitions"]:
            rule["Transitions"].append({
                "Days": transition["days"],
                "StorageClass": AWS_STORAGE_CLASS_MAP.get(transition["target"], "GLACIER_IR"),
            })
        if config["transitions"]:
            rule["NoncurrentVersionTransitions"] = [
                {
                    "NoncurrentDays": config["transitions"][0]["days"],
                    "StorageClass": AWS_STORAGE_CLASS_MAP.get(
                        config["transitions"][0]["target"], "GLACIER_IR"
                    ),
                }
            ]
        rules.append(rule)

    return {"Rules": rules}


def generate_s3_object_lock_config(mode: str = "GOVERNANCE", days: int = 2190) -> dict:
    """Generate S3 Object Lock configuration."""
    if mode not in ("GOVERNANCE", "COMPLIANCE"):
        raise ValueError("Mode must be GOVERNANCE or COMPLIANCE")
    return {
        "ObjectLockConfiguration": {
            "ObjectLockEnabled": "Enabled",
            "Rule": {
                "DefaultRetention": {
                    "Mode": mode,
                    "Days": days,
                }
            },
        }
    }


def generate_azure_lifecycle_rules() -> dict:
    """Generate Azure Blob Storage lifecycle management rules."""
    rules = []
    for prefix, config in RETENTION_TIERS.items():
        rule = {
            "enabled": True,
            "name": f"{prefix}-retention",
            "type": "Lifecycle",
            "definition": {
                "filters": {
                    "blobTypes": ["blockBlob"],
                    "prefixMatch": [f"{prefix}/"],
                },
                "actions": {
                    "baseBlob": {
                        "delete": {
                            "daysAfterModificationGreaterThan": config["retention_days"],
                        }
                    },
                    "snapshot": {
                        "delete": {
                            "daysAfterCreationGreaterThan": config["retention_days"],
                        }
                    },
                },
            },
        }
        for transition in config["transitions"]:
            azure_action = AZURE_TIER_MAP.get(transition["target"])
            if azure_action:
                rule["definition"]["actions"]["baseBlob"][azure_action] = {
                    "daysAfterModificationGreaterThan": transition["days"],
                }
        rules.append(rule)

    return {"rules": rules}


def generate_azure_immutability_policy(retention_days: int, allow_append: bool = True) -> dict:
    """Generate Azure Blob immutability policy."""
    return {
        "properties": {
            "immutabilityPeriodSinceCreationInDays": retention_days,
            "allowProtectedAppendWrites": allow_append,
            "allowProtectedAppendWritesAll": False,
        }
    }


def generate_gcp_retention_policy(retention_days: int, locked: bool = False) -> dict:
    """Generate GCP GCS bucket retention policy."""
    retention_seconds = retention_days * 86400
    return {
        "retentionPolicy": {
            "retentionPeriod": str(retention_seconds),
            "isLocked": locked,
        }
    }


def generate_gcp_lifecycle_rules() -> dict:
    """Generate GCP GCS lifecycle rules."""
    rules = []
    for prefix, config in RETENTION_TIERS.items():
        for transition in config["transitions"]:
            rules.append({
                "action": {
                    "type": "SetStorageClass",
                    "storageClass": GCP_CLASS_MAP.get(transition["target"], "NEARLINE"),
                },
                "condition": {
                    "age": transition["days"],
                    "matchesPrefix": [f"{prefix}/"],
                },
            })
        rules.append({
            "action": {"type": "Delete"},
            "condition": {
                "age": config["retention_days"],
                "matchesPrefix": [f"{prefix}/"],
            },
        })

    return {"lifecycle": {"rule": rules}}


def audit_cross_region_alignment(source_config: dict, destination_config: dict) -> dict:
    """Audit cross-region replication retention alignment."""
    findings = []
    compliant = True

    source_rules = {r.get("ID") or r.get("name"): r for r in source_config.get("Rules", source_config.get("rules", []))}
    dest_rules = {r.get("ID") or r.get("name"): r for r in destination_config.get("Rules", destination_config.get("rules", []))}

    for rule_id, source_rule in source_rules.items():
        if rule_id not in dest_rules:
            findings.append({
                "rule": rule_id,
                "finding": "MISSING — rule exists in source but not destination",
                "severity": "critical",
            })
            compliant = False
        else:
            dest_rule = dest_rules[rule_id]
            source_exp = source_rule.get("Expiration", {}).get("Days")
            dest_exp = dest_rule.get("Expiration", {}).get("Days")
            if source_exp != dest_exp:
                findings.append({
                    "rule": rule_id,
                    "finding": f"MISMATCH — source expiration {source_exp}d vs destination {dest_exp}d",
                    "severity": "high",
                })
                compliant = False

    return {
        "audit_date": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "compliant": compliant,
        "findings": findings,
        "total_rules_checked": len(source_rules),
    }


if __name__ == "__main__":
    print("=== AWS S3 Lifecycle Rules ===")
    s3_config = generate_s3_lifecycle_rules()
    print(json.dumps(s3_config, indent=2)[:500] + "...\n")

    print("=== Azure Blob Lifecycle Rules ===")
    azure_config = generate_azure_lifecycle_rules()
    print(json.dumps(azure_config, indent=2)[:500] + "...\n")

    print("=== GCP GCS Lifecycle Rules ===")
    gcp_config = generate_gcp_lifecycle_rules()
    print(json.dumps(gcp_config, indent=2)[:500] + "...\n")

    print("=== S3 Object Lock (Governance Mode) ===")
    lock_config = generate_s3_object_lock_config("GOVERNANCE", 2190)
    print(json.dumps(lock_config, indent=2))

    print("\n=== Cross-Region Alignment Audit ===")
    audit = audit_cross_region_alignment(s3_config, s3_config)
    print(f"Compliant: {audit['compliant']}")
    print(f"Rules Checked: {audit['total_rules_checked']}")
