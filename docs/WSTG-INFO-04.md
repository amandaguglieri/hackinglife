---
title: Enumerate Applications on Webserver - OWASP Web Security Testing Guide
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web
  - pentesting
  - reconnaissance
  - WSTG-INFO-04
---

# Enumerate Applications on Webserver

!!! quote ""
	[OWASP Web Security Testing Guide 4.2](web-security-testing-guide.md) > 1. Information Gathering > 1.4. Enumerate Applications on Webserver

|ID|Link to Hackinglife|Link to OWASP|Objectives|
|:---|:---|:---|:---|
|1.4|[WSTG-INFO-04](WSTG-INFO-04.md)|[Enumerate Applications on Webserver](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/04-Enumerate_Applications_on_Webserver)|- Enumerate the applications within the scope that exist on a web server.  - Find applications hosted in the webserver (Virtual hosts/Subdomain), non-standard ports, DNS zone transfers|

Web application discovery is a process aimed at identifying web applications on a given infrastructure:

## 1. Different based URL

https://example.com/application1  and https://example.com/application2

### google dork

If these applications are indexed, try this google dork:

```
site:example.com
```

### gobuster 

[gobuster Cheat sheet](gobuster.md).

Brute force directory discovery but it's not recursive (you need to specify a directory to perform a deeper scanner). 

```bash
gobuster dir -u <exact target url> -w </path/dic.txt> --wildcard -b 401
# -b flag is to exclude from results an specific http response
```


### More tools

|  Tool + Cheat sheet | URL | 
| ------------------ | --- |
| [dirb](dirb.md) | DIRB is a **web content** fingerprinting tool. It scans the web server for directories using a dictionary file | 
| [feroxbuster](feroxbuster.md) | FEROXBUSTER is a **web content** fingerprintinf tool that uses brute force combined with a wordlist to search for unlinked content in target directories. |
| [httprint](httprint.md) | HTTPRINT is a **web server** fingerprinting tool. It identifies web servers and detects web enabled devices which do not have a server banner string, such as wireless access points, routers, switches, cable modems, etc. | 
| [wpscan](wpscan.md) | WPSCAN is a **wordpress** security scanner. | 



## 2. Non standard ports

https://example.com:1234/  and https://example.com:8088/

```bash
nmap -Pn -sT -p0-65535 $ip
```


## 3. Virtual hosts

https://example.com/  and https://webmail.example.com/

A virtual host (`vHost`) is a feature that allows several websites to be hosted on a single server. 

There are two ways to configure virtual hosts:

- `IP`-based virtual hosting
- `Name`-based virtual hosting: The distinction for which domain the service was requested is made at the application level. For example, several domain names, such as `admin.inlanefreight.htb` and `backup.inlanefreight.htb`, can refer to the same IP. Internally on the server, these are separated and distinguished using different folders. 


### Identify name server

```bash
host -t ns example.com
```

Request a zone transfer for example.com from one of its nameservers:

```bash
host -l example.com ns1.example.com
```



### DNS enumeration

More about [DNS enumeration](53-dns.md).

**gobuster** (More complete cheat sheet: [gobuster](gobuster.md))

```shell-session
gobuster dns -d <DOMAIN (without http)> -w /usr/share/SecLists/Discovery/DNS/namelist.txt
```


**Bash script**, using Sec wordlist:

```shell-session
for sub in $(cat /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-110000.txt);do dig $sub.example.com @$ip | grep -v ';\|SOA' | sed -r '/^\s*$/d' | grep $sub | tee -a subdomains.txt;done
```


**dig** (More complete cheat sheet: [dig](dig.md))

```bash
# Get email of administrator of the domain
dig soa www.example.com
# The email will contain a (.) dot notation instead of @

# ENUMERATION
# List nameservers known for that domain
dig ns example.com @$ip
# -ns: other name servers are known in NS record
#  `@` character specifies the DNS server we want to query.

# View all available records
dig any example.com @$ip

# Display version. query a DNS server's version using a class CHAOS query and type TXT. However, this entry must exist on the DNS server.
dig CH TXT version.bind $ip
```


**nslookup** (More complete cheat sheet: [nslookup](nslookup.md))

```bash
# Query `A` records by submitting a domain name: default behaviour
nslookup $TARGET

# We can use the `-query` parameter to search specific resource records
# Querying: A Records for a Subdomain
nslookup -query=A $TARGET

# Querying: PTR Records for an IP Address
nslookup -query=PTR 31.13.92.36

# Querying: ANY Existing Records
nslookup -query=ANY $TARGET

# Querying: TXT Records
nslookup -query=TXT $TARGET

# Querying: MX Records
nslookup -query=MX $TARGET

#  Specify a nameserver if needed by adding `@<nameserver/IP>` to the command
```



**DNScan** (More complete cheat sheet: [DNScan](dnscan.md)): Python wordlist-based DNS subdomain scanner. The script will first try to perform a zone transfer using each of the target domain's nameservers.

```bash
dnscan.py (-d \<domain\> | -l \<list\>) [OPTIONS]
# Mandatory Arguments
#    -d  --domain                              Target domain; OR
#    -l  --list                                Newline separated file of domains to scan
```


### VHOST enumeration


**vHost Fuzzing**

```bash
# use a vhost dictionary file
cp /usr/share/wordlists/secLists/Discovery/DNS/namelist.txt ./vhosts

cat ./vhosts | while read vhost;do echo "\n********\nFUZZING: ${vhost}\n********";curl -s -I http://$ip -H "HOST: ${vhost}.example.com" | grep "Content-Length: ";done
```

**vHost Fuzzing with [ffuf](ffuf.md):**

```bash
# Virtual Host enumeration
# use a vhost dictionary file
cp /usr/share/wordlists/secLists/Discovery/DNS/namelist.txt ./vhosts

ffuf -w ./vhosts -u http://$ip -H "HOST: FUZZ.example.com" -fs 612
# `-w`: Path to our wordlist
# `-u`: URL we want to fuzz
# `-H "HOST: FUZZ.randomtarget.com"`: This is the `HOST` Header, and the word `FUZZ` will be used as the fuzzing point.
# `-fs 612`: Filter responses with a size of 612, default response size in this case.
```


**gobuster** (More complete cheat sheet: [gobuster](gobuster.md))


```bash
gobuster vhost -w /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u <exact target url>
# vhost : Uses VHOST for brute-forcing
# -w : Path to the wordlist
# -u : Specify the URL
```

**Wfuzz** (More complete cheat sheet: [Wfuzz](wfuzz.md):

```shell-session
wfuzz -c --hc 404 -t 200 -u https://nunchucks.htb/ -w /usr/share/dirb/wordlists/common.txt -H "Host: FUZZ.nunchucks.htb" --hl 546
# -c: Color in output
# –hc 404: Hide 404 code responses
# -t 200: Concurrent Threads
# -u http://nunchucks.htb/: Target URL
# -w /usr/share/dirb/wordlists/common.txt: Wordlist 
# -H “Host: FUZZ.nunchucks.htb”: Header. Also with "FUZZ" we indicate the injection point for payloads
# –hl 546: Filter out responses with a specific number of lines. In this case, 546
```
