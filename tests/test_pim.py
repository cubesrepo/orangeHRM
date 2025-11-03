import pytest

from pages.pim_page import PimPage

@pytest.mark.pim
class TestPimPage:
    @pytest.fixture
    def pim_page(self, login_driver, delay):
        return PimPage(login_driver, delay)

    #@pytest.mark.skip
    def test_adding_valid_employee_details(self, pim_page):
        current_result_success_message = pim_page.verify_adding_valid_employee_details()

        expected_result_success_message = "Successfully Saved"

        assert  current_result_success_message == expected_result_success_message,\
            f"Expected result to be {expected_result_success_message}, but got {current_result_success_message} instead"

    #@pytest.mark.skip
    def test_username_exists_validation(self, pim_page):
        current_result_username_exists_message = pim_page.verify_username_exists_validation()

        expected_result_username_exists_message = "Username already exists"

        assert  current_result_username_exists_message == expected_result_username_exists_message,\
            f"Expected result to be {expected_result_username_exists_message}, but got {current_result_username_exists_message} instead"

    #@pytest.mark.skip
    def test_required_validation(self, pim_page):
        current_result_required_message = pim_page.verify_required_validation_message()

        expected_result_required_message = "Required"

        assert  current_result_required_message == expected_result_required_message,\
            f"Expected result to be {expected_result_required_message}, but got {current_result_required_message} instead"

    #@pytest.mark.skip
    def test_password_validation(self, pim_page):
        current_result_password_must_be_7_char, current_result_password_do_not_match,current_result_password_must_contain_1_number\
            = pim_page.verify_password_validation()

        expected_result_password_must_be_7_char = "Should have at least 7 characters"
        expected_result_password_do_not_match = "Passwords do not match"
        expected_result_password_must_contain_1_number = "Your password must contain minimum 1 number"

        assert  current_result_password_must_be_7_char == expected_result_password_must_be_7_char,\
            f"Expected result to be {expected_result_password_must_be_7_char}, but got {current_result_password_must_be_7_char} instead"

        assert current_result_password_do_not_match == expected_result_password_do_not_match, \
            f"Expected result to be {expected_result_password_do_not_match}, but got {current_result_password_do_not_match} instead"

        assert current_result_password_must_contain_1_number == expected_result_password_must_contain_1_number, \
            f"Expected result to be {expected_result_password_must_contain_1_number}, but got {current_result_password_must_contain_1_number} instead"

    def test_searching_added_employee(self, pim_page):
        current_result_employee_id_after_search, expected_result_employee_id_after_search, current_result_record_found = pim_page.verify_searching_added_employee()

        expected_result_record_found = "(1) Record Found"

        assert current_result_employee_id_after_search == expected_result_employee_id_after_search, \
            f"Expected result to be {expected_result_employee_id_after_search}, but got {current_result_employee_id_after_search} instead"

        assert current_result_record_found == expected_result_record_found, \
            f"Expected result to be {expected_result_record_found}, but got {current_result_record_found} instead"
