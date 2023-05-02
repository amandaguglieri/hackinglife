---
title: winspy - A tool to view windows properties in the system
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
  - thick client
---

# winspy - A tool to view windows properties in the system 


## Installation

Download it from [https://www.catch22.net/software/winspy](https://www.catch22.net/software/winspy#)

## What it does

Basically winspy allows us to  select and view the properties of any window in the system.  WinSpy is based around the Spy++ utility that ships with Microsoft Visual Studio.

It allows us to retrieve passwords from password-edit controls.

Here an example:

![[Pasted image 20230201192438.png]]

Another nice example:

![[Pasted image 20230201192528.png]]


Here a list of all windows properties that it retrieves:

-   Window Class and Name.
-   Window procedure address.
-   All window styles and extended styles.
-   Window properties (set using the SetProp API call).
-   Complete Child and Sibling window relationships.
-   Scrollbar positional information.
-   Full window Class information.
-   Retrieve passwords from password-edit controls!
-   Edit window styles!
-   Alter window captions!
-   Show / Hide / Enable / Disable / Adjust any window in the system!
-   Massively improved user-interface!
-   View the complete system window hierarchy!
-   Multi-monitor support!
-   Now works correctly for all versions of Windows.
-   Tree hierarchy now groups by process.