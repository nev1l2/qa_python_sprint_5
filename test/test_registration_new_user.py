import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import TestUrl
from helpers import generates_email, generates_password
from locators import TestLocators
from conftest import driver

class TestRegistration:

    # Тестирование формы регистрации с валидными данными "Email" и "Пароль"
    @pytest.mark.parametrize('email_char_num, psw_char_num', [[1,6], [2,7], [15,15]])
    def test_registration_with_valid_email_and_password(self,driver, email_char_num, psw_char_num):

        driver.get(TestUrl.MAIN_URL_TEST)

        # Найти кнопку "Войти в акаунт" и нажать
        driver.find_element(*TestLocators.BUTTON_LOGIN_IN_ACC_IN_MAIN).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.HEADER_FORM_LOGIN)
        )

        # Найти кнопку "Зарегистрироваться" и нажать
        driver.find_element(*TestLocators.HYPERTEXT_REGISTRATION).click()

        # Найти поле "Имя" и заполнить его
        driver.find_element(*TestLocators.INPUT_FORM_REGISTRATION_NAME).send_keys('Андрей')

        # Найти поле "Email" и заполни его
        driver.find_element(*TestLocators.INPUT_FORM_REGISTRATION_EMAIL).send_keys(generates_email(email_char_num))

        # Найти поле "Пароль" и заполни его
        driver.find_element(*TestLocators.INPUT_FORM_REGISTRATION_PASSWORD).send_keys(generates_password(psw_char_num))

        # Найти кнопку "Зарегистрироваться" и нажать
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.HEADER_FORM_LOGIN)
        )


        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_registration_with_incorrect_psw(self, driver):
        driver.get(TestUrl.MAIN_URL_TEST)

        # Найти кнопку "Войти в акаунт" и нажать
        driver.find_element(*TestLocators.BUTTON_LOGIN_IN_ACC_IN_MAIN).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.HEADER_FORM_LOGIN)
        )

        # Найти кнопку "Зарегистрироваться" и нажать
        driver.find_element(*TestLocators.HYPERTEXT_REGISTRATION).click()

        # Найти поле "Имя" и заполнить его
        driver.find_element(*TestLocators.INPUT_FORM_REGISTRATION_NAME).send_keys('Андрей')

        # Найти поле "Email" и заполни его
        driver.find_element(*TestLocators.INPUT_FORM_REGISTRATION_EMAIL).send_keys(generates_email(5))

        # Найти поле "Пароль" и заполни его
        driver.find_element(*TestLocators.INPUT_FORM_REGISTRATION_PASSWORD).send_keys('qw1')

        # Найти кнопку "Зарегистрироваться" и нажать
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()

        # Добавить явное ожидание для появления на странице сообщения об ошибке
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.INCORRECT_PASSWORD_MESSAGE)
        )

        # Убедиться в появлении сообщения об ошибке
        text_error = driver.find_element(*TestLocators.INCORRECT_PASSWORD_MESSAGE).text


        assert 'Некорректный пароль' in text_error