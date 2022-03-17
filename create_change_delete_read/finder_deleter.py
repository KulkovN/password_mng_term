import json
import os
import sys
sys.path.append(os.path.join(os.getcwd(), ''))
from all_keys_srvices.show_all_serv import show_all, checkin

def deleter(path:str, data:dict, name_service:str) -> None:
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
    print('\nВаши данные по запросу:\n')
    lst = ['Сервис: ', 'Логин: ', 'Пароль: ']
    counter = 0
    for i in _data.values():
        print(f'{lst[counter]}{i}')
        counter += 1


def runner_to_find(path:str, flag:str) -> None:
    """Для поиска нужного словаря в файле

    Args:
        flag (str): если поиск - то просто распечатает
            если удаление - передаст в deleter для удаление
    """
    with open(path, 'r') as file:
        data = json.load(file)
        show_all(data)
        name_service = input('\nНапишите имя сервиса: ')
        if not checkin(name_service, data):
            print('Выбранный сервис не записан. Попробуйте еще раз...')
            runner_to_find(flag='find')
        for _dict in data['Loggins & passwords']:
            if name_service == _dict['service']:
                if flag in ['find', 'найти']:
                     data_printer(_dict)
                     break
                else:
                    deleter(path, data, name_service)

if __name__ == "__main__":
    runner_to_find('find')
