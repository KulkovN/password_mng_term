from calendar import c
from genericpath import exists
import re
import json
import configparser
from pathlib import Path, PurePosixPath
from utils._crypt import _hash
from utils.texts import AFTER_CONF_CREATION
# from _crypt import _hash
# from texts import AFTER_CONF_CREATION


def configur(profile:str) -> tuple:
    """ 
    Создание конфига с путем для сохранения
    :param: profile: профиль под парсинг
    :return: float с путем и паролем для расшифровки 
    """
    config = configparser.ConfigParser()
    path_for_cnfg = Path(f'{Path.home()}/.py_pass')
    path_to_confrFile = f'{path_for_cnfg}/config.ini'
    raw_profile_path = Path(f'{Path.home()}/.py_pass/profiles/{profile}')

    if not Path(path_for_cnfg).exists():
        path_for_cnfg.mkdir(parents=True) # https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir
        paswd = input('Пароль профиля: ')
        raw_profile_path.mkdir(parents=True)
        config.add_section(f'Config_{profile}')
        config.set(f'Config_{profile}', f'Profile_{profile}_file', f'{raw_profile_path}/slp.json.aes') # для шифрования
        config.set(f'Config_{profile}', f'Profile_{profile}_master_pwd', _hash(paswd))
        # добавление секции профилей
        config.add_section(f'Profile:{profile}')
        config.set(f'Profile:{profile}', f'{profile}', profile)
        # запись конфига
        with open(path_to_confrFile, 'a') as file:
            config.write(file)
        print(AFTER_CONF_CREATION)
    config.read(path_to_confrFile)
    pts, check_pswd, profile = \
        config.get(f'Config_{profile}', f'Profile_{profile}_file'), config.get(f'Config_{profile}',
        f'Profile_{profile}_master_pwd'), config.get(f'Profile:{profile}', profile)
    # js_run(pts, check_pswd, profile)
    js_run(pts)
    return pts, check_pswd, profile

# def new_profile(config_:str):
#     pass


def js_run(path_js:str) -> None:
    """ Проверка json наличие / отсутствие
    :param profile: ссылка на вызываемый профиль конкретного пользователя
    :param path_js: строка пути с учетом крипты
    :param paswd: пароль из конфига
    """
    path = path_js.split(PurePosixPath(path_js).suffix)[0]
    if not Path(path).exists(): # .json
        if not Path(path_js).exists(): # .aes
            with open(path, 'w') as jf:
                json.dump({'Loggins & passwords':[]}, jf)
            print(f'профиль создан по пути {path}')
        else:
            return True


if __name__ == "__main__":
    configur('test')
