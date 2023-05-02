---
title: veil - A backdoor generator
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
---

# veil

## Installation

Repository: [https://github.com/Veil-Framework/Veil/](https://github.com/Veil-Framework/Veil/)


Quick install for kali:

```bash
apt update
apt install -y veil
/usr/share/veil/config/setup.sh --force --silent
```


To run veil:

```bash
veil
```

## Usage and basic command


Tool "Evasion" creates undetectable backdoors.

"Ordenance" is the payload part that we will launch to this backdoor.

Reading list:

* https://www.zonasystem.com/2020/07/shellter-veil-evasion-evasion-de-antivirus-ocultando-shellcodes-de-binarios.html
* https://www.hackingloops.com/veil-evasion-virustotal/---


One nice thing about veil is that it provides a metasploit RC file, meaning that in order to launch the multihandler you just need to run:

```bash
msfconsole -r path/to/metasploitRCfile
```