---
title: Bashfuscator - Evasion tool for code obfuscating in Linux
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - bash
  - evasion
  - obfuscation
---
# Bashfuscator - Evasion tool for code obfuscating in Linux

Bashfuscator is a modular and extendable Bash obfuscation framework written in Python 3. It provides numerous different ways of making Bash one-liners or scripts much more difficult to understand. It accomplishes this by generating convoluted, randomized Bash code that at runtime evaluates to the original input and executes it. Bashfuscator makes generating highly obfuscated Bash commands and scripts easy, both from the command line and as a Python library.

Repo in github: [https://github.com/Bashfuscator/Bashfuscator](https://github.com/Bashfuscator/Bashfuscator)


## Installation


```bash
git clone https://github.com/Bashfuscator/Bashfuscator
cd Bashfuscator
pip3 install setuptools==65
python3 setup.py install --user
```


## Basic commands

```shell-session
cd ./bashfuscator/bin/

# List help
./bashfuscator -h

# providing the command we want to obfuscate with the -c flag
./bashfuscator -c 'cat /etc/passwd'

# You can copy the obfuscated payload to your clipboard with --clip, or write it to a file with -o.
./bashfuscator -c 'cat /etc/passwd' -o file.sh

# The -s and -t options control the added size and execution time of the obfuscated payload respectively. They both default to 2, but can be set to 1-3 to control the generated payload more closely. The higher the -s or -t options, the greater the variety of the payload, at the expense of added size. 
./bashfuscator -c 'cat /etc/passwd' -s 1 -t 1 --no-mangling --layers 1

# You should make sure the obfuscated payload works as expected, and the –test option will make that easier. When used, –test will invoke the obfuscated payload in memory, and show the output.
./bashfuscator -c "cat /etc/passwd" --test
```

