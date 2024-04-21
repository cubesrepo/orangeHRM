import time

import test_data
from pages.base_page import BasePage


class LoginPage(BasePage):
    def verify_login_without_username(self):
        time.sleep(2)

        assert self.title_is("OrangeHRM"), "wrong page title"

        #input password
        self.send_keys(test_data.login.PASSWORD, test_data.PASSWORD)

        time.sleep(0.5)

        # click login btn
        login_btn = self.wait_clickable(test_data.login.LOGIN_BTN)
        self.action_click(login_btn)

        time.sleep(0.5)
        #assertion of username validation
        assert self.get_text(test_data.login.USERNAME_VALIDATION) == "Required"

    def verify_login_without_password(self):
        time.sleep(2)

        #input username
        username = self.wait_visibility(test_data.login.USERNAME)
        self.action_send_keys(username, test_data.USERNAME)

        # clear password
        password = self.wait_visibility(test_data.login.PASSWORD)
        self.action_clear_input(password)

        time.sleep(0.5)

        # click login btn
        login_btn = self.wait_clickable(test_data.login.LOGIN_BTN)
        self.action_click(login_btn)

        time.sleep(0.5)
        # assertion of password validation
        assert self.get_text(test_data.login.PASSWORD_VALIDATION) == "Required"

    def verify_login_without_username_and_password(self):
        time.sleep(2)

        #clear username
        username = self.wait_visibility(test_data.login.USERNAME)
        self.action_clear_input(username)

        # click login btn
        login_btn = self.wait_clickable(test_data.login.LOGIN_BTN)
        self.action_click(login_btn)

        time.sleep(0.5)
        # assertion of username and password validation
        assert self.get_text(test_data.login.USERNAME_VALIDATION) == "Required"
        assert self.get_text(test_data.login.PASSWORD_VALIDATION) == "Required"

    def verify_login_with_wrong_username(self):
        time.sleep(2)

        # invalid username
        username = self.wait_visibility(test_data.login.USERNAME)
        self.action_send_keys(username, "Admin1")

        time.sleep(0.5)
        #valid password
        password = self.wait_visibility(test_data.login.PASSWORD)
        self.action_send_keys(password, test_data.PASSWORD)

        # click login btn
        login_btn = self.wait_clickable(test_data.login.LOGIN_BTN)
        self.action_click(login_btn)

        time.sleep(0.5)

        assert self.get_text(test_data.login.INVALID_CREDENTIALS) == "Invalid credentials"

    def verify_login_with_wrong_password(self):
        time.sleep(2)

        #valid username
        username = self.wait_visibility(test_data.login.USERNAME)
        self.action_send_keys(username,  test_data.USERNAME)

        time.sleep(0.5)
        #invalid password
        password = self.wait_visibility(test_data.login.PASSWORD)
        self.action_send_keys(password, "admin1234")

        # click login btn
        login_btn = self.wait_clickable(test_data.login.LOGIN_BTN)
        self.action_click(login_btn)

        time.sleep(0.5)

        assert self.get_text(test_data.login.INVALID_CREDENTIALS) == "Invalid credentials"

    def verify_login_with_wrong_username_and_password(self):
        time.sleep(2)

        #invalid username
        username = self.wait_visibility(test_data.login.USERNAME)
        self.action_send_keys(username,  "Admin1")

        time.sleep(0.5)
        #invalid password
        password = self.wait_visibility(test_data.login.PASSWORD)
        self.action_send_keys(password, "admin1234")

        # click login btn
        login_btn = self.wait_clickable(test_data.login.LOGIN_BTN)
        self.action_click(login_btn)

        time.sleep(0.5)

        assert self.get_text(test_data.login.INVALID_CREDENTIALS) == "Invalid credentials"

    def verify_login_with_valid_credentials(self):
        time.sleep(2)

        # valid username
        self.send_keys(test_data.login.USERNAME, test_data.USERNAME)

        time.sleep(0.5)
        # valid password
        password = self.wait_visibility(test_data.login.PASSWORD)
        self.action_send_keys(password, test_data.PASSWORD)

        # click login btn
        login_btn = self.wait_clickable(test_data.login.LOGIN_BTN)
        self.action_click(login_btn)

        time.sleep(1)

        assert self.url_is("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

