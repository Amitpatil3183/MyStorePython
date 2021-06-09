import random
import string
from lib2to3.pgen2 import driver
from TestData.registerUserData import registerUserData
import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.MyAccountPage import MyAccountPage
from Utilities.customLogger import LogGen
from TestData.loginData import loginData
import time



class Test_RegisterUser:

    baseURL = loginData.getApplicationURL()
    email = loginData.getUseremail()
    password = loginData.getPassword()
    logger = LogGen.loggen()
    CustFname = registerUserData.setCustFname()
    CustLname = registerUserData.setCustFname()
    CustPwd = registerUserData.setCustPwd()
    AddressFname = registerUserData.setAddressFname()
    AddressLname = registerUserData.setAddressLname()
    Address1 = registerUserData.setAddress1()
    City = registerUserData.setCity()
    State = registerUserData.selectState()
    Zip = registerUserData.setZip()
    HomePhone = registerUserData.setHomePhone()
    AliasAdd = registerUserData.setAliasAdd()



    @pytest.mark.Sanity
    def test_register_user(self, setup):
        self.logger.info("This is nice info")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.lp.clickSignInLink()
        time.sleep(5)
        self.email = random_generator() + "@test.com"
        self.lp.setCreateAccEmail(self.email)
        self.lp.ClickCreateAccountBtn()
        self.lp.ClickTittle()
        self.lp.setCustFname(self.CustFname)
        self.lp.setCustLname(self.CustLname)
        self.lp.setCustPwd(self.CustPwd)
        self.lp.setAddressFname(self.AddressFname)
        self.lp.setAddressLname(self.AddressLname)
        self.lp.setAddress1(self.Address1)
        self.lp.setCity(self.City)
        self.lp.selectState(self.State)
        self.lp.setZip(self.Zip)
        self.lp.setHomePhone(self.HomePhone)
        self.lp.setAliasAdd(self.AliasAdd)
        self.lp.ClickRegisterBtn()

        act_tittle = self.driver.title

        if act_tittle == "My account - My Store":
            self.logger.info("*** User Registration Test Passed ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** User Registration Test Failed ***")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_user_registration.png")
            self.driver.close()
            assert False

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


