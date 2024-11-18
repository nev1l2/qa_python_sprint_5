import random
#генерация email содержащего прописные буквы и цифры
def generates_email(email_char_num):
    email = ''.join(random.choice(list('123456789qwertyuiopasdfghjklzxcvbnm')) for i in range(email_char_num))
    return f'{email}@yandex.ru'

#генерация пароля длинной 6 символов
def generates_password(psw_char_num):
    psw = ''.join(random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(psw_char_num))
    return psw