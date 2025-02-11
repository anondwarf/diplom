import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils import environment


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-nss')
    options.add_argument('--disable-extensions')
    service = Service(executable_path=environment.CHROME_DRIVER)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()