import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.customLogger import LogGen
from TestData.loginData import loginData


class Test_Login:

    baseURL = loginData.getApplicationURL()
    email = loginData.getUseremail()
    password = loginData.getPassword()
    passwordW= loginData.getPassword1()
    logger = LogGen.loggen()


    @pytest.mark.Regression
    def test_valid_login(self, setup):

        self.logger.info("*** Verify Login Test ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.clickSignInLink()
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickSignInButton()
        act_tittle = self.driver.title

        if act_tittle == "My account - My Store":
            self.logger.info("**** Login Test Case is passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("*** Login Test Case is Failed ***")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_valid_login.png")
            self.driver.close()
            assert False


    @pytest.mark.Regression
    def test_invalid_login(self, setup):
        self.logger.info("*** Verify Invalid Login Test ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.clickSignInLink()
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.passwordW)
        self.lp.clickSignInButton()
        self.msg = self.driver.find_elements_by_tag_name("li")

        is_auth_failed = False
        for m in self.msg:
            if 'Authentication failed.' in m.text:
                is_auth_failed = True
                break

        if is_auth_failed:
            self.driver.close()
            assert True
            self.logger.info("********* Invalid Login Test passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_invalidLogin.png")  # Screenshot
            self.logger.error("********* Invalid Login Test Failed ************")
            self.driver.close()
            assert False






