import os
import sys
import json
sys.path.append(os.path.join(os.getcwd(), ''))
from config.texts import VARABLES
from all_keys_srvices.show_all_serv import checkin, show_all

def changer_js(path:str) -> None:
    """
    Парсит и вносит изменения +
    запишет новые данные в файл
    :param path - путь до файла
    """
    with open(path, 'r') as jsf:
        data = json.load(jsf)
    show_all(data)
    service = input('введите сервис, данные которого\
 нужно заменить: ')
    if not checkin(service, data):
        print('Выбранный отсутствует. Попробуйте еще раз...')
        changer_js(path)
    key = input('Введите что вы хотите заменить(service / login / password): ')
    if key not in VARABLES:
        key = input(f'Вы ввели {key}! Если уверены, что хотите \
добавить новый "ключ", повторите ввод. \
В противном случае - введите корректное значение ключа')
    value = input('Введите значение для замены: ')
    for i in data['Loggins & passwords']:
        if i['service'] == service:
            i[key] = value
    with open(path, 'w') as js_f:
        json.dump(data, js_f, ensure_ascii=False, indent=4)
        print(f' Данные по {service} в {key} \
изменены на {value}')

