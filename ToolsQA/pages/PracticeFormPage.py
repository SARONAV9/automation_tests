from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from conf.config import TestData

class PracticeFormPage(BasePage):

    # Practice Form page locators
    ELEMENTS = "//*[text()='Elements']"
    CLOSE_ELEMENTS = "//*[@class='header-wrapper'][1]"
    FORMS = "//*[text()='Forms']"
    PRACTICE_FORM = "//*[contains(.//span,'Practice Form')][1]"
    FIRST_NAME = "//*[@id='firstName']"
    LAST_NAME = "//*[@id='lastName']"
    EMAIL = "//*[@id='userEmail']"
    GENDER = "//*[text()='Male']"
    MOBILE_NUMBER = "//*[@id='userNumber']"
    DATE_OF_BIRTH_INPUT = "//*[@id='dateOfBirthInput']"
    DATE_OF_BIRTH = "//div[text()='12']"
    SUBJECTS_CONTAINER = "subjectsInput"
    HOBBIES = "//*[text()='Sports']"
    CHOOSE_FILE = "uploadPicture"
    CURRENT_ADDRESS = "//*[@id='currentAddress']"
    SELECT_STATE = "react-select-3-input"
    SELECT_CITY = "react-select-4-input"
    SUBMIT = "submit"

    # Form modal table locators
    MODAL_WINDOW_TITLE = "example-modal-sizes-title-lg"
    CLOSE_MODAL_WINDOW_BUTTON = "//*[@id='closeLargeModal']"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def go_test_page(self):
        self.do_click(By.XPATH, self.ELEMENTS)
        self.do_click(By.XPATH, self.CLOSE_ELEMENTS)
        self.do_click(By.XPATH, self.FORMS)
        self.do_click(By.XPATH, self.PRACTICE_FORM)

    def fill_the_form(self):
        self.do_send_key(By.XPATH, self.FIRST_NAME, TestData.FIRST_NAME)
        self.do_send_key(By.XPATH, self.LAST_NAME, TestData.LAST_NAME)
        self.do_send_key(By.XPATH, self.EMAIL, TestData.EMAIL)
        self.do_send_key(By.XPATH, self.MOBILE_NUMBER, TestData.MOBILE_NUMBER)
        self.do_click(By.XPATH, self.DATE_OF_BIRTH_INPUT)
        self.do_click(By.XPATH, self.DATE_OF_BIRTH)
        self.do_click(By.XPATH, self.HOBBIES)
        self.upload_picture(By.ID, self.CHOOSE_FILE, TestData.CHOOSE_FILE )
        self.do_send_key(By.XPATH, self.CURRENT_ADDRESS, TestData.CURRENT_ADDRESS)
        self.fill_auto_complete_field(By.ID, self.SELECT_STATE, TestData.SELECT_STATE)
        self.fill_auto_complete_field(By.ID, self.SELECT_CITY, TestData.SELECT_CITY)
        self.fill_auto_complete_field(By.ID, self.SUBJECTS_CONTAINER, TestData.SUBJECTS_CONTAINER)
        self.do_click(By.XPATH, self.GENDER)
        self.click_enter(By.ID, self.SUBMIT)

    def fill_the_form_negative_data(self):
        self.do_send_key(By.XPATH, self.FIRST_NAME, "")
        self.do_send_key(By.XPATH, self.LAST_NAME, TestData.EMPTY_LASTNAME)
        self.do_send_key(By.XPATH, self.MOBILE_NUMBER, TestData.WRONG_NUMBER)
        self.fill_auto_complete_field(By.ID, self.SELECT_STATE, TestData.SELECT_STATE)
        self.click_enter(By.ID, self.SUBMIT)
        self.do_click(By.XPATH, self.FIRST_NAME)
        assert self.get_color(By.XPATH, self.FIRST_NAME) == "#dc3545", "The form control isn't work"
        self.do_click(By.XPATH, self.LAST_NAME)
        assert self.get_color(By.XPATH, self.LAST_NAME) == "#dc3545", "The form control isn't work"
        assert self.get_color(By.XPATH, self.GENDER) == "#dc3545", "The form control isn't work"
        self.do_click(By.XPATH, self.MOBILE_NUMBER)
        assert self.get_color(By.XPATH, self.MOBILE_NUMBER) == "#dc3545", "The form control isn't work"

    def check_window_title(self):
        title = self.get_element_text(By.ID, self.MODAL_WINDOW_TITLE)
        assert title == TestData.SUBMITTING_PAGE_TITLE, "The form modal window title is wrong"

    def check_page_title(self):
        title = self.get_title(TestData.PAGE_TITLE)
        assert title == TestData.PAGE_TITLE, TestData.PAGE_TITLE

    def check_submitted_data_is_correct(self):
        labels = ["Student Name", "Student Email", "Gender", "Mobile", "Date of Birth", "Subjects", "Hobbies", "Picture", "Address", "State and City"]
        submitted_values = [TestData.FIRST_NAME + " " + TestData.LAST_NAME, TestData.EMAIL, TestData.GENDER, TestData.MOBILE_NUMBER, TestData.DATA, TestData.SUBJECTS_CONTAINER, TestData.HOBBIES, TestData.FILE_NAME, TestData.CURRENT_ADDRESS, TestData.STATE_AND_CITY]
        for i in range(10):
            value = "//td[contains(text()," + " " + "\"" + labels[i] + "\"" + ")]/../td[2]"
            element = self.driver.find_element(By.XPATH, value)
            assert element.text == submitted_values[i]

    def close_the_modal_window(self):
        self.do_click(By.XPATH, self.CLOSE_MODAL_WINDOW_BUTTON)
