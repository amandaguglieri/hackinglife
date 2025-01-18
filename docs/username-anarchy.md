---
title: Username Anarchy
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - CPTS
  - dictionary
  - password
---
# Username Anarchy

Ruby-based tool for generating usernames.

This is useful for user account/password brute force guessing and username enumeration when usernames are based on the users' names. By attempting a few weak passwords across a large set of user accounts, user account lockout thresholds can be avoided.

## Installation

Download from github repo: [https://github.com/urbanadventurer/username-anarchy](https://github.com/urbanadventurer/username-anarchy).

```bash
git clone https://github.com/urbanadventurer/username-anarchy.git
```


## Basic usage

```bash
cd username-anarchy
./username-anarchy -i /home/ltnbob/realneames.txt 
```