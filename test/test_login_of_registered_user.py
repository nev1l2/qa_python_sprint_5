import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators
from conftest import driver

class TestLoginUsers:
    # Тестирование входа по кнопке «Войти в аккаунт» на главной
    def test_login_by_button_on_main(self,driver):
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

    # Тестирование входа через кнопку «Личный кабинет»
    def test_login_by_button_from_personal_account(self,driver):
        driver.get('https://stellarburgers.nomoreparties.site/')

        # Находим кнопку "Личный кабинет" и нажать
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()

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

    # Тестирование входа через кнопку в форме регистрации
    def test_login_by_button_from_registration_form(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')

        # Найти кнопку "Войти" и нажать
        driver.find_element(*TestLocators.LOGIN_FROM_AUTHORIZATIONS).click()

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
    # Тестирование вход через кнопку в форме восстановления пароля
    def test_login_by_button_from_psw_recovery_form (self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')

        # Найти кнопку "Войти" и нажать
        driver.find_element(*TestLocators.LOGIN_FROM_RECOVERY_PSW).click()

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


