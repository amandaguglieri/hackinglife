---
title: crunch - A dictionary generator
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting, enumeration, dictionaries, tools
---

**Crunch** generates combinations of words and manglings to be used later off as attacking dictionaries.

## Installation

Preinstalled in kali linux. To install:

```bash
sudo apt install crunch
```

## Basic commands

```bash
# Generates words from <number1> to <number2> with the specified characters.
crunch <number1> <number2> <characters> -o file.txt
# <number1>: minimum of characters that password has
# <number2>: maximum of characters that password has
# <characters>: those characters included in the set
# -o: Send output to file.txt
# There exists more flags
```

## Resources

- [Advanced crunch: https://secf00tprint.github.io/blog/passwords/crunch/advanced/en](https://secf00tprint.github.io/blog/passwords/crunch/advanced/en).



