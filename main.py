#!/usr/bin/env python3
import sys
from utils.cr_pathes import confy
from create_change_delete_read.finder_deleter import runner_to_find
from create_change_delete_read.creater import write_new_pass
from utils.texts import HI, BYE, TASKS, TASKS_EXIT, MES_S


def main(counter_attempts_to_run:int) -> None:
    """
    запуск работы
    :param counter_attempts_to_run: счетчик попыток запуска
    """
    PTS = confy()
    if PTS:
        if counter_attempts_to_run >= 1:
            print(f"{HI}\n{MES_S['attempts']}")
            condition = input(MES_S['what_u_do'])
            if condition.lower() in TASKS[:6]:
                runner_to_find(PTS, condition.lower())
            elif condition.lower() in TASKS[6:]:
                write_new_pass(PTS)
            elif condition.lower() in TASKS_EXIT:
                print(BYE)
                sys.exit(1)
            else:
                counter_attempts_to_run -= 1
                print(f'Осталось ({counter_attempts_to_run}) попыток')
                main(counter_attempts_to_run)
        else:
            print(f"{MES_S['zero_att']}\n{BYE}")
    else:
        print('Exception - PTS is False !!!')


if __name__ == "__main__":
    counter_attempts_to_run = 3
    main(counter_attempts_to_run)
