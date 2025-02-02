---
title: JoomlaScan - Joomla Security Scanner
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web
  - pentesting
  - enumeration
  - joomla
---
#  JoomlaScan - Joomla Security Scanner


## Installation

JoomlaScan is a bit out-of-date and requires Python2.7 to run. 

Requirements:

```shell-session
sudo python2.7 -m pip install urllib3

sudo python2.7 -m pip install certifi

sudo python2.7 -m pip install bs4
```

As I have a virtual environment for 2.7:

```
# As I have a virtual environment for 2.7:
pyenv activate 27

# Install joomlascan
git clone https://github.com/drego85/JoomlaScan.git
cd JoomlaScan
```

## Basic commands


```shell-session
python2.7 joomlascan.py -u http://$target
```