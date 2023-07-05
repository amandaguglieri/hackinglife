---
title: uploadserver
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - file transfer technique
---

# uploadserver

Python's http.server extended to include a file upload page

## Installation

Download from github repo: [https://github.com/Densaugeo/uploadserver](https://github.com/Densaugeo/uploadserver).

```bash
python3 -m pip install --user uploadserver
```


## Basic usage 


```bash
python3 -m uploadserver
```

Accepts the same options as http.server. After the server starts, the upload page is at /upload. For example, if the server is running at http://localhost:8000/ go to http://localhost:8000/upload .

Now supports uploading multiple files at once! Select multiple files in the web page's file selector, or upload with cURL:

```bash
curl -X POST http://127.0.0.1:8000/upload -F 'files=@multiple-example-1.txt' -F 'files=@multiple-example-2.txt'
```

See an example in [File Transfer techniques for Linux](transferring-files-techniques-linux.md).
