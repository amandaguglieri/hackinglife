

# Pyenv

Popular Python version management tool. Pyenv allows you to easily install and switch between multiple Python versions on the same machine.

Source: [https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)

## Installation in Kali

Check out Pyenv where you want it installed. A good place to choose is $HOME/.pyenv (but you can install it somewhere else):

```
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

Optionally, try to compile a dynamic Bash extension to speed up Pyenv. Don't worry if it fails; Pyenv will still work normally:

```
cd ~/.pyenv && src/configure && make -C src
```

Define environment variable PYENV_ROOT to point to the path where Pyenv will store its data. $HOME/.pyenv is the default. If you installed Pyenv via Git checkout, we recommend to set it to the same location as where you cloned it.

```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
```

Add the `pyenv` executable to your `PATH` if it's not already there

```
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc 
```

run `eval "$(pyenv init -)"` to install `pyenv` into your shell as a shell function, enable shims and autocompletion

```
echo 'eval "$(pyenv init -)"' >> ~/.zshrc 
```


Then, if you have ~/.profile, ~/.bash_profile or ~/.bash_login, add the commands there as well. If you have none of these, add them to ~/.profile. No need in this case, where we have ~/.zshrc.

If you wish to get Pyenv in noninteractive login shells as well, also add the commands to ~/.zprofile or ~/.zlogin.


## Basic usage


Install the desired Python versions using pyenv:

```
pyenv install 3.9.0
```

See installed versions:

```
pyenv versions
```

Set global python version:

```
 pyenv global 2.7.18
``` 