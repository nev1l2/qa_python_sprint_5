import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from locators import TestLocators
from conftest import driver

class TestFilterConstructor:
    # Тестирование перехода к разделу "Соусы"
    def test_go_to_section_cauces(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')

        # Найти и нажать на раздел "Соусы"
        driver.find_element(*TestLocators.BUTTON_SAUCES).click()

        # Добавить явное ожидание подсвечивания элемента "Соусы"
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.ACTIVE_BUTTON_SAUCES)
        )

        # Находим измененый div
        update_class = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]").get_attribute("class")

        time.sleep(3)

        assert 'tab_tab_type_current' in update_class

    # Тестирование перехода к разделу "Начинки"
    def test_go_to_section_fillings(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')

        # Найти и нажать на раздел "Начинки"
        driver.find_element(*TestLocators.BUTTON_FILLINGS).click()

        # Добавить явное ожидание подсвечивания элемента "Начинки"
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.ACTIVE_BUTTON_FILLINGS)
        )

        #
        update_class = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]").get_attribute("class")

        time.sleep(3)

        assert 'tab_tab_type_current' in update_class

    #Тестирование перехода к разделу "Булки"
    def test_go_to_section_buns(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')

        # Найти и нажать на раздел "Начинки"
        driver.find_element(*TestLocators.BUTTON_FILLINGS).click()

        # Найти и нажать на раздел "Булки"
        driver.find_element(*TestLocators.BUTTON_BUNS).click()

        # Добавить явное ожидание подсвечивания элемента "Начинки"
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.ACTIVE_BUTTON_BUNS)
        )

        #
        update_class = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]").get_attribute(
            "class")

        time.sleep(3)

        assert 'tab_tab_type_current' in update_class

