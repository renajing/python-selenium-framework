import pytest
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from conftest import site
from src.BaseDriver import BaseDriver
from src.Driver import Driver
from src.utils.EventListener import EventListener
from src.utils.Logger import Logger


class BaseTest:

    site = 'https://www.saucedemo.com/v1/'

    @pytest.fixture(scope="class")
    def setup_driver_old(self, request, browserType):
        self._driver = BaseDriver(browserType)
        self._driver.launch(self.site)
        request.cls._driver = self._driver
        yield self._driver
        self._driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def setup_driver(self, request, browserType):
        # configure logger
        logger = Logger()

        # configure driver
        baseDriver = BaseDriver(browserType)
        eventFiringDriver = EventFiringWebDriver(baseDriver.getDriver(), EventListener())
        driver = Driver(eventFiringDriver)
        driver.launch(site)
        request.cls._driver = driver
        yield driver
        driver.quit()

