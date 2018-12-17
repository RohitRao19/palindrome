import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options1 = Options()

from selenium.webdriver.firefox.options import Options
options2 = Options()

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
        
        options1.headless = True
        options1.add_argument('--headless')
        options1.add_argument('--no-sandbox')
        options1.add_argument('--disable-dev-shm-usage')
        options2.set_headless(True)
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=options1)
            #driver = webdriver.Chrome('C:\\pythonProject\\drivers\\chromedriver', chrome_options=options)
        else:
            driver = webdriver.Firefox(firefox_options=options2, '/usr/local/bin/geckodriver')

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)
        return driver