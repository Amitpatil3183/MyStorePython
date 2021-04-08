import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.customLogger import LogGen
from TestData.loginData import loginData
from PageObjects.MyAccountPage import MyAccountPage

class Test_MyAccounts:

    baseURL = loginData.getApplicationURL()
    email = loginData.getUseremail()
    password = loginData.getPassword()
    passwordW= loginData.getPassword1()
    logger = LogGen.loggen()


    @pytest.mark.Sanity
    def test_myaccount_navigation(self, setup):
        self.logger.info("*** Verify MyAccounts Test ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.clickSignInLink()
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickSignInButton()
        self.ma = MyAccountPage(self.driver)
        Header = self.ma.getMyAccountHeader()
        print(Header)

        if Header == "MY ACCOUNT":
            self.logger.info("*** User is on the My Accounts page ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** User is failed to land on My Accounts page  ***")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_user_myAccount.png")
            self.driver.close()
            assert False


