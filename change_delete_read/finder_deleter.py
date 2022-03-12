import json
from pathlib import Path

PATH_TO_FILE = f'{Path.home()}/Desktop/.allpwd.json'

def deleter(data, name_service):
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
    когда пользвоатель просто ищет нужный пароль

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
    name_service = input('Напишите имя сервиса: ')
    with open(PATH_TO_FILE, 'r') as file:
        data = json.load(file)
        for _dict in data['Loggins & passwords']:
            if _dict['service'] == name_service:
                if flag in ['find', 'найти']:
                    # print(_dict)
                     data_printer(_dict)
                else:
                    deleter(data, name_service)

if __name__ == "__main__":
    runner_to_find('find')
