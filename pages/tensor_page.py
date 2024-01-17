import allure
from selenium.webdriver import ActionChains
from locators.tensor_locators import TensorLocators
from pages.base_page import BasePage


class TensorPage(BasePage):
    @allure.step("Проверим наличие блока Сила в людях")
    def should_be_strength_is_in_people(self):
        self.element_is_visible(TensorLocators.CLICK_ON_THE_CROSS).click()
        text_assert = self.element_is_visible(TensorLocators.TEXT_POWER_IS_IN_PEOPLE)
        show_more_button = self.element_is_visible(TensorLocators.MORE_DETAILS_BUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(show_more_button).perform()
        assert text_assert.text == "Сила в людях"

    @allure.step("Нажать подробнее")
    def open_detail_info(self):
        self.element_is_visible(TensorLocators.MORE_DETAILS_BUTTON).click()

    @allure.step("Проверим размеры изображений")
    def should_be_image_same_size(self):
        basic_image_elements = [
            TensorLocators.PICTURE_ONE,
            TensorLocators.PICTURE_TWO,
            TensorLocators.PICTURE_THREE,
            TensorLocators.PICTURE_FOUR,
        ]
        images_size = []
        for element in basic_image_elements:
            images_size.append(self.element_is_visible(element).size)
        assert images_size[:-1] == images_size[1:], 'Одно или несколько изображений разных размеров'
