Тестирование сервиса Stellar Burgers
Реализованы тесты
1. Регистрация // test_registration_new_user
- Успешную регистрацию. Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен. Минимальный пароль — шесть символов.
- Ошибку для некорректного пароля.
2. Вход // test_login_of_registered_user
- вход по кнопке «Войти в аккаунт» на главной,
- вход через кнопку «Личный кабинет»,
- вход через кнопку в форме регистрации,
- вход через кнопку в форме восстановления пароля.
3. Переход в личный кабинет // test_transitions_from_personal_account
- Проверь переход по клику на «Личный кабинет».
- Переход из личного кабинета в конструктор 
- Проверь переход по клику на «Конструктор» и на логотип Stellar Burgers.
4. Выход из аккаунта // test_logout
- Проверь выход по кнопке «Выйти» в личном кабинете.
5. Раздел «Конструктор» // test_constructor
Работают переходы к разделам:
- «Булки»,
- «Соусы»,
- «Начинки».