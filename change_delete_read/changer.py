import os
import sys
from all_keys_srvices.show_all_serv import checkin, show_all
sys.path.append(os.path.join(os.getcwd(), ''))
import json
from const import PATH_TO_FILE


# def ex_params():
#     service = input('введите сервис, данные которого\
#  нужно заменить: ')
#     key = input('Введите что вы хотите заменить\
# (service / login / password): ')
#     value = input('Введите значение для замены: ')
#     return service, key, value
    

def changer_js(path):
    """парсит и вносит изменения +
         запишет новые данные в файл
    Args:
        path (str): путь до файла
    """
    with open(path, 'r') as jsf:
        data = json.load(jsf)
    show_all(data)
    service = input('введите сервис, данные которого\
 нужно заменить: ')
    if not checkin(service, data):
        print('Выбранный сервис не записан. Попробуйте еще раз...')
        changer_js(path)
    key = input('Введите что вы хотите заменить(service / login / password): ')
    if key not in ['service', 'login', 'password']:
        key = input(f'Вы ввели {key}! Если уверены, что хотите \
добавить новый "ключ", повторите ввод. \
В противном случае - введите верное значение ключа')
    value = input('Введите значение для замены: ')
    for i in data['Loggins & passwords']:
        if i['service'] == service:
            i[key] = value
    with open(path, 'w') as js_f:
        json.dump(data, js_f, ensure_ascii=False, indent=4)
        print(f' Данные по {service} в {key} \
изменены на {value}')

# if __name__ == "__main__":
#     changer_js(PATH_TO_FILE, ex_params())
