from selenium.webdriver.common.by import By
from core import BasePage
from core.base_page import WebDriver
from utils import environment


class _Locator(object):

    LINK_ACCOUNT = (By.XPATH, "//a[@href='/account']")
    LINK_FEED = (By.XPATH, "//a[@href='/feed']")
    MODAL_OPEN = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    MODAL_CLOSE = (By.XPATH, "//section[contains(@class, 'Modal_modal__P3_V5')]")
    BUTTON_CLOSE_MODAL = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    LINK_FIRST_INGREDIENT = (By.XPATH, "//a[contains(@class, 'ingredient')]")
    COUNTER_FIRST_INGREDIENT = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")
    BURGER_CONSTRUCTOR = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")
    APPROVE_ORDER_CREATED = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")
    BUTTON_CREATE_ORDER = (By.XPATH, "//button[text() = 'Оформить заказ']")


class MainPage(BasePage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.page_url = str(environment.BASE_URL)

    def click_link_account(self) -> None:
        self.click(locator=_Locator.LINK_ACCOUNT)

    def got_to_feed_page(self) -> None:
        self.click(locator=_Locator.LINK_FEED)

    def click_fist_ingredient(self) -> None:
        self.click(locator=_Locator.LINK_FIRST_INGREDIENT)

    def close_modal(self) -> None:
        self.click(locator=_Locator.BUTTON_CLOSE_MODAL)

    @property
    def is_modal_present(self) -> bool:
        return self.is_element_present(locator=_Locator.MODAL_OPEN)

    @property
    def is_modal_not_present(self) -> bool:
        return self.is_element_present(locator=_Locator.MODAL_CLOSE)

    @property
    def count_ingredients(self) -> int:
        return int(self.driver.find_element(*_Locator.COUNTER_FIRST_INGREDIENT).text)

    def add_first_ingredient_to_constructor(self) -> None:
        self.move_element(start_locator=_Locator.LINK_FIRST_INGREDIENT, end_locator=_Locator.BURGER_CONSTRUCTOR)

    def create_order(self) -> None:
        self.add_first_ingredient_to_constructor()
        self.click(locator=_Locator.BUTTON_CREATE_ORDER)

    @property
    def is_order_created(self) -> bool:
        return self.is_text_present(locator=_Locator.APPROVE_ORDER_CREATED, text="Ваш заказ начали готовить")
