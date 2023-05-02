---
title: Process Hacker tool
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - thick client application
---

# Process Hacker tool

## Usage

In the course [Pentesting thick clients applications](thick-applications/tca-introduction.md).

We will be using the portable version.

**1.** Open the application you want to test.

**2.** Open Process Hacker Tool.

**3.** Select the application, click right on "Properties".

**4.** Select tab "Memory".

**5.** Click on "Strings".

![graphic](img/tca-46.png)


**6.** Check "Image" and "Mapped" and search!

![graphic](img/tca-47.png)

**7**. In the results you can use the Filter option to search for (in this case) "data source". 

![graphic](img/tca-48.png)

Other possible searches: Decrypt.
Clear text conection string in memory reveals credentials: powned!!!

