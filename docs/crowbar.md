---
title: Crowbar
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - brute
  - forcing
  - windows
  - passwords
---
# Crowbar

**Crowbar** _(formally known as Levye)_ is a brute forcing tool that can be used during penetration tests. It was developed to brute force some protocols in a different manner according to other popular brute forcing tools.

## Installation

Repo: [https://github.com/galkan/crowbar](https://github.com/galkan/crowbar)

```
git clone https://github.com/galkan/crowbar
cd crowbar/
pip3 install -r requirements.txt
```

## Basic commands

```bash
crowbar -b rdp -s $ip/32 -U users.txt -c 'password123'
```
