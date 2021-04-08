import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    SummaryCheckoutBtn = "//a[@class='button btn btn-default standard-checkout button-medium']//span[contains(text(),'Proceed to checkout')]"
    AddressComment = "//textarea[@name='message']"
    AddressCheckoutBtn = "//button[@name='processAddress']//span[contains(text(),'Proceed to checkout')]"
    ShippingTerms = "//input[@id='cgv']"
    ShippingCheckoutBtn = "//button[@name='processCarrier']//span[contains(text(),'Proceed to checkout')]"
    PayByCheckBtn = "//a[@title='Pay by check.']"
    ConfirmOrderBtn = "//span[normalize-space()='I confirm my order']"
    ConfirmOrderMsg = "//p[@class='alert alert-success']"


    def clickSummaryCheckout(self):
        self.driver.find_element_by_xpath(self.SummaryCheckoutBtn).click()

    def setComment(self, Comment):
        self.driver.find_element_by_xpath(self.AddressComment).clear()
        self.driver.find_element_by_xpath(self.AddressComment).send_keys(Comment)

    def clickAddressCheckout(self):
        self.driver.find_element_by_xpath(self.AddressCheckoutBtn).click()

    def clickShippingTerms(self):
        self.driver.find_element_by_xpath(self.ShippingTerms).click()

    def clickShippingCheckout(self):
        self.driver.find_element_by_xpath(self.ShippingCheckoutBtn).click()

    def clickPyByCheckBtn(self):
        self.driver.find_element_by_xpath(self.PayByCheckBtn).click()

    def clickConfirmOrderBtn(self):
        self.driver.find_element_by_xpath(self.ConfirmOrderBtn).click()

    def getOrderConfirmMsg(self):
        return self.driver.find_element_by_xpath(self.ConfirmOrderMsg).text