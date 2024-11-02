import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators
from conftest import driver

class TestTransitions:
    # Тестирование перехода из ЛК в конструктор
    def test_button_constructor(self, driver):
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

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.BUTTON_LOGOUT)
        )

        # Найти "Конструктор" и нажать
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()

        # Добавить явное ожидание
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.FORM_CONSTRUCTOR)
        )

        time.sleep(3)

        assert driver.find_element(*TestLocators.FORM_CONSTRUCTOR)

    # Тестирование перехода из ЛК по Логотипу
    def test_logo_stellar_burgers (self, driver):
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

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.BUTTON_LOGOUT)
        )

        #Найти логотип и нажать
        driver.find_element(*TestLocators.LOGO).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.BUTTON_PLACE_AN_ORDER)
        )

        time.sleep(3)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'





