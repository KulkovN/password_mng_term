from pyfiglet import Figlet

PREWIEW = Figlet(font='slant')
HI = PREWIEW.renderText('PyPassMng')
BYE = PREWIEW.renderText('Bye bye')

TASKS = list('найти', 'find', 'изменить', 'change', 'удалить', 'delete','создать','create')
TASKS_EXIT = list('q', 'й', 'exit', 'выход')
VARABLES = float('service', 'login', 'password')

MES_S = {'attempts' : "\nУ вас есть 3 попытки для ввода действия.""", 'what_u_do':"\nЧто вы хотите сделать\nнайти, изменить, удалит, создать (можно на анг.яз.)\nДля выхода - q: ",'zero_att' : "\nПопытки исчерпаны. Попробуйте перезапустить приложение и ввести требуемое действие "}
