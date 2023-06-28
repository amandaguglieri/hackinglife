---
title: postfix - A SMTP server
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - linux
  - tool
  - SMTP
  - SMTP server
---

# postfix - A SMTP server

## Local installation

```bash
sudo apt update

sudo apt install mailutils
# At the end of the installation a pop up will prompt you about the general type of mail configuration. Pick "Internet site". If not prompted, run this to execute it:
sudo dpkg-reconfigure postfix
# System mail name must coincide with the  server's name you provided before.
```

To edit the configuration of the service:

```bash
sudo nano /etc/postfix/main.cf
```

[More on https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postfix-as-a-send-only-smtp-server-on-ubuntu-18-04-es](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postfix-as-a-send-only-smtp-server-on-ubuntu-18-04-es).

