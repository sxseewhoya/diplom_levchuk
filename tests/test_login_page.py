from locators.login_page_locators import LOGIN_FIELD, PASSWORD_FIELD
from pages.base_page import BasePage


class TestLoginPage:

    def test_hp_login(self, login_playwright):
        login_playwright.input_text(locator=LOGIN_FIELD, text='standard-user')
        login_playwright.input_text(locator=PASSWORD_FIELD, text='secret_sauce')

class TestProductsPage:

    def test_burger_menu_items(self, login_playwright, page):
        login_playwright.input_text(locator=LOGIN_FIELD, text='standard-user')
        login_playwright.input_text(locator=PASSWORD_FIELD, text='secret_sauce')
        items = BasePage(page)
        assert items.find_all_items()