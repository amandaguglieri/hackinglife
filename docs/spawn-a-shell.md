---
title: Spawn a shell
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting, terminal, shells
---

# Spawn a shell

## python

```bash
python -c 'import os; os.system("/bin/sh")'
```

```bash
 # using pty
python -c 'import pty; pty.spawn("/bin/bash")'
```


