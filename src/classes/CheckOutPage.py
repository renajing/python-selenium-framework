from selenium.webdriver.common.by import By


class CheckOutPage:

    checkout_locator = (By.XPATH, "//a[contains(@class,'checkout_button')]")

    first_name_locator = (By.ID, 'first-name')
    last_name_locator = (By.ID, 'last-name')
    postal_code_locator = (By.ID, 'postal-code')

    continue_locator = (By.XPATH, '//input[contains(@class,\'cart_button\')]')

    def __init__(self, driver):
        self.driver = driver

    def clickCheckOut(self):
        checkout = self.driver.findElement(self.checkout_locator)
        checkout.click()

    def setUserDetails(self, first, last, postalCode):
        firstName = self.driver.findElement(self.first_name_locator)
        firstName.send_keys(first)
        lastName = self.driver.findElement(self.last_name_locator)
        lastName.send_keys(last)
        postalCodeElem = self.driver.findElement(self.postal_code_locator)
        postalCodeElem.send_keys(postalCode)

        continueElem = self.driver.findElement(self.continue_locator)
        continueElem.click()

    def verifyTotal(self, total):
        total_xpath = f"//*[text()='{total}']"
        total_locator = (By.XPATH, total_xpath)
        total = self.driver.findElement(total_locator)
        assert total.is_displayed()





