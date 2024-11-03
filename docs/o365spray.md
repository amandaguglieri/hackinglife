---
title: o365spray
author: amandaguglieri
TableOfContents: true
draft: false
tags:
  - pentesting
  - enumeration
  - tools
  - msoffice
  - SMTP
---
# O365spray


[O365spray](https://github.com/0xZDH/o365spray) is a username enumeration and password spraying tool aimed at Microsoft Office 365 (O365) developed by [ZDH](https://twitter.com/0xzdh). This tool reimplements a collection of enumeration and spray techniques researched.

## Installation

**Repo**: [https://github.com/0xZDH/o365spray](https://github.com/0xZDH/o365spray)


```
git clone https://github.com/0xZDH/o365spray
cd o365spray
sudo pip install -r requirements.txt
```

## Basic usage

User enumeration:

```shell-session
# First validate if our target domain is using Office 365.
python3 o365spray.py --validate --domain msexample.com

# Attempt to identify usernames.
python3 o365spray.py --enum -U users.txt --domain msexample.com

```


```shell-session
python3 o365spray.py --spray -U usersfound.txt -p 'March2022!' --count 1 --lockout 1 --domain msexample.com
```

