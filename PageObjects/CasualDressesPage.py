import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select


class CasualDressesPage:

    def __init__(self, driver):
        self.driver = driver

    CasualDressesHeader = "//span[@class='cat-name']"



    def getCasualDressesText(self):
        return self.driver.find_element_by_xpath(self.CasualDressesHeader).text

