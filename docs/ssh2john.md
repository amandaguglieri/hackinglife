---
title: ssh2jonh.py
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - brute
  - force
  - dictionary
  - attack
  - enumeration
---
# ssh2jonh.py

There is a Python script called `ssh2john.py` for SSH keys, which generates the corresponding hashes for encrypted SSH keys, which we can then store in files. It's preinstalled in Kali linux:

## Basic commands

 Save the ssh private key as a hash:

```shell-session
ssh2john.py SSH.private > ssh.hash
```

Now we can crack the hash with [johntheripper](john-the-ripper.md):

```shell-session
john --wordlist=rockyou.txt ssh.hash
```