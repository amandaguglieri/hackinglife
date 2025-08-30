---
title: Information gathering
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentest
  - information gathering
  - web
---

# Information gathering


??? abstract "Sources for these notes"
    - [Hack The Box: Penetration Testing Learning Path](https://academy.hackthebox.com/path/preview/penetration-tester)
    - [INE eWPT2 Preparation course](https://my.ine.com/CyberSecurity/courses/79af5ed1/web-application-penetration-testing-web-fingerprinting-and-enumeration)
    - [OWASP Web Security Testing Guide 4.2](OWASP/index.md) > 1. Information Gathering 
    - My own notes coming from experience pentesting.


## Methodology

Information gathering is typically broken down into two types: 

- **Passive information gathering** - Involves gathering as much information as possible without actively engaging with the target. 
- **Active information gathering/Enumeration** - Involves gathering as much information as possible by actively engaging with the target system. (You will require authorization in order to perform active information gathering).


| Passive Information Gathering                              | Active Information Gathering/Enumeration             |
| ---------------------------------------------------------- | ---------------------------------------------------- |
| Identifying domain names and domain ownership information. | Identify website content structure.                  |
| Discovering hidden/disallowed files and directories.       | Downloading & analyzing website/web app source code. |
| Identifying web server IP addresses & DNS records.         | Port scanning & service discovery.                   |
| Identifying web technologies being used on target sites.   | Web server fingerprinting.                           |
| WAF detection.                                             | Web application scanning.                            |
| Identifying subdomains.                                    | DNS Zone Transfers.                                  |
| Identify website content structure.                        | Subdomain enumeration via Brute-Force.               |


## 1. Passive information gathering

### 1.1. Fingerprint Web Server

Or Passive server enumeration.

!!! quote ""
	[OWASP Web Security Testing Guide 4.2](OWASP/index.md) > 1. Information Gathering > 1.2. Fingerprint Web Server

| ID  | Link to Hackinglife                   | Link to OWASP                                                                                                                                                                   | Objectives                                                                                                         |
| :-- | :------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------- |
| 1.2 | [WSTG-INFO-02](OWASP/WSTG-INFO-02.md) | [Fingerprint Web Server](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/02-Fingerprint_Web_Server) | - Determine the version and type of a running web server to enable further discovery of any known vulnerabilities. |

#### host command

DNS lookup utility. 

```bash
# By default host command search for A records:
host domain.com

# Search for type mx
host -t mx domain.com

# Using wordlists to discover hostnames:
for ip in $(cat list.txt); do host $ip.domain.com; done


# Enumerate hosts:
for i in $(seq 1 254); do host 172.16.5.$i; done | grep -v "not found"
```

#### whois command

WHOIS is a query and response protocol that is used to query databases that store the registered users or organizations of an internet resource like a domain name or an IP address block.

WHOIS lookups can be performed through the command line interface via the whois client or through some third party web-based tools to lookup the domain ownership details from different databases.

```shell-session
 whois $TARGET

whois example.com -h $ipTarget
```


```cmd-session
whois.exe <TARGET>
```

#### netcraft

[Netcraft](https://www.netcraft.com) can offer us information about the servers without even interacting with them, and this is something valuable from a passive information gathering point of view. We can use the service by visiting `https://sitereport.netcraft.com` and entering the target domain. We need to pay special attention to the latest IPs used. Sometimes we can spot the actual IP address from the webserver before it was placed behind a load balancer, web application firewall, or IDS, allowing us to connect directly to it if the configuration.

More issues fired up by netcraft: cms, server programming,...

#### censys

[https://search.censys.io/](https://search.censys.io/)

#### Shodan

- [https://www.shodan.io/](https://www.shodan.io/)



#### Wayback machine

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


### 1.2. Passive DNS enumeration

A valuable resource for this information is the Domain Name System (DNS). We can query DNS to identify the DNS records associated with a particular domain or IP address.


!!! quote ""
    - [Complete DNS enumeration guide: definition and techniques](53-dns.md).


> Some if these tools can also be used in Active DNS enumerations.

Worth trying: [DNSRecon](dnsrecon.md) and https://domain.glass/

| Tool + Cheat sheet                            | What it does                                                                                                                                                                                                  |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Google dorks](google-dorks.md)               | Google hacking, also named Google dorking, is a hacker technique that uses Google Search and other Google applications to find security holes in the configuration and computer code that websites are using. |
| [crt.sh](ctr.md)                              | It collects information about SSL certificates. If you visit a domain and it contains a certificate you can extract other subdomain by using the View Certificate functionality.                              |
| [dnscan](dnscan.md)                           | Python wordlist-based DNS subdomain scanner.                                                                                                                                                                  |
| [DNSRecon](dnsrecon.md)                       | Preinstalled with Linux: dsnrecon is a simple python script that enables to gather  DNS-oriented  information on a given target.                                                                              |
| [dnsdumpster.com](https://dnsdumpster.com/)   | DNSdumpster.com is a FREE domain research tool that can discover hosts related to a domain. Finding visible hosts from the attackers perspective is an important part of the security assessment process.     |
| https://domain.glass/                         |                                                                                                                                                                                                               |
| [viewdns.info](https://viewdns.info/)         |                                                                                                                                                                                                               |
| [domaintools](https://whois.domaintools.com/) |                                                                                                                                                                                                               |
|                                               |                                                                                                                                                                                                               |


### 1.3. Reviewing server metafiles

!!! quote ""
	[OWASP Web Security Testing Guide 4.2](OWASP/index.md) > 1. Information Gathering > 1.5. Review Webpage content for Information Leakage

|ID|Link to Hackinglife|Link to OWASP|Objectives|
|:---|:---|:---|:---|
|1.5|[WSTG-INFO-05](OWASP/WSTG-INFO-05.md) |[Review Webpage Content for Information Leakage](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/05-Review_Webpage_Content_for_Information_Leakage)|- Review webpage comments, metadata, and redirect bodies to find any information leakage.  - Gather JavaScript files and review the JS code to better understand the application and to find any information leakage.  - Identify if source map files or other front-end debug files exist.|


Some of these files:

- robots.txt
- sitemap.xml
- security.txt (proposed standard which allows websites to define security policies and contact details.)
- human.txt (initiative for knowing the people behind a website.)

### 1.4. Conduct search Search Engine Discovery

!!! tip "Dorking"
    - [Complete google dork guide](google-dorks.md).
    - [Complete github dork guide](github-dorks.md).

!!! quote ""
	[OWASP Web Security Testing Guide 4.2](OWASP/index.md) > 1. Information Gathering > 1.1. Conduct search engine discovery reconnaissance for information leakage

| ID  | Link to Hackinglife                   | Link to OWASP                                                                                                                                                                                                                                                                   | Objectives                                                                                                                                                                                               |
| :-- | :------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.1 | [WSTG-INFO-01](OWASP/WSTG-INFO-01.md) | [Conduct Search Engine Discovery Reconnaissance for Information Leakage](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/01-Conduct_Search_Engine_Discovery_Reconnaissance_for_Information_Leakage) | - Identify what sensitive design and configuration information of the application, system, or organization is exposed directly (on the organization's website) or indirectly (via third-party services). |

### 1.5. Cloud resources

Buckets, blob, ...: https://buckets.grayhatwarfare.com/


#### Greyhat Warfare

Monitoring breaches in buckets and storage accounts in the cloud.

[Greyhat Warfare](https://buckets.grayhatwarfare.com/)

#### Trufflehog 

A tool for continuously monitoring **Git, Jira, Slack, Confluence, Microsoft Teams, Sharepoint, and more.**
[Trufflehog](https://github.com/trufflesecurity/truffleHog)


### 1.6. Fingerprint web application technology and frameworks

!!! quote ""
	[OWASP Web Security Testing Guide 4.2](OWASP/index.md) > 1. Information Gathering > 1.8. Fingerprint Web Application Framework

|ID|Link to Hackinglife|Link to OWASP|Objectives|
|:---|:---|:---|:---|
|1.8|[WSTG-INFO-08](OWASP/WSTG-INFO-08.md) |[Fingerprint Web Application Framework](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/08-Fingerprint_Web_Application_Framework)|- Fingerprint the components being used by the web applications.  - Find the type of web application framework/CMS from HTTP headers, Cookies, Source code, Specific files and folders, Error message.|

If we discover the webserver behind the target application, it can give us a good idea of what operating system is running on the back-end server. 

For instance:

- IIS 6.0: Windows Server 2003
- IIS 7.0-8.5: Windows Server 2008 / Windows Server 2008R2
- IIS 10.0 (v1607-v1709): Windows Server 2016
- IIS 10.0 (v1809-): Windows Server 2019

Although this is usually correct when dealing with Windows, we can not be sure in the case of Linux or BSD-based distributions as they can run different web server versions

How to spot a web server?

#### HTTP headers

X-Powered-By and cookies: 
- .NET: `ASPSESSIONID<RANDOM>=<COOKIE_VALUE>`
- PHP: `PHPSESSID=<COOKIE_VALUE>`
- JAVA: `JSESSION=<COOKIE_VALUE>`

More manual techniques on  [OWASP 4.2: WSTG-INFO-08](OWASP/WSTG-INFO-08.md)


**Banner Grabbing / Web Server Headers**

#### whatweb

[whatweb](whatweb.md)**.

```bash
whatweb -a3 https://www.example.com -v
# -a3: aggression level 3
# -v: verbose mode
```

#### Wappalyzer

 [Wappalyzer](https://www.wappalyzer.com/)**


#### wafw00f

[wafw00f](wafw00f.md)**:

```shell-session
wafw00f -v https://www.example.com

# -a: check all possible WAFs in place instead of stopping scanning at the first match.
# -i: read targets from an input file 
# -p proxy the requests 
```

#### Aquatone

[Aquatone](aquatone.md)

```bash
cat example_of_list.txt | aquatone -out ./aquatone -screenshot-timeout 1000
```

#### BuiltWith

Addons [BuiltWith](https://addons.mozilla.org/es/firefox/addon/builtwith/): BuiltWith® covers 93,551+ internet technologies which include analytics, advertising, hosting, CMS and many more.


#### Curl

 [Curl](curl.md):

```bash
curl -IL https://<TARGET>
# -I: --head (HTTP  FTP  FILE) Fetch the headers only!
# -L, --location: (HTTP) If the server reports that the requested page has moved to a different location (indicated with a Location: header and a 3XX response  code),  this  option  will make  curl  redo the request on the new place. If used together with -i, --include or -I, --head, headers from all requested pages will be shown. 
```

#### nmap

[nmap](nmap.md):

```shell-session
sudo nmap -v $ip --script banner.nse
```



### 1.7. WAF detection

#### wafw00f

[wafw00f](wafw00f.md)**:

```shell-session
wafw00f -v https://www.example.com

# -a: check all possible WAFs in place instead of stopping scanning at the first match.
# -i: read targets from an input file 
# -p proxy the requests 
```

#### nmap

[nmap](nmap.md):

```
nmap -p443 --script http-waf-detect <host>
```

### 1.8. Code analysis: HTTRack and EyeWitness

!!! quote ""
	[OWASP Web Security Testing Guide 4.2](OWASP/index.md) > 1. Information Gathering > 1.7. Map Execution Paths through applications

|ID|Link to Hackinglife|Link to OWASP|Objectives|
|:---|:---|:---|:---|
|1.7|[WSTG-INFO-07](OWASP/WSTG-INFO-07.md)|[Map Execution Paths Through Application](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/07-Map_Execution_Paths_Through_Application)|- Map the target application and understand the principal workflows.  - Use HTTP(s) Proxy Spider/Crawler feature aligned with application walkthrough|



#### HTTRack

[HTTRack tutorial](httrack.md)

Create a folder for replicating in it your target.

```
mkdir targetsite
httrack domain.com  targetsite/
```

Interactive mode:

```
httrack
```

#### EyeWitness

[EyeWitness tutorial](eyewitness.md)

First, create a file with the target domains, like for instance, listOfdomains.txt.

Then, run:

```
eyewitness --web -f listOfdomains.txt -d path/to/save/
```

After that you will get a report.html file with the request and a screenshot of those domains.

```
# Proxing the request via BurpSuite
eyewitness --web -f listOfdomains.txt -d path/to/save/ --proxy-ip 127.0.0.1 --proxy-port 8080
```

### 1.9. Crawlers

**Crawling** is the process of navigating around the web application, following links, submitting forms and logging in (where possible) with the objective of mapping out and cataloging the web application and the navigational paths within it. 

Crawling is typically passive as engagement with the target is done via what is publicly accessible, we can utilize Burp Suite’s passive crawler to help us map out the web application to better understand how it is setup and how it works.


- [BurpSuite](burpsuite.md) Community edition has only Crawler feature available. For spidering, you need Pro edition. Burp Suite Spider
- [OWASP ZAP (Zed Attack Proxy)](owasp-zap.md): ZAP is a free, open-source web application security scanner. It can be used in automated and manual modes and includes a spider component to crawl web applications and identify potential vulnerabilities. has both Spider and Crawler features available.
- `Scrapy (Python Framework)`: Scrapy is a versatile and scalable Python framework for building custom web crawlers. It provides rich features for extracting structured data from websites, handling complex crawling scenarios, and automating data processing. Its flexibility makes it ideal for tailored reconnaissance tasks.
- `Apache Nutch (Scalable Crawler)`: Nutch is a highly extensible and scalable open-source web crawler written in Java. It's designed to handle massive crawls across the entire web or focus on specific domains. While it requires more technical expertise to set up and configure, its power and flexibility make it a valuable asset for large-scale reconnaissance projects.
#### Scrapy

`Scrapy (Python Framework)`: Scrapy is a versatile and scalable Python framework for building custom web crawlers. It provides rich features for extracting structured data from websites, handling complex crawling scenarios, and automating data processing. Its flexibility makes it ideal for tailored reconnaissance tasks.

```shell-session
# Installation
pip3 install scrapy
```

#### ReconSpider

```
# Installation
wget -O ReconSpider.zip https://academy.hackthebox.com/storage/modules/144/ReconSpider.v1.2.zip

unzip ReconSpider.zip 
```


```shell-session
# Basic usage
python3 ReconSpider.py http://domain.com
```

After running `ReconSpider.py`, the data will be saved in a JSON file, `results.json`. This file can be explored using any text editor. 



## 2. Active  information gathering

### 2.1. Enumerate applications and services on Webserver

!!! quote ""
	[OWASP Web Security Testing Guide 4.2](OWASP/index.md) > 1. Information Gathering > 1.4. Enumerate Applications on Webserver

|ID|Link to Hackinglife|Link to OWASP|Objectives|
|:---|:---|:---|:---|
|1.4|[WSTG-INFO-04](OWASP/WSTG-INFO-04.md)|[Enumerate Applications on Webserver](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/04-Enumerate_Applications_on_Webserver)|- Enumerate the applications within the scope that exist on a web server.  - Find applications hosted in the webserver (Virtual hosts/Subdomain), non-standard ports, DNS zone transfers|

Hostname discovery

```shell-session
nmap --script smb-os-discovery $ip
```

Scanning the IP looking for services:

```
nmap -sV -sC -- <target>
```

### 2.2. Web Server Fingerprinting

!!! quote ""
	[OWASP Web Security Testing Guide 4.2](OWASP/index.md) > 1. Information Gathering > 1.2. Fingerprint Web Server

|ID|Link to Hackinglife|Link to OWASP|Objectives|
|:---|:---|:---|:---|
|1.2|[WSTG-INFO-02](OWASP/WSTG-INFO-02.md) |[Fingerprint Web Server](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/02-Fingerprint_Web_Server)|- Determine the version and type of a running web server to enable further discovery of any known vulnerabilities.|

#### HTTP headers and source code

HTTP headers and HTML Source code (with [Burpsuite](burpsuite.md) and [curl](curl.md)).  Or CRTL-u on the browser to see the source code.


- Note the response header  `Server`, `X-Powered-By`, or `X-Generator` as well.
- Identify framework specific cookies. For instance, the cookie `CAKEPHP` for php.
- Review the source code and identify `<meta>` or attributes with typical patterns from some servers (and/or frameworks).

#### nmap

Conduct an scan

```
nmap -sV -F target
```

If a server version found is potentially vulnerable, use [searchsploit](searchsploit.md):

```
searchsploit apache 2.4.18
```

#### metasploit 

Additionally you can use [metasploit](metasploit.md):

```
use auxiliary/scanner/http_version
```


#### whatweb 

[whatweb](whatweb.md).

```bash
# version of web servers, supporting frameworks, and applications
whatweb $ip
whatweb <hostname>

# Automate web application enumeration across a network.
whatweb --no-errors $ip/24
```

#### Nikto

[nikto](nikto.md).


```bash
nikto -h domain.com -o nikto.html -Format html


nikto -h http://domain.com/index.php?page=target-page.php -Tuning 5 -Display V
# -Display V : turn verbose mode on
# -Tuning 5 : Level 5 is considered aggressive, covering a wide range of tests but may also increase the likelihood of false positives. 
```


### 2.3. # Well-Known URIs

!!! quote "OWASP"
	[OWASP Web Security Testing Guide 4.2](OWASP/index.md) > 1. Information Gathering > 1.3. Review Webserver Metafiles for Information Leakage

| ID  | Link to Hackinglife                   | Link to OWASP                                                                                                                                                                                                                           | Objectives                                                                                                                                                                                                                                   |
| :-- | :------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.3 | [WSTG-INFO-03](OWASP/WSTG-INFO-03.md) | [Review Webserver Metafiles for Information Leakage](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/03-Review_Webserver_Metafiles_for_Information_Leakage) | - Identify hidden or obfuscated paths and functionality through the analysis of metadata files (robots.txt, `<META>` tag, sitemap.xml) - Extract and map other information that could lead to a better understanding of the systems at hand. |

The `.well-known` standard, defined in [RFC 8615](https://datatracker.ietf.org/doc/html/rfc8615), serves as a standardized directory within a website's root domain. This designated location, typically accessible via the `/.well-known/` path on a web server, centralizes a website's critical metadata, including configuration files and information related to its services, protocols, and security mechanisms.

| URI Suffix                     | Description                                                                                           | Status      | Reference                                                                               |
| ------------------------------ | ----------------------------------------------------------------------------------------------------- | ----------- | --------------------------------------------------------------------------------------- |
| `security.txt`                 | Contains contact information for security researchers to report vulnerabilities.                      | Permanent   | RFC 9116                                                                                |
| `/.well-known/change-password` | Provides a standard URL for directing users to a password change page.                                | Provisional | https://w3c.github.io/webappsec-change-password-url/#the-change-password-well-known-uri |
| `openid-configuration`         | Defines configuration details for OpenID Connect, an identity layer on top of the OAuth 2.0 protocol. | Permanent   | http://openid.net/specs/openid-connect-discovery-1_0.html                               |
| `assetlinks.json`              | Used for verifying ownership of digital assets (e.g., apps) associated with a domain.                 | Permanent   | https://github.com/google/digitalassetlinks/blob/master/well-known/specification.md     |
| `mta-sts.txt`                  | Specifies the policy for SMTP MTA Strict Transport Security (MTA-STS) to enhance email security.      | Permanent   | RFC 8461                                                                                |


### 2.4. Directory/File enumeration

#### nmap

```
nmap -sV -p80 --script=http-enum <target>
```

#### dirb

[Cheat sheet with dirb](dirb.md).

```
dirb http://domain.com /usr/share/metasploit-framework/data/wordlists/directory.txt
```


#### gobuster

[Gobuster](gobuster.md):

```bash
gobuster dir -u <exact target url> -w </path/dic.txt> -b 403,4.4 -x .php,.txt -r 
# -b: exclude from results an specific http response`
# -r: follow redirects
# -x: add to the path provided by dictionary these extensions
```


#### Ffuf

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


#### Wfuzz

[Wfuzz](wfuzz.md)

#### feroxbuster

[feroxbuster](feroxbuster.md)

#### amass

[amass](amass.md)


```bash
amass enum -active -d crapi.apisec.ai  -ip -brute -dir path/to/save/results/
# enum: Perform enumerations and network mapping
# -active: Attempt zone transfer and certificate name grabs, among others.
# -ip: Show ip addresses of cached subdomais.
# -brute: Perform a brute force dns attack.

amass enum -passive -d crapi.apisec.ai -src  -dir path/to/save/results/
# enum: Perform enumerations and network mapping.
# -pasive: Performs passive scan
# src: display sources of the host domain.
# -dir: Specify a folder to save results.

amass intel -d crapi.apisec.ai
# intel: Discover targets for enumerations. It actively automate active enumeration. 
```

Some flags:

```
-active: Attempt zone transfer and certificate name grabs.
-pasive: Passive fingerprinting.
-bl: Blacklist of subdomain names that will not be investigated
-d: to specify a domain
-ip: Show ip addresses of cached subdomais.
–include-unresolvable: output DNS names that did not resolve.
-o file.txt: To output the result into a file
-w: path to a different wordlist file
```

#### Spidering with OWASP ZAP

**Spidering** is an active technique. It's the process of automatically discovering new resources (URLs) on a web application/site. It typically begins with a list of target URLs called seeds, after which the  spider will visit the URLs and identified hyperlinks in the page and adds them to the list of URLs to visit and repeats the process recursively.

Spidering can be quite loud and as a result, it is typically considered to be an active information gathering technique.

We can utilize OWASP ZAP’s Spider to automate the process of spidering a web application to map out the web application and learn more about how the site is laid out and how it works.


[BurpSuite](burpsuite.md) Community edition has only Crawler feature available. For spidering, you need Pro edition.

[OWASP Zap](owasp-zap.md) has both Spider and Crawler features available.




### 2.5. Active DNS enumeration

Domain Name System (DNS) is a protocol that is used to resolve domain names/hostnames to IP addresses. During the early days of the internet, users would have to remember the IP addresses of the sites that they wanted to visit, DNS resolves this issue by mapping domain names (easier to recall) to their respective IP addresses. 

A DNS server (nameserver) is like a telephone directory that contains domain names and their corresponding IP addresses. A plethora of public DNS servers have been set up by companies like Cloudflare (1.1.1.1) and Google (8.8.8.8). These DNS servers contain the records of almost all domains on the internet.

DNS interrogation is the process of enumerating DNS records for a specific domain. The objective of DNS interrogation is to probe a DNS server to provide us with DNS records for a specific domain. This process can provide us with important information like the IP address of a domain, subdomains, mail server addresses etc.

More about [DNS enumeration](53-dns.md).


| Tool + Cheat sheet | What it does |
| ---- | ---- |
| [dnsenum](dnsenum.md) | multithreaded perl script to enumerate DNS information of a domain and to discover non-contiguous ip blocks. |
| [dig](dig.md) |  discover non-contiguous ip blocks. |
| [fierce](fierce.md) |  DNS scanner that helps locate non-contiguous IP space and hostnames. |
| [dnscan](dnscan.md) | Python wordlist-based DNS subdomain scanner. |
| [gobuster](gobuster.md) | For brute force enumerations. |
| [nslookup](nslookup.md) | . |
| [amass](amass.md) | In depth DNS Enumeration and network mapping. |
 

#### dnsenum

[dnsenum](dnsenum.md) Multithreaded perl script to enumerate DNS information of a domain and to discover non-contiguous ip blocks.  Used for active fingerprinting:

```
dnsenum domain.com
```

One cool thing about dnsenum is that it can perform dns transfer zone, like [dig]](dig.md). dnsenum performs DNS brute force with /usr/share/dnsenum/dns.txt.

#### dig 

Additionally, [see dig axfr](dig.md). 

**dig** (More complete cheat sheet: [dig](dig.md))

```bash
#Syntax for dns transferring a zone
dig axfr @nameserver example.com

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

#### Fierce

**Fierce** (More complete cheat sheet: [fierce](fierce.md))


```
# Perform a dns transfer using a wordlist againts domain.com
fierce -dns domain.com 
```



#### DNScan

**DNScan** (More complete cheat sheet: [DNScan](dnscan.md)): Python wordlist-based DNS subdomain scanner. The script will first try to perform a zone transfer using each of the target domain's nameservers.

```bash
dnscan.py (-d \<domain\> | -l \<list\>) [OPTIONS]
# Mandatory Arguments
#    -d  --domain                              Target domain; OR
#    -l  --list                                Newline separated file of domains to scan
```


#### gobuster

**gobuster** (More complete cheat sheet: [gobuster](gobuster.md))

```shell-session
gobuster dns -d <DOMAIN (without http)> -w /usr/share/SecLists/Discovery/DNS/namelist.txt
```

#### nslookup

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



### 2.6. Subdomain enumeration

`Subdomain enumeration` is the process of systematically identifying and listing these subdomains. From a DNS perspective, subdomains are typically represented by `A` (or `AAAA` for IPv6) records, which map the subdomain name to its corresponding IP address. Additionally, `CNAME` records might be used to create aliases for subdomains, pointing them to other domains or subdomains. 

Using Sec wordlist:

```shell-session
for sub in $(cat /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-110000.txt);do dig $sub.example.com @$ip | grep -v ';\|SOA' | sed -r '/^\s*$/d' | grep $sub | tee -a subdomains.txt;done
```

#### Sublist3r 

[Sublist3r](sublist3r.md)  enumerates subdomains using many search engines such as Google, Yahoo, Bing, Baidu and Ask. Sublist3r also enumerates subdomains using Netcraft, Virustotal, ThreatCrowd, DNSdumpster and ReverseDNS. Easily blocked by Google.


```bash
python3 sublist3r.py -d example.com -o file.txt
# -d: Specify the domain.
# -o file.txt: It prints the results to a file
# -b: Enable the bruteforce module. This built-in module relies on the names.txt wordlist. To find it, use: locate names.txt (you can edit it).

# Select an engine for enumeration, for instance, google.
python3 sublist3r.py -d example.com -e google
```

#### fierce

```
# Brute force subdomains with a seclist
fierce --domain domain.com --subdomain-file fierce-hostlist.txt
```

#### gobuster

[Gobuster](gobuster.md):

```bash
gobuster vhost -w /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u <exact target url>
# vhost : Uses VHOST for brute-forcing
# -w : Path to the wordlist
# -u : Specify the URL
```

#### wfuzz

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

#### dnsenum

Using [dnsenum](dnsenum.md).

#### Bash script with dig and seclist

Bash script, using Sec wordlist:

```shell-session
for sub in $(cat /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-110000.txt);do dig $sub.example.com @$ip | grep -v ';\|SOA' | sed -r '/^\s*$/d' | grep $sub | tee -a subdomains.txt;done
```

### 2.7. VHOST enumeration

A virtual host (`vHost`) is a feature that allows several websites to be hosted on a single server.  At the core of `virtual hosting` is the ability of web servers to distinguish between multiple websites or applications sharing the same IP address. This is achieved by leveraging the `HTTP Host` header, a piece of information included in every `HTTP` request sent by a web browser. The key difference between `VHosts` and `subdomains` is their relationship to the `Domain Name System (DNS)` and the web server's configuration.

There are 3 ways to configure virtual hosts:

1. `Name-Based Virtual Hosting`: This method relies solely on the `HTTP Host header` to distinguish between websites. It is the most common and flexible method, as it doesn't require multiple IP addresses. It requires the web server to support name-based `virtual hosting` and can have limitations with certain protocols like `SSL/TLS`.
2. `IP-Based Virtual Hosting`: This type of hosting assigns a unique IP address to each website hosted on the server. The server determines which website to serve based on the IP address to which the request was sent. It doesn't rely on the `Host header`, can be used with any protocol, and offers better isolation between websites. Still, it requires multiple IP addresses, which can be expensive and less scalable.
3. `Port-Based Virtual Hosting`: Different websites are associated with different ports on the same IP address. For example, one website might be accessible on port 80, while another is on port 8080. `Port-based virtual hosting` can be used when IP addresses are limited, but it’s not as common or user-friendly as `name-based virtual hosting` and might require users to specify the port number in the URL.

In essence, the `Host` header functions as a switch, enabling the web server to dynamically determine which website to serve based on the domain name requested by the browser.

vHost Fuzzing

```bash

# use a vhost dictionary file
cp /usr/share/wordlists/secLists/Discovery/DNS/namelist.txt ./vhosts

cat ./vhosts | while read vhost;do echo "\n********\nFUZZING: ${vhost}\n********";curl -s -I http://$ip -H "HOST: ${vhost}.example.com" | grep "Content-Length: ";done
```

#### vHost Fuzzing with [ffuf](ffuf.md)

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

####  vHost Fuzzing with [gobuster](gobuster.md) 

There are a couple of things you need to prepare to brute force `Host` headers:

1. `Target Identification`: First, identify the target web server's IP address. This can be done through DNS lookups or other reconnaissance techniques.
2. `Wordlist Preparation`: Prepare a wordlist containing potential virtual host names. You can use a pre-compiled wordlist, such as SecLists, or create a custom one based on your target's industry, naming conventions, or other relevant information.

```shell-session
gobuster vhost -u http://$ip -w <wordlist_file> --append-domain
# The `-u` flag specifies the target URL
# The `-w` flag specifies the wordlist file 
# The `--append-domain` flag appends the base domain to each word in the wordlist.
```


and [feroxbuster](feroxbuster.md).


### 2.8. Certificate enumeration

SSL/TLS certificates are another potentially valuable source of information if HTTPS is in use (for instance, in gathering information to prepare a phising attack).

#### sslyze and sslabs

For this we can use: 
- [sslyze](sslyze.md)
- [ssllabs by Qalys](https://www.ssllabs.com/ssltest/)
- [https://ciphersuite.info](https://ciphersuite.info).

#### nmap 

Also, you can use a script for nmap:

```bash
nmap --script ssl-enum-ciphers <HOSTNAME>
```

#### virustotal

[virustotal](https://www.virustotal.com/).


#### crt.sh with curl

**[crt.sh](https://crt.sh/)**: it enables the verification of issued digital certificates for encrypted Internet connections. This is intended to enable the detection of false or maliciously issued certificates for a domain.

```bash
# Get all subdomais with that digital certificate
curl -s https://crt.sh/\?q\=example.com\&output\=json | jq .

# Filter all by unique subdomain
curl -s https://crt.sh/\?q\=example.com\&output\=json | jq . | grep name | cut -d":" -f2 | grep -v "CN=" | cut -d'"' -f2 | awk '{gsub(/\\n/,"\n");}1;' | sort -u

# With the list of unique subdomains, list all the Company hosted servers
for i in $(cat subdomainlist);do host $i | grep "has address" | grep example.com | cut -d" " -f4 >> ip-addresses.txt;done

# Find all 'dev' subdomains on facebook.com using curl and jq:
curl -s "https://crt.sh/?q=facebook.com&output=json" | jq -r '.[]
 | select(.name_value | contains("dev")) | .name_value' | sort -u
# -s  -s "https://crt.sh/?q=facebook.com&output=json":his command fetches the JSON output from crt.sh for certificates matching the domain `facebook.com`.  : 


curl -s "https://crt.sh/?q=${TARGET}&output=json" | jq -r '.[] | "\(.name_value)\n\(.common_name)"' | sort -u > "${TARGET}_crt.sh.txt"
# curl -s: Issue the request with minimal output.
# https://crt.sh/?q=<DOMAIN>&output=json: Ask for the json output.
# jq -r '.[]' "\(.name_value)\n\(.common_name)"': Process the json output and print certificate's name value and common name one per line.
# sort -u: Sort alphabetically the output provided and removes duplicates.

# We also can manually perform this operation against a target using OpenSSL via:
openssl s_client -ign_eof 2>/dev/null <<<$'HEAD / HTTP/1.0\r\n\r' -connect "${TARGET}:${PORT}" | openssl x509 -noout -text -in - | grep 'DNS' | sed -e 's|DNS:|\n|g' -e 's|^\*.*||g' | tr -d ',' | sort -u

```

#### censys.io

[https://censys.io](https://censys.io): We can navigate to https://search.censys.io/certificates or https://crt.sh and introduce the domain name of our target organization to start discovering new subdomains.

#### The Harvester 

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

#### Shodan 

**[Shodan](shodan.md)**:  Once we see which hosts can be investigated further, we can generate a list of IP addresses with a minor adjustment to the `cut` command and run them through `Shodan`.

```shell-session
for i in $(cat ip-addresses.txt);do shodan host $i;done

```

With this we'll get an IP list, that we can use to search for [DNS records](53-dns.md).





