---
title: nishang
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - payloads
  - tools
---

# Nishang 

Nishang is a framework and collection of scripts and payloads which enables usage of PowerShell for offensive security, penetration testing and red teaming. Nishang is useful during all phases of penetration testing.

## Installation

Download from github repo: [https://github.com/samratashok/nishang](https://github.com/samratashok/nishang).

```bash
sudo apt install nishang
```


## Antak Webshell

Antak is a webshell written in ASP.Net which utilizes PowerShell. Active Server Page Extended (ASPX) is a file type/extension written for Microsoft's ASP.NET Framework. Antak is included within the [Nishang project](https://github.com/samratashok/nishang). 

The Antak files can be found in the `/usr/share/nishang/Antak-WebShell` directory.


When uploaded on a http server in the victim machine, Antak web shell functions like a Powershell Console. However, it will execute each command as a new process. It can also execute scripts in memory and encode commands you send.

Before uploading Antak you will need to specify the user and password you want to use.

