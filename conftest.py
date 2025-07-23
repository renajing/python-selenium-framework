import logging

import pytest
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from src.BaseDriver import BaseDriver
from src.Driver import Driver
from src.utils.EventListener import EventListener

site = 'https://www.saucedemo.com/v1/'

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser type", choices=("chrome", "firefox")
    )

@pytest.fixture(scope="session")
def browserType(request):
    return request.config.getoption("--browser")

'''
@pytest.fixture(scope="session", autouse=True)
def setup_driver(request, browserType):
    baseDriver = BaseDriver(browserType)
    eventFiringDriver = EventFiringWebDriver(baseDriver.getDriver(), EventListener())
    driver = Driver(eventFiringDriver)
    driver.launch(site)
    #request.cls._driver = driver
    yield driver
    driver.quit()
'''