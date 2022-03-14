#!/usr/bin/env python3
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
        print(prewiew_text.renderText('PyPassMng'))
        print(f'\n\nУ вас есть 3 попытки для ввода действия. Сейчас {counter_attempts_to_run}')
        condition = input('\nЧто вы хотите сделать\nнайти, изменить, \
удалит, создать (можно на анг.яз.): ')
        cond = ['найти', 
                'find', 
                'изменить', 
                'change', 
                'удалить', 
                'delete',
                'создать',
                'create']
        if condition.lower() in cond[0:2]:
            show_all()
            runner_to_find(condition.lower())
        elif condition.lower() in cond[2:4]:
            changer_js(PATH_TO_FILE, ex_params())
        elif condition.lower() in cond[4:6]:
            runner_to_find(condition.lower())
        elif condition.lower() in cond[6:]:
            write_new_pass(checExist(),\
                createn_data_struct(new_inputer_datas()))
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
