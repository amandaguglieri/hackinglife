---
title: SSH for github
author: amandaguglieri
draft: false
TableOfContents: true
---

# SSH for github

## How to configure multiple two or more deploy keys for different private github repositories on the same computer without using ssh-agent

Let's say I want to have a ssh key A for repo1 and ssh key b for repo2. 

1. Create a ssh pair keys for each repository

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
# ed25519 is the algorithm
```

For the second key and the subsequent ones, you will need to specify a different name.

+ Private key should have permissions set to 600.
+ .ssh folder should have permissions set to 700.

2. Add your SSH keys to the ssh-agent. In my case 

```bash
# start the ssh-agent in the background
eval "$(ssh-agent -s)"

# add your ssh private key to the ssh-agent.
ssh-add ~/.ssh/id_ed25519
```

3. Add your ssh public keys as deploy keys in the Settings tab of repo1 and repo2 .

4. Edit .git/config file in both repositories.

```
# For repo1
[remote "origin"]
        url = "ssh://git@repo1.github.com:username/repo1.git"

# For repo2
[remote "origin"]
        url = "ssh://git@repo2.github.com:username/repo2.git"
```

5. For each repo set name and email

```bash
# navigate to your repo1
git config user.name "yourName1"
git config user.email "email1@domain.com"

# navigate to your repo2
git config user.name "name2"
git config user.email "email2@domain.com"
```

6. Create a config file in .ssh to manage keys:

```
# Default github account: username1
Host github.com/username1
   HostName github.com
   IdentityFile ~/.ssh/username1_private_key
   IdentitiesOnly yes
   
# Other github account: username2
Host github.com/username2
   HostName github.com
   IdentityFile ~/.ssh/username2_private_key
   IdentitiesOnly yes
```


7. Make sure you don't have all credentials cached in your ssh agent

```
ssh-add -D
```

8. Add new credentials to your ssh agent

```
ssh-add ~/.ssh/username1_private_key
ssh-add ~/.ssh/username2_private_key
```

9. See added keys

```
ssh-add -l
```

10. Test your conection

```bash
ssh -T git@github.com
```
