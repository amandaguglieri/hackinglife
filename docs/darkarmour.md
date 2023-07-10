---
title: darkarmour
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - payloads
  - tools
---

# darkarmour

Store and execute an encrypted windows binary from inside memory, without a single bit touching disk: generate an undetectable version of a pe executable.


## Installation

Download from github repo: [https://github.com/bats3c/darkarmour](https://github.com/bats3c/darkarmour).

It uses the python stdlib so no need to worry about any python dependencies, so the only issue you could come accoss are binary dependencies. The required binarys are: i686-w64-mingw32-g++, i686-w64-mingw32-gcc and upx (probly osslsigncode soon as well). These can all be installed via apt.

```bash
sudo apt install mingw-w64-tools mingw-w64-common g++-mingw-w64 gcc-mingw-w64 upx-ucl osslsigncode
```

## Basic usage

```bash
./darkarmour.py -f bins/meter.exe --encrypt xor --jmp -o bins/legit.exe --loop 5


# -f: file to crypt, assumed as binary if not told otherwise
# -e: encryption algorithm to use (xor)
# -S: SHELLCODE file contating the shellcode, needs to be in the 'msfvenom -f raw' style format 
# -b: provide if file is a binary exe
# -d, --dll: use reflective dll injection to execute the binary inside another process
# -s: provide if the file is c source code
# -k: key to encrypt with, randomly generated if not supplied
# -l LOOP, --loop: LOOP  number of levels of encryption
# -o: name of outfile, if not provided then random filenameis assigned
```

