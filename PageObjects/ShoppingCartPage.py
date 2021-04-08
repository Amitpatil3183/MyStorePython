import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select


class ShoppingCartPage:

    def __init__(self, driver):
        self.driver = driver

    Item1 = "//li[@class='ajax_block_product col-xs-12 col-sm-6 col-md-4 first-in-line last-line first-item-of-tablet-line first-item-of-mobile-line last-mobile-line']//a[@title='Printed Summer Dress'][normalize-space()='Printed Summer Dress']"
    AddToCartButton = "//span[normalize-space()='Add to cart']"
    ItemAddedMsg = "//span[normalize-space()='There is 1 item in your cart.']"
    ItemAddedMessage = "//h2[normalize-space()='Product successfully added to your shopping cart']"
    ContinueShoppingBtn = "//span[@title='Continue shopping']//span[1]"
    PrintedDress = "//h1[normalize-space()='Printed Summer Dress']"
    ProceedToCheckoutBtn = "//span[normalize-space()='Proceed to checkout']"
    CartTittle = "//h1[@id='cart_title']"
    SummerDressInCart = "//td[@class='cart_description']//a[contains(text(),'Printed Summer Dress')]"
    TrashIconOnCart = "//i[@class='icon-trash']"
    EmptyCartMsg = "//p[@class='alert alert-warning']"
    SizeDropdown = "//select[@id='group_1']"


    def getItemAddMsg(self):
        return self.driver.find_element_by_xpath(self.ItemAddedMessage).text

    def clickItem1(self):
        self.driver.find_element_by_xpath(self.Item1).click()

    def clickAddToCartButton(self):
        self.driver.find_element_by_xpath(self.AddToCartButton).click()

    def SuccessMessage(self):
        msg = self.driver.find_element_by_xpath(self.ItemAddedMessage).text
        return msg

    def ClickContShopp(self):
        self.driver.find_element_by_xpath(self.ContinueShoppingBtn).click()

    def getPrintedDressText(self):
        return self.driver.find_element_by_xpath(self.PrintedDress).text

    def ClickCheckout(self):
        self.driver.find_element_by_xpath(self.ProceedToCheckoutBtn).click()

    def getCartTittle(self):
        return self.driver.find_element_by_xpath(self.CartTittle).text

    def getSummerDress(self):
        return self.driver.find_element_by_xpath(self.SummerDressInCart).text

    def ClickTrashIcon(self):
        self.driver.find_element_by_xpath(self.TrashIconOnCart).click()

    def ClickMessage(self):
        self.driver.find_element_by_xpath(self.EmptyCartMsg).click()

    def getEmptyCartMsg(self):
        return self.driver.find_element_by_xpath(self.EmptyCartMsg).text

    def selectSize(self, value):
        select = Select(self.driver.find_element_by_xpath(self.SizeDropdown))
        select.select_by_visible_text(value)
