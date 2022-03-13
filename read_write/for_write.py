import os
import json
from pathlib import *

# путь файла
PATH_TO_FILE = f'{Path.home()}/Desktop/.allpwd.json'

def checExist():
    """
    Проверка пути до файла / если файл есть - пропускается
    если файла нет - то создается / Cам файл используется 
    для физического хранения паролей 
    """
    if os.path.exists(PATH_TO_FILE):
        print(f'\nФайл для записи найден, данные будут\
записаны по пути:\n{PATH_TO_FILE}')
    else:
        with open(PATH_TO_FILE, 'w'):
            print(f'\nФайл для записи отсутствует. Создан \
файл для записи по пути:\n{PATH_TO_FILE}')
    return PATH_TO_FILE


def new_inputer_datas():
    """сборщик данных от пользователя
    Returns:
        lst: для дальнейшей передачи в запись
    """    
    data = []
    elem_name = ['сервис', 'логин', 'пароль'] 
    for ind, elem in enumerate(elem_name):
        data.append(input(f'Введите {elem}: '))
    return data


def createn_data_struct(lst_data):
    """Создает словарь данных под запись
    Args:
        lst_data (list): список введенных значений под 
        запись
    Returns:
        data (dict): словарь с введенными данными
    """
    data = { 
    'service' : '',
    'login' : '',
    'password': ''
    }
    for ind, elem in enumerate(data):
        data[elem] = lst_data[ind]
    return data


def write_new_pass(save_path, data):
    """Запись данных в json
    Args:
        save_path (str): Путь до файла хранения данных
        data (dict): данные под запись
    """
    with open(save_path, 'r+', encoding='utf-8') as file:
        js_data = json.load(file)
    js_data['Loggins & passwords'].append(data)
    with open(save_path, 'w', encoding='utf-8') as f:
        json.dump(js_data, f, ensure_ascii=False, indent=3)


if __name__== '__main__':
    write_new_pass(
        checExist(),\
            createn_data_struct(
                new_inputer_datas()))