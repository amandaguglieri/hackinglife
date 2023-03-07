---
title: HTTP headers
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting HTTP headers
---

# HTTP headers

## Cache-control

Cache-control is a header used to specify caching policies for browsers and other caching services. 

## Set-Cookie

From [geeksforgeeks](https://www.geeksforgeeks.org/http-headers-set-cookie/): "The **HTTP header Set-Cookie** is a response header and used to send cookies from the server to the user agent. So the user agent can send them back to the server later so the server can detect the user."

### Directives

```
# The cookie name have to avoid this character ( ) @, ; : \ ” / [ ] ? = { } plus control characters, spaces, and tabs. It can be any US-ASCII characters.
Set-Cookie: <cookie-name>=<cookie-value>

# This directive defines the host where the cookie will be sent. It is an optional directive.
Set-Cookie: <cookie-name>=<cookie-value>; Domain=<domain-value>

# It is an optional directive that contains the expiry date of the cookie.
Set-Cookie: <cookie-name>=<cookie-value>; Expires=<date>

# Forbids JavaScript from accessing the cookie, for example, through the `Document.cookie` property. Note that a cookie that has been created with `HttpOnly` will still be sent with JavaScript-initiated requests, for example, when calling `XMLHttpRequest.send()` or `fetch()`. This mitigates attacks against cross-site scripting XSS.
Set-Cookie: <cookie-name>=<cookie-value>; HttpOnly

# It contains the life span in a digit of seconds format, zero or negative value will make the cookie expired immediately.
Set-Cookie: <cookie-name>=<cookie-value>; Max-Age=<number>

Set-Cookie: <cookie-name>=<cookie-value>; Partitioned

# This directive define a path that must exist in the requested URL, else the browser can’t send the cookie header.
Set-Cookie: <cookie-name>=<cookie-value>; Path=<path-value>

Set-Cookie: <cookie-name>=<cookie-value>; Secure

# This directives providing some protection against cross-site request forgery attacks.
# Strict means that the browser sends the cookie only for same-site requests, that is, requests originating from the same site that set the cookie. If a request originates from a different domain or scheme (even with the same domain), no cookies with the `SameSite=Strict` attribute are sent.

Set-Cookie: <cookie-name>=<cookie-value>; SameSite=Strict

# Lax means that the cookie is not sent on cross-site requests, such as on requests to load images or frames, but is sent when a user is navigating to the origin site from an external site (for example, when following a link). This is the default behavior if the `SameSite` attribute is not specified.

Set-Cookie: <cookie-name>=<cookie-value>; SameSite=Lax

# means that the browser sends the cookie with both cross-site and same-site requests. The `Secure` attribute must also be set when setting this value, like so `SameSite=None; Secure`

Set-Cookie: <cookie-name>=<cookie-value>; SameSite=None; Secure

// Multiple attributes are also possible, for example:
Set-Cookie: <cookie-name>=<cookie-value>; Domain=<domain-value>; Secure; HttpOnly

```


## CORS - Cross-Origin Resource Sharing 

Cross-Origin Resource Sharing (CORS) is an HTTP-header based mechanism that allows a server to indicate any origins (domain, scheme, or port) other than its own from which a browser should permit loading resources.

For security reasons, browsers restrict cross-origin HTTP requests initiated from scripts.

![cors_principle.png](img/cors_principle.png)


## X-XSS-Protection

The HTTP **`X-XSS-Protection`** response header is a feature of Internet Explorer, Chrome and Safari that stops pages from loading when they detect reflected cross-site scripting XSS  attacks.

### Syntax

```
# Disables XSS filtering.
X-XSS-Protection: 0

# Enables XSS filtering (usually default in browsers). If a cross-site scripting attack is detected, the browser will sanitize the page (remove the unsafe parts).
X-XSS-Protection: 1

# Enables XSS filtering. Rather than sanitizing the page, the browser will prevent rendering of the page if an attack is detected.
X-XSS-Protection: 1; mode=block

# Enables XSS filtering. If a cross-site scripting attack is detected, the browser will sanitize the page and report the violation. This uses the functionality of the CSP report-uri directive to send a report.
X-XSS-Protection: 1; report=<reporting-uri>
```
