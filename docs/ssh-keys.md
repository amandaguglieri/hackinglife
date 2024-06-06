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

Having read access over the .ssh directory for a specific user, we may read their private ssh keys found in /home/user/.ssh/id_rsa or /root/.ssh/id_rsa, and we can copy it to our machine and use the -i flag to log in with it:

```shell-session
vim id_rsa
chmod 600 id_rsa
# If ssh keys have lax permissions, i.e., maybe read by other people, the ssh server would prevent them from working.
ssh user@10.10.10.10 -i id_rsa
```

## Write access to .ssh

Having write access over the .ssh directory for a specific user, we may place our public key in /home/user/.ssh/authorized_keys.

But for this we need to have gained access first as that user. With this technique we obtain ssh access to the machine. 

```
# Generating a public private rsa key pair
ssh-keygen -f key
```

This will give us two files: `key` (which we will use with `ssh -i`) and `key.pub`, which we will copy to the remote machine.

Let us copy `key.pub`, then on the remote machine, we will add it into `/root/.ssh/authorized_keys`: