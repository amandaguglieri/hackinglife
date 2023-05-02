---
title: Creating malware and custom payloads
author: amandaguglieri
draft: false
TableOfContents: true
---

# Creating malware and custom payloads


## msfvenom

[msfvenom cheat sheet](msfvenom.md).


## Empire

[Empire cheat sheet](empire.md).


## AV0id

AV0id.


## Syringe

syringe


## FatRat

[FatRat cheat sheet](fatrat.md).


## Veil 

[Veil cheat sheet](veil.md).


## Creating malware in pdf

These two modules in metasploit:

+ exploit/windows/fileformat/adobe_pdf_embedded_exe
+ exploit/windows/fileformat/adobe_pdf_embedded_exe_nojs 


## Creating malware in word document

**1.** Craft an executable

Use for instance [veil](veil.md).

**2.** Convert it to a VisualBasic script - macro code

```bash
locate exe2vba
# Result: /usr/share/metasploit-framework/tools/exploit/exe2vba.rb

# Go to the folder
cd /usr/share/metasploit-framework/tools/exploit/

# Create the malicious vba script
./exe2vba.rb <first-parameter> path/to/nameOfOutputFile.vba
# first parameter: malicious executable file that will be converted to macro code. Take the path to the .exe file provided by veil
```

**3.** Create an MS Word document

**4.** Opena new macro and embed macro code

**5.** Copy the payload as text in the word document. If it's too long, disguise it (set font color to white).

**6.** Convince the victim to have macros enabled.

**7.** Start a listener and wait for the victim to connect.


## Creating malware in a Firefox addon

Use the metasploit module to generate the addon: exploit/multi/browser/firefox_xpi_bootstrapped_addon

It will be served from SRVHOST:SRVPORT/URIPATH. This URL you can serve it from a phishing email.
