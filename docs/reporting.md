---
title: Documentation and reporting
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - CPTS
---

# Documentation and reporting

There are many tools available for notetaking, and the choice is very much personal preference. Here are some of the options available:

|                                                       |                                                      |                                              |
| ----------------------------------------------------- | ---------------------------------------------------- | -------------------------------------------- |
| [CherryTree](https://www.giuspen.com/cherrytree/)     | [Visual Studio Code](https://code.visualstudio.com/) | [Evernote](https://evernote.com/)            |
| [Notion](https://www.notion.so/)                      | [GitBook](https://www.gitbook.com/)                  | [Sublime Text](https://www.sublimetext.com/) |
| [Notepad++](https://notepad-plus-plus.org/downloads/) | [OneNote](https://www.onenote.com/?public=1)         | [Outline](https://www.getoutline.com/)       |
| [Obsidian](https://obsidian.md/)                      | [Cryptpad](https://cryptpad.fr/)                     | [Standard Notes](https://standardnotes.com/) |


Logging tools: [tmux](tmux.md)

### Suggested organization

Below is a suggested baseline folder structure: 

- `Admin`
    
    - Scope of Work (SoW) that you're working off of, your notes from the project kickoff meeting, status reports, vulnerability notifications, etc
- `Deliverables`
    
    - Folder for keeping your deliverables as you work through them. This will often be your report but can include other items such as supplemental spreadsheets and slide decks, depending on the specific client requirements.
- `Evidence`
    
    - Findings
        - We suggest creating a folder for each finding you plan to include in the report to keep your evidence for each finding in a container to make piecing the walkthrough together easier when you write the report.
    - Scans
        - Vulnerability scans
            - Export files from your vulnerability scanner (if applicable for the assessment type) for archiving.
        - Service Enumeration
            - Export files from tools you use to enumerate services in the target environment like Nmap, Masscan, Rumble, etc.
        - Web
            - Export files for tools such as ZAP or Burp state files, EyeWitness, Aquatone, etc.
        - AD Enumeration
            - JSON files from BloodHound, CSV files generated from PowerView or ADRecon, Ping Castle data, Snaffler log files, CrackMapExec logs, data from Impacket tools, etc.
    - Notes
        - A folder to keep your notes in.
    - OSINT
        - Any OSINT output from tools like Intelx and Maltego that doesn't fit well in your notes document.
    - Wireless
        - Optional if wireless testing is in scope, you can use this folder for output from wireless testing tools.
    - Logging output
        - Logging output from Tmux, Metasploit, and any other log output that does not fit the `Scan` subdirectories listed above.
    - Misc Files
        - Web shells, payloads, custom scripts, and any other files generated during the assessment that are relevant to the project.
- `Retest`
    
    - This is an optional folder if you need to return after the original assessment and retest the previously discovered findings. You may want to replicate the folder structure you used during the initial assessment in this directory to keep your retest evidence separate from your original evidence.


It's a good idea to have scripts and tricks for setting up at the beginning of an assessment. We could take the following command to make our directories and subdirectories and adapt it further.

```shell-session
 mkdir -p ACME-IPT/{Admin,Deliverables,Evidence/{Findings,Scans/{Vuln,Service,Web,'AD Enumeration'},Notes,OSINT,Wireless,'Logging output','Misc Files'},Retest}


tree ACME-IPT/
```

