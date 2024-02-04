---
title: HTTrack - A tool for mirrowing sites
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - reconnaissance
  - scanning
  - passiverecon
---

# HTTrack - A tool for mirrowing sites

HTTrack is a free (GPL, libre/free software) offline browser utility that allows you to download a World Wide Web site from the Internet to a local directory, building recursively all directories, getting HTML, images, and other files from the server to your computer. 

HTTrack arranges the original site's relative link-structure. Simply open a page of the "mirrored" website in your browser, and you can browse the site from link to link, as if you were viewing it online. HTTrack can also update an existing mirrored site, and resume interrupted downloads. HTTrack is fully configurable, and has an integrated help system.



## Installation

Link to the project: [https://www.httrack.com/](https://www.httrack.com/).

```
sudo apt-get install httrack
```

## Basic usage

Create a folder for replicating in it your target.

```
mkdir targetsite
httrack domain.com  targetsite/
```

Interactive mode:

```
httrack
```


