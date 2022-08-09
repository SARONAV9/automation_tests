import pytest
from selenium import webdriver
from conf.config import TestData
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(params=["chrome"], scope='class')

def init_driver(request):
    if request.param == "chrome":
        options = Options()
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    request.cls.driver = web_driver
    yield
    web_driver.close()
