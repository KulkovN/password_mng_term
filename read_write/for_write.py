import os
import sys
from pathlib import Path
sys.path.append(os.path.join(os.getcwd(), ''))
import json
from config.cr_pathes import PATH


# def path_creater():
#     PATH_TO_FILE = input('Введите путь для сохранения файла ваших паролей(полный): ')
#     path_const = f'{Path.cwd().parent}/const.py'
#     with open(path_const, 'w') as const_f:
#         const_f.write(f'from pathlib import Path\n\n\
# PATH_TO_FILE="{path_const}"')
#     with open(PATH_TO_FILE, 'w', encoding='utf-8') as file:
#             json.dump({'Loggins & passwords':[]}, file,
#                 ensure_ascii=False, indent=3)
#     return PATH_TO_FILE


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


if __name__ == "__main__":
    uid = {i:input(f'Введите ваш {i}') for i in \
                dict(service='', login='', password='')}
    write_new_pass(PATH_TO_FILE, uid)
