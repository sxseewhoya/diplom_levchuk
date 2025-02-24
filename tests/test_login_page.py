import allure

from locators.login_page_locators import LOGIN_FIELD, PASSWORD_FIELD

@allure.feature('login_page')
class TestLoginPage:

    @allure.story('Тест hp авторизации')
    def test_hp_login(self, login_playwright):
        login_playwright.input_text(locator=LOGIN_FIELD, text='standard-user')
        login_playwright.input_text(locator=PASSWORD_FIELD, text='secret_sauce')
