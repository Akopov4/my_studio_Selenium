import pytest
from . import TestBase
from constants import MANGER_EMAIL, MANAGER_PASS, STAFF_EMAIl, STAFF_PASS
from pages.log_in_page.login_page import Login, LogInPageLocators


class LogInTest(TestBase):
    @pytest.mark.parametrize('email,password',[(MANGER_EMAIL, MANAGER_PASS),(STAFF_EMAIl, STAFF_PASS)])
    def test_manager_log_in(self,driver, email, password):
        log_in_page = Login(driver=driver)
        log_in_page.enter_login(email)
        log_in_page.enter_psswd(password)
        log_in_page.click_submit()
        if email == MANGER_EMAIL:
            assert log_in_page.verify_text(LogInPageLocators.CAPTION, "Analytics3333") == 'Analytics' ,"wrong message \ for manager"       
        else:
            assert log_in_page.verify_text(LogInPageLocators.CAPTION,"Customers3333") == 'Customers', 'wrong message \ for staff'

    