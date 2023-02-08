---
title: "To-do list"
author: amandaguglieri
draft: false
TableOfContents: true
---

!!! note "Sources"
    -  https://johnjhacking.com/blog/oscp-reborn-2023/
    - https://help.offensive-security.com/hc/en-us/articles/4412170923924#h_01FP8BXRYRTQM6QKB9FPH2FQM7
    - 


**1.** PWK PDF workbook  (search for an alternative for Buffer Overflow ) + PWK labs. 

Goal: having 25 host compromised

**2.** Go through these courses:
- Windows Privilege Escalation  
[https://www.udemy.com/course/windows-privilege-escalation-for-beginners/](https://www.udemy.com/course/windows-privilege-escalation-for-beginners/ "https://www.udemy.com/course/windows-privilege-escalation-for-beginners/")  
- Linux Privilege Escalation  
[https://www.udemy.com/course/linux-privilege-escalation-for-beginners/](https://www.udemy.com/course/linux-privilege-escalation-for-beginners/ "https://www.udemy.com/course/linux-privilege-escalation-for-beginners/")
- Next, get ready to learn Buffer Overflow, the RIGHT way. Go watch TCM’s Buffer Overflow Series, use my Github reference guide for an easy recap of TCM’s playlist and to clone the scripts that you’ll need prior to the start:
- TCM’s Buffer Overflow Series  
[https://www.youtube.com/playlist?list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G](https://www.youtube.com/playlist?list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G "https://www.youtube.com/playlist?list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G")  
- Buffer Overflow Guide  
[https://github.com/johnjhacking/Buffer-Overflow-Guide](https://github.com/johnjhacking/Buffer-Overflow-Guide "https://github.com/johnjhacking/Buffer-Overflow-Guide")
Maybe THM to reforce Buffer Overflow [https://tryhackme.com/path/outline/pentesting](https://tryhackme.com/path/outline/pentesting "https://tryhackme.com/path/outline/pentesting")

**3**. TJ Null’s Retired Box List on HackTheBox
Do **NOT** complete these boxes, save them for the dry run!  **Sense, Cronos, Chatterbox, Jeeves**

**4.** Dry Run is a step to test your mettle and preparedness for the exam. Practicing a full exam. Schedule 24 hours where you can hack as if you were taking the OSCP. **Your Practice Environment:**  
Buffer Overflow Machine (25 Points)  
Jeeves (25 Points)  
Chatterbox (20 Points)  
Cronos (20 Points)  
Sense (10 Points)
 If you can acquire 70 points, you’re in a good place. You’ll want to know that you can get that buffer overflow done in two hours or less.
 
**5.** TryHackMe king of the hill



## The exam

### Exploit Code

If you have not made any modifications to an exploit, you should only provide the URL where the exploit can be found. Do not include the full unmodified code, especially if it is several pages long.

If you have modified an exploit, you should include:

-   The modified exploit code
-   The URL to the original exploit code
-   The command used to generate any shellcode (if applicable)
-   Highlighted changes you have made
-   An explanation of why those changes were made

### Exam Proofs

Your objective is to exploit each of the target machines and provide proof of exploitation. Each target machine contains at least one proof file (local.txt or proof.txt), which you must retrieve, submit in your control panel, and include in a screenshot with your documentation.

The valid way to provide the contents of the proof files is in an interactive shell on the target machine with the `type` or `cat` command from their original location.
**Obtaining the contents of the proof files in any other way will result in zero points for the target machine; this includes any type of web-based shell.**

On all Windows targets, you must have a shell running with the permissions of one of the following to receive full points:

-   SYSTEM user
-   Administrator user
-   User with Administrator privileges

On all Linux targets, you must have a root shell in order to receive full points.


### Screenshot Requirements

Each local.txt and proof.txt found must be shown in a screenshot that includes the contents of the file, as well as the **IP address** of the target by using `ipconfig`, `ifconfig` or `ip addr`. An example of this is shown below:

![proof-text.png](https://help.offensive-security.com/hc/article_attachments/360085581591/proof-text.png)


### Exam restrictions

You cannot use any of the following on the exam:

- Spoofing (IP, ARP, DNS, NBNS, etc)
- Commercial tools or services (Metasploit Pro, Burp Pro, etc.)
- Automatic exploitation tools (e.g. db_autopwn, browser_autopwn, SQLmap, SQLninja etc.)
- Mass vulnerability scanners (e.g. Nessus, NeXpose, OpenVAS, Canvas, Core Impact, SAINT, etc.)
- Chatbots (e.g. ChatGPT, YouChat, etc.)
- Features in other tools that utilize either forbidden or restricted exam limitations

You may however, use tools such as Nmap (and its scripting engine), Nikto, Burp Free, DirBuster etc. against any of your target systems.

### Metasploit restrictions

The usage of Metasploit and the Meterpreter payload are restricted during the exam. You may only use Metasploit modules ( **Auxiliary, Exploit, and Post** ) or the Meterpreter payload against **one** single target machine of your choice. Once you have selected your one target machine, you cannot use Metasploit modules ( Auxiliary, Exploit, or Post ) or the Meterpreter payload against any other machines.

Metasploit/Meterpreter **should not** be used to test vulnerabilities on multiple machines before selecting your one target machine ( this includes the use of **check** ) . You may use Metasploit/Meterpreter as many times as you would like against your one target machine.

If you decide to use Metasploit or Meterpreter on a specific target and the attack fails, then you **may not** attempt to use it on a second target. In other words, the use of Metasploit and Meterpreter becomes locked in as soon as you decide to use either one of them.

Metasploit **cannot** be used for **pivoting**, because it would thereby be used on more than one target.

You may use the following against all of the target machines:

-   multi handler (aka exploit/multi/handler)
-   msfvenom
-   pattern_create.rb
-   pattern_offset.rb

### Machine Reverts

You have a limit of 24 reverts. This limit can be reset once during the exam. All of the machines have been freshly reverted at the start of your exam so you will not be required to revert the machines when you begin. Please wait patiently for the machine to revert and only click the button once per attempt. Note that reverting a target machine will cause it to return to its original state and any changes you have made to the machine will be lost.

---

### Exam Proof Filenames

-   proof.txt - This file is only accessible to the root or Administrator user and can be found under the **/root/** directory or the **Administrator Desktop.** 
-   local.txt - This file is accessible to an un-privileged user account.