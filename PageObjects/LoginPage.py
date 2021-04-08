import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select




class LoginPage:

    ###################### Login elements #######################################

    SignInLink = ".//*[@title='Log in to your customer account']"
    Email = "//input[@id='email']"
    Password = "//input[@id='passwd']"
    SignInButton = "//span[normalize-space()='Sign in']"
    SignOutButton = "//a[@title='Log me out']"

    ###################### create account elements ###############################

    CreateAccountEmail = "//input[@id='email_create']"
    CreateAccountBtn = "//span[normalize-space()='Create an account']"
    Tittle = "//label[normalize-space()='Mr.']"
    CustFirstName = "//input[@id='customer_firstname']"
    CustLastName = "//input[@id='customer_lastname']"
    CustPassword = "//input[@id='passwd']"

    ###################### Customer Address elements ##############################

    AddressFirstName = "//input[@id='firstname']"
    AddressLastName = "//input[@id='lastname']"
    Address1 = "//input[@id='address1']"
    City = "//input[@id='city']"
    State = "//select[@id='id_state']"
    Zip = "//input[@id='postcode']"
    Country = "//select[@id='id_country']"
    HomePhone = "//input[@id='phone']"
    AliasAddress = "//input[@id='alias']"
    RegisterBtn = "//span[normalize-space()='Register']"



    def __init__(self, driver):
        self.driver = driver

    def clickSignInLink(self):
        self.driver.find_element_by_xpath(self.SignInLink).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.Email).clear()
        self.driver.find_element_by_xpath(self.Email).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.Password).clear()
        self.driver.find_element_by_xpath(self.Password).send_keys(password)

    def clickSignInButton(self):
        self.driver.find_element_by_xpath(self.SignInButton).click()

    def clickSignOutButton(self):
        self.driver.find_element_by_xpath(self.SignOutButton).click()

############################### Register User methods ##############################

    def setCreateAccEmail(self, AccEmail):
        self.driver.find_element_by_xpath(self.CreateAccountEmail).clear()
        self.driver.find_element_by_xpath(self.CreateAccountEmail).send_keys(AccEmail)

    def ClickCreateAccountBtn(self):
        self.driver.find_element_by_xpath(self.CreateAccountBtn).click()

    def ClickTittle(self):
        self.driver.find_element_by_xpath(self.Tittle).click()

    def setCustFname(self, CustFname):
        self.driver.find_element_by_xpath(self.CustFirstName).clear()
        self.driver.find_element_by_xpath(self.CustFirstName).send_keys(CustFname)

    def setCustLname(self, CustLname):
        self.driver.find_element_by_xpath(self.CustLastName).clear()
        self.driver.find_element_by_xpath(self.CustLastName).send_keys(CustLname)

    def setCustPwd(self, CustPwd):
        self.driver.find_element_by_xpath(self.CustPassword).clear()
        self.driver.find_element_by_xpath(self.CustPassword).send_keys(CustPwd)

    def setAddressFname(self, AddFname):
        self.driver.find_element_by_xpath(self.AddressFirstName).clear()
        self.driver.find_element_by_xpath(self.AddressFirstName).send_keys(AddFname)

    def setAddressLname(self, AddLname):
        self.driver.find_element_by_xpath(self.AddressLastName).clear()
        self.driver.find_element_by_xpath(self.AddressLastName).send_keys(AddLname)

    def setAddress1(self, Address1):
        self.driver.find_element_by_xpath(self.Address1).clear()
        self.driver.find_element_by_xpath(self.Address1).send_keys(Address1)

    def setCity(self, City):
        self.driver.find_element_by_xpath(self.City).clear()
        self.driver.find_element_by_xpath(self.City).send_keys(City)

    def selectState(self, value):
        select = Select(self.driver.find_element_by_xpath(self.State))
        select.select_by_visible_text(value)

    def setZip(self, Zip):
        self.driver.find_element_by_xpath(self.Zip).clear()
        self.driver.find_element_by_xpath(self.Zip).send_keys(Zip)

    def setHomePhone(self, Homephone):
        self.driver.find_element_by_xpath(self.HomePhone).clear()
        self.driver.find_element_by_xpath(self.HomePhone).send_keys(Homephone)

    def setAliasAdd(self, AliasAdd):
        self.driver.find_element_by_xpath(self.AliasAddress).clear()
        self.driver.find_element_by_xpath(self.AliasAddress).send_keys(AliasAdd)

    def ClickRegisterBtn(self):
        self.driver.find_element_by_xpath(self.RegisterBtn).click()
