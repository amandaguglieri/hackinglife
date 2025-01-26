---
title: CPTS labs - 02 Network Enumeration with nmap
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - certification
  - CPTS
  - labs
---
# CPTS labs - 02 Network Enumeration with nmap

## [Network Enumeration with Nmap](https://academy.hackthebox.com/module/details/19)

### Host Enumeration

#### [Host Discovery](https://academy.hackthebox.com/module/19/section/101)

**Based on the last result, find out which operating system it belongs to. Submit the name of the operating system as result.**


```
sudo nmap $ip -sn -oA host -PE --packet-trace --disable-arp-ping 
```

**Result**: Windows

#### [Host and Port Scanning](https://academy.hackthebox.com/module/19/section/102)


**Find all TCP ports on your target. Submit the total number of found TCP ports as the answer.**

```
nmap $ip
```

**Results**: 7


**Enumerate the hostname of your target and submit it as the answer. (case-sensitive):**

```
sudo nmap $ip -Pn -sC -sV -p22,80,110,139,143,445,31337
```

**Results**: nix-nmap-default


#### [Saving the Results](https://academy.hackthebox.com/module/19/section/104)

 Perform a full TCP port scan on your target and create an HTML report. Submit the number of the highest port as the answer.

```
nmap $ip
```

Results: 31337


#### [Service Enumeration](https://academy.hackthebox.com/module/19/section/103)

Enumerate all ports and their services. One of the services contains the flag you have to submit as the answer.

```
sudo nmap $ip -Pn -sC -sV -p22,80,110,139,143,445,31337
```

Results: HTB{pr0F7pDv3r510nb4nn3r}


#### [Nmap Scripting Engine](https://academy.hackthebox.com/module/19/section/108)

**Use NSE and its scripts to find the flag that one of the services contain and submit it as the answer.**

```
sudo nmap $ip -p80 --script vuln
```

Result:

```
Pre-scan script results:
| broadcast-avahi-dos: 
|   Discovered hosts:
|     224.0.0.251
|   After NULL UDP avahi packet DoS (CVE-2011-1002).
|_  Hosts are all up (not vulnerable).
Nmap scan report for 10.129.68.164
Host is up (0.047s latency).

PORT   STATE SERVICE
80/tcp open  http
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-enum: 
|_  /robots.txt: Robots file
```

Go to robots.txt and get the flag.

Results: HTB{873nniuc71bu6usbs1i96as6dsv26}


### Bypass Security Measures


#### [Firewall and IDS/IPS Evasion - Easy Lab](https://academy.hackthebox.com/module/19/section/117)

Our client wants to know if we can identify which operating system their provided machine is running on. Submit the OS name as the answer.

```
sudo nmap -sC -sV $ip -p80  -Pn --max-retries 3 --initial-rtt-timeout 50ms --max-rtt-timeout 100ms
```

Results: Ubuntu



#### [Firewall and IDS/IPS Evasion - Medium Lab](https://academy.hackthebox.com/module/19/section/118)

After the configurations are transferred to the system, our client wants to know if it is possible to find out our target's DNS server version. Submit the DNS server version of the target as the answer.

```
sudo nmap -sU -p53 --script dns-nsid $ip 
```

Results: HTB{GoTtgUnyze9Psw4vGjcuMpHRp}


#### [Firewall and IDS/IPS Evasion - Hard Lab](https://academy.hackthebox.com/module/19/section/119)

 Now our client wants to know if it is possible to find out the version of the running services. Identify the version of service our client was talking about and submit the flag as the answer.

```
sudo nc -nv -p 53 $ip  50000 
```


Results: HTB{kjnsdf2n982n1827eh76238s98di1w6}

