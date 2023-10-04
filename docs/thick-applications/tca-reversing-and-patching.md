---
title: Reversing and patching thick clients applications
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - thick client applications
  - thick client applications pentesting
  - dnspy
  - dotpeek
  - ilspy
  - reflexil
  - ilasm
  - idasm
---

# Reversing and patching thick clients applications

!!! abstract "General index of the course"
    - [Tools for pentesting thick client applications](tools-for-thick-apps.md).
    - [Introduction](tca-introduction.md).
    - [Basic lab setup](tca-basic-lab-setup.md).
    - [First challenge: enabling a button](tca-first-challenge.md).
    - [Information gathering phase](tca-information-gathering-phase.md).
    - [Traffic analysis](tca-traffic-analysis.md).
    - [Attacking thick clients applications](tca-attacking-thick-clients-applications.md).
    - [Reversing and patching thick clients applications](tca-reversing-and-patching.md).    
    - [Common vulnerabilities](tca-common-vulnerabilities.md).



## Reversing .NET applications

### Required software

- [dnspy](../dnspy.md): c# code + IL code + patching the application
- [dotPeek](../dotpeek.md) (from JetBrains)
- ILspy / Reflexil
- ILASM (IL Assembler) (comes with .NET Framework).
- ILDASM (IL Disassembler) (comes with Visual Studio).

IL stands for Intermediate Language.

### Installing Visual Studio Community 2019 (version 16.11)

Download from: https://my.visualstudio.com/Downloads?q=Visual%20Studio%202019

![graphic](../img/tca-56.png)


### Installing dotPeek

[dotPeek Cheatsheet](../dotpeek.md) 
Download from: https://www.jetbrains.com/es-es/decompiler/download/#section=web-installer

![graphic](../img/tca-57.png)


## decompiling with dotPeek + executing with Visual Studio

We will try to decompile the app using dotPeek to decrypt the database connection. Remember from the config file 

```

      <add key="DBPASSWORD" value="CTsvjZ0jQghXYWbSRcPxpQ==" />
      <add key="AESKEY" value="J8gLXc454o5tW2HEF7HahcXPufj9v8k8" />
      <add key="IV" value="fq20T0gMnXa6g0l4" />
```


(The config file was  DVTA.exe.Config, located in the same directory as the app).

We will use dotpeek + Visual Studio to understand the logic under that connection.

Open the app DVTA from dotpeek, go to DVTA>References>DBAccess and double click it. Then you will get a Resource uploaded with the name > DBAccess Class. In it there is a function called decryptPassword() 

```
public string decryptPassword()
    {
      string s1 = ConfigurationManager.AppSettings["DBPASSWORD"].ToString();
      string s2 = ConfigurationManager.AppSettings["AESKEY"].ToString();
      string s3 = ConfigurationManager.AppSettings["IV"].ToString();
      byte[] inputBuffer = Convert.FromBase64String(s1);
      AesCryptoServiceProvider cryptoServiceProvider = new AesCryptoServiceProvider();
      cryptoServiceProvider.BlockSize = 128;
      cryptoServiceProvider.KeySize = 256;
      cryptoServiceProvider.Key = Encoding.ASCII.GetBytes(s2);
      cryptoServiceProvider.IV = Encoding.ASCII.GetBytes(s3);
      cryptoServiceProvider.Padding = PaddingMode.PKCS7;
      cryptoServiceProvider.Mode = CipherMode.CBC;
      this.decryptedDBPassword = Encoding.ASCII.GetString(cryptoServiceProvider.CreateDecryptor(cryptoServiceProvider.Key, cryptoServiceProvider.IV).TransformFinalBlock(inputBuffer, 0, inputBuffer.Length));
      Console.WriteLine(this.decryptedDBPassword);
      return this.decryptedDBPassword;
```

![graphic](../img/tca-57.png)

So we will open Visual Studio and we will create a New Project, a Windows Form  Application (.NET Framework).
We will call the project PasswordDecryptor. 
Create a button. Name it Decrypt.

![graphic](../img/tca-58.png)



By double-clicking on the Decrypt button we will be taken to the Source code of that button.

This is what we are going to put in that button:

```
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Security.Cryptography;

namespace decryptorpassword
{
    public partial class Decrypt : Form
    {
        public Decrypt()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string dbpassword = "CTsvjZ0jQghXYWbSRcPxpQ==";
            string  aeskey = "J8gLXc454o5tW2HEF7HahcXPufj9v8k8";
            string iv = "fq20T0gMnXa6g0l4";
            byte[] inputBuffer = Convert.FromBase64String(dbpassword);
            AesCryptoServiceProvider cryptoServiceProvider = new AesCryptoServiceProvider();
            cryptoServiceProvider.BlockSize = 128;
            cryptoServiceProvider.KeySize = 256;
            cryptoServiceProvider.Key = Encoding.ASCII.GetBytes(aeskey);
            cryptoServiceProvider.IV = Encoding.ASCII.GetBytes(iv);
            cryptoServiceProvider.Padding = PaddingMode.PKCS7;
            cryptoServiceProvider.Mode = CipherMode.CBC;
            string decryptedDBPassword = Encoding.ASCII.GetString(cryptoServiceProvider.CreateDecryptor(cryptoServiceProvider.Key, cryptoServiceProvider.IV).TransformFinalBlock(inputBuffer, 0, inputBuffer.Length));
            Console.WriteLine(decryptedDBPassword);
        }
    }
}
```


Some things not said in the video: it's quite possible you will need to debug this simple application. For that, the best thing to do is reading error messages and try to fix them. In my case,  a basic library for the execution of this code was missing:

```
using System.Security.Cryptography;
```

Also, it was needed to rename the .exe output file in the Main() function like this

```
# what it said
  Application.Run(new Form1());
# what it needed to say to match to my code
  Application.Run(new Decrypt());
```



## Decompiling and executing with dnspy

**1.** Open the application in dnspy. Go to Login. Click on namespace DBAccess

![graphic](../img/tca-60.png)

**2.** Click on DBAccessClass

![graphic](../img/tca-61.png)

**3.** Locate the function decryptPassword(). That's the one we would love to run. For that locate where it is called from. Add a Breakpoint there. Run the code. You will be asked about which executable to run (select DVTA.exe). After that, the code will be executed up to the breakpoint. Enter credentials and see in the Notification area how variables are being called.

![graphic](../img/tca-62.png)

Eventually, you will see the decrypted connection string in those variables. You can add more breakpoints.

![graphic](../img/tca-63.png)


## Using ILSpy + Reflexil to patch applications


### ILSpy Setup

Repository: [https://github.com/icsharpcode/ILSpy/releases](https://github.com/icsharpcode/ILSpy/releases)

Requirements: .NET 6.0. Download zip to tools. Place the file ILSpy_binaries_8.0.0.7246-preview3.zip into the tool folder and extract files. 

### Setup Reflexil plugin in ILSpy

**1.** Download from: https://github.com/sailro/Reflexil/releases

**2.** Place the file reflexil.for.ILSpy.2.7.bin into tools and extract files. 

**3.** Enter the Reflexil folder and copy the .dll file Reflexil.ILSpy.Plugin.dll. 

**4.** Place it into ILSpy directory. Now the plugin is installed.


### Patching with ILSpy + Reflexil

One interesting thing about ILSpy (different from other tools) is that you can see code in 3 modes: IL, C# and the combined mode, C# + IL. This last mode comes in hand to be able to interpretate much better what the code is about.

**1.** Open DVTA app from ILSpy and locate this code:

![code](../img/tca-64.png)

Access to the admin pannel is decided with an IF statement and a integer variable set to 0/1. We will modify this value using ILSpy + Reflexil and patch again the application.

**2.** Open Reflexil plugin:

![code](../img/tca-65.png)


**3.** In the Reflexil pannel, look for the specific instruction (the one that moves to the pile the value 1) and change the value to 0. 

![code](../img/tca-66.png)


**4.** Save the changes in your DVTA application with a different name:

![code](../img/tca-67.png)


**5.** When opening the new saved application, you will access admin pannel even if you login with normal user credentials.

![code](../img/tca-68.png)


## Using ilasm and ldasm to patch applications

ilasm (IL assembler) and ldasm (il disasembler) are tools provided by Microsoft in Visual Studio.

We will use ILDASM to disasembler the DVTA application

```
C:\Program Files (x86)\Microsoft SDKs\Windows\v10.0A\bin\NETFX 4.8 Tools\ildasm.exe
```

And ILASM to assemble again the application:

```
C:\Windows\Microsoft.NET\Framework\v4.0.30319\ilasm.exe
```

**1.** Open DVTA.exe with ILDASM.exe from command line:

![code](../img/tca-69.png)


**2.** Dump the folder. FILES> Dump

![code](../img/tca-70.png)

**3.** Save that dumped code (which will be IL) into a folder. Close the ILDASM application. The folder generated contains the IL code. There is an specific file called DVTA.il

**4.** Open DVTA.il in a text editor and modify the instruction you want to modify. In our case we will change "ldc.i4.1" to "ldc.i4.0".

![code](../img/tca-71.png)

**5.** From command line, we will use ILASM to assemble that DVTA.il file into a new application

```
cd C:\Windows\Microsoft.NET\Framework\v4.0.30319\
.\ilasm.exe C:\User\lala\Desktop\RE\DVTA.il
```

## Anti piracy measures implemented by some apps

Mechanism to track or prevent illegitimate copying or usage of the software:

- Does the app use serial keys, or License Keys to ensure that only allowed number of users can load and operate the software?
- Does the application stop operating after the expiration of license or serial key?
- 
- • Tracking back the legitimate and illegitimate usage of the application