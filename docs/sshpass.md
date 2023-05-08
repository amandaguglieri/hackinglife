---
title: sshpass - A program to pass passwords in the command line to ssh 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - tools
---

# sshpass - A program to pass passwords in the command line to ssh 

sshpass is a program that allows us to pass passwords in the command line to ssh. This way we can automate the login process.

## Installation

```bash
sudo apt install sshpass
```

## Usage

```bash
sshpass -p 'thepasswordisthis' ssh user@IP
```

