---
title: Linux credentials storage
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - linux
---

# Linux 

## Find sensitive files

### Configuration files

```bash
# Return files with extension .conf, .config and .cnf, which in linux are configuration files.
for l in $(echo ".conf .config .cnf");do echo -e "\nFile extension: " $l; find / -name *$l 2>/dev/null | grep -v "lib\|fonts\|share\|core" ;done


# Search for three words (user, password, pass) in each file with the file extension .cnf.
for i in $(find / -name *.cnf 2>/dev/null | grep -v "doc\|lib");do echo -e "\nFile: " $i; grep "user\|password\|pass" $i 2>/dev/null | grep -v "\#";done

```

### Databases

```bash
# Search for databases
for l in $(echo ".sql .db .*db .db*");do echo -e "\nDB File extension: " $l; find / -name *$l 2>/dev/null | grep -v "doc\|lib\|headers\|share\|man";done
```


### Scripts

```bash
for l in $(echo ".py .pyc .pl .go .jar .c .sh");do echo -e "\nFile extension: " $l; find / -name *$l 2>/dev/null | grep -v "doc\|lib\|headers\|share";done
```

### Files including the .txt file extension and files that have no file extension at all

Admin may change the name of configuration files. But you can try to find them:

```bash
find /home/* -type f -name "*.txt" -o ! -name "*.*"
```

### cronjobs

These are divided into the system-wide area (`/etc/crontab`) and user-dependent executions. Some applications and scripts require credentials to run and are therefore incorrectly entered in the cronjobs. Furthermore, there are the areas that are divided into different time ranges (/etc/cron.daily, /etc/cron.hourly, /etc/cron.monthly, /etc/cron.weekly). The scripts and files used by cron can also be found in /etc/cron.d/ for Debian-based distributions.

### SSH Keys

```bash
grep -rnw "PRIVATE KEY" /home/* 2>/dev/null | grep ":1"

grep -rnw "ssh-rsa" /home/* 2>/dev/null | grep ":1"
```

### Bash History

```bash
tail -n5 /home/*/.bash*
```

### Logs

|**Log File**|**Description**|
|---|---|
|`/var/log/messages`|Generic system activity logs.|
|`/var/log/syslog`|Generic system activity logs.|
|`/var/log/auth.log`|(Debian) All authentication related logs.|
|`/var/log/secure`|(RedHat/CentOS) All authentication related logs.|
|`/var/log/boot.log`|Booting information.|
|`/var/log/dmesg`|Hardware and drivers related information and logs.|
|`/var/log/kern.log`|Kernel related warnings, errors and logs.|
|`/var/log/faillog`|Failed login attempts.|
|`/var/log/cron`|Information related to cron jobs.|
|`/var/log/mail.log`|All mail server related logs.|
|`/var/log/httpd`|All Apache related logs.|
|`/var/log/mysqld.log`|All MySQL server related logs.|


```bash
 for i in $(ls /var/log/* 2>/dev/null);do GREP=$(grep "accepted\|session opened\|session closed\|failure\|failed\|ssh\|password changed\|new user\|delete user\|sudo\|COMMAND\=\|logs" $i 2>/dev/null); if [[ $GREP ]];then echo -e "\n#### Log file: " $i; grep "accepted\|session opened\|session closed\|failure\|failed\|ssh\|password changed\|new user\|delete user\|sudo\|COMMAND\=\|logs" $i 2>/dev/null;fi;done
```



## Credentials storage

### Shadow file

The /etc/shadow file has a unique format in which the entries are entered and saved when new users are created.

```
htb-student: 	$y$j9T$3QSBB6CbHEu...SNIP...f8Ms: 	18955: 	0: 	99999: 	7: 	: 	: 	:
<username>: 	<encrypted password>: 	<day of last change>: 	<min age>: 	<max age>: 	<warning period>: 	<inactivity period>: 	<expiration date>: 	<reserved field>
```


The encryption of the password in this file is formatted as follows:

| | | |
|---|---|---|
|`$ <id>`|`$ <salt>`|`$ <hashed>`|
|`$ y`|`$ j9T`|`$ 3QSBB6CbHEu...SNIP...f8Ms`|


The type (`id`) is the cryptographic hash method used to encrypt the password. Many different cryptographic hash methods were used in the past and are still used by some systems today.

|**ID**|**Cryptographic Hash Algorithm**|
|---|---|
|`$1$`|[MD5](https://en.wikipedia.org/wiki/MD5)|
|`$2a$`|[Blowfish](https://en.wikipedia.org/wiki/Blowfish_(cipher))|
|`$5$`|[SHA-256](https://en.wikipedia.org/wiki/SHA-2)|
|`$6$`|[SHA-512](https://en.wikipedia.org/wiki/SHA-2)|
|`$sha1$`|[SHA1crypt](https://en.wikipedia.org/wiki/SHA-1)|
|`$y$`|[Yescrypt](https://github.com/openwall/yescrypt)|
|`$gy$`|[Gost-yescrypt](https://www.openwall.com/lists/yescrypt/2019/06/30/1)|
|`$7$`|[Scrypt](https://en.wikipedia.org/wiki/Scrypt)|

The /etc/shadow file can only be read by the user root.

### Passwd file

The /etc/passwd

```						
htb-student: 	x: 	1000: 	1000: 	,,,: 	/home/htb-student: 	/bin/bash
<username>: 	<password>: 	<uid>: 	<gid>: 	<comment>: 	<home directory>: 	<cmd executed after logging in>
```

The `x` in the password field indicates that the encrypted password is in the `/etc/shadow` file.



## Opasswd

The PAM library (`pam_unix.so`) can prevent reusing old passwords. The file where old passwords are stored is the `/etc/security/opasswd`. Administrator/root permissions are also required to read the file if the permissions for this file have not been changed manually.

```bash
# Reading /etc/security/opasswd
sudo cat /etc/security/opasswd

# cry0l1t3:1000:2:$1$HjFAfYTG$qNDkF0zJ3v8ylCOrKB0kt0,$1$kcUjWZJX$E9uMSmiQeRh4pAAgzuvkq1
```

Looking at the contents of this file, we can see that it contains several entries for the user cry0l1t3, separated by a comma (,). Another critical point to pay attention to is the hashing type that has been used. This is because the MD5 ($1$) algorithm is much easier to crack than SHA-512. This is especially important for identifying old passwords and maybe even their pattern because they are often used across several services or applications. We increase the probability of guessing the correct password many times over based on its pattern.


## Dumping memory and cache

[mimipenguin](https://github.com/huntergregal/mimipenguin)
[lazagne](https://github.com/AlessandroZ/LaZagne)

Firefox stored credentials:

```bash
ls -l .mozilla/firefox/ | grep default 

cat .mozilla/firefox/xxxxxxxxx-xxxxxxxxxx/logins.json | jq .
```

The tool [Firefox Decrypt](https://github.com/unode/firefox_decrypt) is excellent for decrypting these credentials, and is updated regularly. It requires Python 3.9 to run the latest version. Otherwise, `Firefox Decrypt 0.7.0` with Python 2 must be used.

