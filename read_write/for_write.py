import os
from pathlib import Path
import json


def path_finder(func:object) -> str:
    """
    Декоратор для проверки пути до файла /
    если файла нет - то создается / 
    файл для хранения паролей 
    """
    def wrap(path:str, data:dict) -> None: # обертка
        if os.path.exists(path):
            func(path, data)
            print(f'\nФайл найден, данные записаны в:\n{path}')
        else:
            with open(path, 'w', encoding='utf-8') as file:
                json.dump({'Loggins & passwords':[]}, file,
                    ensure_ascii=False, indent=3)
            print(f'\nФайл отсутствует. Создан файл:\n{path}')
            wrap(path, data)
    return wrap


@path_finder
def write_new_pass(save_path:str, data:dict) -> None:
    """
    Запись данных в json
    :param save_path (str): Путь до файла хранения данных
    :param data (dict): данные под запись
    """
    with open(save_path, 'r+', encoding='utf-8') as file:
        js_data = json.load(file)
    js_data['Loggins & passwords'].append(data)
    with open(save_path, 'w', encoding='utf-8') as f:
        json.dump(js_data, f, ensure_ascii=False, indent=3)
