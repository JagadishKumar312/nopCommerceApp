import random
import string
import time

import self
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium import webdriver
from pageObjects.Loginpage import Loginpage
from pageObjects.SearchforCustomer import Searchforcustomer
from pageObjects.AddCustomerrs import AddCustomer
import pytest


class Test_SearchCustomersbyEmail:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.logen()


    @pytest.mark.regression
    def test_searchCustomerbyEmail__04(self):
        self.logger.info("******SearchCustomersbyEmail_004*********")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp=Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****Login successful*******")

        self.addcust = AddCustomer(self.driver)

        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.logger.info("***Entered into Customers module")
        self.logger.info("*****Start searching Customer by Email")
        searchcust=Searchforcustomer(self.driver)
        searchcust.setEmail("admin@yourStore.com")

        searchcust.clickSearch()

        time.sleep(3)
        status=searchcust.searchCustomerbyEmail("admin@yourStore.com")
        assert True==status
        self.logger.info("*******test_searchCustomerbyEmail__04 Passed****")
        self.driver.close()






