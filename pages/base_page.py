from typing import Union

from selenium.webdriver.chrome.webdriver import WebDriver as C_Webdriver
from selenium.webdriver.firefox.webdriver import WebDriver as F_WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from constants import MAIN_PAGE


class BasePage:
    def __init__(self, driver: Union[F_WebDriver, C_Webdriver]):
        self.driver = driver

    def navigate_to_main_page(self):
        self.driver.get(MAIN_PAGE)

    def find_element(self, locator: tuple) -> WebElement:
        return self.driver.find_element(*locator)

    def enter_text(self, locator: tuple, text: str):
        input_filed = self.find_element(*locator)
        input_filed.send_keys(text)

    def click_on_element(self, locator: tuple):
        self.driver.find_element(*locator)

    def verify_text(self, loctator: tuple, txt_to_compare: str):
        element = self.find_element(*loctator)
        assert element.text == txt_to_compare

    def wait_element_to_be_visible(self, locator) -> WebElement:
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(*locator))
        return element

    def is_element_visible(self, locator):
        return self.find_element(*locator).is_displayed()
