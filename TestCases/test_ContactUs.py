import pytest
from selenium import webdriver
from PageObjects.ContactUsPage import ContactUsPage
from PageObjects.LoginPage import LoginPage
from PageObjects.MyAccountPage import MyAccountPage
from Utilities.customLogger import LogGen
from TestData.loginData import loginData
from TestData.contactUsData import contactUsData


class Test_ContactUs:

    baseURL = loginData.getApplicationURL()
    email = loginData.getUseremail()
    password = loginData.getPassword()
    passwordW= loginData.getPassword1()
    logger = LogGen.loggen()
    subject = contactUsData.setSubjectHeading()
    reference = contactUsData.setOrderReference()
    product = contactUsData.setProduct()
    message = contactUsData.setMessage()


    @pytest.mark.Sanity
    def test_Contact_Us(self, setup):
        self.logger.info("*** Verify Contact Us Test ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.clickSignInLink()
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickSignInButton()
        self.ma = MyAccountPage(self.driver)
        self.ma.clickContactUsLink()
        self.driver.implicitly_wait(10)
        self.cu = ContactUsPage(self.driver)
        self.driver.execute_script("window.scrollTo(0, 500);")
        self.cu.selectSubject(self.subject)
        self.cu.selectOrderReference(self.reference)
        self.cu.selectProduct(self.product)
        self.cu.uploadFile()
        self.driver.implicitly_wait(10)
        self.cu.typeMessage(self.message)
        self.cu.ClickSendBtn()
        self.driver.implicitly_wait(10)
        SuccessMessage = self.cu.getSuccessMsg()
        print(SuccessMessage)

        if SuccessMessage == "Your message has been successfully sent to our team.":
            self.logger.info("*** Contact Us query submitted successfully ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** Unable to submit Contact Us query ***")
            self.driver.save_screenshot(".\\Screenshots\\" + "Contact_Us.png")
            self.driver.close()
            assert False