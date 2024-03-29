#!/usr/bin/env python3
import sys
import stdiomask
import readline
from pathlib import Path, PurePosixPath
from utils.cr_pathes import configur
from crud.reader import runner_to_find
from crud.creater import write_new_pass
from utils._crypt import crypt, check_pwd
from utils.compliter import MyCompleter
from utils.texts import HI, BYE, TASKS, TASKS_EXIT, MES_S


def main(counter:int) -> None:
    """
    запуск работы
    :param counter: счетчик попыток запуска
    """
    print(HI)
    profile = input('Введите ПРОФИЛЬ пользователя: ')
    PTS = configur(profile)
    path_to_json = PTS[0].split(PurePosixPath(PTS[0]).suffix)[0]
    while True:
        paswd = stdiomask.getpass(prompt=f'{counter} попытки для ввода мастер-пароля: ')
        user_check = check_pwd(PTS[1] ,paswd)
        if counter != 1:
            try:
                if user_check:
                    # комплитер на список режимов
                    completer = MyCompleter(TASKS)
                    readline.set_completer(completer.complete)
                    readline.parse_and_bind('tab: complete')
                    if Path(PTS[0]).exists() or Path(path_to_json).exists():
                        if not Path(path_to_json).exists():
                            crypt(PTS[0], paswd, ' ')
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
                    crypt(path_to_json, paswd, 'crypt')
                    break
                elif not user_check: # or counter >= 1:
                    counter -= 1
                else:
                    break
            except Exception as ex:
                print (f'Ошибка: {ex}')
                crypt(path_to_json, paswd, 'crypt')
        else:
            print(f'Попытки исчерпаны...\n{BYE}')
            break


if __name__ == "__main__":
    main(3)
    