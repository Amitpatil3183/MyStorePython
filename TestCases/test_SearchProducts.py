import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.ContactUsPage import ContactUsPage
from PageObjects.LoginPage import LoginPage
from PageObjects.MyAccountPage import MyAccountPage
from Utilities.customLogger import LogGen
from TestData.loginData import loginData
from TestData.searchProductsData import searchProductData


class Test_SearchProducts:

    baseURL = loginData.getApplicationURL()
    email = loginData.getUseremail()
    password = loginData.getPassword()
    passwordW= loginData.getPassword1()
    logger = LogGen.loggen()
    productCode = searchProductData.searchProduct()


    @pytest.mark.Sanity
    def test_search_product(self, setup):

        self.logger.info("*** Verify Search Products Test ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.clickSignInLink()
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickSignInButton()
        self.ma = MyAccountPage(self.driver)

        self.ma.EnterProductCode(self.productCode)
        self.driver.implicitly_wait(10)
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located(By.NAME, "Printed Chiffon Dress"))
        DressName = self.ma.getDressName()

        print(DressName)

        if DressName == "Printed Chiffon Dress":
            self.logger.info("*** Item searched successfully ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** Unable to search item ***")
            self.driver.save_screenshot(".\\Screenshots\\" + "remove_item.png")
            self.driver.close()
            assert False
