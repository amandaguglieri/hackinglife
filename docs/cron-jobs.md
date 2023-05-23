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


In Linux, a common form of maintaining scheduled tasks is through Cron Jobs. The equivalent in Windows would be a Scheduled task. There are specific directories that we may be able to utilize to add new cron jobs if we have the write permissions over them:

**1.**  /etc/crontab

**2.**  /etc/cron.d

**3.** /var/spool/cron/crontabs/root


Basically, the principle behind this technique is:

+ writing to a directory called by a cron job, 
+ and include a bash script with a reverse shell command,
+ which should send us a reverse shell when executed.