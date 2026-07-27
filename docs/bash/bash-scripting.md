---
title: Bash scripting
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - bash
  - scripting
---

# Bash scripting

Fundamentals for writing and reading bash scripts. For a command reference (not scripting), see the [bash cheat sheet](../bash.md).

## Shebang and permissions

```bash
#!/usr/bin/env bash
# The shebang tells the shell which interpreter to use.
# #!/bin/bash is also common, but #!/usr/bin/env bash resolves bash from $PATH.

chmod +x script.sh
./script.sh
```

## Variables

```bash
name="offsec"
echo "$name"

# No spaces around the = sign, or bash treats it as a command.
readonly PI=3.14   # constant
unset name         # remove a variable

# Command substitution
current_user=$(whoami)
files=$(ls /tmp)
```

## Quoting

```bash
var="hello world"

echo $var    # word-splits: hello world (two args to echo)
echo "$var"  # preserves as a single string: hello world

# Single quotes disable all expansion
echo '$var'  # prints literally: $var
```

## Special variables and parameters

```bash
$0     # script name
$1..$9 # positional arguments
$#     # number of arguments
$@     # all arguments, each as a separate word
$*     # all arguments, as one word
$?     # exit code of the last command
$$     # PID of the current shell
$!     # PID of the last background job
```

## Arrays

```bash
hosts=(10.10.10.1 10.10.10.2 10.10.10.3)

echo "${hosts[0]}"     # first element
echo "${hosts[@]}"     # all elements
echo "${#hosts[@]}"    # array length

for host in "${hosts[@]}"; do
    echo "$host"
done
```

## Conditionals

```bash
if [ -f "/etc/passwd" ]; then
    echo "file exists"
elif [ -d "/etc" ]; then
    echo "it's a directory instead"
else
    echo "not found"
fi

# Common test operators
# -f  regular file exists      -d  directory exists
# -e  path exists              -r/-w/-x  readable/writable/executable
# -z  string is empty          -n  string is not empty
# -eq -ne -lt -le -gt -ge      numeric comparisons
# ==  != (string comparisons, use [[ ]] for these)

if [[ "$1" == "admin" ]]; then
    echo "welcome, admin"
fi
```

## Loops

```bash
# for loop
for i in 1 2 3; do
    echo "$i"
done

# C-style for loop
for ((i = 0; i < 5; i++)); do
    echo "$i"
done

# while loop
count=0
while [ "$count" -lt 5 ]; do
    echo "$count"
    ((count++))
done

# until loop
until ping -c 1 10.10.10.10 &>/dev/null; do
    echo "waiting for host..."
    sleep 1
done

# reading a file line by line
while IFS= read -r line; do
    echo "$line"
done < targets.txt
```

## Functions

```bash
greet() {
    local name="$1"     # local restricts scope to the function
    echo "hello, $name"
    return 0            # exit status, not a return value
}

greet "amanda"
echo "exit code: $?"

# Capturing "output" (functions don't return values, only exit codes)
result=$(greet "amanda")
```

## Command-line argument parsing with getopts

```bash
#!/usr/bin/env bash

usage() {
    echo "Usage: $0 -t <target> -p <port>"
    exit 1
}

while getopts ":t:p:h" opt; do
    case "$opt" in
        t) target="$OPTARG" ;;
        p) port="$OPTARG" ;;
        h) usage ;;
        \?) echo "Invalid option: -$OPTARG"; usage ;;
        :) echo "Option -$OPTARG requires an argument"; usage ;;
    esac
done

echo "target=$target port=$port"
```

## Exit codes and error handling

```bash
set -e          # exit immediately if a command fails
set -u          # error on unset variables
set -o pipefail # a pipeline fails if any command in it fails
set -x          # print each command before running it (debugging)

command || echo "command failed, but we continue"
command && echo "command succeeded"

trap 'echo "cleaning up..."; rm -f /tmp/scratch.$$' EXIT
```

## Input/output redirection

```bash
command > out.txt     # stdout to file (overwrite)
command >> out.txt    # stdout to file (append)
command 2> err.txt    # stderr to file
command &> all.txt    # stdout and stderr to file
command 2>&1          # redirect stderr to wherever stdout is going
command < in.txt       # stdin from file

# Discard output entirely
command &>/dev/null
```

## Debugging scripts

```bash
bash -x script.sh   # trace execution
bash -n script.sh   # syntax check only, don't run
```
