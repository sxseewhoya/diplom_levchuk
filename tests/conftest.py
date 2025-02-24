import pytest
from playwright.sync_api import sync_playwright

from lesson_15.pages.login_page import LoginPage


@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope='function')
def page(browser):
    page = browser.new_page()
    page.goto('https://saucedemo.com/')
    yield page
    page.close()

@pytest.fixture()
def login_playwright(page):
    return LoginPage(page)