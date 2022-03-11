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
            if _dict['service'] == name_service \
                and flag in ['find', 'найти']:
                        print(_dict)
            else:
                deleter(data, name_service)
