---
title: Testing for improper assets management
author: amandaguglieri
draft: false
TableOfContents: true
---

# Testing for improper assets management

Testing for improper assets management is all about discovering unsupported and non-production versions of an API. 

## Finding API versions

Paths to check out:

+ api.target.com/v3
+ /api/v2/accounts
+ /api/v3/accounts
+ /v2/accounts

API versioning could also be maintained as a header:

+ Accept: version=2.0
+ Accept api-version=3

In addition versioning could also be set within a query parameter or request body.

```
/api/accounts?ver=2
POST /api/accounts

{
"ver":1.0,
"user":"hapihacker";
}
```

The discovery of non-production versions of an API might not be treated with the same security controls as the production version. 


## Exploiting non-production, old and deprecate api versions

We'll use postman. We are assuming that we have build our collection of requests and that we have identify those parameters regarding API version.

**1.** Run a test "Status code: Code is 200". In your collection options, go to tab Test and select the option that gives you this code:

```
pm.test("Status code is 200", function () { pm.response.to.have.status(200); })
```

**2.** Run an unauthenticated baseline scan of the crAPI collection with the Collection Runner. Make sure that "Save Responses" is checked. Important. Review the results from your unauthenticated baseline scan to have an idea of how the API provider responds to requests using supported production versioning.

**3.** Next, use "Find and Replace" to turn the collection's current versions into a variable. For that, use Environmental variables.

**4.** Run the collection with the variable set to v1, v2, v3, mobile, internal, test, uat..., and check out the different responses.


```
In the course, we are using the crAPI app, and by replicating these steps you can spot different code responses for the request {{base_url}}/identity/api/auth/{{var}}/check-otp.
/v1 received a 404 Not Found
/v2 received a 500 response
/v3 received a 500 response

Also, body response in /v2 is different from body response in /v3: 

The /v2 password reset request responds with the body (left):
{"message":"Invalid OTP! Please try again..","status":500}

The /v3 password reset request responds with the body (right):
{"message":"ERROR..","status":500}

That might be a sign of improper assets management. Going further and testing it, you can discover that /v2 does not have a limitation on the number of times we can guess the OTP. With a four-digit OTP, we should be able to brute force the OTP within 10,000 requests. Since this endpoint manages resetting passwords, in the end this vulnerability allows you to gain control on any account in the system. 
```
