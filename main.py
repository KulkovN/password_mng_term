#!/usr/bin/env python3
import stdiomask
import readline
from pathlib import Path, PurePosixPath
from utils.cr_pathes import configur
from crud.reader import runner_to_find
from crud.creater import write_new_pass
# from utils._crypt import crypt ,check_pwd
from utils.compliter import MyCompleter
from utils.texts import HI, BYE, TASKS, TASKS_EXIT, MES_S


def main(counter:int) -> None:
    """
    запуск работы
    :param counter: счетчик попыток запуска
    """

    PTS = configur()
    path_to_json = PTS[0].split(PurePosixPath(PTS[0]).suffix)[0]
    print(HI)
    try:
        # комплитер на список режимов
        completer = MyCompleter(TASKS)
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')
        if Path(PTS[0]).exists():
            condition = input(MES_S['what_u_do']).strip()
            while counter > 0 :
                if condition.lower() not in TASKS and condition.lower() not in TASKS_EXIT:
                    counter -= 1
                    condition = input('У программы нет такого режима работы. Введите режим: ')
                else:
                    break
            if condition.lower() in TASKS[0:3]:
                write_new_pass(path_to_json)
            elif condition.lower() in TASKS[3:]:
                runner_to_find(path_to_json, condition.lower())
            elif condition.lower() in TASKS_EXIT:
                counter = 0
                print(BYE)
    except Exception as ex:
        print (f'Ошибка: {ex}')
        


if __name__ == "__main__":
    counter_attempts_to_run = 3
    main(counter_attempts_to_run)
    