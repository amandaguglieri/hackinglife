---
title: Virtualbox and Extension Pack
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - bypass techniques
---

# VirtualBox and Extension Pack

How to install the Extension Pack manually, bypassing possible policies existing in a Windows DC.

1. The .vbox-extpack file that can be downloaded. Actually, it is just a .tar.gz archive so its contents can be unpacked. 
2. Place these contents in subdirectory ExtensionPacks of the VirtualBox installation directory, tipically C:\Program Files\Oracle\VirtualBox
3. That's it. Run Virtualbox and click on Install extension in the corresponding section. Installation now will be successful. 


## How to Enlarge a Virtual Machine’s Disk in VirtualBox 

In VirtualBox, go to File > Virtual Media Manager and use the slider to adjust the disk size. In VMWare, right-click your virtual machine (VM), then go to Settings > Hard Disk > Expand, and expand the disk. Finally, boot your VM and expand the partition using GParted on Linux or Disk Management on Windows.


## VirtualBox Troubleshooting Guide (Memory Ballooning Issue)

**1. Check VirtualBox Memory Settings**

```bash
VBoxManage showvminfo "VM_NAME" | grep -i memory
```

 **Ensure `Configured memory balloon` is set to `0MB`.**

---

**2. Disable Memory Ballooning**

**Using VBoxManage**

```bash
VBoxManage modifyvm "VM_NAME" --guest-memory-balloon 0
```

Then verify:

```bash
VBoxManage showvminfo "VM_NAME" | grep -i memory
```

**Using VirtualBox GUI**
1. Open **VirtualBox**.
2. Select your VM.
3. Click **Settings → System**.
4. Disable **Memory Ballooning** or set it to **0 MB**.
5. Click **OK** and restart the VM.

---

**3. Restart VirtualBox Kernel Modules**

```bash
sudo systemctl restart vboxdrv
```

If the above fails, manually remove and reload the modules:

```bash
sudo modprobe -r vboxdrv vboxnetflt vboxnetadp
sudo modprobe vboxdrv
```

---

**4. Kill Stuck VirtualBox Processes**

```bash
ps aux | grep -i vbox
```

Kill any **stuck processes**:

```bash
sudo kill -9 <PID>
```

---

**5. Restart VirtualBox Service**

```bash
sudo systemctl restart vboxdrv
```

---

**6. Start the VM Again**

```bash
VBoxManage startvm "VM_NAME"
```

---

**7. Check for Secure Boot Issues**ç

If **kernel modules fail to load**, check Secure Boot status:

```bash
mokutil --sb-state
```

If **Secure Boot is enabled**, disable it from BIOS.

---

**8. Check VirtualBox Version & Dependencies**

If VirtualBox still has issues, reinstall it properly:

```bash
VBoxManage --version
```

Ensure necessary dependencies are installed:

```bash
sudo apt install -y linux-headers-$(uname -r) dkms
```

If `vboxdrv` fails to load:

```bash
sudo /sbin/vboxconfig
```

---

**Final Notes**
- The **main fix** is setting `--guest-memory-balloon 0` or disabling it in the GUI.
- Ensure **VirtualBox modules are loaded** (`lsmod | grep vbox`).
- If VirtualBox **keeps freezing**, try removing and reinstalling it:

  ```bash
  sudo apt remove --purge virtualbox
  sudo apt install virtualbox
  ```
  
- If all else fails, **reboot** after applying these changes:

  ```bash
  sudo reboot
  ```

---
