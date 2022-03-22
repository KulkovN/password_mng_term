import os
import sys
import json
sys.path.append(os.path.join(os.getcwd(), ''))
from utils.texts import VARABLES


TEXTS = [f'Вы ввели значение ключа, которого нет в описание вашего серсива. \
Попробуйте езе раз: ']


def write_change(data:dict, service:str, path:str) -> None:
    """
    Функция парсера разита на две
    что бы была возможность зациклить проверку
    ввода пользователя на ключе под замену

    """
    key = input(f'Что меняем? (service/login/password): ')
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
