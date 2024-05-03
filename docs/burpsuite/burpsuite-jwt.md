---
title: BurpSuite Labs - Json Web Token jwt
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - burpsuite
  - jwt
---

# BurpSuite Labs - Json Web Token jwt


## JWT authentication bypass via unverified signature

### Enunciation

This lab uses a JWT-based mechanism for handling sessions. Due to implementation flaws, the server doesn't verify the signature of any JWTs that it receives.

To solve the lab, modify your session token to gain access to the admin panel at `/admin`, then delete the user `carlos`.

You can log in to your own account using the following credentials: `wiener:peter`

### Solution

![JWT](../img/jwt_01.png)

![JWT](../img/jwt_02.png)

![JWT](../img/jwt_03.png)


## JWT authentication bypass via flawed signature verification

### Enunciation

This lab uses a JWT-based mechanism for handling sessions. The server is insecurely configured to accept unsigned JWTs.

To solve the lab, modify your session token to gain access to the admin panel at `/admin`, then delete the user `carlos`.

You can log in to your own account using the following credentials: `wiener:peter`

### Solution

![JWT](../img/jwt_04.png)

![JWT](../img/jwt_05.png)

![JWT](../img/jwt_06.png)

![JWT](../img/jwt_07.png)


## JWT authentication bypass via weak signing key

### Enunciation

This lab uses a JWT-based mechanism for handling sessions. It uses an extremely weak secret key to both sign and verify tokens. This can be easily brute-forced using a [wordlist of common secrets](https://github.com/wallarm/jwt-secrets/blob/master/jwt.secrets.list).

To solve the lab, first brute-force the website's secret key. Once you've obtained this, use it to sign a modified session token that gives you access to the admin panel at `/admin`, then delete the user `carlos`.

You can log in to your own account using the following credentials: `wiener:peter`

### Solution

Capture the JWT of wiener user and run hashcat with a well-known dictionary of jwt secrets such as    [https://github.com/wallarm/jwt-secrets/blob/master/jwt.secrets.list](https://github.com/wallarm/jwt-secrets/blob/master/jwt.secrets.list)


```
hashcat -a 0 -m 16500 capturedJWT <wordlist>
```

Results:

```
eyJraWQiOiI2YTNmZjdmMi0xMDNmLTQyZGEtYmNkZC0yN2JiZmM4ZTU3OTQiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTcxNDYwMTIyNSwic3ViIjoid2llbmVyIn0.AeWLmJpWTsA-c-dA5j6UHIQ-f9Mo6F9Y-OrXBsGu6Gw:secret1
```

Open JWT Editor, go to Keys tab and generate a new signature.

![JWT](../img/jwt_08.png)

Send your request to repeater, go to JSON Web Token tab, modify username to administrator, click on Sign and select your signature. Modify endpoint to /admin and send request.

![JWT](../img/jwt_09.png)

Trigger the delete user carlos endpoint:

![JWT](../img/jwt_10.png)


## JWT authentication bypass via jwk header injection

### Enunciation

This lab uses a JWT-based mechanism for handling sessions. The server supports the `jwk` parameter in the JWT header. This is sometimes used to embed the correct verification key directly in the token. However, it fails to check whether the provided key came from a trusted source.

To solve the lab, modify and sign a JWT that gives you access to the admin panel at `/admin`, then delete the user `carlos`.

You can log in to your own account using the following credentials: `wiener:peter`

### Solution

Capture wiener JWT and send the request GET /admin to the Repeater module. Once there, go to JSON Web Token tab and:

![JWT](../img/jwt_11.png)

![JWT](../img/jwt_12.png)


![JWT](../img/jwt_13.png)


## JWT authentication bypass via jku header injection

### Enunciation

This lab uses a JWT-based mechanism for handling sessions. The server supports the `jku` parameter in the JWT header. However, it fails to check whether the provided URL belongs to a trusted domain before fetching the key.

To solve the lab, forge a JWT that gives you access to the admin panel at `/admin`, then delete the user `carlos`.

You can log in to your own account using the following credentials: `wiener:peter`

### Solution

```
##### Part 1 - Upload a malicious JWK Set

1. In Burp, load the JWT Editor extension from the BApp store.
    
2. In the lab, log in to your own account and send the post-login `GET /my-account` request to Burp Repeater.
    
3. In Burp Repeater, change the path to `/admin` and send the request. Observe that the admin panel is only accessible when logged in as the `administrator` user.
    
4. Go to the **JWT Editor Keys** tab in Burp's main tab bar.
    
5. Click **New RSA Key**.
    
6. In the dialog, click **Generate** to automatically generate a new key pair, then click **OK** to save the key. Note that you don't need to select a key size as this will automatically be updated later.
    
7. In the browser, go to the exploit server.
    
8. Replace the contents of the **Body** section with an empty JWK Set as follows:
    
    `{ "keys": [ ] }`
9. Back on the **JWT Editor Keys** tab, right-click on the entry for the key that you just generated, then select **Copy Public Key as JWK**.
    
10. Paste the JWK into the `keys` array on the exploit server, then store the exploit. The result should look something like this:
    
    `{ "keys": [ { "kty": "RSA", "e": "AQAB", "kid": "893d8f0b-061f-42c2-a4aa-5056e12b8ae7", "n": "yy1wpYmffgXBxhAUJzHHocCuJolwDqql75ZWuCQ_cb33K2vh9mk6GPM9gNN4Y_qTVX67WhsN3JvaFYw" } ] }`

##### Part 2 - Modify and sign the JWT

1. Go back to the `GET /admin` request in Burp Repeater and switch to the extension-generated **JSON Web Token** message editor tab.
    
2. In the header of the JWT, replace the current value of the `kid` parameter with the `kid` of the JWK that you uploaded to the exploit server.
    
3. Add a new `jku` parameter to the header of the JWT. Set its value to the URL of your JWK Set on the exploit server.
    
4. In the payload, change the value of the `sub` claim to `administrator`.
    
5. At the bottom of the tab, click **Sign**, then select the RSA key that you generated in the previous section.
    
6. Make sure that the **Don't modify header** option is selected, then click **OK**. The modified token is now signed with the correct signature.
    
7. Send the request. Observe that you have successfully accessed the admin panel.
    
8. In the response, find the URL for deleting `carlos` (`/admin/delete?username=carlos`). Send the request to this endpoint to solve the lab.

```

## B

### Enunciation

T

### Solution

I


## B

### Enunciation

T

### Solution

I


## B

### Enunciation

T

### Solution

I

