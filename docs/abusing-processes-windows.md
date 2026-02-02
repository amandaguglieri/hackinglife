---
title: Abusing processes in Windows
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - privilege
  - escalation
  - windows
---
# Abusing processes in Windows

One of the best places to look for privilege escalation is the processes that are running on the system. Even if a process is not running as an administrator, it may lead to additional privileges. The most common example is discovering a web server like IIS or XAMPP running on the box, placing an aspx/php shell on the box, and gaining a shell as the user running the web server. Generally, this is not an administrator but will often have the SeImpersonate token, allowing for Rogue/Juicy/Lonely Potato to provide SYSTEM permissions.

Display Running Processes:

```
# With Netstat
netstat -ano

# With Get-CimInstance
Get-CimInstance -ClassName win32_service | Select Name,State,PathName | Where-Object {$_.State -like 'Running'}
```

The main thing to look for with Active Network Connections are entries listening on loopback addresses (127.0.0.1 and ::1) that are not listening on the IP Address (10.129.43.8) or broadcast (0.0.0.0, ::/0).

## PowerUp

Download from PowerSploit Github repo: [https://github.com/ZeroDayLab/PowerSploit](https://github.com/ZeroDayLab/PowerSploit).

```powershell
# Import the module
Import-Module .\PowerUp.ps1

# Find services vulnerables in my machine
Invoke-AllChecks

# Exploit a vulnerable service to escalate to the more privilege user that runs that service
Invoke-ServiceAbuse -Name ‘<NAME OF THE SERVICE>’ -UserName ‘<DOMAIN CONTROLLER>\<MY CURRENT USERNAME>’
```

## Filezilla on port 14147

If we see  port `14147`, which is used for FileZilla's administrative interface, we could connect to this port, and possibly extract FTP passwords in addition to creating an FTP Share at c:\ as the FileZilla Server user (potentially Administrator).

## Splunk Universal Forwarder Hijacking: port 8089

 the `Splunk Universal Forwarder`, installed on endpoints to send logs into Splunk. The default configuration of Splunk did not have any authentication on the software and allowed anyone to deploy applications, which could lead to code execution. Again, the default configuration of Splunk was to run it as SYSTEM$ and not a low privilege user.

[See vulnerability + exploit](8089-splunk-universal-forwarder.md).


## Erlang Port  on port 25672 

Erlang is a programming language designed around distributed computing and will have a network port that allows other Erlang nodes to join the cluster. The secret to join this cluster is called a cookie. Many applications that utilize Erlang will either use a weak cookie (RabbitMQ uses `rabbit` by default) or place the cookie in a configuration file that is not well protected. Some example Erlang applications are SolarWinds, RabbitMQ, and CouchDB.

[See vulnerability + exploitation](25672-erlang-port.md).