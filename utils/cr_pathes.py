import configparser 
import json
from pathlib import Path


def confy() -> None:
    """ 
    Создание конфига с путем для сохранения
    """
    config = configparser.ConfigParser()
    path_for_cnfg = Path(f'{Path.home()}/py_pass_conf/pathes')
    path_to_confrFile = f'{path_for_cnfg}/pathes.ini'
    try:
        if not Path(path_for_cnfg).exists():
            path_for_cnfg.mkdir(parents=True) # https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir
            path = f'{input("Введите путь для записи файла с данными: ")}'
            path = f'{path}/.allpwd.json'
            config.add_section('SavePath')
            config.set('SavePath', 'Path', path)
            # запись конфига
            with open(path_to_confrFile, 'w') as file:
                config.write(file)
            # создание json
            with open(path, 'w') as jf:
                json.dump({'Loggins & passwords':[]}, jf)
            print(f'Новый файл создан по пути {path}')
            config.read(path_to_confrFile)
            pts = config.get('SavePath', 'Path')
            return str(pts)
        else:
            config.read(path_to_confrFile)
            # config_file = config.get('ConfigPath', 'Path')
            pts = config.get('SavePath', 'Path')
            return str(pts)
    except FileNotFoundError:
        confy(input(f'Напишите корректный путь (полный): '))


if __name__ == "__main__":
    print(confy())
