---
title: wget
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - bash
  - tools
  - pentesting
---

# Wget

Retrieve a file:

```
wget http://example.com/filename.zip
```


Retrieve all files under a given folder

```
wget -r -np -nH --cut-dirs=1 --reject="index.html*" http://example.com/folder/
```

**Explanation of options:**

- `-r`: Recursively download the files.
- `-np`: Prevents `wget` from following links to parent directories.
- `-nH`: Disables the creation of directories based on the hostname.
- `--cut-dirs=1`: Skips the first directory level when saving the files locally (adjust this depending on your folder structure).
- `--reject="index.html*"`: Excludes the index file from being downloaded.