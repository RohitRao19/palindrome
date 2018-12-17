from pages.home.login_page import Login
from utilities.teststatus import TestStatus
import unittest
import pytest
from base.selenium_driver import SeleniumDriver


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = Login(self.driver)
        self.ts = TestStatus(self.driver)
        self.sd = SeleniumDriver(self.driver)

    @pytest.mark.run(order=1)
    def test_InvalidLogin(self):
        self.lp.login("tes1", "pwd11")
        result1 = self.lp.verifyLoginFail()
        self.ts.mark(result1, "Login Failed")
        self.ts.markFinal("test_invalidLogin", result1, "Login Not Succesfull")

    @pytest.mark.run(order=2)
    def test_InvalidBlankLogin(self):
        self.lp.login("", "")
        result2 = self.lp.verifyBlankCredential()
        self.ts.mark(result2, "Login Failed")
        self.ts.markFinal("test_invalidBlankLogin", result2, "Login Not Succes"
                          + "full")

    @pytest.mark.run(order=3)
    def test_InvalidBlankPwd(self):
        self.lp.login("test", "")
        result2 = self.lp.verifyBlankCredential()
        self.ts.mark(result2, "Login Failed")
        self.ts.markFinal("test_invalidBlankLogin", result2, "Login Not Succes"
                          + "full")

    @pytest.mark.run(order=4)
    def test_InvalidBlankUsr(self):
        self.lp.login("", "password")
        result2 = self.lp.verifyBlankCredential()
        self.ts.mark(result2, "Login Failed")
        self.ts.markFinal("test_invalidBlankLogin", result2, "Login Not Succes"
                          + "full")

    @pytest.mark.run(order=5)
    def test_InvalidCaseSensitive(self):
        self.lp.login("Test", "Password")
        result2 = self.lp.verifyBlankCredential()
        self.ts.mark(result2, "Login Failed")
        self.ts.markFinal("test_invalidBlankLogin", result2, "Login Not Succes"
                          + "full")

    @pytest.mark.run(order=6)
    def test_Login(self):
        self.lp.login("test", "password")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_Login", result2, "Login Success")
