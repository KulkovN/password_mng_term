import configparser 
import json
from pathlib import Path


def confy() -> None:
    """ Создание конфига с путем для сохранения """
    config = configparser.ConfigParser()
    path_for_cnfg = f'{Path.cwd()}/pathes.ini'
    try:
        if not Path(path_for_cnfg).exists():
            path = input('Введите путь для записи файла с данными: ')
            path = f'{path}/test.json'
            config.add_section('SavePath')
            config.set('SavePath', 'Path', path)
            # запись конфига
            with open(path_for_cnfg, 'w') as file:
                config.write(file)
            # создание json
            with open(path, 'w') as jf:
                json.dump({'Loggins & passwords':[]}, jf)
            print(f'Новый файл создан по пути {path}')
        else:
            config.read(path_for_cnfg)
            PTS = config.get('SavePath', 'Path')
            return str(PTS)
    except FileNotFoundError:
        confy(input(f'Напишите корректный путь (полный): '))
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    confy()

# str(Path.cwd().parent)



# PATH = '/Users/kulkovni/Desktop/.allpwd.json'

