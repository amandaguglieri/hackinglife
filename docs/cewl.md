---
title: cewl - A custom dictionary generator
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - enumeration
  - dictionaries
  - tools
---
# cewl - A custom dictionary generator

## Installation

Preintalled in Kali Linux.

Github repo: [https://github.com/digininja/CeWL](https://github.com/digininja/CeWL).

## Basic commands

```bash
cewl -m 6 -d 3 --lowercase  URL
# -d <x>,--depth <x>: Depth to spider to, default 2.
# -m, --min_word_length: Minimum word length, default 3.
# --lowercase: save as lowercase
```

## Examples from real life

```bash
cewl domain/path-to-post -w outputfile.txt
# -w output a list of words to a file.
```
