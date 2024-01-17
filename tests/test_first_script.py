from pages.sbis_page import SbisPage, SbisContactsPage
from pages.tensor_page import TensorPage
import allure


class TestCases:
    target_link = 'https://tensor.ru/about'

    @allure.title("Первый сценарий")
    def test_first_script_actions(self, driver):
        sbis_page = SbisPage(driver, "https://sbis.ru/")
        sbis_page.open()
        sbis_page.open_contacts()
        sbis_page.open_tensor_page()
        tensor_page = TensorPage(driver, "https://tensor.ru/")
        tensor_page.should_be_strength_is_in_people()
        tensor_page.open_detail_info()
        tensor_page.should_be_image_same_size()
        assert driver.current_url == self.target_link, f'Ссылка не соответствует {self.target_link}!'

    @allure.title("Второй сценарий")
    def test_second_script_actions(self, driver):
        sbis_page = SbisPage(driver, "https://sbis.ru/")
        sbis_page.open()
        sbis_page.open_contacts()
        sbis_contacts = SbisContactsPage(driver, "https://sbis.ru/contacts")
        sbis_contacts.check_region_was_decided()
        list_of_partners = sbis_contacts.check_list_of_partners()
        sbis_contacts.change_region()
        sbis_contacts.check_region()
        sbis_contacts.check_list_of_partners_has_changed(list_of_partners)
        target_url = 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
        assert driver.current_url == target_url
        assert 'kamchatskij-kraj' in target_url, f'Ссылка не соответствует {target_url}!'
