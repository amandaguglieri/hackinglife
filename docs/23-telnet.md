---
title: "23 telnet"
author: amandaguglieri
draft: false
TableOfContents: true
---

Sometimes, due to configuration mistakes, some important accounts can be left with blank passwords for the sake of accessibility. This is a significant issue with some network devices or hosts, leaving them open to simple brute-forcing attacks, where the attacker can try logging in sequentially, using a list of usernames with no password input. Some typical important accounts have self-explanatory names, such as:
+ admin
+ administrator
+ root
A direct way to attempt logging in with these credentials in hopes that one of them exists and has a blank password is to input them manually in the terminal when the hosts request them. If the list were longer, we could use a script to automate this process, feeding it a wordlist for usernames and one for passwords.
Typically, the wordlists used for this task consist of typical people names, abbreviations, or data from previous database leaks. For now, we can resort to manually trying these three main usernames above.
