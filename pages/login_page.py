from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators
import allure

class LoginPage(BasePage):
    @allure.step("Customer login")
    def customer_login(self, user_name):
        self.click(LoginPageLocators.CUSTOMER_LOGIN_BTN)
        self.select_option(LoginPageLocators.USER_SELECT, label=user_name)
        self.click(LoginPageLocators.LOGIN_BTN)
        self.wait_for_selector(LoginPageLocators.CUSTOMER_LOGOUT_BTN, timeout=15000)