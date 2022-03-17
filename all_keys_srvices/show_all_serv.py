from prettytable import PrettyTable


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


if __name__ == "__main__":
    d = {"Loggins & passwords": 
            [
                {"service": "google",
                "login": "kulkovnik93@gmail.com",
                "password": "3571827_Nike"}, 
                {"service": "google",
                "login": "kulkovnik93@gmail.com",
                "password": "3571827_Nike"}
            ]
        }
    show_all(d)