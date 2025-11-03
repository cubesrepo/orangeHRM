import time

from faker import Faker
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities import test_data


class PimPage(BasePage):
    def click_pim_menu(self):
        self.wait_clickable(test_data.pim.PIM_MENU).click()
    def click_add_employee_btn(self):
        self.wait_clickable(test_data.pim.ADD_EMPLOYEE_BTN).click()
    def type_employee_information(self, first_name, middle_name, last_name):
        self.type(test_data.pim.FIRST_NAME, first_name)
        self.type(test_data.pim.MIDDLE_NAME, middle_name)
        self.type(test_data.pim.LAST_NAME, last_name)

    def type_login_details(self, username, password, confirm_password):
        self.wait_clickable(test_data.pim.CREATE_LOGIN_TOGGLE).click()

        self.type(test_data.pim.USERNAME, username)
        self.type(test_data.pim.PASSWORD, password)
        self.type(test_data.pim.CON_PASSWORD, confirm_password)

    def get_success_message(self):
        return self.get_text(test_data.pim.SUCCESS_MESSAGE)
    def get_username_exists(self):
        return self.get_text(test_data.pim.USERNAME_EXISTS)
    def get_required_validation(self):
        for i in range(1, 5):
            locator = By.XPATH, f"(//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message'][normalize-space()='Required'])[{i}]"
            text = self.get_text(locator)
            if text != "Required":
                return text
        return "Required"

    def get_password_validation(self):
        password_must_be_7_char = self.get_text(test_data.pim.PASSWORD_MUST_BE_7_CHAR_ERROR)
        password_do_not_match = self.get_text(test_data.pim.PASSWORD_DO_NOT_MATCH)

        return password_must_be_7_char, password_do_not_match
    def get_input_fields_value(self, locator):
        element = self.wait_visibility(locator)
        return element.get_attribute("value")
    def add_employee(self):
        self.click_pim_menu()
        self.click_add_employee_btn()
        fake = Faker()

        password = "password123"

        self.type_employee_information(fake.first_name(),
                                       fake.name(),
                                       fake.last_name())
        self.type_login_details(fake.user_name(),
                                password,
                                password)
        employee_id = self.get_input_fields_value(test_data.pim.EMPLOYEE_ID_IN_ADD_EMPLOYEE)
        return employee_id
    def verify_adding_valid_employee_details(self):
        self.add_employee()

        self.wait_clickable(test_data.pim.SAVE).click()

        current_result_success_message = self.get_success_message()

        return current_result_success_message
    def verify_username_exists_validation(self):
        self.click_pim_menu()
        self.click_add_employee_btn()
        fake = Faker()
        username = "employee1"
        password = "password123"

        self.type_employee_information(fake.first_name(),
                                       fake.name(),
                                       fake.last_name())
        self.type_login_details(username,
                                password,
                                password)

        current_result_username_exists_message = self.get_username_exists()

        return current_result_username_exists_message

    def verify_required_validation_message(self):
        self.click_pim_menu()
        self.click_add_employee_btn()

        self.type_employee_information(" ",
                                       " ",
                                       " ")
        self.type_login_details(" ",
                                " ",
                                 " ")

        current_result_required_message = self.get_required_validation()

        return current_result_required_message
    def verify_password_validation(self):
        self.click_pim_menu()
        self.click_add_employee_btn()

        fake = Faker()

        password = "passw"
        conf_password = "pass"
        self.type_employee_information(fake.first_name(),
                                       fake.name(),
                                       fake.last_name())
        self.type_login_details(fake.user_name(),
                                password,
                                conf_password)

        current_result_password_must_be_7_char, current_result_password_do_not_match = self.get_password_validation()

        password_no_number = "password"
        self.type(test_data.pim.PASSWORD, password_no_number)
        time.sleep(1)
        current_result_password_must_contain_1_number = self.get_text((By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']"))
        return current_result_password_must_be_7_char, current_result_password_do_not_match, current_result_password_must_contain_1_number


    def verify_searching_added_employee(self):
        employee_id = self.add_employee()


        self.wait_clickable(test_data.pim.SAVE).click()
        time.sleep(2)
        self.wait_clickable(test_data.pim.EMPLOYEE_LISTS_BTN).click()
        self.type(test_data.pim.EMPLOYEE_ID_SEARCH, employee_id)

        time.sleep(2)
        self.wait_clickable(test_data.pim.SEARCH_BTN).click()

        current_result_employee_id_after_search = self.get_text(test_data.pim.EMPLOYEE_ID_RECORD_FOUND)
        expected_result_employee_id_after_search = employee_id
        current_result_record_found = self.get_text(test_data.pim.RECORD_FOUND)

        return current_result_employee_id_after_search,expected_result_employee_id_after_search,  current_result_record_found


