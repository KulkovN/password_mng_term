import configparser 
import json
from pathlib import Path


def confy(path):
    """
    Создание конфига с путем для сохранения
    :param path: путь для сохранения json-файла
    """
    # path=f'{Path.home()}/Desktop/test.json'
    config = configparser.ConfigParser()
    path_for_cnfg = Path.cwd().parent
    if not Path(path_for_cnfg).exists:
        config.add_section('SavePath')\
            .set('SavePath', 'Path', path)
        # запись конфига
        with open(f'{path_for_cnfg}/config.ini', 'w') as file:
            config.write(file)
        # создание json
        with open(f'{path}/.allupwd.json', 'w') as jfile:
            json.dump({'Loggins & passwords':[]}, jfile)
        print(f'Новый файл создан по пути {path}')
    else:
        config.read(path_for_cnfg)
        pts = config.get('SavePath', 'Path')
        print(pts)


if __name__ == "__main__":
    path = input('Введите путь где будут хранится данные: ')
    confy(path)

# str(Path.cwd().parent)



# PATH = '/Users/kulkovni/Desktop/.allpwd.json'

