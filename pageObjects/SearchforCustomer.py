from selenium import webdriver
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Searchforcustomer:
    txt_Email_id = "SearchEmail"
    txt_Firstname_id = "SearchFirstName"
    txt_Lastname_id = "SearchLastName"
    btnSearch_id = "search-customers"
    tableSearch_Results_xpath = "//div[@id='customers-grid_wrapper']//div[@class='row']"
    table_xpath = "//table[@id='customers-grid']"
    table_Rows_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_Columns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(by=By.ID, value=self.txt_Email_id).clear()
        self.driver.find_element(by=By.ID, value=self.txt_Email_id).send_keys(email)

    def setFirstName(self, firstname):
        self.driver.find_element(by=By.ID, value=self.txt_Firstname_id).clear()
        self.driver.find_element(by=By.ID, value=self.txt_Firstname_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(by=By.ID, value=self.txt_Lastname_id).clear()
        self.driver.find_element(by=By.ID, value=self.txt_Lastname_id).send_keys(lastname)

    def clickSearch(self):
        self.driver.find_element(by=By.ID, value=self.btnSearch_id).click()

    def getNoRows(self):
        return len(self.driver.find_elements(by=By.XPATH, value=self.table_Rows_xpath))

    def getNoColumns(self):
        return len(self.driver.find_elements(by=By.XPATH, value=self.table_Columns_xpath))

    def searchCustomerbyEmail(self, email):
        flag = False
        for r in range(1, self.getNoRows()+1):
            table = self.driver.find_element(by=By.XPATH,value=self.table_xpath)
            emailid = table.find_element(by=By.XPATH,value="//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searCustomerbyName(self, name):
        flag = False
        for r in range(1, self.getNoRows() + 1):
            table = self.driver.find_element(by=By.XPATH,value=self.table_xpath)
            fullname = table.find_element(by=By.XPATH,value="//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if fullname == name:
                flag = True
                break
        return flag
