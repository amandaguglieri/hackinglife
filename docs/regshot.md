---
title: regshot
author: amandaguglieri
draft: false
TableOfContents: true
---

# regshot

regshot helps you to identify changes in Registry made by a Thick client application.  It's used to compare the amount of registry entries that have been changed during an installation or a change in your system settings.

## Installation

Download from: https://sourceforge.net/projects/regshot/


## Usage

From the course  [Pentesting thick clients applications](thick-applications/index.md).


**1.**  Run  regshot version according to your thick-app (84 or 64 v).

**2.** Click on "First shot". It will make a "shot" of the existing registry entries.

**3.** Open the app you want to test and login into it.

**4.** Perform some kind of action, like for instance, viewing the profile.

**5.** Take a "Second shot" of the Registry entries.

**6.** After that, you will see the button "Compare" enabled. Click on it.


![graphic](img/tca-42.png)

![graphic](img/tca-43.png)

An HTML file will be generated and you will see the registry entries:

![graphic](img/tca-44.png)

An interesting registry is "isLoggedIn", that has change from false to true. This may be a potential vector of attack (we could set it to true and also change username to admin). 

```
HKU\S-1-5-21-1067632574-3426529128-2637205584-1000\dvta\isLoggedIn: "false"  
HKU\S-1-5-21-1067632574-3426529128-2637205584-1000\dvta\isLoggedIn: "true"
```

![graphic](img/tca-45.png)
