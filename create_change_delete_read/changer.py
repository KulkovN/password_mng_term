import os
import sys
import json
import readline
sys.path.append(os.path.join(os.getcwd(), ''))
from utils.texts import VARABLES
from utils.compliter import MyCompleter
from all_keys_srvices.show_all_serv import checkin, show_all


TEXTS = [f'Вы ввели значение ключа, которого нет в описание вашего серсива. \
Попробуйте езе раз: ']


def changer_js(path:str) -> None:
    """
    Парсит и вносит изменения +
    запишет новые данные в файл
    :param path - путь до файла
    """
    with open(path, 'r') as jsf:
        data = json.load(jsf)
    show_all(data)
    # compliter тут
    completer = MyCompleter([i['service'] for i in data['Loggins & passwords']])
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')
    service = input('введите сервис, данные которого\
 нужно заменить: ')
    if not checkin(service, data):
        print('Такой сервис отсутствует. Попробуйте еще раз')
        changer_js(path)
    key = input(f'Что меняем? (service/login/password): ')
    write_change(key, data, service, path)


def write_change(key:str, data:dict, service:str, path:str) -> None:
    """
    Функция парсера разита на две
    что бы была возможность зациклить проверку
    ввода пользователя на ключе под замену

    """
    if key in VARABLES:
        value = input('Введите значение для замены: ')
        for i in data['Loggins & passwords']:
            if i['service'] == service:
                i[key] = value
        with open(path, 'w') as js_f:
            json.dump(data, js_f, ensure_ascii=False, indent=4)
            print(f' Данные {service} в {key} изменены на {value}')
    else:
        key = input(TEXTS[0])
        write_change(key, data, service, path)
