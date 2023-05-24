---
title: Index of walkthroughs
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
---

# Index of walkthroughs

## Well, this is a mess

It feels like an eternity since I embarked on my first walkthroughs of the Overthewire game challenges. However, the reality is that this happened just one year ago (or maybe two). During those days, I was consumed by an intense obsession with documenting every single step I took. Allow me to relive and share a snippet of my explanation for progressing from level 31 to level 32 in Bandit so you can draw your own conclusions:

??? abstract "Click to keep reading why this is a mess"
	```
	1. mkdir /tmp/amanda31
	2. cd /tmp/amanda31
	3. git clone ssh://bandit31-git@localhost/home/bandit31-git/repo
	4. cd repo
	
	# when listing repo, you can realize that there is a .gitignore file
	5. ls -la
	
	# Print the .gitignore file to see which changes are not being commited
	6. cat .gitignore
	
	# "*.txt" files are being excluded from being pushed
	7. cat README.md
	
	# README.md file will provide you with the instructions to pass the level: "This time your task is to push a file to the remote repository.
	# Details:
	#    File name: key.txt
	#    Content: 'May I come in?'
	#    Branch: master  "
	
	# Remove "*.txt" from .gitignore"
	8. echo "" > .gitignore
	
	# Create a key.txt file
	9. echo "May I come in?" > ./.git/key.txt
	
	# Add these changes to the commit
	10. git add -A
	
	# Commit the changes in your repository. A line with the explanation of the changes may be required
	11. git commit
	
	# Push the changes to the server
	12. git push
	
	# In the results of the git push commands, the server will 
	# provide the password for the next level.
	```

	Smile on my face. I even commented what "git push" or "cat file.txt" were executing! XDDDDDDDD
	
	I also vividly remember spending **A LOT** of time doing this. But you know what? I don't care what my colleagues say. All that time was completely worthwhile because it helped me integrate that knowledge into my tired brain. Take, for instance, [the walkthrough of vulnhub Goldeneye 1](vulnhub-goldeneye-1.md). It took me a while to format and prepare it for sharing (and I did it with the intention of sharing).
		
	Now things have changed. **I don't do that anymore. I've become selfish. My walkthroughs have transformed into a list of steps linked to tools, tags and concise explanations, solely for the purpose of helping me remember that machine**. They are probably only useful to me (not suitable for LinkedIn hahaha). 
	
	Anyway, at some point, I needed to make this decision. More labs and self-centered documentation? Or more detailed walkthroughs and fewer labs (and consequently falling behind on my goals)? More labs, geee!
	
	All of this is just to say that in this repository, you will find incredibly detailed walkthroughs (even with multiple ways of exploiting a machine) along with quick guides containing raw commands. All of them together and for no reason. Please, bear with me!


## Updated list of walkthroughs - writeups

-   [Vulnhub GoldenEye 1](https://amandaguglieri.github.io/hackinglife/vulnhub-goldeneye-1/)
-   [Vulnhub Raven 1](https://amandaguglieri.github.io/hackinglife/vulnhub-raven-1/)
-   [Vulnhub Raven 2](https://amandaguglieri.github.io/hackinglife/vulnhub-raven-2/)
-   [HTB appointment](https://amandaguglieri.github.io/hackinglife/htb-appointment/)
-   [HTB archetype](https://amandaguglieri.github.io/hackinglife/htb-archetype/)
-   [HTB base](https://amandaguglieri.github.io/hackinglife/htb-base/)
-   [HTB crocodile](https://amandaguglieri.github.io/hackinglife/htb-crocodile/)
-   [HTB explosion](https://amandaguglieri.github.io/hackinglife/htb-explosion/)
-   [HTB friendzone](https://amandaguglieri.github.io/hackinglife/htb-friendzone/)
-   [HTB funnel](https://amandaguglieri.github.io/hackinglife/htb-funnel/)
-   [HTB included](https://amandaguglieri.github.io/hackinglife/htb-included/)
-   [HTB ignition](https://amandaguglieri.github.io/hackinglife/htb-ignition/)
-   [HTB lame](https://amandaguglieri.github.io/hackinglife/htb-lame/)
-   [HTB markup](https://amandaguglieri.github.io/hackinglife/htb-markup/)
-   [HTB metatwo](https://amandaguglieri.github.io/hackinglife/htb-metatwo/)
-   [HTB mongod](https://amandaguglieri.github.io/hackinglife/htb-mongod/)
-  [HTB nibbles](htb-nibbles.md)
- [HTB nunchucks](htb-nunchucks.md)
-   [HTB oopsie](https://amandaguglieri.github.io/hackinglife/htb-oopsie/)
-   [HTB pennyworth](https://amandaguglieri.github.io/hackinglife/htb-pennyworth/)
-   [HTB photobomb](https://amandaguglieri.github.io/hackinglife/htb-photobomb/)
-   [HTB redeemer](https://amandaguglieri.github.io/hackinglife/htb-redeemer/)
-   [HTB responder](https://amandaguglieri.github.io/hackinglife/htb-responder/)
-   [HTB sequel](https://amandaguglieri.github.io/hackinglife/htb-sequel/)
-   [HTB support](https://amandaguglieri.github.io/hackinglife/htb-support/)
-   [HTB tactics](https://amandaguglieri.github.io/hackinglife/htb-tactics/)
-   [HTB trick](https://amandaguglieri.github.io/hackinglife/htb-trick/)
-   [HTB unified](https://amandaguglieri.github.io/hackinglife/htb-unified/)
-   [HTB vaccine](https://amandaguglieri.github.io/hackinglife/htb-vaccine/)


