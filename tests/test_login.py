import pytest

from pages.login_page import LoginPage
from tests.base_test import BaseTest

@pytest.mark.order(1)
class TestLogin(BaseTest):

    def test_login_form_without_username(self, driver):
        loginPage = LoginPage(driver)
        loginPage.verify_login_without_username()


    def test_login_form_without_password(self, driver):
        loginPage = LoginPage(driver)
        loginPage.verify_login_without_password()


    def test_login_form_without_username_and_password(self, driver):
        loginPage = LoginPage(driver)
        loginPage.verify_login_without_username_and_password()


    def test_login_form_with_wrong_username(self, driver):
        loginPage = LoginPage(driver)
        loginPage.verify_login_with_wrong_username()


    def test_login_form_with_wrong_password(self, driver):
        loginPage = LoginPage(driver)
        loginPage.verify_login_with_wrong_password()


    def test_login_form_with_wrong_username_and_password(self, driver):
        loginPage = LoginPage(driver)
        loginPage.verify_login_with_wrong_username_and_password()

    def test_login_form_with_valid_credentials(self, driver):
        loginPage = LoginPage(driver)
        loginPage.verify_login_with_valid_credentials()
