---
title: The Harvester - A tool for pasive and active reconnaissance
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - reconnaissance
  - tools
---

# The Harvester - A tool for pasive and active reconnaissance

[The Harvester](https://github.com/laramies/theHarvester): simple-to-use yet powerful and effective tool for early-stage penetration testing and red team engagements. We can use it to gather information to help identify a company's attack surface. The tool collects `emails`, `names`, `subdomains`, `IP addresses`, and `URLs` from various public data sources for passive information gathering. It has modules. 

Automate the modules we want to launch:

**1.** Create a list of sources, one per line, sources.txt.

**2.** Execute:

```bash
 cat sources.txt | while read source; do theHarvester -d "${TARGET}" -b $source -f "${source}_${TARGET}";done
```

**3.** When the process finishes, extract all the subdomains found and sort them:

```bash
cat *.json | jq -r '.hosts[]' 2>/dev/null | cut -d':' -f 1 | sort -u > "${TARGET}_theHarvester.txt"
```

**4.** Merge all the passive reconnaissance files:

```shell-session
cat facebook.com_*.txt | sort -u > facebook.com_subdomains_passive.txt
$ cat facebook.com_subdomains_passive.txt | wc -l
```
