---
title: "bash"
draft: false
TableOfContents: true
---

## Shortcuts

+Delete last word CTRL-W
+Fill out the next word that appears in gray: CTRL ->

## Commands

### ss
Sockets statistic. It can be used to check which ports are listening locally on a given machine.

```bash
ss -ltn
#-l: Display only listening sockets.
#-t: Display TCP sockets.
#-n: Do not try to resolve service name.
```

