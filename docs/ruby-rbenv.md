---
title: Ruby and rbenv Cheat Sheet
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - ruby
  - rbenv
---
# Ruby and rbenv Cheat Sheet

## Essential Ruby and rbenv Commands

### Check Installed Ruby Version

```sh
ruby -v
```

### Install Multiple Ruby Versions

```sh
rbenv install 3.0.6
rbenv install 3.1.0
```

### List Installed Versions

```sh
rbenv versions
```

### Set Global Ruby Version

```sh
rbenv global <version>
```

### Set Local Ruby Version (Per Directory)

```sh
rbenv local <version>
```

### Update Shims (Ensure Commands Use the Correct Ruby Version)

```sh
rbenv rehash
```

### Install a Gem System-Wide

```sh
gem install <gem_name>
```

---

## Troubleshooting Running WPScan with Ruby 3.0.6 and Metasploit with Ruby 3.1.0

### Step 1: Set Global Ruby Version for WPScan

To ensure WPScan runs with Ruby 3.0.6, set it as the global version:

```sh
rbenv global 3.0.6
rbenv rehash
```

Verify the active version:

```sh
rbenv versions
```

Install WPScan:

```sh
gem install wpscan
```

### Step 2: Configure Ruby 3.1.0 for Metasploit

To ensure Metasploit uses Ruby 3.1.0, set a local Ruby version inside its directory:

```sh
cd /usr/share/metasploit-framework
rbenv local 3.1.0
rbenv rehash
```

### Running Metasploit from Any Directory

By default, `msfconsole -q` will only work inside `/usr/share/metasploit-framework`. To run it from anywhere, use one of these approaches:

#### Approach 1: Specify the Version Inline

```sh
RBENV_VERSION=3.1.0 msfconsole -q
```

#### Approach 2: Create a Wrapper Script (Recommended)

Modify your `.zshrc` file:

```sh
sudo nano ~/.zshrc
```

Add the following function at the bottom:

```sh
# Wrapper for Metasploit to ensure it runs with Ruby 3.1.0
msfconsole() {
  echo "Launching Metasploit..."
  (cd /usr/share/metasploit-framework && exec /usr/share/metasploit-framework/msfconsole "$@")
}
```

Apply the changes:

```sh
source ~/.zshrc
```

Now, both `wpscan` and `msfconsole` can be used from anywhere in the system with their respective Ruby versions.