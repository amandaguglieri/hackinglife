---
title: RFD attack - Reflected File Download
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
---

# RFD attack - Reflected File Download

**Reflected File Download** attack (RFD) combines url path segments with web services vulnerable to JSONP injection, being the goal to deliver malware to end users of the system.

## Cool proof of concept

[https://medium.com/@Johne_Jacob/rfd-reflected-file-download-what-how-6d0e6fdbe331](https://medium.com/@Johne_Jacob/rfd-reflected-file-download-what-how-6d0e6fdbe331).

Read more: [https://hackerone.com/reports/39658](https://hackerone.com/reports/39658)

## Prevention and mitigation

- "X-Content-Type-Options: nosniff" header to API response.
- 


## Tools and payloads 

- See updated chart: [Attacks and tools for web pentesting](web-security-testing-guide.md).

