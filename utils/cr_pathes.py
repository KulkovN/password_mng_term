import json
import configparser
from pathlib import Path, PurePosixPath
from utils._crypt import _hash

def configur() -> float:
    """ 
    Создание конфига с путем для сохранения
    """
    config = configparser.ConfigParser()
    # path_for_cnfg = Path(f'{Path.home()}/.py_pass_conf/config')
    path_for_cnfg = Path(f'{Path.home()}/.py_pass/config')
    path_to_confrFile = f'{path_for_cnfg}/config.ini'
    try:
        if not Path(path_for_cnfg).exists():
            path_for_cnfg.mkdir(parents=True) # https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir
            paswd = input('Придумайте мастер-пароль для доступа к данным: ')
            path = f'{input("Введите путь для записи файла с данными: ")}'
            path = f'{path}/.all_pwd.json'
            config.add_section('Config')
            config.set('Config', 'Path', f'{path}.aes') # для шифрования
            config.set('Config', 'MasterPaswd', \
                _hash(paswd))
            # запись конфига
            with open(path_to_confrFile, 'w') as file:
                config.write(file)
        config.read(path_to_confrFile)
        pts, check_pswd = \
            config.get('Config', 'Path'), config.get('Config', 'MasterPaswd')
        js_run(pts, check_pswd)
        return pts, check_pswd
    except FileNotFoundError:
        configur(input(f'Напишите корректный путь (полный): '))


def js_run(path_js:str, paswd:str) -> None:
    """ Проверка json наличие / отсутствие
    + закриптует после создания

    :param path_js: строка пути с учетом крипты
    :param paswd: пароль из конфига
    """
    path = path_js.split(PurePosixPath(path_js).suffix)[0]
    if not Path(path).exists(): # .json
        if not Path(path_js).exists(): # .aes
            with open(path, 'w') as jf:
                json.dump({'Loggins & passwords':[]}, jf)
            print(f'Новый файл создан по пути {path}')
        else:
            return True

if __name__ == '__main__':
    print(configur())