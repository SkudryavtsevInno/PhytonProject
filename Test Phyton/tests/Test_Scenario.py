from selenium import webdriver
from Login_Page import LoginPage


driver = webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com/v1/")
    login_page=LoginPage(driver)
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login()


finally:
    driver.quit()


