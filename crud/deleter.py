import json


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
                #   запись в файл
                with open (path, 'w') as file:
                    json.dump(data, file, \
                        ensure_ascii=False, indent=4)
                    print(f'{name_service} - удален')
    except Exception as ex:
        print(ex)