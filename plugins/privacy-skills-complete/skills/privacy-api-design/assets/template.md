# Privacy API Design — Configuration Template

## API Overview

| Field | Value |
|-------|-------|
| Base URL | |
| API Version | |
| Authentication | OAuth2 / JWT / API Key |
| Rate Limiting | |

## Endpoints

### DSAR API

| Method | Path | Auth Scope | Rate Limit | Description |
|--------|------|-----------|------------|-------------|
| POST | /dsar/requests | dsar:write | 10/min | Submit DSAR |
| GET | /dsar/requests | dsar:read | 30/min | List DSARs |
| GET | /dsar/requests/{id} | dsar:read | 30/min | Get status |
| GET | /dsar/requests/{id}/download | dsar:read | 5/min | Download data |

### Consent API

| Method | Path | Auth Scope | Rate Limit | Description |
|--------|------|-----------|------------|-------------|
| GET | /consent/preferences | consent:read | 30/min | Get preferences |
| PUT | /consent/preferences | consent:write | 10/min | Update preferences |
| GET | /consent/purposes | consent:read | 60/min | List purposes |

### Deletion API

| Method | Path | Auth Scope | Rate Limit | Description |
|--------|------|-----------|------------|-------------|
| POST | /deletion/requests | deletion:write | 5/min | Submit deletion |
| GET | /deletion/requests/{id} | deletion:read | 10/min | Get status |

### Audit API

| Method | Path | Auth Scope | Rate Limit | Description |
|--------|------|-----------|------------|-------------|
| GET | /audit/events | audit:read | 50/min | Query events |
| GET | /audit/reports | audit:read | 5/min | Generate report |

## Error Codes

| Code | Type | Description |
|------|------|-------------|
| PRIVACY_001 | identity_verification_required | Identity must be verified |
| PRIVACY_002 | invalid_purpose | Purpose ID not recognized |
| PRIVACY_003 | consent_required | Consent needed for operation |
| PRIVACY_004 | deletion_blocked | Legal hold prevents deletion |
| PRIVACY_005 | rate_limited | Too many requests |

## Sign-Off

| Role | Name | Date |
|------|------|------|
| API Architect | | |
| Privacy Engineer | | |
| Security Engineer | | |
