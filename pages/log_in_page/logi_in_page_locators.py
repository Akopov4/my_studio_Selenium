from selenium.webdriver.common.by import By


class LogInPageLocators:
    LOG_IN_FIELD = (By.ID, "login")
    PASSWORD_FILED = (By.ID, "pwd")
    SUBMIT_BUTTON = (By.ID, 'smbt')
    CAPTION = (By.ID, 'caption')
