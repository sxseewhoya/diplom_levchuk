import time
from .base_page import BasePage
from locators.account_page_locators import AccountPageLocators
import allure


class AccountPage(BasePage):
    @allure.step("Make deposit")
    def make_deposit(self, amount):
        self.click(AccountPageLocators.DEPOSIT_BTN)
        self.fill(AccountPageLocators.AMOUNT_INPUT, str(amount))
        self.click(AccountPageLocators.SUBMIT_BTN)
        self.wait_for_selector(AccountPageLocators.MSG, timeout=10000)

    @allure.step("Make withdrawal")
    def make_withdrawal(self, amount) -> None:
        self.click(AccountPageLocators.WITHDRAW_BTN)
        time.sleep(1)
        self.fill(AccountPageLocators.AMOUNT_INPUT, str(amount))
        time.sleep(1)
        self.click(AccountPageLocators.SUBMIT_BTN)
        self.wait_for_selector(AccountPageLocators.MSG, timeout=10000)

    @allure.step("Get balance")
    def get_balance(self):
        return self.get_text(AccountPageLocators.BALANCE)

    @allure.step("Switch account")
    def switch_account(self, index):
        self.select_option(AccountPageLocators.ACCOUNT_SELECT, index=index)
        self.wait_for_selector(AccountPageLocators.ACCOUNT_SELECT, timeout=5000)

    @allure.step("Get Account ID")
    def get_account_number(self):
        return self.get_text(AccountPageLocators.ACCOUNT_ID)
