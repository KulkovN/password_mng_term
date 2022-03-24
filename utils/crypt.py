import os
import pyAesCrypt


def crypt(file, paswd, flag):
    buffer = 512 * 1024
    # шифруем 
    if flag == 'crypt':
        pyAesCrypt.encryptFile(file, f'{file}.aes'\
            ,paswd, buffer) 
        os.remove(file)
        print("Файл зашифрован...")
    # дешифруем
    else:
        pyAesCrypt.decryptFile(file\
            ,os.path.splitext(file)[0],
            paswd, buffer)
        os.remove(file)
        print('Файл разшифрован...')
