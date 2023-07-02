---
title: Web enumeration
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
  - enumeration
---

# Web enumeration

Along with all these tools and techniques it is always recommendable to review:

 - Source code
 - Some typical files such as robots.txt


## Web scanner

More about [whatweb](whatweb.md).

```bash
# version of web servers, supporting frameworks, and applications
whatweb $ip
whatweb <hostname>

# Automate web application enumeration across a network.
whatweb --no-errors $ip/24
```


## Banner Grabbing / Web Server Headers

[Curl](curl.md):

```bash
curl -IL https://<TARGET>
# -I: --head (HTTP  FTP  FILE) Fetch the headers only!
# -L, --location: (HTTP) If the server reports that the requested page has moved to a different location (indicated with a Location: header and a 3XX response  code),  this  option  will make  curl  redo the request on the new place. If used together with -i, --include or -I, --head, headers from all requested pages will be shown. 
```


## Hostname discovery

```shell-session
nmap --script smb-os-discovery $ip
```



## DNS enumeration

More about [DNS enumeration](53-dns.md).

**gobuster** (More complete cheat sheet: [gobuster](gobuster.md))

```shell-session
gobuster dns -d <DOMAIN (without http)> -w /usr/share/SecLists/Discovery/DNS/namelist.txt
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



**DNScan** (More complete cheat sheet: [DNScan](dnscan.md)): Python w/ordlist-based DNS subdomain scanner. The script will first try to perform a zone transfer using each of the target domain's nameservers.

```bash
dnscan.py (-d \<domain\> | -l \<list\>) [OPTIONS]
# Mandatory Arguments
#    -d  --domain                              Target domain; OR
#    -l  --list                                Newline separated file of domains to scan
```



## Subdomain enumeration

[Gobuster](gobuster.md):

```bash
gobuster vhost -w /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u <exact target url>
# vhost : Uses VHOST for brute-forcing
# -w : Path to the wordlist
# -u : Specify the URL
```


[Wfuzz](wfuzz.md):

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

Using [dnsenum](dnsenum.md).

Bash script, using Sec wordlist:

```shell-session
for sub in $(cat /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-110000.txt);do dig $sub.example.com @$ip | grep -v ';\|SOA' | sed -r '/^\s*$/d' | grep $sub | tee -a subdomains.txt;done
```


## Passive web server enumeration

[Netcraft](https://www.netcraft.com) can offer us information about the servers without even interacting with them, and this is something valuable from a passive information gathering point of view. We can use the service by visiting `https://sitereport.netcraft.com` and entering the target domain. We need to pay special attention to the latest IPs used. Sometimes we can spot the actual IP address from the webserver before it was placed behind a load balancer, web application firewall, or IDS, allowing us to connect directly to it if the configuration.

We can access several versions of these websites using the [Wayback Machine](http://web.archive.org) to find old versions that may have interesting comments in the source code or files that should not be there.

We can also use the tool [waybackurls](https://github.com/tomnomnom/waybackurls) to inspect URLs saved by Wayback Machine and look for specific keywords. Installation:

```shell-session
go install github.com/tomnomnom/waybackurls@latest
```

Basic usage:

```shell-session
waybackurls -dates https://example.com > waybackurls.txt

cat waybackurls.txt
```


## Active web server enumeration

If we discover the webserver behind the target application, it can give us a good idea of what operating system is running on the back-end server.

For instance:

- IIS 6.0: Windows Server 2003
- IIS 7.0-8.5: Windows Server 2008 / Windows Server 2008R2
- IIS 10.0 (v1607-v1709): Windows Server 2016
- IIS 10.0 (v1809-): Windows Server 2019

Although this is usually correct when dealing with Windows, we can not be sure in the case of Linux or BSD-based distributions as they can run different web server versions

How to spot a web server?

**1. HTTP headers**:

X-Powered-By and cookies: 
- .NET: `ASPSESSIONID<RANDOM>=<COOKIE_VALUE>`
- PHP: `PHPSESSID=<COOKIE_VALUE>`
- JAVA: `JSESSION=<COOKIE_VALUE>`

**2. [whatweb](whatweb.md)**.

```bash
whatweb -a3 https://www.example.com -v
# -a3: aggression level 3
# -v: verbose mode
```

**3. Wappalyzer**

**4. [wafw00f](wafw00f.md)**:

```shell-session
wafw00f -v https://www.example.com

# -a: check all possible WAFs in place instead of stopping scanning at the first match.
# -i: read targets from an input file 
# -p proxy the requests 
```

**5. [Aquatone](aquatone.md)

```bash
cat example_of_list.txt | aquatone -out ./aquatone -screenshot-timeout 1000
```


## VHOST enumeration

A virtual host (`vHost`) is a feature that allows several websites to be hosted on a single server. 

There are two ways to configure virtual hosts:

- `IP`-based virtual hosting
- `Name`-based virtual hosting: The distinction for which domain the service was requested is made at the application level. For example, several domain names, such as `admin.inlanefreight.htb` and `backup.inlanefreight.htb`, can refer to the same IP. Internally on the server, these are separated and distinguished using different folders. 

vHost Fuzzing

```bash
# use a vhost dictionary file
cp /usr/share/wordlists/secLists/Discovery/DNS/namelist.txt ./vhosts

cat ./vhosts | while read vhost;do echo "\n********\nFUZZING: ${vhost}\n********";curl -s -I http://$ip -H "HOST: ${vhost}.example.com" | grep "Content-Length: ";done
```

vHost Fuzzing with ffuf:

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


## Certificate enumeration

SSL/TLS certificates are another potentially valuable source of information if HTTPS is in use (for instance, in gathering information to prepare a phising attack).

For this we can use: 
- [sslyze](sslyze.md)
- [ssllabs by Qalys](https://www.ssllabs.com/ssltest/)

Also, you can use a script for nmap:

```bash
nmap --script ssl-enum-ciphers <HOSTNAME>
```


[virustotal](https://www.virustotal.com/).

**[crt.sh](https://crt.sh/)**: it enables the verification of issued digital certificates for encrypted Internet connections. This is intended to enable the detection of false or maliciously issued certificates for a domain.

```bash
# Get all subdomais with that digital certificate
curl -s https://crt.sh/\?q\=example.com\&output\=json | jq .

# Filter all by unique subdomain
curl -s https://crt.sh/\?q\=example.com\&output\=json | jq . | grep name | cut -d":" -f2 | grep -v "CN=" | cut -d'"' -f2 | awk '{gsub(/\\n/,"\n");}1;' | sort -u

# With the list of unique subdomains, list all the Company hosted servers
for i in $(cat subdomainlist);do host $i | grep "has address" | grep example.com | cut -d" " -f4 >> ip-addresses.txt;done

curl -s "https://crt.sh/?q=${TARGET}&output=json" | jq -r '.[] | "\(.name_value)\n\(.common_name)"' | sort -u > "${TARGET}_crt.sh.txt"
# curl -s: Issue the request with minimal output.
# https://crt.sh/?q=<DOMAIN>&output=json: Ask for the json output.
# jq -r '.[]' "\(.name_value)\n\(.common_name)"': Process the json output and print certificate's name value and common name one per line.
# sort -u: Sort alphabetically the output provided and removes duplicates.

# We also can manually perform this operation against a target using OpenSSL via:
openssl s_client -ign_eof 2>/dev/null <<<$'HEAD / HTTP/1.0\r\n\r' -connect "${TARGET}:${PORT}" | openssl x509 -noout -text -in - | grep 'DNS' | sed -e 's|DNS:|\n|g' -e 's|^\*.*||g' | tr -d ',' | sort -u

```

[https://censys.io](https://censys.io): We can navigate to https://search.censys.io/certificates or https://crt.sh and introduce the domain name of our target organization to start discovering new subdomains.

[The Harvester](https://github.com/laramies/theHarvester): simple-to-use yet powerful and effective tool for early-stage penetration testing and red team engagements. We can use it to gather information to help identify a company's attack surface. The tool collects `emails`, `names`, `subdomains`, `IP addresses`, and `URLs` from various public data sources for passive information gathering. It has modules. 

Automate the modules we want to launch:

**1.** Create a list of sources, one per line, sources.txt.

**2.** Execute:

```bash
 cat sources.txt | while read source; do theHarvester -d "${TARGET}" -b $source -f "${source}_${TARGET}";done
```

**3.** When the process finishes, extract all the subdomains found and sort them:

```bash
cat *.json | jq -r '.hosts[]' 2>/dev/null | cut -d':' -f 1 | sort -u > "${TARGET}_theHarvester.txt"
```

**4.** Merge all the passive reconnaissance files:

```shell-session
cat facebook.com_*.txt | sort -u > facebook.com_subdomains_passive.txt
$ cat facebook.com_subdomains_passive.txt | wc -l
```

**[Shodan](shodan.md)**:  Once we see which hosts can be investigated further, we can generate a list of IP addresses with a minor adjustment to the `cut` command and run them through `Shodan`.

```shell-session
for i in $(cat ip-addresses.txt);do shodan host $i;done

```

With this we'll get an IP list, that we can use to search for [DNS records](53-dns.md).


## Directory/File enumeration

[Cheat sheet with dirb](dirb.md).

[Gobuster](gobuster.md):

```bash
gobuster dir -u <exact target url> -w </path/dic.txt> -b 401 
# -b flag is to exclude from results an specific http response`
```

[Ffuf](ffuf.md):

```bash
ffuf -w /path/to/wordlist -u https://target/FUZZ

# Assuming that the default virtualhost response size is 4242 bytes, we can filter out all the responses of that size (`-fs 4242`)while fuzzing the Host - header:
ffuf -w /path/to/vhost/wordlist -u https://target -H "Host: FUZZ" -fs 4242

# Enumerating directories and folders:
ffuf -recursion -recursion-depth 1 -u http://$ip/FUZZ -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-small-directories-lowercase.txt
# -recursion: activates the recursive scan
# -recursion-depth 1: specifies the maximum depth to scan

# fuzz a combination of folder names, with a wordlist of possible files and a dictionary of extensions
ffuf -w ./folders.txt:FOLDERS,./wordlist.txt:WORDLIST,./extensions.txt:EXTENSIONS -u http://$ip/FOLDERS/WORDLISTEXTENSIONS
```

## Crawling

[OWASP Zap](owasp-zap.md).




## Tools

- Enumeration of directories, as3 buckets, dns... : [Gobuster](gobuster.md)
- Fuzzing: [ffuf](ffuf.md), [Burpsuite](burpsuite.md), [Wfuzz](wfuzz.md), [feroxbuster](feroxbuster.md)
- Web scanner of web servers, supporting frameworks, and applications using the command-line: [whatweb].
- Taking screenshots and identify default credentials if known: [EyeWitness](eyewitness.md)
