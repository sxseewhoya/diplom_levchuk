from playwright.sync_api import Page
import allure


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Open URL: {url}")
    def goto(self, url):
        self.page.goto(url)

    @allure.step("Click element: {locator}")
    def click(self, locator):
        self.page.click(locator)

    @allure.step("Fill field: {locator} with {text}")
    def fill(self, locator, text):
        self.page.fill(locator, text)

    @allure.step("Select option: {locator}")
    def select_option(self, locator, **kwargs):
        self.page.select_option(locator, **kwargs)

    @allure.step("Wait for element: {locator}")
    def wait_for_selector(self, locator, **kwargs):
        return self.page.wait_for_selector(locator, **kwargs)

    @allure.step("Check visibility: {locator}")
    def is_visible(self, locator):
        return self.page.is_visible(locator)

    @allure.step("Get text: {locator}")
    def get_text(self, locator):
        return self.page.inner_text(locator)

    @allure.step("Get element count: {locator}")
    def get_elements_count(self, locator):
        return len(self.page.query_selector_all(locator))
