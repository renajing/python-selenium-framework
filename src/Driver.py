from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.bidi.browser import Browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from src.utils.Logger import log


class Driver:

    timeout = 10

    def __init__(self, eventFiringWebDriver : EventFiringWebDriver):
        self.__driver = eventFiringWebDriver

    def quit(self):
        self.__driver.quit()

    def getDriver(self):
        return self.__driver

    def launch(self, site):
        self.__driver.get(site)

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