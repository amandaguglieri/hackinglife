---
title: Authentication workflows
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
---

# Authentication workflows

Reference notes on how the common authentication protocols actually work on the wire — the message flow, where the secrets live, why each one is weak, and how it maps to offensive and defensive techniques elsewhere in these notes.

Each page is written as **theory first, then pentesting**, so it works both as a refresher and as a field reference during an engagement.

## Workflows

- [**NTLM**](ntlm) — challenge–response suite (LM / NTLMv1 / NTLMv2), NT hash vs NetNTLM, capture, cracking, Pass-the-Hash and relay.

