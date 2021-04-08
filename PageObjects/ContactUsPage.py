import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select


class ContactUsPage:

    def __init__(self, driver):
        self.driver = driver

    SubjectDropdown = "//select[@id='id_contact']"
    OrderReference = "//select[@name='id_order']"
    ProductDropdown = "//select[@id='291472_order_products']"
    SendBtn = "//span[normalize-space()='Send']"
    ChooseFileBtn = "//input[@id='fileUpload']"
    MessageTextBox = "//textarea[@id='message']"
    ContactUsSuccessMsg = "//p[@class='alert alert-success']"

    def selectSubject(self, value):
        select = Select(self.driver.find_element_by_xpath(self.SubjectDropdown))
        select.select_by_visible_text(value)

    def selectOrderReference(self, value):
        select = Select(self.driver.find_element_by_xpath(self.OrderReference))
        select.select_by_visible_text(value)

    def selectProduct(self, value):
        select = Select(self.driver.find_element_by_xpath(self.ProductDropdown))
        select.select_by_visible_text(value)

    def uploadFile(self):
        self.driver.find_element_by_xpath(self.ChooseFileBtn).send_keys("C:\\Users\\Amit\Desktop\\MyStoreQuery.txt")

    def ClickSendBtn(self):
        self.driver.find_element_by_xpath(self.SendBtn).click()

    def typeMessage(self, message):
        self.driver.find_element_by_xpath(self.MessageTextBox).clear()
        self.driver.find_element_by_xpath(self.MessageTextBox).send_keys(message)

    def getSuccessMsg(self):
        return self.driver.find_element_by_xpath(self.ContactUsSuccessMsg).text
