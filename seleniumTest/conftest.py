import pytest

from config.settings import BASE_URL, PASSWORD, USERNAME
from core.driver_factory import create_driver
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    web_driver = create_driver()
    web_driver.get(BASE_URL)
    yield web_driver
    web_driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(USERNAME, PASSWORD)
    yield driver
