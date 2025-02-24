from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import LoginPageLocators, InventoryPageLocators
import allure

@allure.feature('Test open page')

@allure.story('Проверка открытия страницы')
def test_page_title(browser):
    with allure.step('Проверка наличия лого'):
        assert browser.title == "Swag Labs", 'Страница не открылась'


def test_login_fields(browser):
    username = browser.find_element(*LoginPageLocators.USERNAME_INPUT)
    password = browser.find_element(*LoginPageLocators.PASSWORD_INPUT)

    assert username.is_displayed(), 'Поле логина отсутствует'
    assert password.is_displayed(), 'Поле пароля отсутствует'


def test_login_button_clickable(browser):
    login_button = browser.find_element(*LoginPageLocators.LOGIN_BUTTON)

    assert login_button.is_displayed(), "Кнопка не отображается на странице"
    assert login_button.is_enabled(), "Кнопка заблокирована (не кликабельна)"

    assert login_button.get_attribute("value") == "Login", "Некорректный текст на кнопке"


def test_successful_login(browser):
    browser.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys("standard_user")
    browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("secret_sauce")
    browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(browser, 10).until(EC.url_contains("/inventory.html"))
    title = browser.find_element(*InventoryPageLocators.TITLE)
    assert title.text == "Products", 'Авторизация не удалась'


def test_unsuccessful_login(browser):
    browser.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys("locked_out_user")
    browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("invalid_pass")
    browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    error = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.ERROR_MESSAGE)
    )
    assert "Epic sadface" in error.text, 'Сообщение об ошибке отсутствует'
