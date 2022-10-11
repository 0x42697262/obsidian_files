> [!INFO]
> Status:
> Tags:  #arch #arch_system_changes

----
# 013 System Changes

## 2022-10-11
Removed `/etc/X11/xorg.conf.d/10-optimus-manager.conf`
```sh
mv 10-optimus-manager.conf 10-optimus-manager.conf.bak
```
This didn't change anything after reboot.
```sh
sudo pacman -Rcns optimus-manager-git
```
## 2022-09-09 
```sh
sudo usermod -aG kvm birb 
```

## 2022-09-08
### XORG DAEMON
```conf
Section "InputClass"
    Identifier "touchpad"
    Driver "libinput"
    MatchIsTouchpad "on"
    Option "Tapping" "on"
    Option "TappingButtonMap" "lmr"
EndSection
```
Created a new file for touchpad. I wanted the touchpad to click like touchscreen.