---
title: Git - A version controller system for programming 
author: amandaguglieri
draft: false
TableOfContents: true
---

# Git - A version controller system for programming

Git is  a distributed version control system that tracks changes in any set of computer files, usually used for coordinating work among programmers [wikipedia](https://en.wikipedia.org/wiki/Git)

## Install

From: https://git-scm.com/

## Git basic commands

Go to your prooject folder and, then, initialize a repo with

```bash
git init
```

Once you do that, you will see a .git folder in your project folder.

### git status

This tells you what it is not still saved in the repository. These are the "untrack" files.

```bash
git status
```


### git add

"Git add" add changed files/folders to the repository staging area of the branch. It tracks them. You can add a single file with:

```bash
git add <file>
```

You can also add a folder

```bash
git add <folder>
```
You can add all unstaged files with a dot: 

```
git add .
```

### git rm --cached

You can unstage files from being commited

```bash
git rm --cached <file>
```

### git commit

Commit the changes you have staged properly with:

```bash
git commit -m "message that describes what you have changed"
```

To undo the most recent commit we've made:

```bash
git reset --soft HEAD~
```

### git config

To setup user name and user email:

```bash
git config --global user.name "NameOfUser"
git config --global user.email "email@email.com"
```


### git branch

To create a new branch:
```
git branch <newBranchName>
```

To list all existing branches:

```bash
git branch
```

To switch to a branch:

```bash
git checkout <destinationBranch>
```

To create a new branch and checkout into it in one command:

```bash
git checkout -b <branchName>
```
To delete a branch:

```bash
git branch <branchName> -d
```

If you want to force the deletion (maybe some changes are not staged), then:

```bash
git branch <branchName> -D
```


### git merge

Having two branches (main and newbranch), to merge changes contained in newbranch to main branch, go to main branch with "git checkout main" and merge the new branch with:

```bash
git merge <newBranch>
```

### git log

It displays all commits and their commit message. Every commit has an id associated. Yo can use that id for reverting changes.

```bash
git log
```

### git revert

It allows us to revert back to a previous version of our project.

```bash
git revert <commitId>
```

### .gitignore

It's a configuration file that allows you to hide existing files and folders in your repository. Content listed there don't get pushed to a public repository. The file is called .gitignore and has one line per resource to be ignored.

Also, important,  if a file was staged before you will need to remove it from cache...

### git remove --cached

To remove from cached files and include it later into the .gitignore file list.

```bash
git remove --cache <fileName>
```

### git remote 

To check out which remote repository our local repository is connected to:

```bash
git remote
```

To connect my local project folder to the github repo.

```bash
git remote add origin https://github.com/username/reponame.git
```


### git push

To push our local changes into the connected github repo:

```bash
git push -u origin main
```

Note: origin references the connection, and main is because we are in the main branch (that's what we are pushing). The first git push is a little different from future gitpushes, since we'll need to use the -u gflag in order to set origin as the defaulto remote repository so we won't have to provide its name every time.

### Some tricks

#### Counting commits

```
git rev-list --count
```

If you want to specify a branch name:

```
git rev-list --count <branch>
```

#### Backing-up untracked files
Git, along with some Bash command piping, makes it easy to create a zip archive for your untracked files.

```
$ git ls-files --others --exclude-standard -z |\
xargs -0 tar rvf ~/backup-untracked.zip
```

#### Viewing a file of another branch

Sometimes you want to view the content of the file from another branch. It's possible with a simple Git command, and without actually switching your branch.

Suppose you have a file called README.md, and it's in the main branch. You're working on a branch called dev: git show main:README.md

```
git show <branchName>:<fileName>
```

#### Modify author in commits

```bash
# Make sure that the author is set globally
git config --global user.name "username"     
git config --global user.email "whatever@example.com"    

git rebase -r 787dda7 --exec 'git commit --amend --no-edit --reset-author'
# -r: rebase until the commit
# --exec: here we place the command to reset the author

git add .
git commit -m "updating author"

# After that:
git push --force origin main
```

## Submodules

#### Use Git Submodules – recommended if want to keep each original repo’s history


```bash
mkdir Privescalation
cd Privescalation
git init
git remote add origin git@github.com:[USERNAME]/Privescalation.git


git clone  https://github.com/itm4n/PrivescCheck.git temp
mkdir -p tools
mv temp tools/PrivescCheck
rm -rf tools/PrivescCheck/.git

git add tools/PrivescCheck
git commit -m "Add PrivescCheck source"
git push -u origin main
```

The following tools will be

```bash
cd Privescalation

git clone  https://github.com/repo/toolName.git temp
mv temp tools/toolName
rm -rf tools/toolName/.git

git add tools/toolName
git commit -m "Add toolName source"
git push -u origin main
```

For instance, this [SeRestoreAbuse](https://github.com/xct/SeRestoreAbuse) repo:

```bash
cd Privescalation

git clone https://github.com/xct/SeRestoreAbuse.git temp
mv temp tools/SeRestoreAbuse
rm -rf tools/SeRestoreAbuse/.git

git add tools/SeRestoreAbuse
git commit -m "Add SeRestoreAbuse source"
git push -u origin main


git commit -m "Add SeRestoreAbuse binaries"
```

Or this other https://github.com/rvazarkar/GMSAPasswordReader.git

```bash
cd Privescalation

git clone https://github.com/rvazarkar/GMSAPasswordReader.git temp
mv temp tools/GMSAPasswordReader
rm -rf tools/GMSAPasswordReader/.git

git add tools/GMSAPasswordReader
git commit -m "Add GMSAPasswordReader tools from rvazarkar/GMSAPasswordReader source"
git push -u origin main


git commit -m "Add SeLoadDriverPrivilege binaries"
```

Troubleshooting. It's very common for third parties to have a .gitignore file that prevents folder Debug and folder Release to be uploaded. Locate it with:

```bash
git check-ignore -v tools/SeManageVolumeAbuse/releases/x64/SeManageVolumeAbuse.exe 
```


## Pentesting git

Source: https://thecyberpunker.com/tools/git-exposed-pentesting-git-tools/

### git-dumper

[https://github.com/arthaud/git-dumper](https://github.com/arthaud/git-dumper)

