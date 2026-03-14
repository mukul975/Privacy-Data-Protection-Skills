"""
Cloud Storage Retention Configuration Process
Generates and validates retention policies for AWS S3, Azure Blob, and GCP Cloud Storage.
"""

import json
from datetime import datetime
from typing import Optional


# Retention periods in days mapped to data categories
RETENTION_PERIODS = {
    "customer-data": {"days": 2190, "description": "6 years — HMRC/Companies Act"},
    "marketing-data": {"days": 730, "description": "2 years — consent-based"},
    "analytics-data": {"days": 790, "description": "26 months — ICO/CNIL"},
    "cctv-footage": {"days": 30, "description": "30 days — ICO CCTV Code"},
    "applicant-data": {"days": 180, "description": "6 months — unsuccessful applicants"},
    "financial-records": {"days": 2190, "description": "6 years — Companies Act/HMRC"},
    "employee-records": {"days": 2190, "description": "6 years post-employment"},
    "aml-records": {"days": 1825, "description": "5 years — MLR 2017"},
    "audit-records": {"days": 2555, "description": "7 years — SOX (if applicable)"},
}


def generate_s3_lifecycle_rule(
    rule_id: str,
    prefix: str,
    retention_days: int,
    glacier_transition_days: int = 90,
    deep_archive_days: int = 365,
) -> dict:
    """Generate an AWS S3 lifecycle rule configuration."""
    rule = {
        "ID": rule_id,
        "Filter": {"Prefix": prefix},
        "Status": "Enabled",
        "Transitions": [],
        "Expiration": {"Days": retention_days},
        "NoncurrentVersionTransitions": [
            {"NoncurrentDays": 30, "StorageClass": "GLACIER_IR"}
        ],
        "NoncurrentVersionExpiration": {"NoncurrentDays": retention_days},
    }

    if retention_days > glacier_transition_days:
        rule["Transitions"].append({
            "Days": glacier_transition_days,
            "StorageClass": "GLACIER_IR",
        })
    if retention_days > deep_archive_days:
        rule["Transitions"].append({
            "Days": deep_archive_days,
            "StorageClass": "DEEP_ARCHIVE",
        })

    return rule


def generate_s3_object_lock_config(
    mode: str = "GOVERNANCE",
    retention_days: int = 2190,
) -> dict:
    """Generate S3 Object Lock configuration."""
    if mode not in ("GOVERNANCE", "COMPLIANCE"):
        raise ValueError("Mode must be GOVERNANCE or COMPLIANCE")
    return {
        "ObjectLockConfiguration": {
            "ObjectLockEnabled": "Enabled",
            "Rule": {
                "DefaultRetention": {
                    "Mode": mode,
                    "Days": retention_days,
                }
            },
        }
    }


def generate_azure_lifecycle_rule(
    rule_name: str,
    prefix: str,
    retention_days: int,
    cool_transition_days: int = 90,
    archive_transition_days: int = 365,
) -> dict:
    """Generate Azure Blob Storage lifecycle management rule."""
    actions = {"baseBlob": {}, "snapshot": {"delete": {"daysAfterCreationGreaterThan": retention_days}}}

    if retention_days > cool_transition_days:
        actions["baseBlob"]["tierToCool"] = {"daysAfterModificationGreaterThan": cool_transition_days}
    if retention_days > archive_transition_days:
        actions["baseBlob"]["tierToArchive"] = {"daysAfterModificationGreaterThan": archive_transition_days}
    actions["baseBlob"]["delete"] = {"daysAfterModificationGreaterThan": retention_days}

    return {
        "enabled": True,
        "name": rule_name,
        "type": "Lifecycle",
        "definition": {
            "filters": {
                "blobTypes": ["blockBlob"],
                "prefixMatch": [prefix],
            },
            "actions": actions,
        },
    }


def generate_azure_immutability_policy(retention_days: int, allow_append: bool = True) -> dict:
    """Generate Azure Blob immutability policy."""
    return {
        "properties": {
            "immutabilityPeriodSinceCreationInDays": retention_days,
            "allowProtectedAppendWrites": allow_append,
            "allowProtectedAppendWritesAll": False,
        }
    }


def generate_gcp_retention_policy(retention_seconds: int, lock: bool = False) -> dict:
    """Generate GCP Cloud Storage bucket retention policy."""
    return {
        "retentionPolicy": {
            "retentionPeriod": str(retention_seconds),
            "isLocked": lock,
        }
    }


def generate_gcp_lifecycle_rules(
    prefix: str,
    retention_days: int,
    nearline_days: int = 90,
    archive_days: int = 365,
) -> dict:
    """Generate GCP Cloud Storage lifecycle rules."""
    rules = []

    if retention_days > nearline_days:
        rules.append({
            "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
            "condition": {"age": nearline_days, "matchesPrefix": [prefix]},
        })
    if retention_days > archive_days:
        rules.append({
            "action": {"type": "SetStorageClass", "storageClass": "ARCHIVE"},
            "condition": {"age": archive_days, "matchesPrefix": [prefix]},
        })
    rules.append({
        "action": {"type": "Delete"},
        "condition": {"age": retention_days, "matchesPrefix": [prefix]},
    })

    return {"lifecycle": {"rule": rules}}


def days_to_seconds(days: int) -> int:
    """Convert days to seconds for GCP retention policy."""
    return days * 86400


def generate_full_cloud_config(data_category: str) -> dict:
    """Generate retention configuration for all three cloud platforms."""
    if data_category not in RETENTION_PERIODS:
        raise ValueError(f"Unknown data category: {data_category}")

    period = RETENTION_PERIODS[data_category]
    days = period["days"]
    prefix = f"{data_category}/"

    return {
        "data_category": data_category,
        "retention_period": period,
        "generated_at": datetime.utcnow().isoformat(),
        "aws_s3": {
            "lifecycle_rule": generate_s3_lifecycle_rule(
                f"{data_category}-lifecycle", prefix, days
            ),
            "object_lock": generate_s3_object_lock_config("GOVERNANCE", days),
        },
        "azure_blob": {
            "lifecycle_rule": generate_azure_lifecycle_rule(
                f"{data_category}-retention", prefix, days
            ),
            "immutability_policy": generate_azure_immutability_policy(days),
        },
        "gcp_gcs": {
            "retention_policy": generate_gcp_retention_policy(days_to_seconds(days)),
            "lifecycle_rules": generate_gcp_lifecycle_rules(prefix, days),
        },
    }


def audit_cross_region_alignment(
    source_config: dict, destination_config: dict
) -> list[dict]:
    """Audit cross-region replication retention alignment."""
    findings = []

    for platform in ["aws_s3", "azure_blob", "gcp_gcs"]:
        if platform in source_config and platform in destination_config:
            source_str = json.dumps(source_config[platform], sort_keys=True)
            dest_str = json.dumps(destination_config[platform], sort_keys=True)
            if source_str != dest_str:
                findings.append({
                    "platform": platform,
                    "finding": "MISALIGNMENT",
                    "severity": "HIGH",
                    "description": f"Source and destination {platform} retention configs differ",
                })
            else:
                findings.append({
                    "platform": platform,
                    "finding": "ALIGNED",
                    "severity": "INFO",
                    "description": f"{platform} retention configs match",
                })

    return findings


if __name__ == "__main__":
    config = generate_full_cloud_config("customer-data")
    print(json.dumps(config, indent=2))
