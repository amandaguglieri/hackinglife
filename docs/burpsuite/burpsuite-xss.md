---
title: BurpSuite Labs - Cross-site Scripting
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting, burpsuite, xss
---

# BurpSuite Labs - Cross-site Scripting


## Reflected XSS into HTML context with nothing encoded

### Enuntiation

This lab contains a simple [reflected cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/reflected) vulnerability in the search functionality.

To solve the lab, perform a cross-site scripting attack that calls the `alert` function.

### Solution

Copy and paste the following into the search box: 
 
```
<script>alert(1)</script>
```

Click Search.

## Stored XSS into HTML context with nothing encoded

### Enuntiation

This lab contains a [stored cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/stored) vulnerability in the comment functionality.

To solve this lab, submit a comment that calls the `alert` function when the blog post is viewed.

### Solution

Go to a post, and in the comment box enter:

```
<script>alert(1)</script>
```

Once you go back to the post, the script will be load.

