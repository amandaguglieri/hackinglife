---
title: Linikatz
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - kerberos
  - linikatz
---
# Linikatz

Linikatz brings a similar principle to `Mimikatz` to UNIX environments. Just like `Mimikatz`, to take advantage of Linikatz, we need to be root on the machine.  This tool will extract all credentials, including Kerberos tickets, from different Kerberos implementations such as FreeIPA, SSSD, Samba, Vintella, etc. Once it extracts the credentials, it places them in a folder whose name starts with `linikatz.`

## Installation

Repo: https://github.com/CiscoCXSecurity/linikatz

```shell-session
wget https://raw.githubusercontent.com/CiscoCXSecurity/linikatz/master/linikatz.sh
```