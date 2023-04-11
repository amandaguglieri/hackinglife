---
title: CUPP - Common User Password Profiler
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - enumeration
  - tools
  - dictionary
  - dictionary generator
---

# CUPP - Common User Password Profiler

This **Common User Password Profiler** tool (CUPP) generates a dictionary based on the input that you introduce when asked for names, dates, places... 

## Installation

Github repo: [https://github.com/Mebus/cupp](https://github.com/Mebus/cupp).

## Basic commands

```
python cupp.py <flag options>
#    -i      Interactive questions for user password profiling
#    -w      Use this option to profile existing dictionary, or WyD.pl output to make some pwnsauce :)
#    -l      Download huge wordlists from repository
#    -a      Parse default usernames and passwords directly from Alecto DB. Project Alecto uses purified databases of Phenoelit and CIRT which where merged and enhanced.
#    -v      Version of the program
```

