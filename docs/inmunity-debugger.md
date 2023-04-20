---
title: Inmunity Debugger
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - python
  - python pentesting
  - tools
---

# Inmunity Debugger

## Installation

https://www.immunityinc.com/products/debugger/


## Firefox API hooking with Inmunity Debugger

Firefox uses a function called PR_Write inside a dll module  called nss3.dll to write/submit data.  So once  the target enters his username and password and click  on login button the fireforx process will call  PR_Write function from nss3.dll module, if we setup a break point at that function we should see the data in clear text. 

Reference:-  https://developer.mozilla.org/en-docs/Mozilla/Projects/NSPR/Reference/PR_Write 