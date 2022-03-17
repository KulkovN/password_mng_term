#!/usr/bin/env python3
import sys
from config.cr_pathes import confy
from change_delete_read.changer import changer_js
from change_delete_read.finder_deleter import runner_to_find
from read_write.for_write import write_new_pass
from config.texts import HI, BYE, PREWIEW, TASKS, TASKS_EXIT, MES_S


def main(counter_attempts_to_run:int) -> None:
    """
    Превью и запуск работы
    :param counter_attempts_to_run: счетчик попыток запуска
    """
    PTS = confy()
    if PTS:
        if counter_attempts_to_run <= 3:
            print(f"{HI}\n{MES_S['attempts']}")
            condition = input(MES_S['what_u_do'])
            if condition.lower() in TASKS[0:2]:
                runner_to_find(PTS, condition.lower())
            elif condition.lower() in TASKS[2:4]:
                changer_js(PTS)
            elif condition.lower() in TASKS[4:6]:
                runner_to_find(PTS, condition.lower())
            elif condition.lower() in TASKS[6:]:
                uid = {i:input(f'Введите ваш {i}: ') for i in \
                    dict(service='', login='', password='')} # user input data (uid)
                write_new_pass(PTS, uid)
            elif condition.lower() in TASKS_EXIT:
                print(PREWIEW.renderText(MES_S['bye']))
                sys.exit(1)
            else:
                counter_attempts_to_run += 1
                main(counter_attempts_to_run)
        else:
            print(f"{MES_S['zero_att']}\n{BYE}")
    else:
        print('Exception')


if __name__ == "__main__":
    counter_attempts_to_run = 1
    main(counter_attempts_to_run)
