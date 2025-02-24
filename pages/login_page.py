from locators.login_page_locators import LOGIN_FIELD, PASSWORD_FIELD, AUTH_BUTTON, ERROR_LOCATOR
from pages.base_page import BasePage


class LoginPage(BasePage):

    def login_playwright(self, username: str, password: str):
        self.input_text(locator=LOGIN_FIELD, text=username)
        self.input_text(locator=PASSWORD_FIELD, text=password)
        self.click(locator=AUTH_BUTTON)

    def get_error_login_message(self):
        return self.get_text(locator=ERROR_LOCATOR)
