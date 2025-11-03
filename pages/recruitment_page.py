
from faker import Faker

from pages.base_page import BasePage
from utilities import test_data


class RecruitmentPage(BasePage):
    def click_recruitment_menu(self):
        self.wait_clickable(test_data.recruitment.RECRUITMENT_MENU).click()

    def click_add_candidate_btn(self):
        self.wait_clickable(test_data.recruitment.ADD_BTN).click()
    def add_candidate_info(self, first_name, middle_name, last_name, email, contact):
        candidate_data = {
            test_data.recruitment.FIRSTNAME: first_name,
            test_data.recruitment.MIDDLE_NAME: middle_name,
            test_data.recruitment.LASTNAME: last_name,
            test_data.recruitment.EMAIL: email,
            test_data.recruitment.CONTACT_NO: contact
        }
        values = []
        for locator, value in candidate_data.items():
            self.type(locator, value)
            element = self.wait_clickable(locator).get_attribute("value")
            values.append(element)

        return values
    def verify_candidate_info(self):
        locators = ["FIRSTNAME_PROFILE", "MIDDLENAME_PROFILE", "LASTNAME_PROFILE",
                     "EMAIL_PROFILE", "CONTACT_NO_PROFILE"
                    ]
        candidate_values = []
        for locator in locators:
            element = getattr(test_data.recruitment, locator)
            text_value = self.wait_clickable(element).get_attribute("value")
            candidate_values.append(text_value)

        return candidate_values

    def verify_add_valid_candidate(self):
        self.click_recruitment_menu()
        self.click_add_candidate_btn()
        fake =Faker()
        expected_result_values = self.add_candidate_info(fake.first_name(), fake.last_name(), fake.last_name(), fake.email(), "45123")

        self.action_click(test_data.recruitment.SAVE)
        current_result_values = self.verify_candidate_info()

        return current_result_values, expected_result_values

