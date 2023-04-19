---
title: Remove bloatware from android phones
author: amandaguglieri
draft: false
TableOfContents: true
---

# Remove bloatware from android phones

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
-  **com.zhiliaoapp.musically**: TikTok
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

