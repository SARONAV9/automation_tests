from pages.PracticeFormPage import PracticeFormPage
from tests.test_Base import BaseTest


class TestPracticeFormPage(BaseTest):

    def test_practice_form_submission(self):
        self.practiceFormPage = PracticeFormPage(self.driver)
        self.practiceFormPage.check_page_title()
        self.practiceFormPage.go_test_page()
        self.practiceFormPage.fill_the_form()
        self.practiceFormPage.check_window_title()
        self.practiceFormPage.check_submitted_data_is_correct()
        self.practiceFormPage.close_the_modal_window()

    def test_practice_form_submission_negative_flow(self):
        self.practiceFormPage = PracticeFormPage(self.driver)
        self.practiceFormPage.check_page_title()
        self.practiceFormPage.go_test_page()
        self.practiceFormPage.fill_the_form_negative_data()