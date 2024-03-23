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


## mkvirtualenv

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
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
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


# To work on another version of python:
mkvirtualenv -p python3.x venv_name
# You will see something like this: (venv_name)
```
