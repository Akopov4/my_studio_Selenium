
from typing import Any, Generator, Union

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as C_Service
from selenium.webdriver.chrome.webdriver import WebDriver as C_Webdriver
from selenium.webdriver.firefox.service import Service as F_SERVICE
from selenium.webdriver.firefox.webdriver import WebDriver as F_WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from constants import BROWSER


@pytest.fixture(scope="function")
def driver(request) -> Generator[Union[C_Webdriver, F_WebDriver], Any, None]:
    if BROWSER == 'Firefox':
        driver = webdriver.Firefox(
            service=F_SERVICE(GeckoDriverManager().install()))

    else:
        driver = webdriver.Chrome(service=C_Service(
            ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()
