import pytest
from selenium import webdriver

from PageObjects.CasualDressesPage import CasualDressesPage
from PageObjects.LoginPage import LoginPage
from Utilities.customLogger import LogGen
from TestData.loginData import loginData
from PageObjects.MyAccountPage import MyAccountPage

class Test_CasualDresses:


    baseURL = loginData.getApplicationURL()
    email = loginData.getUseremail()
    password = loginData.getPassword()
    passwordW = loginData.getPassword1()
    logger = LogGen.loggen()

    @pytest.mark.Sanity
    def test_CasualDresses_navigation(self, setup):
        self.logger.info("*** Verify Casual Dresses navigation ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.clickSignInLink()
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickSignInButton()
        self.ma = MyAccountPage(self.driver)
        self.driver.implicitly_wait(10)
        self.ma.clickCasualDressesMenu()
        self.cd = CasualDressesPage(self.driver)
        self.driver.execute_script("window.scrollTo(0, 300);")
        self.driver.implicitly_wait(10)
        Title = self.driver.title
        self.driver.implicitly_wait(10)
        print(Title)

        if Title == "Casual Dresses - My Store":
            self.logger.info("*** User navigates to Casual Dresses page successfully ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** Unable to navigate to Casual Dresses page ***")
            self.driver.save_screenshot(".\\Screenshots\\" + "Casual_Dresses.png")
            self.driver.close()
            assert False
