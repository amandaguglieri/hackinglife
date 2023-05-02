---
title: ffuzz - ffuzz - A fast web fuzzer written in Go
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
  - enumeration
---

# ffuzz - A fast web fuzzer written in Go

## Installation

Download from: [https://github.com/ffuf/ffuf](https://github.com/ffuf/ffuf)

## Basic commands

```bash
ffuf -w /path/to/wordlist -u https://target/FUZZ

# Assuming that the default virtualhost response size is 4242 bytes, we can filter out all the responses of that size (`-fs 4242`)while fuzzing the Host - header:
ffuf -w /path/to/vhost/wordlist -u https://target -H "Host: FUZZ" -fs 4242
```