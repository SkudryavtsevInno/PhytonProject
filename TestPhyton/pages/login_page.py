from selenium.webdriver.common.by import By
from TestPhyton.pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com"

    # Locators
    #USERNAME_FIELD = (By.CSS_SELECTOR, "[data-test='username']") - CSS
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
