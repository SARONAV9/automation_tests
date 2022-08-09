
from selenium.webdriver import Keys
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator_type, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((locator_type, locator))).click()

    def do_send_key(self, locator_type, locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((locator_type, locator))).send_keys(text)

    def get_element_text(self, locator_type, locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((locator_type, locator))).text
        return element

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(ec.title_is(title))
        return self.driver.title

    def fill_auto_complete_field(self, locator_type, locator, text):
        field = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((locator_type, locator)))
        field.send_keys(text)
        field.send_keys(Keys.ENTER)

    def click_enter(self, locator_type, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((locator_type, locator))).send_keys(Keys.ENTER)

    def upload_picture(self, locator_type, locator, photo_path):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((locator_type, locator))).send_keys(photo_path)

    def get_color(self, locator_type, locator):
        rgb = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((locator_type, locator))).value_of_css_property('border-color')
        hex_color = Color.from_string(rgb).hex
        return hex_color
