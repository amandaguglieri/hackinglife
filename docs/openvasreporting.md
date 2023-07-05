---
title: openVAS Reporting
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - reconnaissance
  - scanner
  - vulnerability assessment
  - reporting
---

# openVAS Reporting


## Installation

Download from github repo: [https://github.com/TheGroundZero/openvasreporting](https://github.com/TheGroundZero/openvasreporting).


```bash
# Install Python3 and pip3 before.

# Clone git repository
git clone https://github.com/TheGroundZero/openvasreporting.git

# Install required python packages
cd openvasreporting
pip3 install pip --upgrade
pip3 install build --upgrade
python -m build

# Install module
pip3 install dist/OpenVAS_Reporting-X.x.x-py3-xxxx-xxx.whl
```

Alternative with pip3

```bash
# Install Python3 and pip3
apt(-get) install python3 python3-pip # Debian

# Install the package
pip3 install OpenVAS-Reporting
```


## Basic usage

```bash
python3 -m openvasreporting -i report-2bf466b5-627d-4659-bea6-1758b43235b1.xml -f xlsx
```
