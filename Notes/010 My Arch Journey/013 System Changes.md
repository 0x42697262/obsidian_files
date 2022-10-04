> [!INFO]
> Status:
> Tags:  #arch #arch_system_changes

----
# 013 System Changes
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