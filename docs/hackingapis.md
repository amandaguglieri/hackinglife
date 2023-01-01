---
title: "Hacking APIs"
date: 2022-10-29T00:00:00Z
draft: false
TableOfContents: true
---


## About the course

Notes from the course "APIsec Certified Expert" a practical course in API hacking imparted by Corey J. Ball.
+ Course: https://university.apisec.ai/
+ Book: https://www.amazon.com/Hacking-APIs-Application-Programming-Interfaces/dp/1718502443
+ Instructor: [Corey J. Ball](https://www.linkedin.com/in/coreyjball/).

## Pending

Mass Assignment. Coming up next 11 Dec.
Server side Request Forgery. Coming up next 11 Dec.
Injection Attacks. Coming up next 18 Dec.
Evasion and Combining techniques. Coming up next 19 Dec.
Conclusion. Coming up next 19 Dec.


## Passive reconnaissance

**Google Dorks**

| Google Dorking Query | Expected results |
|------------------------------- | ---------------------- |
| intitle:"api" site: "example.com" |  Finds all publicly available API related content in a given hostname. Another cool example for API versions:  inurl:"/api/v1" site: "example.com" |
| intitle:"json" site: "example.com" |  Many APIs use json, so this might be a cool filter |
| inurl:"/wp-son/wp/v2/users" |  Finds all publicly available WordPress API user directories. |
| intitle:"index.of" intext:"api.txt" | Finds publicly available API key files. |
|  inurl:"/api/v1" intext:"index of /" | Finds potentially interesting API directories. |
| intitle:"index of" api_key OR "api key" OR apiKey -pool | This is one of my favorite queries. It lists potentially exposed API keys. |

**Github**
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

**Shodan**
|  Shodan Dowking Query |  Expected results |
| --------------------- | ----------------- |
|  "content-type: application/json" |  This type of content is usually related to APIs |
|  "wp-json" |  If you are using wordpress |


**WaybackMachine**
|  Waybackmachine Dowking Query |  Expected results |
| ----------------------------- | ----------------- |
| Path to a API |  We are trying to see is there is a recorded history of the API. It may provide us with endpoints that used to exist but allegedly not anymore. |


## Active reconnaissance

### nmap

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

Great tool to brute force directory discovery but it's not recursive (you need to specify a directory to perform a deeper scanner). Also, dictionaries are not API-specific. But here are some commands for Gobuster:


```bash
gobuster dir -u <exact target url> -w </path/dic.txt> -b 401
# -b flag is to exclude from results an specific http response
```


### Kiterunner

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




## Reverse engineering an API

### Endpoint analysis

If an API is not documented or the documentation is unavailable to you, then you will need to build out your own collection of requests. Two different methods:

1. Build a collection in Postman

2. Build out an API specification using mitmproxy2swagger.

### Build a collection in Postman

In the instance where there is no documentation and no specification file, you will have to reverse-engineer the API based on your interactions with it. Mapping an API with several endpoints and a few methods can quickly grow into quite a large attack surface.  There are two ways to manually reverse engineer an API with Postman. 

+ One way is by constructing each request. 
+ The other way is to proxy web traffic through Postman, then use it to capture a stream of requests. This process makes it much easier to construct requests within Postman, but you’ll have to remove or ignore unrelated requests. 

**Steps**:
1. Start crapi application

```bash
cd ~/lab/crapi
sudo docker-compose start
```

2. Open the browser, and select "postman 5555" in your Foxyproxy addon to proxy the traffic. 
3. Open your local crapi application in the browser: http://localhost:8888
4. Run postman from the command line:

```bash
postman
```
5. Once postman is open, press on "Capture traffic link" (at the bottom right of the application). Set up the capture, and make sure that proxy is enabled in the application. A useful shortcut to go to Settings is CTRL-, (comma).
6. Now you are capturing the traffic. Go through your crapi application and when done, go to postman and stop the capture. 
7. Final step is to filter out the requests you want and add them to a collection. In the collection, you will be able to organize these requests in folders /endpoints.


### Build out an API specification using mitmproxy2swagger

**Steps**
1. From cli, run:

```bash
mitmweb
```
2. Select burp 8080 in the foxyproxy addon in your browser.
3. Open a tab in your browser with the mitmweb proxy service: http://localhost:8081, and make sure that traffic is being captured there.
4. Now you are capturing the traffic. Go through your crapi application and when done, turn off the foxyproxy.
5. In the mitmweb service at http://localhost:8081, go to File>Save. A file called "flows" will be downloaded to your download folder.
6. We need to parse this "flows" file into something understandable by Postman. For that, we will use a tool called mitmproxy2swagger, which will transform our captured traffic into an Open API 3.0 YAML file that can be viewed in a browser and imported as a collection into Postman. Run:

```bash
sudo mitmproxy2swagger -i ~/Downloads/flows -o spec.yml -p http://localhost:8888/ -f flow 
# -i: input    |  -o: output   | -p: target   |  -f: force format to the specified.
```

7. Edit spec.yml to remove "ignore:" when it proceeds, and save changes. Run again mitmproxy2swagger to populate your spec with examples.

```bash
sudo mitmproxy2swagger -i ~/Downloads/flows -o spec.yml -p http://localhost:8888/ -f flow --examples
# --examples will grab the previously created spec.yml and will populate it with real examples. We do this in two steps to avoid creating examples for request out of scope.  
```

8. Open https://editor.swagger.io/ and click on File > Import. Import your spec.yml. The goal here is to validate the structure of your file.
9. If everything is ok, open the postman application:

```bash
postman
```

10. In postman, go to File > Import, and select the spec.yml file. After importing it, you will be able to add it to a collection, and compare this collection against that created by browsing just with postman.

API Documentation Conventions
| Convention | Example | Meaning |
| ---------- | ------- | ------- |
| : or {} | /user/:id
/user/{id}
/user/2727
/account/:username
/account/{username}
/account/scuttleph1sh |  The colon or curly brackets are used by some APIs to indicate a path variable. In other words, “:id” represents the variable for an ID number and “{username}” represents the account username you are trying to access. | 
|  [] | /api/v1/user?find=[name] | Square brackets indicate that the input is optional. |
| || | “blue” || “green” || “red” | Double bars represent different possible values that can be used. |



## Scanning APIs

Once you have discovered an API and used it as it was intended, you can proceed to perform a baseline vulnerability scan. Most of these scans return false-negative results (because they are web-oriented)  but they are helpful in structuring next steps.

Basic scans you can run:

### nikto

You will get some results related to headers such as:

+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type

Run:

```bash
nikto -h http://localhost:8888
```

### OWASP zap

To launch it, run:

```bash
zaproxy
```

You can do several things:

+ Run an automatic attack.
+ Import your spec.yml file and run an automatic attack.
+ Run a manual attack. 

The manual explore option will allow you to perform authenticated scanning. Set the URL to your target, make sure the HUD is enabled, and choose "Launch Browser". 

**How to run a manual attack**: Select "Continue to your target". On the right-hand side of the HUD, you can set the Attack Mode to On. This will begin scanning and performing authenticated testing of the target. Now you  perform all the actions (sign up a new user, log  in into the account, modify you avatar, post a comment...).

After that, OWASP Zap allows you to narrow the results to your target. How? In the Sites module, right click on your site and select "Include in context". After that, click on the icon shaped as a "target" to filter out sites by context. 

With the results, start your analysis and remove false-negative vulnerabilities.
 


## API Authentication Attacks

### Classic authentication attacks

We'll consider two attacks: Password Brute-Force Attack, and Password Spraying. These attacks may take place every time that Basic Authentication is deployed in the context of a RESTful API.

The principle of Basic authentication is that the consumer issues a request containing a username and password, th>

As RESTful APIs don't maintain a state, the API need to leverage basic authentication across all endpoints. Instead of doing this, the API may leverage basic authentication once using an authentication portal, then upon providing the correct credentials, a token would be issued to be used in subsequent requests.
 
#### 1. Password Brute-Force Attacks

Brute-forcing an API's authentication is not very different from any other brute-force attack, except you will send the request to an API endpoint, the payload will often be in JSON, and the authentication values may be base64 encoded.

Infinite ways to do it. You can use: 

+ Intruder module of BurpSuite.
+ ZAP proxy tool.
+ wfuzz.
+ ffuzz. 
+ others.

Let's see wfuzz:

```bash
wfuzz -d {"email":"hapihacker@hapihacjer.com","password":"PASSWORD"} -z file,/usr/share/wordlists/rockyou.txt -u http://localhost:8888/identity/api/auth/login --hc 500
# -H to specify content-type headers. 
# -d allows you to include the POST Body data. 
# -u specifies the url
# --hc/hl/hw/hh hide responses with the specified code/lines/words/chars. In our case, "--hc 500" hides 500 code responses.
# -z specifies a payload   
```

Tools to build password lists:
+ https://github.com/sc0tfree/mentalist
+ https://github.com/Mebus/cupp
+ crunch (already installed in kali)

#### 2. Password Spraying

Very useful if you know the password policy of the API we are attacking. Say that there is a lockout account policy for te tries. Then you can password spray attack with 9 tries and use for that the 9 most probable password for all the accounts email spotted.

As in crapi we have detected before a disclosure of information in the forum page (a json response with all kind of data from users who have posted on the forum), we can save that json response as response.json and filter out the emails of users:

Also, using this grep command should pull everything out of a file that resembles an email. Then you can save those captured emails to a file and use that file as a payload in Burp Suite. You can then use a command like sort -u to get rid of duplicate emails.

```bash
grep -oe "[a-zA-Z0-9._]\+@[a-zA-Z]\+.[a-zA-Z]\+" response.json | uniq | sort -u > mailusers.txt
```


## API Authentication Attacks

To go further in authentification attacks we will need to analyze the API tokens and the way they are generated, and when talking about token generation and analysis, a word comes out inmediately: **entropy**.

*Entropy definition: Entropy, in cyber security, is a measure of the randomness or diversity of a data-generating >


### Entropy analysis: BurpSuite Sequencer's live capture

BurpSuite Sequencer provides two methods for token analysis:

+ Manually analysing tokens provided in a text file. To perform a manual analys, you need to provide to BurpSuite Sequencer a minimum of 100 tokens.
+ Performing a live capture to automatically generate tokens.

Let's focus out attention on a live capture using BurpSuite Sequencer. A live capture  will provide us with 20.000 tokens automatically generated. What for?

+ To elaborate a token analysis report that measures the entropy of the token generation process (and gives us precious tips about how to brute-force, or password spray, or bypass the authentication). For instance, if an API provider is generating tokens sequentially, then even if the token were 20 plus characters long, it could be the case that many of the characters in the token do not actually change.
+ To have this large collection of 20.000 identities can help us to evade security controls.


**The token analysis report**

+ *The summary of the findings* provides info about the quality of randomness within the token sample. The goal is to determine if there are parts of the token that do not change and other parts that often change. So full entropy would be a 100% of ramdonness (any patterns found). 
+ *Character-level analysis* provides the degree of confidence in the randomness of the sample at each character position. The significance level at each position is the probability of the observed character-level results occurring.
* *Bit-level analysis* indicates the degree of confidence in the randomness of the sample at each bit position.


### JWT attacks

Two tools: [jwt.io](https://jwt.io) and [jwt_tools](https://github.com/ticarpi/jwt_tool).

To see a jwt decoded on your CLI:

```bash
jwt_tool eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJoYXBpaGFja2VyQGhhcGloYWNoZXIuY29tIiwiaWF0IjoxNjY5NDYxODk5LCJleHAiOjE2Njk
1NDgyOTl9.yeyJzdWIiOiJoYXBpaGFja2VyQGhhcGloYWNoZXIuY29tIiwiaWF0IjoxNjY5NDYxODk5LCJleHAiOjE2Njk121Lj2Doa7rA9oUQk1Px7b2hUCMQJeyCsGYLbJ8hZMWc7304aX_hfkLB__1o2YfU49VajMBhhRVP_OYNafttug 
```

Result:

{{< figure src="../../images/jwt-tool.png" title="Running JWT TOOL" width="600" >}}


Also, to see the decoded jwt, knowing that is encoded in base64, we could echo each of its parts:

```bash
echo eyJhbGciOiJIUzUxMiJ9 | base64 -d  && echo eyJzdWIiOiJoYXBpaGFja2VyQGhhcGloYWNoZXIuY29tIiwiaWF0
IjoxNjY5NDYxODk5LCJleHAiOjE2Njk1NDgyOTl9 | base64 -d
```

Results:

```
{"alg":"HS512"}{"sub":"hapihacker@hapihacher.com","iat":1669461899,"exp":1669548299} 
```

To run a JWT scan with jwt_tool, run: 

```bash
jwt_tool -t <http://target-site.com/> -rc "<Header>: <JWT_Token>" -M pb
# in the target site specify a path that leverages a call to a token
# replace Header with the name of the Header and JWT_Tocker with the actual token.
# -M: Scanning mode. 'pb' is playbook audit. 'er': fuzz existing claims to force errors. 'cc': fuzz common claims. 'at': All tests.
```


Some more jwt_tool flags that may come in hand:

```
# -X EXPLOIT, --exploit EXPLOIT
#                        eXploit known vulnerabilities:
#                        a = alg:none
#                        n = null signature
#                        b = blank password accepted in signature
#                        s = spoof JWKS (specify JWKS URL with -ju, or set in jwtconf.ini to automate this attack)
#                        k = key confusion (specify public key with -pk)
#                        i = inject inline JWKS

```


#### The none attack

A JWT with "none" as its algorithm is a free ticket. Modify user and become admin, root,... 
Also, in poorly implemented JWT, sometimes user and password can be found in the payload.

To craft a jwt with "none" as the value for "alg", run:

```bash
jwt_tool <JWT_Token> -X a
```


#### The null signature attack

Second attack in this section is removing the signature from the token. This can be done by erasing the signature altogether and leaving the last period in place.


#### The blank password accepted in signature

Launching this attack is relatively simple. Just remove the password value from the payload and leave it in blank. Then, regenerate the jwt.

Also, with jwt_tool, run:

```bash 
jwt_tool <JWT_Token> -X b
```
 
#### The algorithm switch (or key-confusion) attack

A more likely scenario than the provider accepting no algorithm is that they accept multiple algorithms. For example, if the provider uses RS256 but doesn’t limit the acceptable algorithm values, we could alter the algorithm to HS256. This is useful, as RS256 is an asymmetric encryption scheme, meaning we need both the provider’s private key and a public key in order to accurately hash the JWT signature. Meanwhile, HS256 is symmetric encryption, so only one key is used for both the signature and verification of the token. If you can discover the provider’s RS256 public key and then switch the algorithm from RS256 to HS256, there is a chance you may be able to leverage the RS256 public key as the HS256 key.

```bash
jwt_tool <JWT_Token> -X k -pk public-key.pem
# You will need to save the captured public key as a file on your attacking machine.
```


#### The jwt crack attack

JWT_Tool can still test 12 million passwords in under a minute. To perform a JWT Crack attack using JWT_Tool, use the following command:


```bash
jwt_tool <JWT Token> -C -d /wordlist.txt
# -C indicates that you are conducting a hash crack attack
# -d specifies the dictionary or wordlist
```

Once you crack the secret of the signature, we can create our own trusted tokens. 
1. Grab another user email (in the crapi app, from the data exposure vulnerability when getting the forum (GET {{baseUrl}}/community/api/v2/community/posts/recent).
2. Generate a token with the secret.


#### Spoofing JWS 

Specify JWS URL with -ju, or set in jwtconf.ini to automate this attack.


#### Inject inline JW

¿?¿?¿?¿?



## Setting up other labs
Besides "crapi" and "vapi", the book "Hacking APIs" indicates some other interesting labs. Following chapter 5 of Hacking APIs book ("Setting up vuñnerable API targets"), I have installed:

### vapi app writeups

Source: https://github.com/roottusk/vapi

APIs have become critical element of security landscape. In 2019, OWASP released a list of top 10 API Security vulnerabilities for the first time. Vapi stands for Vulnerable Adversely Programmed Interface, and it's a self-hostable PHP Interface that mimics OWASP API Top 10 scenarios.

**Install**

```bash
# Under /home/kali/labs
git clone https://github.com/roottusk/vapi.git
cd vapi
docker-compose up -d
# prerrequisite: having docker up and running
```

**Setting up Postman**

+ Go to https://www.postman.com/roottusk/workspace/vapi/ 
+ Locate and import vAPI.postman_collection.json in Postman
+ Locate and Import vAPI_ENV.postman_environment.json in Postman
+ Configure the collection to use vAPI_ENV

#### Writeup: API1

Tip provided by vAPI: Broken Object Level Authorization. You can register yourself as a User , Thats it ....or is there something more?
 
Solution:

+ Postman: Under folder API0, send a request to Create User. When done, the vAPI_ENV will be filled with two more variables: api1_id, api1_auth.
+ Postman: Under folder API1, send a request to Get User. Initially you will get the user that you have created. BUT if you modify the api1_id in the vAPI_ENV environment, then you will receive the data from (let's say) user with id 1. Or 2. Or 3. Or... Tadam! BOLA.
+ The flag is in user with id 1. See the response body:  

#### Writeup: API2

Tip provided by vAPI: Broken Authentication. We don't seem to have credentials for this , How do we login? (There's something in the Resources Folder given to you).


Solution:

+ Download creds.csv from https://raw.githubusercontent.com/roottusk/vapi/master/Resources/API2_CredentialStuffing/creds.csv.
+ Execute:

```bash
cat creds.csv | cut -d, -f1 >users.txt
cat creds.csv | cut -d, -f3 >pass.txt
```

+ Intercept in mode ON in Burp, enable foxyproxy at 8080 in the browser, and enable proxy in Postman at 8080.
+ Postman: Under  folder API2, send a POST request to login and intercept it with Burp.
+ Burp: send the request to Intruder. Use Pitchfork attack with two payloads (Simplelist). One will be users.txt and second payload, pass.txt. Careful, remove the url encoding when setting up the payloads.
+ Burp: sort by Code (or length). You will get credentials for three users.
+ Postman: Login with the credentials of every user and save the file as an example just in case that you need to go back to this.
+ Postman: Once you are login into the app, a new enviromental variable has been saved in vAPI_ENV: api2_auth. With this authentication now we can sesend the request Get Details. Flag will be in the response.

#### Writeup: API3

#### Writeup: API4

#### Writeup: API5

#### Writeup: API6

#### Writeup: API7

#### Writeup: API8

#### Writeup: API9

#### Writeup: API10


### OWASP DevSlop Pixi

Pixi is a MongoDB, Express.js, Angular, Node (MEAN) stack web applica­tion that was designed with deliberately vulnerable APIs.


To install it:

```bash
cd ~/lab.
git clone https://github.com/DevSlop/Pixi.git
```

To run it:

```bash
cd ~/lab
sudo docker-compose up
```

Now, in the browser, go to: http://localhost:8000/login


### OWASP Juice Shop

Juice Shop encompasses vulnerabilities from the entire OWASP Top Ten along with many other security flaws found in real-world applications.

To install, go to the github page (https://github.com/juice-shop/juice-shop) and follow the isntructions.

To run it:

```bash
sudo docker run --rm -p 3000:3000 bkimminich/juice-shop
```

Now, in the browser, go to: http://localhost:3000/#/


### Damn-Vulnerable-GraphQL-Application

Damn Vulnerable Web Services is a vulnerable application with a web service and an API that can be used to learn about webservices/API related vulnerabilities.

To install, see the github page: https://github.com/dolevf/Damn-Vulnerable-GraphQL-Application 

To run it:

```bash
sudo docker run -t -p 5013:5013 -e WEB_HOST=0.0.0.0 dvga
```

Now, in the browser, go to: http://localhost:5013/


## Exploiting API Authorization

### BOLA - Broken Object Level Authorization

BOLA vulnerability allows UserA to request UserB's resources.

{{< figure src="../../images/bola-endpoint.png" title="Some endpoints worth targeting" width="600" >}}

Methodology:
1. Create a UserA account.
2. Use the API and discover requests that involve resource IDs as UserA.
3. Document requests that include resource IDs and should require authorization.
4. Create a UserB account.
5. Obtaining a valid UserB token and attempt to access UserA's resources.

You could also do this by using UserB's resources with a UserA token.

### BFLA - Broken Function Level Authorization

BFLA is about UserA requesting to create, update, post or delete object values that belong to UserB.   

- BFLA request with lateral actions. UserA has the same role or privilege level than UserB.
- BFLA request with escalated actions. UserB has a privilege level and UserA is able to perform actions reserved for UserB.

Important: being careful with DELETE request.

Methodology:
1. Postman. Go through the collection and select requests for resources of UserA. Focus on resources for private information. 
2. Swap out your UserA token for UserB's.
3. Send GET, PUT, POST, and DELETE requests for UserA's resources using Userb's token.
4. Investigate code 200, 401, and responses with strange lengths.


BFLA pays special attention to requests that perform authorized actions. 

Tools: 
+ Postman: ue the collection variables. Create specific collections for attacks.
+ BurpSute: use the Match and Replace functionality (tab PROXY>OPTIONS) to perform a large-scale replacement of a variable like an authorization token.


## Testing for Improper assets management

Testing for Improper Assets Management is all about discovering unsupported and non-production versions of an API. 

Paths to check out:

+ api.target.com/v3
+ /api/v2/accounts
+ /api/v3/accounts
+ /v2/accounts

API versioning could also be maintained as a header:

+ Accept: version=2.0
+ Accept api-version=3

In addition versioning could also be set within a query parameter or request body.

```
/api/accounts?ver=2
POST /api/accounts

{
"ver":1.0,
"user":"hapihacker";
}
```

The discovery of non-production versions of an API might not be treated with the same security controls as the production version. 

### Methodology

We'll use postman. We are assuming that we have build our collection of requests and that we have identify those parameters regarding API version.

1. Run a test "Status code: Code is 200". In your collection options, go to tab Test and select the option that gives you this code:

```
pm.test("Status code is 200", function () { pm.response.to.have.status(200); })
```

2. Run an unauthenticated baseline scan of the crAPI collection with the Collection Runner. Make sure that "Save Responses" is checked. Important. Review the results from your unauthenticated baseline scan to have an idea of how the API provider responds to requests using supported production versioning.
3. Next, use "Find and Replace" to turn the collection's current versions into a variable. For that, use Environmental variables.
4. Run the collection with the variable set to v1, v2, v3, mobile, internal, test, uat..., and check out the different responses.

```
In the course, we are using the crAPI app, and by replicating these steps you can spot different code responses for the request {{base_url}}/identity/api/auth/{{var}}/check-otp.
/v1 received a 404 Not Found
/v2 received a 500 response
/v3 received a 500 response

Also, body response in /v2 is different from body response in /v3: 

The /v2 password reset request responds with the body (left):
{"message":"Invalid OTP! Please try again..","status":500}

The /v3 password reset request responds with the body (right):
{"message":"ERROR..","status":500}

That might be a sign of improper assets management. Going further and testing it, you can discover that /v2 does not have a limitation on the number of times we can guess the OTP. With a four-digit OTP, we should be able to brute force the OTP within 10,000 requests. Since this endpoint manages resetting passwords, in the end this vulnerability allows you to gain control on any account in the system. 
```


## Mass Assignment. Coming up next 11 Dec.

*What is mass asset management?* Basically UserA is said in the frontend to have the ability to post/update an object and we use that request to post/update a different object. We are sending a request that updates or overwrites server-side variables.
 

## Server side Request Forgery. Coming up next 11 Dec.

## Injection Attacks. Coming up next 18 Dec.

## Evasion and Combining techniques. Coming up next 19 Dec.

## Conclusion. Coming up next 19 Dec.




