import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Инициализация WebDriver
    driver = webdriver.Chrome()
    yield driver
    # Закрытие браузера после теста
    driver.quit()