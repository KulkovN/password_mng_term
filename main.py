#!/usr/bin/env python3
import sys
from pathlib import Path, PurePosixPath
from utils.cr_pathes import configur
from create_change_delete_read.finder_deleter import runner_to_find
from create_change_delete_read.creater import write_new_pass
from utils.crypt import crypt
from utils.texts import HI, BYE, TASKS, TASKS_EXIT, MES_S


def main(counter_attempts_to_run:int) -> None:
    """
    запуск работы
    :param counter_attempts_to_run: счетчик попыток запуска
    """
    PTS = configur() # return type is `float`
    path_to_json = PTS[0].split(PurePosixPath(PTS[0]).suffix)[0]
    paswd = input(f"{HI}\n{MES_S['attempts']}. Для старта введите мастер-пароль: ")
    if counter_attempts_to_run >= 1 and paswd == PTS[1]:
        if Path(PTS[0]).exists():
            crypt(PTS[0], paswd, ' ')
        condition = input(MES_S['what_u_do'])
        if condition.lower() in TASKS[:6]:
            runner_to_find(path_to_json, condition.lower())
        elif condition.lower() in TASKS[6:]:
            write_new_pass(path_to_json)
        elif condition.lower() in TASKS_EXIT:
            print(BYE)
            sys.exit(1)
        else:
            counter_attempts_to_run -= 1
            print(f'Осталось ({counter_attempts_to_run}) попыток')
            main(counter_attempts_to_run)
        crypt(path_to_json, paswd, 'crypt')
    else:
        print(f"{MES_S['zero_att']}\n{BYE}")



if __name__ == "__main__":
    counter_attempts_to_run = 3
    main(counter_attempts_to_run)
    