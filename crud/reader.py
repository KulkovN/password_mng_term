import json
from pathlib import Path
import sys
import readline
from prettytable import PrettyTable

sys.path.append(Path.joinpath(Path.cwd(), ''))
from all_keys_srvices.spec_for_crud import show_all, checkin, triger_flags
from utils.compliter import MyCompleter


def data_printer(_data:dict) -> None:
    """Вывод значений словаря с данными, 
    когда пользватель просто ищет нужный пароль
    Args:
        _data (dict): словарь данных, который был 
        найден по совпадению значения сервиса внутри файла
    """
    table = PrettyTable()
    table.field_names = ["Сервис", "Логин", "Пароль"]
    table.add_row([i for i in _data.values()])
    print(table)


def runner_to_find(path:str, flag:str) -> float:
    """Для поиска нужного словаря в файле
    Args:
        flag (str): если поиск - то просто распечатает
            если удаление - передаст в deleter для удаление
    """
    with open(path, 'r') as file:
        data = json.load(file)
        show_all(data)
        # compliter тут
        completer = MyCompleter([i['service'] for i in data['Loggins & passwords']])
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')
        name_service = input('\nВведите искомый сервис для ваших целей: ')
        while not checkin(name_service, data):
            name_service = input('Выбранный сервис не записан. Попробуйте еще раз...')
        triger_flags(data, name_service, flag, path)
        