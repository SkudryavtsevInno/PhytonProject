from Base_Page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "[id='user-name']")
    PASSWORD_INPUT = (By.ID, "[id='password']")
    LOGIN_BUTTON = (By.ID, "[id='login-button']")

    def enter_username(self, username):
        """Ввод имени пользователя."""
        self.send_keys(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
