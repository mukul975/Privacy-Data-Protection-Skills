---
name: cloud-retention-config
description: >-
  Configures cloud storage retention policies across AWS S3, Azure Blob Storage, and
  Google Cloud Storage. Covers lifecycle rules, object lock, legal hold, immutability
  policies, cross-region replication retention alignment, and compliance mode configuration.
  Activate for cloud retention, S3 lifecycle, Azure retention, GCP retention policy queries.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-retention-deletion
  tags: "cloud-retention, s3-lifecycle, azure-blob-retention, gcp-retention, object-lock"
---

# Cloud Storage Retention Configuration

## Overview

Cloud storage platforms provide native retention and lifecycle management features that can enforce data retention schedules at the infrastructure level. Proper configuration ensures that personal data stored in cloud environments is automatically transitioned, archived, or deleted according to retention policies, while legal hold and object lock features prevent premature deletion of data subject to regulatory or litigation requirements. This skill covers configuration for the three major cloud platforms: AWS S3, Microsoft Azure Blob Storage, and Google Cloud Storage.

## Legal Context

### GDPR Article 5(1)(e) — Storage Limitation

Cloud storage retention policies are a technical implementation of the storage limitation principle, ensuring data is not retained beyond the period necessary for processing purposes.

### GDPR Article 32 — Security of Processing

Retention configuration must include appropriate security measures, including encryption at rest, access controls, and audit logging for all retention-related operations.

### GDPR Article 25 — Data Protection by Design and by Default

Cloud retention policies should be configured as default settings on all storage resources, rather than applied retroactively.

## AWS S3 Lifecycle and Retention Configuration

### S3 Lifecycle Rules

S3 Lifecycle rules automate transitions between storage classes and object expiration:

#### Lifecycle Rule Configuration for Orion Data Vault Corp

| Rule Name | Prefix/Tag Filter | Transition | Expiration | Purpose |
|-----------|-------------------|------------|------------|---------|
| customer-data-lifecycle | prefix: `customer-data/` | 90 days → S3 Glacier Instant Retrieval; 365 days → S3 Glacier Deep Archive | 2,190 days (6 years) | Customer transaction records — HMRC retention |
| marketing-data-lifecycle | tag: `data-category=marketing` | 180 days → S3 Intelligent-Tiering | 730 days (2 years) | Marketing contact data — consent-based retention |
| analytics-data-lifecycle | prefix: `analytics/` | 90 days → S3 Glacier Instant Retrieval | 790 days (26 months) | Website analytics — ICO/CNIL recommended period |
| cctv-footage-lifecycle | prefix: `cctv/` | None | 30 days | CCTV footage — ICO CCTV Code of Practice |
| applicant-data-lifecycle | prefix: `recruitment/` | None | 180 days (6 months) | Unsuccessful job applicant data |
| financial-records-lifecycle | prefix: `finance/` | 365 days → S3 Glacier Deep Archive | 2,190 days (6 years) | Financial and tax records — Companies Act 2006 |
| employee-records-lifecycle | tag: `data-category=employee` | 730 days → S3 Glacier Deep Archive | Controlled by HR system (employment + 6 years) | Employee HR records |

#### S3 Lifecycle Rule — JSON Configuration Example

```json
{
  "Rules": [
    {
      "ID": "customer-data-lifecycle",
      "Filter": {
        "Prefix": "customer-data/"
      },
      "Status": "Enabled",
      "Transitions": [
        {
          "Days": 90,
          "StorageClass": "GLACIER_IR"
        },
        {
          "Days": 365,
          "StorageClass": "DEEP_ARCHIVE"
        }
      ],
      "Expiration": {
        "Days": 2190
      },
      "NoncurrentVersionTransitions": [
        {
          "NoncurrentDays": 30,
          "StorageClass": "GLACIER_IR"
        }
      ],
      "NoncurrentVersionExpiration": {
        "NoncurrentDays": 2190
      }
    }
  ]
}
```

### S3 Object Lock

S3 Object Lock prevents objects from being deleted or overwritten for a fixed retention period or indefinitely. It operates in two modes:

| Mode | Behaviour | Use Case at Orion Data Vault Corp |
|------|-----------|----------------------------------|
| **Governance Mode** | Prevents deletion by most users; users with `s3:BypassGovernanceRetention` permission can override | Standard retention enforcement — allows DPO-approved early deletion for valid Art. 17 requests |
| **Compliance Mode** | Prevents deletion by ALL users, including root account, for the entire retention period | Regulatory records where deletion before expiry is legally prohibited (e.g., AML records under MLR 2017) |

#### Object Lock Configuration

```json
{
  "ObjectLockConfiguration": {
    "ObjectLockEnabled": "Enabled",
    "Rule": {
      "DefaultRetention": {
        "Mode": "GOVERNANCE",
        "Days": 2190
      }
    }
  }
}
```

**Critical consideration for GDPR erasure**: If using Compliance Mode, data subject erasure requests under Art. 17 cannot be fulfilled until the retention period expires. Use Governance Mode for data categories where erasure requests are possible, and reserve Compliance Mode only for data with mandatory statutory retention that overrides the right to erasure under Art. 17(3)(b).

### S3 Legal Hold

Legal hold is an independent, on/off flag that prevents object deletion regardless of retention settings:

```
aws s3api put-object-legal-hold \
  --bucket orion-data-vault-regulated \
  --key customer-data/2024/transaction-batch-0142.parquet \
  --legal-hold Status=ON
```

Legal hold must be:
- Applied immediately upon receipt of a litigation hold notice
- Tracked in the litigation hold management register (cross-reference: litigation-hold-mgmt skill)
- Removed only upon written authorization from Legal counsel
- Auditable — all legal hold changes logged via CloudTrail

## Microsoft Azure Blob Storage Retention

### Immutability Policies

Azure Blob Storage supports immutability policies at the container level:

| Policy Type | Behaviour | Configuration |
|------------|-----------|---------------|
| **Time-based retention** | Prevents modification and deletion for a specified interval | Set retention interval in days; can be locked (irreversible) or unlocked |
| **Legal hold** | Prevents modification and deletion until all legal hold tags are cleared | Apply named legal hold tags; multiple holds can coexist |

#### Time-Based Retention Policy Configuration

```json
{
  "properties": {
    "immutabilityPeriodSinceCreationInDays": 2190,
    "allowProtectedAppendWrites": true,
    "allowProtectedAppendWritesAll": false
  }
}
```

#### Azure Lifecycle Management Rules

```json
{
  "rules": [
    {
      "enabled": true,
      "name": "customer-data-retention",
      "type": "Lifecycle",
      "definition": {
        "filters": {
          "blobTypes": ["blockBlob"],
          "prefixMatch": ["customer-data/"]
        },
        "actions": {
          "baseBlob": {
            "tierToCool": {
              "daysAfterModificationGreaterThan": 90
            },
            "tierToArchive": {
              "daysAfterModificationGreaterThan": 365
            },
            "delete": {
              "daysAfterModificationGreaterThan": 2190
            }
          },
          "snapshot": {
            "delete": {
              "daysAfterCreationGreaterThan": 2190
            }
          }
        }
      }
    },
    {
      "enabled": true,
      "name": "analytics-data-retention",
      "type": "Lifecycle",
      "definition": {
        "filters": {
          "blobTypes": ["blockBlob"],
          "prefixMatch": ["analytics/"]
        },
        "actions": {
          "baseBlob": {
            "tierToCool": {
              "daysAfterModificationGreaterThan": 90
            },
            "delete": {
              "daysAfterModificationGreaterThan": 790
            }
          }
        }
      }
    }
  ]
}
```

#### Azure Legal Hold

```
az storage container legal-hold set \
  --account-name oriondatavault \
  --container-name regulated-data \
  --tags "litigation-2026-001" "regulatory-investigation-2026-003"
```

### Azure Versioning and Soft Delete Interaction

When configuring retention, account for Azure's soft delete and versioning features:

| Feature | Retention Impact | Recommended Setting |
|---------|-----------------|-------------------|
| Blob soft delete | Deleted blobs retained for recovery period | Set to 14 days — ensure actual deletion occurs after soft delete period |
| Container soft delete | Deleted containers retained for recovery | Set to 14 days |
| Blob versioning | Previous versions retained | Apply lifecycle rules to versions; ensure expired versions are deleted |

## Google Cloud Storage Retention

### Bucket-Level Retention Policy

GCP applies retention policies at the bucket level. Objects cannot be deleted or overwritten until the retention period expires:

```json
{
  "retentionPolicy": {
    "retentionPeriod": "189216000",
    "isLocked": false
  }
}
```

The `retentionPeriod` is specified in seconds. Common values:

| Retention Period | Seconds | Use Case |
|-----------------|---------|----------|
| 30 days | 2,592,000 | CCTV footage |
| 6 months | 15,552,000 | Unsuccessful applicant data |
| 26 months | 68,256,000 | Analytics data |
| 2 years | 63,072,000 | Marketing data |
| 6 years | 189,216,000 | Financial/tax records |
| 7 years | 220,752,000 | Audit records |

#### Locking a Retention Policy

```
gcloud storage buckets update gs://orion-regulated-finance \
  --lock-retention-policy
```

**Warning**: Locking a retention policy is IRREVERSIBLE. Once locked, the retention period cannot be reduced or removed. The bucket cannot be deleted until every object in it has met its retention period. Only lock policies for data categories with absolute statutory retention requirements that override Art. 17 rights.

### GCP Object Hold

| Hold Type | Behaviour | Use Case |
|-----------|-----------|----------|
| **Temporary hold** | Prevents deletion; can be removed at any time | Art. 17 request pauses (assessment period); temporary preservation |
| **Event-based hold** | Prevents deletion until the hold is released; retention period begins on hold release | Data where retention period starts from a future event (e.g., contract termination) |

```
gcloud storage objects update gs://orion-regulated-data/customer-data/batch-0142.parquet \
  --temporary-hold
```

### GCP Lifecycle Rules

```json
{
  "lifecycle": {
    "rule": [
      {
        "action": {
          "type": "SetStorageClass",
          "storageClass": "NEARLINE"
        },
        "condition": {
          "age": 90,
          "matchesPrefix": ["customer-data/"]
        }
      },
      {
        "action": {
          "type": "SetStorageClass",
          "storageClass": "ARCHIVE"
        },
        "condition": {
          "age": 365,
          "matchesPrefix": ["customer-data/"]
        }
      },
      {
        "action": {
          "type": "Delete"
        },
        "condition": {
          "age": 2190,
          "matchesPrefix": ["customer-data/"]
        }
      }
    ]
  }
}
```

## Cross-Region Replication Retention Alignment

When data is replicated across regions for availability or disaster recovery, retention policies must be aligned:

### Alignment Requirements

1. **Identical retention periods**: Replicated data in the destination region must have the same retention period as the source.
2. **Synchronized lifecycle rules**: Lifecycle transitions and expirations must be configured identically on source and destination buckets/containers.
3. **Legal hold propagation**: Legal holds applied in the source must also be applied in the destination. Configure automated propagation.
4. **Deletion propagation**: When an object expires or is deleted in the source, the replica must also be deleted. Configure replication to handle delete markers.
5. **Jurisdictional considerations**: If the destination region is in a different jurisdiction, confirm that the applicable retention requirements in that jurisdiction do not conflict with the source retention period.

### Cross-Region Configuration Checklist

| Check | AWS | Azure | GCP |
|-------|-----|-------|-----|
| Lifecycle rules match source | Apply identical S3 lifecycle rules to destination bucket | Apply identical lifecycle management policy to destination container | Apply identical lifecycle rules to destination bucket |
| Retention/lock settings match | Configure identical Object Lock settings on destination | Apply identical immutability policy to destination | Apply identical retention policy to destination |
| Delete marker replication | Enable `DeleteMarkerReplication` in replication config | Enable blob change feed and handle deletes | Configure bucket notifications for deletion events |
| Legal hold synchronization | Use Lambda triggered by CloudTrail to propagate legal holds | Use Event Grid + Azure Function to propagate legal holds | Use Cloud Functions triggered by audit logs to propagate holds |
| Monitoring | CloudWatch metrics on replication lag | Azure Monitor replication metrics | Cloud Monitoring replication metrics |

## Compliance Monitoring

### Monthly Cloud Retention Audit

1. **Policy drift detection**: Compare active lifecycle rules and retention policies against the approved retention schedule. Flag any discrepancies.
2. **Coverage verification**: Confirm that all storage buckets/containers holding personal data have applicable retention policies.
3. **Legal hold inventory**: List all active legal holds across all cloud platforms. Cross-reference with the litigation hold register to identify holds that should have been released.
4. **Expiration verification**: Sample recently expired objects to confirm they were actually deleted (not just transitioned or soft-deleted).
5. **Cross-region consistency**: Verify that replicated buckets/containers maintain identical retention configuration.

### Alert Configuration

| Alert | Condition | Action |
|-------|-----------|--------|
| Policy removed | Retention policy or lifecycle rule deleted from a regulated bucket | Immediate alert to Cloud Security + DPO |
| Object lock bypass | `s3:BypassGovernanceRetention` used | Alert to DPO; verify authorized deletion |
| Legal hold change | Legal hold applied or removed | Log to litigation hold register; alert Legal |
| Retention policy unlock attempt | Attempt to modify locked retention policy | Alert to Cloud Security (should fail — investigate) |
| Replication lag > 24h | Cross-region replication behind by more than 24 hours | Alert IT Operations — potential retention gap in DR region |
