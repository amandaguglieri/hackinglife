---
title: BloodHound
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active directory
  - ldap
  - windows
  - enumeration
  - reconnaissance
  - tools
---
# BloodHound

(C# and PowerShell Collectors)

BloodHound is a single page Javascript web application, built on top of [Linkurious](http://linkurio.us/), compiled with [Electron](http://electron.atom.io/), with a [Neo4j](https://neo4j.com/) database fed by a C# data collector.

Download github repo from: [https://github.com/BloodHoundAD/BloodHound](https://github.com/BloodHoundAD/BloodHound).

Sharphound is the official data collector for BloodHound.

```bash
sudo apt-get install bloodhound
```

Initialize the console:

```bash
sudo neo4j console 
```

Open the browser at the indicated address: http://localhost:7474/

The first time it will ask you for default user and password:  neo4j:neo4j.

After loging into the application you will be prompted to change default password. We will use later this password to enter the Bloodhound tool.

Upload and install the bloodhound binary into the foothold: [releases](https://github.com/SpecterOps/BloodHound-Legacy/releases).

If bloodhound is already installed, you can run the [bloodhound.py](https://github.com/dirkjanm/BloodHound.py) in the foothold machine: 

```shell-session
sudo bloodhound-python -u '$username' -p '$password' -ns $ip -d $domain -c all 
# -u: username
# -p: password
# -ns: name server
# -d: domain
# -c: checks. With -c all we are telling the tool to run all checks.

# Once the script finishes, we will see the output files in the current working directory in the format of <date_object.json>.
```

Move the json files to where you have your blodhound tool installed. Open bloodhound, we should have the BloodHound GUI tool loaded with a blank slate. 

```bash
# Launch Bloodhound interface from your kali attacker machine.
bloodhound
# enter user:password already set before for the neo4j console.
```


Now we need to upload the data. We can either upload each JSON file one by one or zip them first with a command such as `zip -r ilfreight_bh.zip *.json` and upload the Zip file. We do this by clicking the `Upload Data` button on the right side of the window.

## Basic usage

Along with the Analytics tab, we can do some  [custom Cypher queries](https://hausec.com/2019/09/09/bloodhound-cypher-cheatsheet/).
