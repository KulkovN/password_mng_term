#!/usr/bin/env python3
import os
import sys 
from pyfiglet import Figlet
from change_delete_read.changer import *
from change_delete_read.finder_deleter import *
from read_write.for_write import *
from all_keys_srvices.show_all_serv import show_all


def main(counter_attempts_to_run):
    """
    Превью и запуск по запись условий работы

    Args:
        type (int) : counter_attempts_to_run: счетчик попыток запуска

    """
    prewiew_text = Figlet(font='slant')
    if counter_attempts_to_run <= 3:
        hellower = prewiew_text.renderText('PyPassMng')
        good_bye = prewiew_text.renderText('Bye bye') 
        print(f'{hellower}')
        print(f'\n\nУ вас есть 3 попытки для ввода действия. Сейчас {counter_attempts_to_run}')
        condition = input('\nЧто вы хотите сделать\nнайти, изменить, \
удалит, создать (можно на анг.яз.)\nДля выхода - q: ')
        cond = ['найти', 'find', 'изменить', 
                'change', 'удалить', 'delete',
                'создать','create']
        if condition.lower() in cond[0:2]:
            runner_to_find(condition.lower())
        elif condition.lower() in cond[2:4]:
            # show_all()
            # changer_js(ex_params(PATH_TO_FILE))
            changer_js(PATH_TO_FILE)
        elif condition.lower() in cond[4:6]:
            runner_to_find(condition.lower())
        elif condition.lower() in cond[6:]:
            write_new_pass(checExist(),\
                createn_data_struct(new_inputer_datas()))
        elif condition.lower() in ['q', 'й', 'exit', 'выход']:
            print(f'{good_bye}')
            sys.exit(1)
        else:
            counter_attempts_to_run += 1
            main(counter_attempts_to_run)
    else:
        print('\nПопытки исчерпаны. \
Попробуйте перезапустить приложение и ввести требуемое действие ')
        print(prewiew_text.renderText('Good bye'))

if __name__ == "__main__":
    counter_attempts_to_run = 1
    main(counter_attempts_to_run)
