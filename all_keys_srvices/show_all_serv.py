import os
import sys
sys.path.append(os.path.join(os.getcwd(), ''))
import json
from const import PATH_TO_FILE # константа пути для файла


def show_all(data):
    """
    Дает вывод всех значений ключа 'service'
    для более удобной навигации во время выборки 
    под поиск, удаление и изменения данных
    """
    print("Ваши сервисы:\n")
    counter = 1
    for i in data['Loggins & passwords']:
        print(f"{counter}) {i['service']}")
        counter+=1
    

def checkin(us_inp, data):
    """
    Проверка ввода и сопостовление по ключу
    проверяет наличие сервисов по ключу
    т.е. сравнивает ввод пользователя и сохраненные значения
    ключей внутри словара файла

    :param _str_ us_inp: пользовательский ввод (когда вводит сервис)
    :param _dict_ data: словарь корневого файла, где лежат все пассы
    :return _bool_: в зависимости от результата проверки 
    """
    return True if us_inp in (i["service"] for i \
        in data["Loggins & passwords"]) else False
