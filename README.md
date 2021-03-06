### Менеджер паролей
Простой-консольный менеджер паролей на python

`Важно`:
1) О возможных проблемах: 
- нет тестов запуска приложения на Microsoft Windows (не ставил целью кросплатформенность, на на unix работает стабильно)
- владельцам MacBook M1 - запускать проект с включенной галочокой Rosseta (причина проста - некоторые модули не компилируются под этот процессор)
2) Для работы скрипта - нужны модули python описанные в `reqruetments.txt`:
- astroid==2.9.3
- cffi==1.15.0
- cryptography==36.0.2
- isort==5.10.1
- lazy-object-proxy==1.7.1
- mccabe==0.6.1
- platformdirs==2.5.1
- prettytable==3.2.0
- pyAesCrypt==6.0.0
- pyasn1==0.4.8
- pycparser==2.21
- pyfiglet==0.8.post1
- pylint==2.12.2
- stdiomask==0.0.6
- toml==0.10.2
- typing_extensions==4.1.1
- wcwidth==0.2.5
- wrapt==1.13.3


Для установки (если установлен python2 и python3 - вместо `pip` пишите `pip3` ): 

        pip install -r /path/to/requirements.txt


### Цель и задачи приложения:
Поставленные цели при работе над приложением:  
- практика написания кода на python;
- предоставление простого консольного клиента для хранения данных в определенной структуре.

Приложение позволяет решать следующие задачи: 
- Приложение обладает функциями создания, чтения, изменения, удаления, данных пользователя;
- Приложение обеспечивает прозрачный механизм хранения данных пользователя в примитивном виде с возможностью чтения данных, посредством самого приложения и никаким другим;
-  Приложение обладает инструментов "простого шифрования" файла, в котором хранятся данные пользователя. Сам инструмент не имеет сложного алгоритма (учитывается "размер и сложность приложения"). Важно понимать, что непосредственно в момент работы скрипта - файл не является зашифрованным, а шифруется после прекращения выполнения.

### Алгоритм работы:
* Запуск скрипта и вся работа с ним происходит в терминале - при запуске main.py посредством интерпретатора python:

        $~: python3 ~/Desktop/password_mng_term/main.py
        или
        $~: ./Desktop/password_mng_term/main.py 


*`aliases` in your help ;)*

*как пример для вашего ~/.zshrc или ~/.bashrc:*

        alias pypass="~source py_env/bin/activate; ./${path_to_repo}/main.py; deactivate"
    
    
   При первом запуске - программа запросит: 
- мастер-пароль (это процедура "примитивной авторизации". 

в дальнейшем он будет запрошиваться сразу после инициализации приложения. Такая переменная необходима для реализации функционала шифрования/расшифровки файла, хранящего данные о паролях. Важно запомнить мастер пароль, т.к. в конфигурационном файле (`.py_pass/config/config.ini`) он хранится в зашифровонном виде. Функционал "Вспомнить пароль" или подобный не предусмотрен;
- полный путь для хранения данных о паролях пользователя, который будет сохранен в `.py_pass/config/config.ini` (папка конфига создается в корне папки пользователя системы. Мастер-пароль хранится захешированным, из соображений безопасности). 

Путь необходимо передать интерпретатору в виде:

        $~: home/Users/${your_user_name}/Desktop
Имя файла хранения, присваиваемое по умолчанию: `.allpwd.json` (точка перед файлам обозначает файл как скрытый). Функция "шифровальщик" - допишет расширение `.aes` что бы файл можно было прочесть только используя приложение, и никаким иным способом (или обладая специальными знаниями, конечно же :) )

Файл, до шифрования, создается в следующей структуре и содержанием ( { dict:[ list { dict } ] } ): 
    
        {
            "Loggins & passwords": 
                [
                    {}
                ]
        }


* После создания файла хранения - приложение запросит команду `режима работы` из списка возможных:

        ['создать','create', 'c', 
        'найти', 'find', 'f', 'r', 
        'изменить', 'change', 'ch', 'u'
        'удалить', 'delete', 'd'] 

в зависимости от ввода - приложение работает с json-файлом в соответствующем режиме. 
* Не зависимо от режима (за исключением создания) - пользователю предлагается выбрать сервис, к данным которого необходим доступ для: отображения, изменения, удаления. 

* При создании приложение запросит ввести все данные для записи по списку ['service', 'login', 'password'], при этом в момент сохранения элементы такого списка выступают в виде ключей. После ввода значений - скрипт сохранить данные в json, зашифрует файл и завершит работу.

<img src="https://user-images.githubusercontent.com/68808458/160195543-c79c38e5-ba61-4e86-bdc6-5a3ecfc1edb3.png" width="550"/>


*В режимах поиска, изменения, удаления - пользователю предоставляется полный список сервисов для удобства выбора нужного.*

*Кроме того во всех режимах (кроме [`create`]), реализован функционал автодополнения значения сервиса в вводе пользователя при нажатии клавиши `Tab`()*

*Поиск, замена, удаление - осуществляется по ключу: [`service`] - "имя сервиса":*

* После ввода ключа нужного сервиса - приложение вернет необходимые пользователю данные и прекратит выполнение.

<img src="https://user-images.githubusercontent.com/68808458/160195590-426f79b4-bbf0-4134-a253-146463820c49.png" width=550/>

* режим удаления и изменений работаю по такому же принципу:

*(при изменении данных) ввел ключ который необходимо заменить ['service', 'login', 'password'] -> ввел новое значение)*

<img src="https://user-images.githubusercontent.com/68808458/160195716-d3226de6-2154-46e2-bb81-36ace1ea966b.png" width=550/>

*(при удалении данных) ввел значения ключа сервис -> удалил его данные сервиса (логин, пароль, сам сервис из файла;*

<img src="https://user-images.githubusercontent.com/68808458/160195747-5f6592c1-d19a-4d56-931f-82d41581f033.png" width=550/>
