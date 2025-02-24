from playwright.sync_api import Page

from locators.login_page_locators import *


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open_url(self, url: str):
        self.page.goto(url=url)

    def click(self, locator: str):
        element = self.page.wait_for_selector(selector=locator)
        element.click()

    def input_text(self, text: str, locator: str):
        element = self.page.wait_for_selector(selector=locator)
        element.fill(value=text)

    def get_text(self, locator: str):
        element = self.page.wait_for_selector(selector=locator)
        return element.inner_text()

    def is_element_visible(self, locator: str):
        is_element = self.page.is_visible(selector=locator)
        if is_element:
            return True
        else:
            raise Exception('Элемент не отобразился на странице')

    def is_element_clickable(self, locator: str):
        is_element = self.page.is_enabled(selector=locator)
        if is_element:
            return True
        else:
            raise Exception('Элемент не кликабелен на странице')

    def is_not_element_clickable(self, locator: str):
        is_element = self.page.is_disabled(selector=locator)
        if is_element:
            return True
        else:
            raise Exception('Элемент не активен на странице')

    def login(self, login_locator: str, login: str, password_locator: str, password: str, button_locator: str,
              error_locator: str):

            login_field = self.page.wait_for_selector(login_locator)
            login_field.fill(login)

            password_field = self.page.wait_for_selector(password_locator)
            password_field.fill(password)

            auth_button = self.page.wait_for_selector(button_locator)
            auth_button.click()

            return self.page.wait_for_selector(selector=error_locator)

    def login_playwright(self, username: str, password: str):
            self.input_text(locator=LOGIN_FIELD, text='standard-user')
            self.input_text(locator=PASSWORD_FIELD, text='secret_sauce')
            self.click(locator=AUTH_BUTTON)

    def error_message(self, locator: str):
        return self.page.wait_for_selector(selector=locator)