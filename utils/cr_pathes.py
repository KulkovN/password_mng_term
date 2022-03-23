import configparser 
import json
from pathlib import Path
from crypt import crypt


def confy() -> None:
    """ 
    Создание конфига с путем для сохранения
    """
    config = configparser.ConfigParser()
    # path_for_cnfg = Path(f'{Path.home()}/.py_pass_conf/pathes')
    path_for_cnfg = Path(f'{Path.home()}/Desktop/pathes')
    path_to_confrFile = f'{path_for_cnfg}/pathes.ini'
    try:
        if not Path(path_for_cnfg).exists():
            path_for_cnfg.mkdir(parents=True) # https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir
            # 
            paswd = input('Придумайте мастер-пароль для доступа к данным: ')
            #
            path = f'{input("Введите путь для записи файла с данными: ")}'
            # path = f'{path}/.allpwd.json'
            path = f'{path}/test.json'
            config.add_section('SavePath')
            # config.set('SavePath', 'Path', path)
            config.set('SavePath', 'Path', f'{path}.csp') # для шифрования
            config.set('SavePath', 'MasterPaswd', paswd)
            # запись конфига
            with open(path_to_confrFile, 'w') as file:
                config.write(file)
            # создание json
            with open(path, 'w') as jf:
                json.dump({'Loggins & passwords':[]}, jf)
            print(f'Новый файл создан по пути {path}')
            # 
            flag = 'crypt'
            crypt(path, paswd, flag)
            #
        config.read(path_to_confrFile)
        pts, check_pswd = config.get('SavePath', 'Path'),\
            config.get('SavePath', 'MasterPaswd')
            #
        paswd = input('Введите мастер-пароль: ')
        if paswd == check_pswd:
            flag = 'uncrypt'
            crypt(pts, paswd, flag)
        else:
            print('Не верный мастер-пароль...')
            confy()
        #
        return str(pts), check_pswd
        # else:
        #     config.read(path_to_confrFile)
        #     # config_file = config.get('ConfigPath', 'Path')
        #     pts = config.get('SavePath', 'Path')
        #     return str(pts)
    except FileNotFoundError:
        confy(input(f'Напишите корректный путь (полный): '))


if __name__ == "__main__":
    print(confy())
    