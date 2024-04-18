from typing import Union
from pages.base_page import BasePage
from logi_in_page_locators import LogInPageLocators
from selenium.webdriver.chrome.webdriver import WebDriver as C_Webdriver
from selenium.webdriver.firefox.webdriver import WebDriver as F_WebDriver


class Login(BasePage):

    def enter_login(self, email: str):
        self.enter_text(LogInPageLocators.LOG_IN_FIELD, email)

    def enter_psswd(self, txt):
        self.enter_text(LogInPageLocators.PASSWORD_FILED, txt)

    def click_submit(self):
        self.click_on_element(LogInPageLocators.SUBMIT_BUTTON)
