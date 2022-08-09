import os

class TestData:

    BASE_URL = "https://demoqa.com/"
    PAGE_TITLE = "ToolsQA"

    FIRST_NAME = "Saro"
    LAST_NAME = "Navasardyan"
    EMPTY_LASTNAME = ""
    FULL_NAME = "Saro Navasardyan"
    EMAIL = "saronav@gmail.com"
    GENDER = "Male"
    MOBILE_NUMBER = "0077812521"
    WRONG_NUMBER = "sD2FER43FR"
    DATA = "12 August,2022"
    SUBJECTS_CONTAINER = "English"
    HOBBIES = "Sports"
    CHOOSE_FILE = os.path.abspath(os.curdir) + "/data/pic.jpg"
    FILE_NAME = "pic.jpg"
    CURRENT_ADDRESS = "Varser"
    SELECT_STATE = "NCR"
    SELECT_CITY = "Gurgaon"
    STATE_AND_CITY = "NCR Gurgaon"
    SUBMITTING_PAGE_TITLE = "Thanks for submitting the form"