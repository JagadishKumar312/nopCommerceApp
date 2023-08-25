import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:

    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath= "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstname_xpath = "//input[@id='FirstName']"
    txtLastname_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDOB_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtCustomersRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[contains(text(), 'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(), 'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(), 'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(), 'Vendors')]"
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(by=By.XPATH,value=self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(by=By.XPATH,value=self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(by=By.XPATH,value=self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(by=By.XPATH,value=self.txtEmail_xpath).send_keys(email)
    def setPassword(self,password):
        self.driver.find_element(by=By.XPATH,value=self.txtPassword_xpath).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element(by=By.XPATH,value=self.txtFirstname_xpath).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element(by=By.XPATH,value=self.txtLastname_xpath).send_keys(lastname)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element(by=By.ID,value=self.rdMaleGender_id).click()
        elif gender=='Female':
            self.driver.find_element(by=By.ID,value=self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(by=By.ID,value=self.rdMaleGender_id).click()

    def setDob(self,dob):
        self.driver.find_element(by=By.XPATH,value=self.txtDOB_xpath).send_keys(dob)

    def setCompanyName(self,compname):
        self.driver.find_element(by=By.XPATH,value=self.txtCompanyName_xpath).click()

    def setCustomerRoles(self,role):
        self.driver.find_element(by=By.XPATH,value=self.txtCustomersRoles_xpath).click()
        time.sleep(3)
        if role =='Registered':
            self.listitem=self.driver.find_element(by=By.XPATH,value=self.lstitemRegistered_xpath)
        elif role=='Administrators':
            self.listitem=self.driver.find_element(by=By.XPATH,value=self.lstitemAdministrators_xpath)
        elif role=='Guests':
            #here user can be registered or guests,only one
            time.sleep(3)
            self.driver.find_element(by=By.XPATH,value="//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]")
            self.listitem=self.driver.find_element(by=By.XPATH,value=self.lstitemGuests_xpath)
        elif role =='Registered':
            self.listitem=self.driver.find_element(by=By.XPATH,value=self.lstitemRegistered_xpath)
        elif role=='Vendors':
            self.listitem=self.driver.find_element(by=By.XPATH,value=self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(by=By.XPATH, value=self.lstitemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listitem)


    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(by=By.XPATH,value=self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)


    def setAdminContent(self,content):
        self.driver.find_element(by=By.XPATH,value=self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(by=By.XPATH,value=self.btnSave_xpath).click()