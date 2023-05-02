---
title: grep
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - reconnaissance
---

# grep

It filters out output

```
# -C return 5 lines up and 5 lines down the line where the criteria is matched
cat text.txt  | grep -C 5 "password"`
```