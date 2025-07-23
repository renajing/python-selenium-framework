from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.bidi.browser import Browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from enum import Enum

from src.utils.Logger import log


class BaseDriver:

    class Browser(Enum):
        CHROME = "chrome"
        FIREFOX = "firefox"

    timeout = 10

    def __init__(self, browserType : str):
        # Optional: Add Chrome options
        options = Options()
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-notifications")
        options.add_argument("--start-maximized")
        options.add_argument("--incognito")
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        if(browserType == self.Browser.CHROME.value):
            driver = webdriver.Chrome(options=options)
        elif(browserType == self.Browser.FIREFOX.value):
            driver = webdriver.Firefox(options=options)
        else:
            raise TypeError("Browser type must be firefox or chrome")

        self.__driver = driver

    def launch(self, site):
        self.__driver.get(site)

    def quit(self):
        self.__driver.quit()

    def getDriver(self):
        return self.__driver

    def dismissAlert(self):
        try:
            WebDriverWait(self.__driver, self.timeout).until(EC.alert_is_present())
            alert = self.__driver.switch_to.alert
            alert.dismiss()
            print("Alert dismissed.")
        except TimeoutException:
            print("No alert present — nothing to dismiss.")

    def findElement(self, locator):
        element = WebDriverWait(self.__driver, self.timeout).until(EC.presence_of_element_located(locator))
        return element

    def scrollToElement(self, locator):
        element = self.findElement(locator)
        self.__driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    @log
    def click(self, locator):
        element = self.scrollToElement(locator)
        element.click()




