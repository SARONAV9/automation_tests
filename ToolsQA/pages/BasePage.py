
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from re import search

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def element_wait(self, locator):
        if search("//\*", locator):
            return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, locator)))
        elif search("css=", locator):
            return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        else:
            return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, locator)))

    def click(self, locator):
        self.element_wait(locator).click()

    def send_key(self, locator, text):
        self.element_wait(locator).send_keys(text)

    def get_element_text(self, locator):
        element = self.element_wait(locator).text
        return element

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(ec.title_is(title))
        return self.driver.title

    def fill_auto_complete_field(self, locator, text):
        field = self.element_wait(locator)
        field.send_keys(text)
        field.send_keys(Keys.ENTER)

    def click_enter(self, locator):
        self.element_wait(locator).send_keys(Keys.ENTER)

    def upload_picture(self, locator, photo_path):
        self.element_wait(locator).send_keys(photo_path)

    def get_color(self, locator):
        rgb = self.element_wait(locator).value_of_css_property('border-color')
        hex_color = Color.from_string(rgb).hex
        return hex_color
