---
title: system timers
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - linux
---

# system timers

A **systemd timer** is the modern replacement for a cron job. Instead of a line in `/etc/crontab`, a scheduled task on a systemd box is two files that work as a pair:

- A **`.timer` unit** — the _schedule_. It says "when." It does nothing on its own except wait for its time and then activate its partner.
- A **`.service` unit** — the _work_. It says "what to run and as whom." The timer starts this service each time it fires.

