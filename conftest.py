import os
import pytest

from config import settings
from core.driver_factory import create_driver
from pages.login_page import LoginPage
from utils.screenshot import save_screenshot


def pytest_configure(config):
    os.makedirs("reports", exist_ok=True)


@pytest.fixture(scope="function")
def driver():
    web_driver = create_driver()
    web_driver.implicitly_wait(settings.IMPLICIT_WAIT_SECONDS)
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(settings.USERNAME, settings.PASSWORD)
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        web_driver = item.funcargs.get("driver") or item.funcargs.get("logged_in_driver")
        if web_driver:
            screenshot_path = save_screenshot(web_driver, item.name)
            extra = getattr(report, "extra", [])
            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html:
                extra.append(pytest_html.extras.image(screenshot_path))
                report.extra = extra
