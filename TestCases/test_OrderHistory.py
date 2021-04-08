import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.customLogger import LogGen
from TestData.loginData import loginData
from PageObjects.MyAccountPage import MyAccountPage

class Test_OrderHistory:

    baseURL = loginData.getApplicationURL()
    email = loginData.getUseremail()
    password = loginData.getPassword()
    passwordW= loginData.getPassword1()
    logger = LogGen.loggen()


    @pytest.mark.Sanity
    def test_created_Order_On_history(self, setup):
        self.logger.info("*** Verify MyAccounts Test ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.clickSignInLink()
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickSignInButton()
        self.ma = MyAccountPage(self.driver)
        self.ma.clickOrderHistory()
        self.driver.execute_script("window.scrollTo(0, 500);")

        self.table = self.driver.find_element_by_id("order-list")
        self.body  = self.driver.find_elements_by_tag_name("tbody")
        self.cells = self.driver.find_elements_by_tag_name("td")

        is_order_present = False
        for c in self.cells:
            if 'VQCPYIUSG' in c.text:
                is_order_present = True
                break


        if is_order_present:
            assert True
            self.logger.info("********* Order is present on History Page *********")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Order_Missing_On_History.png")  # Screenshot
            self.logger.error("********* Order is NOT present on History Page ************")
            self.driver.close()
            assert False





