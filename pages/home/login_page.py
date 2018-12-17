from base.basepage import BasePage
import utilities.custom_logger as cl  # from customLogger under utilities
import logging  # for loggin messages


class Login(BasePage):  # this is now child class for SeleniumDriver Class.
    log = cl.customLogger(logging.DEBUG)  # from customLogger under utilities

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

#   Locators
    _username = 'inputUsername'
    _pswrd = 'inputPassword'
    _loginbutton = "//button[@type='submit']"
    _loginErrorMsg = 'alert'
    _loginHeader = "//h1[contains(text(),'Please sign in')]"
    _homeSign = "//a[contains(text(),'Home')]"

    def enterUsername(self, username):
        self.sendKeys(username, self._username, locatorType='id')

    def enterPswrd(self, password):
        self.sendKeys(password, self._pswrd, locatorType='id')

    def clickButton(self):
        self.elementClick(self._loginbutton, locatorType='xpath')

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._homeSign, locatorType='xpath')
        return result

    def verifyBlankCredential(self):
        result = self.isElementPresent(self._loginHeader, locatorType='xpath')
        return result

    def verifyLoginFail(self):
        result = self.isElementPresent(self._loginErrorMsg, locatorType='id')
        return result

    def login(self, username="", password=""):
        self.enterUsername(username)
        self.enterPswrd(password)
        self.clickButton()
