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
# Curl

[cURL](https://curl.haxx.se/) (client URL) is a command-line tool and library that primarily supports HTTP along with many other protocols.  This makes it a good candidate for scripts as well as automation, making it essential for sending various types of web requests from the command line, which is necessary for many types of web penetration tests.

## Basic usage

```bash
# Download a web page. In this example, downloading index.html
curl -O example.com/index.html

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

# Skip the certificate check with cURL
curl -k https://example.com

# Sends a GET request
curl -X GET $ip

# Sends a HEAD request
curl -I $ip

# Sends a OPTIONS request
curl -X OPTIONS  $ip

# Sends a POST request with parameters name and password in the body data
curl -X POST  $ip -d "name=username&password=password" -v

# Upload a file with a PUT method
curl $ip/uploads/ --upload-file hello.txt

curl -XDELETE $ip/uploads/hello.txt
# Delete a file

# Send an HTTP/3 request:
curl --http3 -v https://examplecom/users/login.html
```

Some flags:

```
-s: silent the status
-h/--help: help
```


### Handling authorization with CURL

Basic HTTP auth:

```
curl -u admin:admin http://<SERVER_IP>:<PORT>/

curl http://admin:admin@<SERVER_IP>:<PORT>/
```

Authorization header:

```
curl -H 'Authorization: Basic YWRtaW46YWRtaW4=' http://<SERVER_IP>:<PORT>/
```