---
title: Frida - A dynamic instrumentation toolkit 
author: amandaguglieri
draft: false
TableOfContents: true
tag: mobile pentesting
---

# Frida - A dynamic instrumentation toolkit

Dynamic instrumentation toolkit for developers, reverse-engineers, and security researchers.  It lets you inject snippets of JavaScript or your own library into native apps on Windows, macOS, GNU/Linux, iOS, watchOS, tvOS, Android, FreeBSD, and QNX. Frida also provides you with some simple tools built on top of the Frida API. These can be used as-is, tweaked to your needs, or serve as examples of how to use the API. [More](https://frida.re/docs/home/).


## Installation and set up

Download it:

```bash
pip install frida-tools
pip install frida
wget https://github.com/frida/frida/releases/download/15.1.14/frida-server-15.1.14-android-x86.xz
```

Unzip the file with extension xz:

```bash
unxz frida-server-15.1.14-android-x86.xz
```

Make sure we're connected to the device:

```bash
adb connect 192.168.156.103:5555
```

Upload frida file to the device:

```bash
adb push frida-server-15.1.14-android-x86 /data/local/tmp/frida-server
```

We go to the path where we have stored the file:

```bash
adb shell
cd /data/local/temp
```

We list contents, see frida-server file, and we change permissions:

```bash
ls -la
chmod 777 frida-server
```

Now we can run the binary:

```bash
./frida-server
```

From another terminal we can see processes running on the device:

```bash
frida-ps U
```

## Install Burp Certificate in Frida

Our goal is to install it at: /system/etc/security/cacerts. Here we can find stored Authority certificates and it 's the place where we will install Burp certificate.

First, we open Burp > Proxy > Options > Proxy Listener and we click on "Import / Export CA Certificate". We save it in DER format to a folder accessible from kali. We can give it the name: cacert.der.

Second, we convert der format to pem:

```bash
openssl x509 -inform DER -in cacert.der -out cacert.pem
```

Now, we extract the hash that we will use later on to name the certificate.

```bash
openssl x509 -inform PEM -subject_hash_old -in cacert.pem | head -1
```

It returns (for instance): 9a5ba575.

Let's change the name to cacert.pem:

```bash
mv cacert.pem 9a5ba575.0
```

To act as root we'll run:

```bash
adb root
```

And to mount again the units:

```bash
adb remount
```

Netx step will be to upload the certificate 9a5ba575.0 to the SD Card:

```bash
adb push 9a5ba575.0 /sdcard/
```

Let's go to that directory and move the file to our preferred location:

```bash
adb shell
cd /sdcard
ls -la
mv 9a5ba575.0 /system/etc/security/cacerts
```

Change permissions to the file:

```bash
chmod 644 /system/etc/security/cacerts/9a5ba575.0

In Burp now we need a Proxy Listener. We will indicate the Host-Only IP that we have in our kali. For instance: 192.168.156.107. Port: 8080.

And in the wifi settings of the virtual device running on GenyMotion (for instance a Galaxy6), we need to indicate this same IP on Host-Only mode from our kali.

## Basic commands
 
```
# Display active processes, and installed
frida-ps -Ua


# Restaurate class loaders
Java.perform(function() {
	var application = Java.use("android.com.application");
	var classloader;
	application.attach.overload('android.content.Context').implementation = function(context) {
		var result = this.attach(context);
		classloader = context.getClassLoader();
		Java.classFactory.loader = classloader;
	return result;
	}
})

# Enumerate classes loaded in memory
Java.perform(function() {
	Java.enumerateLoadedClasses
	({
		"onMatch": function(className) {
			console.log(className)
			},
		"onComplete": function(){]
	})
})

# Enumerate classes loaded in memory linked to a specific <package>
Java.enumerateLoadedClasses
({
	"onMatch": function(className) {
		if(className.includes("<package>")) {
			console.log(className);
		}
	},
	"onComplete": function(){]
});

# Android version installed on device
Java.androidVersion

# Execute a method of an Activity
Java.choose("<Name and path of the activity>"), {
	onMatch: function(instance) {
	// This function will be called for every instance found by frida console.log (Found instance: "+ instance).
		instace.<Method name>/<function()>;
	},
	onComplete: function(){}
});

# Save an Activity in a variable
var NameofVariable = Java.use(com.android.application.<nameOfActivity>); 

# Execute a script js from Frida
frida -U com.android.applicationName -l instance.js

# Modify the implementation of a function
var activity = Java.use(com.droidhem.basketball.adapters.Game);
activity.normalshoot.implementation = function(x,y){
	//print the original arguments
	console.log("Dentro de normalshoot");
	this.score.value += 10000;
	// in the original code:
	// this.score += 2;
}




