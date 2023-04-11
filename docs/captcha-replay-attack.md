---
title: Captcha Replay attack
author: amandaguglieri
draft: false
TableOfContents: true
tags: 
  - web pentesting
  - attack
---

# Captcha Replay attack

Captcha replay attack is a vulnerability in which the Captcha validation system accepts old Captcha values which have already expired.  This is sometimes considered legitimate behavior (as would be expected if the user refreshed the browser after submitting a successful captcha), however in many cases, such functionality would make the captcha significantly less effective at preventing automation. 

In this case, the attacker resubmitted a request that had already been successfully validated through a captcha, and "replay" was explicitly disabled for the captcha. This is not necessarily a malicious incident on its own, because the user can have accidentally refreshed the browser, however multiple attempts would definitely represent malicious intent.