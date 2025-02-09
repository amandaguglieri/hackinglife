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

## 1. Installation in the attacking machine

(C# and PowerShell Collectors)

BloodHound is a single page Javascript web application, built on top of [Linkurious](http://linkurio.us/), compiled with [Electron](http://electron.atom.io/), with a [Neo4j](https://neo4j.com/) database fed by a C# data collector.

Download github repo from: [https://github.com/BloodHoundAD/BloodHound](https://github.com/BloodHoundAD/BloodHound).

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

## 2. Collecting data in the foothold machine

Upload and install the bloodhound binary into the foothold: [releases](https://github.com/SpecterOps/BloodHound-Legacy/releases).

### 2.1. Bloodhound.py
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

### 2.2. Sharphound.exe

Sharphound is the official data collector for BloodHound.

We run the SharpHound.exe collector from the attack host (our foothold).

```powershell
.\SharpHound.exe -c All --zipfilename $zipName
# -c: checks. With -c all we are telling the tool to run all checks.
# --zipfilename: saves all to a file, named $zipName
```



## 3. Using bloodhound 

In our attacker machine we had launched the neo4j database. Now we need to launch bloodhound, and import the generated by the collector files to be interpreted.

Move the json files to where you have your blodhound tool installed. Open bloodhound, we should have the BloodHound GUI tool loaded with a blank slate. 

```bash
# Launch Bloodhound interface from your kali attacker machine.
bloodhound
# enter user:password already set before for the neo4j console.
```


Now, we upload the data. We can either upload each JSON file one by one or zip them first with a command such as `zip -r ilfreight_bh.zip *.json` and upload the Zip file. We do this by clicking the `Upload Data` button on the right side of the window.

Along with the Analytics tab, we can do some  [custom Cypher queries](https://hausec.com/2019/09/09/bloodhound-cypher-cheatsheet/).

- `Find Computers with Unsupported Operating Systems` is great for finding outdated and unsupported operating systems running legacy software.
- `Find Computers where Domain Users are Local Admin` to quickly see if there are any hosts where all users have local admin rights.

We can also type `domain:` in the search bar and select one.


### Enumerate  Remote Desktop Users Group

In Bloodhound, we can use this Cypher query and add it as a custom query:

```cypher
MATCH p1=shortestPath((u1:User)-[r1:MemberOf*1..]->(g1:Group)) MATCH p2=(u1)-[:CanPSRemote*1..]->(c:Computer) RETURN p2
```


### Enumerate  SQL Server Admin

Enumerate via Bloodhound and the `SQLAdmin` edge. We can check for `SQL Admin Rights` in the `Node Info` tab for a given user or use this custom Cypher query to search:

```cypher
MATCH p1=shortestPath((u1:User)-[r1:MemberOf*1..]->(g1:Group)) MATCH p2=(u1)-[:SQLAdmin*1..]->(c:Computer) RETURN p2
```


### Visualizing Trust Relationships in BloodHound

![](img/blood02.png)

