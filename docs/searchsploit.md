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

```shell-session
searchsploit <WhatYouAreLookingFor>
```

Example:

![searchsploit results for ApPHP](img/searchsploit.png)

If you want to have a look at those POCs, append the path provided to the root location for the searchsploit database (`/usr/share/exploitdb/exploits`).