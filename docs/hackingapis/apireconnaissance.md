---
title: Api Reconnaissance
author: amandaguglieri
draft: false
TableOfContents: true
---

# Api Reconnaissance

??? abstract "General index of the course"
    - [Setting up the environment](setting-up-kali.md)
    - [Api Reconnaissance](api-authentication-attacks.md).
    - [Endpoint Analysis](endpoint-analysis.md).
    - [Scanning APIS](scanning-apis.md).
    - [API Authorization Attacks](api-authentication-attacks.md).
    - [Exploiting API Authorization](exploiting-api-authorization.md).
    - [Testing for Improper Assets Management](improper-assets-management.md).
    - [Mass Assignment](mass-assignment.md).
    - [Server side Request Forgery](server-side-request-forgery-ssrf.md).
    - [Injection Attacks](injection-attacks.md). 
    - [Evasion and Combining techniques](evasion-combining-techniques.md).
    - [Setting up the labs + Writeups](other-labs.md)

## Passive reconnaissance

### Google Dorks

| Google Dorking Query | Expected results |
|------------------------------- | ---------------------- |
| intitle:"api" site: "example.com" |  Finds all publicly available API related content in a given hostname. Another cool example for API versions:  inurl:"/api/v1" site: "example.com" |
| intitle:"json" site: "example.com" |  Many APIs use json, so this might be a cool filter |
| inurl:"/wp-son/wp/v2/users" |  Finds all publicly available WordPress API user directories. |
| intitle:"index.of" intext:"api.txt" | Finds publicly available API key files. |
|  inurl:"/api/v1" intext:"index of /" | Finds potentially interesting API directories. |
| intitle:"index of" api_key OR "api key" OR apiKey -pool | This is one of my favorite queries. It lists potentially exposed API keys. |



### Github

Also Github can be a good platform to search for overshared information relating to APIs.

|  Github Dowking Query |  Expected results |
| --------------------- | ----------------- |
| applicationName api key | After getting results, filter by issue and you may find some api keys. It's common to leave api keys exposed when rebasing a git repo, for instance |
|  api_key | -  |
|  authorization_bearer | -   |
|  oauth |  -  |
|  auth |  -  |
|  authentication |  -  |
|  client_secret |  -  |
|  api_token |  -  |
|  client_id  |  -  |
|  OTP |  -  |
|  HOMEBREW_GITHUB_API_TOKEN | -   |
|  SF_USERNAME |  -  |
|  HEROKU_API_KEY  |  -  |
|  JEKYLL_GITHUB_TOKEN | -   |
|  api.forecast.io  | -   |
|  password |  -  |
|  user_password | -   |
|  user_pass |  -  |
|  passcode  |  -  |
|  client_secret | -   |
|  secret |  -  |
|  password hash |  -  |
|  user auth | -   |
| extension: json nasa | Results show some extensions that include json, so they might be API related |
| shodan_api_key | Results show shodan api keys |
| "authorization: Bearer" | This search reveal some authorization token. |
| filename: swagger.json | Go to Code tab and you will have the swagger file. |



### Shodan


|  Shodan Dowking Query |  Expected results |
| --------------------- | ----------------- |
|  "content-type: application/json" |  This type of content is usually related to APIs |
|  "wp-json" |  If you are using wordpress |



### WaybackMachine

|  Waybackmachine Dowking Query |  Expected results |
| ----------------------------- | ----------------- |
| Path to a API |  We are trying to see is there is a recorded history of the API. It may provide us with endpoints that used to exist but allegedly not anymore. |



## Active reconnaissance

### nmap

[Nmap Cheat sheet](../nmap.md).
First, we do a service enumeration. The Nmap general detection scan uses default scripts (-sC) and service enumeration (-sV) against a target and then saves the output in three formats for later review (-oX for XML, -oN for Nmap, -oG for greppable, or -oA for all three):

```bash
nmap -sC -sV [target address or network range] -oA nameofoutput
```

The Nmap all-port scan will quickly check all 65,535 TCP ports for running services, application versions, and host operating system in use:

```bash
nmap -p- [target address] -oA allportscan
```

You’ll most likely discover APIs by looking at the results related to HTTP traffic and other indications of web servers. Typically, you’ll find these running on ports 80 and 443, but an API can be hosted on all sorts of different ports. Once you discover a web server, you can perform HTTP enumeration using a Nmap NSE script (use -p to specify which ports you'd like to test).

```bash
nmap -sV --script=http-enum <target> -p 80,443,8000,8080
```

### amass

[amass Cheat sheet](../amass.md).
 
Before diving into using Amass, we should make the most of it by adding API keys to it. 

1. First, we can see which data sources are available for Amass (paid and free) by running:

```bash
amass enum -list 
```

2. Next, we will need to create a config file to add our API keys to.

```bash
sudo curl https://raw.githubusercontent.com/OWASP/Amass/master/examples/config.ini >~/.config/amass/config.ini
```

3. Now, see the file ~/.config/amass/config.ini and register in as many services as you can. Once you have obtained your API ID and Secret, edit the config.ini file and add the credentials to the file.

```bash
sudo nano ~/.config/amass/config.ini
```

4. Now, edit the file to add the sources. It is recommended to add:

+ censys.io: guesswork out of understanding and protecting your organization’s digital footprint.
+ https://asnlookup.com: Quickly lookup updated information about specific Autonomous System Number (ASN), Organization, CIDR, or registered IP addresses (IPv4 and IPv6) among other relevant data. We also offer a free and paid API access!
+ https://otx.alienvault.com:  Quickly identify if your endpoints have been compromised in major cyber attacks using OTX Endpoint Security and many other.
+ https://bigdatacloud.com
+ https://cloudflare.com
+ https://www.digicert.com/tls-ssl/certcentral-tls-ssl-manager: 
+ https://fullhunt.io
+ https://github.com
+ https://ipdata.co
+ https://leakix.net
+ as many more as you can.

5. When ready, we can run amass:

```bash
amass enum -active -d crapi.apisec.ai  
```

Also, to be more precise:

```bash
amass enum -active -d <target> | grep api
# amass enum -active -d microsoft.com | grep api
```

Amass has several useful command-line options. Use the intel command to collect SSL certificates, search reverse Whois records, and find ASN IDs associated with your target. Start by providing the command with target IP addresses

```bash
amass intel -addr [target IP addresses]
```

If this scan is successful, it will provide you with domain names. These domains can then be passed to intel with the whois option to perform a reverse Whois lookup:

```bash
amass intel -d [target domain] –whois
```

This could give you a ton of results. Focus on the interesting results that relate to your target organization. Once you have a list of interesting domains, upgrade to the enum subcommand to begin enumerating subdomains. If you specify the -passive option, Amass will refrain from directly interacting with your target:

```bash
amass enum -passive -d [target domain]
```

The active enum scan will perform much of the same scan as the passive one, but it will add domain name resolution, attempt DNS zone transfers, and grab SSL certificate information:

```bash
amass enum -active -d [target domain]
```

To up your game, add the -brute option to brute-force subdomains, -w to specify the API_superlist wordlist, and then the -dir option to send the output to the directory of your choice:

```bash
amass enum -active -brute -w /usr/share/wordlists/API_superlist -d [target domain] -dir [directory name]  
```


### gobuster

[gobuster Cheat sheet](../gobuster.md).

Great tool to brute force directory discovery but it's not recursive (you need to specify a directory to perform a deeper scanner). Also, dictionaries are not API-specific. But here are some commands for Gobuster:

```bash
gobuster dir -u <exact target url> -w </path/dic.txt> --wildcard -b 401
# -b flag is to exclude from results an specific http response
```


### Kiterunner

[kiterunner Cheat sheet](../kiterunner.md).

Kiterunner is an excellent tool that was developed and released by Assetnote. Kiterunner is currently the best tool available for discovering API endpoints and resources. While directory brute force tools like Gobuster/Dirbuster/ work to discover URL paths, it typically relies on standard HTTP GET requests. Kiterunner will not only use all HTTP request methods common with APIs (GET, POST, PUT, and DELETE) but also mimic common API path structures. In other words, instead of requesting GET /api/v1/user/create, Kiterunner will try POST /api/v1/user/create, mimicking a more realistic request.

1. First, download the dictionaries from the [project](https://github.com/assetnote/kiterunner). In my case I downloaded it to /usr/share/wordlists/kiterunner/:

+ https://wordlists-cdn.assetnote.io/rawdata/kiterunner/routes-large.json.tar.gz
+ https://wordlists-cdn.assetnote.io/rawdata/kiterunner/routes-small.json.tar.gz
+ https://wordlists-cdn.assetnote.io/data/kiterunner/routes-large.kite.tar.gz
+ https://wordlists-cdn.assetnote.io/data/kiterunner/routes-small.kite.tar.gz

2. Run a quick scan of your target’s URL or IP address like this:

```bash
kr scan HTTP://127.0.0.1 -w ~/api/wordlists/data/kiterunner/routes-large.kite  
```

But. Note that we conducted this scan without any authorization headers, which the target API likely requires.

To use a dictionary (and not a kite file): 

```bash
kr brute <target> -w ~/api/wordlists/data/automated/nameofwordlist.txt
```

If you have many targets, you can save a list of line-separated targets as a text file and use that file as the target.

One of the coolest Kiterunner features is the ability to replay requests. Thus, not only will you have an interesting result to investigate, you will also be able to dissect exactly why that request is interesting. In order to replay a request, copy the entire line of content into Kiterunner, paste it using the kb replay option, and include the wordlist you used:

```bash
kr kb replay "GET     414 [    183,    7,   8]://192.168.50.35:8888/api/privatisations/count 0cf6841b1e7ac8badc6e237ab300a90ca873d571" -w ~/api/wordlists/data/kiterunner/routes-large.kite
```

Running this will replay the request and provide you with the HTTP response.

To run Kiterunner providing an authorization token as it could be "x-access-token", we can take the full authorization token and add it to your Kiterunner scan with the -H option:

```bash
kr scan http://IP -w /path/to/dict.txt -H 'x-access-token: eyJhGcwisdfdsfdfsdfsdfsdfdsfdsfddfdf.eyfakefakefakefaketokenfakeken._wcoooooo_kkkkkk_kkkk'
```




