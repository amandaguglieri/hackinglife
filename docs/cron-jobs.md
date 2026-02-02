---
title: Cron jobs - path, wildcards, file overwrite.
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - linux
---

# Cron jobs

These are divided into the system-wide area (`/etc/crontab`) and user-dependent executions. Some applications and scripts require credentials to run and are therefore incorrectly entered in the cronjobs. Furthermore, there are the areas that are divided into different time ranges (/etc/cron.daily, /etc/cron.hourly, /etc/cron.monthly, /etc/cron.weekly). The scripts and files used by cron can also be found in /etc/cron.d/ for Debian-based distributions.


Scheduled tasks are listed under the /etc/cron.* directories, there * represents the frequency at which the task will run.

```bash
# Check scheduled cron jobs
ls -la /etc/cron.*
```

System admin sometimes add their own scheduled task in the `/etc/crontab` file:

```bash
# One way
cat /etc/crontab

# Other way
crontab -l

# Check also with sudo
sudo crontab -l
```


Basically, the principle behind this technique is:

+ writing to a directory called by a cron job, 
+ and include a bash script with a reverse shell command,
+ which should send us a reverse shell when executed.

```shell-session
find / -path /proc -prune -o -type f -perm -o+w 2>/dev/null
```

The command explained:

```
**`-path /proc -prune`**

- `-path /proc` matches the `/proc` directory.
- `-prune` prevents `find` from descending into `/proc`, which is a virtual filesystem and does not contain actual files.

**`-o` (OR operator)**

- Ensures that if `/proc` is pruned, the next condition (`-type f -perm -o+w`) is still evaluated.

**`-perm -o+w`**

- Finds files that are **world-writable** (i.e., writable by "others").
- Equivalent to `chmod o+w`, meaning anyone on the system can modify these files.
```

Basically, if we spot a file listed here and located in one of the cron locations, it may be running as a cron job.



## **1.**  /etc/crontab
The crontab command can create a cron file, which will be run by the cron daemon on the schedule specified. When created, the cron file will be created in /var/spool/cron for the specific user that creates it. 

Each entry in the crontab file requires six items in the following order: minutes, hours, days, months, weeks, commands. For example, the entry `0 */12 * * * /home/admin/backup.sh` would run every 12 hours.

The root crontab is almost always only editable by the root user or a user with full sudo privileges

## 2. /var/log/cron.log

Inspect the cron log file (/var/log/cron.log) for running cron jobs:

```bash
grep "CRON" /var/log/syslog
```

Example of output:

```text
Feb  2 14:23:13 debian-privesc CRON[1308]: (root) CMD (/bin/bash /home/joe/.scripts/user_backups.sh)
Feb  2 14:24:01 debian-privesc CRON[1393]: (root) CMD (/bin/bash /home/joe/.scripts/user_backups.sh)
Feb  2 14:25:01 debian-privesc CRON[1517]: (root) CMD (/bin/bash /home/joe/.scripts/user_backups.sh)
```

## **3.**  /etc/cron.d

Certain applications create cron files in the /etc/cron.d directory and may be misconfigured to allow a non-root user to edit them.


## **4.** /var/spool/cron/crontabs/root


## pspy

[See pspy](pspy.md).

This tool can help you to locate running processes.  