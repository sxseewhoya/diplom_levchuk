import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    yield driver

    driver.quit()