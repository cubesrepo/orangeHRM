from selenium.webdriver.common.by import By

BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

CREDENTIALS = {
    "USERNAME" : "Admin",
    "PASSWORD" : "admin123",
    "INVALID_USERNAME": "Admin123",
    "INVALID_PASSWORD": "Admin"

}

class login:
    USERNAME = By.XPATH, "//input[@name='username']"
    PASSWORD = By.XPATH, "//input[@name='password']"
    LOGIN_BTN = By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']"

    USERNAME_VALIDATION = By.XPATH, "(//div[@class='oxd-input-group oxd-input-field-bottom-space'])[1]/span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']"
    PASSWORD_VALIDATION = By.XPATH, "(//div[@class='oxd-input-group oxd-input-field-bottom-space'])[2]/span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']"

    INVALID_CREDENTIALS = By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"
class pim:
    PIM_MENU = By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']"
    ADD_EMPLOYEE_BTN = By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-item' and text()='Add Employee']"
    EMPLOYEE_LISTS_BTN = By.XPATH, "//a[normalize-space()='Employee List']"
    # for adding employee
    FIRST_NAME = By.XPATH, "//input[@name='firstName']"
    MIDDLE_NAME = By.XPATH, "//input[@name='middleName']"
    LAST_NAME = By.XPATH, "//input[@name='lastName']"
    ADD_IMAGE = By.CSS_SELECTOR, "input[type='file']"
    CREATE_LOGIN_TOGGLE = By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']"
    USERNAME = By.XPATH, "(//input[@autocomplete='off'])[1]"
    PASSWORD = By.XPATH, "(//input[@type='password'])[1]"
    CON_PASSWORD = By.XPATH, "(//input[@type='password'])[2]"
    SAVE = By.XPATH, "//button[normalize-space()='Save']"
    USERNAME_EXISTS = By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']"
    SUCCESS_MESSAGE = By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']"
    EMPLOYEE_ID_IN_ADD_EMPLOYEE = By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
    EMPLOYEE_ID = By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input[@class='oxd-input oxd-input--active']"
    PASSWORD_MUST_BE_7_CHAR_ERROR = By.XPATH,"(//span[normalize-space()='Should have at least 7 characters'])[1]"
    PASSWORD_DO_NOT_MATCH = By.XPATH, "//span[normalize-space()='Passwords do not match']"
    #delete records
    SELECT_ALL_ID = By.XPATH, "//span[@class='oxd-checkbox-input oxd-checkbox-input--active --label-right oxd-checkbox-input']"
    DELETE_SELECTED_BTN = By.XPATH, "//button[@type='button' and normalize-space()='Delete Selected']"
    YES_DELETE = By.XPATH, "//button[@type='button' and normalize-space() ='Yes, Delete']"

    #personal details assertion
    EMPLOYEE_FIRSTNAME = By.XPATH, "//input[@name='firstName']"
    EMPLOYEE_MIDDLENAME = By.XPATH, "//input[@name='middleName']"
    EMPLOYEE_LASTNAME = By.XPATH, "//input[@name='lastName']"



    #for searchin employee
    EMPLOYEE_ID_SEARCH = By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]"
    SEARCH_BTN = By.CSS_SELECTOR, "button[type='submit']"
    RECORD_FOUND = By.CSS_SELECTOR, "div[class='orangehrm-horizontal-padding orangehrm-vertical-padding'] span[class='oxd-text oxd-text--span']"
    EMPLOYEE_ID_RECORD_FOUND = By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)"
    EDIT_BTN = By.XPATH, "(//button[@class='oxd-icon-button oxd-table-cell-action-space'])[2]"
    EDIT_NATIONALITY = By.XPATH, "(//div[@class='oxd-select-text oxd-select-text--active'])[1]"
    EDIT_NATIONALITY_VALUE = By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active'][1]/div[@class='oxd-select-text-input']"
    EDIT_MARITAL = By.XPATH, "(//div[@class='oxd-select-text oxd-select-text--active'])[2]"
    EDIT_MARITAL_VALUE = By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active'][2]/div[@class='oxd-select-text-input']"
    EDIT_DATE_BIRTH = By.XPATH, "//input[@placeholder='yyyy-dd-mm']"
    EDIT_YEAR_HEADER = By.XPATH, "//li[@class='oxd-calendar-selector-year']"
    EDIT_YEAR_VALUE = By.XPATH, "//li[@class='oxd-calendar-dropdown--option' and text()='2000']"
    EDIT_DAY = By.XPATH, "//div[@class='oxd-calendar-date' and normalize-space()='4']"
    EDIT_FEMALE_GENDER = By.XPATH, "//label[normalize-space()='Female']"
    EDIT_ADD = By.XPATH, "//button[@type='button' and normalize-space()='Add']"

    EDIT_UPLOAD_FILE = By.XPATH, "//div[text()='No file selected']"
    EDIT_COMMENT = By.XPATH, "//textarea[@placeholder='Type comment here']"

    EDIT_SAVE_ONE = By.XPATH, "(//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'])[1]"

    EDIT_SAVE_THREE = By.XPATH, "(//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'])[3]"

class recruitment:
    RECRUITMENT_MENU = By.XPATH, "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']"

    ADD_BTN = By.XPATH, "//button[@type='button']/i[@class='oxd-icon bi-plus oxd-button-icon']"

    FIRSTNAME = By.XPATH, "//input[@name='firstName']"
    MIDDLE_NAME = By.XPATH, "//input[@name='middleName']"
    LASTNAME = By.XPATH, "//input[@name='lastName']"
    VACANCY = By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']"
    VACANCY_ITEM = By.XPATH, "//div[@role='option']/span[text()='Senior QA Lead']"
    EMAIL = By.XPATH, "(//input[@placeholder='Type here'])[1]"
    CONTACT_NO = By.XPATH, "(//input[@placeholder='Type here'])[2]"

    SAVE = By.XPATH, "//button[normalize-space()='Save']"

    #candidate profile

    FIRSTNAME_PROFILE = By.XPATH, "//input[@placeholder='First Name']"
    MIDDLENAME_PROFILE = By.XPATH, "//input[@placeholder='Middle Name']"
    LASTNAME_PROFILE = By.XPATH, "//input[@placeholder='Last Name']"
    VACANCY_PROFILE = By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active oxd-select-text--readonly']/div[@class='oxd-select-text-input']"
    EMAIL_PROFILE = By.XPATH, "(//input[@placeholder='Type here'])[1]"
    CONTACT_NO_PROFILE = By.XPATH, "(//input[@placeholder='Type here'])[2]"

    CANDIDATES_BTN = By.XPATH, "//li[@class='oxd-topbar-body-nav-tab --visited']/a[@class='oxd-topbar-body-nav-tab-item' and text()='Candidates']"

