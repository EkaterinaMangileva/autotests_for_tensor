from selenium.webdriver.common.by import By


class SbisLocators:
    CONTACTS = (By.XPATH, "//a[contains(text(), 'Контакты')]")
    TENSOR_LOGO = (By.XPATH, "(//img[contains(@src, 'images/logo.svg')])[1]")
    SVERDLOVSK_REGION = (By.XPATH, "(//span[contains(text(), 'Свердловская обл.')])[1]")
    KAMCHATKA_KRAI = (By.XPATH, "//span[@title = 'Камчатский край']")
    CHECK_THERE_IS_KAMCHATKA_KRAI = (By.XPATH, '//span[text() = "Камчатский край"]')
    LIST_OF_PARTNERS = (By.XPATH, '//div[@data-qa="items-container"]')
    SBIS_KAMCHATKA_TITLE = (By.XPATH, "//div[@title='СБИС - Камчатка']")
