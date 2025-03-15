---
title: CPTS labs - 26 Documentation and Reporting
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - certification
  - CPTS
  - labs
---

# CPTS labs - 26 Documentation and Reporting

## Preparation

**RDP to  with user "htb-student" and password "HTB_@cademy_stdnt!". What tool mentioned in this section can make logging a session easier?**

Results: tmux


Steve is learning about the tool that can make logging a session easier. He messages you for help mentioning that he would like to try to split the panes vertically. What do you tell him? (Answer format: [key] + [key] + [key], i.e., fill in the values for "key" and leave the brackets and + signs.)

Results: [Ctrl] + [b] + [Shift] + [%]

#### Optional Exercises

Challenge your understanding of the Module content and answer the optional question(s) below. These are considered supplementary content and are not required to complete the Module. You can reveal the answer at any time to check your work.   
Connect to the testing VM using Xfreerdp, play around with the assessment directory structure and Obsidian notebook, and experiment with Tmux logging. Type DONE as your answer when you have finished.

Results: DONE


**Inlanefreight has contracted Elizabeth's firm to complete a type of assessment that is mostly automated where no exploitation is attempted. What kind of assessment is she going to be contracted for?**

Result: vulnerability assessment

**Nicolas is performing an external & internal penetration test for Inlanefreight. The client has only provided the company's name and a network connection onsite at their office and no additional detail. From what perspective is he performing the penetration test?**

Results: Black box


**What component of a report should be written in a simple to understand and non-technical manner?**

Results: Executive summary

 **It is a good practice to name and recommend specific vendors in the component of the report mentioned in the last question. True or False?**

Results: False


## Reporting

**RDP to ACADEMY-DOCRPT-PAR01) with user "htb-student" and password "HTB_@cademy_stdnt!".  "An attacker can own your whole entire network cause your DC is way out of date. You should really fix that!". Is this a Good or Bad remediation recommendation? (Answer Format: Good or Bad)**

Results: Bad

**Connect to the testing VM using Xfreerdp and practice writing findings based on the evidence in the Obsidian notebook. Use your penetration testing skills to gather additional evidence for the findings where evidence is not provided. Type DONE as your answer when you have finished.**

Results: DONE


## Next Steps: Documentation & Reporting Practice Lab


RDP to with user "htb-student" and password " HTB_@cademy_stdnt!"

**Connect to the testing VM using Xfreerdp and practice testing, documentation, and reporting against the target lab. Once the target spawns, browse to the WriteHat instance on port 443 and authenticate with the provided admin credentials. Play around with the tool and practice adding findings to the database to get a feel for the reporting tools available to us. Remember that all data will be lost once the target resets, so save any practice findings locally! Next, complete the in-progress penetration test. Once you achieve Domain Admin level access, submit the contents of the flag.txt file on the Administrator Desktop on the DC01 host.**


```

```





**After achieving Domain Admin, submit the NTLM hash of the KRBTGT account.**


```

```




**Dump the NTDS file and perform offline password cracking. Submit the password of the svc_reporting user as your answer.**

```

```



**What powerful local group does this user belong to?**

```

```



**Complete the internal penetration test against the INLANEFREIGHT.LOCAL domain, write up your attack chain and findings, and draft a professional report using the provided report template. Once done, perform self-QA. Though optional, this exercise is excellent practice, and we highly encourage you to work through it. Type REPORT as your answer once you are done.**

Results: DONE