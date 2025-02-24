


class TestLoginPage:

    def test_hp_login(self, login_playwright):
        from locators.login_page_locators import LOGIN_FIELD
        login_playwright.input_text(locator=LOGIN_FIELD, text='standard-user')
        from locators.login_page_locators import PASSWORD_FIELD
        login_playwright.input_text(locator=PASSWORD_FIELD, text='secret_sauce')