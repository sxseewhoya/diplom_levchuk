from .base_page import BasePage
from locators.transactions_page_locators import TransactionsPageLocators
import allure


class TransactionsPage(BasePage):
    @allure.step("Reset transactions")
    def reset_transactions(self):
        self.wait_for_selector(TransactionsPageLocators.RESET_BTN, timeout=20000)
        self.click(TransactionsPageLocators.RESET_BTN)
        self.wait_for_selector(
            TransactionsPageLocators.TRANSACTION_ROW,
            state="hidden",
            timeout=15000
        )

    @allure.step("Get transactions count")
    def get_transactions_count(self):
        return len(self.page.query_selector_all(
            TransactionsPageLocators.TRANSACTION_ROW
        ))

    @allure.step("Verify transaction")
    def verify_transaction(self, amount, t_type):
        self.wait_for_selector(TransactionsPageLocators.TRANSACTION_ROW, timeout=30000)
        return any(
            str(amount) in row.inner_text() and t_type in row.inner_text()
            for row in self.page.query_selector_all(TransactionsPageLocators.TRANSACTION_ROW)
        )
