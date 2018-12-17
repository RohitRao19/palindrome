from pages.palindrome.palindrome_page import Palindrome
from pages.home.login_page import Login
from utilities.teststatus import TestStatus
import unittest
import pytest
from base.selenium_driver import SeleniumDriver


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class PalindromeTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.pd = Palindrome(self.driver)
        self.lp = Login(self.driver)
        self.ts = TestStatus(self.driver)
        self.sd = SeleniumDriver(self.driver)

    @pytest.mark.run(order=1)
    def test_radio(self):
        self.lp.login("test", "password")
        self.pd.searchPalindrome()

        count = 0
        palindrom = []
        for item in self.pd.mainlist:
            if item == item[::-1]:
                palindrom.append(item)
                count += 1
        outFile = open("outputfile.txt", "w")
        outFile.write("Total Palindrome words: " + str(count))
        outFile.close()
        self.ts.markFinal("Palindrome test", str(count), "Total count")
