---
title: Man in the browser attack
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - python
  - python pentesting
  - techniques
  - firefox
  - browsers
---

# Man in the browser attack

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


All the browsers offer to save username/password when you submit these data into a login page, so on the next time you visit the same login page you will see your username/password are automatically filled in without typing a single letter. Also, there's third party software like lastpass can do the same job for you.  

If the target was using this method for login, then neither the keylogger nor the clipboard methods will work.  

Modern hackers have invented a new attack called -man in the browser- to overcome the above scenario.

In a nutshell, man in the browser attack intercepts the browser API calls and extracts the data (clear text) before it's getting out to the network socket (SSL encrypted).

## Steps to intercept a process API calls are:- 

A. Get the Process ID (PID) of the browser process 

B. Attach a debugger to this PID 

C. Specify the DLL library that you want to intercept 

D. Specify the function name and resolve its memory  address 

E. Set BreakPoint and register a call back function  

F. Wait for debug events using debug loop 

G. Once the debug event occur ( meaning once the browser  calls the function inside the DLL),  execute the call back function 

H. Return the original process   