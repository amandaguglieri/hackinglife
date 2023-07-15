---
title: unshadow
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - bash
---

# unshadow

unshadow - combines passwd and shadow files



### Brute forcing /etc/passwd and /etc/shadow

**First**, save /etc/passwd and john /etc/shadow from the victim machine to the attacker machine.

**Second**, use unshadow to put users and passwords in the same file:

```bash
unshadow passwd shadow > crackme
# passwd: file saved with /etc/passwd content.
# shadow: file saved with /etc/shadow content.
```

**Third**, run [johtheripper](john-the-ripper.md) or [hashcat](hashcat.md) to crack the hash.
