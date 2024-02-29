---
title: Installing python
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - python
  - python pentesting
  - scripting
---

# Installing python


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

# If you get this error:
AttributeError: NoneType object has no attribute people
# Try Installing  python3-launchpadlib 
sudo apt-get install  python3-launchpadlib 
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


## Other methods

No very orthodox but:

```bash
# Check current Python pointer
ls -l /usr/bin/python

# Check available Python versions**
ls -l /usr/bin/python*

# Unlink current python version**
cd /usr/bin
sudo unlink python

# Select required python version and lin to python command**
sudo ln -s /usr/bin/python2.7 python

# Confirm change in pointer**
ls -l /usr/bin/python
```



## Installing pip

```bash
python3 -m pip install pip
```

 If you get error: externally-managed-environment, then the solution is create an environment. As the message explains, _**this is actually not an issue with Python itself**_, but rather your Linux distribution (Kali, Debian, etc.) implementing a deliberate policy to ensure you don't break your operating system and system packages by using `pip` (or Poetry, Hatch, PDM or another non-OS package manager) outside the protection of a virtual environment.

## Creating a virtual environment with venv

```
python3 -m venv <DIR>
source <DIR>/bin/activate
```

Now you can activate or deactivate the virtual environment with:

```
<DIR>\Scripts\activate
```


## Creating a virtual environment with mkvirtualenv

```bash
mkvirtualenv nameOfEnv
```
