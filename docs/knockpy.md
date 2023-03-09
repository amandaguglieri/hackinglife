---
title: knockpy - A subdomain scanner
draft: false
TableOfContents: true
tag: pentesting, web pentesting, enumeration
---

# knockpy - A subdomain scanner

## Installation

Repository:  https://github.com/guelfoweb/knock

```bash
git clone https://github.com/guelfoweb/knock.git
cd knock
pip3 install -r requirements.txt
 
# Optional: Make an alias for knockpy
sudo chmod +x knockpy.py 
sudo ln -s /home/kali/tools/knock/knockpy.py /usr/bin/knockpy

```


## Usage

```bash
# From the tools/knock folder
python3 knockpy.py <DOMAIN>

# If you have made an alias, just run:
knockpy <domain>
```
