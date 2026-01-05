---
title: searchsploit
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
  - exploitation
---
# searchsploit

The Exploit Database is an archive of public exploits and corresponding vulnerable software, developed for use by penetration testers and vulnerability researchers.

## Installation

Pre-installed in kali. Download it from: [https://gitlab.com/exploit-database/exploitdb](https://gitlab.com/exploit-database/exploitdb)
Also:

```shell-session
sudo apt install exploitdb -y
```

## Basic usage

Default search is case insensitive:

```shell-session
searchsploit <WhatYouAreLookingFor>
```

Example:

![searchsploit results for ApPHP](img/searchsploit.png)

If you want to have a look at those POCs, append the path provided to the root location for the searchsploit database (`/usr/share/exploitdb/exploits`).

Basic commands:

```bash
searchsploit -t oracle windows
# -t, --title: Search JUST the exploit title (Default is title AND the file's path)

searchsploit -p 45788
# -p: Copy the Local path of the exploit to the clipboard

searchsploit -m 45788
# -m: Copy the exploit to current working directory

searchsploit linux kernel --exclude="(PoC)|/dos/"
# --exclude: Exclude from search
```

When viewing the output of a search, the field Path will indicate where in our machine the exploit is stored:

```bash
searchsploit MS14-040 
```

will return:

```text
----------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                     |  Path
----------------------------------------------------------------------------------- ---------------------------------
Microsoft Windows 7 (x64) - 'afd.sys' Dangling Pointer Privilege Escalation (MS14- | windows_x86-64/local/39525.py
Microsoft Windows 7 (x86) - 'afd.sys' Dangling Pointer Privilege Escalation (MS14- | windows_x86/local/39446.py
----------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```

For showing the web path to the exploit:

```bash
searchsploit MS14-040 -w   
```

will return:

```text
------------------------------------------------------------------------ --------------------------------------------
 Exploit Title                                                          |  URL
------------------------------------------------------------------------ --------------------------------------------
Microsoft Windows 7 (x64) - 'afd.sys' Dangling Pointer Privilege Escala | https://www.exploit-db.com/exploits/39525
Microsoft Windows 7 (x86) - 'afd.sys' Dangling Pointer Privilege Escala | https://www.exploit-db.com/exploits/39446
------------------------------------------------------------------------ --------------------------------------------
Shellcodes: No Results
```

