---
title: windapsearch - A tool for enumerating resources in Active Directory
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - tools
---
# Windapsearch - A tool for enumerating resources in Active Directory

## Installation

Download from: [https://github.com/ropnop/windapsearch](https://github.com/ropnop/windapsearch)

```shell
git clone https://github.com/ropnop/windapsearch.git
pip install python-ldap #or apt-get install python-ldap
# Troubleshooting: The python-ldap is based on OpenLDAP, so you need to have the development files (headers) in order to compile the Python module. If you're on Ubuntu, the package is called libldap2-dev.
# sudo apt-get install libsasl2-dev python-dev-is-python3 libldap2-dev libssl-dev

```

## Basic commands


```shell-session
# Enumerate Users
./windapsearch.py -d $domain -u $username\\ldapbind -p $password -U
# -U: returns only USERS
# -u: specifies username. "" for blank
# -p: indicates password
# -d: indicates domain

# Enumerate users with no user foothold
./windapsearch.py --dc-ip $ip -u "" -U
# -u: specifies username. "" for blank
# -U: returns only USERS

# Enumerate Domain Admins
./windapsearch.py --dc-ip $ip -u $username@$domain -p $password --da
./windapsearch.py -d $domain -u $username\\ldapbind -p $password --da
# --da: returns only Domain admins
# -u: specifies username. "" for blank
# -p: indicates password
# -d: indicates domain
# Example:
# python3 windapsearch.py --dc-ip 172.16.5.5 -u forend@inlanefreight.local -p Klmcargo2 --da

# Enumerating Computers
./windapsearch.py -d $domain -u $username\\ldapbind -p $password -C -r
# -r or --resolve option: the tool will perform a DNS lookup on every enumerated dNSHostName found and output the computer information, including IP address in CSV format. 
# -C: list all matching entries where objectClass=Computer

# Custom Search 
./windapsearch.py -d $domain -u $username\\ldapbind -p $password -s Lalala
# -s: search everywhere the term, in this case Lalala.

# Enumerate Privilege Users with -PU
python3 windapsearch.py --dc-ip $ip -u $username@$domain -p $password -PU
```

