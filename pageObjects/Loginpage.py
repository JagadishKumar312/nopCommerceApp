from selenium import webdriver
from selenium.webdriver.common.by import By


class Loginpage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_Login_xpath = "//button[@class='button-1 login-button']"
    link_Logout_link_text = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(by=By.ID, value=self.textbox_username_id).clear()
        self.driver.find_element(by=By.ID, value=self.textbox_username_id).send_keys(username)
        

    def setPassword(self, password):
        self.driver.find_element(by=By.ID, value=self.textbox_password_id).clear()

        self.driver.find_element(by=By.ID, value=self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(by=By.XPATH, value=self.button_Login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.link_Logout_link_text).click()
