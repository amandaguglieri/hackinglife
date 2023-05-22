---
title: Packet manager
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - bash
---

# Package Manager (APT)

```bash
# Search for a package or text string:
apt search <text_string>

# Show package information:
apt show <package>

# Show package dependencies:
apt depends <package>

# Show the names of all the packages installed in the system:
apt list --installed

# Install a package:
apt install <package>

# Uninstall a package:
apt remove <package>

# Delete a package including its configuration files:
apt purge <package>

# Delete automatically those packages that are not being used (be careful with this command, due to apt's hell dependency it may delete unwanted packages):
apt autoremove

# Update the repositories information:
apt update

# Update a package to the last available version in the repository:
apt upgrade <package>

# Update the full distribution. It will update our system to the next available version:
apt upgrade -y

# Clean caches, downloaded packages, etc:
apt clean && apt autoclean

```
