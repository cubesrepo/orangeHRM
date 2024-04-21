import random
import string
import time

from faker import Faker
from selenium.webdriver.common.by import By

import test_data
from pages.base_page import BasePage


class RecruitmentPage(BasePage):
    def go_to_recruiment_page(self):
        time.sleep(2)

        #click recruitment menu
        recruitment_menu = self.wait_clickable(test_data.recruitment.RECRUITMENT_MENU)
        self.action_click(recruitment_menu)

        time.sleep(1)

        assert self.url_is("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")

    def add_valid_candidates(self):
        time.sleep(2)

        #click add btn
        self.wait_clickable(test_data.recruitment.ADD_BTN).click()

        time.sleep(2)

        self.url_is("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addCandidate")

        fake = Faker()
        #input firstname
        firstname_value = fake.first_name()
        self.send_keys(test_data.recruitment.FIRSTNAME, firstname_value)

        time.sleep(0.5)
        # input middlename
        middlename_value = ''.join(random.choices(string.ascii_lowercase, k=5))
        self.send_keys(test_data.recruitment.MIDDLENAME, middlename_value)

        time.sleep(0.5)
        # input lastname
        lastname_value = fake.last_name()
        self.send_keys(test_data.recruitment.LASTNAME, lastname_value)

        time.sleep(0.5)

        #click vacancy
        vacancy = self.wait_clickable(test_data.recruitment.VACANCY)
        vacancy.click()

        time.sleep(0.5)
        #lists of vacancy names
        vacancy_names = ["Sales Representative", "Senior QA Lead", "Senior Support Specialist", "Software Engineer", "Payroll Administrator"]

        #pick a random vacancy from the vacancy_names
        random_vacancy = random.choice(vacancy_names)

        #eleement of vacancy
        vacancy_item_element = By.XPATH, f"//div[@role='option']/span[text()='{random_vacancy}']"

        #click the vacancy item
        vacancy_item = self.wait_clickable(vacancy_item_element)
        self.action_click(vacancy_item)

        time.sleep(0.5)

        #input email
        email_value = f"{firstname_value}@gmail.com"
        self.send_keys(test_data.recruitment.EMAIL, email_value)

        time.sleep(0.5)

        # input contact number
        contac_no_value = fake.numerify("###########")
        self.send_keys(test_data.recruitment.CONTACT_NO, contac_no_value)

        time.sleep(0.5)
        # scroll down
        self.scroll_by_amount(0,150)

        time.sleep(0.5)
        #click save button
        self.wait_clickable(test_data.recruitment.SAVE).click()

        time.sleep(2)

        # assertion of inputted values
        assert self.get_value(test_data.recruitment.FIRSTNAME_PROFILE) == firstname_value
        assert self.get_value(test_data.recruitment.MIDDLENAME_PROFILE) == middlename_value
        assert self.get_value(test_data.recruitment.LASTNAME_PROFILE) == lastname_value
        assert self.get_text(test_data.recruitment.VACANCY_PROFILE) == random_vacancy
        assert self.get_value(test_data.recruitment.EMAIL_PROFILE) == email_value
        assert self.get_value(test_data.recruitment.CONTACT_NO_PROFILE) == contac_no_value

        self.wait_clickable(test_data.recruitment.CANDIDATES_BTN).click()

