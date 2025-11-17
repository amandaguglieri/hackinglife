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

!!! tip "Related resources"
	- [POP3/IMAP4 protocol](110-143-993-995-imap-pop3.md)


The Simple Mail Transfer Protocol (SMTP) is a protocol for sending emails in an IP network. By default, SMTP servers accept connection requests on port 25. However, newer SMTP servers also use other ports such as TCP port 587. This port is used to receive mail from authenticated users/servers, usually using the STARTTLS command. SMTP works unencrypted without further measures and transmits all commands, data, or authentication information in plain text. To prevent unauthorized reading of data, the SMTP is used in conjunction with SSL/TLS encryption. Under certain circumstances, a server uses a port other than the standard TCP port 25 for the encrypted connection, for example, TCP port 465.

![SMTP. Source: https://wiki.inf.ufpr.br/maziero/doku.php?id=espec:servico_de_e-mail](img/smtp.gif)


`Mail User Agent` (`MUA`): SMTP client who sends the email. MUA converts it into a  header and a body and uploads both to the SMTP server. 

`Mail Submission Agent` (`MSA`), which checks the validity, i.e., the origin of the e-mail. This `MSA` is also called `Relay` server. These are very important later on, as the so-called `Open Relay Attack`. Proxy that occasionally precedes the MTA to relieve the load. It checks the validity, i.e., the origin of the e-mail. This `MSA` is also called `Relay` server.  


`Mail Transfer Agent` (`MTA`):  The MTA checks the e-mail for size and spam and then stores it. At this point of the process, this MTA works as the sender's server. The MTA then searches the DNS for the IP address of the recipient mail server. On arrival at the destination SMTP server, the receiver's MTA reassembles the data packets to form a complete e-mail.

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

MAIL FROM: <cry0l1t3inlanefreight.htb>  
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

| **Port**  | **Service**                                                                |
| --------- | -------------------------------------------------------------------------- |
| `TCP/25`  | SMTP Unencrypted                                                           |
| `TCP/143` | IMAP4 Unencrypted                                                          |
| `TCP/110` | POP3 Unencrypted                                                           |
| `TCP/465` | SMTP Encrypted                                                             |
| `TCP/587` | SMTP Encrypted/[STARTTLS](https://en.wikipedia.org/wiki/Opportunistic_TLS) |
| `TCP/993` | IMAP4 Encrypted                                                            |
| `TCP/995` | POP3 Encrypted                                                             |


## Enumeration

When it comes to enumeration it is critical to understand if we are facing a cloud service or a custom mail server implementation. 


### Custom mail server implementation

We will focus on typical misconfigurations

#### User enumeration with commands

The SMTP server has different commands that can be used to enumerate valid usernames `VRFY`, `EXPN`, and `RCPT TO`. If we successfully enumerate valid usernames, we can attempt to password spray, brute-forcing, or guess a valid password.
##### VRFY 

First we try to connect to the server. From linux:

```bash
telnet $ip 25
```

From Windows with Powershell:

```
Test-NetConnection -Port 25 $ip

# If Test-NetConnection cannot fully interact with SMTP, we can install the Microsoft version of the Telnet client with:
dism /online /Enable-Feature /Feature-Name:TelnetClient
# installing Telnet requires administrative privileges

# Alternative, grab the Telnet binary located on another development machine of ours at c:\windows\system32\telnet.exe and transfer it to the Windows machine we are testing from.
```


If anonymous login is enabled, we are in. Otherwise we could try to login, for instance with user `root`:

```
VRFY root
```

The code 252 in the answer means that the user exists. The code 550 means that it is an unknown user. 

##### EXPN 

`EXPN` is similar to `VRFY`, except that when used with a distribution list. 
First we try to connect to the server:

```bash
telnet $ip 25
```

Then we try to list all users on that distribution list with EXPN:

```shell-session
EXPN support-team
```

A typical response could be:

```shell-session
250 2.0.0 carol@inlanefreight.htb
250 2.1.5 elisa@inlanefreight.htb
```

##### RCPT TO Command

`RCPT TO` identifies the recipient of the email message. This command can be repeated multiple times for a given message to deliver a single message to multiple recipients.

First we try to connect to the server:

```bash
telnet $ip 25
```

Then we attempt the `RCPT TO` command:

```shell-session
MAIL FROM:test@htb.com
it is
250 2.1.0 test@htb.com... Sender ok


RCPT TO:julio

550 5.1.1 julio... User unknown


RCPT TO:kate

550 5.1.1 kate... User unknown


RCPT TO:john

250 2.1.5 john... Recipient ok
```

##### USER

We can also use the `POP3` protocol to enumerate users depending on the service implementation. For example, we can use the command `USER` followed by the username, and if the server responds `OK`. This means that the user exists on the server. First we try to connect to the server:

```bash
telnet $ip 25
```

Then we attempt the `USER` command:

```shell-session
USER julio
-ERR


USER john
+OK
```


#### User enumeration with commands

A way to automate this enumeration is this **script for user enumeration**:

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

We may also use this python script:

```python
#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 3:
        print("Usage: vrfy.py <username> <target_ip>")
        sys.exit(0)

# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Server
ip = sys.argv[2]
connect = s.connect((ip,25))

# Receive the banner
banner = s.recv(1024)

print(banner)

# VRFY a user
user = (sys.argv[1]).encode()
s.send(b'VRFY ' + user + b'\r\n')
result = s.recv(1024)

print(result)

# Close the socket
s.close()
```

```bash
# Run the above script smtp.py with:
python3 smtp.py root 192.168.50.8
```


#### smtp-user-enum

Username guessing tool primarily for use against the default Solaris SMTP service. Can use either EXPN, VRFY or RCPT TO.

Repo: [https://github.com/pentestmonkey/smtp-user-enum](https://github.com/pentestmonkey/smtp-user-enum)

Basic usage:

```shell-session
# Go to ~/tools/smtp-user-enum
./smtp-user-enum.pl -M RCPT -U userlist.txt -D inlanefreight.htb -t $ip
# -M: Enumeration mode, it can be `VRFY`, `EXPN`, or `RCPT`
# -U: file with list of users
# -D: domain
# -t: target
```

**Enumerating from Windows?** Test-NetConnection can not perform VRFY connections on port 25. We may try with telnet if installed. If installed we can enable it with:

```powershell
dism /online /Enable-feature /FeatureName:TelnetClient
```

And now, perform enumeration:

```powershell
telnet $ip 25
VRFY root
```

Otherwise, installing telnet requires administrator permissions.

### Cloud mail server implementation

#### Enumerating users in Microsoft Office 365 (O365)

##### O365spray

[O365spray](o365spray.md) is a username enumeration and password spraying tool aimed at Microsoft Office 365 (O365). This tool reimplements a collection of enumeration and spray techniques.

```
sudo pip install -r requirements.txt
```

Basic usage:

```shell-session
# First validate if our target domain is using Office 365.
python3 o365spray.py --validate --domain msexample.com

# Attempt to identify usernames.
python3 o365spray.py --enum -U users.txt --domain msexample.com

```


## Password Attacks

### Custom mail servers
#### hydra

```shell-session
# Attacking a pop3 service
hydra -L users.txt -p 'Company01!' -f $ip pop3

hydra -l user@inlanefreight.htb -P passwords.list -t 64 -f $ip smtp
```


### Cloud mail services

If cloud services support SMTP, POP3, or IMAP4 protocols, we may be able to attempt to perform password spray using tools like `Hydra`, but these tools are usually blocked.

#### MSOffice 365

##### O365spray

See [O365spray](o365spray.md)

```shell-session
# First validate if our target domain is using Office 365.
python3 o365spray.py --validate --domain msexample.com

# Password spraying technique 
python3 o365spray.py --spray -U usersfound.txt -p 'March2022!' --count 1 --lockout 1 --domain msexample.com
```

##### MailSniper

See [MailSniper](mailsniper.md)

#### Gmail and Okta

 [CredKing](https://github.com/ustayready/CredKing)

## Open relay attack

An open relay is a Simple Mail Transfer Protocol (`SMTP`) server, which is improperly configured and allows an unauthenticated email relay.

First, identify if an SMTP port allows an open relay:

```shell-session
nmap -p25 -Pn --script smtp-open-relay $ip
```

Next, we can use any mail client to connect to the mail server and send our email.

```shell-session
swaks --from notifications@inlanefreight.com --to employees@inlanefreight.com --header 'Subject: Company Notification' --body 'Hi All, we want to hear from you! Please complete the following survey. http://mycustomphishinglink.com/' --server $ipSMTPServerVictim
```

See [swaks](swaks.md).

## Attacks on SMTPD

**Affected version**:  [OpenSMTPD](https://www.opensmtpd.org/) up to version 6.6.2
**Vulnerability**: [CVE-2020-7247](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-7247) and leads to RCE.

The vulnerability in this service lies in the program's code, namely in the function that records the sender's email address. This offers the possibility of escaping the function using a semicolon (`;`) and making the system execute arbitrary shell commands. However, there is a limit of 64 characters, which can be inserted as a command. The technical details of this vulnerability can be found [here](https://www.openwall.com/lists/oss-security/2020/01/28/3). Exploit [here](https://www.exploit-db.com/exploits/47984)

## Postfix, an example of a SMTP server

### Configuration file

[See how to install postfix server](postfix.md).

The configuration file for Porsfix service is `/etc/postfix/main.cf`

