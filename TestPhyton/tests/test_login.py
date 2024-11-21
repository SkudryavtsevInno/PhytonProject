from TestPhyton.pages.login_page import LoginPage

import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Инициализация WebDriver
    driver = webdriver.Chrome()
    yield driver
    # Закрытие браузера после теста
    driver.quit()


def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    # Добавьте проверку успешного входа, например, по наличию элемента на следующей странице

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("invalid_user", "invalid_password")
