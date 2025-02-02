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


## pyenv

**Install prerequisites**: Ensure you have the required dependencies for `pyenv` installation.

```
sudo apt update sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev \ libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \ xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git
```

**Install `pyenv`**: Use the following commands to install `pyenv`:

```
curl https://pyenv.run | bash
```


Update .bashrc to set up pyenv: Add the following to your .bashrc (or .zshrc if using zsh):

```
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Then, reload your shell configuration:

```
pyenv install 2.7.18
```


This command installs Python 2.7.18, or you can choose another Python 2.7 version if needed.

Create a Python 2.7 virtual environment: Once Python 2.7 is installed, you can create a virtual environment with:

```
pyenv virtualenv 2.7.18 env_name
```

**Activate the virtual environment**: To activate the environment, run:

```
pyenv activate env_name
```

Or deactivate:

```
deactivate
```
