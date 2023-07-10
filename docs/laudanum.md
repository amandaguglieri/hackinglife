---
title: Laudanum - Injectable Web Exploit Code 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
  - web shells
---


# Laudanum: Injectable Web Exploit Code 

Laudanum is a repository of ready-made files that can be used to inject onto a victim and receive back access via a reverse shell, run commands on the victim host right from the browser, and more. The repo includes injectable files for many different web application languages to include asp, aspx, jsp, php, and more. 

## Installation

Pre-built in Kali.

Download from github repo: [https://github.com/jbarcia/Web-Shells/tree/master/laudanum](https://github.com/jbarcia/Web-Shells/tree/master/laudanum).


## Basic usage

The Laudanum files can be found in the /usr/share/webshells/laudanum directory. For most of the files within Laudanum, you can copy them as-is and place them where you need them on the victim to run. For specific files such as the shells, you must edit the file first to insert your attacking host IP address

```bash
locate laudanum
```
