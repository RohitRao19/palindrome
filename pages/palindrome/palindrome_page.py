from base.basepage import BasePage
import utilities.custom_logger as cl  # from customLogger under utilities
import logging  # for loggin messages


class Palindrome(BasePage):
    log = cl.customLogger(logging.DEBUG)  # from customLogger under utilities

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    _radiobuttons = "//input[@type='radio']//following-sibling::span"
    _textboxes = "//input[@type = 'text']"
    _checkboxes = "//input[@type = 'checkbox']//following-sibling::div"
    _dropdown = "//select[@id='select']"
    _table = "//tbody"
    _morebtn = "//button[text() = 'More Palindromes!' ]"

    mainlist = []

    def radioBtnText(self):
        radios = self.getElementList(self._radiobuttons, locatorType='xpath')
        for radio in radios:
            self.mainlist.append(self.getText(element=radio))
        return self.mainlist

    def textBoxText(self):
        texts = self.getElementList(self._textboxes, locatorType='xpath')
        for text in texts:
            self.mainlist.append(self.getText(element=text))
        return self.mainlist

    def checkboxes(self):
        chckboxes = self.getElementList(self._checkboxes, locatorType='xpath')
        for box in chckboxes:
            self.mainlist.append(self.getText(element=box))
        return self.mainlist

    def dropdownText(self):
        dropdown = self.getElementList(self._dropdown, locatorType='xpath')
        for drop in dropdown:
            droptext = self.getText(element=drop).split()
        return self.mainlist.extend(droptext)
            #droptext = self.getText(element=drop)
            #print(droptext.split())

    def tableElements(self):
        tables = self.waitToLoadElements(self._table, locatorType='xpath')
        for elemnt in tables:
            t = self.getText(element=elemnt).split()
        return self.mainlist.extend(t)

    def clickPalindromeBtn(self):
        self.elementClick(self._morebtn,locatorType='xpath')

    def textFromAlert(self):
        alert = self.waitForSwitchAlert()
        alertText = str(alert.text).split()
        return self.mainlist.extend(alertText)

    def searchPalindrome(self):
        self.radioBtnText()
        self.textBoxText()
        self.checkboxes()
        self.dropdownText()
        self.tableElements()
        self.clickPalindromeBtn()
        self.textFromAlert()





        # count = 0
        # for item in tableList:
        #     if item == item[::-1]:
        #         print(item)
        #         count += 1
        # print(count)
##################################################################################


        # count = 0
        # for item in mainlist:
        #     if item == item[::-1]:
        #         print(item)
        #         count += 1
        # print(count)
        # print(mainlist)
        #time.sleep(5)

            # ###############
            #         mainlist = []
            #
            # #############radio Button#############
            #         radio = driver.find_elements(By.XPATH, "//input[@type='radio']//following-sibling::span")
            #         for rad in radio:
            #             r = rad.text
            #             mainlist.append(r)
            #
            # ############text box#################
            #         textbox = driver.find_elements(By.XPATH, "//input[@type = 'text']")  #
            #         for tex in textbox:
            #             t = tex.get_attribute('value')
            #             mainlist.append(t)
            #
            #         checkbox = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']//following-sibling::div")
            #         for chec in checkbox:
            #             c = chec.text
            #             mainlist.append(c)
            #
            #
            # #######################dropdown#############
            #         dropelement = driver.find_elements(By.XPATH, "//select[@id='select']")
            #         for ele in dropelement:
            #             e= ele.text.split()
            #             mainlist.extend(e)
            #

# #################################################
# #############table 2##################
#         elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
#             (By.XPATH, "//tbody")))
#
#         for element in elements:
#             z = element.text.split()
#
#             mainlist.extend(z)
## #######################Alert########################################################
#         palindromeButton = driver.find_element(By.XPATH,"//button[text() = 'More Palindromes!' ]")
#         palindromeButton.click()
#
#         try:
#             WebDriverWait(driver,10).until(EC.alert_is_present(), 'Timed out waiting for PA creation '+''
#                                                                         'confirmation popup to appear')
#             alert = driver.switch_to.alert
#             alertText = str(alert.text).split()
#             # print(alertText)
#             # for char in alertText:
#             #     print(char)
#             mainlist.extend(alertText)
#             #time.sleep(3)
#             #alert.accept()
#         except TimeoutException:
#             print("no Alert")


################################## TABLE #############
        # elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
        #     (By.XPATH, "//tbody/tr")))
        #
        # tableList = []
        # for element in elements:
        #     z = element.text
        #     g = z.split()
        #     tableList.extend(g)
        # print(tableList)
        #