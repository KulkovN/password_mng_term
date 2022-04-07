import sys
from prettytable import PrettyTable
from pathlib import Path

sys.path.append(Path.joinpath(Path.cwd(), '')) 
import crud.reader as cr
import crud.deleter as cd
import crud.updater as cu
from utils.texts import TASKS


def show_all(data:dict) -> None:
    """
    Дает вывод всех значений ключа 'service'
    для более удобной навигации во время выборки 
    под поиск, удаление и изменения данных
    """
    table = PrettyTable()
    table.field_names = ['№','Сервисы']
    lst_services  = [j['service'] for j in data['Loggins & passwords']]
    counter = 1
    for i in lst_services:
        table.add_row([counter ,i])
        counter += 1
    print(table)
    

def checkin(us_inp:str, data:dict) -> bool:
    """
    Проверка ввода и сопостовление по ключу
    :param us_inp: пользовательский ввод (когда вводит сервис)
    :param data: словарь корневого файла, где лежат все пассы
    :return bool в зависимости от результата проверки 
    """
    return True if us_inp in (i["service"] for i \
        in data["Loggins & passwords"]) else False


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
            if flag in TASKS[3:7]:
                cr.data_printer(_dict)
                break
            elif flag in TASKS[7:11]:
                cu.write_change(args[0], args[1], args[3])
                break
            else:
                cd.deleter_(args[0], args[1], args[3])
                break
