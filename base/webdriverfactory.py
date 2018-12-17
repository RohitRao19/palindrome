import traceback
from selenium import webdriver


class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "http://qa-home-palindrome.s3-website.us-east-2.amazonaws.com/login.html"

        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path='C:\pythonProject\drivers\geckodriver.exe')
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome('C:\\pythonProject\\drivers\\chromedriver')
        else:
            driver = webdriver.Chrome('C:\\pythonProject\\drivers\\chromedriver')

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)
        return driver
