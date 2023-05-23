---
title: SSH keys 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege escalation
  - linux
---

# SSH keys

## Read access to .ssh

Having read access over the .ssh directory for a specific user, we may read their private ssh keys found in /home/user/.ssh/id_rsa or /root/.ssh/id_rsa, and use it to log in to the server.

```shell-session
vim id_rsa
chmod 600 id_rsa
ssh user@10.10.10.10 -i id_rsa
```

## Write access to .ssh

Having write access over the .ssh directory for a specific user, we may place our public key in /home/user/.ssh/authorized_keys.

But for this we need to have gained access first as that user. With this technique we obtain ssh access to the machine. 