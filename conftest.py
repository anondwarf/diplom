from pytest import fixture
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


@fixture
def driver():
    s = Service(executable_path="/snap/bin/geckodriver")
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
