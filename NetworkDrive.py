import os
import subprocess
import re


def connectDrive(username, password):
    # ---------------------
    #username = 'MicrosoftAccount\dima.sak.dmitriy.sak@mail.ru'
    #password = '89519821Dd'
    drive_letter = 'U:'
    driveList = [r'\\Desktop-ceiepvc\Rackstation']
    # ---------------------

    output = subprocess.check_output(["net", "use"]).decode("cp866")
    pattern = r"([A-Z]:) +([^ ]+) +(.+)"
    matches = re.findall(pattern, output)

    for drive in driveList:
        if matches != []:
            for match in matches:
                local_drive, remote_path, status = match
                if remote_path == drive:
                    print(f'Диск {drive} подключен!')
                    return True
                else:
                    cmd = ['net', 'use', drive_letter, drive, '/user:' + username, password]
                    result = subprocess.run(cmd, input=password.encode(), capture_output=True)

                    if result.returncode == 0:
                        print(f"Диск '{drive}' успешно подключен")
                        return True
                    else:
                        print(f"Ошибка при подключении диска '{drive}' ")
                        return False
        else:
            cmd = ['net', 'use', drive_letter, drive, '/user:' + username]
            result = subprocess.run(cmd, input=password.encode(), capture_output=True)
            if result.returncode == 0:
                print(f"Диск '{drive}' успешно подключен")
                return True
            else:
                print(f"Ошибка при подключении диска '{drive}' ")
                return False