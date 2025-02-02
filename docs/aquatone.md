---
title: Aquatone - Automatize web scanner in large subdomain lists
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
  - enumeration
---

# Aquatone - Automatize web scanner in large subdomain lists

[Aquatone](https://github.com/michenriksen/aquatone) is a tool for automatic and visual inspection of websites across many hosts and is convenient for quickly gaining an overview of HTTP-based attack surfaces by scanning a list of configurable ports, visiting the website with a headless Chrome browser, and taking a screenshot. This is helpful, especially when dealing with huge subdomain lists.

```bash
wget https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip

unzip aquatone_linux_amd64_1.7.0.zip 

# We can move it to a location in our $PATH such as /usr/local/bin to be able to call the tool from anywhere
sudo mv aquatone /usr/local/bin
```

## Basic usage

```bash
cat example_of_list.txt | aquatone -out ./aquatone -screenshot-timeout 1000
```