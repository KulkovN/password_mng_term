from calendar import c
import re
import json
import configparser
from pathlib import Path, PurePosixPath
from _crypt import _hash
from texts import AFTER_CONF_CREATION



def configur(profile:str) -> float:
    """ 
    Создание конфига с путем для сохранения
    :return: float с путем и паролем для расшифровки 
    """
    config = configparser.ConfigParser()
    path_for_cnfg = Path(f'{Path.home()}/.py_pass/config')
    path_to_confrFile = f'{path_for_cnfg}/config.ini'
    # profile = input('Введите профиль пользователя: ')
    if not Path(path_for_cnfg).exists():
        path_for_cnfg.mkdir(parents=True) # https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir
        paswd = input('Придумайте мастер-пароль для доступа к данным: ')
        raw_profile_path = Path(f'{Path.home()}/.py_pass/profiles/{profile}/')
        raw_profile_path.mkdir(parents=True)
        # path = js_path_cre(input("Введите путь для записи файла с данными: "))
        config.add_section('Config')
        # config.set('Config', 'Path', f'{path}.aes') # для шифрования
        config.set('Config', f'{profile}_path_file', f'{raw_profile_path}_pwds.json.aes') # для шифрования
        config.set('Config', f'{profile}_master_password', _hash(paswd))
        # добавление секции профилей
        config.add_section('Profiles')
        config.set('Profiles', f'{profile}', profile)
        # запись конфига
        with open(path_to_confrFile, 'w') as file:
            config.write(file)
        print(AFTER_CONF_CREATION)
    config.read(path_to_confrFile)
    pts, check_pswd, profile = \
        config.get('Config', f'{profile}_path_file'), config.get('Config', f'{profile}_master_password')\
            , config.get('Profiles', profile)
    # js_run(pts, check_pswd, profile)
    js_run(pts)
    return pts, check_pswd, profile

    
def js_run(path_js:str) -> None:
    """ Проверка json наличие / отсутствие
    :param profile: ссылка на вызываемый профиль конкретного пользователя
    :param path_js: строка пути с учетом крипты
    :param paswd: пароль из конфига
    """
    path = path_js.split(PurePosixPath(path_js).suffix)[0]
    print(path)
    if not Path(path).exists(): # .json
        if not Path(path_js).exists(): # .aes
            with open(path, 'w') as jf:
                json.dump({'Loggins & passwords':[]}, jf)
            print(f'профиль создан по пути {path}')
        else:
            return True


if __name__ == '__main__':
    cnf = configur()
