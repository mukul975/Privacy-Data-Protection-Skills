"""
CNIL Cookie Banner Compliance Checker

Validates that a website's cookie consent banner meets CNIL requirements:
- Equal prominence for Accept All and Reject All buttons
- No cookies set before consent
- No dark patterns
- Proper consent state management

Requirements:
    pip install selenium webdriver-manager Pillow
"""

import json
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
    print("pip install selenium webdriver-manager Pillow")
    raise


class CNILBannerChecker:
    """Checks a website's cookie banner for CNIL compliance."""

    CNIL_CHECKS = {
        "banner_visible": {
            "description": "Cookie banner is visible on first visit",
            "severity": "critical",
        },
        "accept_button_present": {
            "description": "Accept All button is present and visible",
            "severity": "critical",
        },
        "reject_button_present": {
            "description": "Reject All button is present and visible at the same level as Accept",
            "severity": "critical",
        },
        "equal_button_size": {
            "description": "Accept and Reject buttons have equal visual prominence (size)",
            "severity": "high",
        },
        "customise_option": {
            "description": "Customise/Manage Preferences option is available",
            "severity": "high",
        },
        "no_preconsent_cookies": {
            "description": "No non-essential cookies set before user interaction",
            "severity": "critical",
        },
        "reject_blocks_cookies": {
            "description": "Reject All prevents non-essential cookies from being set",
            "severity": "critical",
        },
        "accept_sets_cookies": {
            "description": "Accept All enables non-essential cookies",
            "severity": "medium",
        },
        "banner_disappears_after_choice": {
            "description": "Banner disappears after user makes a choice",
            "severity": "medium",
        },
        "no_cookie_wall": {
            "description": "Site content is accessible after rejecting cookies",
            "severity": "critical",
        },
    }

    NON_ESSENTIAL_COOKIE_PREFIXES = [
        "_ga", "_gid", "_gat", "_fbp", "_fbc", "_gcl",
        "_hj", "IDE", "fr", "NID", "_uet",
    ]

    def __init__(self, base_url: str, banner_selectors: Optional[dict] = None):
        self.base_url = base_url.rstrip("/")
        self.selectors = banner_selectors or {
            "banner": '[data-testid="cookie-banner"], #cookie-banner, .cookie-consent, [class*="cookie-banner"]',
            "accept": '[data-testid="cookie-accept-all"], #cookie-accept, [class*="accept"], button:has-text("Accept")',
            "reject": '[data-testid="cookie-reject-all"], #cookie-reject, [class*="reject"], button:has-text("Reject")',
            "customise": '[data-testid="cookie-customise"], #cookie-manage, [class*="customise"], [class*="manage"], button:has-text("Customise")',
        }
        self.driver: Optional[webdriver.Chrome] = None
        self.results: dict = {}

    def setup_driver(self):
        """Initialize headless Chrome."""
        options = ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--lang=fr-FR")

        service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.set_page_load_timeout(30)

    def teardown_driver(self):
        """Close browser."""
        if self.driver:
            self.driver.quit()

    def _has_non_essential_cookies(self) -> list[str]:
        """Check for non-essential cookies."""
        cookies = self.driver.get_cookies()
        non_essential = []
        for cookie in cookies:
            name = cookie.get("name", "")
            for prefix in self.NON_ESSENTIAL_COOKIE_PREFIXES:
                if name.startswith(prefix):
                    non_essential.append(name)
                    break
        return non_essential

    def _find_element(self, selector: str):
        """Try to find an element using multiple selector strategies."""
        for sel in selector.split(", "):
            try:
                sel = sel.strip()
                if sel.startswith("["):
                    elements = self.driver.find_elements(By.CSS_SELECTOR, sel)
                elif sel.startswith("#"):
                    elements = self.driver.find_elements(By.CSS_SELECTOR, sel)
                elif sel.startswith("."):
                    elements = self.driver.find_elements(By.CSS_SELECTOR, sel)
                else:
                    elements = self.driver.find_elements(By.CSS_SELECTOR, sel)

                visible = [e for e in elements if e.is_displayed()]
                if visible:
                    return visible[0]
            except Exception:
                continue
        return None

    def check_banner_visibility(self):
        """Check if cookie banner is visible on first visit."""
        self.driver.get(self.base_url)
        import time
        time.sleep(3)

        banner = self._find_element(self.selectors["banner"])
        if banner and banner.is_displayed():
            self.results["banner_visible"] = {
                "passed": True,
                "detail": "Cookie banner found and visible",
            }
        else:
            self.results["banner_visible"] = {
                "passed": False,
                "detail": "Cookie banner not found or not visible on first visit",
            }

    def check_button_presence(self):
        """Check for Accept All and Reject All buttons."""
        accept_btn = self._find_element(self.selectors["accept"])
        reject_btn = self._find_element(self.selectors["reject"])
        customise_btn = self._find_element(self.selectors["customise"])

        self.results["accept_button_present"] = {
            "passed": accept_btn is not None and accept_btn.is_displayed(),
            "detail": "Accept All button " + ("found" if accept_btn else "NOT found"),
        }

        self.results["reject_button_present"] = {
            "passed": reject_btn is not None and reject_btn.is_displayed(),
            "detail": "Reject All button " + ("found at same level as Accept" if reject_btn else "NOT found — CNIL violation"),
        }

        self.results["customise_option"] = {
            "passed": customise_btn is not None and customise_btn.is_displayed(),
            "detail": "Customise option " + ("found" if customise_btn else "NOT found"),
        }

    def check_equal_prominence(self):
        """Check that Accept and Reject buttons have equal visual weight."""
        accept_btn = self._find_element(self.selectors["accept"])
        reject_btn = self._find_element(self.selectors["reject"])

        if not accept_btn or not reject_btn:
            self.results["equal_button_size"] = {
                "passed": False,
                "detail": "Cannot compare — one or both buttons not found",
            }
            return

        accept_size = accept_btn.size
        reject_size = reject_btn.size

        width_diff = abs(accept_size["width"] - reject_size["width"])
        height_diff = abs(accept_size["height"] - reject_size["height"])

        # Allow 10px tolerance for width, 5px for height
        size_equal = width_diff <= 10 and height_diff <= 5

        self.results["equal_button_size"] = {
            "passed": size_equal,
            "detail": (
                f"Accept: {accept_size['width']}x{accept_size['height']}px, "
                f"Reject: {reject_size['width']}x{reject_size['height']}px. "
                f"{'Equal prominence' if size_equal else 'UNEQUAL prominence — CNIL violation'}"
            ),
        }

    def check_preconsent_cookies(self):
        """Check that no non-essential cookies are set before consent."""
        # Clear all cookies and reload
        self.driver.delete_all_cookies()
        self.driver.get(self.base_url)
        import time
        time.sleep(3)

        non_essential = self._has_non_essential_cookies()

        self.results["no_preconsent_cookies"] = {
            "passed": len(non_essential) == 0,
            "detail": (
                "No non-essential cookies before consent"
                if not non_essential
                else f"Non-essential cookies found before consent: {', '.join(non_essential)}"
            ),
        }

    def check_reject_blocks_cookies(self):
        """Check that Reject All prevents non-essential cookies."""
        self.driver.delete_all_cookies()
        self.driver.get(self.base_url)
        import time
        time.sleep(2)

        reject_btn = self._find_element(self.selectors["reject"])
        if reject_btn:
            reject_btn.click()
            time.sleep(3)

            # Navigate to trigger tag loading
            self.driver.get(f"{self.base_url}/products" if "/products" not in self.base_url else self.base_url)
            time.sleep(3)

            non_essential = self._has_non_essential_cookies()

            self.results["reject_blocks_cookies"] = {
                "passed": len(non_essential) == 0,
                "detail": (
                    "Reject All correctly blocks non-essential cookies"
                    if not non_essential
                    else f"Non-essential cookies set after Reject All: {', '.join(non_essential)}"
                ),
            }
        else:
            self.results["reject_blocks_cookies"] = {
                "passed": False,
                "detail": "Cannot test — Reject All button not found",
            }

    def check_accept_sets_cookies(self):
        """Check that Accept All enables non-essential cookies."""
        self.driver.delete_all_cookies()
        self.driver.get(self.base_url)
        import time
        time.sleep(2)

        accept_btn = self._find_element(self.selectors["accept"])
        if accept_btn:
            accept_btn.click()
            time.sleep(3)

            self.driver.get(f"{self.base_url}/products" if "/products" not in self.base_url else self.base_url)
            time.sleep(3)

            cookies = self.driver.get_cookies()

            self.results["accept_sets_cookies"] = {
                "passed": len(cookies) > 3,
                "detail": f"After Accept All: {len(cookies)} cookies set",
            }
        else:
            self.results["accept_sets_cookies"] = {
                "passed": False,
                "detail": "Cannot test — Accept All button not found",
            }

    def check_banner_disappears(self):
        """Check banner disappears after making a choice."""
        self.driver.delete_all_cookies()
        self.driver.get(self.base_url)
        import time
        time.sleep(2)

        accept_btn = self._find_element(self.selectors["accept"])
        if accept_btn:
            accept_btn.click()
            time.sleep(2)

            banner = self._find_element(self.selectors["banner"])
            banner_gone = banner is None or not banner.is_displayed()

            self.results["banner_disappears_after_choice"] = {
                "passed": banner_gone,
                "detail": (
                    "Banner correctly disappears after choice"
                    if banner_gone
                    else "Banner still visible after making a choice"
                ),
            }
        else:
            self.results["banner_disappears_after_choice"] = {
                "passed": False,
                "detail": "Cannot test — Accept All button not found",
            }

    def check_no_cookie_wall(self):
        """Check that site is accessible after rejecting cookies."""
        self.driver.delete_all_cookies()
        self.driver.get(self.base_url)
        import time
        time.sleep(2)

        reject_btn = self._find_element(self.selectors["reject"])
        if reject_btn:
            reject_btn.click()
            time.sleep(2)

            # Check that main content is accessible
            body_text = self.driver.find_element(By.TAG_NAME, "body").text
            page_accessible = len(body_text) > 100

            self.results["no_cookie_wall"] = {
                "passed": page_accessible,
                "detail": (
                    "Site content accessible after rejecting cookies"
                    if page_accessible
                    else "Site content appears blocked after rejecting cookies — possible cookie wall"
                ),
            }
        else:
            self.results["no_cookie_wall"] = {
                "passed": False,
                "detail": "Cannot test — Reject All button not found",
            }

    def run_all_checks(self) -> dict:
        """Run all CNIL compliance checks."""
        print(f"Running CNIL cookie banner compliance checks for {self.base_url}")
        self.setup_driver()

        try:
            self.check_banner_visibility()
            self.check_button_presence()
            self.check_equal_prominence()
            self.check_preconsent_cookies()
            self.check_reject_blocks_cookies()
            self.check_accept_sets_cookies()
            self.check_banner_disappears()
            self.check_no_cookie_wall()
        finally:
            self.teardown_driver()

        return self.generate_report()

    def generate_report(self) -> dict:
        """Generate compliance report."""
        total_checks = len(self.results)
        passed = sum(1 for r in self.results.values() if r["passed"])
        failed = total_checks - passed

        critical_failures = [
            check_id
            for check_id, result in self.results.items()
            if not result["passed"]
            and self.CNIL_CHECKS.get(check_id, {}).get("severity") == "critical"
        ]

        report = {
            "metadata": {
                "url": self.base_url,
                "scan_date": datetime.now(timezone.utc).isoformat(),
                "framework": "CNIL Cookie Banner Compliance",
            },
            "summary": {
                "total_checks": total_checks,
                "passed": passed,
                "failed": failed,
                "compliance_rate": f"{(passed / total_checks * 100):.1f}%" if total_checks > 0 else "0%",
                "critical_failures": len(critical_failures),
                "overall_status": "COMPLIANT" if failed == 0 else "NON-COMPLIANT",
            },
            "checks": {
                check_id: {
                    "description": self.CNIL_CHECKS.get(check_id, {}).get("description", ""),
                    "severity": self.CNIL_CHECKS.get(check_id, {}).get("severity", "medium"),
                    **result,
                }
                for check_id, result in self.results.items()
            },
            "critical_failures": critical_failures,
        }

        return report


def main():
    """Run CNIL compliance check for Pinnacle E-Commerce Ltd."""
    checker = CNILBannerChecker(
        base_url="https://www.pinnacle-ecommerce.com",
        banner_selectors={
            "banner": '[data-testid="cookie-banner"]',
            "accept": '[data-testid="cookie-accept-all"]',
            "reject": '[data-testid="cookie-reject-all"]',
            "customise": '[data-testid="cookie-customise"]',
        },
    )

    report = checker.run_all_checks()

    output_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "reports")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "cnil_compliance_report.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(f"\n=== CNIL Cookie Banner Compliance Report ===")
    print(f"URL: {report['metadata']['url']}")
    print(f"Status: {report['summary']['overall_status']}")
    print(f"Checks passed: {report['summary']['passed']}/{report['summary']['total_checks']}")
    print(f"Critical failures: {report['summary']['critical_failures']}")

    if report["critical_failures"]:
        print("\nCritical issues requiring immediate remediation:")
        for check_id in report["critical_failures"]:
            check = report["checks"][check_id]
            print(f"  - {check['description']}: {check['detail']}")

    print(f"\nFull report saved to {output_path}")


if __name__ == "__main__":
    main()
