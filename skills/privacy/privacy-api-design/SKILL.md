---
name: privacy-api-design
description: >-
  Design privacy API patterns including data subject API for DSAR endpoints,
  consent API for preference management, deletion API with cascading delete
  orchestration, and audit API for compliance reporting. Provides OpenAPI
  specifications, error handling, rate limiting, and authentication patterns.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-engineering
  tags: "privacy-api, dsar-api, consent-api, deletion-api, openapi-specification"
---

# Privacy API Design Patterns

## Overview

Privacy APIs provide programmatic interfaces for data subject rights exercise, consent management, data deletion, and audit logging. Well-designed privacy APIs enable organizations to automate compliance workflows, integrate with consent management platforms, and provide data subjects with self-service privacy controls. This skill covers API design patterns, OpenAPI specifications, authentication, and error handling for privacy-critical endpoints.

## API Architecture Overview

```
External Consumers                    Privacy API Gateway                    Backend Services
+------------------+                 +--------------------+                 +------------------+
| Data Subject App |----HTTPS/TLS--->| Authentication     |                 | DSAR Service     |
+------------------+                 | Rate Limiting      |----internal---->| Consent Service  |
                                     | Request Validation |                 | Deletion Service |
+------------------+                 | Audit Logging      |                 | Audit Service    |
| Partner Portal   |----HTTPS/TLS--->| Versioning         |                 | Identity Service |
+------------------+                 +--------------------+                 +------------------+
                                            |
+------------------+                        v
| Internal Systems |----mTLS-------->+--------------------+
+------------------+                 | Privacy Event Bus  |
                                     | (async processing) |
                                     +--------------------+
```

## 1. Data Subject API (DSAR Endpoints)

### OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Cipher Engineering Labs - Data Subject Rights API
  version: 1.0.0
  description: >
    API for data subjects to exercise their privacy rights under GDPR,
    CCPA/CPRA, and other applicable privacy regulations.
  contact:
    name: Privacy Engineering Team
    email: privacy-engineering@cipherengineeringlabs.com

servers:
  - url: https://api.cipherengineeringlabs.com/privacy/v1
    description: Production

security:
  - BearerAuth: []
  - OAuth2: [dsar:read, dsar:write]

paths:
  /dsar/requests:
    post:
      operationId: createDSARRequest
      summary: Submit a new data subject access request
      tags: [DSAR]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DSARCreateRequest'
      responses:
        '202':
          description: Request accepted for processing
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DSARResponse'
          headers:
            X-Request-ID:
              schema:
                type: string
                format: uuid
            Location:
              schema:
                type: string
                format: uri
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '429':
          $ref: '#/components/responses/RateLimited'

    get:
      operationId: listDSARRequests
      summary: List data subject's own requests
      tags: [DSAR]
      parameters:
        - name: status
          in: query
          schema:
            type: string
            enum: [pending, in_progress, completed, rejected]
        - name: type
          in: query
          schema:
            type: string
            enum: [access, deletion, portability, rectification, restriction, objection]
        - name: page
          in: query
          schema:
            type: integer
            minimum: 1
            default: 1
        - name: per_page
          in: query
          schema:
            type: integer
            minimum: 1
            maximum: 100
            default: 20
      responses:
        '200':
          description: List of DSAR requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DSARListResponse'

  /dsar/requests/{requestId}:
    get:
      operationId: getDSARRequest
      summary: Get status and details of a specific DSAR
      tags: [DSAR]
      parameters:
        - name: requestId
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: DSAR details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DSARDetailResponse'
        '404':
          $ref: '#/components/responses/NotFound'

  /dsar/requests/{requestId}/download:
    get:
      operationId: downloadDSARData
      summary: Download the data package for a completed access request
      tags: [DSAR]
      parameters:
        - name: requestId
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Data package download
          content:
            application/zip:
              schema:
                type: string
                format: binary
          headers:
            Content-Disposition:
              schema:
                type: string
        '404':
          $ref: '#/components/responses/NotFound'
        '410':
          description: Download link has expired

components:
  schemas:
    DSARCreateRequest:
      type: object
      required:
        - requestType
        - email
        - identityVerification
      properties:
        requestType:
          type: string
          enum: [access, deletion, portability, rectification, restriction, objection]
          description: Type of data subject right being exercised
        email:
          type: string
          format: email
          description: Email address associated with the account
        identityVerification:
          type: object
          properties:
            method:
              type: string
              enum: [account_login, email_verification, document_upload]
            verificationToken:
              type: string
          required: [method]
        details:
          type: string
          maxLength: 2000
          description: Additional details about the request
        dataCategories:
          type: array
          items:
            type: string
            enum: [profile, transactions, communications, analytics, marketing, all]
          description: Specific data categories (for access/portability)
        rectificationData:
          type: object
          additionalProperties: true
          description: Corrected data values (for rectification requests)
        preferredFormat:
          type: string
          enum: [json, csv, pdf]
          default: json
          description: Preferred data export format (for access/portability)

    DSARResponse:
      type: object
      properties:
        requestId:
          type: string
          format: uuid
        status:
          type: string
          enum: [pending, identity_verification, in_progress, completed, rejected]
        requestType:
          type: string
        submittedAt:
          type: string
          format: date-time
        estimatedCompletionDate:
          type: string
          format: date-time
        regulatoryDeadline:
          type: string
          format: date-time
          description: Maximum date by which response must be provided

    DSARDetailResponse:
      allOf:
        - $ref: '#/components/schemas/DSARResponse'
        - type: object
          properties:
            statusHistory:
              type: array
              items:
                type: object
                properties:
                  status:
                    type: string
                  timestamp:
                    type: string
                    format: date-time
                  note:
                    type: string
            downloadAvailable:
              type: boolean
            downloadExpiresAt:
              type: string
              format: date-time

    DSARListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/DSARResponse'
        pagination:
          $ref: '#/components/schemas/Pagination'

    Pagination:
      type: object
      properties:
        page:
          type: integer
        perPage:
          type: integer
        totalPages:
          type: integer
        totalItems:
          type: integer

  responses:
    BadRequest:
      description: Invalid request parameters
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    Unauthorized:
      description: Authentication required
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    NotFound:
      description: Resource not found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    RateLimited:
      description: Rate limit exceeded
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
      headers:
        Retry-After:
          schema:
            type: integer
        X-RateLimit-Limit:
          schema:
            type: integer
        X-RateLimit-Remaining:
          schema:
            type: integer

  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
    OAuth2:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: https://auth.cipherengineeringlabs.com/oauth2/authorize
          tokenUrl: https://auth.cipherengineeringlabs.com/oauth2/token
          scopes:
            dsar:read: Read DSAR request status
            dsar:write: Submit DSAR requests
            consent:read: Read consent preferences
            consent:write: Update consent preferences
            audit:read: Read audit logs
```

## 2. Consent API

### Consent Preference Management

```yaml
paths:
  /consent/preferences:
    get:
      operationId: getConsentPreferences
      summary: Get current consent preferences for the authenticated user
      tags: [Consent]
      responses:
        '200':
          description: Current consent preferences
          content:
            application/json:
              schema:
                type: object
                properties:
                  subjectId:
                    type: string
                  preferences:
                    type: array
                    items:
                      $ref: '#/components/schemas/ConsentPreference'
                  lastUpdated:
                    type: string
                    format: date-time

    put:
      operationId: updateConsentPreferences
      summary: Update consent preferences (bulk update)
      tags: [Consent]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [preferences]
              properties:
                preferences:
                  type: array
                  items:
                    type: object
                    required: [purposeId, granted]
                    properties:
                      purposeId:
                        type: string
                      granted:
                        type: boolean
                      channels:
                        type: array
                        items:
                          type: string
                          enum: [email, sms, push, phone, postal]
      responses:
        '200':
          description: Preferences updated
          content:
            application/json:
              schema:
                type: object
                properties:
                  updated:
                    type: array
                    items:
                      $ref: '#/components/schemas/ConsentPreference'
                  consentReceiptId:
                    type: string
                    format: uuid
                    description: ID of the issued consent receipt

  /consent/purposes:
    get:
      operationId: listConsentPurposes
      summary: List all available consent purposes
      tags: [Consent]
      responses:
        '200':
          description: List of consent purposes
          content:
            application/json:
              schema:
                type: object
                properties:
                  purposes:
                    type: array
                    items:
                      type: object
                      properties:
                        purposeId:
                          type: string
                        name:
                          type: string
                        description:
                          type: string
                        category:
                          type: string
                          enum: [essential, functional, analytics, marketing]
                        mandatory:
                          type: boolean
                        defaultState:
                          type: boolean
                        dataCategories:
                          type: array
                          items:
                            type: string

  /consent/receipts/{receiptId}:
    get:
      operationId: getConsentReceipt
      summary: Retrieve a specific consent receipt
      tags: [Consent]
      parameters:
        - name: receiptId
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Consent receipt
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ConsentReceipt'
```

## 3. Deletion API

### Cascading Delete Orchestration

```python
"""
Privacy deletion API with cascading delete orchestration.
Handles deletion requests across multiple backend services
with verification and audit logging.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional
import uuid


class DeletionStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    PARTIALLY_COMPLETED = "partially_completed"
    COMPLETED = "completed"
    FAILED = "failed"
    VERIFIED = "verified"


class ServiceDeletionStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"  # For legally exempt data


@dataclass
class DeletionTarget:
    service_name: str
    data_categories: list[str]
    priority: int  # Lower number = delete first
    legal_hold_check: bool = True
    retention_exempt: bool = False  # True if data must be retained (e.g., tax records)


@dataclass
class ServiceDeletionResult:
    service_name: str
    status: ServiceDeletionStatus
    records_deleted: int
    records_retained: int
    retention_reason: Optional[str]
    completed_at: Optional[datetime]
    error_message: Optional[str]


@dataclass
class DeletionRequest:
    request_id: str
    subject_id: str
    status: DeletionStatus
    created_at: datetime
    scope: list[str]  # Data categories to delete
    exclude: list[str]  # Data categories exempt from deletion
    service_results: list[ServiceDeletionResult] = field(default_factory=list)
    verified_at: Optional[datetime] = None
    verification_method: Optional[str] = None


class CascadingDeletionOrchestrator:
    """
    Orchestrate data deletion across multiple backend services
    in the correct order, handling dependencies, legal holds,
    and retention requirements.
    """

    def __init__(self, service_registry: list[DeletionTarget], audit_logger):
        self.targets = sorted(service_registry, key=lambda t: t.priority)
        self.audit = audit_logger

    def execute_deletion(
        self,
        subject_id: str,
        scope: list[str],
        exclude: list[str] = None
    ) -> DeletionRequest:
        """
        Execute cascading deletion across all registered services.

        Args:
            subject_id: The data subject whose data should be deleted
            scope: Data categories to delete (or ["all"])
            exclude: Data categories to exclude from deletion

        Returns:
            DeletionRequest with results from each service
        """
        exclude = exclude or []

        request = DeletionRequest(
            request_id=str(uuid.uuid4()),
            subject_id=subject_id,
            status=DeletionStatus.IN_PROGRESS,
            created_at=datetime.now(timezone.utc),
            scope=scope,
            exclude=exclude
        )

        self.audit.log_deletion_start(request)

        for target in self.targets:
            # Skip if data category not in scope
            if "all" not in scope:
                relevant_categories = set(target.data_categories) & set(scope)
                if not relevant_categories:
                    continue

            # Skip if explicitly excluded
            if set(target.data_categories) & set(exclude):
                result = ServiceDeletionResult(
                    service_name=target.service_name,
                    status=ServiceDeletionStatus.SKIPPED,
                    records_deleted=0,
                    records_retained=0,
                    retention_reason="Excluded by request",
                    completed_at=datetime.now(timezone.utc),
                    error_message=None
                )
                request.service_results.append(result)
                continue

            # Check retention exemptions
            if target.retention_exempt:
                result = ServiceDeletionResult(
                    service_name=target.service_name,
                    status=ServiceDeletionStatus.SKIPPED,
                    records_deleted=0,
                    records_retained=0,
                    retention_reason="Legal retention requirement",
                    completed_at=datetime.now(timezone.utc),
                    error_message=None
                )
                request.service_results.append(result)
                continue

            # Check legal holds
            if target.legal_hold_check:
                hold = self._check_legal_hold(subject_id, target.service_name)
                if hold:
                    result = ServiceDeletionResult(
                        service_name=target.service_name,
                        status=ServiceDeletionStatus.SKIPPED,
                        records_deleted=0,
                        records_retained=0,
                        retention_reason=f"Legal hold: {hold}",
                        completed_at=datetime.now(timezone.utc),
                        error_message=None
                    )
                    request.service_results.append(result)
                    continue

            # Execute deletion for this service
            result = self._delete_from_service(subject_id, target)
            request.service_results.append(result)

        # Determine overall status
        statuses = [r.status for r in request.service_results]
        if all(s in (ServiceDeletionStatus.COMPLETED, ServiceDeletionStatus.SKIPPED) for s in statuses):
            request.status = DeletionStatus.COMPLETED
        elif any(s == ServiceDeletionStatus.FAILED for s in statuses):
            request.status = DeletionStatus.PARTIALLY_COMPLETED
        else:
            request.status = DeletionStatus.COMPLETED

        self.audit.log_deletion_complete(request)
        return request

    def verify_deletion(self, request: DeletionRequest) -> DeletionRequest:
        """
        Verify that data was actually deleted from all services.
        Run after deletion to confirm no data remnants exist.
        """
        for result in request.service_results:
            if result.status == ServiceDeletionStatus.COMPLETED:
                # Attempt to query for the subject's data
                remaining = self._check_data_exists(
                    request.subject_id, result.service_name
                )
                if remaining > 0:
                    result.status = ServiceDeletionStatus.FAILED
                    result.error_message = f"Verification failed: {remaining} records still exist"

        request.verified_at = datetime.now(timezone.utc)
        request.verification_method = "post_deletion_query"

        all_verified = all(
            r.status in (ServiceDeletionStatus.COMPLETED, ServiceDeletionStatus.SKIPPED)
            for r in request.service_results
        )
        request.status = DeletionStatus.VERIFIED if all_verified else DeletionStatus.PARTIALLY_COMPLETED

        self.audit.log_deletion_verification(request)
        return request

    def _check_legal_hold(self, subject_id: str, service: str) -> Optional[str]:
        """Check if any legal hold applies to this subject's data."""
        # Integration point with legal hold management system
        return None  # Override in production with actual legal hold check

    def _delete_from_service(
        self, subject_id: str, target: DeletionTarget
    ) -> ServiceDeletionResult:
        """Execute deletion against a specific backend service."""
        # Integration point with actual backend service deletion API
        return ServiceDeletionResult(
            service_name=target.service_name,
            status=ServiceDeletionStatus.COMPLETED,
            records_deleted=0,
            records_retained=0,
            retention_reason=None,
            completed_at=datetime.now(timezone.utc),
            error_message=None
        )

    def _check_data_exists(self, subject_id: str, service: str) -> int:
        """Check if data still exists for a subject in a service."""
        # Integration point with service data existence check
        return 0
```

## 4. Audit API

### Audit Log Query Endpoints

```yaml
paths:
  /audit/events:
    get:
      operationId: queryAuditEvents
      summary: Query privacy audit events
      tags: [Audit]
      security:
        - OAuth2: [audit:read]
      parameters:
        - name: subjectId
          in: query
          schema:
            type: string
        - name: eventType
          in: query
          schema:
            type: string
            enum: [data_access, consent_change, deletion, dsar_submitted, dsar_completed, breach_detected]
        - name: startDate
          in: query
          required: true
          schema:
            type: string
            format: date-time
        - name: endDate
          in: query
          required: true
          schema:
            type: string
            format: date-time
        - name: actorId
          in: query
          schema:
            type: string
        - name: page
          in: query
          schema:
            type: integer
            default: 1
        - name: perPage
          in: query
          schema:
            type: integer
            default: 50
            maximum: 200
      responses:
        '200':
          description: Audit events
          content:
            application/json:
              schema:
                type: object
                properties:
                  events:
                    type: array
                    items:
                      type: object
                      properties:
                        eventId:
                          type: string
                          format: uuid
                        eventType:
                          type: string
                        timestamp:
                          type: string
                          format: date-time
                        actorId:
                          type: string
                        actorType:
                          type: string
                          enum: [user, system, admin, api_client]
                        subjectId:
                          type: string
                        resource:
                          type: string
                        action:
                          type: string
                        purpose:
                          type: string
                        outcome:
                          type: string
                          enum: [success, failure, denied]
                        details:
                          type: object
                  pagination:
                    $ref: '#/components/schemas/Pagination'

  /audit/reports/compliance:
    get:
      operationId: getComplianceReport
      summary: Generate compliance audit report for a date range
      tags: [Audit]
      parameters:
        - name: startDate
          in: query
          required: true
          schema:
            type: string
            format: date
        - name: endDate
          in: query
          required: true
          schema:
            type: string
            format: date
        - name: format
          in: query
          schema:
            type: string
            enum: [json, pdf, csv]
            default: json
      responses:
        '200':
          description: Compliance report
          content:
            application/json:
              schema:
                type: object
                properties:
                  reportId:
                    type: string
                  generatedAt:
                    type: string
                    format: date-time
                  period:
                    type: object
                    properties:
                      start:
                        type: string
                      end:
                        type: string
                  summary:
                    type: object
                    properties:
                      totalDataAccesses:
                        type: integer
                      totalConsentChanges:
                        type: integer
                      totalDeletions:
                        type: integer
                      totalDSARs:
                        type: integer
                      accessDenials:
                        type: integer
                      policyViolations:
                        type: integer
```

## API Security Patterns

### Authentication and Authorization

| Endpoint Category | Auth Method | Scopes Required | Rate Limit |
|-------------------|-------------|-----------------|------------|
| DSAR (data subject) | OAuth2 PKCE / JWT | dsar:read, dsar:write | 10 req/min |
| DSAR (admin) | OAuth2 Client Credentials | dsar:admin | 100 req/min |
| Consent (data subject) | OAuth2 PKCE / JWT | consent:read, consent:write | 30 req/min |
| Deletion (internal) | mTLS + API key | deletion:execute | 5 req/min |
| Audit (compliance) | OAuth2 Client Credentials | audit:read | 50 req/min |

### Error Response Format

```json
{
  "error": {
    "code": "PRIVACY_001",
    "type": "identity_verification_required",
    "message": "Identity verification is required before processing this request",
    "details": {
      "verificationMethods": ["email_verification", "document_upload"],
      "supportUrl": "https://support.cipherengineeringlabs.com/privacy"
    },
    "requestId": "req_a1b2c3d4",
    "timestamp": "2026-03-14T10:30:00.000Z"
  }
}
```

## References

- OpenAPI Specification 3.1.0
- GDPR Articles 12-22 (Data Subject Rights)
- CCPA/CPRA Sections 1798.100-1798.135
- RFC 6749 — OAuth 2.0 Authorization Framework
- RFC 7519 — JSON Web Token (JWT)
- OWASP API Security Top 10 (2023)
- Google Privacy Sandbox API Design Guidelines
- Apple App Tracking Transparency API Design Patterns
