---
title: Remove bloatware from android phones
author: amandaguglieri
draft: false
TableOfContents: true
---

# Remove bloatware from android phones

[Android Debug Bridge - adb cheat sheet](android-debug-bridge.md).

First of all, make sure you have enabled Developer mode in your mobile. Afterward, enable "USB Debug mode" (Depuración USB in spanish). 
 
**1.** Connect mobile to computer with USB cable. 

**2.** Press "File Transfer" in mobile.

**3.** In laptop, open a terminal and run:

```bash
# Check if device is connected. 
adb devices
```

**4.** If device is well connected, mobile will be prompted to accept the computer connection.

**5.** Access the device from terminal:

```bash
adb shell
```

Now you can uninstall packages.

## Basic commands

```bash
# Uninstall app
pm uninstall --user 0 app.package.name

# Deactivate app
pm disable-user app.package.name
```


## List of xiaomi trash

-   **com.miui.analytics**: analytic  de analítica de Xiaomi.
-   **com.xiaomi.mipicks**:  apps store. Occasionaly it displays adds.
-   **com.miui.msa.global**: servicio de anuncios y publicidad de MIUI.
-   **com.miui.cloudservice | com.miui.cloudservice.sysbase | com.miui.newmidrive**: herramientas de Mi Cloud.
-   **com.miui.cloudbackup**: herramienta de copia de seguridad en la nube Mi Cloud Backup.
-   **com.miui.backup**: herramienta de copias de seguridad de MIUI.
-   **com.xiaomi.glgm**: herramienta de juegos de Xiaomi.
-   **comn.xiaomi.payment | com.mipay.wallet.in:** herramientas de pagos móviles de Xiaomi.
-   **com.tencent.soter.soterserver**: función de pagos móviles a través de WeChat y otros servicios populares en China.
-   **cn.wps.xiaomi.abroad.lite**: Mi DocViewer, herramienta de visualización de documentos PDF.
-   **com.miui.videoplayer**: reproductor Mi Video.
-   **com.miui.player**: reproductor Mi Music.
-   **com.mi.globalbrowser**: navegador Mi Browser.
-   **com.mi.midrop**: herramienta ShareMe para compartir archivos con otros dispositivos Xiaomi.
-   **com.miui.yellowpage**: Mi YellowPages, sistema de protección anti-spam telefónico.
-   **com.miui.android.fashiongallery**: carrusel de fondos de pantalla.
-   **com.miui.bugreport | com.miui.miservice**: herramientas para reportar fallos de MIUI.
-   **com.miui.weathe2**: app del tiempo de Xiaomi.
-   **com.xiaomi.joyose**: herramientas de analítica y publicidad.
-   **com.zhiliaoapp.musically**: TikTok
-   **com.facebook.katana**: app de Facebook.
-   **com.facebook.services**: servicios de Facebook.
-   **com.facebook.system:** instalador de apps de Facebook.
-   **com.facebook.appmanager**: gestor de aplicaciones de Facebook.
-   **com.ebay.mobile | com.ebay.carrier**: app de eBay
-   **com.alibaba.aliexpresshd**: app de AliExpress.



More suggestion to remove bloatware from this repo: [**xiaomi_debloat.sh**](https://gist.github.com/ayZagen/d0e2250577904a54376e9baef008997e#file-xiaomi_debloat-sh)

```
pm uninstall --user 0 com.android.inputmethod.latin
pm uninstall --user 0 com.android.camera2
pm uninstall --user 0 com.android.providers.partnerbookmarks
pm uninstall --user 0 com.android.emergency
pm uninstall --user 0 com.android.printspooler
pm uninstall --user 0 com.android.apps.tag
pm uninstall --user 0 com.android.dreams.basic
pm uninstall --user 0 com.android.dreams.phototable
pm uninstall --user 0 com.android.magicsmoke
pm uninstall --user 0 com.android.managedprovisioning
pm uninstall --user 0 com.android.noisefield
pm uninstall --user 0 com.android.phasebeam
pm uninstall --user 0 com.android.wallpaper.holospiral
pm uninstall --user 0 com.android.stk
pm uninstall --user 0 com.android.bluetoothmidiservice
pm uninstall --user 0 com.android.browser
pm uninstall --user 0 com.android.cellbroadcastreciever
pm uninstall --user 0 com.android.hotwordenrollment.okgoogle
pm uninstall --user 0 com.android.printservice.recommendation
pm uninstall --user 0 com.android.quicksearchbox
pm uninstall --user 0 com.android.email
pm uninstall --user 0 com.android.bips
pm uninstall --user 0 com.android.hotwordenrollment.xgoogle
pm uninstall --user 0 com.android.chrome
pm uninstall --user 0 com.android.webview
pm uninstall --user 0 com.android.calendar
pm uninstall --user 0 com.android.providers.calendar
pm uninstall --user 0 android.romstats
pm uninstall --user 0 com.android.documentsui
pm uninstall --user 0 com.android.globalFileexplorer
pm uninstall --user 0 com.android.midrive
pm uninstall --user 0 com.android.calculator2
pm uninstall --user 0 com.android.soundrecorder
pm uninstall --user 0 com.android.musicfx
pm uninstall --user 0 com.android.bookmarkprovider
pm uninstall --user 0 com.android.gallery3d
pm uninstall --user 0 com.android.calllogbackup
pm uninstall --user 0 com.android.traceur
pm uninstall --user 0 com.sec.android.AutoPreconfig
pm uninstall --user 0 com.sec.android.service.health


# Google apps:
pm uninstall --user 0 com.google.android.tts
pm uninstall --user 0 com.google.android.apps.googleassistant
pm uninstall --user 0 com.google.android.apps.setupwizard.searchselector
pm uninstall --user 0 com.google.android.pixel.setupwizard
pm uninstall --user 0 com.google.android.gm
pm uninstall --user 0 com.google.android.calendar
pm uninstall --user 0 com.google.android.calculator
pm uninstall --user 0 com.google.android.apps.recorder
pm uninstall --user 0 com.google.android.printservice.recommendation
pm uninstall --user 0 com.google.android.apps.books
pm uninstall --user 0 com.google.android.apps.cloudprint
pm uninstall --user 0 com.google.android.apps.currents
pm uninstall --user 0 com.google.android.apps.fitness
pm uninstall --user 0 com.google.android.apps.photos
pm uninstall --user 0 com.google.android.apps.plus
pm uninstall --user 0 com.google.android.apps.tachyon
pm uninstall --user 0 com.google.android.music
pm uninstall --user 0 com.google.android.apps.wellbeing
pm uninstall --user 0 com.google.android.email
pm uninstall --user 0 com.google.android.googlequicksearchbox
pm uninstall --user 0 com.google.android.talk
pm uninstall --user 0 com.google.android.syncadapters.contacts
pm uninstall --user 0 com.google.android.videos
pm uninstall --user 0 com.google.tango.measure
pm uninstall --user 0 com.google.android.youtube
pm uninstall --user 0 com.google.android.apps.docs
pm uninstall --user 0 com.google.ar.lens
pm uninstall --user 0 com.google.android.apps.restore
pm uninstall --user 0 com.google.android.soundpicker
pm uninstall --user 0 com.google.android.syncadapters.calendar
pm uninstall --user 0 com.google.ar.core
pm uninstall --user 0 com.google.android.setupwizard
pm uninstall --user 0 com.google.android.apps.wallpaper
pm uninstall --user 0 com.google.android.projection.gearhead
pm uninstall --user 0 com.google.android.marvin.talkback
pm uninstall --user 0 com.google.android.inputmethod.latin


#Xiaomi/MIUI/Baidu stuff:

pm uninstall --user 0 com.mi.health
pm uninstall --user 0 com.miui.zman
pm uninstall --user 0 com.miui.freeform
pm uninstall --user 0 com.miui.miwallpaper.earth
pm uninstall --user 0 com.miui.miwallpaper.mars
pm uninstall --user 0 com.miui.newmidrive
pm uninstall --user 0 cn.wps.xiaomi.abroad.lite
pm uninstall --user 0 com.miui.miservice
pm uninstall --user 0 com.xiaomi.mi_connect_service
pm uninstall --user 0 com.xiaomi.miplay_client
pm uninstall --user 0 com.miui.mishare.connectivity
pm uninstall --user 0 com.miui.huanji
pm uninstall --user 0 com.miui.misound
pm uninstall --user 0 com.xiaomi.mirecycle
pm uninstall --user 0 com.miui.cloudbackup
pm uninstall --user 0 com.miui.backup
pm uninstall --user 0 com.mfashiongallery.emag
pm uninstall --user 0 com.miui.accessibility
pm uninstall --user 0 com.xiaomi.account
pm uninstall --user 0 com.xiaomi.xmsf
pm uninstall --user 0 com.xiaomi.simactivate.service
pm uninstall --user 0 com.miui.daemon
pm uninstall --user 0 com.miui.cloudservice.sysbase
pm uninstall --user 0 com.mi.webkit.core
pm uninstall --user 0 com.sohu.inputmethod.sogou.xiaomi
pm uninstall --user 0 com.miui.notes
pm uninstall --user 0 com.bsp.catchlog
pm uninstall --user 0 com.miui.vsimcore
pm uninstall --user 0 com.xiaomi.scanner
pm uninstall --user 0 com.miui.greenguard
pm uninstall --user 0 com.miui.android.fashiongallery
pm uninstall --user 0 com.miui.cloudservice
pm uninstall --user 0 com.miui.micloudsync
pm uninstall --user 0 com.miui.enbbs
pm uninstall --user 0 com.mi.android.globalpersonalassistant
pm uninstall --user 0 com.mi.globalTrendNews
pm uninstall --user 0 com.milink.service
pm uninstall --user 0 com.mipay.wallet.id
pm uninstall --user 0 com.mipay.wallet.in
pm uninstall --user 0 com.miui.analytics
pm uninstall --user 0 com.miui.bugreport
pm uninstall --user 0 com.miui.cleanmaster
pm uninstall --user 0 com.miui.hybrid.accessory
pm uninstall --user 0 com.miui.miwallpaper
pm uninstall --user 0 com.miui.msa.global
pm uninstall --user 0 com.miui.touchassistant
pm uninstall --user 0 com.miui.translation.kingsoft
pm uninstall --user 0 com.miui.translation.xmcloud
pm uninstall --user 0 com.miui.translation.youdao
pm uninstall --user 0 com.miui.translationservice
pm uninstall --user 0 com.miui.userguide
pm uninstall --user 0 com.miui.virtualsim
pm uninstall --user 0 com.miui.yellowpage
pm uninstall --user 0 com.miui.videoplayer
pm uninstall --user 0 com.miui.weather2
pm uninstall --user 0 com.miui.player
pm uninstall --user 0 com.miui.screenrecorder
pm uninstall --user 0 com.miui.providers.weather
pm uninstall --user 0 com.miui.compass
pm uninstall --user 0 com.miui.calculator
pm uninstall --user 0 com.xiaomi.vipaccount
pm uninstall --user 0 com.xiaomi.channel
pm uninstall --user 0 com.mipay.wallet
pm uninstall --user 0 com.xiaomi.pass
pm uninstall --user 0 com.xiaomi.shop
pm uninstall --user 0 com.xiaomi.joyose
pm uninstall --user 0 com.xiaomi.providers.appindex
pm uninstall --user 0 com.miui.fm
pm uninstall --user 0 com.mi.liveassistant
pm uninstall --user 0 com.xiaomi.gamecenter.sdk.service
pm uninstall --user 0 com.xiaomi.payment
pm uninstall --user 0 com.baidu.input_mi
pm uninstall --user 0 com.xiaomi.ab
pm uninstall --user 0 com.xiaomi.jr
pm uninstall --user 0 com.baidu.duersdk.opensdk
pm uninstall --user 0 com.miui.hybrid
pm uninstall --user 0 com.baidu.searchbox
pm uninstall --user 0 com.xiaomi.glgm
pm uninstall --user 0 com.xiaomi.midrop
pm uninstall --user 0 com.xiaomi.mipicks
pm uninstall --user 0 com.miui.personalassistant
pm uninstall --user 0 com.miui.audioeffect
pm uninstall --user 0 com.miui.cit
pm uninstall --user 0 com.miui.qr
pm uninstall --user 0 com.miui.nextpay
pm uninstall --user 0 com.xiaomi.o2o


#Xiaomi.eu:
pm uninstall --user 0 pl.zdunex25.updater


#RevolutionOS: (not well tested)
pm uninstall --user 0 ros.ota.updater

#SyberiaOS: (not well tested)
pm uninstall --user 0 com.syberia.ota
pm uninstall --user 0 com.syberia.SyberiaPapers


#LineageOS: (not well tested)
pm uninstall --user 0 org.lineageos.recorder
pm uninstall --user 0 org.lineageos.snap


#Paranoid Android:
pm uninstall --user 0 com.hampusolsson.abstruct
pm uninstall --user 0 code.name.monkey.retromusic

#Other stuff:
pm uninstall --user 0 com.autonavi.minimap
pm uninstall --user 0 com.caf.fmradio
pm uninstall --user 0 com.opera.preinstall
pm uninstall --user 0 com.qualcomm.qti.perfdump
pm uninstall --user 0 com.duokan.phone.remotecontroller
pm uninstall --user 0 com.samsung.aasaservice
pm uninstall --user 0 org.simalliance.openmobileapi.service
pm uninstall --user 0 com.duokan.phone.remotecontroller.peel.plugin
pm uninstall --user 0 com.facemoji.lite.xiaomi
pm uninstall --user 0 com.facebook.appmanager
pm uninstall --user 0 com.facebook.katana
pm uninstall --user 0 com.facebook.services
pm uninstall --user 0 com.facebook.system
pm uninstall --user 0 com.netflix.partner.activation


# !EXPERIMENTAL STUFF!


#GPS & Location debloat
#Uninstalling these may break apps like Waze.
#You have been warned.
pm uninstall --user 0 com.android.location.fused
pm uninstall --user 0 org.codeaurora.gps.gpslogsave
pm uninstall --user 0 com.google.android.gms.location.history
pm uninstall --user 0 com.qualcomm.location
pm uninstall --user 0 com.xiaomi.bsp.gps.nps
pm uninstall --user 0 com.xiaomi.location.fused


#Use this if you don't like the stock MIUI launcher.
#Uninstalling this without basic setup and an alternative launcher will make the device unstable or softbricked.
#You can't downgrade to a lower version of MIUI launcher after uninstalling this.
#You have been warned.
pm uninstall --user 0 com.miui.home


#Always-on Display removal
#Not recommended, and not well-tested in daily usage
#You have been warned.
pm uninstall --user 0 com.miui.aod
```



# Workshop in Android


Getting the .apk as the first step to to the static analysis. 
After launching the app, run again some checks on the possible folders created locally in your device.

We will follow the OWASP MAS methodology: MASVS MASWE MASTG
Mobile application Security List would be ours: mass.owasp.org and specially: https://mas.owasp.org/MASTG/

MASTG is the guide for mobile pentesting, similar to the WSTG, with tools, techniques...


Backmarket for buying stuff to testing 

Solutions for emulation: ADV from Android Studio, Genymotion (version free and  paid one), Android Corellium (paid). 

Tools: Android Studio, Magisk, adb. MobSF, BurpSuite, Frida, APKTool, JADX, Drozer, and Objection.


## Lab

Follow the setup guide. 

Attention in Frida installation. We need to take into account the target architecture. Also we need to have same Frida version in the mobile and in the laptop.

**Low Hanging Fruits**
- Permissions of the Application: do they make sense?
- How is the data protected? What is the nature of that data (creds, sensible data...) Is HTTP is place or HTTPS? Other protocols...
- Sandboxes? Can you access other apps from yours?
- Update and patches

Basic checklist (see document from zip)


**Application formats**

- APK
- Split APKs (it's like the apk but segmented in different packages): ready for uploading to stores.
- App bundle (AAB)



Cheat sheet

Enable Deb tools in mobile by clicking 7 times on the About the device option

```bash
# Check devices and connectivity
adb devices

# Connect
adb connect 10.0.2.2

# Enter the shell
adb shell 


# Install an apk
adb install app.apk

# reinstall but keeping data
adb install -r aap.apk 

# Install the splitted format of an apk
adb install-multiple base.apk split_config.arm64_v8a.apk split_config.xxhdpi.apk
```

Starting the lab

```
# Show installed packages in mobile
adb shell pm list packages

# What is the name of the packeage of your application
adb instalñ AndroGoat.apk

# Where is it installed
adb shell pm path owasp.sat.agoat
# it returns a path

# We can download the package to our kali
adb pull <paht of the package>

```

From code to  apk: (slide 38)

Anatomy of an apk:
- AndroidManifest.xml
- classes.dex
- assets/
- lib/
- ....
- (slide 39)


great resource for understanding the basic and it's free, in slide 40

Reversing tools:

Apktool - > Manifest + Smali + Res
Dex2jar -> classess.dex -> .jar
JD-GUI/JDAX -Z Java

**Hoe to installl apktool:**

Apktools is for compiling and decompiling applicaitons, so cooool

```
sudo apt update
sudo apt install apktool
apktoll d application.apk
```


```
apktool d AndroGoat.apk
```

Version that goes ok, v. 2.7.0, for windows. Other gives problems

After running apktool the app has been decompiled and we can access folders and files. It returns the SMALI. 


**Now, how to convert the classes.dex to java, with JADX.**

Install Jadx-gui (48):

```
sudo apt install default-jdk

sudo apt install jadx

jadx-gui
```

For windows follow the instructions from slide 49.

Now inside the JADX-GUI we can go to the source code of the application,. 

Interesting files:

- Interestingly enough the resources.arsc/res/values/string.xml, which is the equivalent to running a strings command on the app.
- resources.arsc/res/xml/network_security_config.xml It may says if the traffic is plain, configuration of subdomains, certificates...).
- Another interesting thing to do is using the Search. Look for password, admin and similar relevant string for the application.
- The installed apps in a device are located at /data/data. There you may find the folder cache and code_cache. It's worth having a look at. 


**MobsF**

Installing (slide 52 and 53)
It has a part for dynamic analysis, but it requires certain configurations and connections to other tools such as Andoid Studio.  defaul creds: mobsf:monsf


Has the app the debug mode enabled? See in AndroidManisfest.xml-


**Activities**

Pay attention to the exported ones, since they might be accessed from the outside

Have a look at the Firebase and see if the db is accesible 

```
https://exampledomain.firebase.io/.json
```

Tools gap checker github in https://github.com/joanbono/gap


### AndroidManifest analysis
The installed apps in a device are located at /data/data. There you may find the folder cache and code_cache. It's worth having a look at. 

slide 56

### Drozer

Security tool for mobile app. What can you do (slide 57).

install in slide 58

```
pipx install drozer

wget https://pathinSlide59

# once downloaded, check that we are connected to the device with adb and then
adb install drozer

adb forward tcp:31415 tcp:31515
adb drozer connect
> list
> run app.package.info -a <PackageName> 
```

Activities

Activities represent a View in the application. Basically a Screenshot.
It also contains workflows. It's declared in the manisfest

See slide 

```
adb shell dumpsys package PackageName> 
```


After listing the attack surface we may see activities exported, providers and services... 

```
run app.package.attackSurface -a <applicationPackage> 

run app.activity.start <ActivityName> --component <application package> <application package>.<ActivityName>  

```


This way we may start the activity directly (we have not logged yet)- Same thing can be achieve with adb

```
adb shell am start -n <packageName>/.<ActivityviewName>
```

If an activity is exported it can be access by other apps from the mobile.


Next, we have intents, two types: implicit and explicit. An intent may be defined as a way of Android to tell open an screen or execute this component. 61

```
# Syntax
android.intent.<whatever> 
```

**Service exploitation**

slide 70

A service is a functionality that provides a service to the application. Examples: download an invoice, run a player with music...

When it comes to exploitability, we may abuse services to get them executed. If they are exported, another  application within the device may trigger them.

```
run app.service.start --action DownloadInvoice --component owasp.sat.agoat owasp.sat.agoat.DownloadInvoice
```



**Content Providers (slide 73)**

Component that allows the access to data within an application.


**Fragment**

Fragment is part of the activity. It represents a section of the View. Belonging to the Activity, it inherits their vulnerabilities.


**IPC**

IPC is the mechanism that allows inter process - communication among processes and applications.


**Permissions**

(slide 79)

Recap in slide 80


**Deep links exploitation**

```
# adb shell am start -W -a android.intent.action.VIEW -d scheme://host/congrats?expectedParameter=value

adb shell am start -W -a android.intent.action.VIEW -d allsafe://infosecadventures/congrats?key=a
```

**Webview**

Webview is an android component that allows us to display ...


More attacks on different components UP TO  slide 87

### Static analysis

from slide 87




