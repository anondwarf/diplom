import allure # type: ignore
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage(object):

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.page_url = ""
        self.wait = WebDriverWait(self.driver, 10, 1)

    def open(self) -> None:
        with allure.step(f"Открытие страницы {self.page_url}"): # type: ignore
            self.driver.get(self.page_url)

    @property
    def is_opened(self) -> bool:
        return self.wait.until(EC.url_contains(self.page_url))

    def click(self, locator: tuple[str, str]) -> None:
        with allure.step(f"Клик по элементу {locator}"): # type: ignore
            self.wait.until(EC.presence_of_element_located(locator)).click()

    def input_text(self, locator: tuple[str, str], text: str) -> None:
        with allure.step(f"Ввод текста {text} в {locator}"): # type: ignore
            self.wait.until(EC.presence_of_element_located(locator)).send_keys(text)

    def is_text_present(self, locator: tuple[str, str], text: str) -> bool:
        with allure.step(f"Проверка наличия текста {text} в {locator}"): # type: ignore
            return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    def is_element_present(self, locator: tuple[str, str]) -> bool:
        with allure.step(f"Проверка наличия элемента {locator}"): # type: ignore
            if self.wait.until(EC.presence_of_element_located(locator)):
                return True
            else:
                return False
