

# Pyenv

Popular Python version management tool. Pyenv allows you to easily install and switch between multiple Python versions on the same machine.

Source: https://github.com/pyenv/pyenv

## Installation in Kali

Check out Pyenv where you want it installed. A good place to choose is `$HOME/.pyenv` (but you can install it somewhere else):

```
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

Optionally, try to compile a dynamic Bash extension to speed up Pyenv. Don't worry if it fails; Pyenv will still work normally:

```
cd ~/.pyenv && src/configure && make -C src
```

Define environment variable `PYENV_ROOT` to point to the path where Pyenv will store its data. `$HOME/.pyenv` is the default. If you installed Pyenv via Git checkout, set it to the same location where you cloned it.

```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
```

Add the `pyenv` executable to your `PATH` if it's not already there:

```
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc 
```

Run `eval "$(pyenv init -)"` to install `pyenv` into your shell as a shell function, enable shims, and enable autocompletion:

```
echo 'eval "$(pyenv init -)"' >> ~/.zshrc 
```

Then, if you have `~/.profile`, `~/.bash_profile`, or `~/.bash_login`, add the commands there as well. If you have none of these, add them to `~/.profile`. No need in this case, where we have `~/.zshrc`.

If you wish to get Pyenv in noninteractive login shells as well, also add the commands to `~/.zprofile` or `~/.zlogin`.

## Basic Usage

Install the desired Python versions using pyenv:

```
pyenv install 3.9.0
```

See installed versions:

```
pyenv versions
```

Set global Python version:

```
pyenv global 2.7.18
```

## Managing Different Python Versions for Different Applications

### Set a Local Python Version for a Specific Application

To ensure a specific application runs with Python 3.10.6, navigate to its directory and set a local Python version:

```
cd /path/to/application
pyenv local 3.10.6
pyenv rehash
```

### Running the Application with the Correct Python Version

Pyenv automatically applies the correct Python version when a local version is set. However, you can explicitly specify it if needed:

```
PYENV_VERSION=3.10.6 python script.py
```

### Creating a Wrapper Script (Recommended)

Modify your `.zshrc` or `.bashrc` file:

```
sudo nano ~/.zshrc  # or ~/.bashrc
```

Add the following function at the bottom:

```
# Wrapper for running Python applications with the correct version
run_app() {
  echo "Launching application with Python 3.10.6..."
  (cd /path/to/application && exec python "$@")
}
```

Apply the changes:

```
source ~/.zshrc  # or source ~/.bashrc
```

Now, both general Python usage and application-specific Python versions will work seamlessly.
