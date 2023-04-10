---
title: Bypassing IPS with handmade XOR Encryption
author: amandaguglieri
draft: false
TableOfContents: true
---

# Bypassing IPS with handmade XOR Encryption

The idea is to encrypt our traffic to avoid network analyzers or intrusion prevention sensors. SSL os SSH is not recommended here since Next Generation Firewalls have the ability to decrypt them and pass it as plain text to the IPS, where it's recognized.