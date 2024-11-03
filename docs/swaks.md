---
title: swaks
author: amandaguglieri
TableOfContents: true
draft: false
tags:
  - pentesting
  - tools
  - SMTP
  - server
---
# Swaks

Swaks - Swiss Army Knife SMTP, the all-purpose SMTP transaction tester.     Swaks' primary design goal is to be a flexible, scriptable, transaction-oriented SMTP test tool.  It handles SMTP features and extensions such as TLS, authentication, and pipelining; multiple version of the SMTP protocol including SMTP, ESMTP, and LMTP; and multiple transport methods including UNIX-domain sockets, internet-domain sockets, and pipes to spawned processes.  Options can be specified in environment variables, configuration files, and the command line allowing maximum configurability and ease of use for operators and scripters.

## Basic commands

Next, we can use any mail client to connect to the mail server and send our email.

```shell-session
swaks --from notifications@inlanefreight.com --to employees@inlanefreight.com --header 'Subject: Company Notification' --body 'Hi All, we want to hear from you! Please complete the following survey. http://mycustomphishinglink.com/' --server $ipSMTPServerVictim
```

