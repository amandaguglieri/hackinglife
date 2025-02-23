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

These steps will help you list all the virtual environment management tools available on your Kali system. 

Check System-Wide Package Managers for Installed Tools:

```bash
# Using APT (Default Kali Package Manager)
dpkg --get-selections | grep -E "pyenv|virtualenv|pipenv|conda"

# Using pip to List Installed Python Packages
pip list | grep -E "virtualenv|pipenv|pyenv|conda"


# Verify Installed Tools' Locations
which pyenv
which virtualenv
which pipenv
which conda
```

## Python vs. pyenv


We may have **two different Python environments** on the system:

1. **System Python (Managed by `update-alternatives`)**
    
    - Installed globally in `/usr/bin/python`, `/usr/bin/python3.x`
    - Used by system packages (like APT, scripts in `/usr/bin`, or Kali dependencies)
    - Controlled via `update-alternatives`
    - Can be **Python 3.11** (or any other preferred default)

2. **pyenv Python (User-Managed)**
    
    - Installs Python versions under `~/.pyenv/versions/`
    - Allows switching between multiple Python versions per project or globally
    - Uses **shims** (`~/.pyenv/shims/`) to redirect `python` to the right version
    - **Overrides system Python when active**

**How They Coexist**

- **When pyenv is inactive**, the system **uses the Python version set by `update-alternatives`** (e.g., `/usr/bin/python3.11`).
- **When pyenv is active**, it **intercepts the `python` command** and runs its own managed Python versions from `~/.pyenv/versions/`.
- **Pyenv does NOT modify or replace system Python**—it just **redirects** the `python` command using a shim.

### How to Make Them Work Together

 **1. Set Python 3.11 as System Default (For System-Wide Use)**

```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.11 4 sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 4 sudo update-alternatives --config python sudo update-alternatives --config python3`
```

This makes sure that, when pyenv is NOT active, Python 3.11 is used.


**2. Make Sure Pyenv Works Properly**

Make sure pyenv is correctly installed in your shell:

```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

To persist these settings, add them to `~/.zshrc` or `~/.bashrc`:

```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc 
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc 
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc 
echo 'eval "$(pyenv init -)"' >> ~/.zshrc source ~/.zshrc
```

Now, when you **activate pyenv**, it will take control over Python.

**3. Switching Between System Python and Pyenv**

Use System Python (Python 3.11 from `update-alternatives`). To temporarily disable pyenv and use system Python:

```
pyenv global system
python -V  # Should return Python 3.11
```

Use a Pyenv-Managed Python Version
To switch to a specific pyenv-managed Python version:

```
pyenv install 3.10.6
pyenv global 3.10.6
python -V  # Should return Python 3.10.6
```

**4. To use a project-specific version:**

```
cd my_project
pyenv local 3.9.0
python -V  # Should return Python 3.9.0
```

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
