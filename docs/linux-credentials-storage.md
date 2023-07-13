---
title: Linux credentials storage
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - linux
---

# Linux credentials storage

## Shadow file

The /etc/shadow file has a unique format in which the entries are entered and saved when new users are created.

```
htb-student: 	$y$j9T$3QSBB6CbHEu...SNIP...f8Ms: 	18955: 	0: 	99999: 	7: 	: 	: 	:
<username>: 	<encrypted password>: 	<day of last change>: 	<min age>: 	<max age>: 	<warning period>: 	<inactivity period>: 	<expiration date>: 	<reserved field>
```


The encryption of the password in this file is formatted as follows:

| | | |
|---|---|---|
|`$ <id>`|`$ <salt>`|`$ <hashed>`|
|`$ y`|`$ j9T`|`$ 3QSBB6CbHEu...SNIP...f8Ms`|


The type (`id`) is the cryptographic hash method used to encrypt the password. Many different cryptographic hash methods were used in the past and are still used by some systems today.

|**ID**|**Cryptographic Hash Algorithm**|
|---|---|
|`$1$`|[MD5](https://en.wikipedia.org/wiki/MD5)|
|`$2a$`|[Blowfish](https://en.wikipedia.org/wiki/Blowfish_(cipher))|
|`$5$`|[SHA-256](https://en.wikipedia.org/wiki/SHA-2)|
|`$6$`|[SHA-512](https://en.wikipedia.org/wiki/SHA-2)|
|`$sha1$`|[SHA1crypt](https://en.wikipedia.org/wiki/SHA-1)|
|`$y$`|[Yescrypt](https://github.com/openwall/yescrypt)|
|`$gy$`|[Gost-yescrypt](https://www.openwall.com/lists/yescrypt/2019/06/30/1)|
|`$7$`|[Scrypt](https://en.wikipedia.org/wiki/Scrypt)|

The /etc/shadow file can only be read by the user root.


## Passwd file

The /etc/passwd

```						
htb-student: 	x: 	1000: 	1000: 	,,,: 	/home/htb-student: 	/bin/bash
<username>: 	<password>: 	<uid>: 	<gid>: 	<comment>: 	<home directory>: 	<cmd executed after logging in>
```

The `x` in the password field indicates that the encrypted password is in the `/etc/shadow` file.

