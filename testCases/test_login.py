import pytest

from selenium import webdriver
from pageObjects.Loginpage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.logen()

    @pytest.mark.regression
    def test_homePageTitle(self):
        self.logger.info("************Test_001_Login************")
        self.logger.info("************Verifying Home Page Title************")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)

        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************ Home Page Title Test is passed************")

        else:
            self.driver.save_screenshot(".\\screenShots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************ Home Page Title Test is failed************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self):
        self.logger.info("***verifying login test")
        self.driver = webdriver.Chrome()

        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************ Login Test passed ************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenShots\\" + "test_Login.png")
            self.driver.close()
            self.logger.error("************ Login Test failed ************")
            assert False
