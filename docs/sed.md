---
title: sed Command in Linux
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - tools
  - bash
  - scripting
---
# sed Command in Linux

The sed (Stream Editor) command in Linux is a powerful utility for text manipulation. 


Substitute the string comma (`,`) for a new line in all occurrences of the lines and output a new file:

```bash
sed 's/,/\n/g' file.txt > outputfile.txt

# s: command for substitution
# \n:  new line
# g: do it in all occurrences of each line
```

