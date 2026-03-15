#!/usr/bin/env python3
"""
DSAR Response Timeline Generator

Calculates the full timeline for a Data Subject Access Request (DSAR)
under GDPR Article 15, including identity verification pauses,
extensions for complex requests, and business day adjustments.
"""

import argparse
import json
from datetime import datetime, timedelta
from typing import Optional


# Public holidays for the UK (2025-2026) — extend as needed
UK_PUBLIC_HOLIDAYS = {
    "2025-01-01",  # New Year's Day
    "2025-04-18",  # Good Friday
    "2025-04-21",  # Easter Monday
    "2025-05-05",  # Early May Bank Holiday
    "2025-05-26",  # Spring Bank Holiday
    "2025-08-25",  # Summer Bank Holiday
    "2025-12-25",  # Christmas Day
    "2025-12-26",  # Boxing Day
    "2026-01-01",  # New Year's Day
    "2026-04-03",  # Good Friday
    "2026-04-06",  # Easter Monday
    "2026-05-04",  # Early May Bank Holiday
    "2026-05-25",  # Spring Bank Holiday
    "2026-08-31",  # Summer Bank Holiday
    "2026-12-25",  # Christmas Day
    "2026-12-28",  # Boxing Day (substitute)
}


def is_business_day(date: datetime, holidays: set) -> bool:
    """Check if a date is a business day (not weekend or public holiday)."""
    if date.weekday() >= 5:
        return False
    if date.strftime("%Y-%m-%d") in holidays:
        return False
    return True


def next_business_day(date: datetime, holidays: set) -> datetime:
    """
    If date falls on a weekend or public holiday, move to the next business day.
    Per Regulation (EEC, Euratom) No 1182/71, Article 3.
    """
    while not is_business_day(date, holidays):
        date += timedelta(days=1)
    return date


def calculate_dsar_timeline(
    request_date: str,
    identity_verified: bool = True,
    verification_date: Optional[str] = None,
    is_complex: bool = False,
    extension_days: int = 0,
    holidays: Optional[set] = None,
) -> dict:
    """
    Calculate the full DSAR response timeline.

    Args:
        request_date: Date the DSAR was received (YYYY-MM-DD).
        identity_verified: Whether identity was verified at time of request.
        verification_date: Date identity was verified (YYYY-MM-DD), if not immediate.
        is_complex: Whether the request qualifies for an extension.
        extension_days: Number of extension days (max 60) under Art. 12(3).
        holidays: Set of public holiday date strings (YYYY-MM-DD).

    Returns:
        Dictionary containing all timeline milestones.
    """
    if holidays is None:
        holidays = UK_PUBLIC_HOLIDAYS

    req_date = datetime.strptime(request_date, "%Y-%m-%d")
    timeline = {
        "request_received": req_date.strftime("%Y-%m-%d"),
        "reference_number": f"DSAR-{req_date.strftime('%Y')}-{req_date.strftime('%m%d')}",
    }

    # Acknowledgement: within 3 business days
    ack_date = req_date
    biz_days_counted = 0
    while biz_days_counted < 3:
        ack_date += timedelta(days=1)
        if is_business_day(ack_date, holidays):
            biz_days_counted += 1
    timeline["acknowledgement_due"] = ack_date.strftime("%Y-%m-%d")

    # Determine the clock start date
    if identity_verified:
        clock_start = req_date
        timeline["identity_verification"] = "Verified at receipt"
    elif verification_date:
        ver_date = datetime.strptime(verification_date, "%Y-%m-%d")
        clock_start = ver_date
        pause_days = (ver_date - req_date).days
        timeline["identity_verification"] = ver_date.strftime("%Y-%m-%d")
        timeline["verification_pause_days"] = pause_days
        timeline["verification_id_request_due"] = (
            req_date + timedelta(days=10)
        ).strftime("%Y-%m-%d")
    else:
        # Identity not yet verified — clock has not started
        clock_start = req_date
        timeline["identity_verification"] = "PENDING — clock paused"
        timeline["verification_id_request_due"] = (
            req_date + timedelta(days=10)
        ).strftime("%Y-%m-%d")
        timeline["warning"] = (
            "Response deadline cannot be calculated until identity is verified"
        )
        return timeline

    # Standard 30-day deadline (Art. 12(3))
    # Clock starts the day AFTER receipt/verification
    standard_deadline = clock_start + timedelta(days=30)
    standard_deadline = next_business_day(standard_deadline, holidays)
    timeline["standard_deadline"] = standard_deadline.strftime("%Y-%m-%d")

    # Extension notification deadline (must notify within initial 30 days)
    if is_complex:
        extension_days = min(extension_days, 60)
        if extension_days <= 0:
            extension_days = 60  # Default to maximum extension

        extension_notify_deadline = standard_deadline
        timeline["extension_notification_due"] = extension_notify_deadline.strftime(
            "%Y-%m-%d"
        )

        extended_deadline = clock_start + timedelta(days=30 + extension_days)
        extended_deadline = next_business_day(extended_deadline, holidays)
        timeline["extended_deadline"] = extended_deadline.strftime("%Y-%m-%d")
        timeline["extension_days"] = extension_days
        timeline["final_deadline"] = extended_deadline.strftime("%Y-%m-%d")
    else:
        timeline["final_deadline"] = standard_deadline.strftime("%Y-%m-%d")

    # Internal milestones
    final_deadline = datetime.strptime(timeline["final_deadline"], "%Y-%m-%d")
    days_available = (final_deadline - clock_start).days

    # Data collection should complete by 50% of available time
    collection_date = clock_start + timedelta(days=int(days_available * 0.5))
    collection_date = next_business_day(collection_date, holidays)
    timeline["data_collection_target"] = collection_date.strftime("%Y-%m-%d")

    # Exemption review by 65% of available time
    exemption_date = clock_start + timedelta(days=int(days_available * 0.65))
    exemption_date = next_business_day(exemption_date, holidays)
    timeline["exemption_review_target"] = exemption_date.strftime("%Y-%m-%d")

    # QA review by 80% of available time
    qa_date = clock_start + timedelta(days=int(days_available * 0.8))
    qa_date = next_business_day(qa_date, holidays)
    timeline["qa_review_target"] = qa_date.strftime("%Y-%m-%d")

    # DPO sign-off by 90% of available time
    signoff_date = clock_start + timedelta(days=int(days_available * 0.9))
    signoff_date = next_business_day(signoff_date, holidays)
    timeline["dpo_signoff_target"] = signoff_date.strftime("%Y-%m-%d")

    return timeline


def format_timeline_report(timeline: dict) -> str:
    """Format the timeline as a human-readable report."""
    lines = [
        "=" * 60,
        "DSAR RESPONSE TIMELINE REPORT",
        "=" * 60,
        f"Reference:            {timeline.get('reference_number', 'N/A')}",
        f"Request Received:     {timeline['request_received']}",
        f"Acknowledgement Due:  {timeline.get('acknowledgement_due', 'N/A')}",
        "",
        "--- Identity Verification ---",
        f"Status:               {timeline.get('identity_verification', 'N/A')}",
    ]

    if "verification_pause_days" in timeline:
        lines.append(
            f"Pause Duration:       {timeline['verification_pause_days']} days"
        )
    if "verification_id_request_due" in timeline:
        lines.append(
            f"ID Request Due By:    {timeline['verification_id_request_due']}"
        )

    if "warning" in timeline:
        lines.extend(
            [
                "",
                f"WARNING: {timeline['warning']}",
                "=" * 60,
            ]
        )
        return "\n".join(lines)

    lines.extend(
        [
            "",
            "--- Deadlines ---",
            f"Standard Deadline:    {timeline.get('standard_deadline', 'N/A')} (30 calendar days)",
        ]
    )

    if "extension_days" in timeline:
        lines.extend(
            [
                f"Extension Applied:    {timeline['extension_days']} additional days (Art. 12(3))",
                f"Extension Notice Due: {timeline.get('extension_notification_due', 'N/A')}",
                f"Extended Deadline:    {timeline.get('extended_deadline', 'N/A')}",
            ]
        )

    lines.extend(
        [
            f"FINAL DEADLINE:       {timeline['final_deadline']}",
            "",
            "--- Internal Milestones ---",
            f"Data Collection By:   {timeline.get('data_collection_target', 'N/A')}",
            f"Exemption Review By:  {timeline.get('exemption_review_target', 'N/A')}",
            f"QA Review By:         {timeline.get('qa_review_target', 'N/A')}",
            f"DPO Sign-off By:      {timeline.get('dpo_signoff_target', 'N/A')}",
            "=" * 60,
        ]
    )

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Calculate DSAR response timeline under GDPR Article 15"
    )
    parser.add_argument(
        "request_date",
        help="Date the DSAR was received (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--not-verified",
        action="store_true",
        help="Identity has not been verified at time of request",
    )
    parser.add_argument(
        "--verification-date",
        help="Date identity was verified (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--complex",
        action="store_true",
        help="Flag the request as complex (enables extension)",
    )
    parser.add_argument(
        "--extension-days",
        type=int,
        default=60,
        help="Number of extension days (max 60, default 60)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON instead of formatted report",
    )

    args = parser.parse_args()

    timeline = calculate_dsar_timeline(
        request_date=args.request_date,
        identity_verified=not args.not_verified,
        verification_date=args.verification_date,
        is_complex=args.complex,
        extension_days=args.extension_days,
    )

    if args.json:
        print(json.dumps(timeline, indent=2))
    else:
        print(format_timeline_report(timeline))


if __name__ == "__main__":
    main()
