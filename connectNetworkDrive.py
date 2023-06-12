import os
import subprocess


def connectDrive():
    username = 'MicrosoftAccount\dima.sak.dmitriy.sak@mail.ru'
    password = '89519821Dd1'
    server = r'\\Desktop-ceiepvc\сетевая папка'
    drive_letter = 'Z:'

    cmd = ['net', 'use', drive_letter, server, '/user:' + username]
    result = subprocess.run(cmd, input=password.encode(), capture_output=True)

    if result.returncode == 0:
        print('Диск успешно подключен')
    else:
        print('Ошибка при подключении диска')
