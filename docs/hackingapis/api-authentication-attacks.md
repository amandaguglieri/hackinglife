---
title: API authentication attacks
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - api
---

# API authentication attacks

??? abstract "General index of the course"
    - [Setting up the environment](setting-up-kali.md)
    - [Api Reconnaissance](api-reconnaissance.md).
    - [Endpoint Analysis](endpoint-analysis.md).
    - [Scanning APIS](scanning-apis.md).
    - [API Authorization Attacks](api-authentication-attacks.md).
    - [Exploiting API Authorization](exploiting-api-authorization.md).
    - [Testing for Improper Assets Management](improper-assets-management.md).
    - [Mass Assignment](mass-assignment.md).
    - [Server side Request Forgery](server-side-request-forgery-ssrf.md).
    - [Injection Attacks](injection-attacks.md). 
    - [Evasion and Combining techniques](evasion-combining-techniques.md).
    - [Setting up the labs + Writeups](other-labs.md)


## API Authentication

### Authentication Types

- Basic Authentication: username and password base64 encoded included as a HTTP Authorization header in the request:

```
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
```

- API Keys: there is no standard way to present the API Keys. Usually they go as a HTTP header.
- Certificate based authentication: Using TLS for authentication. It requires HTTPS and requires the API to present a certificate. 
- Token based authentication: issued by a third party. Tokens are used to authenticate the caller, they can expire, they can have an audience. 
- Token based authentication and authorization: Tokens can contains more information than caller id. OAuth uses scopes, OpenID Connect adds claims.


### OAuth 1 and 2.0

- OAuth 1: IETF standard in 2010. Driven by twitter and google. It does not require HTTPS. Difficult to implement.
- OAuth 2: IETF standard in 2012. Widely adopted. It requires HTTPS. Easy to implement.
- OAuth 2.1: underway

The application accesses to the API on user's behalf without seeing the credentials. The user can revoke this delegation. Actors:
- Resource owner
- The Authorization server delegates access to the Client so it can access the resource server.
- Client
- Resource server.

**Code flow: grant_type=authorization_code**

![Code flow](../../img/auth-sequence-auth-code-pkce.png)

1. The user visit the application and clicks on login.
2. The application generates `Code Verifier`and `Code Challenge`.
3. The application redirects the user to an endpoint `/authorize` in the Authorization Server with the following parameters:

```HTTP
GET /authorize
	?response_type=code
	&client_id=myApp  // but we don't prove that this is the real id of the application
	&scope=read
	&code_challenge=MY_CHALLENGE
	&code_challenge_method=S256   // Also called PKCE
	&state=MY_RANDOM_STATE   // it will be sent back to the client
```

PKCE stands for Proof Key for Code Exchange (PKCE).

4. The Authorization Server takes the user to their own Authentication Service (with their own authentication flow).
5. If successful, ...
6. the Authorization Server will redirect back to a predefined callback within the client:

```HTTP
303 /callback
?code=1234  // this is also called 'nonce' (no more than once). A one-time-code with a really short life
&state=MY_RANDOM_STATE
```

7. The client makes a back channel call to the Authorization Server to validate the Code verifier and the challenge.

```HTTP
POST /token
Content-type: application/x-www-form-urlencoded

grant_type=authorization_code //to tell we want to do the code flow
&client_id=myApp 
&client_secret=vErys3crEt //this can be also passed in an Authorization Basic header, or tokens or...
&code_verifier=MY_VERIFIER // This is the actual value of what we sent in the /authorization request. This is what binds these requests together
&code=1234
```

This happens in less than 30 seconds.

8. The Authorization Server evaluates the previous request.
9. The Authorization Server issues a token:

```json
{
"access token": "abcDEF",
"scope": "read",
"expires_in": 300,
"refresh_token": "HJKSGFD",
"token_type": "bearer"
}
```


**Code flow: grant_type=client_credentials**

Everything is as in the previous code flow, but in step 7, there is a deviation:

7. The client makes a back channel call to the Authorization Server to validate the Code verifier and the challenge.

```HTTP
POST /token
Content-type: application/x-www-form-urlencoded

grant_type=client_credentials //to tell we want to do the client credentials flow
&client_id=myserverApp 
&client_secret=vErys3crEt 
&cope=read
```

8. In this case, there is no user interaction. We don't get a refresh token.

```json
{
"access_token": "_0XBPWQQ_1c51e9ed-8979-4c53-af17-159476e1d9fc",
"scope": "read write",
"token_type": "bearer",
"expires_in": 299
}
```


### Tokens

**Types of tokens**

Bearer Tokens: not binded to a sender. 
Proof of Possession Tokens (PoP) or Holder of Key Tokens (HoK): The sender needs to present a proof of ownership (prove that they have the private key)

```
# Bearer tokens
Authorization: Bearer ey...

# PoP tokens
Authorization: DPoP _023123jdkjhjsdehe234bscdks-
DPoP: eyJ0xXAi...4UcbQ
```

**JSON Web Tokens (JWT)**

Not a protocol, but a format. JWT can be:

- **Signed** JWS: proves who issued the token, asymmetric signature, whitelist algorithms allowed. Doesn't rely exclusively on signature, it also verifies contents as well.
- **Encrypted** JWE: keeps data confidential, used in OpenID Connect, ID tokens. Not practical for access tokens. Opaque tokens are preferred to keep confidentiality. 

### Scopes vs Claims

**Scopes** define what the application can access. They are just a set of strings (they are keys, not values). They can be requested by the client. The Authorization Server makes the final decision about if a scope should be issued with the token. Scopes are used to express client privileges (and not user level privileges). 

Examples: read, openid, user_invoice_read...

**Claims** are key value items inside the token and the are asserted by the issuer, which means that it can be used for fine grained access control.

Examples: subject=jacob, age=23, suscription_level=gold...

### Gateways and APIs

They provide a layer of protection in layer 7 (firewalls - HTTP). 

#### Introspection with exchange: Pure introspection

When we want to send a request to an API and there is a Gateway in the middle and the token is opaque (format by reference), then this gateway makes a connection with the Authorization Server to validate this token:

```
POST /instrospection
Content-type: application/x-www-form-urlencoded


&client_id=gateway_client
&client_secret=vErys3crEt
&token=HJKLM
```

The Authorization Server returns a json with the value of the token

```json
{
"sub": "admin",
"purpose": "access_token",
"iss": "https://issuer.example.com/~",
"active": true,
"token_type": "bearer",
"client_id": "client-1",
"aud": "api123",
"nbf": 15465771377,
"scope": "read",
"exp":15465771677,
"delegationId": "cg572fad-0000-0000-0000-00000000",
"iat": 15465771377
}
```


#### Introspection with exchange: Embedded token in JSON introspection

Or the client indicates to the gateway that they want the jwt back, even embedded into the json:

```
POST /instrospection
Content-type: application/x-www-form-urlencoded
Accept: application/jwt

&client_id=gateway_client
&client_secret=vErys3crEt
&token=HJKLM
```

The Authorization Server returns a json with the value of the token

```json
{
"sub": "admin",
"purpose": "access_token",
"iss": "https://issuer.example.com/~",
"active": true,
"token_type": "bearer",
"client_id": "client-1",
"aud": "api123",
"nbf": 15465771377,
"scope": "read",
"exp":15465771677,
"delegationId": "cg572fad-0000-0000-0000-00000000",
"iat": 15465771377,
"jwt": "ey....."
}
```

#### Introspection with exchange: token exchange

We can also use Token exchange specification, which is fairly new and it allows the gateway to call the Authorization Server and, given the token, ask for a different kind of token. The implementation of the different kinds of token are defined in the Authorization server and the documentation for this implementation should be consulted.

```
POST /instrospection
Content-type: application/x-www-form-urlencoded

&client_id=gateway_client
&client_secret=vErys3crEt
&grant_type=urn:ietf:params:oauth:grant-type:token-exchange
&subject_token=HIJKLM
&subject_token_type=urn:ietf:params:oauth:token-type:access_token
&requested_token_type=urn:ietf:params:oauth:token-type:jwt
```


### API to API calls

- Exchange: Use token exchange to get another token. This is used on demand. It has powerful options.
- Embed: Put tokens inside the first token. When it is known to happen on every request.
- Shared: Shared JWT. When the APIs are in the same security domain.



## Classic authentication attacks

We'll consider two attacks: Password Brute-Force Attack, and Password Spraying. These attacks may take place every time that Basic Authentication is deployed in the context of a RESTful API.

The principle of Basic authentication is that the consumer issues a request containing a username and password. 

As RESTful APIs don't maintain a state, the API need to leverage basic authentication across all endpoints. Instead of doing this, the API may leverage basic authentication once using an authentication portal, then upon providing the correct credentials, a token would be issued to be used in subsequent requests.
 
### 1. Password Brute-Force Attacks

Brute-forcing an API's authentication is not very different from any other brute-force attack, except you will send the request to an API endpoint, the payload will often be in JSON, and the authentication values may be base64 encoded.

Infinite ways to do it. You can use: 

+ Intruder module of BurpSuite.
+ [ZAP proxy tool](../owasp-zap.md).
+ [wfuzz](../wfuzz.md).
+ [ffuf](../ffuf.md). 
+ [others](../OWASP/index.md).

Let's see [wfuzz](../wfuzz.md):

```bash
wfuzz -d {"email":"hapihacker@hapihacjer.com","password":"PASSWORD"} -z file,/usr/share/wordlists/rockyou.txt -u http://localhost:8888/identity/api/auth/login --hc 500
# -H to specify content-type headers. 
# -d allows you to include the POST Body data. 
# -u specifies the url
# --hc/hl/hw/hh hide responses with the specified code/lines/words/chars. In our case, "--hc 500" hides 500 code responses.
# -z specifies a payload   
```

Tools to build password lists:
+ [https://github.com/sc0tfree/mentalist](https://github.com/sc0tfree/mentalist).
+ [CUPP - Common User Password Profiler](../cupp-common-user-password-profiler.md).
+ [crunch](../crunch.md) (already installed in kali).

### 2. Password Spraying

Very useful if you know the password policy of the API we are attacking. Say that there is a lockout account policy for ten tries. Then you can password spray attack with 9 tries and use for that the 9 most probable passwords for all the accounts email spotted.

As in crapi we have detected before a disclosure of information in the forum page (a json response with all kind of data from users who have posted on the forum), we can save that json response as response.json and filter out the emails of users:

Also, using this grep command should pull everything out of a file that resembles an email. Then you can save those captured emails to a file and use that file as a payload in Burp Suite. You can then use a command like sort -u to get rid of duplicate emails.

```bash
grep -oe "[a-zA-Z0-9._]\+@[a-zA-Z]\+.[a-zA-Z]\+" response.json | uniq | sort -u > mailusers.txt
```


## API Authentication Attacks

To go further in authentification attacks we will need to analyze the API tokens and the way they are generated, and when talking about token generation and analysis, a word comes out inmediately: **entropy**.


### Entropy analysis: BurpSuite Sequencer's live capture

[Instructions to set up a proxy in Postman to intercept traffic with BurpSuite](../proxies.md) and have it sent to Sequencer.

Once you send a POST request (in which a token is generated) to Sequencer, **you need to define the custom token location** in the context menu. After that you can  click on "Start Live Capture".

BurpSuite Sequencer provides two methods for token analysis:

+ Manually analysing tokens provided in a text file. To perform a manual analys, you need to provide to BurpSuite Sequencer a minimum of 100 tokens.
+ Performing a live capture to automatically generate tokens.

Let's focus out attention on a live capture using BurpSuite Sequencer. A live capture  will provide us with 20.000 tokens automatically generated. What for?

+ To elaborate a token analysis report that measures the entropy of the token generation process (and gives us precious tips about how to brute-force, or password spray, or bypass the authentication). For instance, if an API provider is generating tokens sequentially, then even if the token were 20 plus characters long, it could be the case that many of the characters in the token do not actually change.
+ To have this large collection of 20.000 identities can help us to evade security controls.


**The token analysis report**

+ *The summary of the findings* provides info about the quality of randomness within the token sample. The goal is to determine if there are parts of the token that do not change and other parts that often change. So full entropy would be a 100% of ramdonness (any patterns found). 
+ *Character-level analysis* provides the degree of confidence in the randomness of the sample at each character position. The significance level at each position is the probability of the observed character-level results occurring.
* *Bit-level analysis* indicates the degree of confidence in the randomness of the sample at each bit position.


### JWT attacks

Two tools: [jwt.io](https://jwt.io) and [jwt_tools](../jwt-tool.md).

To see a jwt decoded on your CLI:

```bash
jwt_tool eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJoYXBpaGFja2VyQGhhcGloYWNoZXIuY29tIiwiaWF0IjoxNjY5NDYxODk5LCJleHAiOjE2Njk
1NDgyOTl9.yeyJzdWIiOiJoYXBpaGFja2VyQGhhcGloYWNoZXIuY29tIiwiaWF0IjoxNjY5NDYxODk5LCJleHAiOjE2Njk121Lj2Doa7rA9oUQk1Px7b2hUCMQJeyCsGYLbJ8hZMWc7304aX_hfkLB__1o2YfU49VajMBhhRVP_OYNafttug 
```

Result:

![jwt ](../img/jwt-tool.png)


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

![jwt ](../img/jwt-tool2.png)


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


#### 1. The none attack

A JWT with "none" as its algorithm is a free ticket. Modify user and become admin, root,... 
Also, in poorly implemented JWT, sometimes user and password can be found in the payload.

To craft a jwt with "none" as the value for "alg", run:

```bash
jwt_tool <JWT_Token> -X a
```


#### 2. The null signature attack

Second attack in this section is removing the signature from the token. This can be done by erasing the signature altogether and leaving the last period in place.


#### The blank password accepted in signature

Launching this attack is relatively simple. Just remove the password value from the payload and leave it in blank. Then, regenerate the jwt.

Also, with jwt_tool, run:

```bash 
jwt_tool <JWT_Token> -X b
```
 
#### 3. The algorithm switch (or key-confusion) attack

A more likely scenario than the provider accepting no algorithm is that they accept multiple algorithms. For example, if the provider uses RS256 but doesn’t limit the acceptable algorithm values, we could alter the algorithm to HS256. This is useful, as RS256 is an asymmetric encryption scheme, meaning we need both the provider’s private key and a public key in order to accurately hash the JWT signature. Meanwhile, HS256 is symmetric encryption, so only one key is used for both the signature and verification of the token. If you can discover the provider’s RS256 public key and then switch the algorithm from RS256 to HS256, there is a chance you may be able to leverage the RS256 public key as the HS256 key.

```bash
jwt_tool <JWT_Token> -X k -pk public-key.pem
# You will need to save the captured public key as a file on your attacking machine.
```


#### 4. The jwt crack attack

JWT_Tool can still test 12 million passwords in under a minute. To perform a JWT Crack attack using JWT_Tool, use the following command:


```bash
jwt_tool <JWT Token> -C -d /wordlist.txt
# -C indicates that you are conducting a hash crack attack
# -d specifies the dictionary or wordlist
```

Once you crack the secret of the signature, we can create our own trusted tokens. 
1. Grab another user email (in the crapi app, from the data exposure vulnerability when getting the forum (GET {{baseUrl}}/community/api/v2/community/posts/recent).
2. Generate a token with the secret.


#### 5. Spoofing JWS 

Specify JWS URL with -ju, or set in jwtconf.ini to automate this attack.

