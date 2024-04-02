---
title: Testing for Session Hijacking - OWASP Web Security Testing Guide 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - WSTG-SESS-09
---
# Testing for Session Hijacking

!!! quote ""
	[OWASP Web Security Testing Guide 4.2](index.md) > 6. Session Management Testing > 6.9. Testing for Session Hijacking

|ID|Link to Hackinglife|Link to OWASP|Description|
|:---|:---|:---|:---|
|6.9|[WSTG-SESS-09](WSTG-SESS-09.md)|[Testing for Session Hijacking](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/09-Testing_for_Session_Hijacking)|- Identify vulnerable session cookies.  - Hijack vulnerable cookies and assess the risk level.|

An attacker who gets access to user session cookies can impersonate them by presenting such cookies. This attack is known as session hijacking. 

## Testing

The testing strategy is targeted at network attackers, hence it only needs to be applied to sites without full HSTS adoption (sites with full HSTS adoption are secure, since their cookies are not communicated over HTTP).  

We assume to have two testing accounts on the website under test, one to act as the victim and one to act as the attacker. We Web Security Testing Guide v4.2 214 simulate a scenario where the attacker steals all the cookies which are not protected against disclosure over HTTP, and presents them to the website to access the victim’s account. If these cookies are enough to act on the victim’s behalf, session hijacking is possible.


Steps for executing this test: 
1. Login to the website as the victim and reach any page offering a secure function requiring authentication.
2. Delete from the cookie jar all the cookies which satisfy any of the following conditions. in case there is no HSTS adoption: the Secure attribute is set. in case there is partial HSTS adoption: the Secure attribute is set or the Domain attribute is not set. 
3. Save a snapshot of the cookie jar. 
4. Trigger the secure function identified at step 1. 
5. Observe whether the operation at step 4 has been performed successfully. If so, the attack was successful. 
6. Clear the cookie jar, login as the attacker and reach the page at step 1. 
7. Write in the cookie jar, one by one, the cookies saved at step 3. 
8. Trigger again the secure function identified at step 1. 
9. Clear the cookie jar and login again as the victim. 
10. Observe whether the operation at step 8 has been performed successfully in the victim’s account. If so, the attack was successful; otherwise, the site is secure against session hijacking.


## Mitigation

- Full HSTS adoption. 
