import json
from pathlib import Path


PATH_TO_FILE = f'{Path.home()}/Desktop/.allpwd.json'


def ex_params():
    service = input('введите сервис, данные которого\
 нужно заменить: ')
    key = input('Введите что вы хотите заменить\
(service / login / password): ')
    value = input('Введите значение для замены: ')
    return service, key, value
    

def changer_js(path, params=float): # float(key_service, key_to_change, value)):
    """парсит и вносит изменения +
         запишет новые данные в файл
    Args:
        path (str): _description_
        key_service (str): ключ сервиса для замены
        key_to_change (str): ключ под замену
        value (str): измененное значение
    """
    with open(path, 'r') as jsf:
        data = json.load(jsf)
    for i in data['Loggins & passwords']:
        if i['service'] == params[0]:
            i[params[1]] = params[2]
    with open(path, 'w') as js_f:
        json.dump(data, js_f, ensure_ascii=False, indent=4)
        print(f' Данные по {params[0]} в {params[1]} \
изменены на {params[2]}')


if __name__ == "__main__":
    changer_js(PATH_TO_FILE, ex_params())
