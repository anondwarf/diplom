from pytest import fixture
from selenium import webdriver


@fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
