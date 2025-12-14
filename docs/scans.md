---
title: scans
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active directory
---

# Scans
## IP

### Linux

```shell-session
for i in {1..254} ;do (ping -c 1 172.16.139.$i | grep "bytes from" &) ;done
```

Another way:

```bash
for i in $(seq 1 254); do host 172.16.5.$i; done | grep -v "not found"
```


### PowerShell


```powershell-session
1..254 | % {"172.16.9.$($_): $(Test-Connection -count 1 -comp 172.16.9.$($_) -quiet)"}

1..254 | % {"172.16.6.$($_): $(Test-Connection -count 1 -comp 172.16.6.$($_) -quiet)"}


1..100 | % {"172.16.9.$($_): $(Test-Connection -count 1 -comp 172.16.9.$($_) -quiet)"}
```


## Ports

### Linux

TCP

```bash
nc -nvv -w 1 -z 192.168.50.152 3388-3390
```

UDP 

```bash
nc -nv -u -z -w 1 192.168.50.149 120-123
```

### Powershell:

```powershell
foreach ($ports in 1..1024) {If (($a=Test-NetConnection 10.10.12.123 -Port $port -WarningAction SilentlyContinue).tcpTestSucceeded -eq $true){ "TCP port $port is open}}
```


```powershell
Test-NetConnection -Port 445 192.168.50.151
```

```Powershell
1..1024 | % {echo ((New-Object Net.Sockets.TcpClient).Connect("192.168.50.151", $_)) "TCP port $_ is open"} 2>$null
```

