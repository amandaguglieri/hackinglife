---
title: Testing for Command Injection - OWASP Web Security Testing Guide 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - WSTG-INPV-12
---
# Testing for Command Injection

??? quote "OWASP"
	[OWASP Web Security Testing Guide 4.2](index.md) > 7. Data Validation Testing > 7.12. Testing for Command Injection

	| ID   | Link to Hackinglife             | Link to OWASP                                                                                                                                                                                    | Description                                                                                                                                 |
	| :--- | :------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
	| 7.12 | [WSTG-INPV-12](WSTG-INPV-12.md) | [Testing for Command Injection](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/12-Testing_for_Command_Injection) | - Identify and assess the command injection points with special characters (i.e.: \| ; & $ > < ' !)  For example: ?doc=Doc1.pdf+\|+Dir c:\| |


Command injection vulnerabilities in the context of web application penetration testing occur when an attacker can manipulate the input fields of a web application in a way that allows them to execute arbitrary operating system commands on the underlying server. This type of vulnerability is a serious security risk because it can lead to unauthorized access, data theft, and full compromise of the web server.

Causes:

- User Input Handling: Web applications often take user input through forms, query parameters, or other means. 
- Lack of Input Sanitization: Insecurely coded applications may fail to properly validate, sanitize, or escape user inputs before using them in system commands.
- Injection Points: Attackers identify injection points, such as input fields or URL query parameters, where they can insert malicious commands.

Impact:

- Unauthorized Execution: Attackers can execute arbitrary commands with the privileges of the web server process. This can lead to unauthorized data access, code execution, or system compromise.
- Data Exfiltration: Attackers can exfiltrate sensitive data, such as database content, files, or system configurations.
- System Manipulation: Attackers may manipulate the server, installmalware, or create backdoors for future access.

## How to Test 

Malicious Input: Attackers craft input that includes special characters, like semicolons, pipes, backticks, and other shell metacharacters, to break out of the intended input context and inject their commands. Command Execution: When the application processes the attacker's input, it constructs a shell command using the malicious input.  The server, believing the command to be legitimate, executes it in the underlying operating system


### Case Study: Perl

When viewing a file in a web application, the filename is often shown in the URL. Perl allows piping data from a process into an open statement. The user can simply append the Pipe symbol | onto the end of the filename.

```
# Example URL before alteration
http://sensitive/cgi-bin/userData.pl?doc=user1.txt 

# Example URL modified
http://sensitive/cgi-bin/userData.pl?doc=/bin/ls|
```

### Case Study: PHP

Appending a semicolon to the end of a URL for a .PHP page followed by an operating system command, will execute the command. %3B is URL encoded and decodes to semicolon 

```
http://sensitive/something.php?dir=%3Bcat%20/etc/passwd
```


## Special characters for command injection

The following special character can be used for command injection such as:

```
| ; & $ > < ' ! 
```

```
# Uses of | will make command 2 to be executed weather command 1 execution is successful or not.
cmd1|cmd2

# Uses of ; will make command 2 to be executed weather command 1 execution is successful or not.
cmd1;cmd2

# Command 2 will only be executed if command 1 execution fails. 
cmd1||cmd2


# Command 2 will only be executed if command 1 execution succeeds. 
cmd1&&cmd2

# For example, echo $(whoami) or $(touch test.sh; echo 'ls' > test.sh)
$(cmd)

# It’s used to execute specific command. For example, whoami 
cmd

>(cmd) : >(ls) 
<(cmd) : <(ls)
```

## Code Review Dangerous API 

Be aware of the uses of following API as it may introduce the command injection risks. 

### Java

```
Runtime.exec()
```

### C/C++ 

```
system 
exec 
ShellExecute
```

### Python 

```
exec
eval
os.system
os.popen
subprocess.popen
subprocess.call
```

### PHP

```
system
shell_exec 
exec
proc_open 
eval
```

