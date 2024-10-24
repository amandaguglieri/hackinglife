---
title: Depix - A tool for extracting data from pixeled images
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - reconnaissance
  - scanner
---
# Depix - A tool for extracting data from pixeled images

## Installation

```bash
git clone https://github.com/spipm/Depix.git
cd Depix
```

## Basic usage

```bash
python3 depix.py \
    -p images/testimages/sublime_screenshot_pixels_gimp.png \
    -s images/searchimages/debruin_sublime_Linux_small.png \
    --backgroundcolor 40,41,35 \
    --averagetype linear
```