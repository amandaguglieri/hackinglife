
# Identify Application Entry Points


|ID|Link to Hackinglife|Link to OWASP|Objectives|Tools|
|:---|:---|:---|:---|:---|
|1.6|WSTG-INFO-06|[Identify Application Entry Points](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/06-Identify_Application_Entry_Points)|- Identify possible entry and injection points through request and response analysis which covers hidden fields, parameters, methods HTTP header analysis|OWASP ASD, Burpsuite/ZAP|



### Some enumeration techniques for HTTP verbs

With [netcat](netcat.md)
```bash
# Send a OPTIONS message with netcat
nc victim.target 80
OPTIONS / HTTP/1.0

```
