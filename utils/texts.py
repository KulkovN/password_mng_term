from pyfiglet import Figlet

PREWIEW = Figlet(font='slant')
HI = PREWIEW.renderText('PassMng')
BYE = PREWIEW.renderText('bye bye')

TASKS = ['найти', 'find', 'изменить', 'change', 'удалить', 'delete','создать','create']
TASKS_EXIT = ['q', 'й', 'exit', 'выход']
VARABLES = ['service', 'login', 'password']

MES_S = {'attempts' : "\nУ вас есть 3 попытки для ввода действия.""", 
    'what_u_do':"\nЧто вы хотите сделать\nнайти, изменить, удалит, создать (можно на анг.яз.)\nДля выхода - q: ",
    'zero_att' : "\nПопытки исчерпаны. Попробуйте перезапустить приложение и ввести требуемое действие "}
