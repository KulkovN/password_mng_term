from pyfiglet import Figlet

PREWIEW = Figlet(font='slant')
HI = PREWIEW.renderText('PassMng')
BYE = PREWIEW.renderText('bye bye')

TASKS = ['создать','create', 'c',  # [0:3]
        'найти', 'find', 'f', 'r', # [3:7]
        'изменить', 'change', 'ch', 'update', 'u', # [7:12]
        'удалить', 'delete', 'd'] #[12:]
TASKS_EXIT = ['q', 'й', 'exit', 'выход']
VARABLES = ['service', 'login', 'password']

MES_S = {'attempts' : "\nУ вас есть 3 попытки для ввода режима.""", 
    'what_u_do':"\nВведите режим: ",
    'zero_att' : "\nПопытки исчерпаны.\nПопробуйте перезапустить приложение и ввести требуемое действие "}

AFTER_CONF_CREATION = 'Для ознакомления с функционалом - пройдите по ссылке: https://github.com/KulkovN/password_mng_term/blob/main/README.md'
# "Конфиг создан. При старте приложения нужно ввести мастер-пароль и режим из списка\n\
# 'найти', 'изменить', 'удалит', 'создать', 'create', 'find', 'read', 'update', 'change', 'delete', 'c','r','u','d' - тоже будет работать)\
# \nДля выхода - q"

URL_HELP = 'https://github.com/KulkovN/password_mng_term/blob/main/README.md'