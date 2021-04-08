import pytest
from selenium import webdriver
from selenium.webdriver.common import actions
from PageObjects.LoginPage import LoginPage
from Utilities.customLogger import LogGen
from TestData.loginData import loginData
from PageObjects.MyAccountPage import MyAccountPage
from PageObjects.ShoppingCartPage import ShoppingCartPage
from selenium.webdriver import ActionChains

class Test_ShoppingCart:

    baseURL = loginData.getApplicationURL()
    email = loginData.getUseremail()
    password = loginData.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.Sanity
    def test_continue_shopping(self, setup):
        self.logger.info("*** Verify Continue Shopping scenario ***")
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
        self.sp.ClickContShopp()
        self.driver.implicitly_wait(10)
        ProductText =self.sp.getPrintedDressText()
        print(ProductText)

        if ProductText == "Printed Summer Dress":
            self.logger.info("*** User returns to the Products page successfully ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** Continue Shopping scenario is failed  ***")
            self.driver.save_screenshot(".\\Screenshots\\" + "add_item_cart.png")
            self.driver.close()
            assert False

    @pytest.mark.Sanity
    def test_proceed_to_checkout(self, setup):
        self.logger.info("*** Verify Proceed to Checkout scenario ***")
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
        SummerDressInCart = self.sp.getSummerDress()
        print(SummerDressInCart)

        if SummerDressInCart == "Printed Summer Dress":
            self.logger.info("*** User is on Shopping Cart Summary Page ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** User failed to navigate to Shopping Cart Summary Page ***")
            self.driver.save_screenshot(".\\Screenshots\\" + "shopping_cart_summary.png")
            self.driver.close()
            assert False

    @pytest.mark.Sanity
    def test_remove_item(self, setup):
        self.logger.info("*** Verify remove item from cart scenario ***")
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
        self.sp.ClickTrashIcon()
        self.driver.refresh()
        self.driver.execute_script("window.scrollTo(0, 500);")
        self.driver.implicitly_wait(10)
        CartEmptyMsg = self.sp.getEmptyCartMsg()
        print(CartEmptyMsg)

        if CartEmptyMsg == "Your shopping cart is empty.":
            self.logger.info("*** Item deleted from the cart ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** Unable to remove item from the cart ***")
            self.driver.save_screenshot(".\\Screenshots\\" + "remove_item.png")
            self.driver.close()
            assert False

