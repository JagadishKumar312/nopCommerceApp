import random
import string
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium import webdriver
from pageObjects.Loginpage import Loginpage
from pageObjects.AddCustomerrs import AddCustomer
import pytest


class Test__003_AddCustomer():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.logen()
    @pytest.mark.sanity
    def test_addCustomer(self):
        self.logger.info("*******test_addCustomer***********")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******Login succesfull******")
        self.logger.info("****Starting Add Customer Test")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddnew()
        self.logger.info("*******Providing customer info*******")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword(password="12345")
        self.addcust.setGender(gender='Male')
        self.addcust.setDob(dob='03/24/1998')
        self.addcust.setCompanyName(compname='qspiders')
        self.addcust.setCustomerRoles(role='Vendors')
        self.addcust.setManagerOfVendor(value='Vendor 1')
        self.addcust.setAdminContent(content='This is for Testing')
        self.addcust.clickOnSave()
        self.logger.info("*********Saving customer info***********")

        self.logger.info("**********Add customer Validation started********")
        self.msg = self.driver.find_element(by=By.XPATH,
                                            value="//div[@class='alert alert-success alert-dismissable']").text

        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("***Add Customer  Test Passed")
        else:
            self.driver.save_screenshot(".\\screenShots\\" + "test_addCustomer_scr.png")  # screenshot
            self.logger.info("*******Add customer Test failed")
            assert True == False
        self.driver.close()
        self.logger.info("****Ending home page title test")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
