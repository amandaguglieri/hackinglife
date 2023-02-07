---
title: API authentication attacks
author: amandaguglieri
draft: false
TableOfContents: true
---

# Proxies

## Setting up BurpSuite with Firefox


## Setting up Postman with Firefox


## Setting up Postman with BurpSuite

1 - Postman > Settings 

![Captura](img/postman1.png)

2 - Proxy tab. Check: 

- Use the system proxy
- Add a custom proxy configuration 
- HTTP 
- HTTPS 
- 127.0.0.1
- 8080

![Captura](img/postman2.png)

3 -  BurpSuite. Settup proxy listener

![Captura](img/postman3.png)

4 - Burp Suite. Intercept mode on

![Captura](img/postman4.png)

5 - Postman. Send the interesting request from your collection

![Captura](img/postman5.png)

6 - Your BurpSuite will intercept that traffic. Now you can send it to Intruder, Repeater, Sequencer...

![Captura](img/postman6.png)