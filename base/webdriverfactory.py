import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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
        options = Options()
        options.headless = True
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=options)
            #driver = webdriver.Chrome('C:\\pythonProject\\drivers\\chromedriver', chrome_options=options)
        else:
            driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=options)

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)
        return driver