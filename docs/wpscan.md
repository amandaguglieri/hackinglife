---
title: wpscan - Wordpress Security Scanner
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
  - enumeration
  - wordpress
---

# wpscan - Wordpress Security Scanner

## Installation

Preinstalled in kali. 

See the repo: [https://github.com/wpscanteam/wpscan](https://github.com/wpscanteam/wpscan).

WPScan keeps a local database of metadata that is used to output useful information, such as the latest version of a plugin. The local database can be updated with the following command:

```bash
wpscan --update
```

## Basic commands

```bash

# Using the API token after registering an account at wpscan
wpscan --url http://target.tld --enumerate --api-token f34R3...[SNIP

# Enumerate users
wpscan --url https://target.tld/domain --enumerate u
wpscan --url https://target.tld/ -eu

# Enumerate a range of users 1-100
wpscan --url https://target.tld/ --enumerate u1-100
wpscan --url http://46.101.13.204:31822 --plugins-detection passive

# Brute force attack on login page with passwords:
wpscan --url HOST/domain -usernames admin, webadmin  --password-attack wp-login -passwords filename.txt
# -usernames: those users that you are going to brute force
# --password-attack: your URI target (different in the case of the WP api
# -passwords: path/to/dictionary.txt

# Brute force attack on xmlrpc with passwords:
wpscan --password-attack xmlrpc -t 20 -U username1, username2 -P PATH/TO/passwords.txt --url http://<TARGET>
# -t: Threads in use. Default is 5

# Enumerate plugins on pasive mode 
wpscan --url https://target.tld/ --plugins-detection passive 
# Modes: -mixed (default), -passive or -active

# Common flags
# 	vp (Vulnerable plugins)
#	ap (All plugins)
# 	p (Popular plugins)
#	vt (Vulnerable themes)
#	at (All themes)
#	t (Popular themes)
#	tt (Timthumbs)
# 	cb (Config backups)
#	dbe (Db exports)
# 	u (User IDs range. e.g: u1-5)
#	m (Media IDs range. e.g m1-15)

# Ignore HTTPS Certificate
--disable-tls-checks

```


Troubleshooting for the following error message:

```
in `<module:LoggerThreadSafeLevel>': uninitialized constant ActiveSupport::LoggerThreadSafeLevel::Logger (NameError)

    Logger::Severity.constants.each do |severity|
```

We can  manually specify logger

```
RUBYOPT='-rlogger' wpscan --url http://blog.inlanefreight.local 
```


This forces Ruby to load the logger module.



## Examples from labs:


```bash
# Raven 1 machine
wpscan --url http://192.168.56.104/wordpress --enumerate u --force --wp-content-dir wp-content
```


