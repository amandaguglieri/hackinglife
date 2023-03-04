---
title: API authentication attacks
author: amandaguglieri
draft: false
TableOfContents: true
---

# Proxies

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


## Setting up mitm_relay with Burpsuite

In DVTA we will configure the server to the IP of the local machine. In my lab set up my IP was 10.0.2.15.

In FTP, we will configure the listening port to 2111. Also we will disable IP check for this lab setup to work.

From [https://github.com/jrmdev/mitm_relay](https://github.com/jrmdev/mitm_relay):

![graphic](img/tca-39.png)


This is what we're doing:

![graphic](img/tca-38.png)

**1.** DVTA application sends traffic to port 21, so to intercept it we configure MITM_relay to be listening on port 21.

**2.** mitm_relay encapsulates the application traffic )no matter the protocol, into HTTP protocol so BurpSuite can read it

**3.** Burp Suite will read the traffic. And we can tamper here our code.

**4.** mitm_relay will "unfunnel" the traffic from the HTPP protocol into the raw one

**5.** In a lab setup FTP server will be in the same network, so to not get in conflict with mitm_relay we will modify FTP listen port to 2111. In real life this change is not necessary


Running mitm_relay:

```
python mitm_relay.py -l 0.0.0.0 -r tcp:21:10.0.2.15:2111 -p 127.0.0.1:8080
# -l listening address for mitm_relay (0.0.0.0 means we all listening in all interfaces)
# -r relay configuration: <protocol>:<listeningPort>:<IPofDestinationserver>:<listeningPortonDestinationServer>
# -p Proxy configuration: <IPofProxy>:<portOfProxy> 
```

![graphic](img/tca-36.png)

And this is how the interception looks like:

![graphic](img/tca-37.png)

