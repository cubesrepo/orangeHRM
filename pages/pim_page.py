import random
import string
import time

from faker import Faker
from selenium.webdriver.common.by import By

import test_data
from pages.base_page import BasePage


class PimPage(BasePage):
    #we first delete all records
    def got_to_pim_and_delete_all_records(self):
        time.sleep(3)

        # click pim menu
        pim_menu_item = self.wait_clickable(test_data.pim.PIM_MENU)
        self.action_click(pim_menu_item)

        time.sleep(1)

        # verify page url
        assert self.url_is("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")

        select_all_id = self.wait_clickable(test_data.pim.SELECT_ALL_ID)
        #scroll then click checkbox select all id
        self.scroll_by_amount(0, 100)

        self.action_click(select_all_id)
        #added try except because sometimes theres only one record and it cannot be deleted so the delete btn will not display
        try:
            time.sleep(0.5)
            # click delete btn
            delete_btn = self.wait_clickable(test_data.pim.DELETE_SELECTED_BTN)
            self.action_click(delete_btn)

            time.sleep(0.5)
            # click yest delete btn
            yes_delete = self.wait_clickable(test_data.pim.YES_DELETE)
            self.action_click(yes_delete)
        except:
            pass

    def add_valid_employee(self):
        fake = Faker()
        #add employee btn
        add_employee_btn = self.wait_clickable(test_data.pim.ADD_EMPLOYEE_BTN)
        self.action_click(add_employee_btn)

        time.sleep(3)

        #input firstname
        firstname_value = fake.name().split()[0]
        self.send_keys(test_data.pim.FIRST_NAME, firstname_value)

        time.sleep(0.5)

        # input middlename
        middlename_value = ''.join(random.choices(string.ascii_lowercase, k=5))
        middlename= self.wait_visibility(test_data.pim.MIDDLE_NAME)
        self.action_send_keys(middlename, middlename_value)

        time.sleep(0.5)

        # input lastname
        lastname_value = fake.name().split()[1]
        lastname = self.wait_visibility(test_data.pim.LAST_NAME)
        self.action_send_keys(lastname, lastname_value)

        time.sleep(0.5)
        #input employee id
        emoloyee_id_value = ''.join(random.choices(string.digits, k=4))
        emoployee_id = self.wait_visibility(test_data.pim.EMPLOYEE_ID)
        self.action_clear_input_and_send_keys(emoployee_id, emoloyee_id_value)


        time.sleep(0.5)
        image_path = r"C:\Users\Leonard\Downloads\example image.png"
        image_element = self.wait_presence(test_data.pim.ADD_IMAGE)
        self.action_send_keys(image_element, image_path)

        time.sleep(0.5)
        #click create login details togle
        self.wait_clickable(test_data.pim.CREATE_LOGIN_TOGGLE).click()

        time.sleep(0.5)

        #input username
        username_value = ''.join(random.choices(string.ascii_lowercase, k=6))
        self.send_keys(test_data.pim.USERNAME, username_value)

        time.sleep(0.5)

        # input password
        password_value = "Password123"
        self.send_keys(test_data.pim.PASSWORD, password_value)

        time.sleep(0.5)

        # confirm password
        self.send_keys(test_data.pim.CON_PASSWORD, password_value)

        time.sleep(0.5)

        #click save
        self.scroll_by_amount(0, 100)
        self.wait_visibility(test_data.pim.SAVE).click()

        time.sleep(2)

        #assert if the inputted personal details are correct
        assert self.get_value(test_data.pim.EMPLOYEE_FIRSTNAME) == firstname_value
        assert self.get_value(test_data.pim.EMPLOYEE_MIDDLENAME) == middlename_value
        assert self.get_value(test_data.pim.EMPLOYEE_LASTNAME) == lastname_value

        return emoloyee_id_value

    def loop_to_add_5_employees(self):
        employee_list = []
        #loop for adding 10 valid employeess
        for _ in range(6):
            employee_list.append(self.add_valid_employee())
            time.sleep(1.5)

        time.sleep(1)

        #go to employee list to search for added employee using their employee id
        employee_list_btn = self.wait_clickable(test_data.pim.EMPLOYEE_LIST_BTN)
        self.action_click(employee_list_btn)

        time.sleep(0.5)

        if self.driver.current_url != "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList":
            self.wait_clickable(test_data.pim.EMPLOYEE_LIST_BTN).click()


        time.sleep(1)

        return employee_list

    def search_all_added_employee_using_employee_id(self):
        time.sleep(3)

        lists = self.loop_to_add_5_employees()

        #added loop to search for added employees
        for employee in lists:

            #input userid to search
            employee_id_input = self.wait_visibility(test_data.pim.EMPLOYEE_ID_SEARCH)
            self.action_clear_input_and_send_keys(employee_id_input, employee)

            time.sleep(1)
            #click search btn
            search_btn = self.wait_clickable(test_data.pim.SEARCH_BTN)
            self.action_click(search_btn)

            time.sleep(1.5)

            #check if the employee id is display then scroll
            EMPLOYEE_ID_OUTPUT = By.XPATH, f"//div[contains(text(),'{employee}')]"
            employee = self.wait_presence(EMPLOYEE_ID_OUTPUT)
            self.scroll_to_element(employee)

            #scroll back to employee id searchbtn
            time.sleep(0.5)
            employee_id_field = self.wait_presence(test_data.pim.EMPLOYEE_ID_SEARCH)
            self.scroll_to_element(employee_id_field)

            time.sleep(2)

    def edit_employee(self):
        time.sleep(3)
        employee_id = self.add_valid_employee()

        # go to employee list to search for added employee using their employee id
        employee_list_btn = self.wait_clickable(test_data.pim.EMPLOYEE_LIST_BTN)
        self.action_click(employee_list_btn)

        if self.driver.current_url != "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList":
            time.sleep(0.5)
            self.wait_clickable(test_data.pim.EMPLOYEE_LIST_BTN).click()

        time.sleep(0.5)
        # input userid to search
        employee_id_input = self.wait_visibility(test_data.pim.EMPLOYEE_ID_SEARCH)
        self.action_clear_input_and_send_keys(employee_id_input, employee_id)

        time.sleep(0.5)
        # click search btn
        search_btn = self.wait_clickable(test_data.pim.SEARCH_BTN)
        self.action_click(search_btn)
        time.sleep(0.5)

        # scroll down
        self.scroll_by_amount(0, 150)

        time.sleep(0.5)

        # click edit button
        self.wait_clickable(test_data.pim.EDIT_BTN).click()

        time.sleep(1)

        #scroll down
        self.scroll_by_amount(0, 150)

        time.sleep(2)

        #click nationality and select
        nationality_item = ["Chinese", "German", "American"]
        self.wait_clickable(test_data.pim.EDIT_NATIONALITY).click()
        random_item = random.choice(nationality_item)
        nationality_element = By.XPATH, f"//div[@role='option']/span[text()='{random_item}']"
        nationality = self.wait_clickable(nationality_element)
        self.action_click(nationality)

        time.sleep(0.5)

        # click status and select
        status_item = ["Single", "Married", "Other"]
        self.wait_clickable(test_data.pim.EDIT_MARITAL).click()
        random_status = random.choice(status_item)
        status_element = By.XPATH, f"//div[@role='option']/span[text()='{random_status}']"
        status = self.wait_clickable(status_element)
        self.action_click(status)

        time.sleep(0.5)
        #clickd bday date
        self.wait_clickable(test_data.pim.EDIT_DATE_BIRTH).click()

        time.sleep(0.5)
        # click day 4
        self.wait_clickable(test_data.pim.EDIT_DAY).click()

        time.sleep(0.5)
        #click female gender
        gender =  self.wait_presence(test_data.pim.EDIT_FEMALE_GENDER)
        self.scroll_to_element(gender)
        self.wait_clickable(test_data.pim.EDIT_FEMALE_GENDER).click()

        time.sleep(0.5)
        #click save
        self.wait_clickable(test_data.pim.EDIT_SAVE_ONE).click()




