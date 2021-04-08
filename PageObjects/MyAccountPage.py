from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MyAccountPage:


    def __init__(self, driver):
        self.driver = driver

    MyAccountHeader = "//h1[normalize-space()='My account']"
    DressesMenu = "//body/div[@id='page']/div[@class='header-container']/header[@id='header']/div/div[@class='container']/div[@class='row']/div[@id='block_top_menu']/ul[@class='sf-menu clearfix menu-content sf-js-enabled sf-arrows']/li[2]/a[1]"
    SummerDressesMenu = "//div[@class='block_content']//a[@title='Short dress, long dress, silk dress, printed dress, you will find the perfect dress for summer.'][normalize-space()='Summer Dresses']"
    SummerDressesPageHeader = "//div[@id='block_top_menu']//a[@title='Summer Dresses'])[2]"
    ContactUsLink = "//a[@title='Contact Us']"
    GlobalProductSearch = "//input[@id='search_query_top']"
    ChiffonSearch = "//li[@class='ac_even ac_over']//strong[contains(text(),'Printed Chiffon Dress')]"

    PrintedChiffonDress = "//h1[normalize-space()='Printed Chiffon Dress']"

    OrderHistoryBtn = "//span[normalize-space()='Order history and details']"
    CasualDressMenu = "//li[@class='sfHover']//a[@title='Casual Dresses'][normalize-space()='Casual Dresses']"





    ##################### Methods to add item to the cart ###########################

    def getMyAccountHeader(self):
        return self.driver.find_element_by_xpath(self.MyAccountHeader).text


    def clickDressesMenu(self):
        self.driver.find_element_by_xpath(self.DressesMenu).click()

    def clickSummerDressesMenu(self):
        self.driver.find_element_by_xpath(self.SummerDressesMenu).click()

    def clickContactUsLink(self):
        self.driver.find_element_by_xpath(self.ContactUsLink).click()

    def EnterProductCode(self, ProductCode):
        self.driver.find_element_by_xpath(self.GlobalProductSearch).clear()
        self.driver.find_element_by_xpath(self.GlobalProductSearch).send_keys(ProductCode)

    def getDressName(self):
        return self.driver.find_element_by_xpath(self.PrintedChiffonDress).text

    def clickOrderHistory(self):
        self.driver.find_element_by_xpath(self.OrderHistoryBtn).click()

    def clickCasualDressesMenu(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element_by_xpath("//header/div[3]/div[1]/div[1]/div[6]/ul[1]/li[2]/a[1]")).move_to_element(self.driver.find_element_by_xpath("//header/div[3]/div[1]/div[1]/div[6]/ul[1]/li[2]/ul[1]/li[1]/a[1]")).click().perform()




        # actions = ActionChains(self.driver)
        # actions.move_to_element(self.DressesMenu).perform()
        # wait = WebDriverWait(self.driver, 10)
        # element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Casual Dresses')))
        # element.click()
