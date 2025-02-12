---
title: Cron jobs - path, wildcards, file overwrite.
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege escalation
  - linux
---

# Cron jobs

In Linux, a common form of maintaining scheduled tasks is through Cron Jobs. The equivalent in Windows would be a Scheduled task. There are specific directories that we may be able to utilize to add new cron jobs if we have the write permissions over them.

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

## **2.**  /etc/cron.d

Certain applications create cron files in the /etc/cron.d directory and may be misconfigured to allow a non-root user to edit them.



## **3.** /var/spool/cron/crontabs/root



## pspy

[See pspy](pspy.md).

This tool can help you to locate running processes.  