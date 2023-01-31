---
title: python
author: amandaguglieri
draft: false
TableOfContents: true
tag:
---

# python


## Installing python 3.8 on Ubuntu 20.04.5

First, update and upgrade:

```bash
sudo apt update && sudo apt upgrade
```

Add PPA for Python old versions. The old versions of Python such as 3.9, 3.8, 3.7, and older are not available to install using the default system repository of Ubuntu 22.04 LTS Jammy JellyFish or 20.04 Focal Fossa. Hence, we need to add a PPA offered by the “deadsnakes” team to get the old archived Python versions easily.

```bash
sudo apt install software-properties-common
```

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
```

Check python versions you want. Syntax:

```
sudo apt-cache policy python<version>
```

In my case:

```bash
sudo apt-cache policy python3.9
```

Install the version you want:

```bash
sudo apt install python3.9
```

Set up a default version in your system:

```bash
# Checkout existing versions
ls /usr/bin/python*

# Also, let's check out  whether any version is configured as python alternatives or not. For that run:
sudo update-alternatives --list python

# If the output is: “update-alternatives: error: no alternatives for python”. Then it means there are no alternatives that have been configured, hence let’s do some:
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.9 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.10 2
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 3

# Switch the default Python version 
sudo update-alternatives --config python
```

