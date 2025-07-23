from selenium.webdriver.support.abstract_event_listener import AbstractEventListener


class EventListener(AbstractEventListener):

    def before_click(self, element, driver) -> None:
        pass
        #print(f"Clicked on {element.tag_name} at location {element.location}")

    def after_click(self, element, driver) -> None:
        pass
        #print("Clicked on item")