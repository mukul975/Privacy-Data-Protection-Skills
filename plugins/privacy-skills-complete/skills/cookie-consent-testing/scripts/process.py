"""
Cookie Consent Test Runner

Runs automated cookie consent compliance tests using Selenium and
generates a compliance test report.

Requirements:
    pip install selenium webdriver-manager
"""

import json
import os
import time
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


NON_ESSENTIAL_PREFIXES = [
    "_ga", "_gid", "_gat", "_fbp", "_fbc", "_gcl", "_hj",
    "IDE", "fr", "NID", "_uet", "li_sugr",
]


class ConsentTestRunner:
    """Runs cookie consent compliance tests."""

    def __init__(self, base_url: str, selectors: Optional[dict] = None):
        self.base_url = base_url.rstrip("/")
        self.selectors = selectors or {
            "banner": '[data-testid="cookie-banner"]',
            "accept": '[data-testid="cookie-accept-all"]',
            "reject": '[data-testid="cookie-reject-all"]',
            "customise": '[data-testid="cookie-customise"]',
        }
        self.driver: Optional[webdriver.Chrome] = None
        self.results: list[dict] = []

    def setup_driver(self):
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

    def _find_element(self, selector: str):
        try:
            el = self.driver.find_element(By.CSS_SELECTOR, selector)
            return el if el.is_displayed() else None
        except Exception:
            return None

    def _get_non_essential_cookies(self) -> list[str]:
        cookies = self.driver.get_cookies()
        non_essential = []
        for cookie in cookies:
            name = cookie.get("name", "")
            for prefix in NON_ESSENTIAL_PREFIXES:
                if name.startswith(prefix):
                    non_essential.append(name)
                    break
        return non_essential

    def _run_test(self, test_name: str, test_func):
        """Run a single test and record result."""
        self.driver.delete_all_cookies()
        try:
            passed, detail = test_func()
            self.results.append({
                "test": test_name,
                "passed": passed,
                "detail": detail,
                "timestamp": datetime.now(timezone.utc).isoformat(),
            })
        except Exception as e:
            self.results.append({
                "test": test_name,
                "passed": False,
                "detail": f"Exception: {str(e)}",
                "timestamp": datetime.now(timezone.utc).isoformat(),
            })

    def test_preconsent_blocking(self) -> tuple[bool, str]:
        """Test: No non-essential cookies before consent."""
        self.driver.get(self.base_url)
        time.sleep(3)
        non_essential = self._get_non_essential_cookies()
        if non_essential:
            return False, f"Non-essential cookies found before consent: {', '.join(non_essential)}"
        return True, "No non-essential cookies before consent"

    def test_banner_visible(self) -> tuple[bool, str]:
        """Test: Banner visible on first visit."""
        self.driver.get(self.base_url)
        time.sleep(2)
        banner = self._find_element(self.selectors["banner"])
        if banner:
            return True, "Cookie banner is visible"
        return False, "Cookie banner not found or not visible"

    def test_accept_button(self) -> tuple[bool, str]:
        """Test: Accept All button present."""
        self.driver.get(self.base_url)
        time.sleep(2)
        btn = self._find_element(self.selectors["accept"])
        if btn:
            return True, f"Accept button found: '{btn.text}'"
        return False, "Accept All button not found"

    def test_reject_button(self) -> tuple[bool, str]:
        """Test: Reject All button present at same level."""
        self.driver.get(self.base_url)
        time.sleep(2)
        btn = self._find_element(self.selectors["reject"])
        if btn:
            return True, f"Reject button found: '{btn.text}'"
        return False, "Reject All button not found — CNIL violation"

    def test_equal_prominence(self) -> tuple[bool, str]:
        """Test: Accept and Reject buttons have equal size."""
        self.driver.get(self.base_url)
        time.sleep(2)
        accept = self._find_element(self.selectors["accept"])
        reject = self._find_element(self.selectors["reject"])
        if not accept or not reject:
            return False, "Cannot compare — buttons not found"

        a_size = accept.size
        r_size = reject.size
        w_diff = abs(a_size["width"] - r_size["width"])
        h_diff = abs(a_size["height"] - r_size["height"])

        if w_diff <= 10 and h_diff <= 5:
            return True, f"Equal prominence: Accept {a_size['width']}x{a_size['height']}, Reject {r_size['width']}x{r_size['height']}"
        return False, f"Unequal: Accept {a_size['width']}x{a_size['height']}, Reject {r_size['width']}x{r_size['height']}"

    def test_reject_blocks_cookies(self) -> tuple[bool, str]:
        """Test: Reject All blocks non-essential cookies."""
        self.driver.get(self.base_url)
        time.sleep(2)
        reject = self._find_element(self.selectors["reject"])
        if not reject:
            return False, "Reject button not found"

        reject.click()
        time.sleep(2)
        self.driver.get(f"{self.base_url}/products" if "/products" not in self.base_url else self.base_url)
        time.sleep(3)

        non_essential = self._get_non_essential_cookies()
        if non_essential:
            return False, f"Non-essential cookies after Reject All: {', '.join(non_essential)}"
        return True, "Reject All correctly blocks non-essential cookies"

    def test_no_cookie_wall(self) -> tuple[bool, str]:
        """Test: Site accessible after rejecting cookies."""
        self.driver.get(self.base_url)
        time.sleep(2)
        reject = self._find_element(self.selectors["reject"])
        if not reject:
            return False, "Reject button not found"

        reject.click()
        time.sleep(2)
        body = self.driver.find_element(By.TAG_NAME, "body").text
        if len(body) > 100:
            return True, "Site content accessible after rejection"
        return False, "Site may be blocked after cookie rejection (possible cookie wall)"

    def run_all_tests(self) -> dict:
        """Run all consent compliance tests."""
        print(f"Running cookie consent tests for {self.base_url}")
        self.setup_driver()

        tests = [
            ("preconsent_blocking", self.test_preconsent_blocking),
            ("banner_visible", self.test_banner_visible),
            ("accept_button_present", self.test_accept_button),
            ("reject_button_present", self.test_reject_button),
            ("equal_prominence", self.test_equal_prominence),
            ("reject_blocks_cookies", self.test_reject_blocks_cookies),
            ("no_cookie_wall", self.test_no_cookie_wall),
        ]

        for name, func in tests:
            print(f"  Running: {name}...")
            self._run_test(name, func)

        self.teardown_driver()

        passed = sum(1 for r in self.results if r["passed"])
        failed = len(self.results) - passed

        return {
            "metadata": {
                "url": self.base_url,
                "test_date": datetime.now(timezone.utc).isoformat(),
                "total_tests": len(self.results),
                "passed": passed,
                "failed": failed,
            },
            "status": "PASS" if failed == 0 else "FAIL",
            "results": self.results,
        }


def main():
    """Run consent tests for Pinnacle E-Commerce Ltd."""
    runner = ConsentTestRunner(
        base_url="https://www.pinnacle-ecommerce.com",
        selectors={
            "banner": '[data-testid="cookie-banner"]',
            "accept": '[data-testid="cookie-accept-all"]',
            "reject": '[data-testid="cookie-reject-all"]',
            "customise": '[data-testid="cookie-customise"]',
        },
    )

    report = runner.run_all_tests()

    output_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "reports")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "consent_test_report.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(f"\n=== Consent Test Results: {report['status']} ===")
    print(f"Passed: {report['metadata']['passed']}/{report['metadata']['total_tests']}")
    for r in report["results"]:
        status = "PASS" if r["passed"] else "FAIL"
        print(f"  [{status}] {r['test']}: {r['detail']}")
    print(f"\nReport saved to {output_path}")


if __name__ == "__main__":
    main()
