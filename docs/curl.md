---
title: curl
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - bash
  - tools
  - pentesting
---

## Basic usage

```bash
curl -i -L $host -v
# -L: Follow redirections
# -i: Include headers in the response 
# -v: verbose

curl -T file.txt
# -T, --upload-file <file>; This transfers the specified local file to the remote URL. -T uses PUT http method

curl -o target/path/filename URL
# -o: to specify a location/filename

# Upload a File
curl -F "Filedata=@./shellsample.php" URL

# Sends a GET request
curl -X GET $ip

# Sends a HEAD request
curl -l  $ip

# Sends a OPTIONS request
curl -X OPTIONS  $ip

# Sends a POST request with parameters name and password in the body data
curl -X POST  $ip -d "name=username&password=password" -v

# Upload a file with a PUT method
curl $ip/uploads/ --upload-file hello.txt

curl -XDELETE $ip/uploads/hello.txt
# Delete a file
```