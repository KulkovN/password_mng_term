import json
import os
import sys
import readline
from prettytable import PrettyTable

from create_change_delete_read.changer import write_change
sys.path.append(os.path.join(os.getcwd(), ''))
from all_keys_srvices.show_all_serv import show_all, checkin
from utils.compliter import MyCompleter


def deleter(data:dict, name_service:str, path:str) -> None:
    """удалит выбранный сервис
    :param path : путь до файла json
    :param _dict_ data: словарь из json
    :param _str_ name_service: пользовательский ввод -
    этот сервис будет удален
    """
    try:
        for _dict in data['Loggins & passwords']:
            if _dict['service'] == name_service:
                data['Loggins & passwords'].remove(_dict)
                #   запись в файл
                with open (path, 'w') as file:
                    json.dump(data, file, \
                        ensure_ascii=False, indent=4)
                    print(f'{name_service} - удален')
    except Exception as ex:
        print(ex)


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
        if not checkin(name_service, data):
            print('Выбранный сервис не записан. Попробуйте еще раз...')
            # runner_to_find(flag='find')
            runner_to_find(flag)
        else:
            triger_flags(data, name_service, flag, path)


def triger_flags(*args) -> None:
    """
    Функция филтрации флага, после ввода сервиса
    :para: args - кортеж из:
        - data,
        - name_service, 
        - flag,
        - path 
    полученные из runner_to_find
    """
    flag = args[2]
    for _dict in args[0]['Loggins & passwords']:
        if args[1] == _dict['service']:
            if flag in ['find', 'найти']:
                data_printer(_dict)
                break
            elif flag in ['change', 'изменить']:
                write_change(args[0], args[1], args[3])
                break
            else:
                deleter(args[0], args[1], args[3])
                break

if __name__ == "__main__":
    pass
    print(type(runner_to_find('/Users/kulkovni/Desktop/.allpwd.json', 'find')))

