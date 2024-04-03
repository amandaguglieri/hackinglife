---
title: Test Upload of Unexpected File Types - OWASP Web Security Testing Guide 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - WSTG-BUSL-08
---
# Test Upload of Unexpected File Types

??? quote "OWASP"
	[OWASP Web Security Testing Guide 4.2](index.md) > 10. Business logic Testing > 10.8. Test Upload of Unexpected File Types 

	|ID|Link to Hackinglife|Link to OWASP|Description|
	|:---|:---|:---|:---|
	|10.8|[WSTG-BUSL-08](WSTG-BUSL-08.md)|[Test Upload of Unexpected File Types](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/08-Test_Upload_of_Unexpected_File_Types)|- Review the project documentation for file types that are rejected by the system.  - Verify that the unwelcomed file types are rejected and handled safely. Also, check whether the website only check for "Content-type" or file extension.  - Verify that file batch uploads are secure and do not allow any bypass against the set security measures.|


## See my notes on Arbitrary File Upload

[See my notes on Arbitrary File Upload](../webexploitation/arbitrary-file-upload.md)

