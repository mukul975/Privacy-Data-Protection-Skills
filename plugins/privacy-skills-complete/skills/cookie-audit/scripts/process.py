"""
Cookie Audit Scanner and Report Generator

Scans a website using Selenium WebDriver to identify all cookies, localStorage,
and tracking technologies. Generates a structured audit report with classification
and compliance gap analysis.

Requirements:
    pip install selenium webdriver-manager requests tldextract
"""

import json
import hashlib
import csv
import os
import re
from datetime import datetime, timezone, timedelta
from urllib.parse import urlparse
from typing import Optional

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
    import tldextract
except ImportError:
    print("Required packages not installed. Run:")
    print("pip install selenium webdriver-manager requests tldextract")
    raise


# CNIL maximum cookie lifetime in seconds (13 months)
CNIL_MAX_LIFETIME_SECONDS = 13 * 30 * 24 * 60 * 60  # ~33,696,000 seconds

# Known cookie classifications
COOKIE_CLASSIFICATIONS = {
    # Strictly Necessary
    "session_id": {"category": "strictly_necessary", "purpose": "Session state management"},
    "csrf_token": {"category": "strictly_necessary", "purpose": "Cross-site request forgery protection"},
    "cart_items": {"category": "strictly_necessary", "purpose": "Shopping cart contents"},
    "cart_session": {"category": "strictly_necessary", "purpose": "Shopping cart session"},
    "auth_token": {"category": "strictly_necessary", "purpose": "User authentication"},
    "SERVERID": {"category": "strictly_necessary", "purpose": "Load balancer affinity"},
    "__cf_bm": {"category": "strictly_necessary", "purpose": "Cloudflare bot management"},
    "consent_state": {"category": "strictly_necessary", "purpose": "Cookie consent record"},

    # Analytics / Performance
    "_ga": {"category": "analytics", "purpose": "Google Analytics client ID"},
    "_ga_": {"category": "analytics", "purpose": "GA4 session persistence"},
    "_gid": {"category": "analytics", "purpose": "Google Analytics session distinction"},
    "_gat": {"category": "analytics", "purpose": "Google Analytics rate limiting"},
    "_hjSession": {"category": "analytics", "purpose": "Hotjar session data"},
    "_hjSessionUser": {"category": "analytics", "purpose": "Hotjar user identification"},
    "_hjid": {"category": "analytics", "purpose": "Hotjar user ID"},
    "_pk_id": {"category": "analytics", "purpose": "Matomo visitor ID"},
    "_pk_ses": {"category": "analytics", "purpose": "Matomo session"},

    # Functionality
    "locale": {"category": "functionality", "purpose": "Language preference"},
    "currency": {"category": "functionality", "purpose": "Currency selection"},
    "theme": {"category": "functionality", "purpose": "UI theme preference"},
    "recently_viewed": {"category": "functionality", "purpose": "Recently viewed products"},

    # Advertising / Targeting
    "_fbp": {"category": "advertising", "purpose": "Meta Pixel browser identification"},
    "_fbc": {"category": "advertising", "purpose": "Meta click identifier"},
    "_gcl_au": {"category": "advertising", "purpose": "Google Ads conversion linker"},
    "_gcl_aw": {"category": "advertising", "purpose": "Google Ads click conversion"},
    "IDE": {"category": "advertising", "purpose": "Google DoubleClick ad serving"},
    "fr": {"category": "advertising", "purpose": "Meta ad delivery and measurement"},
    "NID": {"category": "advertising", "purpose": "Google ad personalization"},
    "_uetsid": {"category": "advertising", "purpose": "Microsoft Bing Ads session"},
    "_uetvid": {"category": "advertising", "purpose": "Microsoft Bing Ads user"},
    "li_sugr": {"category": "advertising", "purpose": "LinkedIn ad targeting"},
}

# Known tracking domains
TRACKING_DOMAINS = {
    "google-analytics.com": "Google Analytics",
    "analytics.google.com": "Google Analytics",
    "googletagmanager.com": "Google Tag Manager",
    "doubleclick.net": "Google Ads",
    "googlesyndication.com": "Google Ads",
    "facebook.com": "Meta",
    "facebook.net": "Meta",
    "connect.facebook.net": "Meta Pixel",
    "hotjar.com": "Hotjar",
    "clarity.ms": "Microsoft Clarity",
    "bat.bing.com": "Microsoft Ads",
    "linkedin.com": "LinkedIn",
    "snap.licdn.com": "LinkedIn Insight",
    "tiktok.com": "TikTok",
    "analytics.tiktok.com": "TikTok Pixel",
    "criteo.com": "Criteo",
    "criteo.net": "Criteo",
    "taboola.com": "Taboola",
    "outbrain.com": "Outbrain",
}


class CookieAuditScanner:
    """Scans a website for cookies and tracking technologies."""

    def __init__(self, base_url: str, headless: bool = True):
        self.base_url = base_url.rstrip("/")
        self.headless = headless
        self.driver: Optional[webdriver.Chrome] = None
        self.cookies_found: list[dict] = []
        self.local_storage_found: list[dict] = []
        self.network_requests: list[dict] = []
        self.tracking_requests: list[dict] = []
        self.pages_scanned: list[str] = []

    def setup_driver(self):
        """Initialize Chrome WebDriver with cookie monitoring."""
        options = ChromeOptions()
        if self.headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--window-size=1920,1080")
        # Enable performance logging for network monitoring
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.set_page_load_timeout(30)

    def teardown_driver(self):
        """Close the browser."""
        if self.driver:
            self.driver.quit()

    def scan_page(self, url: str):
        """Scan a single page for cookies and tracking."""
        try:
            self.driver.get(url)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            # Wait for network activity to settle
            import time
            time.sleep(3)

            self.pages_scanned.append(url)
            self._collect_cookies()
            self._collect_local_storage()
            self._collect_network_requests()

        except Exception as e:
            print(f"Error scanning {url}: {e}")

    def _collect_cookies(self):
        """Collect all cookies from the current page."""
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            cookie_entry = {
                "name": cookie.get("name", ""),
                "domain": cookie.get("domain", ""),
                "path": cookie.get("path", "/"),
                "value_hash": hashlib.sha256(
                    cookie.get("value", "").encode()
                ).hexdigest()[:16],
                "secure": cookie.get("secure", False),
                "httpOnly": cookie.get("httpOnly", False),
                "sameSite": cookie.get("sameSite", "None"),
                "expiry": cookie.get("expiry"),
                "session": cookie.get("expiry") is None,
                "scanned_at": datetime.now(timezone.utc).isoformat(),
                "page_url": self.driver.current_url,
            }

            # Calculate lifetime
            if cookie_entry["expiry"]:
                expiry_dt = datetime.fromtimestamp(
                    cookie_entry["expiry"], tz=timezone.utc
                )
                now = datetime.now(timezone.utc)
                lifetime_seconds = (expiry_dt - now).total_seconds()
                cookie_entry["lifetime_seconds"] = max(0, int(lifetime_seconds))
                cookie_entry["lifetime_days"] = max(
                    0, int(lifetime_seconds / 86400)
                )
                cookie_entry["exceeds_cnil_13_months"] = (
                    lifetime_seconds > CNIL_MAX_LIFETIME_SECONDS
                )
            else:
                cookie_entry["lifetime_seconds"] = 0
                cookie_entry["lifetime_days"] = 0
                cookie_entry["exceeds_cnil_13_months"] = False

            # Classify cookie
            classification = self._classify_cookie(cookie_entry["name"])
            cookie_entry["category"] = classification["category"]
            cookie_entry["purpose"] = classification["purpose"]
            cookie_entry["consent_required"] = classification[
                "category"
            ] != "strictly_necessary"

            # Check for duplicates
            if not any(
                c["name"] == cookie_entry["name"]
                and c["domain"] == cookie_entry["domain"]
                for c in self.cookies_found
            ):
                self.cookies_found.append(cookie_entry)

    def _classify_cookie(self, cookie_name: str) -> dict:
        """Classify a cookie based on known patterns."""
        # Exact match
        if cookie_name in COOKIE_CLASSIFICATIONS:
            return COOKIE_CLASSIFICATIONS[cookie_name]

        # Prefix match
        for prefix, classification in COOKIE_CLASSIFICATIONS.items():
            if cookie_name.startswith(prefix):
                return classification

        # Unknown cookie
        return {
            "category": "unknown",
            "purpose": "Unknown — requires manual classification",
        }

    def _collect_local_storage(self):
        """Collect localStorage and sessionStorage entries."""
        try:
            local_items = self.driver.execute_script(
                """
                var items = {};
                for (var i = 0; i < localStorage.length; i++) {
                    var key = localStorage.key(i);
                    items[key] = localStorage.getItem(key).substring(0, 100);
                }
                return items;
            """
            )
            for key, value_preview in (local_items or {}).items():
                if not any(
                    ls["key"] == key for ls in self.local_storage_found
                ):
                    self.local_storage_found.append(
                        {
                            "key": key,
                            "value_preview": value_preview,
                            "storage_type": "localStorage",
                            "page_url": self.driver.current_url,
                        }
                    )
        except Exception:
            pass

        try:
            session_items = self.driver.execute_script(
                """
                var items = {};
                for (var i = 0; i < sessionStorage.length; i++) {
                    var key = sessionStorage.key(i);
                    items[key] = sessionStorage.getItem(key).substring(0, 100);
                }
                return items;
            """
            )
            for key, value_preview in (session_items or {}).items():
                if not any(
                    ls["key"] == key and ls["storage_type"] == "sessionStorage"
                    for ls in self.local_storage_found
                ):
                    self.local_storage_found.append(
                        {
                            "key": key,
                            "value_preview": value_preview,
                            "storage_type": "sessionStorage",
                            "page_url": self.driver.current_url,
                        }
                    )
        except Exception:
            pass

    def _collect_network_requests(self):
        """Analyze performance logs for tracking network requests."""
        try:
            logs = self.driver.get_log("performance")
            for entry in logs:
                try:
                    log_data = json.loads(entry["message"])
                    message = log_data.get("message", {})

                    if message.get("method") == "Network.requestWillBeSent":
                        request_url = (
                            message.get("params", {})
                            .get("request", {})
                            .get("url", "")
                        )
                        parsed = urlparse(request_url)
                        domain = parsed.netloc

                        for tracking_domain, vendor in TRACKING_DOMAINS.items():
                            if tracking_domain in domain:
                                self.tracking_requests.append(
                                    {
                                        "url": request_url[:200],
                                        "domain": domain,
                                        "vendor": vendor,
                                        "page_url": self.driver.current_url,
                                    }
                                )
                                break
                except (json.JSONDecodeError, KeyError):
                    continue
        except Exception:
            pass

    def run_full_audit(self, urls: list[str]):
        """Run a complete cookie audit across multiple URLs."""
        print(f"Starting cookie audit for {self.base_url}")
        print(f"Scanning {len(urls)} pages...")

        self.setup_driver()

        try:
            for i, url in enumerate(urls):
                full_url = (
                    url if url.startswith("http") else f"{self.base_url}{url}"
                )
                print(f"  [{i + 1}/{len(urls)}] Scanning: {full_url}")
                self.scan_page(full_url)
        finally:
            self.teardown_driver()

        return self.generate_report()

    def generate_report(self) -> dict:
        """Generate a structured audit report."""
        # Categorize cookies
        by_category = {}
        for cookie in self.cookies_found:
            cat = cookie["category"]
            if cat not in by_category:
                by_category[cat] = []
            by_category[cat].append(cookie)

        # Identify compliance gaps
        gaps = []

        # Check for cookies exceeding CNIL 13-month limit
        for cookie in self.cookies_found:
            if cookie["exceeds_cnil_13_months"]:
                gaps.append(
                    {
                        "cookie": cookie["name"],
                        "gap": "Exceeds CNIL 13-month maximum lifetime",
                        "severity": "high",
                        "current_lifetime_days": cookie["lifetime_days"],
                        "recommendation": f"Reduce cookie lifetime to 395 days (13 months) or less",
                    }
                )

        # Check for unknown cookies
        unknown_cookies = [
            c for c in self.cookies_found if c["category"] == "unknown"
        ]
        for cookie in unknown_cookies:
            gaps.append(
                {
                    "cookie": cookie["name"],
                    "gap": "Unclassified cookie — category and purpose unknown",
                    "severity": "medium",
                    "recommendation": "Classify cookie and add to cookie policy",
                }
            )

        # Unique tracking vendors
        vendors = list(
            set(r["vendor"] for r in self.tracking_requests)
        )

        report = {
            "audit_metadata": {
                "base_url": self.base_url,
                "scan_date": datetime.now(timezone.utc).isoformat(),
                "pages_scanned": len(self.pages_scanned),
                "total_cookies_found": len(self.cookies_found),
                "total_local_storage_entries": len(self.local_storage_found),
                "total_tracking_requests": len(self.tracking_requests),
                "unique_tracking_vendors": len(vendors),
            },
            "summary": {
                "cookies_by_category": {
                    cat: len(cookies) for cat, cookies in by_category.items()
                },
                "consent_required_cookies": len(
                    [c for c in self.cookies_found if c["consent_required"]]
                ),
                "exempt_cookies": len(
                    [c for c in self.cookies_found if not c["consent_required"]]
                ),
                "cookies_exceeding_cnil_limit": len(
                    [
                        c
                        for c in self.cookies_found
                        if c["exceeds_cnil_13_months"]
                    ]
                ),
                "unknown_cookies": len(unknown_cookies),
                "tracking_vendors": vendors,
            },
            "cookies": self.cookies_found,
            "local_storage": self.local_storage_found,
            "tracking_requests": self.tracking_requests,
            "compliance_gaps": gaps,
            "pages_scanned": self.pages_scanned,
        }

        return report

    def export_csv(self, report: dict, output_path: str):
        """Export the cookie inventory to CSV."""
        csv_path = os.path.join(output_path, "cookie_inventory.csv")
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "name",
                    "domain",
                    "category",
                    "purpose",
                    "lifetime_days",
                    "session",
                    "secure",
                    "httpOnly",
                    "sameSite",
                    "consent_required",
                    "exceeds_cnil_13_months",
                ],
            )
            writer.writeheader()
            for cookie in report["cookies"]:
                writer.writerow(
                    {k: cookie.get(k, "") for k in writer.fieldnames}
                )

        gaps_path = os.path.join(output_path, "compliance_gaps.csv")
        with open(gaps_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "cookie",
                    "gap",
                    "severity",
                    "recommendation",
                ],
            )
            writer.writeheader()
            for gap in report["compliance_gaps"]:
                writer.writerow({k: gap.get(k, "") for k in writer.fieldnames})

        print(f"CSV reports exported to {output_path}")

    def export_json(self, report: dict, output_path: str):
        """Export the full audit report to JSON."""
        json_path = os.path.join(output_path, "cookie_audit_report.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, default=str)

        print(f"JSON report exported to {json_path}")


def main():
    """Run a cookie audit for Pinnacle E-Commerce Ltd."""
    scanner = CookieAuditScanner(
        base_url="https://www.pinnacle-ecommerce.com", headless=True
    )

    # Define pages to scan
    pages_to_scan = [
        "/",
        "/products",
        "/products/widget-pro",
        "/cart",
        "/account/login",
        "/about",
        "/blog",
        "/contact",
        "/privacy-policy",
        "/cookie-policy",
    ]

    report = scanner.run_full_audit(pages_to_scan)

    # Create output directory
    output_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "reports")
    os.makedirs(output_dir, exist_ok=True)

    # Export reports
    scanner.export_json(report, output_dir)
    scanner.export_csv(report, output_dir)

    # Print summary
    print("\n=== Cookie Audit Summary ===")
    print(f"Pages scanned: {report['audit_metadata']['pages_scanned']}")
    print(f"Total cookies found: {report['audit_metadata']['total_cookies_found']}")
    print(f"Cookies by category:")
    for cat, count in report["summary"]["cookies_by_category"].items():
        print(f"  {cat}: {count}")
    print(f"Consent required: {report['summary']['consent_required_cookies']}")
    print(f"Exempt (strictly necessary): {report['summary']['exempt_cookies']}")
    print(
        f"Exceeding CNIL 13-month limit: {report['summary']['cookies_exceeding_cnil_limit']}"
    )
    print(f"Unknown/unclassified: {report['summary']['unknown_cookies']}")
    print(f"Tracking vendors: {', '.join(report['summary']['tracking_vendors'])}")
    print(f"Compliance gaps: {len(report['compliance_gaps'])}")


if __name__ == "__main__":
    main()
