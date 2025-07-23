from selenium.webdriver.common.by import By
import logging

from src import Driver

log = logging.getLogger(__name__)

class LoginPage:

    username_locator = (By.ID, 'user-name')
    password_locator = (By.ID, 'password')

    submit_locator = (By.ID, 'login-button')

    def __init__(self, driver : Driver ):
        self.driver = driver

    def setCredentials(self, username, password):
        username_input = self.driver.findElement(self.username_locator)
        username_input.send_keys(username)
        password_input = self.driver.findElement(self.password_locator)
        password_input.send_keys(password)

    def submit(self):
        log.info("clicking on submit")
        self.driver.click(self.submit_locator)


