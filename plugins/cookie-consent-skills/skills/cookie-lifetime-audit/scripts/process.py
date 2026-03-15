"""
Cookie Lifetime Auditor

Analyzes cookie lifetimes from a scan report and checks compliance
with CNIL 13-month maximum and browser ITP restrictions.

Requirements:
    pip install selenium webdriver-manager
"""

import json
import csv
import os
from datetime import datetime, timezone
from typing import Optional

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    print("Required packages not installed. Run:")
    print("pip install selenium webdriver-manager")
    raise


# Constants
CNIL_MAX_DAYS = 395  # ~13 months
SAFARI_ITP_JS_DAYS = 7
SAFARI_ITP_LINK_DECORATION_HOURS = 24


class CookieLifetimeAuditor:
    """Audits cookie lifetimes for regulatory and browser compliance."""

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.driver: Optional[webdriver.Chrome] = None
        self.cookies: list[dict] = []

    def setup_driver(self):
        """Initialize headless Chrome."""
        options = ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.set_page_load_timeout(30)

    def teardown_driver(self):
        if self.driver:
            self.driver.quit()

    def scan_cookies(self, urls: list[str]):
        """Scan pages and collect cookie lifetime data."""
        self.setup_driver()
        try:
            # First accept all cookies if possible
            self.driver.get(self.base_url)
            import time
            time.sleep(2)

            # Try to click accept button
            for selector in [
                '[data-testid="cookie-accept-all"]',
                '#cookie-accept',
                'button[class*="accept"]',
            ]:
                try:
                    btn = self.driver.find_element(By.CSS_SELECTOR, selector)
                    if btn.is_displayed():
                        btn.click()
                        time.sleep(2)
                        break
                except Exception:
                    continue

            # Scan all URLs
            for url in urls:
                full_url = url if url.startswith("http") else f"{self.base_url}{url}"
                try:
                    self.driver.get(full_url)
                    time.sleep(2)
                    self._collect_cookies()
                except Exception as e:
                    print(f"Error scanning {full_url}: {e}")
        finally:
            self.teardown_driver()

    def _collect_cookies(self):
        """Collect cookies with lifetime analysis."""
        browser_cookies = self.driver.get_cookies()
        now = datetime.now(timezone.utc)

        for cookie in browser_cookies:
            name = cookie.get("name", "")
            # Skip if already recorded
            if any(c["name"] == name and c["domain"] == cookie.get("domain", "") for c in self.cookies):
                continue

            expiry = cookie.get("expiry")
            is_session = expiry is None

            if expiry:
                expiry_dt = datetime.fromtimestamp(expiry, tz=timezone.utc)
                lifetime_seconds = max(0, (expiry_dt - now).total_seconds())
                lifetime_days = int(lifetime_seconds / 86400)
            else:
                lifetime_seconds = 0
                lifetime_days = 0

            # Determine if cookie is set by JavaScript or server
            # Heuristic: httpOnly cookies are likely server-set
            is_server_set = cookie.get("httpOnly", False)

            # Effective Safari ITP lifetime
            if is_session:
                safari_effective_days = 0  # Session cookie
            elif is_server_set:
                safari_effective_days = lifetime_days  # Server-set: no ITP cap
            else:
                safari_effective_days = min(lifetime_days, SAFARI_ITP_JS_DAYS)

            entry = {
                "name": name,
                "domain": cookie.get("domain", ""),
                "path": cookie.get("path", "/"),
                "is_session": is_session,
                "is_server_set": is_server_set,
                "secure": cookie.get("secure", False),
                "httpOnly": cookie.get("httpOnly", False),
                "sameSite": cookie.get("sameSite", "None"),
                "declared_lifetime_days": lifetime_days,
                "declared_lifetime_months": round(lifetime_days / 30, 1),
                "safari_effective_days": safari_effective_days,
                "exceeds_cnil_13_months": lifetime_days > CNIL_MAX_DAYS,
                "affected_by_safari_itp": (
                    not is_server_set and not is_session and lifetime_days > SAFARI_ITP_JS_DAYS
                ),
                "compliance_issues": [],
            }

            # Identify compliance issues
            if entry["exceeds_cnil_13_months"]:
                entry["compliance_issues"].append(
                    f"Exceeds CNIL 13-month maximum ({lifetime_days} days > {CNIL_MAX_DAYS} days)"
                )
            if entry["affected_by_safari_itp"]:
                entry["compliance_issues"].append(
                    f"Effective lifetime on Safari is {SAFARI_ITP_JS_DAYS} days, not {lifetime_days} days"
                )

            self.cookies.append(entry)

    def generate_report(self) -> dict:
        """Generate lifetime audit report."""
        exceeds_cnil = [c for c in self.cookies if c["exceeds_cnil_13_months"]]
        affected_itp = [c for c in self.cookies if c["affected_by_safari_itp"]]
        session_cookies = [c for c in self.cookies if c["is_session"]]
        persistent_cookies = [c for c in self.cookies if not c["is_session"]]

        # Duration distribution
        duration_buckets = {
            "session": len(session_cookies),
            "under_24h": len([c for c in persistent_cookies if c["declared_lifetime_days"] < 1]),
            "1_to_30_days": len([c for c in persistent_cookies if 1 <= c["declared_lifetime_days"] <= 30]),
            "30_days_to_13_months": len([c for c in persistent_cookies if 30 < c["declared_lifetime_days"] <= CNIL_MAX_DAYS]),
            "over_13_months": len(exceeds_cnil),
        }

        return {
            "metadata": {
                "base_url": self.base_url,
                "audit_date": datetime.now(timezone.utc).isoformat(),
                "total_cookies": len(self.cookies),
            },
            "summary": {
                "session_cookies": len(session_cookies),
                "persistent_cookies": len(persistent_cookies),
                "exceeding_cnil_13_months": len(exceeds_cnil),
                "affected_by_safari_itp": len(affected_itp),
                "server_set_cookies": len([c for c in self.cookies if c["is_server_set"]]),
                "js_set_cookies": len([c for c in self.cookies if not c["is_server_set"]]),
                "duration_distribution": duration_buckets,
            },
            "cookies_exceeding_cnil_limit": [
                {
                    "name": c["name"],
                    "domain": c["domain"],
                    "declared_lifetime_days": c["declared_lifetime_days"],
                    "declared_lifetime_months": c["declared_lifetime_months"],
                    "recommendation": f"Reduce to {CNIL_MAX_DAYS} days ({CNIL_MAX_DAYS / 30:.0f} months)",
                }
                for c in exceeds_cnil
            ],
            "cookies_affected_by_itp": [
                {
                    "name": c["name"],
                    "domain": c["domain"],
                    "declared_lifetime_days": c["declared_lifetime_days"],
                    "safari_effective_days": c["safari_effective_days"],
                    "recommendation": "Move to server-side cookie setting (Set-Cookie header)",
                }
                for c in affected_itp
            ],
            "all_cookies": self.cookies,
        }

    def export_report(self, output_dir: str):
        """Export report to JSON and CSV."""
        report = self.generate_report()
        os.makedirs(output_dir, exist_ok=True)

        # JSON report
        with open(os.path.join(output_dir, "lifetime_audit_report.json"), "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, default=str)

        # CSV summary
        with open(os.path.join(output_dir, "cookie_lifetimes.csv"), "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=[
                "name", "domain", "is_session", "is_server_set",
                "declared_lifetime_days", "declared_lifetime_months",
                "safari_effective_days", "exceeds_cnil_13_months",
                "affected_by_safari_itp",
            ])
            writer.writeheader()
            for cookie in self.cookies:
                writer.writerow({k: cookie.get(k, "") for k in writer.fieldnames})

        print(f"Reports exported to {output_dir}")
        return report


def main():
    """Run cookie lifetime audit for Pinnacle E-Commerce Ltd."""
    auditor = CookieLifetimeAuditor("https://www.pinnacle-ecommerce.com")

    urls = ["/", "/products", "/products/widget-pro", "/cart", "/about", "/blog"]
    auditor.scan_cookies(urls)

    output_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "reports")
    report = auditor.export_report(output_dir)

    print("\n=== Cookie Lifetime Audit Summary ===")
    print(f"Total cookies: {report['metadata']['total_cookies']}")
    print(f"Session cookies: {report['summary']['session_cookies']}")
    print(f"Persistent cookies: {report['summary']['persistent_cookies']}")
    print(f"Exceeding CNIL 13-month limit: {report['summary']['exceeding_cnil_13_months']}")
    print(f"Affected by Safari ITP: {report['summary']['affected_by_safari_itp']}")

    if report["cookies_exceeding_cnil_limit"]:
        print("\nCookies exceeding CNIL limit:")
        for c in report["cookies_exceeding_cnil_limit"]:
            print(f"  {c['name']}: {c['declared_lifetime_days']} days ({c['declared_lifetime_months']} months)")


if __name__ == "__main__":
    main()
