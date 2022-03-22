import os
import pyAesCrypt


def crypt(file, paswd, flag):
    buffer = 512 * 1024
    # шифруем 
    if flag == 'crypt':
        pyAesCrypt.encryptFile(
            file, f'{file}.csp', 
            paswd, buffer 
        ) 
        os.remove(file)
        print("Шифр")
    # дешифруем
    else:
        pyAesCrypt.decryptFile(file,
            os.path.splitext(file)[0],
            paswd, buffer)
        print('Разшифр')


if __name__ == "__main__":
    # passwd = input('Введите пароль: ')
    crypt('/Users/kulkovni/Desktop/allpwd_2.json.csp', '3571', '')
    
