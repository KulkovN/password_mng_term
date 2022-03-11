from pyfiglet import Figlet
from change_delete_read.changer import *
from change_delete_read.finder_deleter import *
from read_write.for_write import *


def main():
    """
    Превью и запуск по запись условий работы
    """
    prewiew_text = Figlet(font='slant')
    print(prewiew_text.renderText('PyPassMng'))
    condition = input('Что вы хотите сделать\nнайти, изменить, \
удалит (можно на анг.яз.): ')
    cond = [
            'найти', 
            'find', 
            'изменить', 
            'change', 
            'удалить', 
            'delete',
            'создать',
            'create']
    if condition.lower() in cond[0:2]:
        runner_to_find(condition.lower())
    elif condition.lower() in cond[2:4]:
        changer_js(PATH_TO_FILE, ex_params())
    elif condition.lower() in cond[4:6]:
        runner_to_find(condition.lower())
    elif condition.lower() in cond[6:]:
        write_new_pass(checExist(),\
            createn_data_struct(new_inputer_datas()))
    else:
        main()

if __name__ == "__main__":
    main()
