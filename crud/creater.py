import os
import json


def path_finder(func:object) -> str:
    """
    Декоратор для проверки пути до файла /
    если файла нет - то создается / 
    файл для хранения паролей 
    """
    def wrap(path:str) -> None: # обертка
        if os.path.exists(path):
            func(path)
            print(f'\nФайл найден, данные записаны в:\n{path}')
        else:
            with open(path, 'w', encoding='utf-8') as file:
                json.dump({'Loggins & passwords':[]}, file,
                    ensure_ascii=False, indent=3)
            print(f'\nФайл отсутствует. Создан файл:\n{path}')
            wrap(path)
    return wrap


@path_finder
def write_new_pass(save_path:str) -> None: #, data:dict) -> None:
    """
    Запись данных в json
    :param save_path (str): Путь до файла хранения данных
    # :param data (dict): данные под запись
    """
    uid = {i:input(f'Введите ваш {i}: ') for i in \
                    dict(service='', login='', password='')} # user input data (uid)
    with open(save_path, 'r+', encoding='utf-8') as file:
        js_data = json.load(file)
    if uid['service'] in \
        [name_serv['service'] for name_serv in js_data['Loggins & passwords']]:
        print(f"{uid['service']} уже записан в файл. Выберете другое имя сервиса...")
        write_new_pass(save_path)
    else:
        js_data['Loggins & passwords'].append(uid)
        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(js_data, f, ensure_ascii=False, indent=3)
