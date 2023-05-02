---
title: File Upload
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
---

# File Upload


## Cheat sheet for php 

Source: [Repo from imran-parray](https://github.com/imran-parray/Web-Sec-CheatSheet/blob/master/File-Upload-test.txt)
OWASP deep explanation: [link](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)

```
# try to upload a simple php file
upload.php 

# To bypass the blacklist.
upload.php.jpeg 

# To bypass the blacklist.
upload.jpg.php
#  and Then Change the content type of the file to image or jpeg.
upload.php 

# version - 1 2 3 4 5 6 7
upload.php*

# To bypass The BlackList
upload.PHP 
upload.PhP 
upload.pHp 

#  By uploading this [jpg,png] files can be executed as php with milicious code within it.
upload .htaccess

# To test againt the DOS.
pixelFlood.jpg

#  upload gif file with 10^10 Frames
frameflood.gif

# upload UBER.jpg
Malicious zTXT 

# Add backdoor in comments using Exiftool and 
upload.php [getimagesize() 
# rename the jpg file with php so that it will be execute. This Time The Verification of server is only limited to contents of the uploaded file not on the extension

# backdoor in php chunks
phppng.png 

# backdoor in php chunks 
xsspng.png 


```