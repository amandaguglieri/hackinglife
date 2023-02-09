---
title: Setting up the environment
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - api
---

# Setting up the environment

??? abstract "General index of the course"
    - [Setting up the environment](setting-up-kali.md)
    - [Api Reconnaissance](api-reconnaissance.md).
    - [Endpoint Analysis](endpoint-analysis.md).
    - [Scanning APIS](scanning-apis.md).
    - [API Authorization Attacks](api-authentication-attacks.md).
    - [Exploiting API Authorization](exploiting-api-authorization.md).
    - [Testing for Improper Assets Management](improper-assets-management.md).
    - [Mass Assignment](mass-assignment.md).
    - [Server side Request Forgery](server-side-request-forgery-ssrf.md).
    - [Injection Attacks](injection-attacks.md). 
    - [Evasion and Combining techniques](evasion-combining-techniques.md).
    - [Setting up the labs + Writeups](other-labs.md)


For this course, I'll use a Kali machine installed on VirtualBox. I downloaded last .ova version, 2022-3. 

After that, follow these steps:

## 1. Install a kali ova on VirtualBox

For this course I've downloaded a Kali .ova machine. I will be using VirtualBox and I will modify these elements in the ova installation:

- 4GB RAM
- Bridge mode Interface

## 2.  Update our system

```bash
sudo apt update -y
sudo apt upgrade -y
sudo apt-dist upgrade -y
```

Also, update credentials:

```bash
sudo passwd kali    (enter in a new more complex password)
sudo useradd -m hapihacker
sudo usermod -a -G sudo hapihacker
sudo chsh -s /bin/zsh hapihacker
```

## 3. Install Burp Suite and make sure that is up-to-date.

```bash
sudo apt-get install burpsuite -y
```

## 4.  Adding extension Authorize extension to BurpSuite: this will require to have Jython installed. 

1. Download jython from: [https://www.jython.org/download.html](https://www.jython.org/download.html) and add the .jar file to the Extender Options.
2.  Under the Extender BApp Store search for Autorize and install the extension.

## 5. Install Foxy-proxy in Firefox to proxy the traffic to BurpSuite and Postman.  Once intalled, we'll set up manually two proxies

1.  Postman - 127.0.0.1 - 5555
2.  BurpSuite - 127.0.0.1 - 8080.

Download BurpSuite certificate and have it installed in Firefox. 

## 6. MITMweb certificate setup

1. Install mitmweb from the terminal:

```bash
mitmweb
```

We need to make sure that Burpsuite is stopped, since mitmweb is also going to use port 8080.

2. Activate FoxyProxy in Firefox to send traffic  to the BurpSuite proxy (8080).

3.  Download mitmproxy-ca-cert.pem from mitm.it (in Firefox) and have it installed in Firefox.

## 7. Install Postman

```bash
sudo wget https://dl.pstmn.io/download/latest/linux64 -O postman-linux-x64.tar.gz && sudo tar -xvzf postman-linux-x64.tar.gz -C /opt && sudo ln -s /opt/Postman/Postman /usr/bin/postman
```

## 8.  Install mitmproxy2swagger

```bash
cd /opt
sudo pip3 install mitmproxy2swagger
```

## 9. Install git

```bash
cd /opt
sudo apt-get install git
```

## 10. Install docker

```bash
cd /opt
sudo apt-get install docker.io docker-compose
```

## 11. Install Go

```bash
cd /opt
sudo apt install golang-go
```

## 12. Install  JSON Web Token Toolkit v2

```bash
cd /opt
sudo git clone https://github.com/ticarpi/jwt_tool
cd jwt_tool
python3 -m pip install termcolor cprint pycryptodomex requests

# Optional: Make an alias for jwt_tool.py**
sudo chmod +x jwt_tool.py
sudo ln -s /opt/jwt_tool/jwt_tool.py /usr/bin/jwt_tool
```

## 13. Install Kiterunner

```bash
sudo git clone https://github.com/assetnote/kiterunner.git
cd kiterunner
sudo make build
sudo ln -s /opt/kiterunner/dist/kr /usr/bin/kr
```

## 14. Install Arjun

[More about arjun](../arjun.md).

```bash
sudo git clone https://github.com/s0md3v/Arjun.git
```

## 15.  Install OWASP ZAP

```bash
sudo apt install zaproxy
```

Run ZAP and open the "Manage Add-ons" option and make sure that  the add-on "OpenAPI Support" is marked to be updated.

## 16.  Have these useful wordlist API oriented

```bash
# SecLists https://github.com/danielmiessler/SecLists
sudo wget -c https://github.com/danielmiessler/SecLists/archive/master.zip -O SecList.zip \  
&& sudo unzip SecList.zip \  
&& sudo rm -f SecList.zip

# Hacking-APIs https://github.com/hAPI-hacker/Hacking-APIs
sudo wget -c https://github.com/hAPI-hacker/Hacking-APIs/archive/refs/heads/main.zip -O HackingAPIs.zip \  
&& sudo unzip HackingAPIs.zip \  
&& sudo rm -f HackingAPIs.zip
```

