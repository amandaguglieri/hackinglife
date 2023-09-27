---
title: curl
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - bash
  - tools
  - pentesting
---

## Basic usage

```bash
curl -i -L $host
# -L: Follow redirections
# -i: Include headers in the response 

curl -T file.txt
# -T, --upload-file <file>; This transfers the specified local file to the remote URL. -T uses PUT http method

curl -o target/path/filename URL
# -o: to specify a location/filename
```