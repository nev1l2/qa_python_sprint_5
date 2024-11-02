import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators
from conftest import driver

class TestButtonPersAcc:
    # Тестирование перехода авторизованного пользователя
    def test_click_button_autorized_user(self,driver):
        driver.get('https://stellarburgers.nomoreparties.site/')

        # Найти кнопку "Войти в акаунт" и нажать
        driver.find_element(*TestLocators.BUTTON_LOGIN_IN_ACC_IN_MAIN).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.HEADER_FORM_LOGIN)
        )

        # Найти поле "Email" и заполни его
        driver.find_element(*TestLocators.INPUT_FORM_AUTHORIZATIONS_EMAIL).send_keys('buzov_andrey_12_123@yandex.ru')
        # Найти поле "Пароль" и заполни его
        driver.find_element(*TestLocators.INPUT_FORM_AUTHORIZATIONS_PASSWORD).send_keys('qwerty')
        # Найти кнопку "Войти" и нажать
        driver.find_element(*TestLocators.BUTTON_FORM_AUTHORIZATIONS_LOGIN).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.BUTTON_PLACE_AN_ORDER)
        )

        # Переходим в личный кабинет
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()

        time.sleep(3)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    # Тестирование перехода не авторизованного пользователя
    def test_click_button_unautorized_user(self,driver):
        driver.get('https://stellarburgers.nomoreparties.site/')

        # Переходим в личный кабинет
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.HEADER_FORM_LOGIN)
        )

        time.sleep(3)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


