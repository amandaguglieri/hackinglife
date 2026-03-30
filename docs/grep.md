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

TRouble shootung:

```
file upgrader_default.log  
xxd -l 64 upgrader_default.log
```

If it says something like `Little-endian UTF-16 Unicode text`, use one of these:

```
grep -a "Exiting" upgrader_default.log
```

or better:

```
iconv -f UTF-16LE -t UTF-8 upgrader_default.log | grep "Exiting"
```

with context:

```
iconv -f UTF-16LE -t UTF-8 upgrader_default.log | grep -C 2 "Exiting"
```