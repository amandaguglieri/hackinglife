---
title: Python Library Hijacking
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege
  - escalation
  - linux
---
# Python Library Hijacking

Many libraries are used in Python and are used in many different fields. One of them is [NumPy](https://numpy.org/doc/stable/).

`NumPy` is an open-source extension for Python. The module provides precompiled functions for numerical analysis.

Another library is [Pandas](https://pandas.pydata.org/docs/). `Pandas` is a library for data processing and data analysis with Python. It extends Python with data structures and functions for processing data tables. A particular strength of Pandas is time series analysis.

Python has [the Python standard library](https://docs.python.org/3/library/), with many modules on board from a standard installation of Python. These modules provide many solutions that would otherwise have to be laboriously worked out by writing our programs. 

Importing modules:

```python
#!/usr/bin/env python3

# Method 1
import pandas

# Method 2
from pandas import *

# Method 3
from pandas import Series
```

There are many ways in which we can hijack a Python library. Much depends on the script and its contents itself. However, there are three basic vulnerabilities where hijacking can be used:

1. Wrong write permissions
2. Library Path
3. PYTHONPATH environment variable


## Wrong Write Permissions

In a development environment a python module has write permissions set for all users by mistake. If a python script importing that module has `DUID / SGID` permissions, we could include malicious code in the imported python module. 

Where are these modules located? A typical location would be `/usr/local/lib/python3.8/dist-packages/nameOfLibrary/*`.  

Example, searching for the module psutil:

```shell-session
pip3 show psutil
```

When reading the scripts that imports the module, see which function is importing/using.  For instance, if we have a script lala.py that import psutil module and uses the function virtual_memory, try to locate that function in the module:

```shell-session
grep -r "def virtual_memory" /usr/local/lib/python3.8/dist-packages/psutil/*
```

Then you can spot the file implementing the function and check if you have write access and add to the function a payload. An example of a payload would be:

```
#### Hijacking
	import os
	os.system('id')
```

Now we can run the script with sudo and check if we get the desired result.

## Library Path

In Python, each version has a specified order in which libraries (modules) are searched and imported from. The order in which Python imports modules from are based on a priority system, meaning that paths higher on the list take priority over ones lower on the list. 

PYTHONPATH Listing: 

```shell-session
python3 -c 'import sys; print("\n".join(sys.path))'
```

For the attack to succeed we need

1. The module that is imported by the script is located under one of the lower priority paths listed via the `PYTHONPATH` variable.
2. We must have write permissions to one of the paths having a higher priority on the list.

If this is the case we can create a module ourselves with the same name and include our own desired functions.

Now we locate our library (example: psutil library):

```shell-session
pip3 show psutil
```

Ok, now we need to ensure that the location is in a lower position within the PYTHONPATH variable (see the listing above).

Now, we also need to check that we have write permissions on at least one of the locations listed before in the PYTHONPATH variable.

```
ls -la /path/to/module
```

Then, we can craft a module named after the one called by the script (in the example psutil.py):

```python
#!/usr/bin/env python3

import os

def virtual_memory():
    os.system('id')
```

Now we run the script and it will call to our crafted library.

## PYTHONPATH Environment Variable

PYTHONPATH is an environment variable that indicates what directory (or directories) Python can search for modules to import

If a user is allowed to manipulate and set this variable while running the python binary, they can effectively redirect Python's search functionality to a user-defined location when it comes time to import modules.
