import json
import os
from pickle import DICT
import sys
sys.path.append(os.path.join(os.getcwd(), ''))
from const import PATH_TO_FILE # дирректория для записи файла
from all_keys_srvices.show_all_serv import show_all, checkin

def deleter(data, name_service):
    """удалит выбранный сервис

    :param _dict_ data: словарь из json
    :param _str_ name_service: пользовательский ввод -
    этот сервис будет удален
    """
    try:
        for _dict in data['Loggins & passwords']:
            if _dict['service'] == name_service:
                data['Loggins & passwords'].remove(_dict)
                #   запись в файл
                with open (PATH_TO_FILE, 'w') as file:
                    json.dump(data, file, \
                        ensure_ascii=False, indent=4)
                    print(f'{name_service} - удален')
    except Exception as ex:
        print(ex)


def data_printer(_data):
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


def runner_to_find(flag):
    """Для поиска нужного словаря в файле

    Args:
        flag (str): если поиск - то просто распечатает
            если удаление - передаст в deleter для удаление
    """
    counter = 1
    with open(PATH_TO_FILE, 'r') as file:
        data = json.load(file)
        show_all(data)
        name_service = input('\nНапишите имя сервиса: ')
        if not checkin(name_service, data):
            print('Выбранный сервис не записан. Попробуйте еще раз...')
            runner_to_find(flag='find')
        for _dict in data['Loggins & passwords']:
            print(f"{counter}) {_dict['service']}")
            if name_service == _dict['service']:
                if flag in ['find', 'найти']:
                     data_printer(_dict)
                     break
                else:
                    deleter(data, name_service)

if __name__ == "__main__":
    runner_to_find('find')
