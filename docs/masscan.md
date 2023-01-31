---
title: masscan - An IP scanner 
author: amandaguglieri
draft: false
TableOfContents: true
tag: reconnaissance,scanning
---

# masscan - An IP scanner

Masscan was designed to deal with large networks and to scan thousands of Ip addresses at once. It’s faster than nmap but probably less accurate.

## Installation

```bash
sudo apt-get install git gcc make libpcap-dev
git clone https://github.com/robertdavidgraham/masscan
cd masscan/
make
```

"make" puts the program in the `masscan/bin` subdirectory. To install it (on Linux) run:

```bash
make install
``` 

The source consists of a lot of small files, so building goes a lot faster by using the multi-threaded build. This requires more than 2gigs on a 
Raspberry Pi (and breaks), so you might use a smaller number, like `-j4` rather than all possible threads.

```bash
make -j
```

Make sure that is running properly:

```bash
cd bin
./masscan --regress
```

## Usage

Usage is similar to `nmap`. To scan a network segment for some ports:

```bash
./masscan -p22,80,443,53,3389,8080,445 -Pn --rate=800 --banners 10.0.2.1/24 -e tcp0 --router-ip 10.0.2.456  --echo >  masscan.conf
# To see the complete list of options, use the `--echo` feature. This dumps the current configuration and exits. This output can be used as input back into the program:
```

Another example:

```bash
masscan -p80,8000-8100 10.0.0.0/8 2603:3001:2d00:da00::/112
# This will scan the `10.x.x.x` subnet, and `2603:3001:2d00:da00::x` subnets
# Scan port 80 and the range 8000 to 8100, or 102 ports total, on both subnets
# Print output to `<stdout>` that can be redirected to a file
```

## Editing config file

```bash
nano masscan.conf
# here, you add:  output-filename = scan.list //also json, xml
```

Now to tun it again using the configuration file: 

```bash
masscan -c masscan.conf
```
