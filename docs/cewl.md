---
title: cewl - A custom dictionary generator
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting, enumeration, dictionaries
---

# cewl - A custom dictionary generator

## Installation

Preintalled in Kali Linux.

Github repo: [https://github.com/digininja/CeWL](https://github.com/digininja/CeWL).

## Basic commands

```bash
cewl -m 6 -d 3 URL
# -d <x>,--depth <x>: Depth to spider to, default 2.
# -m, --min_word_length: Minimum word length, default 3.
```

## Examples from real life

```bash
cewl domain/path-to-post -w wordlist.txt
# -w output a list of words to a file.
```
