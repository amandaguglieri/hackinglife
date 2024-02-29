---
title: Mobile Security Framework - MobSF
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - mobile pentesting
---

# Mobile Security Framework - MobSF

Mobile Security Framework (MobSF) is an automated, all-in-one mobile application (Android/iOS/Windows) pen-testing, malware analysis and security assessment framework capable of performing static and dynamic analysis. MobSF supports mobile app binaries (APK, XAPK, IPA & APPX) along with others


## Installation

1. Install Git using below provided command in terminal

```bash
sudo apt-get install git
```

2. Install Python 3.8/3.9 using below provided command

```bash
sudo apt-get install python3.8**
```

3. Install latest version of **JDK**

Download from: [https://www.oracle.com/java/technologies/javase-java-archive-javase6-downloads.html](https://www.oracle.com/java/technologies/javase-java-archive-javase6-downloads.html)

Then: 
```bash
chmod +x jdk-6u45-linux-x64.bin
sh jdk-6u45-linux-x64.bin      
```


4. Install the required dependencies using below provided command

```bash
sudo apt install python3-dev python3-venv python3-pip build-essential libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg62-turbo-dev zlib1g-dev wkhtmltopdf
```

5. Download **MobSF** using below provided command

```bash
git clone https://github.com/MobSF/Mobile-Security-Framework-MobSF.git
```




Setup MobSF using command:

```
sudo ./setup.sh
```


Run!

```bash
./run.sh 127.0.0.1:8000

# Note: we can use any port number instead of **8000**, but it must be available
```


Access the MobSF web interface in browser using the URL: [**http://127.0.0.1:8000**](http://127.0.0.1:8000)