from pages.base_page import BasePage
from utilities import test_data

class LoginPage(BasePage):

    def enter_username_password(self, username, password):
        self.type(test_data.login.USERNAME, username)
        self.type(test_data.login.PASSWORD, password)
        self.wait_clickable(test_data.login.LOGIN_BTN).click()

    def get_invalid_credentials_error(self):
        return self.get_text(test_data.login.INVALID_CREDENTIALS)
    def get_username_required_error(self):
        return self.get_text(test_data.login.USERNAME_VALIDATION)
    def get_password_required_error(self):
        return self.get_text(test_data.login.PASSWORD_VALIDATION)
    def get_home_page_url(self, url):
        return self.get_url(url)

    def verify_login_with_valid_credentials(self):
        self.enter_username_password(test_data.CREDENTIALS["USERNAME"],
                                     test_data.CREDENTIALS["PASSWORD"])
        current_url = self.get_home_page_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

        return current_url

    def verify_login_with_invalid_credentials(self):
        self.enter_username_password(test_data.CREDENTIALS["INVALID_USERNAME"],
                                     test_data.CREDENTIALS["INVALID_PASSWORD"])

        current_result_invalid_credential_error = self.get_invalid_credentials_error()

        return current_result_invalid_credential_error

    def verify_login_without_username_and_password(self):
        self.enter_username_password(" ",
                                     " ")

        current_result_username_required_error = self.get_username_required_error()
        current_result_password_required_error = self.get_password_required_error()

        return current_result_username_required_error, current_result_password_required_error
