import allure
from locators.sbis_locators import SbisLocators
from pages.base_page import BasePage


class SbisPage(BasePage):
    @allure.step("Откроем контакты")
    def open_contacts(self):
        self.element_is_visible(SbisLocators.CONTACTS).click()

    @allure.step("Откроем страницу тензора")
    def open_tensor_page(self):
        self.element_is_visible(SbisLocators.TENSOR_LOGO).click()
        self.switch_handles_window()


class SbisContactsPage(BasePage):
    @allure.step("Откроем страницу тензора")
    def open_tensor_page(self):
        self.element_is_visible(SbisLocators.TENSOR_LOGO).click()
        self.switch_handles_window()

    @allure.step("Проверить, что Свердловская область определилась")
    def check_region_was_decided(self):
        check_my_region = self.element_is_visible(SbisLocators.SVERDLOVSK_REGION)
        assert check_my_region.text == "Свердловская обл."

    @allure.step("Проверить, что есть список партнеров")
    def check_list_of_partners(self):
        check_list_of_partners_sverdlovsk_region = self.element_is_present(SbisLocators.LIST_OF_PARTNERS)
        assert check_list_of_partners_sverdlovsk_region.text is not None
        return check_list_of_partners_sverdlovsk_region.text

    @allure.step("Изменить регион на Камчатский край")
    def change_region(self):
        self.element_is_visible(SbisLocators.SVERDLOVSK_REGION).click()
        self.element_is_visible(SbisLocators.KAMCHATKA_KRAI).click()

    @allure.step("Проверить, что подставился выбранный регион")
    def check_region(self):
        check_the_region_was_changed = self.element_is_present(SbisLocators.CHECK_THERE_IS_KAMCHATKA_KRAI)
        assert check_the_region_was_changed.text == "Камчатский край"

    @allure.step("Проверить, что список партнеров изменился")
    def check_list_of_partners_has_changed(self, partners):
        check_list_of_partners_kamchatka_krai = self.element_is_present(SbisLocators.LIST_OF_PARTNERS)
        assert check_list_of_partners_kamchatka_krai.text is not None
        assert check_list_of_partners_kamchatka_krai.text != partners
