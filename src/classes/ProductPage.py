from selenium.webdriver.common.by import By


class ProductPage:

    header_locator = (By.XPATH, '//div[contains(@class, \'product_label\')]')
    shopping_card_locator = (By.XPATH, '//a[contains(@class,\'shopping_cart_link\')]')

    def __init__(self, driver):
        self.driver = driver
        header = self.driver.findElement(self.header_locator)
        assert header.is_displayed()

    def addItem(self, itemName):
        itemXpath = f"//div[contains(@class, \'inventory_item\')][.//div[text()='{itemName}']]//button[contains(@class,\'btn_primary btn_inventory\')]"
        item_locator = (By.XPATH, itemXpath)
        add_item_button = self.driver.findElement(item_locator)
        add_item_button.click()

    def clickShoppingCart(self):
        cart = self.driver.findElement(self.shopping_card_locator)
        cart.click()







