import logger
import pytest
from urllib3 import request

from src.classes.LoginPage import LoginPage
from src.tests.BaseTest import BaseTest


@pytest.fixture(params=["standard_user", "problem_user"], scope="class")
def usernameFactory(request):
    return request.param

class TestLogin(BaseTest):

    def testLogin(self, usernameFactory):
        self._driver.launch(BaseTest.site)
        loginPage = LoginPage(self._driver)
        password = 'secret_sauce'
        loginPage.setCredentials(usernameFactory, password)
        loginPage.submit()
        assert self._driver.getDriver().title == "Swag Labs"




