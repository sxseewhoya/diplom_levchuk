import time
import allure
import pytest
from locators.login_page_locators import *
from locators.account_page_locators import *


@allure.feature("Banking_Operations")
class TestBanking:
    @pytest.fixture(autouse=True)
    def auto_auth(self, login):
        login.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
        login.customer_login("Harry Potter")

    @allure.story("Customer Login")
    def test_customer_login(self, login):
        assert login.is_visible(LoginPageLocators.CUSTOMER_LOGOUT_BTN)

    @allure.story("Customer Logout")
    def test_customer_logout(self, login):
        login.click(LoginPageLocators.CUSTOMER_LOGOUT_BTN)
        assert login.is_visible("text=Your Name :")

    @allure.story("Deposit Operation")
    def test_deposit(self, login, account):
        account.make_deposit(100)
        assert '100' in account.get_balance()

    @allure.story("Withdrawal Operation")
    def test_withdrawal(self, login, account):
        account.make_deposit(500)
        account.make_withdrawal(200)
        assert '300' in account.get_balance()

    @allure.story("Transaction History")
    def test_transactions(self, login, account, transactions):
        account.make_deposit(200)
        time.sleep(2)
        account.click(AccountPageLocators.TRANSACTIONS_BTN)
        assert transactions.verify_transaction(200, "Credit")

    @allure.story("Reset Transactions")
    def test_reset_transactions(self, login, account, transactions):
        account.make_deposit(100)
        account.click(AccountPageLocators.TRANSACTIONS_BTN)
        transactions.reset_transactions()
        final_count = transactions.get_transactions_count()
        assert final_count == 0, f"Transactions not reset. Current quantity: {final_count}"

    @allure.story("Account Switching")
    def test_account_switch(self, login, account):
        initial_account_id = account.get_account_number()
        account.switch_account(1)
        new_account_id = account.get_account_number()
        assert initial_account_id != new_account_id, f"The account has not been changed. Current ID: {new_account_id}"

    @allure.story("Home Button")
    def test_home_button(self, login):
        login.click(AccountPageLocators.HOME_BTN)
        assert login.is_visible("text=Customer Login")

    @allure.story("Transaction Validation")
    def test_transaction_validation(self, login, account, transactions):
        account.make_deposit(300)
        time.sleep(2)
        account.click(AccountPageLocators.TRANSACTIONS_BTN)
        assert transactions.verify_transaction(300, "Credit")

    @allure.story("User Profile Display")
    def test_user_profile_display(self, login):
        username_element = login.wait_for_selector(
            LoginPageLocators.USERNAME_DISPLAY,
            timeout=10000
        )
        assert "Harry Potter" in username_element.inner_text(), \
            f"It was expected 'Harry Potter', received: {username_element.inner_text()}"
