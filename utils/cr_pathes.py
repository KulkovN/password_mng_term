from calendar import c
from genericpath import exists
import re
import json
import configparser
from pathlib import Path, PurePosixPath
from utils._crypt import _hash
from utils.texts import AFTER_CONF_CREATION


def configur(profile:str) -> tuple:
    """ 
    Создание конфига с путем для сохранения
    :param: profile: профиль под парсинг
    :return: float с путем и паролем для расшифровки 
    """
    config = configparser.ConfigParser()
    raw_profile_path = Path(f'{Path.home()}/.py_pass/profiles/{profile}')
    path_to_confrFile = f'{raw_profile_path}/config.ini'
    if not Path(raw_profile_path).exists():
        print('Такой профиль не зарегистрирован, поэтому будет создан как новый.')
        raw_profile_path.mkdir(parents=True)
        paswd = input('Введите мастер - пароль для профиля: ') 
        config.add_section(f'Config')
        config.set(f'Config', f'Profile_{profile}_file', f'{raw_profile_path}/slp.json.aes') # для шифрования
        config.set(f'Config', f'Profile_{profile}_master_pwd', _hash(paswd))
        # запись конфига
        with open(path_to_confrFile, 'a') as file:
            config.write(file)
        print(AFTER_CONF_CREATION)
    config.read(path_to_confrFile)
    pts, check_pswd =\
        config.get(f'Config', f'Profile_{profile}_file'), config.get('Config', f'Profile_{profile}_master_pwd')
    js_run(pts)
    return pts, check_pswd


def js_run(path_js:str) -> None:
    """ Проверка json наличие / отсутствие
    :param path_js: строка пути с учетом крипты
    """
    path = path_js.split(PurePosixPath(path_js).suffix)[0]
    if not Path(path).exists(): # .json
        if not Path(path_js).exists(): # .aes
            with open(path, 'w') as jf:
                json.dump({'Loggins & passwords':[]}, jf)
            # print(f'профиль создан по пути {path}')
        else:
            return True


if __name__ == "__main__":
    configur('test')
