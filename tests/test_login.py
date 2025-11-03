import pytest

from pages.login_page import LoginPage


@pytest.mark.login
class TestLogin:
    @pytest.fixture
    def login_page(self, driver, delay):
        return LoginPage(driver, delay)

    def test_login_with_valid_credentials(self,login_page):
        current_url = login_page.verify_login_with_valid_credentials()

        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

        assert current_url == expected_url, \
            f"Expected url to be {expected_url}, but got {current_url} instead."

    def test_login_with_invalid_credentials(self, login_page):
        current_result_invalid_credential_error = login_page.verify_login_with_invalid_credentials()

        expected_result_invalid_credential_error = "Invalid credentials"

        assert current_result_invalid_credential_error == expected_result_invalid_credential_error, \
            f"Expected url to be {expected_result_invalid_credential_error}, but got {current_result_invalid_credential_error} instead."

    def test_login_without_username_and_password(self, login_page):
        current_result_username_required_error, current_result_password_required_error = login_page.verify_login_without_username_and_password()
        expected_result_username_required_error = "Required"
        expected_result_password_required_error = "Required"

        assert current_result_username_required_error == expected_result_username_required_error, \
            f"Expected url to be {expected_result_username_required_error}, but got {current_result_username_required_error} instead."

        assert current_result_password_required_error == expected_result_password_required_error, \
            f"Expected url to be {expected_result_password_required_error}, but got {current_result_password_required_error} instead."
