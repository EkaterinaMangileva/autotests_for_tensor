from selenium.webdriver.common.by import By


class TensorLocators:
    TEXT_POWER_IS_IN_PEOPLE = (By.XPATH, "//p[contains(text(), 'Сила в людях')]")
    CLICK_ON_THE_CROSS = (By.XPATH, "//div[contains(@class, 'Close')]")
    MORE_DETAILS_BUTTON = (By.XPATH, "(//a[contains(text(), 'Подробнее')])[3]")
    PICTURE_ONE = (By.XPATH, "//img[@alt='Разрабатываем систему СБИС']")
    PICTURE_TWO = (By.XPATH, "//img[@alt='Продвигаем сервисы']")
    PICTURE_THREE = (By.XPATH, "//img[@alt='Создаем инфраструктуру']")
    PICTURE_FOUR = (By.XPATH, "//img[@alt='Сопровождаем клиентов']")

