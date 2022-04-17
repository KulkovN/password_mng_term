import os
import pyAesCrypt
from uuid import uuid4
from hashlib import sha256


def _hash(pwd) -> str:
    """ Создает хеш для записи в конфиг

    :param pwd: строка пароля под запись
    :return: венет строку в хеше
    """
    salt = uuid4().hex
    return sha256(salt.encode() + pwd.encode()).hexdigest() + ':' + salt


def check_pwd(h_pwd:str, pwd) -> bool:
    """ Проверка пароля пользователя

    :param h_pwd: захешованый пароль из конфига
    :param pwd: пароль пользователя при входе
    :return: булево-значение проверки
    """
    password, salt = h_pwd.split(':')
    return password == sha256(salt.encode() + pwd.encode()).hexdigest()


def crypt(file, paswd, flag):
    """ Функция для шифровки и проверки
    шифрования существующего файла

    :param file: файл для шифрования
    :param paswd: пароль для шифрования
    :param flag: флаг шифрования
    """
    buffer = 512 * 1024
    # шифруем 
    if flag == 'crypt':
        pyAesCrypt.encryptFile(file, f'{file}.aes'\
            ,paswd, buffer) 
        os.remove(file)
    # дешифруем
    else:
        pyAesCrypt.decryptFile(file\
            ,os.path.splitext(file)[0],
            paswd, buffer)
        os.remove(file)


# if __name__ == '__main__':
#     crypt('/Users/kulkovni/Desktop/.all_pwd.json', '3571', 'crypt')