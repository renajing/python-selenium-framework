import pytest

from src.BaseDriver import BaseDriver

from src.classes.CheckOutPage import CheckOutPage
from src.classes.LoginPage import LoginPage
from src.classes.ProductPage import ProductPage
from src.tests.BaseTest import BaseTest

#@pytest.mark.usefixtures("setup_driver")
class TestCheckOut(BaseTest):

    user = 'standard_user'
    password = 'secret_sauce'

    @pytest.fixture(scope="class")
    def login(self):
        loginPage = LoginPage(self._driver)
        loginPage.setCredentials(self.user, self.password)
        loginPage.submit()
        yield loginPage
        loginPage = None

    @pytest.fixture(scope="class")
    def addItem(self, login):
        productPage = ProductPage(self._driver)
        productPage.addItem('Sauce Labs Backpack')
        productPage.addItem('Sauce Labs Bike Light')
        productPage.clickShoppingCart()
        yield productPage
        productPage = None

    @pytest.fixture(scope="class")
    def checkout(self, login, addItem):
        checkOutPage = CheckOutPage(self._driver)
        checkOutPage.clickCheckOut()
        checkOutPage.setUserDetails('Standard', 'User', '94112')
        yield checkOutPage

    def testCheckoutVerifyDetails(self, login, addItem, checkout):
        checkout.verifyTotal("Sauce Labs Backpack")

    def testCheckoutVerifyTotal(self, login, addItem, checkout):
        checkout.verifyTotal("39.98")


