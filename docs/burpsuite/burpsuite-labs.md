---
title: BurpSuite Labs
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - burpsuite
---
# BurpSuite Labs


## SQL injection

| Solution | SQL injection| level  | link  | Solved |   
| ------------- | ------------- | ---- | ----- | -------- |
| [sqli-1](burpsuite-sqli.md#sql-injection-vulnerability-in-where-clause-allowing-retrieval-of-hidden-data) | SQL injection | Apprentice | [SQL injection vulnerability in WHERE clause allowing retrieval of hidden data](https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data) | Solved | 
| [sqli-2](burpsuite-sqli.md#sql-injection-vulnerability-allowing-login-bypass) | SQL injection | Apprentice | [SQL injection vulnerability allowing login bypass](https://portswigger.net/web-security/sql-injection/lab-login-bypass) | Solved |  
| [sqli-3](burpsuite-sqli.md#sql-injection-union-attack-determining-the-number-of-columns-returned-by-the-query) | SQL injection | Practitioner | [SQL injection UNION attack, determining the number of columns returned by the query](https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns) | Solved |  
| [sqli-4](burpsuite-sqli.md#sql-injection-union-attack-determining-the-number-of-columns-returned-by-the-query) | SQL injection | Practitioner | [SQL injection UNION attack, finding a column containing text](https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text) | Solved |   
| [sqli-5](burpsuite-sqli.md#sql-injection-union-attack-finding-a-column-containing-text) | SQL injection | Practitioner | [SQL injection UNION attack, retrieving data from other tables](https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables) | Solved |  
| [sqli-6](burpsuite-sqli.md#sql-injection-union-attack-retrieving-multiple-values-in-a-single-column)  | SQL injection | Practitioner | [SQL injection UNION attack, retrieving multiple values in a single column](https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-multiple-values-in-single-column) | Solved |   
| | SQL injection | Practitioner | [SQL injection attack, querying the database type and version on Oracle](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle) | Not solved |  
| | SQL injection | Practitioner | [SQL injection attack, querying the database type and version on MySQL and Microsoft](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-mysql-microsoft) | Not solved |
| | SQL injection | Practitioner | [SQL injection attack, listing the database contents on non-Oracle databases](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-non-oracle) | Not solved |  
| | SQL injection | Practitioner | [SQL injection attack, listing the database contents on Oracle](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-oracle) | Not solved |  
| | SQL injection | Practitioner | [Blind SQL injection with conditional responses](https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses) | Not solved |  
| | SQL injection | Practitioner | [Blind SQL injection with conditional errors](https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors) | Not solved |  
| | SQL injection | Practitioner | [Blind SQL injection with time delays](https://portswigger.net/web-security/sql-injection/blind/lab-time-delays) | Not solved |  
| | SQL injection | Practitioner | [Blind SQL injection with time delays and information retrieval](https://portswigger.net/web-security/sql-injection/blind/lab-time-delays-info-retrieval) | Not solved | 
| | SQL injection | Practitioner | [Blind SQL injection with out-of-band interaction](https://portswigger.net/web-security/sql-injection/blind/lab-out-of-band) | Not solved | 
| | SQL injection | Practitioner | [Blind SQL injection with out-of-band data exfiltration](https://portswigger.net/web-security/sql-injection/blind/lab-out-of-band-data-exfiltration) | Not solved |  
| | SQL injection | Practitioner | [SQL injection with filter bypass via XML encoding](https://portswigger.net/web-security/sql-injection/lab-sql-injection-with-filter-bypass-via-xml-encoding) | Not solved  |  


## Cross-site scripting

| Solution                                                                                            | level                | link               | Solved                                                                                                                                                                                                                                                                                          | Solution                                                                                                                                                                                                     |            |     |
| --------------------------------------------------------------------------------------------------- | -------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | --- |
| [xss-1](burpsuite-xss.md#Reflected-XSS-into-HTML-context-with-nothing-encoded)                      | Cross-site scripting | Apprentice         | [Reflected XSS into HTML context with nothing encoded](https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded)                                                                                                                                    | Solved                                                                                                                                                                                                       |            |     |
| [xss-2](burpsuite-xss.md#Stored-XSS-into-HTML-context-with-nothing-encoded)                         | Cross-site scripting | Apprentice         | [Stored XSS into HTML context with nothing encoded](https://portswigger.net/web-security/cross-site-scripting/stored/lab-html-context-nothing-encoded)                                                                                                                                          | Solved                                                                                                                                                                                                       |            |     |
| [xss-3](burpsuite-xss.md#DOM-XSS-in-document.write-sink-using-source)                               | Cross-site scripting | Apprentice         | [DOM XSS in `document.write` sink using source `location.search`](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink)                                                                                                                                  | Solved                                                                                                                                                                                                       |            |     |
| [xss-4](burpsuite-xss.md#DOM-XSS-in-innerHTML-sink-using-source)                                    | Cross-site scripting | Apprentice         | [DOM XSS in `innerHTML` sink using source `location.search`](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-innerhtml-sink)                                                                                                                                            | Solved                                                                                                                                                                                                       |            |     |
| [xss-5](burpsuite-xss.md#DOM-XSS-in-jQuery-anchor-href-attribute-sink-using-location.search-source) | Cross-site scripting | Apprentice         | [DOM XSS in jQuery anchor `href` attribute sink using `location.search` source](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-href-attribute-sink)                                                                                                             | Solved                                                                                                                                                                                                       |            |     |
| [xss-6](burpsuite-xss.md#DOM-XSS-in-jQuery-selector-sink using-a-hashchange-event)                  | Cross-site scripting | Apprentice         | [DOM XSS in jQuery selector sink using a hashchange event](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-selector-hash-change-event)                                                                                                                           | Solved                                                                                                                                                                                                       |            |     |
|                                                                                                     | Cross-site scripting | Apprentice         | [Reflected XSS into attribute with angle brackets HTML-encoded](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-attribute-angle-brackets-html-encoded)                                                                                                                   | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | Apprentice         | [Stored XSS into anchor `href` attribute with double quotes HTML-encoded](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-href-attribute-double-quotes-html-encoded)                                                                                                     | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | Apprentice         | [Reflected XSS into a JavaScript string with angle brackets HTML encoded](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-angle-brackets-html-encoded)                                                                                                 | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | (burpsuite-xss.md) | Practitioner                                                                                                                                                                                                                                                                                    | [DOM XSS in `document.write` sink using source `location.search` inside a select element](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink-inside-select-element) | Not solved |     |
|                                                                                                     | Cross-site scripting | Practitioner       | [DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-angularjs-expression)                                                                                                              | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | Practitioner       | [Reflected DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-dom-xss-reflected)                                                                                                                                                                                  | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | Practitioner       | [Stored DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-dom-xss-stored)                                                                                                                                                                                        | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | Practitioner       | [Exploiting cross-site scripting to steal cookies](https://portswigger.net/web-security/cross-site-scripting/exploiting/lab-stealing-cookies)                                                                                                                                                   | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | Practitioner       | [Exploiting cross-site scripting to capture passwords](https://portswigger.net/web-security/cross-site-scripting/exploiting/lab-capturing-passwords)                                                                                                                                            | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | Practitioner       | [Exploiting XSS to perform CSRF](https://portswigger.net/web-security/cross-site-scripting/exploiting/lab-perform-csrf)                                                                                                                                                                         | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | Practitioner       | [Reflected XSS into HTML context with most tags and attributes blocked](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-html-context-with-most-tags-and-attributes-blocked)                                                                                              | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | Practitioner       | [Reflected XSS into HTML context with all tags blocked except custom ones](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-html-context-with-all-standard-tags-blocked)                                                                                                  | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | Practitioner       | [Reflected XSS with some SVG markup allowed](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-some-svg-markup-allowed)                                                                                                                                                    | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | Practitioner       | [Reflected XSS in canonical link tag](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-canonical-link-tag)                                                                                                                                                                | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | Practitioner       | [Reflected XSS into a JavaScript string with single quote and backslash escaped](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-single-quote-backslash-escaped)                                                                                       | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | Practitioner       | [Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-angle-brackets-double-quotes-encoded-single-quotes-escaped)                      | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | Practitioner       | [Stored XSS into `onclick` event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-onclick-event-angle-brackets-double-quotes-html-encoded-single-quotes-backslash-escaped)    | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | Practitioner       | [Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-template-literal-angle-brackets-single-double-quotes-backslash-backticks-escaped) | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | Expert             | [Reflected XSS with event handlers and `href` attributes blocked](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-event-handlers-and-href-attributes-blocked)                                                                                                            | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | Expert             | [Reflected XSS in a JavaScript URL with some characters blocked](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-url-some-characters-blocked)                                                                                                                 | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | Expert             | [Reflected XSS with AngularJS sandbox escape without strings](https://portswigger.net/web-security/cross-site-scripting/contexts/client-side-template-injection/lab-angular-sandbox-escape-without-strings)                                                                                     | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | Expert             | [Reflected XSS with AngularJS sandbox escape and CSP](https://portswigger.net/web-security/cross-site-scripting/contexts/client-side-template-injection/lab-angular-sandbox-escape-and-csp)                                                                                                     | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | Expert             | [Reflected XSS protected by very strict CSP, with dangling markup attack](https://portswigger.net/web-security/cross-site-scripting/content-security-policy/lab-very-strict-csp-with-dangling-markup-attack)                                                                                    | Not solved                                                                                                                                                                                                   |            |     |
|                                                                                                     | Cross-site scripting | Expert             | [Reflected XSS protected by CSP, with CSP bypass](https://portswigger.net/web-security/cross-site-scripting/content-security-policy/lab-csp-bypass)                                                                                                                                             | Not solved                                                                                                                                                                                                   |            |     |


## Cross-Site Request Forgery

| Cross-site Request Forgery | level        | link                                                                                                                                                                                               | Solved     |     |
| -------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | --- |
| Cross-site Request Forgery | Apprentice   | [CSRF vulnerability with no defenses](https://portswigger.net/web-security/csrf/lab-no-defenses)                                                                                                   | Not solved |     |
| Cross-site Request Forgery | Practitioner | [CSRF where token validation depends on request method](https://portswigger.net/web-security/csrf/bypassing-token-validation/lab-token-validation-depends-on-request-method)                       | Not solved |     |
| Cross-site Request Forgery | Practitioner | [CSRF where token validation depends on token being present](https://portswigger.net/web-security/csrf/bypassing-token-validation/lab-token-validation-depends-on-token-being-present)             | Not solved |     |
| Cross-site Request Forgery | Practitioner | [CSRF where token is not tied to user session](https://portswigger.net/web-security/csrf/bypassing-token-validation/lab-token-not-tied-to-user-session)                                            | Not solved |     |
| Cross-site Request Forgery | Practitioner | [CSRF where token is tied to non-session cookie](https://portswigger.net/web-security/csrf/bypassing-token-validation/lab-token-tied-to-non-session-cookie)                                        | Not solved |     |
| Cross-site Request Forgery | Practitioner | [CSRF where token is duplicated in cookie](https://portswigger.net/web-security/csrf/bypassing-token-validation/lab-token-duplicated-in-cookie)                                                    | Not solved |     |
| Cross-site Request Forgery | Practitioner | [SameSite Lax bypass via method override](https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions/lab-samesite-lax-bypass-via-method-override)                                   | Not solved |     |
| Cross-site Request Forgery | Practitioner | [SameSite Strict bypass via client-side redirect](https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions/lab-samesite-strict-bypass-via-client-side-redirect)                   | Not solved |     |
| Cross-site Request Forgery | Practitioner | [SameSite Strict bypass via sibling domain](https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions/lab-samesite-strict-bypass-via-sibling-domain)                               | Not solved |     |
| Cross-site Request Forgery | Practitioner | [SameSite Lax bypass via cookie refresh](https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions/lab-samesite-strict-bypass-via-cookie-refresh)                                  | Not solved |     |
| Cross-site Request Forgery | Practitioner | [CSRF where Referer validation depends on header being present](https://portswigger.net/web-security/csrf/bypassing-referer-based-defenses/lab-referer-validation-depends-on-header-being-present) | Not solved |     |
| Cross-site Request Forgery | Practitioner | [CSRF with broken Referer validation](https://portswigger.net/web-security/csrf/bypassing-referer-based-defenses/lab-referer-validation-broken)                                                    | Not solved |     |


## Clickjacking

| Clikjacking | level | link | Solved |
| ------------- | ---- | ----- | -------- |
| Clikjacking | Apprentice | [Basic clickjacking with CSRF token protection](https://portswigger.net/web-security/clickjacking/lab-basic-csrf-protected) | Not solved |
| Clikjacking | Apprentice | [Clickjacking with form input data prefilled from a URL parameter](https://portswigger.net/web-security/clickjacking/lab-prefilled-form-input) | Not solved |
| Clikjacking | Apprentice | [Clickjacking with a frame buster script](https://portswigger.net/web-security/clickjacking/lab-frame-buster-script) | Not solved |
| Clikjacking | Practitioner | [Exploiting clickjacking vulnerability to trigger DOM-based XSS](https://portswigger.net/web-security/clickjacking/lab-exploiting-to-trigger-dom-based-xss) | Not solved |
| Clikjacking | Practitioner | [Multistep clickjacking](https://portswigger.net/web-security/clickjacking/lab-multistep) | Not solved | 


## DOM-based vulnerabilities

| DOM-based vulnerabilities | level | link | Solved |
| ------------- | ---- | ----- | -------- |
| DOM-based vulnerabilities | Practitioner | [DOM XSS using web messages](https://portswigger.net/web-security/dom-based/controlling-the-web-message-source/lab-dom-xss-using-web-messages) | Not solved | 
| DOM-based vulnerabilities | Practitioner | [DOM XSS using web messages and a JavaScript URL](https://portswigger.net/web-security/dom-based/controlling-the-web-message-source/lab-dom-xss-using-web-messages-and-a-javascript-url) | Not solved |
| DOM-based vulnerabilities | Practitioner | [DOM XSS using web messages and `JSON.parse`](https://portswigger.net/web-security/dom-based/controlling-the-web-message-source/lab-dom-xss-using-web-messages-and-json-parse) | Not solved |
| DOM-based vulnerabilities | Practitioner | [DOM-based open redirection](https://portswigger.net/web-security/dom-based/open-redirection/lab-dom-open-redirection) | Not solved |
| DOM-based vulnerabilities | Practitioner | [DOM-based cookie manipulation](https://portswigger.net/web-security/dom-based/cookie-manipulation/lab-dom-cookie-manipulation) | Not solved |
| DOM-based vulnerabilities | Expert | [Exploiting DOM clobbering to enable XSS](https://portswigger.net/web-security/dom-based/dom-clobbering/lab-dom-xss-exploiting-dom-clobbering) | Not solved |
| DOM-based vulnerabilities | Expert | [Clobbering DOM attributes to bypass HTML filters](https://portswigger.net/web-security/dom-based/dom-clobbering/lab-dom-clobbering-attributes-to-bypass-html-filters) | Not solved | 


## Cross-origin resource sharing


| Cross-origin resource sharing | level | link | Solved |
| ------------- | ---- | ----- | -------- |
| Cross-origin resource sharing | Apprentice | [CORS vulnerability with basic origin reflection](https://portswigger.net/web-security/cors/lab-basic-origin-reflection-attack) | Not solved |
| Cross-origin resource sharing | Apprentice | [CORS vulnerability with trusted null origin](https://portswigger.net/web-security/cors/lab-null-origin-whitelisted-attack) | Not solved |
| Cross-origin resource sharing | Practitioner | [CORS vulnerability with trusted insecure protocols](https://portswigger.net/web-security/cors/lab-breaking-https-attack) | Not solved |
| Cross-origin resource sharing | Expert | [CORS vulnerability with internal network pivot attack](https://portswigger.net/web-security/cors/lab-internal-network-pivot-attack) | Not solved |


## XML external entity

| XML external entity | level | link | Solved |
| ------------- | ---- | ----- | -------- |
| XML external entity | Apprentice | [Exploiting XXE using external entities to retrieve files](https://portswigger.net/web-security/xxe/lab-exploiting-xxe-to-retrieve-files) | Not solved |
| XML external entity | Apprentice | [Exploiting XXE to perform SSRF attacks](https://portswigger.net/web-security/xxe/lab-exploiting-xxe-to-perform-ssrf) | Not solved |
| XML external entity | Practitioner | [Blind XXE with out-of-band interaction](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-out-of-band-interaction) | Not solved |
| XML external entity | Practitioner | [Blind XXE with out-of-band interaction via XML parameter entities](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-out-of-band-interaction-using-parameter-entities) | Not solved |
| XML external entity | Practitioner | [Exploiting blind XXE to exfiltrate data using a malicious external DTD](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-out-of-band-exfiltration) | Not solved |
| XML external entity | Practitioner | [Exploiting blind XXE to retrieve data via error messages](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-data-retrieval-via-error-messages) | Not solved |
| XML external entity | Practitioner | [Exploiting XInclude to retrieve files](https://portswigger.net/web-security/xxe/lab-xinclude-attack) | Not solved |
| XML external entity | Practitioner | [Exploiting XXE via image file upload](https://portswigger.net/web-security/xxe/lab-xxe-via-file-upload) | Not solved |
| XML external entity | Expert | [Exploiting XXE to retrieve data by repurposing a local DTD](https://portswigger.net/web-security/xxe/blind/lab-xxe-trigger-error-message-by-repurposing-local-dtd) | Not solved | 


## Server-side request forgery

|                                                                        | Server-side request forgery | level        | link                                                                                                                                                | Solved     |
| ---------------------------------------------------------------------- | --------------------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [ssrf-1](burpsuite-ssrf.md#basic-ssrf-against-the-local-server)        | Server-side request forgery | Apprentice   | [Basic SSRF against the local server](https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-localhost)                                   | Solved     |
| [ssrf-2](burpsuite-ssrf.md#basic-ssrf-against-another-back-end-system) | Server-side request forgery | Apprentice   | [Basic SSRF against another back-end system](https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-backend-system)                       | Solved     |
| [ssrf-3](burpsuite-ssrf.md#ssrf-with-blacklist-based-input-filters)    | Server-side request forgery | Practitioner | [SSRF with blacklist-based input filter](https://portswigger.net/web-security/ssrf/lab-ssrf-with-blacklist-filter)                                  | Solved     |
| [ssrf-4](burpsuite-ssrf.md#ssrf-filter-bypass-via-open-redirection)    | Server-side request forgery | Practitioner | [SSRF with filter bypass via open redirection vulnerability](https://portswigger.net/web-security/ssrf/lab-ssrf-filter-bypass-via-open-redirection) | Not solved |
|                                                                        | Server-side request forgery | Practitioner | [Blind SSRF with out-of-band detection](https://portswigger.net/web-security/ssrf/blind/lab-out-of-band-detection)                                  | Not solved |
|                                                                        | Server-side request forgery | Expert       | [SSRF with whitelist-based input filter](https://portswigger.net/web-security/ssrf/lab-ssrf-with-whitelist-filter)                                  | Not solved |
|                                                                        | Server-side request forgery | Expert       | [Blind SSRF with Shellshock exploitation](https://portswigger.net/web-security/ssrf/blind/lab-shellshock-exploitation)                              | Not solved |


## HTTP request smuggling

| HTTP request smuggling | level | link | Solved |
| ------------- | ---- | ----- | -------- |
| HTTP request smuggling | Practitioner | [HTTP request smuggling, basic CL.TE vulnerability](https://portswigger.net/web-security/request-smuggling/lab-basic-cl-te) | Not solved |
| HTTP request smuggling | Practitioner | [HTTP request smuggling, basic TE.CL vulnerability](https://portswigger.net/web-security/request-smuggling/lab-basic-te-cl) | Not solved |
| HTTP request smuggling | Practitioner | [HTTP request smuggling, obfuscating the TE header](https://portswigger.net/web-security/request-smuggling/lab-obfuscating-te-header) | Not solved |
| HTTP request smuggling | Practitioner | [HTTP request smuggling, confirming a CL.TE vulnerability via differential responses](https://portswigger.net/web-security/request-smuggling/finding/lab-confirming-cl-te-via-differential-responses) | Not solved |
| HTTP request smuggling | Practitioner | [HTTP request smuggling, confirming a TE.CL vulnerability via differential responses](https://portswigger.net/web-security/request-smuggling/finding/lab-confirming-te-cl-via-differential-responses) | Not solved |
| HTTP request smuggling | Practitioner | [Exploiting HTTP request smuggling to bypass front-end security controls, CL.TE vulnerability](https://portswigger.net/web-security/request-smuggling/exploiting/lab-bypass-front-end-controls-cl-te) | Not solved |
| HTTP request smuggling | Practitioner | [Exploiting HTTP request smuggling to bypass front-end security controls, TE.CL vulnerability](https://portswigger.net/web-security/request-smuggling/exploiting/lab-bypass-front-end-controls-te-cl) | Not solved |
| HTTP request smuggling | Practitioner | [Exploiting HTTP request smuggling to reveal front-end request rewriting](https://portswigger.net/web-security/request-smuggling/exploiting/lab-reveal-front-end-request-rewriting) | Not solved |
| HTTP request smuggling | Practitioner | [Exploiting HTTP request smuggling to capture other users' requests](https://portswigger.net/web-security/request-smuggling/exploiting/lab-capture-other-users-requests) | Not solved |
| HTTP request smuggling | Practitioner | [Exploiting HTTP request smuggling to deliver reflected XSS](https://portswigger.net/web-security/request-smuggling/exploiting/lab-deliver-reflected-xss) | Not solved |
| HTTP request smuggling | Practitioner | [Response queue poisoning via H2.TE request smuggling](https://portswigger.net/web-security/request-smuggling/advanced/response-queue-poisoning/lab-request-smuggling-h2-response-queue-poisoning-via-te-request-smuggling) | Not solved |
| HTTP request smuggling | Practitioner | [H2.CL request smuggling](https://portswigger.net/web-security/request-smuggling/advanced/lab-request-smuggling-h2-cl-request-smuggling) | Not solved |
| HTTP request smuggling | Practitioner | [HTTP/2 request smuggling via CRLF injection](https://portswigger.net/web-security/request-smuggling/advanced/lab-request-smuggling-h2-request-smuggling-via-crlf-injection) | Not solved |
| HTTP request smuggling | Practitioner | [HTTP/2 request splitting via CRLF injection](https://portswigger.net/web-security/request-smuggling/advanced/lab-request-smuggling-h2-request-splitting-via-crlf-injection) | Not solved |
| HTTP request smuggling | Practitioner | [CL.0 request smuggling](https://portswigger.net/web-security/request-smuggling/browser/cl-0/lab-cl-0-request-smuggling) | Not solved |
| HTTP request smuggling | Expert | [Exploiting HTTP request smuggling to perform web cache poisoning](https://portswigger.net/web-security/request-smuggling/exploiting/lab-perform-web-cache-poisoning) | Not solved |
| HTTP request smuggling | Expert | [Exploiting HTTP request smuggling to perform web cache deception](https://portswigger.net/web-security/request-smuggling/exploiting/lab-perform-web-cache-deception) | Not solved |
| HTTP request smuggling | Expert | [Bypassing access controls via HTTP/2 request tunnelling](https://portswigger.net/web-security/request-smuggling/advanced/request-tunnelling/lab-request-smuggling-h2-bypass-access-controls-via-request-tunnelling) | Not solved |
| HTTP request smuggling | Expert | [Web cache poisoning via HTTP/2 request tunnelling](https://portswigger.net/web-security/request-smuggling/advanced/request-tunnelling/lab-request-smuggling-h2-web-cache-poisoning-via-request-tunnelling) | Not solved |
| HTTP request smuggling | Expert | [Client-side desync](https://portswigger.net/web-security/request-smuggling/browser/client-side-desync/lab-client-side-desync) | Not solved |
| HTTP request smuggling | Expert | [Browser cache poisoning via client-side desync](https://portswigger.net/web-security/request-smuggling/browser/client-side-desync/lab-browser-cache-poisoning-via-client-side-desync) | Not solved |
| HTTP request smuggling | Expert | [Server-side pause-based request smuggling](https://portswigger.net/web-security/request-smuggling/browser/pause-based-desync/lab-server-side-pause-based-request-smuggling) | Not solved |


## OS command injection

| OS command injection | level | link | Solved |
| ------------- | ---- | ----- | -------- |
| OS command injection | Apprentice | [OS command injection, simple case](https://portswigger.net/web-security/os-command-injection/lab-simple) | Not solved |
| OS command injection | Practitioner | [Blind OS command injection with time delays](https://portswigger.net/web-security/os-command-injection/lab-blind-time-delays) | Not solved |
| OS command injection | Practitioner | [Blind OS command injection with output redirection](https://portswigger.net/web-security/os-command-injection/lab-blind-output-redirection) | Not solved |
| OS command injection | Practitioner | [Blind OS command injection with out-of-band interaction](https://portswigger.net/web-security/os-command-injection/lab-blind-out-of-band) | Not solved |
| OS command injection | Practitioner | [Blind OS command injection with out-of-band data exfiltration](https://portswigger.net/web-security/os-command-injection/lab-blind-out-of-band-data-exfiltration) | Not solved | 


## Server-side template injection

| Server-side template injection | level | link | Solved |
| ------------- | ---- | ----- | -------- |
| Server-side template injection | Practitioner | [Basic server-side template injection](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-basic) | Not solved |
| Server-side template injection | Practitioner | [Basic server-side template injection (code context)](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-basic-code-context) | Not solved |
| Server-side template injection | Practitioner | [Server-side template injection using documentation](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-using-documentation) | Not solved |
| Server-side template injection | Practitioner | [Server-side template injection in an unknown language with a documented exploit](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-in-an-unknown-language-with-a-documented-exploit) | Not solved |
| Server-side template injection | Practitioner | [Server-side template injection with information disclosure via user-supplied objects](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-with-information-disclosure-via-user-supplied-objects) | Not solved |
| Server-side template injection | Expert | [Server-side template injection in a sandboxed environment](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-in-a-sandboxed-environment) | Not solved |
| Server-side template injection | Expert | [Server-side template injection with a custom exploit](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-with-a-custom-exploit) | Not solved | 


## Directory traversal

| Directory traversal | level | link | Solved |
| ------------- | ---- | ----- | -------- |
| Directory traversal | Apprentice | [File path traversal, simple case](https://portswigger.net/web-security/file-path-traversal/lab-simple) | Not solved |
| Directory traversal | Practitioner | [File path traversal, traversal sequences blocked with absolute path bypass](https://portswigger.net/web-security/file-path-traversal/lab-absolute-path-bypass) | Not solved |
| Directory traversal  | Practitioner | [File path traversal, traversal sequences stripped non-recursively](https://portswigger.net/web-security/file-path-traversal/lab-sequences-stripped-non-recursively) | Not solved |
| Directory traversal | Practitioner | [File path traversal, traversal sequences stripped with superfluous URL-decode](https://portswigger.net/web-security/file-path-traversal/lab-superfluous-url-decode) | Not solved |
| Directory traversal | Practitioner | [File path traversal, validation of start of path](https://portswigger.net/web-security/file-path-traversal/lab-validate-start-of-path) | Not solved |
| Directory traversal | Practitioner | [File path traversal, validation of file extension with null byte bypass](https://portswigger.net/web-security/file-path-traversal/lab-validate-file-extension-null-byte-bypass) | Not solved | 


## Access control vulnerabilities

| Solution                                                                                                             | Access control vulnerabilities | level        | link                                                                                                                                                                                                   | Solved |
| -------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| [access-1](burpsuite-broken-access-control.md#unprotected-admin-functionality)                                       | Access control vulnerabilities | Apprentice   | [Unprotected admin functionality](https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality)                                                                             | Solved |
| [access-2](burpsuite-broken-access-control.md#unprotected-admin-functionality-with-unpredictable-url)                | Access control vulnerabilities | Apprentice   | [Unprotected admin functionality with unpredictable URL](https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality-with-unpredictable-url)                               | Solved |
| [access-3](burpsuite-broken-access-control.md#user-role-controlled-by-request-parameter)                             | Access control vulnerabilities | Apprentice   | [User role controlled by request parameter](https://portswigger.net/web-security/access-control/lab-user-role-controlled-by-request-parameter)                                                         | Solved |
| [access-4](burpsuite-broken-access-control.md#user-role-can-be-modified-in-user-profile)                             | Access control vulnerabilities | Apprentice   | [User role can be modified in user profile](https://portswigger.net/web-security/access-control/lab-user-role-can-be-modified-in-user-profile)                                                         | Solved |
| [access-5](burpsuite-broken-access-control.md#user-id-controlled-by-request-parameter)                               | Access control vulnerabilities | Apprentice   | [User ID controlled by request parameter](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter)                                                             | Solved |
| [access-6](burpsuite-broken-access-control.md#user-id-controlled-by-request-parameter-with-unpredictable-user-ids)   | Access control vulnerabilities | Apprentice   | [User ID controlled by request parameter, with unpredictable user IDs](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-unpredictable-user-ids)    | Solved |
| [access-7](burpsuite-broken-access-control.md#user-id-controlled-by-request-parameter-with-data-leakage-in-redirect) | Access control vulnerabilities | Apprentice   | [User ID controlled by request parameter with data leakage in redirect](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-data-leakage-in-redirect) | Solved |
| [access-8](burpsuite-broken-access-control.md#user-id-controlled-by-request-parameter-with-password-disclosure)      | Access control vulnerabilities | Apprentice   | [User ID controlled by request parameter with password disclosure](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-password-disclosure)           | Solved |
| [access-9](burpsuite-broken-access-control.md#insecure-direct-object-references)                                     | Access control vulnerabilities | Apprentice   | [Insecure direct object references](https://portswigger.net/web-security/access-control/lab-insecure-direct-object-references)                                                                         | Solved |
| [access-10](burpsuite-broken-access-control.md#url-based-access-control-can-be-circumvented)                         | Access control vulnerabilities | Practitioner | [URL-based access control can be circumvented](https://portswigger.net/web-security/access-control/lab-url-based-access-control-can-be-circumvented)                                                   | Solved |
| [access-11](burpsuite-broken-access-control.md#method-based-access-control-can-be-circumvented)                      | Access control vulnerabilities | Practitioner | [Method-based access control can be circumvented](https://portswigger.net/web-security/access-control/lab-method-based-access-control-can-be-circumvented)                                             | Solved |
| [access-12](burpsuite-broken-access-control.md#multi-step-process-with-no-access-control-on-one-step)                | Access control vulnerabilities | Practitioner | [Multi-step process with no access control on one step](https://portswigger.net/web-security/access-control/lab-multi-step-process-with-no-access-control-on-one-step)                                 | Solved |
| [access-13](burpsuite-broken-access-control.md#referer-based-access-control)                                         | Access control vulnerabilities | Practitioner | [Referer-based access control](https://portswigger.net/web-security/access-control/lab-referer-based-access-control)                                                                                   | Solved |


## Authentication

| Authentication | level | link | Solved |
| ------------- | ---- | ----- | -------- |
| Authentication | Apprentice | [Username enumeration via different responses](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses) | Not solved |
| Authentication | Apprentice | [2FA simple bypass](https://portswigger.net/web-security/authentication/multi-factor/lab-2fa-simple-bypass) | Not solved |
| Authentication | Apprentice | [Password reset broken logic](https://portswigger.net/web-security/authentication/other-mechanisms/lab-password-reset-broken-logic) | Not solved |
| Authentication | Practitioner | [Username enumeration via subtly different responses](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-subtly-different-responses) | Not solved |
| Authentication | Practitioner | [Username enumeration via response timing](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-response-timing) | Not solved |
| Authentication | Practitioner | [Broken brute-force protection, IP block](https://portswigger.net/web-security/authentication/password-based/lab-broken-bruteforce-protection-ip-block) | Not solved |
| Authentication | Practitioner | [Username enumeration via account lock](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-account-lock) | Not solved |
| Authentication | Practitioner | [2FA broken logic](https://portswigger.net/web-security/authentication/multi-factor/lab-2fa-broken-logic) | Not solved |
| Authentication | Practitioner | [Brute-forcing a stay-logged-in cookie](https://portswigger.net/web-security/authentication/other-mechanisms/lab-brute-forcing-a-stay-logged-in-cookie) | Not solved |
| Authentication | Practitioner | [Offline password cracking](https://portswigger.net/web-security/authentication/other-mechanisms/lab-offline-password-cracking) | Not solved |
| Authentication | Practitioner | [Password reset poisoning via middleware](https://portswigger.net/web-security/authentication/other-mechanisms/lab-password-reset-poisoning-via-middleware) | Not solved |
| Authentication | Practitioner | [Password brute-force via password change](https://portswigger.net/web-security/authentication/other-mechanisms/lab-password-brute-force-via-password-change) | Not solved |
| Authentication | Expert | [Broken brute-force protection, multiple credentials per request](https://portswigger.net/web-security/authentication/password-based/lab-broken-brute-force-protection-multiple-credentials-per-request) | Not solved |
| Authentication | Expert | [2FA bypass using a brute-force attack](https://portswigger.net/web-security/authentication/multi-factor/lab-2fa-bypass-using-a-brute-force-attack) | Not solved | 


## WebSockets
 
| WebSockets | level | link | Solved |
| ------------- | ---- | ----- | -------- |
| WebSockets | Apprentice | [Manipulating WebSocket messages to exploit vulnerabilities](https://portswigger.net/web-security/websockets/lab-manipulating-messages-to-exploit-vulnerabilities) | Not solved |
| WebSockets | Practitioner | [Manipulating the WebSocket handshake to exploit vulnerabilities](https://portswigger.net/web-security/websockets/lab-manipulating-handshake-to-exploit-vulnerabilities) | Not solved |
| WebSockets | Practitioner | [Cross-site WebSocket hijacking](https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking/lab) | Not solved | 


## Web cache poisoning

| Web cache poisoning | level | link | Solved |
| ------------- | ---- | ----- | -------- |
|  Web cache poisoning | Practitioner | [Web cache poisoning with an unkeyed header](https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-with-an-unkeyed-header) | Not solved |
| Web cache poisoning | Practitioner | [Web cache poisoning with an unkeyed cookie](https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-with-an-unkeyed-cookie) | Not solved |
| Web cache poisoning | Practitioner | [Web cache poisoning with multiple headers](https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-with-multiple-headers) | Not solved |
| Web cache poisoning | Practitioner | [Targeted web cache poisoning using an unknown header](https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-targeted-using-an-unknown-header) | Not solved |
| Web cache poisoning | Practitioner | [Web cache poisoning via an unkeyed query string](https://portswigger.net/web-security/web-cache-poisoning/exploiting-implementation-flaws/lab-web-cache-poisoning-unkeyed-query) | Not solved |
| Web cache poisoning | Practitioner | [Web cache poisoning via an unkeyed query parameter](https://portswigger.net/web-security/web-cache-poisoning/exploiting-implementation-flaws/lab-web-cache-poisoning-unkeyed-param) | Not solved |
| Web cache poisoning | Practitioner | [Parameter cloaking](https://portswigger.net/web-security/web-cache-poisoning/exploiting-implementation-flaws/lab-web-cache-poisoning-param-cloaking) | Not solved |
| Web cache poisoning | Practitioner | [Web cache poisoning via a fat GET request](https://portswigger.net/web-security/web-cache-poisoning/exploiting-implementation-flaws/lab-web-cache-poisoning-fat-get) | Not solved |
| Web cache poisoning | Practitioner | [URL normalization](https://portswigger.net/web-security/web-cache-poisoning/exploiting-implementation-flaws/lab-web-cache-poisoning-normalization) | Not solved |
| Web cache poisoning | Expert | [Web cache poisoning to exploit a DOM vulnerability via a cache with strict cacheability criteria](https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-to-exploit-a-dom-vulnerability-via-a-cache-with-strict-cacheability-criteria) | Not solved |
| Web cache poisoning | Expert | [Combining web cache poisoning vulnerabilities](https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-combining-vulnerabilities) | Not solved |
| Web cache poisoning | Expert | [Cache key injection](https://portswigger.net/web-security/web-cache-poisoning/exploiting-implementation-flaws/lab-web-cache-poisoning-cache-key-injection) | Not solved |
| Web cache poisoning | Expert | [Internal cache poisoning](https://portswigger.net/web-security/web-cache-poisoning/exploiting-implementation-flaws/lab-web-cache-poisoning-internal) | Not solved | 


## Insecure deserialization
 
| Insecure deserialization | level | link | Solved |
| ------------- | ---- | ----- | -------- |
| Insecure deserialization | Apprentice | [Modifying serialized objects](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-modifying-serialized-objects) | Not solved |
| Insecure deserialization | Practitioner | [Modifying serialized data types](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-modifying-serialized-data-types) | Not solved |
| Insecure deserialization  | Practitioner | [Using application functionality to exploit insecure deserialization](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-using-application-functionality-to-exploit-insecure-deserialization) | Not solved |
| Insecure deserialization | Practitioner | [Arbitrary object injection in PHP](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-arbitrary-object-injection-in-php) | Not solved |
| Insecure deserialization | Practitioner | [Exploiting Java deserialization with Apache Commons](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-exploiting-java-deserialization-with-apache-commons) | Not solved |
| Insecure deserialization | Practitioner | [Exploiting PHP deserialization with a pre-built gadget chain](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-exploiting-php-deserialization-with-a-pre-built-gadget-chain) | Not solved |
| Insecure deserialization | Practitioner | [Exploiting Ruby deserialization using a documented gadget chain](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-exploiting-ruby-deserialization-using-a-documented-gadget-chain) | Not solved |
| Insecure deserialization | Expert | [Developing a custom gadget chain for Java deserialization](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-developing-a-custom-gadget-chain-for-java-deserialization) | Not solved |
| Insecure deserialization | Expert | [Developing a custom gadget chain for PHP deserialization](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-developing-a-custom-gadget-chain-for-php-deserialization) | Not solved |
| Insecure deserialization | Expert | [Using PHAR deserialization to deploy a custom gadget chain](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-using-phar-deserialization-to-deploy-a-custom-gadget-chain) | Not solved | 


## Information disclosure

| Information disclosure| level | link | Solved |
| ------------- | ---- | ----- | -------- |
| Information disclosure | Apprentice | [Information disclosure in error messages](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-in-error-messages) | Not solved |
| Information disclosure | Apprentice | [Information disclosure on debug page](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-on-debug-page) | Not solved |
| Information disclosure | Apprentice | [Source code disclosure via backup files](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-via-backup-files) | Not solved |
| Information disclosure | Apprentice | [Authentication bypass via information disclosure](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-authentication-bypass) | Not solved |
| Information disclosure | Practitioner | [Information disclosure in version control history](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-in-version-control-history) | Not solved | 

## Business logic vulnerabilities

| Business logic vulnerabilities | level | link | Solved |
| ------------- | ---- | ----- | -------- |
| Business logic vulnerabilities | Apprentice | [Excessive trust in client-side controls](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-excessive-trust-in-client-side-controls) | Not solved |
| Business logic vulnerabilities | Apprentice | [High-level logic vulnerability](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-high-level) | Not solved |
| Business logic vulnerabilities | Apprentice | [Inconsistent security controls](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-inconsistent-security-controls) | Not solved |
| Business logic vulnerabilities | Apprentice | [Flawed enforcement of business rules](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-flawed-enforcement-of-business-rules) | Not solved |
| Business logic vulnerabilities | Practitioner | [Low-level logic flaw](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-low-level) | Not solved |
| Business logic vulnerabilities | Practitioner | [Inconsistent handling of exceptional input](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-inconsistent-handling-of-exceptional-input) | Not solved |
| Business logic vulnerabilities | Practitioner | [Weak isolation on dual-use endpoint](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-weak-isolation-on-dual-use-endpoint) | Not solved |
| Business logic vulnerabilities | Practitioner | [Insufficient workflow validation](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-insufficient-workflow-validation) | Not solved |
| Business logic vulnerabilities | Practitioner | [Authentication bypass via flawed state machine](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-authentication-bypass-via-flawed-state-machine) | Not solved |
| Business logic vulnerabilities | Practitioner | [Infinite money logic flaw](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-infinite-money) | Not solved |
| Business logic vulnerabilities | Practitioner | [Authentication bypass via encryption oracle](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-authentication-bypass-via-encryption-oracle) | Not solved | 


## HTTP Host header attacks

| HTTP Host header attacks | level | link | Solved |
| ------------- | ---- | ----- | -------- |
| HTTP Host header attacks | Apprentice | [Basic password reset poisoning](https://portswigger.net/web-security/host-header/exploiting/password-reset-poisoning/lab-host-header-basic-password-reset-poisoning) | Not solved |
| HTTP Host header attacks | Apprentice | [Host header authentication bypass](https://portswigger.net/web-security/host-header/exploiting/lab-host-header-authentication-bypass) | Not solved |
| HTTP Host header attacks | Practitioner | [Web cache poisoning via ambiguous requests](https://portswigger.net/web-security/host-header/exploiting/lab-host-header-web-cache-poisoning-via-ambiguous-requests) | Not solved |
| HTTP Host header attacks | Practitioner | [Routing-based SSRF](https://portswigger.net/web-security/host-header/exploiting/lab-host-header-routing-based-ssrf) | Not solved |
| HTTP Host header attacks | Practitioner | [SSRF via flawed request parsing](https://portswigger.net/web-security/host-header/exploiting/lab-host-header-ssrf-via-flawed-request-parsing) | Not solved |
| HTTP Host header attacks | Practitioner | [Host validation bypass via connection state attack](https://portswigger.net/web-security/host-header/exploiting/lab-host-header-host-validation-bypass-via-connection-state-attack) | Not solved |
| HTTP Host header attacks | Expert | [Password reset poisoning via dangling markup](https://portswigger.net/web-security/host-header/exploiting/password-reset-poisoning/lab-host-header-password-reset-poisoning-via-dangling-markup) | Not solved | 

## OAuth authentication

| OAuth authentication | level | link | Solved |
| ------------- | ---- | ----- | -------- |
| OAuth authentication | Apprentice | [Authentication bypass via OAuth implicit flow](https://portswigger.net/web-security/oauth/lab-oauth-authentication-bypass-via-oauth-implicit-flow) | Not solved |
| OAuth authentication | Practitioner | [Forced OAuth profile linking](https://portswigger.net/web-security/oauth/lab-oauth-forced-oauth-profile-linking) | Not solved |
| OAuth authentication | Practitioner | [OAuth account hijacking via redirect_uri](https://portswigger.net/web-security/oauth/lab-oauth-account-hijacking-via-redirect-uri) | Not solved |
| OAuth authentication | Practitioner | [Stealing OAuth access tokens via an open redirect](https://portswigger.net/web-security/oauth/lab-oauth-stealing-oauth-access-tokens-via-an-open-redirect) | Not solved |
| OAuth authentication | Practitioner | [SSRF via OpenID dynamic client registration](https://portswigger.net/web-security/oauth/openid/lab-oauth-ssrf-via-openid-dynamic-client-registration) | Not solved |
| OAuth authentication | Expert | [Stealing OAuth access tokens via a proxy page](https://portswigger.net/web-security/oauth/lab-oauth-stealing-oauth-access-tokens-via-a-proxy-page) | Not solved | 

## File upload vulnerabilities

| File upload vulnerabilities | level | link | Solved |
| ------------- | ---- | ----- | -------- |
| File upload vulnerabilities | Apprentice | [Remote code execution via web shell upload](https://portswigger.net/web-security/file-upload/lab-file-upload-remote-code-execution-via-web-shell-upload) | Not solved |
| File upload vulnerabilities | Apprentice | [Web shell upload via Content-Type restriction bypass](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-content-type-restriction-bypass) | Not solved |
| File upload vulnerabilities | Practitioner | [Web shell upload via path traversal](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-path-traversal) | Not solved |
| File upload vulnerabilities | Practitioner | [Web shell upload via extension blacklist bypass](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-extension-blacklist-bypass) | Not solved |
| File upload vulnerabilities | Practitioner | [Web shell upload via obfuscated file extension](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-obfuscated-file-extension) | Not solved |
| File upload vulnerabilities | Practitioner | [Remote code execution via polyglot web shell upload](https://portswigger.net/web-security/file-upload/lab-file-upload-remote-code-execution-via-polyglot-web-shell-upload) | Not solved |
| File upload vulnerabilities | Expert | [Web shell upload via race condition](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-race-condition) | Not solved | 

## JWT

| JWT | level | link | Solved |
| ------------- | ---- | ----- | -------- |
| JWT | Apprentice | [JWT authentication bypass via unverified signature](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-unverified-signature) | Not solved |
| JWT | Apprentice | [JWT authentication bypass via flawed signature verification](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-flawed-signature-verification) | Not solved |
| JWT | Practitioner | [JWT authentication bypass via weak signing key](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-weak-signing-key) | Not solved |
| JWT | Practitioner | [JWT authentication bypass via jwk header injection](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-jwk-header-injection) | Not solved |
| JWT | Practitioner | [JWT authentication bypass via jku header injection](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-jku-header-injection) | Not solved |
| JWT | Practitioner | [JWT authentication bypass via kid header path traversal](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-kid-header-path-traversal) | Not solved |
| JWT | Expert | [JWT authentication bypass via algorithm confusion](https://portswigger.net/web-security/jwt/algorithm-confusion/lab-jwt-authentication-bypass-via-algorithm-confusion) | Not solved |
| JWT | Expert | [JWT authentication bypass via algorithm confusion with no exposed key](https://portswigger.net/web-security/jwt/algorithm-confusion/lab-jwt-authentication-bypass-via-algorithm-confusion-with-no-exposed-key) | Not solved | 


## Essential skills

| Essential skills | level | link | Solved |
| ------------- | ---- | ----- | -------- |
| Essential skills | Practitioner | [Discovering vulnerabilities quickly with targeted scanning](https://portswigger.net/web-security/essential-skills/using-burp-scanner-during-manual-testing/lab-discovering-vulnerabilities-quickly-with-targeted-scanning) | Not solved | 


## Prototype pollution

| Prototype pollution | level | link | Solved |
| ------------- | ---- | ----- | -------- |
| Prototype pollution | Practitioner | [DOM XSS via client-side prototype pollution](https://portswigger.net/web-security/prototype-pollution/finding/lab-prototype-pollution-dom-xss-via-client-side-prototype-pollution) | Not solved |
| Prototype pollution | Practitioner | [DOM XSS via an alternative prototype pollution vector](https://portswigger.net/web-security/prototype-pollution/finding/lab-prototype-pollution-dom-xss-via-an-alternative-prototype-pollution-vector) | Not solved |
| Prototype pollution | Practitioner | [Client-side prototype pollution in third-party libraries](https://portswigger.net/web-security/prototype-pollution/finding/lab-prototype-pollution-client-side-prototype-pollution-in-third-party-libraries) | Not solved |
| Prototype pollution | Practitioner | [Client-side prototype pollution via browser APIs](https://portswigger.net/web-security/prototype-pollution/browser-apis/lab-prototype-pollution-client-side-prototype-pollution-via-browser-apis) | Not solved |
| Prototype pollution | Practitioner | [Client-side prototype pollution via flawed sanitization](https://portswigger.net/web-security/prototype-pollution/preventing/lab-prototype-pollution-client-side-prototype-pollution-via-flawed-sanitization) | Not solved | 

