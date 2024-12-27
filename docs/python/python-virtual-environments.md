---
title: Virtual environments
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - database
  - relational
  - database
  - SQL
---

# Virtual environments


## virtualenvwrapper 

### Installation

```
# Make sure you have pip installed.
sudo apt-get install python3-pip

# Installing virtualenvwrapper 
sudo pip3 install virtualenvwrapper

# Open bashrc by –
sudo gedit ~/.bashrc

# After opening it, add the following  lines to it :

export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Projects
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
```

### Basic usage

```bash
# Creating a virtual environment with mkvirtualenv
mkvirtualenv nameOfEnvironment

# List exisiting environment in your 
lsvirtualenv -b

# Work on an environment
workon nameOfEnvironment

# Close current environment
deactivate

# Delete virtual environment
rmvirtualenv nameOfEnvironment

# To work on another version of python:
mkvirtualenv -p python3.x venv_name
# You will see something like this: (venv_name)
```


Backing up virtual environment before removing it:

```
pip freeze > requirements.txt
```


## venv

```
python3 -m venv <DIR>
source <DIR>/bin/activate
```

Now you can activate or deactivate the virtual environment with:

```
<DIR>\Scripts\activate
```


