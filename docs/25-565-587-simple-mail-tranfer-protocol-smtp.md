---
title: Ports 25, 565, 587 - Simple Mail Tranfer Protocol (SMTP)
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - port 25
  - port 465
  - port 587
  - SMTP
  - Simple Mail Transfer Protocol
---

# Ports 25, 565, 587 - Simple Mail Tranfer Protocol (SMTP)


The Simple Mail Transfer Protocol (SMTP) is a protocol for sending emails in an IP network. By default, SMTP servers accept connection requests on port 25. However, newer SMTP servers also use other ports such as TCP port 587. This port is used to receive mail from authenticated users/servers, usually using the STARTTLS command. SMTP works unencrypted without further measures and transmits all commands, data, or authentication information in plain text. To prevent unauthorized reading of data, the SMTP is used in conjunction with SSL/TLS encryption. Under certain circumstances, a server uses a port other than the standard TCP port 25 for the encrypted connection, for example, TCP port 465.

![SMTP. Source: https://wiki.inf.ufpr.br/maziero/doku.php?id=espec:servico_de_e-mail](img/smtp.gif)


`Mail User Agent` (`MUA`): SMTP client who sends the email. MUA converts it into a  header and a body and uploads both to the SMTP server. 

`Mail Submission Agent` (`MSA`), which checks the validity, i.e., the origin of the e-mail. This `MSA` is also called `Relay` server. These are very important later on, as the so-called `Open Relay Attack`.

`Mail Transfer Agent` (`MTA`):  The MTA checks the e-mail for size and spam and then stores it. At this point of the process, this MTA works as the sender's server. The MTA then searches the DNS for the IP address of the recipient mail server. On arrival at the destination SMTP server, the receiver's MTA reassembles the data packets to form a complete e-mail.

`Mail Submission Agent` (`MSA`): Proxy that occasionally precedes the MTA to relieve the load. It checks the validity, i.e., the origin of the e-mail. This `MSA` is also called `Relay` server.  

`Mail delivery agent` (`MDA`): It deals with transferring the email to the recipient's mailbox.

>Other concepts:
>
> - [DKIM](http://dkim.org/) : DomainKeys Identified Mail (DKIM)  provides a method for validating a domain name identity that is associated with a message through cryptographic authentication. The identity is independent of other email identities, such as the author's From: field.
> - [Sender Policy Framework](https://dmarcian.com/what-is-spf/) (`SPF`): Sender Policy Framework (SPF) is used to authenticate the sender of an email. With an SPF record in place, Internet Service Providers can verify that a mail server is authorized to send email for a specific domain. An SPF record is a DNS TXT record containing a list of the IP addresses that are allowed to send email on behalf of your domain.


## Extended SMTP (ESMTP)

Extended SMTP (ESMTP) deals with the main two shortcomings of SMTP protocol: 

- In SMTP, users are not authenticated, therefore the sender is unreliable.
- SMTP doesn't have confirmations.

For this, ESMTP uses TLS for encryption and [AUTH PLAIN](https://www.samlogic.net/articles/smtp-commands-reference-auth.htm) extension for authentication. See also [Postfix](postfix.md)

## Basic commands


```shell-session
# We can use telnet protocol to connect to a SMTP server
telnet $ip 25

# AUTH is a service extension used to authenticate the client
AUTH PLAIN 	

# The client logs in with its computer name and thus starts the session. It also lists all available commands
EHLO
	# Example: 
	# HELO mail1.inlanefreight.htb

# The client names the email sender
MAIL FROM 	

# The client names the email recipient
RCPT TO

# The client initiates the transmission of the email
DATA 

# The client aborts the initiated transmission but keeps the connection between client and server
RSET

# The client checks if a mailbox is available for message transfer. This also means that this command could  be used to enumerate existing users on the system. However, this does not always work. Depending on how the SMTP server is configured, the SMTP server may issue `code 252` and confirm the existence of a user that does not exist on the system.
VRFY
# Example: VRFY root

# The client also checks if a mailbox is available for messaging with this command 
EXPN

# The client requests a response from the server to prevent disconnection due to time-out
NOOP

# The client terminates the session
QUIT
```

If we are connected to a proxy and we want this proxy to connect to a SMTP server, the command that we would send than would look something like this: 

```bash 
CONNECT 10.129.14.128:25 HTTP/1.0
```


Example:

```bash
telnet $ip 25  

# Trying 10.129.14.128... ç
# Connected to 10.129.14.128. 
# Escape character is '^]'. 
# 220 ESMTP Server   

EHLO inlanefreight.htb  
# 250-mail1.inlanefreight.htb 
# 250-PIPELINING 
# 250-SIZE 10240000 
# 250-ETRN 
# 250-ENHANCEDSTATUSCODES 
# 250-8BITMIME 
# 250-DSN 
# 250-SMTPUTF8 
# 250 CHUNKING   

MAIL FROM: <cry0l1t3@inlanefreight.htb>  
# 250 2.1.0 Ok   

RCPT TO: <mrb3n@inlanefreight.htb> NOTIFY=success,failure  
# 250 2.1.5 Ok   

DATA  
# 354 End data with <CR><LF>.<CR><LF>  

# From: <cry0l1t3@inlanefreight.htb> 
# To: <mrb3n@inlanefreight.htb> 
# Subject: DB 
# Date: Tue, 28 Sept 2021 16:32:51 +0200 

`Hey man, I am trying to access our XY-DB but the creds dont work.  Did you make any changes there?.`  
# 250 2.0.0 Ok: queued as 6E1CF1681AB   

QUIT  
# 221 2.0.0 Bye Connection closed by foreign host.`
```

```shell-session
mynetworks = 0.0.0.0/0
```

With this setting, this SMTP server can send fake emails and thus initialize communication between multiple parties. Another attack possibility would be to spoof the email and read it.

## Footprinting SMTP

```shell-session
sudo nmap $ip -sC -sV -p25

sudo nmap $ip -p25 --script smtp-open-relay -v
```

**Scripts for user enumeration**:

```bash
# Enumerate users:
for user in $(cat users.txt); do echo VRFY $user | nc -nv -w 6 $ip 25  ; done
# -w: Include a delay in passing the argument. In seconds.
```

Results from script in user enumeration:

```
(UNKNOWN) [10.129.16.141] 25 (smtp) open
220 InFreight ESMTP v2.11
252 2.0.0 root
(UNKNOWN) [10.129.16.141] 25 (smtp) open
220 InFreight ESMTP v2.11
550 5.1.1 <lala>: Recipient address rejected: User unknown in local recipient table
(UNKNOWN) [10.129.16.141] 25 (smtp) open
220 InFreight ESMTP v2.11
550 5.1.1 <admin>: Recipient address rejected: User unknown in local recipient table
(UNKNOWN) [10.129.16.141] 25 (smtp) open
220 InFreight ESMTP v2.11
252 2.0.0 robin                 
```



## Postfix, an example of a SMTP server

### Configuration file

[See how to install postfix server](postfix.md).

The configuration file for Porsfix service is `/etc/postfix/main.cf`

