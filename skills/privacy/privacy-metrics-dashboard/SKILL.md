---
name: privacy-metrics-dashboard
description: >-
  Build privacy KPI dashboards tracking DSAR volume and response time, breach
  count and severity, DPIA completion rate, training coverage, and consent rates.
  Includes metric definitions, data collection patterns, visualization designs,
  and executive reporting templates for privacy program measurement.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-engineering
  tags: "privacy-metrics, kpi-dashboard, dsar-tracking, breach-metrics, privacy-reporting"
---

# Privacy Metrics Dashboard

## Overview

A privacy metrics dashboard provides quantitative visibility into the effectiveness and maturity of an organization's privacy program. This skill defines the key privacy performance indicators (KPIs), data collection methods, visualization patterns, and reporting cadences needed to measure, monitor, and continuously improve privacy operations.

## Core Privacy KPI Categories

### 1. Data Subject Access Requests (DSARs)

| Metric | Definition | Target | Frequency |
|--------|-----------|--------|-----------|
| DSAR Volume | Total DSARs received per period | Trend monitoring | Monthly |
| DSAR by Type | Breakdown by right exercised (access, deletion, portability, rectification) | N/A (distribution) | Monthly |
| Average Response Time | Mean calendar days from receipt to completion | < 25 days (GDPR: 30 day limit) | Monthly |
| Median Response Time | Median calendar days from receipt to completion | < 20 days | Monthly |
| P95 Response Time | 95th percentile response time | < 28 days | Monthly |
| On-Time Completion Rate | % completed within regulatory deadline | > 98% | Monthly |
| DSAR Backlog | Open DSARs at period end | < 10% of monthly volume | Weekly |
| Automated Fulfillment Rate | % of DSARs fulfilled without manual intervention | > 60% | Quarterly |
| Identity Verification Failure Rate | % of DSARs where identity could not be verified | < 5% | Monthly |
| Cost per DSAR | Average cost to process one DSAR | Trend reduction | Quarterly |

### 2. Data Breaches

| Metric | Definition | Target | Frequency |
|--------|-----------|--------|-----------|
| Breach Count | Total confirmed breaches per period | 0 (minimize) | Monthly |
| Breach Severity Distribution | Count by severity level (low/medium/high/critical) | No critical breaches | Monthly |
| Mean Time to Detect (MTTD) | Average hours from breach occurrence to detection | < 24 hours | Per incident |
| Mean Time to Notify (MTTN) | Average hours from detection to regulatory notification | < 48 hours (GDPR: 72 hours) | Per incident |
| Mean Time to Contain (MTTC) | Average hours from detection to containment | < 12 hours | Per incident |
| Records Affected | Total data subject records affected | Minimize | Per incident |
| Repeat Breach Rate | % of breaches with same root cause as prior breach | 0% | Quarterly |
| Regulatory Fines | Total fines imposed due to breaches | $0 | Annual |
| Breach Simulation Score | Score from most recent tabletop exercise | > 85% | Semi-annual |

### 3. Privacy Impact Assessments (DPIAs)

| Metric | Definition | Target | Frequency |
|--------|-----------|--------|-----------|
| DPIA Completion Rate | % of high-risk processing with completed DPIA | 100% | Quarterly |
| DPIA Backlog | DPIAs required but not yet started | 0 | Monthly |
| Average DPIA Duration | Mean days from initiation to sign-off | < 30 days | Quarterly |
| DPIA Findings Remediated | % of identified risks with implemented mitigations | > 90% | Quarterly |
| DPIA Review Rate | % of existing DPIAs reviewed within their review cycle | > 95% | Quarterly |
| New Processing Without DPIA | Count of new high-risk processing launched without DPIA | 0 | Monthly |

### 4. Training and Awareness

| Metric | Definition | Target | Frequency |
|--------|-----------|--------|-----------|
| Training Completion Rate | % of staff who completed required privacy training | > 95% | Quarterly |
| Training Pass Rate | % passing the assessment on first attempt | > 85% | Quarterly |
| New Hire Training Time | Average days from start date to training completion | < 14 days | Monthly |
| Specialist Certification Rate | % of privacy team with professional certification | > 80% | Annual |
| Privacy Champion Coverage | % of business units with designated privacy champion | 100% | Quarterly |
| Phishing Simulation Pass Rate | % of staff correctly identifying privacy-related phishing | > 90% | Quarterly |

### 5. Consent Management

| Metric | Definition | Target | Frequency |
|--------|-----------|--------|-----------|
| Consent Rate | % of users providing consent (by purpose) | Trend monitoring | Monthly |
| Opt-in Rate | % choosing to opt in to optional processing | Trend monitoring | Monthly |
| Opt-out/Withdrawal Rate | % withdrawing previously given consent | < 5% monthly | Monthly |
| Consent Freshness | % of active consents collected within last 12 months | > 70% | Quarterly |
| Consent Collection Coverage | % of data processing with documented consent/legal basis | 100% | Quarterly |
| Cookie Consent Rate | % of website visitors accepting cookies (by category) | Trend monitoring | Monthly |
| Consent Record Accuracy | % of consent records matching actual processing | > 99% | Quarterly |

### 6. Operational Metrics

| Metric | Definition | Target | Frequency |
|--------|-----------|--------|-----------|
| Privacy Incidents Reported | Internal privacy incidents reported (not just breaches) | Trend monitoring | Monthly |
| Vendor Privacy Assessments Completed | % of high-risk vendors assessed | 100% | Quarterly |
| Data Inventory Completeness | % of processing activities documented in ROPA | > 95% | Quarterly |
| Policy Acknowledgment Rate | % of staff acknowledging updated privacy policies | > 98% | Per update |
| Privacy-by-Design Gate Pass Rate | % of projects passing privacy review at design gate | > 85% | Quarterly |
| Regulatory Inquiry Response Time | Average days to respond to regulatory inquiries | < 5 days | Per event |

## Data Collection Architecture

```
Data Sources                    Collection Layer              Dashboard Layer
+------------------+
| DSAR Platform    |---+
+------------------+   |
                       |    +-------------------+    +-----------------------+
+------------------+   +--->|                   |    |                       |
| Breach Tracker   |------->| Data Integration  |--->| Visualization Engine  |
+------------------+   +--->| (ETL Pipeline)    |    | (Grafana / Tableau /  |
                       |    |                   |    |  Power BI / Metabase) |
+------------------+   |    +-------------------+    +-----------------------+
| DPIA Register    |---+           |                          |
+------------------+   |           v                          v
                       |    +-------------------+    +-----------------------+
+------------------+   |    | Metrics Database  |    | Alerting System       |
| LMS (Training)   |---+    | (Time-series /    |    | - Threshold breaches  |
+------------------+   |    |  PostgreSQL)      |    | - Trend deviations    |
                       |    +-------------------+    | - SLA warnings        |
+------------------+   |                              +-----------------------+
| Consent Platform |---+
+------------------+
```

## Metric Collection Implementation

```python
"""
Privacy metrics collection and aggregation engine.
Collects KPI data from multiple privacy operational systems
and computes dashboard-ready metrics.
"""

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional
import statistics


@dataclass
class DSARMetrics:
    period_start: datetime
    period_end: datetime
    total_received: int
    total_completed: int
    total_overdue: int
    avg_response_days: float
    median_response_days: float
    p95_response_days: float
    on_time_rate: float
    by_type: dict[str, int]
    backlog: int
    automated_rate: float


@dataclass
class BreachMetrics:
    period_start: datetime
    period_end: datetime
    total_breaches: int
    by_severity: dict[str, int]
    avg_detection_hours: float
    avg_notification_hours: float
    avg_containment_hours: float
    total_records_affected: int
    repeat_breach_count: int


@dataclass
class ConsentMetrics:
    period_start: datetime
    period_end: datetime
    total_consent_events: int
    opt_in_rate: float
    withdrawal_rate: float
    consent_rate_by_purpose: dict[str, float]
    cookie_acceptance_rate: float
    consent_freshness_pct: float


class PrivacyMetricsCollector:
    """
    Collect and compute privacy KPIs from operational data sources.
    """

    def __init__(self, dsar_repo, breach_repo, dpia_repo, training_repo, consent_repo):
        self.dsar_repo = dsar_repo
        self.breach_repo = breach_repo
        self.dpia_repo = dpia_repo
        self.training_repo = training_repo
        self.consent_repo = consent_repo

    def compute_dsar_metrics(
        self,
        start_date: datetime,
        end_date: datetime,
        regulatory_deadline_days: int = 30
    ) -> DSARMetrics:
        """Compute DSAR KPIs for a given period."""
        dsars = self.dsar_repo.get_by_period(start_date, end_date)

        completed = [d for d in dsars if d.status == "completed"]
        response_times = [
            (d.completed_at - d.received_at).days
            for d in completed
            if d.completed_at and d.received_at
        ]

        on_time = [
            d for d in completed
            if (d.completed_at - d.received_at).days <= regulatory_deadline_days
        ]

        automated = [d for d in completed if d.automated]
        open_dsars = [d for d in dsars if d.status in ("open", "in_progress")]

        by_type = {}
        for d in dsars:
            by_type[d.request_type] = by_type.get(d.request_type, 0) + 1

        return DSARMetrics(
            period_start=start_date,
            period_end=end_date,
            total_received=len(dsars),
            total_completed=len(completed),
            total_overdue=len(dsars) - len(on_time) - len(open_dsars),
            avg_response_days=statistics.mean(response_times) if response_times else 0,
            median_response_days=statistics.median(response_times) if response_times else 0,
            p95_response_days=(
                sorted(response_times)[int(len(response_times) * 0.95)]
                if len(response_times) >= 20 else
                max(response_times) if response_times else 0
            ),
            on_time_rate=len(on_time) / len(completed) if completed else 1.0,
            by_type=by_type,
            backlog=len(open_dsars),
            automated_rate=len(automated) / len(completed) if completed else 0,
        )

    def compute_breach_metrics(
        self,
        start_date: datetime,
        end_date: datetime
    ) -> BreachMetrics:
        """Compute breach KPIs for a given period."""
        breaches = self.breach_repo.get_by_period(start_date, end_date)

        by_severity = {}
        detection_hours = []
        notification_hours = []
        containment_hours = []
        total_records = 0

        for b in breaches:
            by_severity[b.severity] = by_severity.get(b.severity, 0) + 1
            total_records += b.records_affected or 0

            if b.detected_at and b.occurred_at:
                detection_hours.append(
                    (b.detected_at - b.occurred_at).total_seconds() / 3600
                )
            if b.notified_at and b.detected_at:
                notification_hours.append(
                    (b.notified_at - b.detected_at).total_seconds() / 3600
                )
            if b.contained_at and b.detected_at:
                containment_hours.append(
                    (b.contained_at - b.detected_at).total_seconds() / 3600
                )

        # Count repeat breaches (same root cause as previous)
        root_causes = [b.root_cause for b in breaches if b.root_cause]
        repeat_count = len(root_causes) - len(set(root_causes))

        return BreachMetrics(
            period_start=start_date,
            period_end=end_date,
            total_breaches=len(breaches),
            by_severity=by_severity,
            avg_detection_hours=statistics.mean(detection_hours) if detection_hours else 0,
            avg_notification_hours=statistics.mean(notification_hours) if notification_hours else 0,
            avg_containment_hours=statistics.mean(containment_hours) if containment_hours else 0,
            total_records_affected=total_records,
            repeat_breach_count=repeat_count,
        )

    def generate_executive_report(
        self,
        period_start: datetime,
        period_end: datetime
    ) -> dict:
        """
        Generate a comprehensive executive privacy report.
        Combines all KPI categories into a single report structure.
        """
        dsar = self.compute_dsar_metrics(period_start, period_end)
        breach = self.compute_breach_metrics(period_start, period_end)

        # Calculate overall privacy health score (0-100)
        health_components = []

        # DSAR component (25% weight)
        dsar_score = min(100, dsar.on_time_rate * 100)
        health_components.append(("DSAR Compliance", dsar_score, 0.25))

        # Breach component (30% weight)
        breach_score = 100 if breach.total_breaches == 0 else max(0, 100 - breach.total_breaches * 20)
        health_components.append(("Breach Prevention", breach_score, 0.30))

        # Response time component (20% weight)
        response_score = min(100, max(0, (30 - dsar.avg_response_days) / 30 * 100))
        health_components.append(("Response Timeliness", response_score, 0.20))

        # Detection speed component (25% weight)
        detection_score = min(100, max(0, (72 - breach.avg_detection_hours) / 72 * 100)) if breach.total_breaches > 0 else 100
        health_components.append(("Detection Speed", detection_score, 0.25))

        overall_score = sum(score * weight for _, score, weight in health_components)

        return {
            "period": {
                "start": period_start.isoformat(),
                "end": period_end.isoformat()
            },
            "overall_privacy_health_score": round(overall_score, 1),
            "health_rating": (
                "Excellent" if overall_score >= 90 else
                "Good" if overall_score >= 75 else
                "Needs Improvement" if overall_score >= 60 else
                "Critical"
            ),
            "components": {
                name: {"score": round(score, 1), "weight": f"{weight*100:.0f}%"}
                for name, score, weight in health_components
            },
            "dsar_summary": {
                "volume": dsar.total_received,
                "on_time_rate": f"{dsar.on_time_rate*100:.1f}%",
                "avg_response_days": round(dsar.avg_response_days, 1),
                "backlog": dsar.backlog
            },
            "breach_summary": {
                "count": breach.total_breaches,
                "severity_distribution": breach.by_severity,
                "avg_detection_hours": round(breach.avg_detection_hours, 1),
                "records_affected": breach.total_records_affected
            },
        }
```

## Dashboard Visualization Patterns

### Executive Summary View

| Panel | Chart Type | Metrics Displayed | Refresh Rate |
|-------|-----------|-------------------|-------------|
| Privacy Health Score | Gauge (0-100) | Overall weighted score | Daily |
| DSAR Volume Trend | Line chart | Monthly DSAR count (12-month rolling) | Daily |
| Breach Timeline | Event timeline | Breaches by severity over time | Real-time |
| On-Time Rate | Single stat with spark line | DSAR on-time completion % | Daily |
| Training Coverage | Horizontal bar | Completion rate by department | Weekly |
| Consent Rate Trend | Multi-line chart | Opt-in rate by purpose (6-month) | Daily |

### Operational View

| Panel | Chart Type | Metrics Displayed | Refresh Rate |
|-------|-----------|-------------------|-------------|
| Active DSARs | Table with status | Open requests with deadlines | Hourly |
| DSAR Aging | Histogram | Distribution of open DSAR ages | Daily |
| Response Time Box Plot | Box plot | Response time distribution by month | Daily |
| Breach Detection Funnel | Funnel chart | Detection > Assessment > Notification > Resolution | Per event |
| DPIA Pipeline | Kanban | DPIAs by status (draft, review, approved) | Daily |
| Vendor Risk Heat Map | Heat map | Vendors by risk score and last assessment date | Weekly |

## Alerting Rules

| Alert | Condition | Severity | Recipient |
|-------|-----------|----------|-----------|
| DSAR SLA Warning | Any DSAR open > 21 days | Warning | DSAR team |
| DSAR SLA Breach | Any DSAR open > 28 days | Critical | CPO + Legal |
| Breach Detected | New breach record created | Critical | Incident team + CPO |
| Training Compliance Drop | Department completion < 90% | Warning | HR + Privacy |
| Consent Rate Anomaly | Opt-in rate drops > 20% in a week | Warning | Privacy + Marketing |
| DPIA Overdue | DPIA review past scheduled date | Warning | DPIA owner + CPO |
| Vendor Assessment Due | High-risk vendor assessment > 11 months old | Warning | Procurement + Privacy |

## Executive Reporting Template

### Monthly Privacy Board Report Structure

1. **Privacy Health Score**: Overall score with trend arrow
2. **Key Highlights**: 3-5 bullet points on notable events
3. **DSAR Performance**: Volume, on-time rate, top request types
4. **Breach Status**: Count, severity, response times, lessons learned
5. **Compliance Posture**: DPIA coverage, training rates, policy updates
6. **Risk Outlook**: Emerging risks, regulatory developments, planned changes
7. **Resource Needs**: Budget requests, headcount, tooling

## References

- IAPP Privacy Program Management Guide (CIPM Body of Knowledge)
- NIST Privacy Framework — GV.MT Monitoring and Review
- ISO/IEC 27701:2019 — Clause 9 (Performance Evaluation)
- EDPB Guidelines on Data Breach Notification (WP250 rev.01)
- Gartner Privacy Program Metrics Framework
- ISACA Privacy Audit and Assurance Program
