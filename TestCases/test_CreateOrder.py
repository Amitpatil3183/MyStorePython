import pytest
from selenium import webdriver
from selenium.webdriver.common import actions
from PageObjects.LoginPage import LoginPage
from Utilities.customLogger import LogGen
from TestData.loginData import loginData
from PageObjects.MyAccountPage import MyAccountPage
from PageObjects.ShoppingCartPage import ShoppingCartPage
from selenium.webdriver import ActionChains
from PageObjects.OrderPage import OrderPage
from TestData.createOrderData import createOrderData

class Test_CreateOrder:
    baseURL = loginData.getApplicationURL()
    email = loginData.getUseremail()
    password = loginData.getPassword()
    logger = LogGen.loggen()
    DressSize = createOrderData.setDressSize()
    comment = createOrderData.setAddressComment()

    @pytest.mark.Sanity
    def test_Create_Order(self, setup):
        self.logger.info("*** Verify order creation scenario ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.clickSignInLink()
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickSignInButton()
        self.driver.implicitly_wait(10)
        self.ma = MyAccountPage(self.driver)
        self.driver.implicitly_wait(10)
        self.ma.clickDressesMenu()
        self.ma.clickSummerDressesMenu()
        self.sp = ShoppingCartPage(self.driver)
        self.driver.execute_script("window.scrollTo(0, 500);")
        self.driver.implicitly_wait(10)
        self.sp.clickItem1()
        self.driver.implicitly_wait(20)
        self.sp.selectSize(self.DressSize)
        self.sp.clickAddToCartButton()
        self.driver.implicitly_wait(10)
        p = self.driver.current_window_handle
        # get first child window
        chwnd = self.driver.window_handles
        for w in chwnd:
            # switch focus to child window
            if (w != p):
                self.driver.switch_to.window(w)
                break
        self.sp.ClickCheckout()
        self.driver.implicitly_wait(10)
        self.driver.execute_script("window.scrollTo(0, 1000);")
        self.op = OrderPage(self.driver)
        self.op.clickSummaryCheckout()
        self.op.setComment(self.comment)
        self.op.clickAddressCheckout()
        self.driver.implicitly_wait(10)
        self.op.clickShippingTerms()
        self.driver.implicitly_wait(10)
        self.op.clickShippingCheckout()
        self.driver.implicitly_wait(10)
        self.driver.execute_script("window.scrollTo(0, 600);")
        self.op.clickPyByCheckBtn()
        self.driver.implicitly_wait(10)
        self.driver.execute_script("window.scrollTo(0, 500);")
        self.op.clickConfirmOrderBtn()
        self.driver.execute_script("window.scrollTo(0, 400);")
        self.driver.implicitly_wait(10)
        OrderConfirmMsg = self.op.getOrderConfirmMsg()
        print(OrderConfirmMsg)

        if OrderConfirmMsg == "Your order on My Store is complete.":
            self.logger.info("*** Order created successfully ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** Unable to create order ***")
            self.driver.save_screenshot(".\\Screenshots\\" + "create_order.png")
            self.driver.close()
            assert False
