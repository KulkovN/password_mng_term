import json
from pathlib import Path


PATH_TO_FILE = f'{Path.home()}/Desktop/.allpwd.json'


def show_all():
    with open(PATH_TO_FILE) as file:
        data = json.load(file)
        print('Ваши сервисы:\n')
        for i in data['Loggins & passwords']:
            print(i['service'])

if __name__ == "__main__":
    show_all()
    