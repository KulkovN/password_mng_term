#!/usr/bin/env python3
import stdiomask
from pathlib import Path, PurePosixPath
from utils.cr_pathes import configur
from crud.reader import runner_to_find
from crud.creater import write_new_pass
from utils._crypt import crypt ,check_pwd
from utils.texts import HI, BYE, TASKS, TASKS_EXIT, MES_S


def main(counter:int) -> None:
    """
    запуск работы
    :param counter: счетчик попыток запуска
    """
    PTS = configur()
    path_to_json = PTS[0].split(PurePosixPath(PTS[0]).suffix)[0]
    print(HI)
    while True:
        if counter > 0:
            paswd = stdiomask.getpass(prompt=f'У вас есть {counter}\
попытки для ввода мастер пароля и режима\nВведите мастер-пароль: ')
            user_check = check_pwd(PTS[1] ,paswd)
            if user_check:
                if Path(PTS[0]).exists():
                    crypt(PTS[0], paswd, ' ')
                condition = input(MES_S['what_u_do'])
                if condition.lower() in TASKS[0:3]:
                    write_new_pass(path_to_json)
                elif condition.lower() in TASKS[3:]:
                    runner_to_find(path_to_json, condition.lower())
                elif condition.lower() in TASKS_EXIT:
                    counter = 0
                    print(BYE)
                crypt(path_to_json, paswd, 'crypt')
                break
            elif not user_check or counter >= 1:
                counter -= 1
            else:
                break
        else:
            print(f'Попытки исчерпаны...\n{BYE}')
            break


if __name__ == "__main__":
    counter_attempts_to_run = 3
    main(counter_attempts_to_run)
    