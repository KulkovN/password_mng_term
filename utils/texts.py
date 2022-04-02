from pyfiglet import Figlet

PREWIEW = Figlet(font='slant')
HI = PREWIEW.renderText('PassMng')
BYE = PREWIEW.renderText('bye bye')

TASKS = ['создать','create', 'c',  # [0:3]
        'найти', 'find', 'f', 'r', # [3:7]
        'изменить', 'change', 'ch', 'u', # [7:11]
        'удалить', 'delete', 'd'] #[11:]
TASKS_EXIT = ['q', 'й', 'exit', 'выход']
VARABLES = ['service', 'login', 'password']

MES_S = {'attempts' : "\nУ вас есть 3 попытки для ввода режима.""", 
    'what_u_do':"\nВведите режим \n(найти, изменить, удалит, создать (можно на анг.яз.))\
        \n('c','r','u','d' - тоже будет работать)\nДля выхода - q: ",
    'zero_att' : "\nПопытки исчерпаны. Попробуйте перезапустить приложение и ввести требуемое действие "}
