---
title: Hugo
author: amandaguglieri
draft: false
TableOfContents: true
---

# Hugo

## Install Hugo

```bash
sudo apt-get install hugo
```

## Hugo basic commands

Go to your project folder and creates a new site 

```bash
hugo new site <name-project>
```

Initialize the repo

```bash
git init
```

Launch the server Hugo so you can open it in your http://localhost:1313

```bash
hugo server
```

Create new content, like for instance:

+ A new chapter:

```bash
hugo new --kind chapter hugo/_index.md
```

+ A new entry:

```bash
hugo new hugo/quick_start.md
```

